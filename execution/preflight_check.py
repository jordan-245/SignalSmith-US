#!/usr/bin/env python3
"""
Pre-flight check: verify all execution scripts can import successfully.
Returns exit code 0 if all checks pass, 1 otherwise.
"""
import sys
import importlib.util
from pathlib import Path

def check_script_imports():
    """Check if key execution scripts can import."""
    scripts = [
        "ingest_docs",
        "ingest_prices", 
        "baseline_pipeline",
        "eod_report",
        "build_features",
    ]
    
    failed = []
    
    for script_name in scripts:
        script_path = Path(f"execution/{script_name}.py")
        if not script_path.exists():
            print(f"⚠️  {script_name}: file not found")
            failed.append(script_name)
            continue
            
        try:
            spec = importlib.util.spec_from_file_location(script_name, script_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[script_name] = module
            spec.loader.exec_module(module)
            print(f"✓ {script_name}: imports OK")
        except Exception as e:
            print(f"✗ {script_name}: {str(e)[:100]}")
            failed.append(script_name)
    
    if failed:
        print(f"\n❌ Failed scripts: {', '.join(failed)}")
        return False
    else:
        print(f"\n✓ All {len(scripts)} scripts checked successfully")
        return True

if __name__ == "__main__":
    success = check_script_imports()
    sys.exit(0 if success else 1)
