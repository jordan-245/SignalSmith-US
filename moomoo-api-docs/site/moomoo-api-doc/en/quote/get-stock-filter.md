



# <a href="#7242" class="header-anchor">#</a> Filter Stocks by Condition









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_stock_filter(market, filter_list, plate_code=None, begin=0, num=200)`

- **Description**

  Filter stocks by condition

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
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Market identifier.
  
    
  
  
   
  
  Does not distinguish between Shanghai and Shenzhen market, either of
  Shanghai or Shenzhen market will return the Shanghai and Shenzhen
  markets.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">filter_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">The list of filter conditions.
  
    
  
  
   
  
  Data type of elements in the list is <em>SimpleFilter</em>,
  <em>AccumulateFilter</em> or <em>FinancialFilter</em>, refer to the
  following tables.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">plate_code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Plate code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">begin</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Data starting point.</td>
  </tr>
  <tr>
  <td style="text-align: left;">num</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The number of requested data.</td>
  </tr>
  </tbody>
  </table>

  - The relevant parameters of the *SimpleFilter* object are as follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9377">StockField</a></td>
    <td style="text-align: left;">Simple filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering.
    
      
    
    
     
    
    True: no filtering.<br />
    False: filtering. No filtering by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9029">SortDir</a></td>
    <td style="text-align: left;">Sort direction.
    
      
    
    
     
    
    No sorting by default.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *AccumulateFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8316">StockField</a></td>
    <td style="text-align: left;">Cumulative filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering.
    
      
    
    
     
    
    True: no filtering.<br />
    False: filtering. No filtering by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9029">SortDir</a></td>
    <td style="text-align: left;">Sort direction.
    
      
    
    
     
    
    No sorting by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">days</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Accumulative days of filtering data.</td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *FinancialFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2317">StockField</a></td>
    <td style="text-align: left;">Financial filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering.
    
      
    
    
     
    
    True: no filtering.<br />
    False: filtering. No filtering by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9029">SortDir</a></td>
    <td style="text-align: left;">Sort direction.
    
      
    
    
     
    
    No sorting by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">quarter</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8409">FinancialQuarter</a></td>
    <td style="text-align: left;">Accumulation time of financial
    report.</td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *CustomIndicatorFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field1</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3936">StockField</a></td>
    <td style="text-align: left;">Custom indicator filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_field1_para</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Custom indicator parameter.
    
      
    
    
     
    
    Pass parameters according to the indicator type:<br />
    1. MA：[Average moving period]<br />
    2.EMA：[Exponential moving average period]<br />
    3.RSI：[RSI period]<br />
    4.MACD：[Fast average, Slow average, DIF value]<br />
    5.BOLL：[Average period, Offset value]<br />
    6.KDJ：[RSV period, K value period, D value period]
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">relative_position</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9084">RelativePosition</a></td>
    <td style="text-align: left;">Relative position.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_field2</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3936">StockField</a></td>
    <td style="text-align: left;">Custom indicator filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_field2_para</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Custom indicator parameter.
    
      
    
    
     
    
    Pass parameters according to the indicator type:<br />
    1. MA：[Average moving period]<br />
    2.EMA：[Exponential moving average period]<br />
    3.RSI：[RSI period]<br />
    4.MACD：[Fast average, Slow average, DIF value]<br />
    5.BOLL：[Average period, Offset value]<br />
    6.KDJ：[RSV period, K value period, D value period]
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Custom value.
    
      
    
    
     
    
    When stock_field2 selects 'VALUE' in <a
    href="/moomoo-api-doc/en/quote/quote.html#3936">StockField</a>, value is
    a mandatory parameter
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ktype</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
    <td style="text-align: left;">K line type KLType (only supports K_60M,
    K_DAY, K_WEEK, K_MON four time periods).</td>
    </tr>
    <tr>
    <td style="text-align: left;">consecutive_period</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Filters data whose consecutive periods are
    all eligible.
    
      
    
    
     
    
    Fill in the range [1,12].
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering. True: no filtering, False: filtering. No filtering by
    default.</td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *PatternFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6605">StockField</a></td>
    <td style="text-align: left;">Pattern filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ktype</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
    <td style="text-align: left;">K line type KLType (only supports K_60M,
    K_DAY, K_WEEK, K_MON four time periods).</td>
    </tr>
    <tr>
    <td style="text-align: left;">consecutive_period</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Filters data whose consecutive periods are
    all eligible.
    
      
    
    
     
    
    Fill in the range [1,12].
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering. True: no filtering, False: filtering. No filtering by
    default.</td>
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
  <td>If ret == RET_OK, stock selection data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock selection data format as follows:

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
    <td style="text-align: left;">last_page</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is it the last page.</td>
    </tr>
    <tr>
    <td style="text-align: left;">all_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total number of lists.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Stock selection data.
    
      
    
    
     
    
    Data type of elements in the list is <em>FilterStockData</em>.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    - *FilterStockData*'s data format as follows:

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
      <td style="text-align: left;">stock_code</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Stock code.</td>
      </tr>
      <tr>
      <td style="text-align: left;">stock_name</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Stock name.</td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price_to_highest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Current price - high in 52 weeks)/high in
      52 weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price_to_lowest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Current price - low in 52 weeks)/low in
      52 weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">high_price_to_highest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Today's high - high in 52 weeks)/high in
      52 weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">low_price_to_lowest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Today's low - low in 52 weeks)/low in 52
      weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">volume_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Volume ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">bid_ask_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">The committee.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">lot_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price per lot.</td>
      </tr>
      <tr>
      <td style="text-align: left;">market_val</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Market value.</td>
      </tr>
      <tr>
      <td style="text-align: left;">pe_annual</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/E ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">pe_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/E ratio TTM.</td>
      </tr>
      <tr>
      <td style="text-align: left;">pb_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/B ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">change_rate_5min</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change in five minutes.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">change_rate_begin_year</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change of this year.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ps_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/S rate TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">pcf_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/CF rate TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">total_share</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Total number of shares.
      
        
      
      
       
      
      unit: share
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">float_share</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Shares outstanding.
      
        
      
      
       
      
      unit: share
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">float_market_val</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Market capitalization.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">change_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">amplitude</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Amplitude.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">volume</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Average daily volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Average daily turnover.</td>
      </tr>
      <tr>
      <td style="text-align: left;">turnover_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profit</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net profit.</td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profix_growth</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net profit growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">sum_of_business</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating income.</td>
      </tr>
      <tr>
      <td style="text-align: left;">sum_of_business_growth</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of operating
      income.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profit_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net interest rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">gross_profit_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Gross profit rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">debt_asset_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Asset-liability ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">return_on_equity_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Return on net assets.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roic</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Return on invested capital.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roa_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Return on Assets TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebit_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Earnings before interest and tax TTM.
      
        
      
      
       
      
      unit: yuan.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebitda</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Earnings before interest and tax,
      depreciation and amortization.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_margin_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating profit margin TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebit_margin</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EBIT profit margin.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebitda_margin</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EBITDA profit margin.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">financial_cost_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Financial cost rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_profit_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating profit TTM.
      
        
      
      
       
      
      unit: yuan.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">shareholder_net_profit_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net profit attributable to the parent
      company.
      
        
      
      
       
      
      unit: yuan.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profit_cash_cover_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Proportion of cash income in profit.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">current_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">quick_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Quick ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">current_asset_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current asset ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">current_debt_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current debt ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">equity_multiplier</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Equity multiplier.</td>
      </tr>
      <tr>
      <td style="text-align: left;">property_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Property ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">cash_and_cash_equivalents</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Cash and cash equivalents.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">total_asset_turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Total asset turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">fixed_asset_turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Fixed asset turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">inventory_turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Inventory turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_cash_flow_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating cash flow TTM.
      
        
      
      
       
      
      unit: yuan. Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">accounts_receivable</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net accounts receivable.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebit_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EBIT year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_profit_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating profit year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">total_assets_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of total assets.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">profit_to_shareholders_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of net profit
      attributable to the parent.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">profit_before_tax_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of total profit.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">eps_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EPS year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roe_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">ROE year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roic_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">ROIC year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">nocf_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of operating cash
      flow.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">nocf_per_share_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of operating cash
      flow per share.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_revenue_cash_cover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating cash income ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_profit_to_total_profit</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">operating profit percentage.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">basic_eps</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Basic earnings per share.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">diluted_eps</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Diluted earnings per share.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">nocf_per_share</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net operating cash flow per share.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">latest price</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Simple moving average
      
        
      
      
       
      
      Returns values based on the MA parameter.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ma5</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">5-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma10</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">10-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma20</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">20-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma30</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">30-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma60</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">60-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma120</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">120-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma250</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">250-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">rsi</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">RSI
      
        
      
      
       
      
      Returns values based on the RSI parameter. The default parameter for RSI
      is 12.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ema</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">exponential moving average
      
        
      
      
       
      
      Returns values based on the EMA parameter.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ema5</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">5-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema10</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">10-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema20</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">20-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema30</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">30-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema60</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">60-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema120</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">120日-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema250</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">250日-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">kdj_k</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">K value of KDJ indicator
      
        
      
      
       
      
      Returns values based on the KDJ parameter. The default parameter for KDJ
      is [9,3,3].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">kdj_d</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">D value of KDJ indicator
      
        
      
      
       
      
      Returns values based on the KDJ parameter. The default parameter for KDJ
      is [9,3,3].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">kdj_j</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">J value of KDJ indicator
      
        
      
      
       
      
      Returns values based on the KDJ parameter. The default parameter for KDJ
      is [9,3,3].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">macd_diff</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">DIFF value of MACD indicator
      
        
      
      
       
      
      Returns values based on the MACD parameter. The default parameter for
      MACD is [12,26,9].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">macd_dea</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">DEA value of MACD indicator
      
        
      
      
       
      
      Returns values based on the MACD parameter. The default parameter for
      MACD is [12,26,9].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">macd</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">MACD value of MACD indicator
      
        
      
      
       
      
      Returns values based on the MACD parameter. The default parameter for
      MACD is [12,26,9].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">boll_upper</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">UPPER value of BOLL indicator
      
        
      
      
       
      
      Returns values based on the BOLL parameter. The default parameter for
      BOLL is [20.2].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">boll_middler</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">MIDDLER value of BOLL indicator
      
        
      
      
       
      
      Returns values based on the BOLL parameter. The default parameter for
      BOLL is [20.2].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">boll_lower</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">LOWER value of BOLL indicator
      
        
      
      
       
      
      Returns values based on the BOLL parameter. The default parameter for
      BOLL is [20.2].
      
      
      
      </td>
      </tr>
      </tbody>
      </table>

- **Example**



``` python
from futu import *
import time

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
simple_filter = SimpleFilter()
simple_filter.filter_min = 2
simple_filter.filter_max = 1000
simple_filter.stock_field = StockField.CUR_PRICE
simple_filter.is_no_filter = False
# simple_filter.sort = SortDir.ASCEND

financial_filter = FinancialFilter()
financial_filter.filter_min = 0.5
financial_filter.filter_max = 50
financial_filter.stock_field = StockField.CURRENT_RATIO
financial_filter.is_no_filter = False
financial_filter.sort = SortDir.ASCEND
financial_filter.quarter = FinancialQuarter.ANNUAL

custom_filter = CustomIndicatorFilter()
custom_filter.ktype = KLType.K_DAY
custom_filter.stock_field1 = StockField.KDJ_K
custom_filter.stock_field1_para = [10,4,4]
custom_filter.stock_field2 = StockField.KDJ_K
custom_filter.stock_field2_para = [9,3,3]
custom_filter.relative_position = RelativePosition.MORE
custom_filter.is_no_filter = False

nBegin = 0
last_page = False
ret_list = list()
while not last_page:
    nBegin += len(ret_list)
    ret, ls = quote_ctx.get_stock_filter(market=Market.HK, filter_list=[simple_filter, financial_filter, custom_filter], begin=nBegin)  # filter with simple, financial and indicator filter for HK market
    if ret == RET_OK:
        last_page, all_count, ret_list = ls
        print('all count = ', all_count)
        for item in ret_list:
            print(item.stock_code)  # Get the stock code
            print(item.stock_name)  # Get the stock name
            print(item[simple_filter])   # Get the value of the variable corresponding to simple_filter
            print(item[financial_filter])   # Get the value of the variable corresponding to financial_filter 
            print(item[custom_filter])  # Get the value of custom_filter
    else:
        print('error: ', ls)
        break
    time.sleep(3)  # Sleep for 3 seconds to avoid trigger frequency limitation

quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
39 39 [ stock_code:HK.08103  stock_name:hmvod Limited  cur_price:2.69  current_ratio(annual):4.413 ,  stock_code:HK.00376  stock_name:Yunfeng Financial  cur_price:2.96  current_ratio(annual):12.585 ,  stock_code:HK.09995  stock_name:RemeGen Co., Ltd.  cur_price:92.85  current_ratio(annual):16.054 ,  stock_code:HK.80737  stock_name:Shenzhen Investment Holdings Bay Area Development  cur_price:2.8  current_ratio(annual):17.249 ,  stock_code:HK.00737  stock_name:Shenzhen Investment Holdings Bay Area Development  cur_price:3.25  current_ratio(annual):17.249 ,  stock_code:HK.03939  stock_name:Wanguo International Mining  cur_price:2.22  current_ratio(annual):17.323 ,  stock_code:HK.01055  stock_name:China Southern Airlines  cur_price:5.17  current_ratio(annual):17.529 ,  stock_code:HK.02638  stock_name:HK Electric Investments and HK Electric Investments  cur_price:7.68  current_ratio(annual):21.255 ,  stock_code:HK.00670  stock_name:China Eastern Airlines Corporation  cur_price:3.53  current_ratio(annual):25.194 ,  stock_code:HK.01952  stock_name:Everest Medicines  cur_price:69.5  current_ratio(annual):26.029 ,  stock_code:HK.00089  stock_name:Tai Sang Land Development  cur_price:4.22  current_ratio(annual):26.914 ,  stock_code:HK.00728  stock_name:China Telecom Corporation  cur_price:2.84  current_ratio(annual):27.651 ,  stock_code:HK.01372  stock_name:Bisu Technology Group  cur_price:5.63  current_ratio(annual):28.303 ,  stock_code:HK.00753  stock_name:Air China Limited  cur_price:6.37  current_ratio(annual):31.828 ,  stock_code:HK.01997  stock_name:Wharf Real Estate Investment  cur_price:44.15  current_ratio(annual):33.239 ,  stock_code:HK.02158  stock_name:Yidu Tech Inc.  cur_price:38.95  current_ratio(annual):34.046 ,  stock_code:HK.02588  stock_name:BOC Aviation Ltd.  cur_price:76.85  current_ratio(annual):34.531 ,  stock_code:HK.01330  stock_name:Dynagreen Environmental Protection Group  cur_price:3.36  current_ratio(annual):35.028 ,  stock_code:HK.01525  stock_name:SHANGHAI GENCH EDUCATION GROUP LIMITED  cur_price:6.28  current_ratio(annual):36.989 ,  stock_code:HK.09908  stock_name:JiaXing Gas Group  cur_price:10.02  current_ratio(annual):37.848 ,  stock_code:HK.06078  stock_name:Hygeia Healthcare Holdings  cur_price:49.2  current_ratio(annual):39.0 ,  stock_code:HK.01071  stock_name:Huadian Power International Corporation  cur_price:2.16  current_ratio(annual):39.507 ,  stock_code:HK.00357  stock_name:Hainan Meilan International Airport  cur_price:33.65  current_ratio(annual):39.514 ,  stock_code:HK.00762  stock_name:China Unicom  cur_price:5.21  current_ratio(annual):40.74 ,  stock_code:HK.01787  stock_name:Shandong Gold Mining  cur_price:15.62  current_ratio(annual):41.604 ,  stock_code:HK.00902  stock_name:Huaneng Power International,Inc.  cur_price:2.67  current_ratio(annual):42.919 ,  stock_code:HK.00934  stock_name:Sinopec Kantons  cur_price:2.98  current_ratio(annual):43.361 ,  stock_code:HK.01117  stock_name:China Modern Dairy  cur_price:2.29  current_ratio(annual):45.037 ,  stock_code:HK.00177  stock_name:Jiangsu Expressway  cur_price:8.78  current_ratio(annual):45.93 ,  stock_code:HK.01379  stock_name:Wenling Zhejiang Measuring and Cutting Tools Trading Centre Company Limited*  cur_price:5.71  current_ratio(annual):46.774 ,  stock_code:HK.01876  stock_name:Budweiser Brewing Company APAC Limited  cur_price:22.45  current_ratio(annual):46.917 ,  stock_code:HK.01907  stock_name:China Risun  cur_price:4.38  current_ratio(annual):47.129 ,  stock_code:HK.02160  stock_name:MicroPort CardioFlow Medtech Corporation  cur_price:15.52  current_ratio(annual):47.384 ,  stock_code:HK.00293  stock_name:Cathay Pacific Airways  cur_price:7.13  current_ratio(annual):47.983 ,  stock_code:HK.00694  stock_name:Beijing Capital International Airport  cur_price:6.29  current_ratio(annual):47.985 ,  stock_code:HK.09922  stock_name:Jiumaojiu International Holdings Limited  cur_price:26.8  current_ratio(annual):48.278 ,  stock_code:HK.01083  stock_name:Towngas China  cur_price:3.38  current_ratio(annual):49.2 ,  stock_code:HK.00291  stock_name:China Resources Beer  cur_price:58.2  current_ratio(annual):49.229 ,  stock_code:HK.00306  stock_name:Kwoon Chung Bus  cur_price:2.29  current_ratio(annual):49.769 ]
HK.08103
hmvod Limited
2.69
2.69
4.413
...
HK.00306
Kwoon Chung Bus
2.29
2.29
49.769
```









## <a href="#2109" class="header-anchor">#</a> Qot_StockFilter.proto

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the Futu API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

* **Parameter**

```protobuf
// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10 
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3215





`uint StockFilter(QotStockFilter.Request req);`  
`virtual void OnReply_StockFilter(FTAPI_Conn client, uint nSerialNo, QotStockFilter.Response rsp);`

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the Futu API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: FTSPI_Qot, FTSPI_Conn {
    FTAPI_Qot qot = new FTAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
        qot.SetQotCallback(this); //Set transaction callback
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        QotStockFilter.BaseFilter filter = QotStockFilter.BaseFilter.CreateBuilder()
                .SetFieldName(QotStockFilter.StockField.StockField_CurPrice)
                .SetFilterMax(100)
                .SetFilterMax(200)
                .Build();
        QotStockFilter.C2S c2s = QotStockFilter.C2S.CreateBuilder()
                .SetBegin(0)
                .SetNum(10)
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .AddBaseFilterList(filter)
            .Build();
        QotStockFilter.Request req = QotStockFilter.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.StockFilter(req);
        Console.Write("Send QotStockFilter: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_StockFilter(FTAPI_Conn client, uint nSerialNo, QotStockFilter.Response rsp)
    {
        Console.Write("Reply: QotStockFilter: {0}\n", nSerialNo, rsp.ToString());
        Console.Write("code: {0}, name: {1} \n", rsp.S2C.DataListList[0].Security.Code,
            rsp.S2C.DataListList[0].Name);
    }

    public static void Main(String[] args) {
        FTAPI.Init();
        Program qot = new Program();
        qot.Start();


        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
Qot onInitConnect: ret=0 desc= connID=6825721743616225277
Send QotStockFilter: 3
Reply: QotStockFilter: 3
code: 00376, name: Yunfeng Financial
```









`int stockFilter(QotStockFilter.Request req);`  
`void onReply_StockFilter(FTAPI_Conn client, int nSerialNo, QotStockFilter.Response rsp);`

- **Description**

  Filter stocks by condition

- **Parameter**



``` protobuf
// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
        qot.setQotSpi(this); //Set transaction callback
    }

    public void start() {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        QotStockFilter.BaseFilter filter = QotStockFilter.BaseFilter.newBuilder()
                .setFieldName(QotStockFilter.StockField.StockField_CurPrice_VALUE)
                .setFilterMax(100)
                .setFilterMax(200)
                .build();
        QotStockFilter.C2S c2s = QotStockFilter.C2S.newBuilder()
                .setBegin(0)
                .setNum(10)
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .addBaseFilterList(filter)
            .build();
        QotStockFilter.Request req = QotStockFilter.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.stockFilter(req);
        System.out.printf("Send QotStockFilter: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_StockFilter(FTAPI_Conn client, int nSerialNo, QotStockFilter.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotStockFilter failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotStockFilter: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        FTAPI.init();
        QotDemo qot = new QotDemo();
        qot.start();

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
Send QotStockFilter: 2
Receive QotStockFilter: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "lastPage": false,
    "allCount": 2431,
    "dataList": [{
      "security": {
        "market": 1,
        "code": "08560"
      },
      "name": "Great World"
    }, ... {
      "security": {
        "market": 1,
        "code": "02171"
      },
      "name": "CARsgen Therapeutics"
    }]
  }
}
```









`Futu::u32_t StockFilter(const Qot_StockFilter::Request &stReq);`  
`virtual void OnReply_StockFilter(Futu::u32_t nSerialNo, const Qot_StockFilter::Response &stRsp) = 0;`

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the Futu API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cpp
class Program : public FTSPI_Qot, public FTSPI_Trd, public FTSPI_Conn
{
public:

    Program() {
        m_pQotApi = FTAPI::CreateQotApi();
        m_pQotApi->RegisterQotSpi(this);
        m_pQotApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pQotApi != nullptr)
        {
            m_pQotApi->UnregisterQotSpi();
            m_pQotApi->UnregisterConnSpi();
            FTAPI::ReleaseQotApi(m_pQotApi);
            m_pQotApi = nullptr;
        }
    }

    void Start() {
        m_pQotApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(FTAPI_Conn* pConn, Futu::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Qot_StockFilter::Request req;
        Qot_StockFilter::C2S *c2s = req.mutable_c2s();
        c2s->set_begin(0);
        c2s->set_num(50);
        c2s->set_market(1);
        
        m_StockFilterSerialNo = m_pQotApi->StockFilter(req);
        cout << "Request StockFilter SerialNo: " << m_StockFilterSerialNo << endl;
    }

    virtual void OnReply_StockFilter(Futu::u32_t nSerialNo, const Qot_StockFilter::Response &stRsp){
        if(nSerialNo == m_StockFilterSerialNo)
        {
            cout << "OnReply_StockFilter SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_StockFilterSerialNo;
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
Request StockFilter SerialNo: 4
OnReply_StockFilter SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "lastPage": false,
  "allCount": 2426,
  "dataList": [
   {
    "security": {
     "market": 1,
     "code": "02930"
    },
    "name": "Silk Road Logistics"
   },
...
   {
    "security": {
     "market": 1,
     "code": "01440"
    },
    "name": "Deyun Holding Ltd."
   }
  ]
 }
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)





`StockFilter(req);`

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the Futu API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotStockFilter(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    begin: 0, 
                    num: 2,
                    market: QotMarket.QotMarket_HK_Security,
                },
            };

            websocket.StockFilter(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("StockFilter: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
StockFilter: errCode 0, retMsg , retType 0
{
  "lastPage": false,
  "allCount": 2438,
  "dataList": [{
    "security": {
      "market": 1,
      "code": "02969"
    },
    "name": "LAI SUN DEV RTS"
  }, {
    "security": {
      "market": 1,
      "code": "08580"
    },
    "name": "Luen Wong Group"
  }]
}
stop
```











Tips

- Use [Get sub-plate list
  function](/moomoo-api-doc/en/quote/get-plate-list.html) to get the
  sub-plate code, the plates supported by conditional stock selection
  are respectively
  1.  The industry plate and concept plate of HK market.
  2.  Industry plate of US market.
  3.  Shanghai and Shenzhen's industry plate, conceptual plate and
      geographic plate.
- Supported plate index codes
  | Code           | Description                           |
  |:---------------|:--------------------------------------|
  | HK.Motherboard | Main plate of HK market               |
  | HK.GEM         | Growth Enterprise Market of HK market |
  | HK.BK1911      | Main plate of H-Share                 |
  | HK.BK1912      | Growth Enterprise Market of H-share   |
  | US.NYSE        | New York Stock Exchange               |
  | US.AMEX        | American Exchange                     |
  | US.NASDAQ      | NASDAQ                                |
  | SH.3000000     | Shanghai main plate                   |
  | SZ.3000001     | Shenzhen main plate                   |
  | SZ.3000004     | Shenzhen Growth Enterprise Market     |





Interface Limitations

- BMP authority of HK market does not support conditional stock
  filteration function
- A maximum of 10 requests per 30 seconds
- At most 200 filter results are returned per page
- It is recommended that the filter conditions do not exceed 250,
  otherwise "business processing timeout did not return" may appear
- The maximum number of the same filter condition for cumulative filter
  properties is 10
- If you use dynamic data such as "current price" as the sorting field,
  the sorting of the data may change between multiple pages
- Non-similar indicators do not support comparison, and are limited to
  the establishment of comparison relationships between similar
  indicators, and comparisons across different types of indicators will
  cause errors. For example: MA5 and MA10 can establish a relationship.
  MA5 and EMA10 cannot establish a relationship.
- The same type of filter conditions of the custom indicator attribute
  exceeds the upper limit of 10
- Simple attributes, financial attributes, and morphological attributes
  do not support repeated designation of filter conditions for the same
  field
- Stock filter function currently does not support irregular trading
  hours (i.e.pre-market, post-market and overnight). All results are
  based on regular trading hours data.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_stock_filter(market, filter_list, plate_code=None, begin=0, num=200)`

- **Description**

  Filter stocks by condition

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
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Market identifier.
  
    
  
  
   
  
  Does not distinguish between Shanghai and Shenzhen market, either of
  Shanghai or Shenzhen market will return the Shanghai and Shenzhen
  markets.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">filter_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">The list of filter conditions.
  
    
  
  
   
  
  Data type of elements in the list is <em>SimpleFilter</em>,
  <em>AccumulateFilter</em> or <em>FinancialFilter</em>, refer to the
  following tables.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">plate_code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Plate code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">begin</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Data starting point.</td>
  </tr>
  <tr>
  <td style="text-align: left;">num</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The number of requested data.</td>
  </tr>
  </tbody>
  </table>

  - The relevant parameters of the *SimpleFilter* object are as follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9377">StockField</a></td>
    <td style="text-align: left;">Simple filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering.
    
      
    
    
     
    
    True: no filtering.<br />
    False: filtering. No filtering by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9029">SortDir</a></td>
    <td style="text-align: left;">Sort direction.
    
      
    
    
     
    
    No sorting by default.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *AccumulateFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8316">StockField</a></td>
    <td style="text-align: left;">Cumulative filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering.
    
      
    
    
     
    
    True: no filtering.<br />
    False: filtering. No filtering by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9029">SortDir</a></td>
    <td style="text-align: left;">Sort direction.
    
      
    
    
     
    
    No sorting by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">days</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Accumulative days of filtering data.</td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *FinancialFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2317">StockField</a></td>
    <td style="text-align: left;">Financial filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">filter_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit of the interval (closed
    interval).
    
      
    
    
     
    
    Default by +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering.
    
      
    
    
     
    
    True: no filtering.<br />
    False: filtering. No filtering by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9029">SortDir</a></td>
    <td style="text-align: left;">Sort direction.
    
      
    
    
     
    
    No sorting by default.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">quarter</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8409">FinancialQuarter</a></td>
    <td style="text-align: left;">Accumulation time of financial
    report.</td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *CustomIndicatorFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field1</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3936">StockField</a></td>
    <td style="text-align: left;">Custom indicator filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_field1_para</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Custom indicator parameter.
    
      
    
    
     
    
    Pass parameters according to the indicator type:<br />
    1. MA：[Average moving period]<br />
    2.EMA：[Exponential moving average period]<br />
    3.RSI：[RSI period]<br />
    4.MACD：[Fast average, Slow average, DIF value]<br />
    5.BOLL：[Average period, Offset value]<br />
    6.KDJ：[RSV period, K value period, D value period]
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">relative_position</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9084">RelativePosition</a></td>
    <td style="text-align: left;">Relative position.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_field2</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3936">StockField</a></td>
    <td style="text-align: left;">Custom indicator filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_field2_para</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Custom indicator parameter.
    
      
    
    
     
    
    Pass parameters according to the indicator type:<br />
    1. MA：[Average moving period]<br />
    2.EMA：[Exponential moving average period]<br />
    3.RSI：[RSI period]<br />
    4.MACD：[Fast average, Slow average, DIF value]<br />
    5.BOLL：[Average period, Offset value]<br />
    6.KDJ：[RSV period, K value period, D value period]
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Custom value.
    
      
    
    
     
    
    When stock_field2 selects 'VALUE' in <a
    href="/moomoo-api-doc/en/quote/quote.html#3936">StockField</a>, value is
    a mandatory parameter
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ktype</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
    <td style="text-align: left;">K line type KLType (only supports K_60M,
    K_DAY, K_WEEK, K_MON four time periods).</td>
    </tr>
    <tr>
    <td style="text-align: left;">consecutive_period</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Filters data whose consecutive periods are
    all eligible.
    
      
    
    
     
    
    Fill in the range [1,12].
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering. True: no filtering, False: filtering. No filtering by
    default.</td>
    </tr>
    </tbody>
    </table>

  - The relevant parameters of the *PatternFilter* object are as
    follows:

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
    <td style="text-align: left;">stock_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6605">StockField</a></td>
    <td style="text-align: left;">Pattern filter properties.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ktype</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
    <td style="text-align: left;">K line type KLType (only supports K_60M,
    K_DAY, K_WEEK, K_MON four time periods).</td>
    </tr>
    <tr>
    <td style="text-align: left;">consecutive_period</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Filters data whose consecutive periods are
    all eligible.
    
      
    
    
     
    
    Fill in the range [1,12].
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_no_filter</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the field does not require
    filtering. True: no filtering, False: filtering. No filtering by
    default.</td>
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
  <td>If ret == RET_OK, stock selection data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock selection data format as follows:

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
    <td style="text-align: left;">last_page</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is it the last page.</td>
    </tr>
    <tr>
    <td style="text-align: left;">all_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total number of lists.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Stock selection data.
    
      
    
    
     
    
    Data type of elements in the list is <em>FilterStockData</em>.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    - *FilterStockData*'s data format as follows:

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
      <td style="text-align: left;">stock_code</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Stock code.</td>
      </tr>
      <tr>
      <td style="text-align: left;">stock_name</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Stock name.</td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price_to_highest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Current price - high in 52 weeks)/high in
      52 weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price_to_lowest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Current price - low in 52 weeks)/low in
      52 weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">high_price_to_highest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Today's high - high in 52 weeks)/high in
      52 weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">low_price_to_lowest_52weeks_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">(Today's low - low in 52 weeks)/low in 52
      weeks.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">volume_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Volume ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">bid_ask_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">The committee.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">lot_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price per lot.</td>
      </tr>
      <tr>
      <td style="text-align: left;">market_val</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Market value.</td>
      </tr>
      <tr>
      <td style="text-align: left;">pe_annual</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/E ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">pe_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/E ratio TTM.</td>
      </tr>
      <tr>
      <td style="text-align: left;">pb_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/B ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">change_rate_5min</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change in five minutes.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">change_rate_begin_year</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change of this year.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ps_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/S rate TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">pcf_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">P/CF rate TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">total_share</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Total number of shares.
      
        
      
      
       
      
      unit: share
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">float_share</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Shares outstanding.
      
        
      
      
       
      
      unit: share
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">float_market_val</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Market capitalization.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">change_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">amplitude</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Amplitude.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">volume</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Average daily volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Average daily turnover.</td>
      </tr>
      <tr>
      <td style="text-align: left;">turnover_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profit</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net profit.</td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profix_growth</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net profit growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">sum_of_business</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating income.</td>
      </tr>
      <tr>
      <td style="text-align: left;">sum_of_business_growth</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of operating
      income.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profit_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net interest rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">gross_profit_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Gross profit rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">debt_asset_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Asset-liability ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">return_on_equity_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Return on net assets.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roic</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Return on invested capital.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roa_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Return on Assets TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebit_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Earnings before interest and tax TTM.
      
        
      
      
       
      
      unit: yuan.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebitda</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Earnings before interest and tax,
      depreciation and amortization.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_margin_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating profit margin TTM.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebit_margin</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EBIT profit margin.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebitda_margin</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EBITDA profit margin.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">financial_cost_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Financial cost rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_profit_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating profit TTM.
      
        
      
      
       
      
      unit: yuan.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">shareholder_net_profit_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net profit attributable to the parent
      company.
      
        
      
      
       
      
      unit: yuan.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">net_profit_cash_cover_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Proportion of cash income in profit.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.<br />
      Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">current_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">quick_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Quick ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">current_asset_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current asset ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">current_debt_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current debt ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">equity_multiplier</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Equity multiplier.</td>
      </tr>
      <tr>
      <td style="text-align: left;">property_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Property ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">cash_and_cash_equivalents</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Cash and cash equivalents.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">total_asset_turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Total asset turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">fixed_asset_turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Fixed asset turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">inventory_turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Inventory turnover rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_cash_flow_ttm</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating cash flow TTM.
      
        
      
      
       
      
      unit: yuan. Only applicable to annual reports.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">accounts_receivable</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net accounts receivable.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ebit_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EBIT year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_profit_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating profit year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">total_assets_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of total assets.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">profit_to_shareholders_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of net profit
      attributable to the parent.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">profit_before_tax_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of total profit.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">eps_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">EPS year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roe_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">ROE year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">roic_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">ROIC year-on-year growth rate.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">nocf_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of operating cash
      flow.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">nocf_per_share_growth_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Year-on-year growth rate of operating cash
      flow per share.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_revenue_cash_cover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Operating cash income ratio.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">operating_profit_to_total_profit</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">operating profit percentage.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">basic_eps</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Basic earnings per share.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">diluted_eps</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Diluted earnings per share.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">nocf_per_share</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Net operating cash flow per share.
      
        
      
      
       
      
      unit: yuan
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">latest price</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Simple moving average
      
        
      
      
       
      
      Returns values based on the MA parameter.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ma5</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">5-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma10</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">10-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma20</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">20-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma30</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">30-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma60</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">60-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma120</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">120-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ma250</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">250-day simple moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">rsi</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">RSI
      
        
      
      
       
      
      Returns values based on the RSI parameter. The default parameter for RSI
      is 12.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ema</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">exponential moving average
      
        
      
      
       
      
      Returns values based on the EMA parameter.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">ema5</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">5-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema10</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">10-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema20</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">20-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema30</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">30-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema60</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">60-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema120</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">120日-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">ema250</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">250日-day exponential moving average</td>
      </tr>
      <tr>
      <td style="text-align: left;">kdj_k</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">K value of KDJ indicator
      
        
      
      
       
      
      Returns values based on the KDJ parameter. The default parameter for KDJ
      is [9,3,3].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">kdj_d</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">D value of KDJ indicator
      
        
      
      
       
      
      Returns values based on the KDJ parameter. The default parameter for KDJ
      is [9,3,3].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">kdj_j</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">J value of KDJ indicator
      
        
      
      
       
      
      Returns values based on the KDJ parameter. The default parameter for KDJ
      is [9,3,3].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">macd_diff</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">DIFF value of MACD indicator
      
        
      
      
       
      
      Returns values based on the MACD parameter. The default parameter for
      MACD is [12,26,9].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">macd_dea</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">DEA value of MACD indicator
      
        
      
      
       
      
      Returns values based on the MACD parameter. The default parameter for
      MACD is [12,26,9].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">macd</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">MACD value of MACD indicator
      
        
      
      
       
      
      Returns values based on the MACD parameter. The default parameter for
      MACD is [12,26,9].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">boll_upper</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">UPPER value of BOLL indicator
      
        
      
      
       
      
      Returns values based on the BOLL parameter. The default parameter for
      BOLL is [20.2].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">boll_middler</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">MIDDLER value of BOLL indicator
      
        
      
      
       
      
      Returns values based on the BOLL parameter. The default parameter for
      BOLL is [20.2].
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">boll_lower</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">LOWER value of BOLL indicator
      
        
      
      
       
      
      Returns values based on the BOLL parameter. The default parameter for
      BOLL is [20.2].
      
      
      
      </td>
      </tr>
      </tbody>
      </table>

- **Example**



``` python
from moomoo import *
import time

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
simple_filter = SimpleFilter()
simple_filter.filter_min = 2
simple_filter.filter_max = 1000
simple_filter.stock_field = StockField.CUR_PRICE
simple_filter.is_no_filter = False
# simple_filter.sort = SortDir.ASCEND

financial_filter = FinancialFilter()
financial_filter.filter_min = 0.5
financial_filter.filter_max = 50
financial_filter.stock_field = StockField.CURRENT_RATIO
financial_filter.is_no_filter = False
financial_filter.sort = SortDir.ASCEND
financial_filter.quarter = FinancialQuarter.ANNUAL

custom_filter = CustomIndicatorFilter()
custom_filter.ktype = KLType.K_DAY
custom_filter.stock_field1 = StockField.KDJ_K
custom_filter.stock_field1_para = [10,4,4]
custom_filter.stock_field2 = StockField.KDJ_K
custom_filter.stock_field2_para = [9,3,3]
custom_filter.relative_position = RelativePosition.MORE
custom_filter.is_no_filter = False

nBegin = 0
last_page = False
ret_list = list()
while not last_page:
    nBegin += len(ret_list)
    ret, ls = quote_ctx.get_stock_filter(market=Market.HK, filter_list=[simple_filter, financial_filter, custom_filter], begin=nBegin)  # filter with simple, financial and indicator filter for HK market
    if ret == RET_OK:
        last_page, all_count, ret_list = ls
        print('all count = ', all_count)
        for item in ret_list:
            print(item.stock_code)  # Get the stock code
            print(item.stock_name)  # Get the stock name
            print(item[simple_filter])   # Get the value of the variable corresponding to simple_filter
            print(item[financial_filter])   # Get the value of the variable corresponding to financial_filter 
            print(item[custom_filter])  # Get the value of custom_filter
    else:
        print('error: ', ls)
        break
    time.sleep(3)  # Sleep for 3 seconds to avoid trigger frequency limitation

quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
39 39 [ stock_code:HK.08103  stock_name:hmvod Limited  cur_price:2.69  current_ratio(annual):4.413 ,  stock_code:HK.00376  stock_name:Yunfeng Financial  cur_price:2.96  current_ratio(annual):12.585 ,  stock_code:HK.09995  stock_name:RemeGen Co., Ltd.  cur_price:92.85  current_ratio(annual):16.054 ,  stock_code:HK.80737  stock_name:Shenzhen Investment Holdings Bay Area Development  cur_price:2.8  current_ratio(annual):17.249 ,  stock_code:HK.00737  stock_name:Shenzhen Investment Holdings Bay Area Development  cur_price:3.25  current_ratio(annual):17.249 ,  stock_code:HK.03939  stock_name:Wanguo International Mining  cur_price:2.22  current_ratio(annual):17.323 ,  stock_code:HK.01055  stock_name:China Southern Airlines  cur_price:5.17  current_ratio(annual):17.529 ,  stock_code:HK.02638  stock_name:HK Electric Investments and HK Electric Investments  cur_price:7.68  current_ratio(annual):21.255 ,  stock_code:HK.00670  stock_name:China Eastern Airlines Corporation  cur_price:3.53  current_ratio(annual):25.194 ,  stock_code:HK.01952  stock_name:Everest Medicines  cur_price:69.5  current_ratio(annual):26.029 ,  stock_code:HK.00089  stock_name:Tai Sang Land Development  cur_price:4.22  current_ratio(annual):26.914 ,  stock_code:HK.00728  stock_name:China Telecom Corporation  cur_price:2.84  current_ratio(annual):27.651 ,  stock_code:HK.01372  stock_name:Bisu Technology Group  cur_price:5.63  current_ratio(annual):28.303 ,  stock_code:HK.00753  stock_name:Air China Limited  cur_price:6.37  current_ratio(annual):31.828 ,  stock_code:HK.01997  stock_name:Wharf Real Estate Investment  cur_price:44.15  current_ratio(annual):33.239 ,  stock_code:HK.02158  stock_name:Yidu Tech Inc.  cur_price:38.95  current_ratio(annual):34.046 ,  stock_code:HK.02588  stock_name:BOC Aviation Ltd.  cur_price:76.85  current_ratio(annual):34.531 ,  stock_code:HK.01330  stock_name:Dynagreen Environmental Protection Group  cur_price:3.36  current_ratio(annual):35.028 ,  stock_code:HK.01525  stock_name:SHANGHAI GENCH EDUCATION GROUP LIMITED  cur_price:6.28  current_ratio(annual):36.989 ,  stock_code:HK.09908  stock_name:JiaXing Gas Group  cur_price:10.02  current_ratio(annual):37.848 ,  stock_code:HK.06078  stock_name:Hygeia Healthcare Holdings  cur_price:49.2  current_ratio(annual):39.0 ,  stock_code:HK.01071  stock_name:Huadian Power International Corporation  cur_price:2.16  current_ratio(annual):39.507 ,  stock_code:HK.00357  stock_name:Hainan Meilan International Airport  cur_price:33.65  current_ratio(annual):39.514 ,  stock_code:HK.00762  stock_name:China Unicom  cur_price:5.21  current_ratio(annual):40.74 ,  stock_code:HK.01787  stock_name:Shandong Gold Mining  cur_price:15.62  current_ratio(annual):41.604 ,  stock_code:HK.00902  stock_name:Huaneng Power International,Inc.  cur_price:2.67  current_ratio(annual):42.919 ,  stock_code:HK.00934  stock_name:Sinopec Kantons  cur_price:2.98  current_ratio(annual):43.361 ,  stock_code:HK.01117  stock_name:China Modern Dairy  cur_price:2.29  current_ratio(annual):45.037 ,  stock_code:HK.00177  stock_name:Jiangsu Expressway  cur_price:8.78  current_ratio(annual):45.93 ,  stock_code:HK.01379  stock_name:Wenling Zhejiang Measuring and Cutting Tools Trading Centre Company Limited*  cur_price:5.71  current_ratio(annual):46.774 ,  stock_code:HK.01876  stock_name:Budweiser Brewing Company APAC Limited  cur_price:22.45  current_ratio(annual):46.917 ,  stock_code:HK.01907  stock_name:China Risun  cur_price:4.38  current_ratio(annual):47.129 ,  stock_code:HK.02160  stock_name:MicroPort CardioFlow Medtech Corporation  cur_price:15.52  current_ratio(annual):47.384 ,  stock_code:HK.00293  stock_name:Cathay Pacific Airways  cur_price:7.13  current_ratio(annual):47.983 ,  stock_code:HK.00694  stock_name:Beijing Capital International Airport  cur_price:6.29  current_ratio(annual):47.985 ,  stock_code:HK.09922  stock_name:Jiumaojiu International Holdings Limited  cur_price:26.8  current_ratio(annual):48.278 ,  stock_code:HK.01083  stock_name:Towngas China  cur_price:3.38  current_ratio(annual):49.2 ,  stock_code:HK.00291  stock_name:China Resources Beer  cur_price:58.2  current_ratio(annual):49.229 ,  stock_code:HK.00306  stock_name:Kwoon Chung Bus  cur_price:2.29  current_ratio(annual):49.769 ]
HK.08103
hmvod Limited
2.69
2.69
4.413
...
HK.00306
Kwoon Chung Bus
2.29
2.29
49.769
```









## <a href="#2109-2" class="header-anchor">#</a> Qot_StockFilter.proto

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the moomoo API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

* **Parameter**

```protobuf
// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10 
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3215





`uint StockFilter(QotStockFilter.Request req);`  
`virtual void OnReply_StockFilter(MMAPI_Conn client, uint nSerialNo, QotStockFilter.Response rsp);`

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the moomoo API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: MMSPI_Qot, MMSPI_Conn {
    MMAPI_Qot qot = new MMAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
        qot.SetQotCallback(this); //Set transaction callback
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        QotStockFilter.BaseFilter filter = QotStockFilter.BaseFilter.CreateBuilder()
                .SetFieldName(QotStockFilter.StockField.StockField_CurPrice)
                .SetFilterMax(100)
                .SetFilterMax(200)
                .Build();
        QotStockFilter.C2S c2s = QotStockFilter.C2S.CreateBuilder()
                .SetBegin(0)
                .SetNum(10)
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .AddBaseFilterList(filter)
            .Build();
        QotStockFilter.Request req = QotStockFilter.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.StockFilter(req);
        Console.Write("Send QotStockFilter: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_StockFilter(MMAPI_Conn client, uint nSerialNo, QotStockFilter.Response rsp)
    {
        Console.Write("Reply: QotStockFilter: {0}\n", nSerialNo, rsp.ToString());
        Console.Write("code: {0}, name: {1} \n", rsp.S2C.DataListList[0].Security.Code,
            rsp.S2C.DataListList[0].Name);
    }

    public static void Main(String[] args) {
        MMAPI.Init();
        Program qot = new Program();
        qot.Start();


        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
Qot onInitConnect: ret=0 desc= connID=6825721743616225277
Send QotStockFilter: 3
Reply: QotStockFilter: 3
code: 00376, name: Yunfeng Financial
```









`int stockFilter(QotStockFilter.Request req);`  
`void onReply_StockFilter(MMAPI_Conn client, int nSerialNo, QotStockFilter.Response rsp);`

- **Description**

  Filter stocks by condition

- **Parameter**



``` protobuf
// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
        qot.setQotSpi(this); //Set transaction callback
    }

    public void start() {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        QotStockFilter.BaseFilter filter = QotStockFilter.BaseFilter.newBuilder()
                .setFieldName(QotStockFilter.StockField.StockField_CurPrice_VALUE)
                .setFilterMax(100)
                .setFilterMax(200)
                .build();
        QotStockFilter.C2S c2s = QotStockFilter.C2S.newBuilder()
                .setBegin(0)
                .setNum(10)
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .addBaseFilterList(filter)
            .build();
        QotStockFilter.Request req = QotStockFilter.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.stockFilter(req);
        System.out.printf("Send QotStockFilter: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_StockFilter(MMAPI_Conn client, int nSerialNo, QotStockFilter.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotStockFilter failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotStockFilter: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        MMAPI.init();
        QotDemo qot = new QotDemo();
        qot.start();

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
Send QotStockFilter: 2
Receive QotStockFilter: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "lastPage": false,
    "allCount": 2431,
    "dataList": [{
      "security": {
        "market": 1,
        "code": "08560"
      },
      "name": "Great World"
    }, ... {
      "security": {
        "market": 1,
        "code": "02171"
      },
      "name": "CARsgen Therapeutics"
    }]
  }
}
```









`moomoo::u32_t StockFilter(const Qot_StockFilter::Request &stReq);`  
`virtual void OnReply_StockFilter(moomoo::u32_t nSerialNo, const Qot_StockFilter::Response &stRsp) = 0;`

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the moomoo API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cpp
class Program : public MMSPI_Qot, public MMSPI_Trd, public MMSPI_Conn
{
public:

    Program() {
        m_pQotApi = MMAPI::CreateQotApi();
        m_pQotApi->RegisterQotSpi(this);
        m_pQotApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pQotApi != nullptr)
        {
            m_pQotApi->UnregisterQotSpi();
            m_pQotApi->UnregisterConnSpi();
            MMAPI::ReleaseQotApi(m_pQotApi);
            m_pQotApi = nullptr;
        }
    }

    void Start() {
        m_pQotApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(MMAPI_Conn* pConn, moomoo::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Qot_StockFilter::Request req;
        Qot_StockFilter::C2S *c2s = req.mutable_c2s();
        c2s->set_begin(0);
        c2s->set_num(50);
        c2s->set_market(1);
        
        m_StockFilterSerialNo = m_pQotApi->StockFilter(req);
        cout << "Request StockFilter SerialNo: " << m_StockFilterSerialNo << endl;
    }

    virtual void OnReply_StockFilter(moomoo::u32_t nSerialNo, const Qot_StockFilter::Response &stRsp){
        if(nSerialNo == m_StockFilterSerialNo)
        {
            cout << "OnReply_StockFilter SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_StockFilterSerialNo;
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
Request StockFilter SerialNo: 4
OnReply_StockFilter SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "lastPage": false,
  "allCount": 2426,
  "dataList": [
   {
    "security": {
     "market": 1,
     "code": "02930"
    },
    "name": "Silk Road Logistics"
   },
...
   {
    "security": {
     "market": 1,
     "code": "01440"
    },
    "name": "Deyun Holding Ltd."
   }
  ]
 }
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)





`StockFilter(req);`

- **Description**

  Filter stocks by condition

- **Parameters**



``` protobuf
// Users who use the following 6 structures (BaseFilter, AccumulateFilter, FinancialFilter, BaseData, AccumulateData, FinancialData) please note that because the attribute field name "field" conflicts with the C # protobuf reserved function name, the moomoo API will change from 3.18 The version began to rename this field to "fieldName". Please pay attention to modify the field name used in the corresponding interface.

// Simple attribute filtering
message BaseFilter
{
    required int32 fieldName = 1; //Simple filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
}

// Cumulative attribute filtering
message AccumulateFilter
{
    required int32 fieldName = 1; //Cumulative filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 days = 6; //Recent days, cumulative time
}

// Financial attribute filtering
message FinancialFilter
{
    required int32 fieldName = 1; //Financial filter properties
    optional double filterMin = 2; //The lower limit of the interval (closed-interval). Default is -∞ if not passed
    optional double filterMax = 3; //The upper limit of the interval (closed-interval). Default is +∞ if not passed
    optional bool isNoFilter = 4; //Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 sortDir = 5; //Sort direction. No sorting by default, if not passed
    required int32 quarter = 6; //Financial report accumulation time
}

// Pattern attribute filtering
message PatternFilter
{
    required int32 fieldName = 1; // Pattern filter properties
    required int32 klType = 2; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    optional bool isNoFilter = 3; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    optional int32 consecutivePeriod = 4; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

// Custom indicator attribute filtering
message CustomIndicatorFilter
{
    required int32 firstFieldName = 1; // Custom indicator filter properties 
    required int32 secondFieldName = 2; // Custom indicator filter properties
    required int32 relativePosition = 3; // Relative position
    optional double fieldValue = 4; // Custom value
    required int32 klType = 5; // K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods   
    optional bool isNoFilter = 6; // Whether the field does not require filtering. True: no filtering, False: filtering. No filtering by default, if not passed
    repeated int32 firstFieldParaList = 7; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    repeated int32 secondFieldParaList = 8; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
    optional int32 consecutivePeriod = 9; // Filters data whose consecutive periods are all eligible. Fill in the range [1,12]
}

message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 market= 3; //Qot_Common::QotMarket. Stock market. does not distinguish between Shanghai and Shenzhen market, either of Shanghai or Shenzhen market will represent the A-share market
    // The following are optional fields of filter conditions, leave it blank means no filter
    optional Qot_Common.Security plate = 4; //Plate
    repeated BaseFilter baseFilterList = 5; //Simple filter properties
    repeated AccumulateFilter accumulateFilterList = 6; //Cumulative filter properties The maximum number of the same filter condition for cumulative filter properties is 10
    repeated FinancialFilter financialFilterList = 7; //Financial filter properties
    repeated PatternFilter patternFilterList = 8; // Indicator pattern filter properties
    repeated CustomIndicatorFilter customIndicatorFilterList = 9; // Custom indicator filter properties
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - For pattern filter properties, refer to
>   [PatternField](/moomoo-api-doc/en/quote/quote.html#6605)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For sorting direction, refer to
>   [SortDir](/moomoo-api-doc/en/quote/quote.html#9029)
> - Relative position, refer to
>   [RelativePosition](/moomoo-api-doc/en/quote/quote.html#9084)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf

// Simple attribute data
message BaseData
{
    required int32 fieldName = 1; //Simple filter properties
    required double value = 2;
}

// Cumulative attribute data
message AccumulateData
{
    required int32 fieldName = 1; //Cumulative filter properties
    required double value = 2;
    required int32 days = 3; //Recent days, cumulative time
}

// Financial attribute data
message FinancialData
{
    required int32 fieldName = 1; //Financial filter properties
    required double value = 2;
    required int32 quarter = 3; //Financial report accumulation time
}

// Custom indicator data
message CustomIndicatorData
{
    required int32 fieldName = 1; // CustomIndicatorField. Custom indicator filter properties 
    required double value = 2; 
    required int32 klType = 3; // Qot_Common.KLType. K line type, only supports K_60M, K_DAY, K_WEEK, K_MON four time periods
    repeated int32 fieldParaList = 4; // Custom indicator parameter. Pass parameters according to the indicator type: 1. MA：[Average moving period] 2.EMA：[Exponential moving average period] 3.RSI：[RSI period] 4.MACD：[Fast average, Slow average, DIF value] 5.BOLL：[Average period, Offset value] 6.KDJ：[RSV period, K value period, D value period]
}

// returned stock data
message StockData
{
    required Qot_Common.Security security = 1; //Security
    required string name = 2; //Security name
    repeated BaseData baseDataList = 3; //Filtered data of simple filter property
    repeated AccumulateData accumulateDataList = 4; //Filtered data of cumulative filter property
    repeated FinancialData financialDataList = 5; //Filtered data of financial filter property
    repeated CustomIndicatorData customIndicatorDataList = 6; // Filtered data of custom indicator filter property
    // The value of firstFieldName and secondFieldName field in CustomIndicatorFilter will be returned seperately
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: It is not the last page, and some remaining warrant record has not been returned; true: It is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated StockData dataList = 3; //Returned stock data list
}

message Response
{
    required int32 retType = 1 [default = -400]; // RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For simple attribute filter conditions, refer to
>   [StockField](/moomoo-api-doc/en/quote/quote.html#9377)
> - For cumulative filter properties, refer to
>   [AccumulateField](/moomoo-api-doc/en/quote/quote.html#8316)
> - For financial filter properties, refer to
>   [FinancialField](/moomoo-api-doc/en/quote/quote.html#2317)
> - For financial report time period, refer to
>   [FinancialQuarter](/moomoo-api-doc/en/quote/quote.html#8409)
> - For custom indicator filter properties, refer to
>   [CustomIndicatorField](/moomoo-api-doc/en/quote/quote.html#3936)
> - K line type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotStockFilter(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    begin: 0, 
                    num: 2,
                    market: QotMarket.QotMarket_HK_Security,
                },
            };

            websocket.StockFilter(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("StockFilter: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
StockFilter: errCode 0, retMsg , retType 0
{
  "lastPage": false,
  "allCount": 2438,
  "dataList": [{
    "security": {
      "market": 1,
      "code": "02969"
    },
    "name": "LAI SUN DEV RTS"
  }, {
    "security": {
      "market": 1,
      "code": "08580"
    },
    "name": "Luen Wong Group"
  }]
}
stop
```











Tips

- Use [Get sub-plate list
  function](/moomoo-api-doc/en/quote/get-plate-list.html) to get the
  sub-plate code, the plates supported by conditional stock selection
  are respectively
  1.  The industry plate and concept plate of HK market.
  2.  Industry plate of US market.
  3.  Shanghai and Shenzhen's industry plate, conceptual plate and
      geographic plate.
- Supported plate index codes
  | Code           | Description                           |
  |:---------------|:--------------------------------------|
  | HK.Motherboard | Main plate of HK market               |
  | HK.GEM         | Growth Enterprise Market of HK market |
  | HK.BK1911      | Main plate of H-Share                 |
  | HK.BK1912      | Growth Enterprise Market of H-share   |
  | US.NYSE        | New York Stock Exchange               |
  | US.AMEX        | American Exchange                     |
  | US.NASDAQ      | NASDAQ                                |
  | SH.3000000     | Shanghai main plate                   |
  | SZ.3000001     | Shenzhen main plate                   |
  | SZ.3000004     | Shenzhen Growth Enterprise Market     |





Interface Limitations

- A maximum of 10 requests per 30 seconds
- At most 200 filter results are returned per page
- It is recommended that the filter conditions do not exceed 250,
  otherwise "business processing timeout did not return" may appear
- The maximum number of the same filter condition for cumulative filter
  properties is 10
- If you use dynamic data such as "current price" as the sorting field,
  the sorting of the data may change between multiple pages
- Non-similar indicators do not support comparison, and are limited to
  the establishment of comparison relationships between similar
  indicators, and comparisons across different types of indicators will
  cause errors. For example: MA5 and MA10 can establish a relationship.
  MA5 and EMA10 cannot establish a relationship.
- The same type of filter conditions of the custom indicator attribute
  exceeds the upper limit of 10
- Simple attributes, financial attributes, and morphological attributes
  do not support repeated designation of filter conditions for the same
  field
- Stock filter function currently does not support irregular trading
  hours (i.e.pre-market, post-market and overnight). All results are
  based on regular trading hours data.













