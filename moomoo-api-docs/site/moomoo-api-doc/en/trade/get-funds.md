



# <a href="#8" class="header-anchor">#</a> Get Account Funds









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`accinfo_query(trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, refresh_cache=False, currency=Currency.HKD)`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th style="text-align: left;">Parameter</th>
  <th style="text-align: left;">Type</th>
  <th style="text-align: left;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="text-align: left;">trd_env</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
  <td style="text-align: left;">Trading environment</td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_id</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Trading account ID.
  
    
  
  
   
  
  <ul>
  <li>When acc_id is 0, the account specified by acc_index is chosen.</li>
  <li>When acc_id is set the ID number (not 0), the account specified by
  acc_id is chosen.</li>
  <li>Using acc_id to query and trade is strongly recommended, acc_index
  will change when adding/closing an account, result in the account you
  specify is inconsistent with the actual trading account.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_index</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The account number in the trading account
  list.
  
    
  
  
   
  
  The default is 0, which means the first trading account.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">refresh_cache</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to refresh the cache.
  
    
  
  
   
  
  <ul>
  <li>True: Re-request data from the Futu server immediately, without
  using the OpenD cache. At this time, it will be restricted by the
  interface frequency limit.</li>
  <li>False: Use OpenD's cache (The cache needs to be refreshed if it is
  not updated in rare circumstances.)</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">currency</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
  <td style="text-align: left;">The display currency of the funds.
  
    
  
  
   
  
  <ul>
  <li>Only applicable to universal securities accounts and futures
  accounts, other single-market accounts will ignore this parameter.</li>
  <li>In the returned DataFrame, all fund-related fields can be converted
  with this parameter, except for the fields that explicitly specify the
  currency.</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

<!-- -->

- **Return**

  <table>
  <thead>
  <tr>
  <th>Field</th>
  <th>Type</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>ret</td>
  <td><a href="../ftapi/common.html#8800">RET_CODE</a></td>
  <td>Interface result.</td>
  </tr>
  <tr>
  <td rowspan="2">data</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, fund data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Fund data format as follows:
    <table>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Field</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;">power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Maximum Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the <em>approximate value</em> calculated according to
    the marginable initial margin of 50%. But in fact, this ratio of each
    financial contract is not the same. We recommend using <em><strong>Buy
    on margin</strong></em>, returned by <a
    href="/moomoo-api-doc/en/trade/get-max-trd-qtys.html">Query the Maximum
    Quantity that Can be Bought or Sold</a>, to get the maximum quantity can
    buy.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_power_short</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the <em>approximate value</em> calculated according to
    the shortable initial margin of 60%. But in fact, this ratio of each
    financial contract is not the same. We recommend using <em><strong>Short
    sell</strong></em>, returned by <a
    href="/moomoo-api-doc/en/trade/get-max-trd-qtys.html">Query the Maximum
    Quantity that Can be Bought or Sold</a>, to get the maximum quantity can
    be shorted.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Cash Buying Power.
    
      
    
    
     
    
    Obsolete. Please use 'us_net_cash_power' or other fields to get the cash
    buying power of each currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">total_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total Net Assets.
    
      
    
    
     
    
    Total Net Assets = Security Assets + Fund Assets + Bond Assets
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">securities_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Security Assets
    
      
    
    
     
    
    Minimum OpenD version requirements: 8.2.4218.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">fund_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Fund Assets
    
      
    
    
     
    
    <ul>
    <li>Universal accounts will return the total fund assets value.
    Currently, it does not support for HKD fund and USD fund assets
    value.</li>
    <li>Minimum OpenD version requirements: 8.2.4218.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">bond_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bond Assets
    
      
    
    
     
    
    Minimum OpenD version requirements: 8.2.4218.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Cash.
    
      
    
    
     
    
    Obsolete. Please use 'us_cash' or other fields to get the cash of each
    currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Securities Market Value.
    
      
    
    
     
    
    Only applicable to securities accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">long_mv</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Long Market Value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">short_mv</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short Market Value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pending_asset</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Asset in Transit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">interest_charged_amount</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Interest Charged Amount.</td>
    </tr>
    <tr>
    <td style="text-align: left;">frozen_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Funds on Hold.</td>
    </tr>
    <tr>
    <td style="text-align: left;">avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Withdrawable Cash.
    
      
    
    
     
    
    Only applicable to securities accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_withdrawal</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Maximum Withdrawal.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to securities accounts of FUTU HK</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">currency</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
    <td style="text-align: left;">The currency used for this query.
    
      
    
    
     
    
    Only applicable to universal securities accounts and futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">available_funds</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Available funds.
    
      
    
    
     
    
    Only applicable to futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">unrealized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Unrealized gain or loss.
    
      
    
    
     
    
    Only applicable to futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">realized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Realized gain or loss.
    
      
    
    
     
    
    Only applicable to futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">risk_level</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#428">CltRiskLevel</a></td>
    <td style="text-align: left;">Risk control level.
    
      
    
    
     
    
    Only applicable to futures accounts. It is recommanded to use
    risk_status field to get the risk status of securities accounts or
    futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">risk_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7469">CltRiskStatus</a></td>
    <td style="text-align: left;">Risk status.
    
      
    
    
     
    
    <ul>
    <li>Applicable to securities accounts and futures accounts.</li>
    <li>Divided into 9 grades, <code>LEVEL1</code> is the safest and
    <code>LEVEL9</code> is the most dangerous.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">initial_margin</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Initial Margin.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to futures accounts.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">margin_call_margin</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Margin-call Margin.</td>
    </tr>
    <tr>
    <td style="text-align: left;">maintenance_margin</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Maintenance Margin.</td>
    </tr>
    <tr>
    <td style="text-align: left;">hk_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HKD Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">hk_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HKD Withdrawable Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">hkd_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HKD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">hkd_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HK Net Assets Value.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 9.0.5008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">us_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">USD Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">us_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">USD Withdrawable Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">usd_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">USD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">usd_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">US Net Assets Value.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 9.0.5008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cn_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CNH Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts and futures
    accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cn_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CNH Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts and futures
    accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cnh_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CNH Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cnh_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CN Net Assets Value.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 9.0.5008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jp_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JPY Cash.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jp_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JPY Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jpy_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JPY Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jpy_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JP Net Assets Value.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 9.0.5008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sg_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SGD Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sg_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SGD Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sgd_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SGD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sgd_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SG Net Assets Value.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 9.0.5008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">au_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AUD Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">au_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AUD Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">aud_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AUD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">aud_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AU Net Assets Value.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 9.0.5008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pdt_seq</td>
    <td style="text-align: left;">string</td>
    <td style="text-align: left;">Day Trades Left.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_pdt</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is it marked as a PDT.
    
      
    
    
     
    
    True: It is a PDT. False: Not a PDT.<br />
    Only applicable to securities accounts of Moomoo US.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">beginning_dtbp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Beginning DTBP.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">remaining_dtbp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Remaining DTBP.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dt_call_amount</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Day-trading Call Amount.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dt_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1018">DtStatus</a></td>
    <td style="text-align: left;">Day-trading Status.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.accinfo_query()
if ret == RET_OK:
    print(data)
    print(data['power'][0])  # Get the first buying power
    print(data['power'].values.tolist())  # convert to list
else:
    print('accinfo_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
power  max_power_short  net_cash_power  total_assets  securities_assets  fund_assets  bond_assets   cash   market_val      long_mv   short_mv  pending_asset  interest_charged_amount  frozen_cash  avl_withdrawal_cash  max_withdrawal currency available_funds unrealized_pl realized_pl risk_level risk_status  initial_margin  margin_call_margin  maintenance_margin  hk_cash  hk_avl_withdrawal_cash  hkd_net_cash_power  hkd_assets  us_cash  us_avl_withdrawal_cash  usd_net_cash_power  usd_assets  cn_cash  cn_avl_withdrawal_cash  cnh_net_cash_power  cnh_assets  jp_cash  jp_avl_withdrawal_cash  jpy_net_cash_power jpy_assets  sg_cash sg_avl_withdrawal_cash sgd_net_cash_power sgd_assets  au_cash au_avl_withdrawal_cash aud_net_cash_power aud_assets  is_pdt pdt_seq beginning_dtbp remaining_dtbp dt_call_amount dt_status
0  465453.903307    465453.903307             0.0   289932.0404        197028.2204     92903.82          0.0  25.18  197003.0448  211960.7568 -14957.712            0.0                      0.0    25.930845                  0.0             0.0      HKD             N/A           N/A         N/A        N/A      LEVEL3   219346.648525       288656.787955       181250.967601      0.0                     0.0          13225.7955     0.0   3.24                     0.0           9656.4365      0.0    0.0                     0.0                 0.0    0.0      0.0                     0.0                 0.0     0.0    N/A                    N/A                N/A     0.0    N/A                    N/A                N/A    0.0        N/A     N/A            N/A            N/A            N/A       N/A
465453.903307
[465453.903307]
```









## <a href="#5465" class="header-anchor">#</a> Trd_GetFunds.proto

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2101





`uint GetFunds(TrdGetFunds.Request req);`  
`virtual void OnReply_GetFunds(FTAPI_Conn client, uint nSerialNo, ${proto_name.Response rsp);`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.CreateBuilder()
                .SetAccID(281756455988247915L)
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdGetFunds.C2S c2s = TrdGetFunds.C2S.CreateBuilder()
                .SetCurrency((int)TrdCommon.Currency.Currency_HKD)
                .SetHeader(header)
                .Build();
        TrdGetFunds.Request req = TrdGetFunds.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetFunds(req);
        Console.Write("Send TrdGetFunds: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetFunds(FTAPI_Conn client, uint nSerialNo, TrdGetFunds.Response rsp)
    {
        Console.Write("Reply: TrdGetFunds: {0}\n", nSerialNo);
        Console.Write("OnReply_GetFunds: {0}\n", rsp.S2C.ToJson());
    }

    public static void Main(String[] args) {
        FTAPI.Init();
        Program trd = new Program();
        trd.Start();


        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
Trd onInitConnect: ret = 0 desc = connID = 7257654332030703443
Send TrdGetFunds: 4
Reply: TrdGetFunds: 4
OnReply_GetFunds: {
    "header": {
        "trdEnv": 1,
        "accID": 283726802395277157,
        "trdMarket": 6
    },
    "funds": {
        "power": 3030.61116601,
        "totalAssets": 152909.6564,
        "cash": -3586.52,
        "marketVal": 156496.1717,
        "frozenCash": 665.78224097,
        "debtCash": 22533.9124353,
        "avlWithdrawalCash": 3030.61,
        "currency": 1,
        "initialMargin": 113686.06186064694,
        "maintenanceMargin": 107790.01800335373,
        "cashInfoList": [{
            "currency": 0,
            "cash": 0,
            "availableBalance": 0,
            "netCashPower": 0
        }, {
            "currency": 1,
            "cash": 9190.04,
            "availableBalance": 3030.61,
            "netCashPower": 3030.61116601
        }, {
            "currency": 3,
            "cash": -836.36,
            "availableBalance": 0,
            "netCashPower": 0
        }, {
            "currency": 2,
            "cash": 1245.03,
            "availableBalance": 0,
            "netCashPower": 17.97126495
        }, {
            "currency": 5,
            "cash": -3070.32,
            "availableBalance": 0,
            "netCashPower": 0
        }, {
            "currency": 4,
            "cash": -68314,
            "availableBalance": 0,
            "netCashPower": 0
        }],
        "maxPowerShort": 3030.61116601,
        "netCashPower": 0,
        "longMv": 111306.2256,
        "shortMv": -8875.8239,
        "pendingAsset": 0,
        "riskStatus": 3,
        "marginCallMargin": 111801.53345828,
        "securitiesAssets": 98843.8864,
        "fundAssets": 54065.77,
        "bondAssets": 0
    }
}
```









`int getFunds(TrdGetFunds.Request req);`  
`void onReply_GetFunds(FTAPI_Conn client, int nSerialNo, ${proto_name.Response rsp);`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts. data. Obtain fund data
  such as the net asset value of the account, the market value of
  securities, cash, and purchasing power.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.newBuilder()
                .setAccID(281756455988247915L)
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        TrdGetFunds.C2S c2s = TrdGetFunds.C2S.newBuilder()
                .setHeader(header)
                .setCurrency(TrdCommon.Currency.Currency_HKD_VALUE)
                .build();
        TrdGetFunds.Request req = TrdGetFunds.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getFunds(req);
        System.out.printf("Send TrdGetFunds: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetFunds(FTAPI_Conn client, int nSerialNo, TrdGetFunds.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetFunds failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetFunds: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        FTAPI.init();
        TrdDemo trd = new TrdDemo();
        trd.start();

        while (true) {
            try {
                Thread.sleep(1000 * 600);
            } catch (InterruptedException exc) {

            }
        }
    }
}
```





- **Output**



``` text
Send TrdGetFunds: 2
Receive TrdGetFunds: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756455988247915",
      "trdMarket": 1
    },
    "funds": {
        "power": 0.61760332
        "totalAssets": 15222.3336
        "cash": -19.83
        "marketVal": 15242.1666
        "frozenCash": 158.34982707
        "debtCash": 2644.58147475
        "avlWithdrawalCash": 1.24
        "currency": 1
        "initialMargin": 14904.738361057309
        "maintenanceMargin": 14805.9362278707
        "cashInfoList" {
        "currency": 2
        "cash": -95.36
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 0
        "cash": 0.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 1
        "cash": -1097.43
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 4
        "cash": -10267.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 3
        "cash": 2049.58
        "availableBalance": 0.6
        "netCashPower": 0.60345798
        }
        "cashInfoList": {
        "currency": 5
        "cash": 18.62
        "availableBalance": 0.1
        "netCashPower": 0.10953234
        }
        "maxPowerShort": 0.61760332
        "netCashPower": 0.0
        "longMv": 1436.1127
        "shortMv": -168.096
        "pendingAsset": 0.0
        "riskStatus": 3
        "marginCallMargin": 14835.22139711
        "securitiesAssets": 1248.1836
        "fundAssets": 13974.15
        "bondAssets": 0.0
    }
  }
}
```









`Futu::u32_t GetFunds(const Trd_GetFunds::Request &stReq);`  
`virtual void OnReply_GetFunds(Futu::u32_t nSerialNo, const Trd_GetFunds::Response &stRsp) = 0;`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cpp
class Program : public FTSPI_Qot, public FTSPI_Trd, public FTSPI_Conn
{
public:

    Program() {
        m_pTrdApi = FTAPI::CreateTrdApi();
        m_pTrdApi->RegisterTrdSpi(this);
        m_pTrdApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pTrdApi != nullptr)
        {
            m_pTrdApi->UnregisterTrdSpi();
            m_pTrdApi->UnregisterConnSpi();
            FTAPI::ReleaseTrdApi(m_pTrdApi);
            m_pTrdApi = nullptr;
        }
    }

    void Start() {
        m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(FTAPI_Conn* pConn, Futu::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Trd_GetFunds::Request req;
        Trd_GetFunds::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);

        m_GetFundsSerialNo = m_pTrdApi->GetFunds(req);
        cout << "Request GetFunds SerialNo: " << m_GetFundsSerialNo << endl;
    }

    virtual void OnReply_GetFunds(Futu::u32_t nSerialNo, const Trd_GetFunds::Response &stRsp){
        if(nSerialNo == m_GetFundsSerialNo)
        {
            cout << "OnReply_GetFunds SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetFundsSerialNo;
};

int32_t main(int32_t argc, char** argv)
{
    FTAPI::Init();

    {
        Program program;
        program.Start();
        getchar();
    }

    protobuf::ShutdownProtobufLibrary();
    FTAPI::UnInit();
    return 0;
}
```





- **Output**



``` text
connect
Request GetFunds SerialNo: 4
OnReply_GetFunds SerialNo: 4
{
    "retType": 0,
    "retMsg": "",
    "errCode": 0,
    "s2c": {
        "header": {
        "trdEnv": 1,
        "accID": "281756455988247915",
        "trdMarket": 1
        },
        "funds": {
            "power": 0.61760332
            "totalAssets": 15222.3336
            "cash": -19.83
            "marketVal": 15242.1666
            "frozenCash": 158.34982707
            "debtCash": 2644.58147475
            "avlWithdrawalCash": 1.24
            "currency": 1
            "initialMargin": 14904.738361057309
            "maintenanceMargin": 14805.9362278707
            "cashInfoList" {
            "currency": 2
            "cash": -95.36
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 0
            "cash": 0.0
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 1
            "cash": -1097.43
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 4
            "cash": -10267.0
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 3
            "cash": 2049.58
            "availableBalance": 0.6
            "netCashPower": 0.60345798
            }
            "cashInfoList": {
            "currency": 5
            "cash": 18.62
            "availableBalance": 0.1
            "netCashPower": 0.10953234
            }
            "maxPowerShort": 0.61760332
            "netCashPower": 0.0
            "longMv": 1436.1127
            "shortMv": -168.096
            "pendingAsset": 0.0
            "riskStatus": 3
            "marginCallMargin": 14835.22139711
            "securitiesAssets": 1248.1836
            "fundAssets": 13974.15
            "bondAssets": 0.0
        }
    }
}
```









`GetFunds(req);`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

TrdGetFunds(){
    const { RetType } = Common
    const { TrdEnv } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType, s2c: { accList }  } = res
                if(retType == RetType.RetType_Succeed){
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK paper trading environment account

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: acc.trdMarketAuthList[0],
                            }
                        },
                    };

                    websocket.GetFunds(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetFunds: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                        if(retType == RetType.RetType_Succeed){
                            let data = beautify(JSON.stringify(s2c), {
                                indent_size: 2,
                                space_in_empty_paren: true,
                            });
                            console.log(data);
                        }
                    })
                    .catch((error) => {
                        console.log("error:", error);
                    });

                }
            })
            .catch((error) => {
                console.log("GetAccList error:", error);
            });
        } else {
            console.log("error", msg);
        }
    };

    websocket.start(addr, port, enable_ssl, key);
    
    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 5000); // Set the script to receive OpenD push duration to 5 seconds
}
```





- **Output**



``` javascript
GetFunds: errCode 0, retMsg , retType 0
{
    "header": {
      "trdEnv": 1,
      "accID": "281756455988247915",
      "trdMarket": 1
    },
    "funds": {
        "power": 0.61760332
        "totalAssets": 15222.3336
        "cash": -19.83
        "marketVal": 15242.1666
        "frozenCash": 158.34982707
        "debtCash": 2644.58147475
        "avlWithdrawalCash": 1.24
        "currency": 1
        "initialMargin": 14904.738361057309
        "maintenanceMargin": 14805.9362278707
        "cashInfoList" {
        "currency": 2
        "cash": -95.36
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 0
        "cash": 0.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 1
        "cash": -1097.43
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 4
        "cash": -10267.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 3
        "cash": 2049.58
        "availableBalance": 0.6
        "netCashPower": 0.60345798
        }
        "cashInfoList": {
        "currency": 5
        "cash": 18.62
        "availableBalance": 0.1
        "netCashPower": 0.10953234
        }
        "maxPowerShort": 0.61760332
        "netCashPower": 0.0
        "longMv": 1436.1127
        "shortMv": -168.096
        "pendingAsset": 0.0
        "riskStatus": 3
        "marginCallMargin": 14835.22139711
        "securitiesAssets": 1248.1836
        "fundAssets": 13974.15
        "bondAssets": 0.0
    }
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- It will be restricted by the frequency limit for this interface, only
  when refresh_cache is True











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`accinfo_query(trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, refresh_cache=False, currency=Currency.HKD)`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th style="text-align: left;">Parameter</th>
  <th style="text-align: left;">Type</th>
  <th style="text-align: left;">Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="text-align: left;">trd_env</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
  <td style="text-align: left;">Trading environment</td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_id</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Trading account ID.
  
    
  
  
   
  
  <ul>
  <li>When acc_id is 0, the account specified by acc_index is chosen.</li>
  <li>When acc_id is set the ID number (not 0), the account specified by
  acc_id is chosen.</li>
  <li>Using acc_id to query and trade is strongly recommended, acc_index
  will change when adding/closing an account, result in the account you
  specify is inconsistent with the actual trading account.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_index</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The account number in the trading account
  list.
  
    
  
  
   
  
  The default is 0, which means the first trading account.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">refresh_cache</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to refresh the cache.
  
    
  
  
   
  
  <ul>
  <li>True: Re-request data from the moomoo server immediately, without
  using the OpenD cache. At this time, it will be restricted by the
  interface frequency limit.</li>
  <li>False: Use OpenD's cache (The cache needs to be refreshed if it is
  not updated in rare circumstances.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">currency</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
  <td style="text-align: left;">The display currency of the funds.
  
    
  
  
   
  
  <ul>
  <li>Only applicable to universal securities accounts and futures
  accounts, other single-market accounts will ignore this parameter.</li>
  <li>In the returned DataFrame, all fund-related fields can be converted
  with this parameter, except for the fields that explicitly specify the
  currency.</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

<!-- -->

- **Return**

  <table>
  <thead>
  <tr>
  <th>Field</th>
  <th>Type</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>ret</td>
  <td><a href="../ftapi/common.html#8800">RET_CODE</a></td>
  <td>Interface result.</td>
  </tr>
  <tr>
  <td rowspan="2">data</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, fund data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Fund data format as follows:
    <table>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Field</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;">power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Maximum Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the <em>approximate value</em> calculated according to
    the marginable initial margin of 50%. But in fact, this ratio of each
    financial contract is not the same. We recommend using <em><strong>Buy
    on margin</strong></em>, returned by <a
    href="/moomoo-api-doc/en/trade/get-max-trd-qtys.html">Query the Maximum
    Quantity that Can be Bought or Sold</a>, to get the maximum quantity can
    buy.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_power_short</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the <em>approximate value</em> calculated according to
    the shortable initial margin of 60%. But in fact, this ratio of each
    financial contract is not the same. We recommend using <em><strong>Short
    sell</strong></em>, returned by <a
    href="/moomoo-api-doc/en/trade/get-max-trd-qtys.html">Query the Maximum
    Quantity that Can be Bought or Sold</a>, to get the maximum quantity can
    be shorted.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Cash Buying Power.
    
      
    
    
     
    
    Obsolete. Please use 'us_net_cash_power' or other fields to get the cash
    buying power of each currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">total_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total Net Assets.
    
      
    
    
     
    
    Total Net Assets = Security Assets + Fund Assets + Bond Assets
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">securities_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Security Assets
    
      
    
    
     
    
    Minimum OpenD version requirements: 8.2.4218.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">fund_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Fund Assets
    
      
    
    
     
    
    <ul>
    <li>Universal accounts will return the total fund assets value.
    Currently, it does not support for HKD fund and USD fund assets
    value.</li>
    <li>Minimum OpenD version requirements: 8.2.4218.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">bond_assets</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bond Assets
    
      
    
    
     
    
    Minimum OpenD version requirements: 8.2.4218.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Cash.
    
      
    
    
     
    
    Obsolete. Please use 'us_cash' or other fields to get the cash of each
    currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Securities Market Value.
    
      
    
    
     
    
    Only applicable to securities accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">long_mv</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Long Market Value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">short_mv</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short Market Value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pending_asset</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Asset in Transit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">interest_charged_amount</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Interest Charged Amount.</td>
    </tr>
    <tr>
    <td style="text-align: left;">frozen_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Funds on Hold.</td>
    </tr>
    <tr>
    <td style="text-align: left;">avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Withdrawable Cash.
    
      
    
    
     
    
    Only applicable to securities accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_withdrawal</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Maximum Withdrawal.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to securities accounts of FUTU HK</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">currency</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
    <td style="text-align: left;">The currency used for this query.
    
      
    
    
     
    
    Only applicable to universal securities accounts and futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">available_funds</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Available funds.
    
      
    
    
     
    
    Only applicable to futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">unrealized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Unrealized gain or loss.
    
      
    
    
     
    
    Only applicable to futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">realized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Realized gain or loss.
    
      
    
    
     
    
    Only applicable to futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">risk_level</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#428">CltRiskLevel</a></td>
    <td style="text-align: left;">Risk control level.
    
      
    
    
     
    
    Only applicable to futures accounts. It is recommanded to use
    risk_status field to get the risk status of securities accounts or
    futures accounts.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">risk_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7469">CltRiskStatus</a></td>
    <td style="text-align: left;">Risk status.
    
      
    
    
     
    
    <ul>
    <li>Applicable to securities accounts and futures accounts.</li>
    <li>Divided into 9 grades, <code>LEVEL1</code> is the safest and
    <code>LEVEL9</code> is the most dangerous.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">initial_margin</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Initial Margin.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to futures accounts.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">margin_call_margin</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Margin-call Margin.</td>
    </tr>
    <tr>
    <td style="text-align: left;">maintenance_margin</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Maintenance Margin.</td>
    </tr>
    <tr>
    <td style="text-align: left;">hk_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HKD Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">hk_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HKD Withdrawable Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">us_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">USD Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">us_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">USD Withdrawable Cash.
    
      
    
    
     
    
    This field is the real value of this currency, instead of the value
    denominated in this currency.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jp_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JPY Cash.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jp_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JPY Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pdt_seq</td>
    <td style="text-align: left;">string</td>
    <td style="text-align: left;">Day Trades Left.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_pdt</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is it marked as a PDT.
    
      
    
    
     
    
    True: It is a PDT. False: Not a PDT.<br />
    Only applicable to securities accounts of Moomoo US.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">beginning_dtbp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Beginning DTBP.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">remaining_dtbp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Remaining DTBP.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dt_call_amount</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Day-trading Call Amount.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dt_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1018">DtStatus</a></td>
    <td style="text-align: left;">Day-trading Status.
    
      
    
    
     
    
    Only applicable to securities accounts of Moomoo US marked as a
    PDT.<br />
    Minimum OpenD version requirements: 5.8.2008.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cn_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CNH Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts and futures
    accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cn_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CNH Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts and futures
    accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sg_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SGD Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sg_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SGD Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency .</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">au_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AUD Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">au_avl_withdrawal_cash</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AUD Withdrawable Cash.
    
      
    
    
     
    
    <ul>
    <li>Only applicable to universal securities accounts.</li>
    <li>Minimum Futu API version requirements: 5.8.2008</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">hkd_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">HKD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">usd_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">USD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">jpy_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">JPY Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cnh_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">CNH Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sgd_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">SGD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">aud_net_cash_power</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">AUD Cash Buying Power.
    
      
    
    
     
    
    <ul>
    <li>This field is the real value of this currency, instead of the value
    denominated in this currency.</li>
    <li>Minimum version requirements: 8.7</li>
    </ul>
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.accinfo_query()
if ret == RET_OK:
    print(data)
    print(data['power'][0])  # Get the first buying power
    print(data['power'].values.tolist())  # convert to list
else:
    print('accinfo_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**

- **Output**



``` python
power  max_power_short  net_cash_power  total_assets  securities_assets  fund_assets  bond_assets   cash   market_val      long_mv   short_mv  pending_asset  interest_charged_amount  frozen_cash  avl_withdrawal_cash  max_withdrawal currency available_funds unrealized_pl realized_pl risk_level risk_status  initial_margin  margin_call_margin  maintenance_margin  hk_cash  hk_avl_withdrawal_cash  hkd_net_cash_power  hkd_assets  us_cash  us_avl_withdrawal_cash  usd_net_cash_power  usd_assets  cn_cash  cn_avl_withdrawal_cash  cnh_net_cash_power  cnh_assets  jp_cash  jp_avl_withdrawal_cash  jpy_net_cash_power jpy_assets  sg_cash sg_avl_withdrawal_cash sgd_net_cash_power sgd_assets  au_cash au_avl_withdrawal_cash aud_net_cash_power aud_assets  is_pdt pdt_seq beginning_dtbp remaining_dtbp dt_call_amount dt_status
0  465453.903307    465453.903307             0.0   289932.0404        197028.2204     92903.82          0.0  25.18  197003.0448  211960.7568 -14957.712            0.0                      0.0    25.930845                  0.0             0.0      HKD             N/A           N/A         N/A        N/A      LEVEL3   219346.648525       288656.787955       181250.967601      0.0                     0.0          13225.7955     0.0   3.24                     0.0           9656.4365      0.0    0.0                     0.0                 0.0    0.0      0.0                     0.0                 0.0     0.0    N/A                    N/A                N/A     0.0    N/A                    N/A                N/A    0.0        N/A     N/A            N/A            N/A            N/A       N/A
465453.903307
[465453.903307]
```









## <a href="#5465-2" class="header-anchor">#</a> Trd_GetFunds.proto

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2101





`uint GetFunds(TrdGetFunds.Request req);`  
`virtual void OnReply_GetFunds(MMAPI_Conn client, uint nSerialNo, ${proto_name.Response rsp);`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: MMSPI_Trd, MMSPI_Conn {
    MMAPI_Trd trd = new MMAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.CreateBuilder()
                .SetAccID(281756455988247915L)
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdGetFunds.C2S c2s = TrdGetFunds.C2S.CreateBuilder()
                .SetCurrency((int)TrdCommon.Currency.Currency_HKD)
                .SetHeader(header)
                .Build();
        TrdGetFunds.Request req = TrdGetFunds.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetFunds(req);
        Console.Write("Send TrdGetFunds: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetFunds(MMAPI_Conn client, uint nSerialNo, TrdGetFunds.Response rsp)
    {
        Console.Write("Reply: TrdGetFunds: {0}\n", nSerialNo);
        Console.Write("OnReply_GetFunds: {0}\n", rsp.S2C.ToJson());
    }

    public static void Main(String[] args) {
        MMAPI.Init();
        Program trd = new Program();
        trd.Start();


        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
Trd onInitConnect: ret = 0 desc = connID = 7257654332030703443
Send TrdGetFunds: 4
Reply: TrdGetFunds: 4
OnReply_GetFunds: {
    "header": {
        "trdEnv": 1,
        "accID": 283726802395277157,
        "trdMarket": 6
    },
    "funds": {
        "power": 3030.61116601,
        "totalAssets": 152909.6564,
        "cash": -3586.52,
        "marketVal": 156496.1717,
        "frozenCash": 665.78224097,
        "debtCash": 22533.9124353,
        "avlWithdrawalCash": 3030.61,
        "currency": 1,
        "initialMargin": 113686.06186064694,
        "maintenanceMargin": 107790.01800335373,
        "cashInfoList": [{
            "currency": 0,
            "cash": 0,
            "availableBalance": 0,
            "netCashPower": 0
        }, {
            "currency": 1,
            "cash": 9190.04,
            "availableBalance": 3030.61,
            "netCashPower": 3030.61116601
        }, {
            "currency": 3,
            "cash": -836.36,
            "availableBalance": 0,
            "netCashPower": 0
        }, {
            "currency": 2,
            "cash": 1245.03,
            "availableBalance": 0,
            "netCashPower": 17.97126495
        }, {
            "currency": 5,
            "cash": -3070.32,
            "availableBalance": 0,
            "netCashPower": 0
        }, {
            "currency": 4,
            "cash": -68314,
            "availableBalance": 0,
            "netCashPower": 0
        }],
        "maxPowerShort": 3030.61116601,
        "netCashPower": 0,
        "longMv": 111306.2256,
        "shortMv": -8875.8239,
        "pendingAsset": 0,
        "riskStatus": 3,
        "marginCallMargin": 111801.53345828,
        "securitiesAssets": 98843.8864,
        "fundAssets": 54065.77,
        "bondAssets": 0
    }
}
```









`int getFunds(TrdGetFunds.Request req);`  
`void onReply_GetFunds(MMAPI_Conn client, int nSerialNo, ${proto_name.Response rsp);`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts. data. Obtain fund data
  such as the net asset value of the account, the market value of
  securities, cash, and purchasing power.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements MMSPI_Trd, MMSPI_Conn {
    MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.newBuilder()
                .setAccID(281756455988247915L)
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        TrdGetFunds.C2S c2s = TrdGetFunds.C2S.newBuilder()
                .setHeader(header)
                .setCurrency(TrdCommon.Currency.Currency_HKD_VALUE)
                .build();
        TrdGetFunds.Request req = TrdGetFunds.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getFunds(req);
        System.out.printf("Send TrdGetFunds: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetFunds(MMAPI_Conn client, int nSerialNo, TrdGetFunds.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetFunds failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetFunds: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        MMAPI.init();
        TrdDemo trd = new TrdDemo();
        trd.start();

        while (true) {
            try {
                Thread.sleep(1000 * 600);
            } catch (InterruptedException exc) {

            }
        }
    }
}
```





- **Output**



``` text
Send TrdGetFunds: 2
Receive TrdGetFunds: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756455988247915",
      "trdMarket": 1
    },
    "funds": {
        "power": 0.61760332
        "totalAssets": 15222.3336
        "cash": -19.83
        "marketVal": 15242.1666
        "frozenCash": 158.34982707
        "debtCash": 2644.58147475
        "avlWithdrawalCash": 1.24
        "currency": 1
        "initialMargin": 14904.738361057309
        "maintenanceMargin": 14805.9362278707
        "cashInfoList" {
        "currency": 2
        "cash": -95.36
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 0
        "cash": 0.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 1
        "cash": -1097.43
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 4
        "cash": -10267.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 3
        "cash": 2049.58
        "availableBalance": 0.6
        "netCashPower": 0.60345798
        }
        "cashInfoList": {
        "currency": 5
        "cash": 18.62
        "availableBalance": 0.1
        "netCashPower": 0.10953234
        }
        "maxPowerShort": 0.61760332
        "netCashPower": 0.0
        "longMv": 1436.1127
        "shortMv": -168.096
        "pendingAsset": 0.0
        "riskStatus": 3
        "marginCallMargin": 14835.22139711
        "securitiesAssets": 1248.1836
        "fundAssets": 13974.15
        "bondAssets": 0.0
    }
  }
}
```









`moomoo::u32_t GetFunds(const Trd_GetFunds::Request &stReq);`  
`virtual void OnReply_GetFunds(moomoo::u32_t nSerialNo, const Trd_GetFunds::Response &stRsp) = 0;`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cpp
class Program : public MMSPI_Qot, public MMSPI_Trd, public MMSPI_Conn
{
public:

    Program() {
        m_pTrdApi = MMAPI::CreateTrdApi();
        m_pTrdApi->RegisterTrdSpi(this);
        m_pTrdApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pTrdApi != nullptr)
        {
            m_pTrdApi->UnregisterTrdSpi();
            m_pTrdApi->UnregisterConnSpi();
            MMAPI::ReleaseTrdApi(m_pTrdApi);
            m_pTrdApi = nullptr;
        }
    }

    void Start() {
        m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(MMAPI_Conn* pConn, moomoo::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Trd_GetFunds::Request req;
        Trd_GetFunds::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);

        m_GetFundsSerialNo = m_pTrdApi->GetFunds(req);
        cout << "Request GetFunds SerialNo: " << m_GetFundsSerialNo << endl;
    }

    virtual void OnReply_GetFunds(moomoo::u32_t nSerialNo, const Trd_GetFunds::Response &stRsp){
        if(nSerialNo == m_GetFundsSerialNo)
        {
            cout << "OnReply_GetFunds SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetFundsSerialNo;
};

int32_t main(int32_t argc, char** argv)
{
    MMAPI::Init();

    {
        Program program;
        program.Start();
        getchar();
    }

    protobuf::ShutdownProtobufLibrary();
    MMAPI::UnInit();
    return 0;
}
```





- **Output**



``` text
connect
Request GetFunds SerialNo: 4
OnReply_GetFunds SerialNo: 4
{
    "retType": 0,
    "retMsg": "",
    "errCode": 0,
    "s2c": {
        "header": {
        "trdEnv": 1,
        "accID": "281756455988247915",
        "trdMarket": 1
        },
        "funds": {
            "power": 0.61760332
            "totalAssets": 15222.3336
            "cash": -19.83
            "marketVal": 15242.1666
            "frozenCash": 158.34982707
            "debtCash": 2644.58147475
            "avlWithdrawalCash": 1.24
            "currency": 1
            "initialMargin": 14904.738361057309
            "maintenanceMargin": 14805.9362278707
            "cashInfoList" {
            "currency": 2
            "cash": -95.36
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 0
            "cash": 0.0
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 1
            "cash": -1097.43
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 4
            "cash": -10267.0
            "availableBalance": 0.0
            "netCashPower": 0.0
            }
            "cashInfoList": {
            "currency": 3
            "cash": 2049.58
            "availableBalance": 0.6
            "netCashPower": 0.60345798
            }
            "cashInfoList": {
            "currency": 5
            "cash": 18.62
            "availableBalance": 0.1
            "netCashPower": 0.10953234
            }
            "maxPowerShort": 0.61760332
            "netCashPower": 0.0
            "longMv": 1436.1127
            "shortMv": -168.096
            "pendingAsset": 0.0
            "riskStatus": 3
            "marginCallMargin": 14835.22139711
            "securitiesAssets": 1248.1836
            "fundAssets": 13974.15
            "bondAssets": 0.0
        }
    }
}
```









`GetFunds(req);`

- **Description**

  Query fund data such as net asset value, securities market value,
  cash, and purchasing power of trading accounts.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional bool refreshCache = 2; //If explicitly set to true, force to update the cache of OpenD. Otherwise just return the local cached data of OpenD.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
    optional int32 currency = 3; //Currency type, see Trd_Common.Currency. Only required for universal securities accounts and futures accounts, other accounts are ignored
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of currency type, refer to
>   [Currency](/moomoo-api-doc/en/trade/trade.html#1655)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.Funds funds = 2; //Account funds
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For structure of account funds, refer to
>   [Funds](/moomoo-api-doc/en/trade/trade.html#1356)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

TrdGetFunds(){
    const { RetType } = Common
    const { TrdEnv } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType, s2c: { accList }  } = res
                if(retType == RetType.RetType_Succeed){
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK paper trading environment account

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: acc.trdMarketAuthList[0],
                            }
                        },
                    };

                    websocket.GetFunds(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetFunds: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                        if(retType == RetType.RetType_Succeed){
                            let data = beautify(JSON.stringify(s2c), {
                                indent_size: 2,
                                space_in_empty_paren: true,
                            });
                            console.log(data);
                        }
                    })
                    .catch((error) => {
                        console.log("error:", error);
                    });

                }
            })
            .catch((error) => {
                console.log("GetAccList error:", error);
            });
        } else {
            console.log("error", msg);
        }
    };

    websocket.start(addr, port, enable_ssl, key);
    
    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 5000); // Set the script to receive OpenD push duration to 5 seconds
}
```





- **Output**



``` javascript
GetFunds: errCode 0, retMsg , retType 0
{
    "header": {
      "trdEnv": 1,
      "accID": "281756455988247915",
      "trdMarket": 1
    },
    "funds": {
        "power": 0.61760332
        "totalAssets": 15222.3336
        "cash": -19.83
        "marketVal": 15242.1666
        "frozenCash": 158.34982707
        "debtCash": 2644.58147475
        "avlWithdrawalCash": 1.24
        "currency": 1
        "initialMargin": 14904.738361057309
        "maintenanceMargin": 14805.9362278707
        "cashInfoList" {
        "currency": 2
        "cash": -95.36
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 0
        "cash": 0.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 1
        "cash": -1097.43
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 4
        "cash": -10267.0
        "availableBalance": 0.0
        "netCashPower": 0.0
        }
        "cashInfoList": {
        "currency": 3
        "cash": 2049.58
        "availableBalance": 0.6
        "netCashPower": 0.60345798
        }
        "cashInfoList": {
        "currency": 5
        "cash": 18.62
        "availableBalance": 0.1
        "netCashPower": 0.10953234
        }
        "maxPowerShort": 0.61760332
        "netCashPower": 0.0
        "longMv": 1436.1127
        "shortMv": -168.096
        "pendingAsset": 0.0
        "riskStatus": 3
        "marginCallMargin": 14835.22139711
        "securitiesAssets": 1248.1836
        "fundAssets": 13974.15
        "bondAssets": 0.0
    }
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id)
- It will be restricted by the frequency limit for this interface, only
  when refresh_cache is True













