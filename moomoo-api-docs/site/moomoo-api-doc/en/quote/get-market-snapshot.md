



# <a href="#8048" class="header-anchor">#</a> Get Market Snapshot









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_market_snapshot(code_list)`

- **Description**

  Get market snapshot

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
  <td style="text-align: left;">code_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Stock list
  
    
  
  
   
  
  Up to 400 targets can be requested each time.<br />
  Data type of elements in the list is str.
  
  
  
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
  <td>If ret == RET_OK, stock snapshot data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock snapshot data format as follows:
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
    <td style="text-align: left;">code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">update_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Current update time.
    
      
    
    
     
    
    yyyy-MM-dd HH:mm:ss.<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Latest price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">open_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">prev_close_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is suspended or not.
    
      
    
    
     
    
    True: suspension.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date.
    
      
    
    
     
    
    yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">equity_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is stock or not.
    
      
    
    
     
    
    The following equity-related fields will be legal only if this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">issued_shares</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total shares.</td>
    </tr>
    <tr>
    <td style="text-align: left;">total_market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total market value.
    
      
    
    
     
    
    Unit: yuan
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_asset</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net asset value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">net_profit</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net profit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">earning_per_share</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Earnings per share.</td>
    </tr>
    <tr>
    <td style="text-align: left;">outstanding_shares</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Shares outstanding.</td>
    </tr>
    <tr>
    <td style="text-align: left;">net_asset_per_share</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Net assets per share.</td>
    </tr>
    <tr>
    <td style="text-align: left;">circular_market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Circulation market value.
    
      
    
    
     
    
    Unit: yuan
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ey_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yield rate.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pb_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/B ratio.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ttm_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio TTM.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_ttm</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend TTM, dividend.</td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_ratio_ttm</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend rate TTM.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_lfy</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend LFY, dividend of the previous
    year.</td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_lfy_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend rate LFY.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The code of the underlying stock to which
    the warrant belongs or the code of the underlying stock of the
    option.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is warrant or not.
    
      
    
    
     
    
    The following warrant related fields will be legal if this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_conversion_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
    <td style="text-align: left;">Warrant type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_maturity_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Maturity date.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_end_trade</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_leverage</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Leverage ratio.
    
      
    
    
     
    
    Unit: times
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_ipop</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">in/out of the money.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_break_even_point</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Breakeven point.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_conversion_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_price_recovery_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Price recovery ratio.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_score</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Comprehensive score of warrant.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The underlying stock of the warrant (This
    field has been deprecated and changed to stock_owner.).</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_recovery_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant recovery price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_street_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant Outstanding quantity.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_issue_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant issuance.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_street_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outstanding percentage.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_delta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Delta value of warrant.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_implied_volatility</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant implied volatility.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant premium.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_upper_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Upper bound price.
    
      
    
    
     
    
    Only Inline Warrant supports this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_lower_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">lower bound price.
    
      
    
    
     
    
    Only Inline Warrant supports this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_inline_price_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9794">PriceType</a></td>
    <td style="text-align: left;">in/out of bounds
    
      
    
    
     
    
    Only Inline Warrant supports this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_issuer_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Issuer code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is option or not.
    
      
    
    
     
    
    The following option related fields will be legal when this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
    <td style="text-align: left;">Option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The option exercise date.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_contract_size</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Number of stocks per contract.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total open contract number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_implied_volatility</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Implied volatility.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Premium.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_delta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Delta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_gamma</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Gamma.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_vega</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Vega.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_theta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Theta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_rho</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Rho.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
    <td style="text-align: left;">Index option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_net_open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net open contract number.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_expiry_date_distance</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of days from the expiry date, a
    negative number means it has expired.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_contract_nominal_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract nominal amount.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_owner_lot_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Equal number of underlying stocks.
    
      
    
    
     
    
    Index options do not have this field, only HK options support this
    field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_area_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3628">OptionAreaType</a></td>
    <td style="text-align: left;">Option type (by exercise time).</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_contract_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract multiplier.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is plate or not.
    
      
    
    
     
    
    The following plate related fields will be legal when this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_raise_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that raises in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_fall_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that falls in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_equal_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that dose not change in
    price in the plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is index or not.
    
      
    
    
     
    
    The following index related fields will be legal when this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">index_raise_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that raises in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_fall_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that falls in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_equal_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that dose not change in
    the plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of shares per lot, stock
    options represent the number of shares per contract
    
      
    
    
     
    
    Index options do not have this field.
    
    
    
    
    , and futures represent contract multipliers.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_spread</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The current upward price difference.
    
      
    
    
     
    
    That is, the quotation difference between ask price and sell 1.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Ask price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bid price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Ask volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bid volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">enable_margin</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether financing is available
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mortgage_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Stock mortgage rate (Deprecated).</td>
    </tr>
    <tr>
    <td style="text-align: left;">long_margin_initial_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The initial margin rate of financing
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">enable_short_sell</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether short-selling is available
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_sell_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short-selling reference rate (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_available_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Remaining quantity that can be sold short
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_margin_initial_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The initial margin rate for short selling
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sec_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#4415">SecurityStatus</a></td>
    <td style="text-align: left;">Stock status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_ask_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The Committee.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">volume_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Volume ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">highest52weeks_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest price in 52 weeks.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lowest52weeks_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest price in 52 weeks .</td>
    </tr>
    <tr>
    <td style="text-align: left;">highest_history_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest historical price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lowest_history_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest historical price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Pre-market volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest price after-hours.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest price after-hours.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">After-hours trading volume.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours turnover.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Overnight volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">future_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is futures or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_last_settle_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_position</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Holding position.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_position_change</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Change in position.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is future main contract or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The last trading time.
    
      
    
    
     
    
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is fund or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_dividend_yield</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_aum</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Asset scale.
    
      
    
    
     
    
    Unit: yuan
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_outstanding_units</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total circulation.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_netAssetValue</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Net asset value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Premium.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_assetClass</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#4696">AssetClass</a></td>
    <td style="text-align: left;">Asset class.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_market_snapshot(['HK.00700', 'US.AAPL'])
if ret == RET_OK:
    print(data)
    print(data['code'][0])    # Take the first stock code
    print(data['code'].values.tolist())   # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
   code  name              update_time  last_price  open_price  high_price  low_price  prev_close_price     volume      turnover  turnover_rate  suspension listing_date  lot_size  price_spread  stock_owner  ask_price  bid_price  ask_vol  bid_vol  enable_margin  mortgage_ratio  long_margin_initial_ratio  enable_short_sell  short_sell_rate  short_available_volume  short_margin_initial_ratio  amplitude  avg_price  bid_ask_ratio  volume_ratio  highest52weeks_price  lowest52weeks_price  highest_history_price  lowest_history_price  close_price_5min  after_volume  after_turnover sec_status  equity_valid  issued_shares  total_market_val     net_asset    net_profit  earning_per_share  outstanding_shares  circular_market_val  net_asset_per_share  ey_ratio  pe_ratio  pb_ratio  pe_ttm_ratio  dividend_ttm  dividend_ratio_ttm  dividend_lfy  dividend_lfy_ratio  wrt_valid  wrt_conversion_ratio wrt_type  wrt_strike_price  wrt_maturity_date  wrt_end_trade  wrt_recovery_price  wrt_street_vol  \
0  HK.00700  TENCENT      2025-04-07 16:09:07      435.40      441.80      462.40     431.00            497.80  123364114  5.499476e+10          1.341       False   2004-06-16       100          0.20          NaN      435.4     435.20   281300    17300            NaN             NaN                        NaN                NaN              NaN                     NaN                         NaN      6.308    445.792        -68.499         5.627             547.00000           294.400000             706.100065            -13.202011            431.60             0    0.000000e+00     NORMAL          True     9202391012      4.006721e+12  1.051300e+12  2.095753e+11             22.774          9202391012         4.006721e+12              114.242     0.199    19.118     3.811        19.118          3.48                0.80          3.48               0.799      False                   NaN      N/A               NaN                NaN            NaN                 NaN             NaN   
1   US.AAPL    APPLE  2025-04-07 05:30:43.301      188.38      193.89      199.88     187.34            203.19  125910913  2.424473e+10          0.838       False   1980-12-12         1          0.01          NaN      180.8     180.48       29      400            NaN             NaN                        NaN                NaN              NaN                     NaN                         NaN      6.172    192.554         86.480         2.226             259.81389           163.300566             259.813890              0.053580            188.93       3151311    5.930968e+08     NORMAL          True    15022073000      2.829858e+12  6.675809e+10  9.133420e+10              6.080         15016677308         2.828842e+12                4.444     1.417    30.983    42.389        29.901          0.99                0.53          0.98               0.520      False                   NaN      N/A               NaN                NaN            NaN                 NaN             NaN   

   wrt_issue_vol  wrt_street_ratio  wrt_delta  wrt_implied_volatility  wrt_premium  wrt_leverage  wrt_ipop  wrt_break_even_point  wrt_conversion_price  wrt_price_recovery_ratio  wrt_score  wrt_upper_strike_price  wrt_lower_strike_price wrt_inline_price_status  wrt_issuer_code  option_valid option_type  strike_time  option_strike_price  option_contract_size  option_open_interest  option_implied_volatility  option_premium  option_delta  option_gamma  option_vega  option_theta  option_rho  option_net_open_interest  option_expiry_date_distance  option_contract_nominal_value  option_owner_lot_multiplier option_area_type  option_contract_multiplier index_option_type  index_valid  index_raise_count  index_fall_count  index_equal_count  plate_valid  plate_raise_count  plate_fall_count  plate_equal_count  future_valid  future_last_settle_price  future_position  future_position_change  future_main_contract  future_last_trade_time  trust_valid  trust_dividend_yield  trust_aum  \
0            NaN               NaN        NaN                     NaN          NaN           NaN       NaN                   NaN                   NaN                       NaN        NaN                     NaN                     NaN                     N/A              NaN         False         N/A          NaN                  NaN                   NaN                   NaN                        NaN             NaN           NaN           NaN          NaN           NaN         NaN                       NaN                          NaN                            NaN                          NaN              N/A                         NaN               N/A        False                NaN               NaN                NaN        False                NaN               NaN                NaN         False                       NaN              NaN                     NaN                   NaN                     NaN        False                   NaN        NaN   
1            NaN               NaN        NaN                     NaN          NaN           NaN       NaN                   NaN                   NaN                       NaN        NaN                     NaN                     NaN                     N/A              NaN         False         N/A          NaN                  NaN                   NaN                   NaN                        NaN             NaN           NaN           NaN          NaN           NaN         NaN                       NaN                          NaN                            NaN                          NaN              N/A                         NaN               N/A        False                NaN               NaN                NaN        False                NaN               NaN                NaN         False                       NaN              NaN                     NaN                   NaN                     NaN        False                   NaN        NaN   

   trust_outstanding_units  trust_netAssetValue  trust_premium trust_assetClass pre_price pre_high_price pre_low_price pre_volume pre_turnover pre_change_val pre_change_rate pre_amplitude after_price after_high_price after_low_price after_change_val after_change_rate after_amplitude overnight_price overnight_high_price overnight_low_price overnight_volume overnight_turnover overnight_change_val overnight_change_rate overnight_amplitude  
0                      NaN                  NaN            NaN              N/A       N/A            N/A           N/A        N/A          N/A            N/A             N/A           N/A         N/A              N/A             N/A              N/A               N/A             N/A             N/A                  N/A                 N/A              N/A                N/A                  N/A                   N/A                 N/A  
1                      NaN                  NaN            NaN              N/A    180.68         181.98        177.47     276016  49809244.83           -7.7          -4.087         2.394       186.6          188.639          186.44            -1.78            -0.944          1.1673          176.94                186.5               174.4           533115        94944250.56               -11.44                -6.072              6.4231  
HK.00700
['HK.00700', 'US.AAPL']
```









## <a href="#338" class="header-anchor">#</a> Qot_GetSecuritySnapshot.proto

- **Description**

  Get snapshot data

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3203





`uint GetSecuritySnapshot(QotGetSecuritySnapshot.Request req);`  
`virtual void OnReply_GetSecuritySnapshot(FTAPI_Conn client, uint nSerialNo, QotGetSecuritySnapshot.Response rsp);`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Qot, FTSPI_Conn {
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetSecuritySnapshot.C2S c2s = QotGetSecuritySnapshot.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetSecuritySnapshot.Request req = QotGetSecuritySnapshot.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetSecuritySnapshot(req);
        Console.Write("Send QotGetSecuritySnapshot: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetSecuritySnapshot(FTAPI_Conn client, uint nSerialNo, QotGetSecuritySnapshot.Response rsp)
    {
        Console.Write("Reply: QotGetSecuritySnapshot: {0} \n", nSerialNo);
        Console.Write("basic price: {0}\n", rsp.S2C.SnapshotListList[0].Basic.CurPrice);
        Console.Write("equityExData issuedShares: {0}\n", rsp.S2C.SnapshotListList[0].EquityExData.IssuedShares);
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
Qot onInitConnect: ret=0 desc= connID=6825619056039643630
Send QotGetSecuritySnapshot: 3
Reply: QotGetSecuritySnapshot: 3
basic price: 474.2
equityExData issuedShares: 9595900007
```









`int getSecuritySnapshot(QotGetSecuritySnapshot.Request req);`  
`void onReply_GetSecuritySnapshot(FTAPI_Conn client, int nSerialNo, QotGetSecuritySnapshot.Response rsp);`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
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

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetSecuritySnapshot.C2S c2s = QotGetSecuritySnapshot.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetSecuritySnapshot.Request req = QotGetSecuritySnapshot.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getSecuritySnapshot(req);
        System.out.printf("Send QotGetSecuritySnapshot: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetSecuritySnapshot(FTAPI_Conn client, int nSerialNo, QotGetSecuritySnapshot.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetSecuritySnapshot failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetSecuritySnapshot: %s\n", json);
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
Send QotGetSecuritySnapshot: 2
Receive QotGetSecuritySnapshot: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "snapshotList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "00700"
        },
        "type": 3,
        "isSuspend": false,
        "listTime": "2004-06-16",
        "lotSize": 100,
        "priceSpread": 0.5,
        "updateTime": "2021-06-24 16:08:14",
        "highPrice": 587.5,
        "openPrice": 584.0,
        "lowPrice": 580.0,
        "lastClosePrice": 582.5,
        "curPrice": 583.0,
        "volume": "10947302",
        "turnover": 6.387238277E9,
        "turnoverRate": 0.114,
        "listTimestamp": 1.0873152E9,
        "updateTimestamp": 1.624522094E9,
        "askPrice": 583.5,
        "bidPrice": 583.0,
        "askVol": "142300",
        "bidVol": "52800",
        "enableMargin": true,
        "mortgageRatio": 0.0,
        "longMarginInitialRatio": 35.0,
        "enableShortSell": true,
        "shortSellRate": 0.9,
        "shortAvailableVolume": "2006700",
        "shortMarginInitialRatio": 60.0,
        "amplitude": 1.288,
        "avgPrice": 583.453,
        "bidAskRatio": -5.273,
        "volumeRatio": 0.553,
        "highest52WeeksPrice": 773.9,
        "lowest52WeeksPrice": 479.4,
        "highestHistoryPrice": 773.9,
        "lowestHistoryPrice": -6.381,
        "secStatus": 1,
        "closePrice5Minute": 583.5
      },
      "equityExData": {
        "issuedShares": "9595206625",
        "issuedMarketVal": 5.594005462375E12,
        "netAsset": 9.17675966408375E11,
        "netProfit": 1.90378494646625E11,
        "earningsPershare": 19.841,
        "outstandingShares": "9595206625",
        "outstandingMarketVal": 5.594005462375E12,
        "netAssetPershare": 95.639,
        "eyRate": 0.232,
        "peRate": 29.383,
        "pbRate": 6.095,
        "peTTMRate": 26.249,
        "dividendTTM": 1.6,
        "dividendRatioTTM": 0.27,
        "dividendLFY": 1.6,
        "dividendLFYRatio": 0.274
      }
    }]
  }
}
```









`Futu::u32_t GetSecuritySnapshot(const Qot_GetSecuritySnapshot::Request &stReq);`  
`virtual void OnReply_GetSecuritySnapshot(Futu::u32_t nSerialNo, const Qot_GetSecuritySnapshot::Response &stRsp) = 0;`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
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
        Qot_GetSecuritySnapshot::Request req;
        Qot_GetSecuritySnapshot::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetSecuritySnapshotSerialNo = m_pQotApi->GetSecuritySnapshot(req);
        cout << "Request GetSecuritySnapshot SerialNo: " << m_GetSecuritySnapshotSerialNo << endl;
    }

    virtual void OnReply_GetSecuritySnapshot(Futu::u32_t nSerialNo, const Qot_GetSecuritySnapshot::Response &stRsp){
        if(nSerialNo == m_GetSecuritySnapshotSerialNo)
        {
            cout << "OnReply_GetSecuritySnapshot SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            // ProtoBufToBodyData和UTF8ToLocal函数的定义参见Sample中的tool.h文件
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetSecuritySnapshotSerialNo;
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
Request GetSecuritySnapshot SerialNo: 4
OnReply_GetSecuritySnapshot SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "snapshotList": [
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "00700"
     },
     "type": 3,
     "isSuspend": false,
     "listTime": "2004-06-16",
     "lotSize": 100,
     "priceSpread": 0.5,
     "updateTime": "2021-06-09 14:12:30",
     "highPrice": 606,
     "openPrice": 600,
     "lowPrice": 597.5,
     "lastClosePrice": 601,
     "curPrice": 600.5,
     "volume": "4382292",
     "turnover": 2638928979,
     "turnoverRate": 0.046,
     "listTimestamp": 1087315200,
     "updateTimestamp": 1623219150,
     "askPrice": 601,
     "bidPrice": 600.5,
     "askVol": "24200",
     "bidVol": "1400",
     "enableMargin": true,
     "mortgageRatio": 0,
     "longMarginInitialRatio": 35,
     "enableShortSell": true,
     "shortSellRate": 0.9,
     "shortAvailableVolume": "1860000",
     "shortMarginInitialRatio": 60,
     "amplitude": 1.414,
     "avgPrice": 602.18,
     "bidAskRatio": 38.289,
     "volumeRatio": 0.418,
     "highest52WeeksPrice": 773.9,
     "lowest52WeeksPrice": 430.6,
     "highestHistoryPrice": 773.9,
     "lowestHistoryPrice": -6.381,
     "secStatus": 1,
     "closePrice5Minute": 601.5
    },
    "equityExData": {
     "issuedShares": "9595206625",
     "issuedMarketVal": 5761921578312.5,
     "netAsset": 917675966408.375,
     "netProfit": 190378494646.625,
     "earningsPershare": 19.841,
     "outstandingShares": "9595206625",
     "outstandingMarketVal": 5761921578312.5,
     "netAssetPershare": 95.639,
     "eyRate": 0.232,
     "peRate": 30.265,
     "pbRate": 6.278,
     "peTTMRate": 27.037,
     "dividendTTM": 1.6,
     "dividendRatioTTM": 0.27,
     "dividendLFY": 1.6,
     "dividendLFYRatio": 0.266
    }
   }
  ]
 }
}
```









`GetSecuritySnapshot(req);`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetSecuritySnapshot(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) {

            const req = {
                c2s: {
                securityList: [
                    {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                ],
                },
            };
            websocket.GetSecuritySnapshot(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("Snapshot: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                if(retType == RetType.RetType_Succeed){
                    let snapshot = beautify(JSON.stringify(s2c), {
                        indent_size: 2,
                        space_in_empty_paren: true,
                    });
                    console.log(snapshot);
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
Snapshot: errCode 0, retMsg , retType 0
{
  "snapshotList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "00700"
      },
      "type": 3,
      "isSuspend": false,
      "listTime": "2004-06-16",
      "lotSize": 100,
      "priceSpread": 0.2,
      "updateTime": "2021-09-09 16:08:17",
      "highPrice": 511.5,
      "openPrice": 509,
      "lowPrice": 479,
      "lastClosePrice": 524.5,
      "curPrice": 480,
      "volume": "54090872",
      "turnover": 26716845932,
      "turnoverRate": 0.563,
      "listTimestamp": 1087315200,
      "updateTimestamp": 1631174897,
      "askPrice": 480.4,
      "bidPrice": 480,
      "askVol": "700",
      "bidVol": "55300",
      "enableMargin": true,
      "mortgageRatio": 0,
      "longMarginInitialRatio": 35,
      "enableShortSell": true,
      "shortSellRate": 0.92,
      "shortAvailableVolume": "3059000",
      "shortMarginInitialRatio": 50,
      "amplitude": 6.196,
      "avgPrice": 493.925,
      "bidAskRatio": 22.703,
      "volumeRatio": 1.775,
      "highest52WeeksPrice": 773.9,
      "lowest52WeeksPrice": 412.2,
      "highestHistoryPrice": 773.9,
      "lowestHistoryPrice": -6.381,
      "secStatus": 1,
      "closePrice5Minute": 483.4
    },
    "equityExData": {
      "issuedShares": "9599810645",
      "issuedMarketVal": 4607909109600,
      "netAsset": 1016063158288.09,
      "netProfit": 190383444711.64,
      "earningsPershare": 19.832,
      "outstandingShares": "9599810645",
      "outstandingMarketVal": 4607909109600,
      "netAssetPershare": 105.842,
      "eyRate": 0.22,
      "peRate": 24.203,
      "pbRate": 4.535,
      "peTTMRate": 20.532,
      "dividendTTM": 1.599,
      "dividendRatioTTM": 0.33,
      "dividendLFY": 1.599,
      "dividendLFYRatio": 0.333
    }
  }]
}
stop
```











Interface Limitations

- Request up to 60 snapshots every 30 seconds
- For each request, the maximum number of stock codes supported by the
  parameter *code_list* is 400.
- Under the authority of Hong Kong stock BMP, the maximum number of
  snapshots of Hong Kong securities (including warrants, CBBC, and
  Inline Warrants) for a single request is 20
- Under the authority of Hong Kong futures and options BMP, the maximum
  number of snapshots of Hong Kong futures and options for a single
  request is 20











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_market_snapshot(code_list)`

- **Description**

  Get market snapshot

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
  <td style="text-align: left;">code_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Stock list
  
    
  
  
   
  
  Up to 400 targets can be requested each time.<br />
  Data type of elements in the list is str.
  
  
  
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
  <td>If ret == RET_OK, stock snapshot data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock snapshot data format as follows:
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
    <td style="text-align: left;">code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">update_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Current update time.
    
      
    
    
     
    
    yyyy-MM-dd HH:mm:ss.<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Latest price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">open_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">prev_close_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is suspended or not.
    
      
    
    
     
    
    True: suspension.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date.
    
      
    
    
     
    
    yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">equity_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is stock or not.
    
      
    
    
     
    
    The following equity-related fields will be legal only if this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">issued_shares</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total shares.</td>
    </tr>
    <tr>
    <td style="text-align: left;">total_market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total market value.
    
      
    
    
     
    
    Unit: yuan
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_asset</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net asset value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">net_profit</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net profit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">earning_per_share</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Earnings per share.</td>
    </tr>
    <tr>
    <td style="text-align: left;">outstanding_shares</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Shares outstanding.</td>
    </tr>
    <tr>
    <td style="text-align: left;">net_asset_per_share</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Net assets per share.</td>
    </tr>
    <tr>
    <td style="text-align: left;">circular_market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Circulation market value.
    
      
    
    
     
    
    Unit: yuan
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ey_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yield rate.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pb_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/B ratio.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ttm_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio TTM.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_ttm</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend TTM, dividend.</td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_ratio_ttm</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend rate TTM.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_lfy</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend LFY, dividend of the previous
    year.</td>
    </tr>
    <tr>
    <td style="text-align: left;">dividend_lfy_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend rate LFY.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The code of the underlying stock to which
    the warrant belongs or the code of the underlying stock of the
    option.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is warrant or not.
    
      
    
    
     
    
    The following warrant related fields will be legal if this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_conversion_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
    <td style="text-align: left;">Warrant type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_maturity_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Maturity date.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_end_trade</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_leverage</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Leverage ratio.
    
      
    
    
     
    
    Unit: times
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_ipop</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">in/out of the money.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_break_even_point</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Breakeven point.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_conversion_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_price_recovery_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Price recovery ratio.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_score</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Comprehensive score of warrant.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The underlying stock of the warrant (This
    field has been deprecated and changed to stock_owner.).</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_recovery_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant recovery price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_street_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant Outstanding quantity.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_issue_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant issuance.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_street_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outstanding percentage.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_delta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Delta value of warrant.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_implied_volatility</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant implied volatility.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Warrant premium.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_upper_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Upper bound price.
    
      
    
    
     
    
    Only Inline Warrant supports this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_lower_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">lower bound price.
    
      
    
    
     
    
    Only Inline Warrant supports this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_inline_price_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9794">PriceType</a></td>
    <td style="text-align: left;">in/out of bounds
    
      
    
    
     
    
    Only Inline Warrant supports this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_issuer_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Issuer code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is option or not.
    
      
    
    
     
    
    The following option related fields will be legal when this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
    <td style="text-align: left;">Option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The option exercise date.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_contract_size</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Number of stocks per contract.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total open contract number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_implied_volatility</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Implied volatility.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Premium.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_delta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Delta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_gamma</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Gamma.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_vega</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Vega.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_theta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Theta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_rho</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Rho.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
    <td style="text-align: left;">Index option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_net_open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net open contract number.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_expiry_date_distance</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of days from the expiry date, a
    negative number means it has expired.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_contract_nominal_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract nominal amount.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_owner_lot_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Equal number of underlying stocks.
    
      
    
    
     
    
    Index options do not have this field, only HK options support this
    field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_area_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3628">OptionAreaType</a></td>
    <td style="text-align: left;">Option type (by exercise time).</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_contract_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract multiplier.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is plate or not.
    
      
    
    
     
    
    The following plate related fields will be legal when this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_raise_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that raises in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_fall_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that falls in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_equal_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that dose not change in
    price in the plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is index or not.
    
      
    
    
     
    
    The following index related fields will be legal when this field is
    True.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">index_raise_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that raises in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_fall_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that falls in the
    plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_equal_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of stocks that dose not change in
    the plate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of shares per lot, stock
    options represent the number of shares per contract
    
      
    
    
     
    
    Index options do not have this field.
    
    
    
    
    , and futures represent contract multipliers.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_spread</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The current upward price difference.
    
      
    
    
     
    
    That is, the quotation difference between ask price and sell 1.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Ask price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bid price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Ask volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_vol</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bid volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">enable_margin</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether financing is available
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mortgage_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Stock mortgage rate (Deprecated).</td>
    </tr>
    <tr>
    <td style="text-align: left;">long_margin_initial_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The initial margin rate of financing
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">enable_short_sell</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether short-selling is available
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_sell_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short-selling reference rate (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_available_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Remaining quantity that can be sold short
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_margin_initial_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The initial margin rate for short selling
    (Deprecated).
    
      
    
    
     
    
    Please use <a href="/moomoo-api-doc/en/trade/get-margin-ratio.html">Get
    Margin Data</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sec_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#4415">SecurityStatus</a></td>
    <td style="text-align: left;">Stock status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_ask_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The Committee.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">volume_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Volume ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">highest52weeks_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest price in 52 weeks.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lowest52weeks_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest price in 52 weeks .</td>
    </tr>
    <tr>
    <td style="text-align: left;">highest_history_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest historical price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lowest_history_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest historical price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Pre-market volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest price after-hours.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest price after-hours.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">After-hours trading volume.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours turnover.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Overnight volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">future_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is futures or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_last_settle_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_position</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Holding position.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_position_change</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Change in position.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is future main contract or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The last trading time.
    
      
    
    
     
    
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is fund or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_dividend_yield</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_aum</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Asset scale.
    
      
    
    
     
    
    Unit: yuan
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_outstanding_units</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total circulation.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_netAssetValue</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Net asset value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Premium.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trust_assetClass</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#4696">AssetClass</a></td>
    <td style="text-align: left;">Asset class.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_market_snapshot(['HK.00700', 'US.AAPL'])
if ret == RET_OK:
    print(data)
    print(data['code'][0])    # Take the first stock code
    print(data['code'].values.tolist())   # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
   code  name              update_time  last_price  open_price  high_price  low_price  prev_close_price     volume      turnover  turnover_rate  suspension listing_date  lot_size  price_spread  stock_owner  ask_price  bid_price  ask_vol  bid_vol  enable_margin  mortgage_ratio  long_margin_initial_ratio  enable_short_sell  short_sell_rate  short_available_volume  short_margin_initial_ratio  amplitude  avg_price  bid_ask_ratio  volume_ratio  highest52weeks_price  lowest52weeks_price  highest_history_price  lowest_history_price  close_price_5min  after_volume  after_turnover sec_status  equity_valid  issued_shares  total_market_val     net_asset    net_profit  earning_per_share  outstanding_shares  circular_market_val  net_asset_per_share  ey_ratio  pe_ratio  pb_ratio  pe_ttm_ratio  dividend_ttm  dividend_ratio_ttm  dividend_lfy  dividend_lfy_ratio  wrt_valid  wrt_conversion_ratio wrt_type  wrt_strike_price  wrt_maturity_date  wrt_end_trade  wrt_recovery_price  wrt_street_vol  \
0  HK.00700  TENCENT      2025-04-07 16:09:07      435.40      441.80      462.40     431.00            497.80  123364114  5.499476e+10          1.341       False   2004-06-16       100          0.20          NaN      435.4     435.20   281300    17300            NaN             NaN                        NaN                NaN              NaN                     NaN                         NaN      6.308    445.792        -68.499         5.627             547.00000           294.400000             706.100065            -13.202011            431.60             0    0.000000e+00     NORMAL          True     9202391012      4.006721e+12  1.051300e+12  2.095753e+11             22.774          9202391012         4.006721e+12              114.242     0.199    19.118     3.811        19.118          3.48                0.80          3.48               0.799      False                   NaN      N/A               NaN                NaN            NaN                 NaN             NaN   
1   US.AAPL    APPLE  2025-04-07 05:30:43.301      188.38      193.89      199.88     187.34            203.19  125910913  2.424473e+10          0.838       False   1980-12-12         1          0.01          NaN      180.8     180.48       29      400            NaN             NaN                        NaN                NaN              NaN                     NaN                         NaN      6.172    192.554         86.480         2.226             259.81389           163.300566             259.813890              0.053580            188.93       3151311    5.930968e+08     NORMAL          True    15022073000      2.829858e+12  6.675809e+10  9.133420e+10              6.080         15016677308         2.828842e+12                4.444     1.417    30.983    42.389        29.901          0.99                0.53          0.98               0.520      False                   NaN      N/A               NaN                NaN            NaN                 NaN             NaN   

   wrt_issue_vol  wrt_street_ratio  wrt_delta  wrt_implied_volatility  wrt_premium  wrt_leverage  wrt_ipop  wrt_break_even_point  wrt_conversion_price  wrt_price_recovery_ratio  wrt_score  wrt_upper_strike_price  wrt_lower_strike_price wrt_inline_price_status  wrt_issuer_code  option_valid option_type  strike_time  option_strike_price  option_contract_size  option_open_interest  option_implied_volatility  option_premium  option_delta  option_gamma  option_vega  option_theta  option_rho  option_net_open_interest  option_expiry_date_distance  option_contract_nominal_value  option_owner_lot_multiplier option_area_type  option_contract_multiplier index_option_type  index_valid  index_raise_count  index_fall_count  index_equal_count  plate_valid  plate_raise_count  plate_fall_count  plate_equal_count  future_valid  future_last_settle_price  future_position  future_position_change  future_main_contract  future_last_trade_time  trust_valid  trust_dividend_yield  trust_aum  \
0            NaN               NaN        NaN                     NaN          NaN           NaN       NaN                   NaN                   NaN                       NaN        NaN                     NaN                     NaN                     N/A              NaN         False         N/A          NaN                  NaN                   NaN                   NaN                        NaN             NaN           NaN           NaN          NaN           NaN         NaN                       NaN                          NaN                            NaN                          NaN              N/A                         NaN               N/A        False                NaN               NaN                NaN        False                NaN               NaN                NaN         False                       NaN              NaN                     NaN                   NaN                     NaN        False                   NaN        NaN   
1            NaN               NaN        NaN                     NaN          NaN           NaN       NaN                   NaN                   NaN                       NaN        NaN                     NaN                     NaN                     N/A              NaN         False         N/A          NaN                  NaN                   NaN                   NaN                        NaN             NaN           NaN           NaN          NaN           NaN         NaN                       NaN                          NaN                            NaN                          NaN              N/A                         NaN               N/A        False                NaN               NaN                NaN        False                NaN               NaN                NaN         False                       NaN              NaN                     NaN                   NaN                     NaN        False                   NaN        NaN   

   trust_outstanding_units  trust_netAssetValue  trust_premium trust_assetClass pre_price pre_high_price pre_low_price pre_volume pre_turnover pre_change_val pre_change_rate pre_amplitude after_price after_high_price after_low_price after_change_val after_change_rate after_amplitude overnight_price overnight_high_price overnight_low_price overnight_volume overnight_turnover overnight_change_val overnight_change_rate overnight_amplitude  
0                      NaN                  NaN            NaN              N/A       N/A            N/A           N/A        N/A          N/A            N/A             N/A           N/A         N/A              N/A             N/A              N/A               N/A             N/A             N/A                  N/A                 N/A              N/A                N/A                  N/A                   N/A                 N/A  
1                      NaN                  NaN            NaN              N/A    180.68         181.98        177.47     276016  49809244.83           -7.7          -4.087         2.394       186.6          188.639          186.44            -1.78            -0.944          1.1673          176.94                186.5               174.4           533115        94944250.56               -11.44                -6.072              6.4231  
HK.00700
['HK.00700', 'US.AAPL']
```









## <a href="#338-2" class="header-anchor">#</a> Qot_GetSecuritySnapshot.proto

- **Description**

  Get snapshot data

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3203





`uint GetSecuritySnapshot(QotGetSecuritySnapshot.Request req);`  
`virtual void OnReply_GetSecuritySnapshot(MMAPI_Conn client, uint nSerialNo, QotGetSecuritySnapshot.Response rsp);`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn {
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetSecuritySnapshot.C2S c2s = QotGetSecuritySnapshot.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetSecuritySnapshot.Request req = QotGetSecuritySnapshot.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetSecuritySnapshot(req);
        Console.Write("Send QotGetSecuritySnapshot: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetSecuritySnapshot(MMAPI_Conn client, uint nSerialNo, QotGetSecuritySnapshot.Response rsp)
    {
        Console.Write("Reply: QotGetSecuritySnapshot: {0} \n", nSerialNo);
        Console.Write("basic price: {0}\n", rsp.S2C.SnapshotListList[0].Basic.CurPrice);
        Console.Write("equityExData issuedShares: {0}\n", rsp.S2C.SnapshotListList[0].EquityExData.IssuedShares);
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
Qot onInitConnect: ret=0 desc= connID=6825619056039643630
Send QotGetSecuritySnapshot: 3
Reply: QotGetSecuritySnapshot: 3
basic price: 474.2
equityExData issuedShares: 9595900007
```









`int getSecuritySnapshot(QotGetSecuritySnapshot.Request req);`  
`void onReply_GetSecuritySnapshot(MMAPI_Conn client, int nSerialNo, QotGetSecuritySnapshot.Response rsp);`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
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

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetSecuritySnapshot.C2S c2s = QotGetSecuritySnapshot.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetSecuritySnapshot.Request req = QotGetSecuritySnapshot.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getSecuritySnapshot(req);
        System.out.printf("Send QotGetSecuritySnapshot: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetSecuritySnapshot(MMAPI_Conn client, int nSerialNo, QotGetSecuritySnapshot.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetSecuritySnapshot failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetSecuritySnapshot: %s\n", json);
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
Send QotGetSecuritySnapshot: 2
Receive QotGetSecuritySnapshot: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "snapshotList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "00700"
        },
        "type": 3,
        "isSuspend": false,
        "listTime": "2004-06-16",
        "lotSize": 100,
        "priceSpread": 0.5,
        "updateTime": "2021-06-24 16:08:14",
        "highPrice": 587.5,
        "openPrice": 584.0,
        "lowPrice": 580.0,
        "lastClosePrice": 582.5,
        "curPrice": 583.0,
        "volume": "10947302",
        "turnover": 6.387238277E9,
        "turnoverRate": 0.114,
        "listTimestamp": 1.0873152E9,
        "updateTimestamp": 1.624522094E9,
        "askPrice": 583.5,
        "bidPrice": 583.0,
        "askVol": "142300",
        "bidVol": "52800",
        "enableMargin": true,
        "mortgageRatio": 0.0,
        "longMarginInitialRatio": 35.0,
        "enableShortSell": true,
        "shortSellRate": 0.9,
        "shortAvailableVolume": "2006700",
        "shortMarginInitialRatio": 60.0,
        "amplitude": 1.288,
        "avgPrice": 583.453,
        "bidAskRatio": -5.273,
        "volumeRatio": 0.553,
        "highest52WeeksPrice": 773.9,
        "lowest52WeeksPrice": 479.4,
        "highestHistoryPrice": 773.9,
        "lowestHistoryPrice": -6.381,
        "secStatus": 1,
        "closePrice5Minute": 583.5
      },
      "equityExData": {
        "issuedShares": "9595206625",
        "issuedMarketVal": 5.594005462375E12,
        "netAsset": 9.17675966408375E11,
        "netProfit": 1.90378494646625E11,
        "earningsPershare": 19.841,
        "outstandingShares": "9595206625",
        "outstandingMarketVal": 5.594005462375E12,
        "netAssetPershare": 95.639,
        "eyRate": 0.232,
        "peRate": 29.383,
        "pbRate": 6.095,
        "peTTMRate": 26.249,
        "dividendTTM": 1.6,
        "dividendRatioTTM": 0.27,
        "dividendLFY": 1.6,
        "dividendLFYRatio": 0.274
      }
    }]
  }
}
```









`moomoo::u32_t GetSecuritySnapshot(const Qot_GetSecuritySnapshot::Request &stReq);`  
`virtual void OnReply_GetSecuritySnapshot(moomoo::u32_t nSerialNo, const Qot_GetSecuritySnapshot::Response &stRsp) = 0;`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
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
        Qot_GetSecuritySnapshot::Request req;
        Qot_GetSecuritySnapshot::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetSecuritySnapshotSerialNo = m_pQotApi->GetSecuritySnapshot(req);
        cout << "Request GetSecuritySnapshot SerialNo: " << m_GetSecuritySnapshotSerialNo << endl;
    }

    virtual void OnReply_GetSecuritySnapshot(moomoo::u32_t nSerialNo, const Qot_GetSecuritySnapshot::Response &stRsp){
        if(nSerialNo == m_GetSecuritySnapshotSerialNo)
        {
            cout << "OnReply_GetSecuritySnapshot SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            // ProtoBufToBodyData和UTF8ToLocal函数的定义参见Sample中的tool.h文件
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetSecuritySnapshotSerialNo;
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
Request GetSecuritySnapshot SerialNo: 4
OnReply_GetSecuritySnapshot SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "snapshotList": [
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "00700"
     },
     "type": 3,
     "isSuspend": false,
     "listTime": "2004-06-16",
     "lotSize": 100,
     "priceSpread": 0.5,
     "updateTime": "2021-06-09 14:12:30",
     "highPrice": 606,
     "openPrice": 600,
     "lowPrice": 597.5,
     "lastClosePrice": 601,
     "curPrice": 600.5,
     "volume": "4382292",
     "turnover": 2638928979,
     "turnoverRate": 0.046,
     "listTimestamp": 1087315200,
     "updateTimestamp": 1623219150,
     "askPrice": 601,
     "bidPrice": 600.5,
     "askVol": "24200",
     "bidVol": "1400",
     "enableMargin": true,
     "mortgageRatio": 0,
     "longMarginInitialRatio": 35,
     "enableShortSell": true,
     "shortSellRate": 0.9,
     "shortAvailableVolume": "1860000",
     "shortMarginInitialRatio": 60,
     "amplitude": 1.414,
     "avgPrice": 602.18,
     "bidAskRatio": 38.289,
     "volumeRatio": 0.418,
     "highest52WeeksPrice": 773.9,
     "lowest52WeeksPrice": 430.6,
     "highestHistoryPrice": 773.9,
     "lowestHistoryPrice": -6.381,
     "secStatus": 1,
     "closePrice5Minute": 601.5
    },
    "equityExData": {
     "issuedShares": "9595206625",
     "issuedMarketVal": 5761921578312.5,
     "netAsset": 917675966408.375,
     "netProfit": 190378494646.625,
     "earningsPershare": 19.841,
     "outstandingShares": "9595206625",
     "outstandingMarketVal": 5761921578312.5,
     "netAssetPershare": 95.639,
     "eyRate": 0.232,
     "peRate": 30.265,
     "pbRate": 6.278,
     "peTTMRate": 27.037,
     "dividendTTM": 1.6,
     "dividendRatioTTM": 0.27,
     "dividendLFY": 1.6,
     "dividendLFYRatio": 0.266
    }
   }
  ]
 }
}
```









`GetSecuritySnapshot(req);`

- **Description**

  Get market snapshot

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
// Additional data of underlying stock type
message EquitySnapshotExData
{
    required int64 issuedShares = 1; //Total shares
    required double issuedMarketVal = 2; //Total market value = total number of shares * current price
    required double netAsset = 3; //Net asset value
    required double netProfit = 4; //Profit or loss
    required double earningsPershare = 5; //Earnings per share
    required int64 outstandingShares = 6; //Shares outstanding
    required double outstandingMarketVal = 7; //Market value of shares outstanding = number of shares outstanding * current price
    required double netAssetPershare = 8; //Net asset per share
    required double eyRate = 9; //Yield rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double peRate = 10; //P/E ratio
    required double pbRate = 11; //P/B ratio
    required double peTTMRate = 12; //P/E ratio TTM
    optional double dividendTTM = 13; //Dividend TTM, dividend
    optional double dividendRatioTTM = 14; //Dividend rate TTM (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double dividendLFY = 15; //Dividend LFY, last year's dividend
    optional double dividendLFYRatio = 16; //Dividend rate LFY (This field is in percentage form, so 20 is equivalent to 20%.)
}

// Additional data for warrant type
message WarrantSnapshotExData
{
    required double conversionRate = 1; //Share conversion ratio
    required int32 warrantType = 2; //Qot_Common.WarrantType, warrant type
    required double strikePrice = 3; //Strike price
    required string maturityTime = 4; //Time string of expiration date
    required string endTradeTime = 5; //Time string of the last trading day
    required Qot_Common.Security owner = 6; //The underlying stock
    required double recoveryPrice = 7; //Call price, only CBBC supports this field
    required int64 streetVolumn = 8; //Outstanding quantity
    required int64 issueVolumn = 9; //Issue volume
    required double streetRate = 10; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 11; //Hedging value, only calls and puts support this field
    required double impliedVolatility = 12; //Implied volatility, only calls and puts support this field
    required double premium = 13; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double maturityTimestamp = 14; //Maturity date timestamp
    optional double endTradeTimestamp = 15; //The last trading day timestamp
    optional double leverage = 16; //Leverage ratio (times)
    optional double ipop = 17; // In/out of money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double breakEvenPoint = 18; //Breakeven point
    optional double conversionPrice = 19; //Conversion price
    optional double priceRecoveryRatio = 20; //Stock price recovery ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double score = 21; //Comprehensive score
    optional double upperStrikePrice = 22; //Upper bound price, only the Inline Warrants support this field
    optional double lowerStrikePrice = 23; //Lower bound price, only the Inline Warrants support this field
    optional int32 inLinePriceStatus = 24; //Qot_Common.PriceType, in/out-of bound, only Inline Warrants support this field
    optional string issuerCode = 25; //Issuer code
}

// Option type additional data
message OptionSnapshotExData
{
    required int32 type = 1; //Qot_Common.OptionType, option type (by direction)
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Time string of exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required int32 contractSize = 5; //Number of stocks per contract (int type)
    optional double contractSizeFloat = 22; //Number of stocks per contract (float type)
    required int32 openInterest = 6; //Number of open position
    required double impliedVolatility = 7; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 8; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 9; //Greek value Delta
    required double gamma = 10; //Greek value Gamma
    required double vega = 11; //Greek value Vega
    required double theta = 12; //Greek value Theta
    required double rho = 13; //Greek value Rho
    optional double strikeTimestamp = 14; //Exercise date timestamp
    optional int32 indexOptionType = 15; //Qot_Common.IndexOptionType, index option type
    optional int32 netOpenInterest = 16; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 17; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 18; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 19; //Equal number of underlying stocks, index options do not have this field , only HK options support this field
    optional int32 optionAreaType = 20; //Qot_Common.OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 21; //Contract multiplier
}

// additional data of index type
message IndexSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

// Additional data of the sector type
message PlateSnapshotExData
{
    required int32 raiseCount = 1; //Number of stocks that raises
    required int32 fallCount = 2; //Number of stocks that falls
    required int32 equalCount = 3; //Number of stocks that does not change
}

//Additional data of futures type
message FutureSnapshotExData
{
    required double lastSettlePrice = 1; //Yesterday's close
    required int32 position = 2; //Holding position
    required int32 positionChange = 3; //Daily change in position
    required string lastTradeTime = 4; //The last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 5; //The last trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 6; //Whether is main-linked contract
}

//Additional data of fund type
message TrustSnapshotExData
{
    required double dividendYield = 1; //Dividend rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double aum = 2; //Asset scale
    required int64 outstandingUnits = 3; //Total circulation
    required double netAssetValue = 4; //Net asset value
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 assetClass = 6; //Qot_Common.AssetClass, asset class
}

//Basic snapshot data
message SnapshotBasicData
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 41; //Stock name
    required int32 type = 2; //Qot_Common.SecurityType, security type
    required bool isSuspend = 3; //Whether is suspended
    required string listTime = 4; //String of listed time (Format: yyyy-MM-dd)
    required int32 lotSize = 5; //Quantity per lot
    required double priceSpread = 6; //Spread
    required string updateTime = 7; //String of updated time (Format: yyyy-MM-dd HH:mm:ss)
    required double highPrice = 8; //High
    required double openPrice = 9; //Open
    required double lowPrice = 10; //low
    required double lastClosePrice = 11; //Yesterday's close
    required double curPrice = 12; //Current price
    required int64 volume = 13; //Volume
    required double turnover = 14; //Turnover
    required double turnoverRate = 15; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double listTimestamp = 16; //Listing timestamp
    optional double updateTimestamp = 17; //Update timestamp
    optional double askPrice = 18;//Ask price
    optional double bidPrice = 19;//Bid price
    optional int64 askVol = 20;//Ask volume
    optional int64 bidVol = 21;//Bid volume
    optional bool enableMargin = 22; //Whether financing is available (Deprecated. Please use Get Margin Data interface.). 
    optional double mortgageRatio = 23; //Stock mortgage rate.
    optional double longMarginInitialRatio = 24; //Initial margin rate for financing (Deprecated. Please use Get Margin Data interface.). 
    optional bool enableShortSell = 25; //Whether it can be short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortSellRate = 26; //Reference rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional int64 shortAvailableVolume = 27; //The remaining quantity that is available for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double shortMarginInitialRatio = 28; //The initial margin rate for short selling (Deprecated. Please use Get Margin Data interface.). 
    optional double amplitude = 29; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double avgPrice = 30; //Average price
    optional double bidAskRatio = 31; //Commission ratio (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double volumeRatio = 32; //Volume ratio
    optional double highest52WeeksPrice = 33; //Highest price in 52 weeks
    optional double lowest52WeeksPrice = 34; //Lowest price in 52 weeks 
    optional double highestHistoryPrice = 35; //Highest historical price
    optional double lowestHistoryPrice = 36; //Lowest historical price
    optional Qot_Common.PreAfterMarketData preMarket = 37; //Qot_Common::PreAfterMarketData data pre-market
    optional Qot_Common.PreAfterMarketData afterMarket = 38; //Qot_Common::PreAfterMarketData data after-hourrs
    optional Qot_Common.PreAfterMarketData overnight = 42; //Qot_Common::PreAfterMarketData data overnight
    optional int32 secStatus = 39; //Qot_Common::SecurityStatus stock status
    optional double closePrice5Minute = 40; //Close for timeframe of 5 minutes
}

message Snapshot
{
    required SnapshotBasicData basic = 1; //Snapshot basic data
    optional EquitySnapshotExData equityExData = 2; //Stock snapshot additional data
    optional WarrantSnapshotExData warrantExData = 3; //Warrant snapshot additional data
    optional OptionSnapshotExData optionExData = 4; //Option snapshot additional data
    optional IndexSnapshotExData indexExData = 5; //Index snapshot additional data
    optional PlateSnapshotExData plateExData = 6; //Plate snapshot additional data
    optional FutureSnapshotExData futureExData = 7; //Futures additional data
    optional TrustSnapshotExData trustExData = 8; //Fund additional data
}

message S2C
{
    repeated Snapshot snapshotList = 1; //Stock snapshot
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure， refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetSecuritySnapshot(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) {

            const req = {
                c2s: {
                securityList: [
                    {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                ],
                },
            };
            websocket.GetSecuritySnapshot(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("Snapshot: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                if(retType == RetType.RetType_Succeed){
                    let snapshot = beautify(JSON.stringify(s2c), {
                        indent_size: 2,
                        space_in_empty_paren: true,
                    });
                    console.log(snapshot);
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
Snapshot: errCode 0, retMsg , retType 0
{
  "snapshotList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "00700"
      },
      "type": 3,
      "isSuspend": false,
      "listTime": "2004-06-16",
      "lotSize": 100,
      "priceSpread": 0.2,
      "updateTime": "2021-09-09 16:08:17",
      "highPrice": 511.5,
      "openPrice": 509,
      "lowPrice": 479,
      "lastClosePrice": 524.5,
      "curPrice": 480,
      "volume": "54090872",
      "turnover": 26716845932,
      "turnoverRate": 0.563,
      "listTimestamp": 1087315200,
      "updateTimestamp": 1631174897,
      "askPrice": 480.4,
      "bidPrice": 480,
      "askVol": "700",
      "bidVol": "55300",
      "enableMargin": true,
      "mortgageRatio": 0,
      "longMarginInitialRatio": 35,
      "enableShortSell": true,
      "shortSellRate": 0.92,
      "shortAvailableVolume": "3059000",
      "shortMarginInitialRatio": 50,
      "amplitude": 6.196,
      "avgPrice": 493.925,
      "bidAskRatio": 22.703,
      "volumeRatio": 1.775,
      "highest52WeeksPrice": 773.9,
      "lowest52WeeksPrice": 412.2,
      "highestHistoryPrice": 773.9,
      "lowestHistoryPrice": -6.381,
      "secStatus": 1,
      "closePrice5Minute": 483.4
    },
    "equityExData": {
      "issuedShares": "9599810645",
      "issuedMarketVal": 4607909109600,
      "netAsset": 1016063158288.09,
      "netProfit": 190383444711.64,
      "earningsPershare": 19.832,
      "outstandingShares": "9599810645",
      "outstandingMarketVal": 4607909109600,
      "netAssetPershare": 105.842,
      "eyRate": 0.22,
      "peRate": 24.203,
      "pbRate": 4.535,
      "peTTMRate": 20.532,
      "dividendTTM": 1.599,
      "dividendRatioTTM": 0.33,
      "dividendLFY": 1.599,
      "dividendLFYRatio": 0.333
    }
  }]
}
stop
```











Interface Limitations

- Request up to 60 snapshots every 30 seconds
- For each request, the maximum number of stock codes supported by the
  parameter *code_list* is 400.













