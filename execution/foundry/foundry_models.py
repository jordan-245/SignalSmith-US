"""Signal Foundry — Model Stack

Provides:
  - BaselineLogistic: L2-regularised logistic regression
  - TreeModel: LightGBM (preferred) or sklearn GradientBoosting (fallback)
  - EnsembleModel: weighted average of heterogeneous sub-models
  - CalibrationWrapper: Platt scaling or isotonic regression on raw probabilities
  - RegimeClassifier: volatility-regime labeller (low / medium / high)

All models expose a unified .fit(X, y) / .predict_proba(X) interface.
"""

from __future__ import annotations

import logging
import warnings
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, log_loss, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# ---------- LightGBM vs sklearn fallback ----------
try:
    import lightgbm as lgb

    _HAS_LGB = True
except ImportError:
    _HAS_LGB = False

if not _HAS_LGB:
    from sklearn.ensemble import GradientBoostingClassifier

logger = logging.getLogger("foundry.models")

# ────────────────────────────────────────────────────────────────────
# Feature column registry (single source of truth)
# ────────────────────────────────────────────────────────────────────
FEATURE_COLS: List[str] = [
    # Original 9 features
    "ret_1d",
    "ret_5d",
    "ret_20d",
    "vol_20d",
    "ma_ratio_20_50",
    "ma_ratio_50_200",
    "px_gt_sma200",
    "sma50_gt_sma200",
    "rel_strength_20d",
    # Volume features (v2)
    "vol_ratio_20d",
    "dollar_volume_20d",
    "volume_trend_5d",
    # Volatility-adjusted returns (v2)
    "sharpe_5d",
    "sharpe_20d",
    # Mean reversion features (v2)
    "rsi_14",
    "z_score_20d",
    # Cross-sectional rank features (v2)
    # NOTE: rank_rel_strength removed — perfectly correlated (r=1.0) with rank_ret_20d
    "rank_ret_20d",
    "rank_vol_20d",
    # Mean-reversion explicit signals (v3)
    "rsi_14_oversold",
    "mean_revert_5d",
    "mean_revert_20d",
]


# ────────────────────────────────────────────────────────────────────
# 1. Baseline Logistic Regression
# ────────────────────────────────────────────────────────────────────
class BaselineLogistic:
    """L2-regularised logistic regression baseline with StandardScaler.

    Raw returns (~0.01 scale) and binary features (0/1) are mixed,
    so StandardScaler is critical for stable convergence.
    """

    def __init__(self, C: float = 5.0, max_iter: int = 500):
        self.model = Pipeline([
            ("scaler", StandardScaler()),
            ("lr", LogisticRegression(C=C, max_iter=max_iter, solver="lbfgs")),
        ])
        self._fitted = False

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "BaselineLogistic":
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self.model.fit(X, y)
        self._fitted = True
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        """Return P(y=1) as 1-D array."""
        if not self._fitted:
            raise RuntimeError("Model not fitted")
        return self.model.predict_proba(X)[:, 1]

    @property
    def name(self) -> str:
        return "logistic"


# ────────────────────────────────────────────────────────────────────
# 2. Tree Model (LightGBM preferred, sklearn GBT fallback)
# ────────────────────────────────────────────────────────────────────
class TreeModel:
    """LightGBM binary classifier, falling back to sklearn GradientBoosting.

    Early stopping is DISABLED by default — with weak cross-sectional signals,
    early stopping can kill the model at 8 trees. Use fixed n_estimators instead.
    Set use_early_stopping=True to re-enable (e.g. for hyperparameter search).
    """

    def __init__(
        self,
        n_estimators: int = 300,
        max_depth: int = 5,
        learning_rate: float = 0.01,
        subsample: float = 0.7,
        min_child_samples: int = 30,
        reg_lambda: float = 3.0,
        reg_alpha: float = 0.5,
        colsample_bytree: float = 0.6,
        random_state: int = 42,
        use_early_stopping: bool = False,
        early_stopping_rounds: int = 50,
        min_estimators: int = 50,
    ):
        self._params = dict(
            n_estimators=n_estimators,
            max_depth=max_depth,
            learning_rate=learning_rate,
            subsample=subsample,
            min_child_samples=min_child_samples,
            reg_lambda=reg_lambda,
            reg_alpha=reg_alpha,
            colsample_bytree=colsample_bytree,
            random_state=random_state,
        )
        self._use_early_stopping = use_early_stopping
        self._early_stopping_rounds = early_stopping_rounds
        self._min_estimators = min_estimators
        self._fitted = False
        self._use_lgb = _HAS_LGB
        self.model = None

    def fit(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        eval_set: Optional[Tuple[pd.DataFrame, pd.Series]] = None,
    ) -> "TreeModel":
        if self._use_lgb:
            self.model = lgb.LGBMClassifier(
                objective="binary",
                n_estimators=self._params["n_estimators"],
                max_depth=self._params["max_depth"],
                learning_rate=self._params["learning_rate"],
                subsample=self._params["subsample"],
                min_child_samples=self._params["min_child_samples"],
                reg_lambda=self._params["reg_lambda"],
                reg_alpha=self._params.get("reg_alpha", 0.5),
                colsample_bytree=self._params["colsample_bytree"],
                random_state=self._params["random_state"],
                verbosity=-1,
                n_jobs=-1,
            )
            fit_kwargs: Dict = {}
            if eval_set is not None and self._use_early_stopping:
                X_val, y_val = eval_set
                fit_kwargs["eval_set"] = [(X_val, y_val)]
                fit_kwargs["callbacks"] = [lgb.early_stopping(
                    self._early_stopping_rounds, verbose=False
                )]
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.model.fit(X, y, **fit_kwargs)

            # Guard against premature early stopping
            if (self._use_early_stopping
                    and hasattr(self.model, 'best_iteration_')
                    and self.model.best_iteration_ < self._min_estimators):
                logger.warning(
                    "Early stopping at %d trees (min=%d) — retraining without early stopping",
                    self.model.best_iteration_, self._min_estimators,
                )
                self.model = lgb.LGBMClassifier(
                    objective="binary",
                    n_estimators=self._params["n_estimators"],
                    max_depth=self._params["max_depth"],
                    learning_rate=self._params["learning_rate"],
                    subsample=self._params["subsample"],
                    min_child_samples=self._params["min_child_samples"],
                    reg_lambda=self._params["reg_lambda"],
                    reg_alpha=self._params.get("reg_alpha", 0.5),
                    colsample_bytree=self._params["colsample_bytree"],
                    random_state=self._params["random_state"],
                    verbosity=-1,
                    n_jobs=-1,
                )
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    self.model.fit(X, y)
        else:
            self.model = GradientBoostingClassifier(
                n_estimators=self._params["n_estimators"],
                max_depth=self._params["max_depth"],
                learning_rate=self._params["learning_rate"],
                subsample=self._params["subsample"],
                random_state=self._params["random_state"],
            )
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                self.model.fit(X, y)

        self._fitted = True
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("Model not fitted")
        return self.model.predict_proba(X)[:, 1]

    @property
    def name(self) -> str:
        return "lgbm" if self._use_lgb else "gbt_sklearn"


# ────────────────────────────────────────────────────────────────────
# 3. Ensemble Model (weighted average)
# ────────────────────────────────────────────────────────────────────
class EnsembleModel:
    """Weighted average of sub-model probabilities.

    Default weights: equal.  Pass explicit weights dict keyed by model name.
    """

    def __init__(self, models: Optional[List] = None, weights: Optional[Dict[str, float]] = None):
        self.models: List = models or []
        self._weights = weights  # {model.name: weight}
        self._fitted = False

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "EnsembleModel":
        for m in self.models:
            if not getattr(m, "_fitted", False):
                m.fit(X, y)
        self._fitted = True
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("Ensemble not fitted")
        preds = []
        w_list = []
        for m in self.models:
            p = m.predict_proba(X)
            preds.append(p)
            if self._weights and m.name in self._weights:
                w_list.append(self._weights[m.name])
            else:
                w_list.append(1.0)
        w_arr = np.array(w_list, dtype=np.float64)
        w_arr /= w_arr.sum()
        stacked = np.column_stack(preds)  # (n, k)
        return stacked @ w_arr

    @property
    def name(self) -> str:
        return "ensemble"


# ────────────────────────────────────────────────────────────────────
# 4. Probability Calibration
# ────────────────────────────────────────────────────────────────────
class CalibrationWrapper:
    """Post-hoc probability calibration via Platt scaling or isotonic regression.

    Usage:
        cal = CalibrationWrapper(method="isotonic")
        cal.fit(uncalibrated_probs, y_true)
        calibrated = cal.transform(new_probs)
    """

    def __init__(self, method: str = "isotonic"):
        assert method in ("isotonic", "platt", "sigmoid"), f"Unknown method: {method}"
        self.method = method
        self._fitted = False
        self._iso: Optional[IsotonicRegression] = None
        self._platt_a: float = 0.0
        self._platt_b: float = 0.0

    def fit(self, raw_probs: np.ndarray, y_true: np.ndarray) -> "CalibrationWrapper":
        raw_probs = np.asarray(raw_probs, dtype=np.float64)
        y_true = np.asarray(y_true, dtype=np.float64)

        if self.method == "isotonic":
            self._iso = IsotonicRegression(y_min=0.0, y_max=1.0, out_of_bounds="clip")
            self._iso.fit(raw_probs, y_true)
        else:
            # Platt / sigmoid scaling: fit logistic regression on raw probs
            from sklearn.linear_model import LogisticRegression as _LR

            lr = _LR(max_iter=500, solver="lbfgs")
            lr.fit(raw_probs.reshape(-1, 1), y_true)
            self._platt_a = float(lr.coef_[0, 0])
            self._platt_b = float(lr.intercept_[0])

        self._fitted = True
        return self

    def transform(self, raw_probs: np.ndarray) -> np.ndarray:
        if not self._fitted:
            raise RuntimeError("CalibrationWrapper not fitted")
        raw_probs = np.asarray(raw_probs, dtype=np.float64)
        if self.method == "isotonic":
            return self._iso.predict(raw_probs)
        else:
            logit = self._platt_a * raw_probs + self._platt_b
            return 1.0 / (1.0 + np.exp(-logit))

    def brier(self, raw_probs: np.ndarray, y_true: np.ndarray) -> float:
        """Brier score of calibrated output."""
        cal = self.transform(raw_probs)
        return float(brier_score_loss(y_true, cal))


# ────────────────────────────────────────────────────────────────────
# 5. Regime Classifier
# ────────────────────────────────────────────────────────────────────
@dataclass
class RegimeClassifier:
    """Classifies each date into a volatility regime (low / medium / high)
    based on rolling volatility percentiles.

    Parameters
    ----------
    vol_col : str
        Column name of the volatility series (e.g. "vol_20d").
    lookback : int
        Rolling window (trading days) for percentile computation.
    low_pctl : float
        Percentile threshold below which regime = 'low'.
    high_pctl : float
        Percentile threshold above which regime = 'high'.
    """

    vol_col: str = "vol_20d"
    lookback: int = 252  # ~1 year
    low_pctl: float = 33.0
    high_pctl: float = 67.0

    def classify(self, df: pd.DataFrame) -> pd.Series:
        """Return a Series of regime labels ('low', 'medium', 'high')
        aligned with the index of *df*.

        Expects *df* to be sorted by date (per-ticker grouping handled externally).
        """
        vol = df[self.vol_col].astype(float)
        roll_low = vol.rolling(self.lookback, min_periods=60).quantile(self.low_pctl / 100.0)
        roll_high = vol.rolling(self.lookback, min_periods=60).quantile(self.high_pctl / 100.0)

        regime = pd.Series("medium", index=df.index)
        regime[vol <= roll_low] = "low"
        regime[vol >= roll_high] = "high"
        return regime

    def classify_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add a 'regime' column to *df*, computing per ticker if 'ticker' column present."""
        if "ticker" in df.columns:
            parts = []
            for _, grp in df.groupby("ticker"):
                grp = grp.sort_values("date")
                grp = grp.copy()
                grp["regime"] = self.classify(grp)
                parts.append(grp)
            return pd.concat(parts, ignore_index=True)
        else:
            df = df.copy()
            df["regime"] = self.classify(df)
            return df


# ────────────────────────────────────────────────────────────────────
# 6. Convenience: train full model stack for one horizon
# ────────────────────────────────────────────────────────────────────
def optimize_ensemble_weights(
    lr_probs: np.ndarray,
    tree_probs: np.ndarray,
    y_true: np.ndarray,
) -> Tuple[float, float]:
    """Find optimal ensemble weights via grid search on calibration set.

    Searches LR weights in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0] and picks
    the pair that maximises AUC-ROC on the calibration set.
    """
    best_auc = 0.0
    best_weights = (0.2, 0.8)  # default fallback
    for w_lr in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        w_tree = 1.0 - w_lr
        ens = w_lr * lr_probs + w_tree * tree_probs
        try:
            auc_val = roc_auc_score(y_true, ens)
            if auc_val > best_auc:
                best_auc = auc_val
                best_weights = (w_lr, w_tree)
        except ValueError:
            pass
    return best_weights


def train_model_stack(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    X_calib: pd.DataFrame,
    y_calib: pd.Series,
    lr_weight: float = 0.2,
    tree_weight: float = 0.8,
    calib_method: str = "isotonic",
    optimize_weights: bool = True,
) -> Tuple["EnsembleModel", "CalibrationWrapper", Dict]:
    """Train baseline + tree, build ensemble, calibrate on held-out set.

    Returns (ensemble, calibrator, diagnostics_dict).

    Diagnostics include ``val_auc`` and ``calibration_error`` keys so that
    ``check_quality_gates_extended()`` in *foundry_run.py* can use them.

    When *optimize_weights* is True (now default), the ensemble weights are
    learned from the calibration set via grid search over LR/tree weight pairs.

    Early stopping is disabled by default to prevent the LightGBM model from
    stopping at very few trees when the signal is weak. The model uses a
    lower learning rate (0.01) with more trees (300) instead.
    """
    lr = BaselineLogistic()
    tree = TreeModel()

    lr.fit(X_train, y_train)
    # No early stopping by default — fixed n_estimators with low learning rate
    tree.fit(X_train, y_train)

    # Always optimize ensemble weights from calibration data
    if optimize_weights:
        lr_calib_probs = lr.predict_proba(X_calib)
        tree_calib_probs = tree.predict_proba(X_calib)
        lr_weight, tree_weight = optimize_ensemble_weights(
            lr_calib_probs, tree_calib_probs, y_calib.values
        )
        logger.info("Learned ensemble weights: LR=%.1f, Tree=%.1f", lr_weight, tree_weight)

    ens = EnsembleModel(models=[lr, tree], weights={lr.name: lr_weight, tree.name: tree_weight})
    ens._fitted = True  # sub-models already fitted

    # Calibrate on held-out calibration set
    raw_calib = ens.predict_proba(X_calib)
    cal = CalibrationWrapper(method=calib_method)
    cal.fit(raw_calib, y_calib.values)

    # Diagnostics
    brier_uncal = float(brier_score_loss(y_calib, raw_calib))
    brier_cal = cal.brier(raw_calib, y_calib.values)
    calibrated_probs = cal.transform(raw_calib)

    # AUC on calibration set — use raw (uncalibrated) probabilities to avoid
    # inflated in-sample AUC from isotonic regression fitted on the same data.
    try:
        val_auc = float(roc_auc_score(y_calib, raw_calib))
    except ValueError:
        val_auc = None

    # Expected Calibration Error (ECE)
    n_bins = 10
    bin_edges = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    total = len(y_calib)
    if total > 0:
        y_arr = np.asarray(y_calib, dtype=np.float64)
        for i in range(n_bins):
            mask = (calibrated_probs >= bin_edges[i]) & (calibrated_probs < bin_edges[i + 1])
            if mask.sum() > 0:
                bin_acc = float(y_arr[mask].mean())
                bin_conf = float(calibrated_probs[mask].mean())
                ece += abs(bin_acc - bin_conf) * mask.sum() / total

    diag: Dict = {
        "brier_uncal": brier_uncal,
        "brier_cal": brier_cal,
        "val_auc": val_auc,
        "calibration_error": round(ece, 6),
        "calib_method": calib_method,
        "lr_weight": lr_weight,
        "tree_weight": tree_weight,
        "tree_backend": tree.name,
        "train_rows": len(X_train),
        "calib_rows": len(X_calib),
    }

    return ens, cal, diag
