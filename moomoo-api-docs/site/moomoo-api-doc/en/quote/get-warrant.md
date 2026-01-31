



# <a href="#5151" class="header-anchor">#</a> Get Filtered Warrant









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_warrant(stock_owner='', req=None)`

- **Description**

  Get Filtered Warrant (only warrants, CBBCs and Inline Warrants of HK
  market are surpported)

- **Parameters**

  | Parameter   | Type             | Description                   |
  |:------------|:-----------------|:------------------------------|
  | stock_owner | str              | Code of the underlying stock. |
  | req         | *WarrantRequest* | Filter parameter combination. |

  - *WarrantRequest*'s details as follows:
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
    <td style="text-align: left;">begin</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Data start point</td>
    </tr>
    <tr>
    <td style="text-align: left;">num</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of requested data.
    
      
    
    
     
    
    The maximum is 200.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#5823">SortField</a></td>
    <td style="text-align: left;">According to which field to sort.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ascend</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">The sort direction.
    
      
    
    
     
    
    True: ascending order.<br />
    False: descending order.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">type_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Warrant Type Filter List.
    
      
    
    
     
    
    Data type of elements in the list is <a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">issuer_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Issuer filter list.
    
      
    
    
     
    
    Data type of elements in the list is <a
    href="/moomoo-api-doc/en/quote/quote.html#5122">Issuer</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">maturity_time_min</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The start time of the maturity date filter
    range.</td>
    </tr>
    <tr>
    <td style="text-align: left;">maturity_time_max</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The end time of the maturity date filter
    range.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_period</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2961">IpoPeriod</a></td>
    <td style="text-align: left;">Listing period.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9794">PriceType</a></td>
    <td style="text-align: left;">In/out of the money.
    
      
    
    
     
    
    The Inline Warrant is not currently supported.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#5892">WarrantStatus</a></td>
    <td style="text-align: left;">Warrant Status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The filter lower limit (closed interval)
    of the latest price.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The filter upper limit (closed interval)
    of the latest price.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the strike price.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the strike price.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">street_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit (closed interval) of
    Outstanding percentage.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">street_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit (closed interval) of
    Outstanding percentage.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">conversion_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the conversion ratio.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">conversion_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the conversion ratio.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_min</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the volume.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_max</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the volume.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">premium_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of premium value.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">premium_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of premium value.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">leverage_ratio_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the leverage ratio.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">leverage_ratio_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the leverage ratio.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the hedge value Delta.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the hedge value Delta.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the implied volatility.
    
      
    
    
     
    
    Only calls and puts support this filtering field.<br />
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the implied volatility.
    
      
    
    
     
    
    Only calls and puts support this filtering field.<br />
    If not passed, the upper limit is +∞(3 decimal place accuracy, the
    excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">recovery_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the recovery price.
    
      
    
    
     
    
    Only CBBCs support this field to filter.<br />
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">recovery_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the recovery price.
    
      
    
    
     
    
    Only CBBCs support this field to filter.<br />
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price_recovery_ratio_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the price recovery ratio.
    
      
    
    
     
    
    Only CBBCs support this field.<br />
    If not passed, the lower limit is -∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price_recovery_ratio_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the price recovery ratio.
    
      
    
    
     
    
    Only CBBCs support this field.<br />
    If not passed, the upper limit is +∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
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
  <td>If ret == RET_OK, warrant data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Warrant data format as follows:

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
    <td style="text-align: left;">warrant_data_list</td>
    <td style="text-align: left;">pd.DataFrame</td>
    <td style="text-align: left;">Warrant data after filtering.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_page</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Weather is the last page.
    
      
    
    
     
    
    True: the last page.<br />
    False: not the last page.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">all_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The total number of warrants in the
    filtered result.</td>
    </tr>
    </tbody>
    </table>

    - Warrant_data_list's detail as follows:
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
      <td style="text-align: left;">stock</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Warrant code.</td>
      </tr>
      <tr>
      <td style="text-align: left;">stock_owner</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Underlying stock.</td>
      </tr>
      <tr>
      <td style="text-align: left;">type</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
      <td style="text-align: left;">Warrant type.</td>
      </tr>
      <tr>
      <td style="text-align: left;">issuer</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#5122">Issuer</a></td>
      <td style="text-align: left;">Issuer.</td>
      </tr>
      <tr>
      <td style="text-align: left;">maturity_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Maturity date.
      
        
      
      
       
      
      Format: yyyy-MM-dd
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">list_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Listing time.
      
        
      
      
       
      
      Format: yyyy-MM-dd
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">last_trade_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Last trading day.
      
        
      
      
       
      
      Format: yyyy-MM-dd
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">recovery_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Recovery price.
      
        
      
      
       
      
      Only CBBCs support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">conversion_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Conversion ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">lot_size</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Quantity per lot.</td>
      </tr>
      <tr>
      <td style="text-align: left;">strike_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Strike price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">last_close_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Yesterday's close.</td>
      </tr>
      <tr>
      <td style="text-align: left;">name</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Name.</td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">price_change_val</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change.</td>
      </tr>
      <tr>
      <td style="text-align: left;">status</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#5892">WarrantStatus</a></td>
      <td style="text-align: left;">Warrant status.</td>
      </tr>
      <tr>
      <td style="text-align: left;">bid_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Bid price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">ask_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Ask price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">bid_vol</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Bid volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">ask_vol</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Ask volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">volume</td>
      <td style="text-align: left;">unsigned int</td>
      <td style="text-align: left;">Volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Turnover.</td>
      </tr>
      <tr>
      <td style="text-align: left;">score</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Comprehensive score.</td>
      </tr>
      <tr>
      <td style="text-align: left;">premium</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Premium.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">break_even_point</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Breakeven point.</td>
      </tr>
      <tr>
      <td style="text-align: left;">leverage</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Leverage ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">ipop</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">In/out of the money.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">price_recovery_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price recovery ratio.
      
        
      
      
       
      
      Only CBBC supports this field.<br />
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">conversion_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Conversion price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">street_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Outstanding percentage.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">street_vol</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Outstanding quantity.</td>
      </tr>
      <tr>
      <td style="text-align: left;">amplitude</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Amplitude.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">issue_size</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Issue size.</td>
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
      <td style="text-align: left;">implied_volatility</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Implied volatility.
      
        
      
      
       
      
      Only calls and puts support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">delta</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Hedging value.
      
        
      
      
       
      
      Only calls and puts support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">effective_leverage</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Effective leverage.
      
        
      
      
       
      
      Only calls and puts support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">upper_strike_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Upper bound price.
      
        
      
      
       
      
      Only Inline Warrants support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">lower_strike_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Lower bound price.
      
        
      
      
       
      
      Only Inline Warrants support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">inline_price_status</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#9794">PriceType</a></td>
      <td style="text-align: left;">In/out of bounds.
      
        
      
      
       
      
      Only Inline Warrants support this field.
      
      
      
      </td>
      </tr>
      </tbody>
      </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

req = WarrantRequest()
req.sort_field = SortField.TURNOVER
req.type_list = WrtType.CALL
req.cur_price_min = 0.1
req.cur_price_max = 0.2
ret, ls = quote_ctx.get_warrant("HK.00700", req)
if ret == RET_OK: # First judge whether the interface return is normal, and then fetch the data
    warrant_data_list, last_page, all_count = ls
    print(len(warrant_data_list), all_count, warrant_data_list)
    print(warrant_data_list['stock'][0]) # Take the first warrant code
    print(warrant_data_list['stock'].values.tolist()) # Convert to list
else:
    print('error: ', ls)
    
req = WarrantRequest()
req.sort_field = SortField.TURNOVER
req.issuer_list = ['UB','CS','BI']
ret, ls = quote_ctx.get_warrant(Market.HK, req)
if ret == RET_OK: 
    warrant_data_list, last_page, all_count = ls
    print(len(warrant_data_list), all_count, warrant_data_list)
else:
    print('error: ', ls)

quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
2 2 
    stock        name stock_owner  type issuer maturity_time   list_time last_trade_time  recovery_price  conversion_ratio  lot_size  strike_price  last_close_price  cur_price  price_change_val  change_rate  status  bid_price  ask_price   bid_vol  ask_vol    volume   turnover   score  premium  break_even_point  leverage    ipop  price_recovery_ratio  conversion_price  street_rate  street_vol  amplitude  issue_size  high_price  low_price  implied_volatility  delta  effective_leverage  list_timestamp  last_trade_timestamp  maturity_timestamp  upper_strike_price  lower_strike_price  inline_price_status
0   HK.20306  MBTENCT@EC2012A    HK.00700  CALL     MB    2020-12-01  2019-06-27      2020-11-25             NaN              50.0      5000        588.88             0.188      0.188             0.000     0.000000  NORMAL      0.000      0.188         0     10000           0          0.0   0.196    1.921            598.28    62.446  -0.319                   NaN              9.40        4.400     1584000      0.000    36000000       0.000      0.000              32.487  0.473              29.536    1.561565e+09          1.606234e+09        1.606752e+09                 NaN                 NaN                  NaN
1   HK.16545  SGTENCT@EC2102B    HK.00700  CALL     SG    2021-02-26  2020-07-14      2021-02-22             NaN             100.0     10000        700.00             0.147      0.143            -0.004    -2.721088  NORMAL      0.141      0.143  28000000  28000000           0          0.0  82.011   21.686            714.30    41.048 -16.142                   NaN             14.30        1.420     2130000      0.000   150000000       0.000      0.000              40.657  0.225               9.235    1.594656e+09          1.613923e+09        1.614269e+09                 NaN                 NaN                  NaN
HK.20306
['HK.20306', 'HK.16545']

200 358
    stock        name stock_owner    type issuer maturity_time   list_time last_trade_time  recovery_price  conversion_ratio  lot_size  strike_price  last_close_price  cur_price  price_change_val  change_rate      status  bid_price  ask_price   bid_vol   ask_vol  volume  turnover   score  premium  break_even_point  leverage     ipop  price_recovery_ratio  conversion_price  street_rate  street_vol  amplitude  issue_size  high_price  low_price  implied_volatility  delta  effective_leverage  list_timestamp  last_trade_timestamp  maturity_timestamp  upper_strike_price  lower_strike_price inline_price_status
0    HK.19839   PINGANRUIYINLINGYIGOUAC    HK.02318    CALL     UB    2020-12-31  2017-12-11      2020-12-24             NaN             100.0     50000         83.88             0.057      0.046            -0.011   -19.298246      NORMAL      0.043      0.046  30000000  30000000       0       0.0  39.585    1.642            88.480    18.923    3.779                   NaN             4.600         1.25     6250000        0.0   500000000         0.0        0.0              25.129  0.692              13.094    1.512922e+09          1.608739e+09        1.609344e+09                 NaN                 NaN                 NaN
1    HK.20084   PINGANZHONGYINLINGYIGOUAC    HK.02318    CALL     BI    2020-12-31  2017-12-19      2020-12-24             NaN             100.0     50000         83.88             0.059      0.050            -0.009   -15.254237      NORMAL      0.044      0.050  10000000  10000000       0       0.0   0.064    2.102            88.880    17.410    3.779                   NaN             5.000         0.07      350000        0.0   500000000         0.0        0.0              29.510  0.668              11.629    1.513613e+09          1.608739e+09        1.609344e+09                 NaN                 NaN                 NaN
......
198  HK.56886   UB#HSI  RC2301F   HK.800000    BULL     UB    2023-01-30  2020-03-24      2023-01-27         21200.0           20000.0     10000      21100.00             0.230      0.232             0.002     0.869565      NORMAL      0.232      0.233  30000000  30000000       0       0.0  46.619   -2.916         25740.000     5.714   25.655             25.062689          4640.000         0.01       40000        0.0   400000000         0.0        0.0                 NaN    NaN               5.714    1.584979e+09          1.674749e+09        1.675008e+09                 NaN                 NaN                 NaN
199  HK.56895   UB#XIAMIRC2012D    HK.01810    BULL     UB    2020-12-30  2020-03-24      2020-12-29             8.0              10.0      2000          7.60             2.010      1.930            -0.080    -3.980100      NORMAL      1.910      1.930   6000000   6000000       0       0.0   0.040    1.127            26.900     1.378  250.000            232.500000            19.300         0.10       60000        0.0    60000000         0.0        0.0                 NaN    NaN               1.378    1.584979e+09          1.609171e+09        1.609258e+09                 NaN                 NaN                 NaN
```









## <a href="#8023" class="header-anchor">#</a> Qot_GetWarrant.proto

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3210





`uint GetWarrant(QotGetWarrant.Request req);`  
`virtual void OnReply_GetWarrant(FTAPI_Conn client, uint nSerialNo, QotGetWarrant.Response rsp);`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
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

        QotGetWarrant.C2S c2s = QotGetWarrant.C2S.CreateBuilder()
                .SetBegin(0)
                .SetNum(50)
                .SetSortField((int)QotCommon.SortField.SortField_Code)
                .SetAscend(true)
            .Build();
        QotGetWarrant.Request req = QotGetWarrant.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetWarrant(req);
        Console.Write("Send QotGetWarrant: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetWarrant(FTAPI_Conn client, uint nSerialNo, QotGetWarrant.Response rsp)
    {
        Console.Write("Reply: QotGetWarrant: {0}\n", nSerialNo);
        Console.Write("retMsg: {0}\n", rsp.RetMsg);
        Console.Write("name: {0}, type: {1}\n", rsp.S2C.WarrantDataListList[0].Name,
            rsp.S2C.WarrantDataListList[0].Type);
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
Qot onInitConnect: ret=0 desc= connID=6825714488755091916
Send QotGetWarrant: 3
Reply: QotGetWarrant: 3
retMsg:
name: MBTENCT@EC2012A, type: 1
```









`int getWarrant(QotGetWarrant.Request req);`  
`void onReply_GetWarrant(FTAPI_Conn client, int nSerialNo, QotGetWarrant.Response rsp);`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
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

        QotGetWarrant.C2S c2s = QotGetWarrant.C2S.newBuilder()
                .setBegin(0)
                .setNum(50)
                .setSortField(QotCommon.SortField.SortField_Code_VALUE)
                .setAscend(true)
            .build();
        QotGetWarrant.Request req = QotGetWarrant.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getWarrant(req);
        System.out.printf("Send QotGetWarrant: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetWarrant(FTAPI_Conn client, int nSerialNo, QotGetWarrant.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetWarrant failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetWarrant: %s\n", json);
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
Send QotGetWarrant: 2
Receive QotGetWarrant: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "lastPage": false,
    "allCount": 15552,
    "warrantDataList": [{
      "stock": {
        "market": 1,
        "code": "10071"
      },
      "owner": {
        "market": 11,
        "code": ".DJI"
      },
      "type": 2,
      "issuer": 7,
      "maturityTime": "2021-06-18",
      "maturityTimestamp": 1.6239456E9,
      "listTime": "2020-11-10",
      "listTimestamp": 1.6049376E9,
      "lastTradeTime": "2021-06-11",
      "lastTradeTimestamp": 1.6233408E9,
      "conversionRatio": 66000.0,
      "lotSize": 10000,
      "strikePrice": 25000.0,
      "lastClosePrice": 0.01,
      "name": "HS-DJI @EP2106B",
      "curPrice": 0.01,
      "priceChangeVal": 0.0,
      "changeRate": 0.0,
      "status": 3,
      "bidPrice": 0.0,
      "askPrice": 0.0,
      "bidVol": "0",
      "askVol": "0",
      "volume": "0",
      "turnover": 0.0,
      "score": 0.02,
      "premium": 0.0,
      "breakEvenPoint": 24340.0,
      "leverage": 0.0,
      "ipop": 100.0,
      "conversionPrice": 660.0,
      "streetRate": 6.54,
      "streetVol": "13080000",
      "amplitude": 0.0,
      "issueSize": "200000000",
      "highPrice": 0.0,
      "lowPrice": 0.0,
      "impliedVolatility": 0.0,
      "delta": 0.0,
      "effectiveLeverage": 0.0
    }, ... {
      "stock": {
        "market": 1,
        "code": "11047"
      },
      "owner": {
        "market": 1,
        "code": "01211"
      },
      "type": 2,
      "issuer": 21,
      "maturityTime": "2021-11-26",
      "maturityTimestamp": 1.637856E9,
      "listTime": "2021-05-17",
      "listTimestamp": 1.6211808E9,
      "lastTradeTime": "2021-11-22",
      "lastTradeTimestamp": 1.6375104E9,
      "conversionRatio": 50.0,
      "lotSize": 25000,
      "strikePrice": 121.0,
      "lastClosePrice": 0.026,
      "name": "VT-BYD @EP2111A",
      "curPrice": 0.026,
      "priceChangeVal": 0.0,
      "changeRate": 0.0,
      "status": 1,
      "bidPrice": 0.026,
      "askPrice": 0.029,
      "bidVol": "125000",
      "askVol": "600000",
      "volume": "0",
      "turnover": 0.0,
      "score": 0.008,
      "premium": 47.407,
      "breakEvenPoint": 119.7,
      "leverage": 175.076,
      "ipop": -88.099,
      "conversionPrice": 1.3,
      "streetRate": 2.25,
      "streetVol": "900000",
      "amplitude": 0.0,
      "issueSize": "40000000",
      "highPrice": 0.0,
      "lowPrice": 0.0,
      "impliedVolatility": 58.629,
      "delta": -0.032,
      "effectiveLeverage": -5.602
    }]
  }
}
```









`Futu::u32_t GetWarrant(const Qot_GetWarrant::Request &stReq);`  
`virtual void OnReply_GetWarrant(Futu::u32_t nSerialNo, const Qot_GetWarrant::Response &stRsp) = 0;`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
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
        Qot_GetWarrant::Request req;
        Qot_GetWarrant::C2S *c2s = req.mutable_c2s();
        c2s->set_begin(0);
        c2s->set_num(50);
        c2s->set_sortfield(1);
        c2s->set_ascend(false);

        m_GetWarrantSerialNo = m_pQotApi->GetWarrant(req);
        cout << "Request GetWarrant SerialNo: " << m_GetWarrantSerialNo << endl;
    }

    virtual void OnReply_GetWarrant(Futu::u32_t nSerialNo, const Qot_GetWarrant::Response &stRsp){
        if(nSerialNo == m_GetWarrantSerialNo)
        {
            cout << "OnReply_GetWarrant SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetWarrantSerialNo;
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
Request GetWarrant SerialNo: 4
OnReply_GetWarrant SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "lastPage": false,
  "allCount": 15685,
  "warrantDataList": [
   {
    "stock": {
     "market": 1,
     "code": "69999"
    },
    "owner": {
     "market": 1,
     "code": "01211"
    },
    "type": 3,
    "issuer": 1,
    "maturityTime": "2022-02-28",
    "maturityTimestamp": 1645977600,
    "listTime": "2021-06-11",
    "listTimestamp": 1623340800,
    "lastTradeTime": "2022-02-25",
    "lastTradeTimestamp": 1645718400,
    "recoveryPrice": 193,
    "conversionRatio": 500,
    "lotSize": 25000,
    "strikePrice": 189,
    "lastClosePrice": 0,
    "name": "SG#BYD  RC2202P",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 4,
    "bidPrice": 0,
    "askPrice": 0,
    "bidVol": "0",
    "askVol": "0",
    "volume": "0",
    "turnover": 0,
    "score": 0,
    "premium": -5.12,
    "breakEvenPoint": 189,
    "leverage": 0,
    "ipop": 5.396,
    "priceRecoveryRatio": 3.2124352331606163,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "150000000",
    "highPrice": 0,
    "lowPrice": 0,
    "effectiveLeverage": 0
   },
...
   {
    "stock": {
     "market": 1,
     "code": "69897"
    },
    "owner": {
     "market": 1,
     "code": "00700"
    },
    "type": 4,
    "issuer": 3,
    "maturityTime": "2021-12-30",
    "maturityTimestamp": 1640793600,
    "listTime": "2021-06-11",
    "listTimestamp": 1623340800,
    "lastTradeTime": "2021-12-29",
    "lastTradeTimestamp": 1640707200,
    "recoveryPrice": 608,
    "conversionRatio": 500,
    "lotSize": 5000,
    "strikePrice": 610.8,
    "lastClosePrice": 0,
    "name": "CS#TENCTRP2112G",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 4,
    "bidPrice": 0,
    "askPrice": 0,
    "bidVol": "0",
    "askVol": "0",
    "volume": "0",
    "turnover": 0,
    "score": 0,
    "premium": -1.715,
    "breakEvenPoint": 610.8,
    "leverage": 0,
    "ipop": 1.686,
    "priceRecoveryRatio": -1.2335526315789473,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "100000000",
    "highPrice": 0,
    "lowPrice": 0,
    "effectiveLeverage": 0
   }
  ]
 }
}
```









`GetWarrant(req);`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetWarrant(){
    const { RetType } = Common
    const { SortField, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    begin: 0,
                    num: 2,
                    sortField: SortField.SortField_CurPrice,
                    ascend: true,

                    owner:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                },
            };

            websocket.GetWarrant(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("Warrant: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Warrant: errCode 0, retMsg , retType 0
{
  "lastPage": false,
  "allCount": 1380,
  "warrantDataList": [{
    "stock": {
      "market": 1,
      "code": "26508"
    },
    "owner": {
      "market": 1,
      "code": "00700"
    },
    "type": 1,
    "issuer": 6,
    "maturityTime": "2022-01-26",
    "maturityTimestamp": 1643126400,
    "listTime": "2021-09-14",
    "listTimestamp": 1631548800,
    "lastTradeTime": "2022-01-20",
    "lastTradeTimestamp": 1642608000,
    "conversionRatio": 100,
    "lotSize": 10000,
    "strikePrice": 575.5,
    "lastClosePrice": 0,
    "name": "GSTENCT@EC2201M",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 1,
    "bidPrice": 0.179,
    "askPrice": 0.18,
    "bidVol": "10280000",
    "askVol": "10280000",
    "volume": "0",
    "turnover": 0,
    "score": 52.327,
    "premium": 19.596,
    "breakEvenPoint": 575.5,
    "leverage": 0,
    "ipop": -16.385,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "120000000",
    "highPrice": 0,
    "lowPrice": 0,
    "impliedVolatility": 0,
    "delta": 0,
    "effectiveLeverage": 0
  }, {
    "stock": {
      "market": 1,
      "code": "52325"
    },
    "owner": {
      "market": 1,
      "code": "00700"
    },
    "type": 3,
    "issuer": 7,
    "maturityTime": "2022-04-29",
    "maturityTimestamp": 1651161600,
    "listTime": "2021-09-14",
    "listTimestamp": 1631548800,
    "lastTradeTime": "2022-04-28",
    "lastTradeTimestamp": 1651075200,
    "recoveryPrice": 492.88,
    "conversionRatio": 500,
    "lotSize": 50000,
    "strikePrice": 488.88,
    "lastClosePrice": 0,
    "name": "HS#TENCTRC2204E",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 3,
    "bidPrice": 0,
    "askPrice": 0,
    "bidVol": "0",
    "askVol": "0",
    "volume": "0",
    "turnover": 0,
    "score": 0.24,
    "premium": 1.596,
    "breakEvenPoint": 488.88,
    "leverage": 0,
    "ipop": -1.57,
    "priceRecoveryRatio": -2.3697451712384368,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "100000000",
    "highPrice": 0,
    "lowPrice": 0,
    "effectiveLeverage": 0
  }]
}
stop
```











Interface Limitations

- Hong Kong stock BMP permission does not support calling this API
- A maximum of 60 requests per 30 seconds
- The maximum number of data per request is 200











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_warrant(stock_owner='', req=None)`

- **Description**

  Get Filtered Warrant (only warrants, CBBCs and Inline Warrants of HK
  market are surpported)

- **Parameters**

  | Parameter   | Type             | Description                   |
  |:------------|:-----------------|:------------------------------|
  | stock_owner | str              | Code of the underlying stock. |
  | req         | *WarrantRequest* | Filter parameter combination. |

  - *WarrantRequest*'s details as follows:
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
    <td style="text-align: left;">begin</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Data start point</td>
    </tr>
    <tr>
    <td style="text-align: left;">num</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of requested data.
    
      
    
    
     
    
    The maximum is 200.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sort_field</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#5823">SortField</a></td>
    <td style="text-align: left;">According to which field to sort.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ascend</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">The sort direction.
    
      
    
    
     
    
    True: ascending order.<br />
    False: descending order.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">type_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Warrant Type Filter List.
    
      
    
    
     
    
    Data type of elements in the list is <a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">issuer_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Issuer filter list.
    
      
    
    
     
    
    Data type of elements in the list is <a
    href="/moomoo-api-doc/en/quote/quote.html#5122">Issuer</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">maturity_time_min</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The start time of the maturity date filter
    range.</td>
    </tr>
    <tr>
    <td style="text-align: left;">maturity_time_max</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The end time of the maturity date filter
    range.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_period</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2961">IpoPeriod</a></td>
    <td style="text-align: left;">Listing period.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9794">PriceType</a></td>
    <td style="text-align: left;">In/out of the money.
    
      
    
    
     
    
    The Inline Warrant is not currently supported.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#5892">WarrantStatus</a></td>
    <td style="text-align: left;">Warrant Status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The filter lower limit (closed interval)
    of the latest price.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The filter upper limit (closed interval)
    of the latest price.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the strike price.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the strike price.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">street_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower limit (closed interval) of
    Outstanding percentage.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">street_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper limit (closed interval) of
    Outstanding percentage.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">conversion_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the conversion ratio.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">conversion_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the conversion ratio.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_min</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the volume.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_max</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the volume.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">premium_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of premium value.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">premium_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of premium value.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">leverage_ratio_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the leverage ratio.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">leverage_ratio_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the leverage ratio.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the hedge value Delta.
    
      
    
    
     
    
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the hedge value Delta.
    
      
    
    
     
    
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the implied volatility.
    
      
    
    
     
    
    Only calls and puts support this filtering field.<br />
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the implied volatility.
    
      
    
    
     
    
    Only calls and puts support this filtering field.<br />
    If not passed, the upper limit is +∞(3 decimal place accuracy, the
    excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">recovery_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the recovery price.
    
      
    
    
     
    
    Only CBBCs support this field to filter.<br />
    If not passed, the lower limit is -∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">recovery_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the recovery price.
    
      
    
    
     
    
    Only CBBCs support this field to filter.<br />
    If not passed, the upper limit is +∞.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price_recovery_ratio_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The lower filter limit (closed interval)
    of the price recovery ratio.
    
      
    
    
     
    
    Only CBBCs support this field.<br />
    If not passed, the lower limit is -∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price_recovery_ratio_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The upper filter limit (closed interval)
    of the price recovery ratio.
    
      
    
    
     
    
    Only CBBCs support this field.<br />
    If not passed, the upper limit is +∞.<br />
    This field is in percentage form, so 20 is equivalent to 20%.<br />
    3 decimal place accuracy, the excess part is discarded.
    
    
    
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
  <td>If ret == RET_OK, warrant data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Warrant data format as follows:

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
    <td style="text-align: left;">warrant_data_list</td>
    <td style="text-align: left;">pd.DataFrame</td>
    <td style="text-align: left;">Warrant data after filtering.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_page</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Weather is the last page.
    
      
    
    
     
    
    True: the last page.<br />
    False: not the last page.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">all_count</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The total number of warrants in the
    filtered result.</td>
    </tr>
    </tbody>
    </table>

    - Warrant_data_list's detail as follows:
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
      <td style="text-align: left;">stock</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Warrant code.</td>
      </tr>
      <tr>
      <td style="text-align: left;">stock_owner</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Underlying stock.</td>
      </tr>
      <tr>
      <td style="text-align: left;">type</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
      <td style="text-align: left;">Warrant type.</td>
      </tr>
      <tr>
      <td style="text-align: left;">issuer</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#5122">Issuer</a></td>
      <td style="text-align: left;">Issuer.</td>
      </tr>
      <tr>
      <td style="text-align: left;">maturity_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Maturity date.
      
        
      
      
       
      
      Format: yyyy-MM-dd
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">list_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Listing time.
      
        
      
      
       
      
      Format: yyyy-MM-dd
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">last_trade_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Last trading day.
      
        
      
      
       
      
      Format: yyyy-MM-dd
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">recovery_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Recovery price.
      
        
      
      
       
      
      Only CBBCs support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">conversion_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Conversion ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">lot_size</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Quantity per lot.</td>
      </tr>
      <tr>
      <td style="text-align: left;">strike_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Strike price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">last_close_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Yesterday's close.</td>
      </tr>
      <tr>
      <td style="text-align: left;">name</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">Name.</td>
      </tr>
      <tr>
      <td style="text-align: left;">cur_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Current price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">price_change_val</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price change.</td>
      </tr>
      <tr>
      <td style="text-align: left;">status</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#5892">WarrantStatus</a></td>
      <td style="text-align: left;">Warrant status.</td>
      </tr>
      <tr>
      <td style="text-align: left;">bid_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Bid price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">ask_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Ask price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">bid_vol</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Bid volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">ask_vol</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Ask volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">volume</td>
      <td style="text-align: left;">unsigned int</td>
      <td style="text-align: left;">Volume.</td>
      </tr>
      <tr>
      <td style="text-align: left;">turnover</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Turnover.</td>
      </tr>
      <tr>
      <td style="text-align: left;">score</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Comprehensive score.</td>
      </tr>
      <tr>
      <td style="text-align: left;">premium</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Premium.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">break_even_point</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Breakeven point.</td>
      </tr>
      <tr>
      <td style="text-align: left;">leverage</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Leverage ratio.</td>
      </tr>
      <tr>
      <td style="text-align: left;">ipop</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">In/out of the money.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">price_recovery_ratio</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Price recovery ratio.
      
        
      
      
       
      
      Only CBBC supports this field.<br />
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">conversion_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Conversion price.</td>
      </tr>
      <tr>
      <td style="text-align: left;">street_rate</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Outstanding percentage.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">street_vol</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Outstanding quantity.</td>
      </tr>
      <tr>
      <td style="text-align: left;">amplitude</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Amplitude.
      
        
      
      
       
      
      This field is in percentage form, so 20 is equivalent to 20%.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">issue_size</td>
      <td style="text-align: left;">int</td>
      <td style="text-align: left;">Issue size.</td>
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
      <td style="text-align: left;">implied_volatility</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Implied volatility.
      
        
      
      
       
      
      Only calls and puts support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">delta</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Hedging value.
      
        
      
      
       
      
      Only calls and puts support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">effective_leverage</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Effective leverage.</td>
      </tr>
      <tr>
      <td style="text-align: left;">upper_strike_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Upper bound price.
      
        
      
      
       
      
      Only Inline Warrants support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">lower_strike_price</td>
      <td style="text-align: left;">float</td>
      <td style="text-align: left;">Lower bound price.
      
        
      
      
       
      
      Only Inline Warrants support this field.
      
      
      
      </td>
      </tr>
      <tr>
      <td style="text-align: left;">inline_price_status</td>
      <td style="text-align: left;"><a
      href="/moomoo-api-doc/en/quote/quote.html#9794">PriceType</a></td>
      <td style="text-align: left;">In/out of bounds.
      
        
      
      
       
      
      Only Inline Warrants support this field.
      
      
      
      </td>
      </tr>
      </tbody>
      </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

req = WarrantRequest()
req.sort_field = SortField.TURNOVER
req.type_list = WrtType.CALL
req.cur_price_min = 0.1
req.cur_price_max = 0.2
ret, ls = quote_ctx.get_warrant("HK.00700", req)
if ret == RET_OK: # First judge whether the interface return is normal, and then fetch the data
    warrant_data_list, last_page, all_count = ls
    print(len(warrant_data_list), all_count, warrant_data_list)
    print(warrant_data_list['stock'][0]) # Take the first warrant code
    print(warrant_data_list['stock'].values.tolist()) # Convert to list
else:
    print('error: ', ls)
    
req = WarrantRequest()
req.sort_field = SortField.TURNOVER
req.issuer_list = ['UB','CS','BI']
ret, ls = quote_ctx.get_warrant(Market.HK, req)
if ret == RET_OK: 
    warrant_data_list, last_page, all_count = ls
    print(len(warrant_data_list), all_count, warrant_data_list)
else:
    print('error: ', ls)

quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
2 2 
    stock        name stock_owner  type issuer maturity_time   list_time last_trade_time  recovery_price  conversion_ratio  lot_size  strike_price  last_close_price  cur_price  price_change_val  change_rate  status  bid_price  ask_price   bid_vol  ask_vol    volume   turnover   score  premium  break_even_point  leverage    ipop  price_recovery_ratio  conversion_price  street_rate  street_vol  amplitude  issue_size  high_price  low_price  implied_volatility  delta  effective_leverage  list_timestamp  last_trade_timestamp  maturity_timestamp  upper_strike_price  lower_strike_price  inline_price_status
0   HK.20306  MBTENCT@EC2012A    HK.00700  CALL     MB    2020-12-01  2019-06-27      2020-11-25             NaN              50.0      5000        588.88             0.188      0.188             0.000     0.000000  NORMAL      0.000      0.188         0     10000           0          0.0   0.196    1.921            598.28    62.446  -0.319                   NaN              9.40        4.400     1584000      0.000    36000000       0.000      0.000              32.487  0.473              29.536    1.561565e+09          1.606234e+09        1.606752e+09                 NaN                 NaN                  NaN
1   HK.16545  SGTENCT@EC2102B    HK.00700  CALL     SG    2021-02-26  2020-07-14      2021-02-22             NaN             100.0     10000        700.00             0.147      0.143            -0.004    -2.721088  NORMAL      0.141      0.143  28000000  28000000           0          0.0  82.011   21.686            714.30    41.048 -16.142                   NaN             14.30        1.420     2130000      0.000   150000000       0.000      0.000              40.657  0.225               9.235    1.594656e+09          1.613923e+09        1.614269e+09                 NaN                 NaN                  NaN
HK.20306
['HK.20306', 'HK.16545']

200 358
    stock        name stock_owner    type issuer maturity_time   list_time last_trade_time  recovery_price  conversion_ratio  lot_size  strike_price  last_close_price  cur_price  price_change_val  change_rate      status  bid_price  ask_price   bid_vol   ask_vol  volume  turnover   score  premium  break_even_point  leverage     ipop  price_recovery_ratio  conversion_price  street_rate  street_vol  amplitude  issue_size  high_price  low_price  implied_volatility  delta  effective_leverage  list_timestamp  last_trade_timestamp  maturity_timestamp  upper_strike_price  lower_strike_price inline_price_status
0    HK.19839   PINGANRUIYINLINGYIGOUAC    HK.02318    CALL     UB    2020-12-31  2017-12-11      2020-12-24             NaN             100.0     50000         83.88             0.057      0.046            -0.011   -19.298246      NORMAL      0.043      0.046  30000000  30000000       0       0.0  39.585    1.642            88.480    18.923    3.779                   NaN             4.600         1.25     6250000        0.0   500000000         0.0        0.0              25.129  0.692              13.094    1.512922e+09          1.608739e+09        1.609344e+09                 NaN                 NaN                 NaN
1    HK.20084   PINGANZHONGYINLINGYIGOUAC    HK.02318    CALL     BI    2020-12-31  2017-12-19      2020-12-24             NaN             100.0     50000         83.88             0.059      0.050            -0.009   -15.254237      NORMAL      0.044      0.050  10000000  10000000       0       0.0   0.064    2.102            88.880    17.410    3.779                   NaN             5.000         0.07      350000        0.0   500000000         0.0        0.0              29.510  0.668              11.629    1.513613e+09          1.608739e+09        1.609344e+09                 NaN                 NaN                 NaN
......
198  HK.56886   UB#HSI  RC2301F   HK.800000    BULL     UB    2023-01-30  2020-03-24      2023-01-27         21200.0           20000.0     10000      21100.00             0.230      0.232             0.002     0.869565      NORMAL      0.232      0.233  30000000  30000000       0       0.0  46.619   -2.916         25740.000     5.714   25.655             25.062689          4640.000         0.01       40000        0.0   400000000         0.0        0.0                 NaN    NaN               5.714    1.584979e+09          1.674749e+09        1.675008e+09                 NaN                 NaN                 NaN
199  HK.56895   UB#XIAMIRC2012D    HK.01810    BULL     UB    2020-12-30  2020-03-24      2020-12-29             8.0              10.0      2000          7.60             2.010      1.930            -0.080    -3.980100      NORMAL      1.910      1.930   6000000   6000000       0       0.0   0.040    1.127            26.900     1.378  250.000            232.500000            19.300         0.10       60000        0.0    60000000         0.0        0.0                 NaN    NaN               1.378    1.584979e+09          1.609171e+09        1.609258e+09                 NaN                 NaN                 NaN
```









## <a href="#8023-2" class="header-anchor">#</a> Qot_GetWarrant.proto

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3210





`uint GetWarrant(QotGetWarrant.Request req);`  
`virtual void OnReply_GetWarrant(MMAPI_Conn client, uint nSerialNo, QotGetWarrant.Response rsp);`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
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

        QotGetWarrant.C2S c2s = QotGetWarrant.C2S.CreateBuilder()
                .SetBegin(0)
                .SetNum(50)
                .SetSortField((int)QotCommon.SortField.SortField_Code)
                .SetAscend(true)
            .Build();
        QotGetWarrant.Request req = QotGetWarrant.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetWarrant(req);
        Console.Write("Send QotGetWarrant: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetWarrant(MMAPI_Conn client, uint nSerialNo, QotGetWarrant.Response rsp)
    {
        Console.Write("Reply: QotGetWarrant: {0}\n", nSerialNo);
        Console.Write("retMsg: {0}\n", rsp.RetMsg);
        Console.Write("name: {0}, type: {1}\n", rsp.S2C.WarrantDataListList[0].Name,
            rsp.S2C.WarrantDataListList[0].Type);
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
Qot onInitConnect: ret=0 desc= connID=6825714488755091916
Send QotGetWarrant: 3
Reply: QotGetWarrant: 3
retMsg:
name: MBTENCT@EC2012A, type: 1
```









`int getWarrant(QotGetWarrant.Request req);`  
`void onReply_GetWarrant(MMAPI_Conn client, int nSerialNo, QotGetWarrant.Response rsp);`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
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

        QotGetWarrant.C2S c2s = QotGetWarrant.C2S.newBuilder()
                .setBegin(0)
                .setNum(50)
                .setSortField(QotCommon.SortField.SortField_Code_VALUE)
                .setAscend(true)
            .build();
        QotGetWarrant.Request req = QotGetWarrant.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getWarrant(req);
        System.out.printf("Send QotGetWarrant: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetWarrant(MMAPI_Conn client, int nSerialNo, QotGetWarrant.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetWarrant failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetWarrant: %s\n", json);
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
Send QotGetWarrant: 2
Receive QotGetWarrant: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "lastPage": false,
    "allCount": 15552,
    "warrantDataList": [{
      "stock": {
        "market": 1,
        "code": "10071"
      },
      "owner": {
        "market": 11,
        "code": ".DJI"
      },
      "type": 2,
      "issuer": 7,
      "maturityTime": "2021-06-18",
      "maturityTimestamp": 1.6239456E9,
      "listTime": "2020-11-10",
      "listTimestamp": 1.6049376E9,
      "lastTradeTime": "2021-06-11",
      "lastTradeTimestamp": 1.6233408E9,
      "conversionRatio": 66000.0,
      "lotSize": 10000,
      "strikePrice": 25000.0,
      "lastClosePrice": 0.01,
      "name": "HS-DJI @EP2106B",
      "curPrice": 0.01,
      "priceChangeVal": 0.0,
      "changeRate": 0.0,
      "status": 3,
      "bidPrice": 0.0,
      "askPrice": 0.0,
      "bidVol": "0",
      "askVol": "0",
      "volume": "0",
      "turnover": 0.0,
      "score": 0.02,
      "premium": 0.0,
      "breakEvenPoint": 24340.0,
      "leverage": 0.0,
      "ipop": 100.0,
      "conversionPrice": 660.0,
      "streetRate": 6.54,
      "streetVol": "13080000",
      "amplitude": 0.0,
      "issueSize": "200000000",
      "highPrice": 0.0,
      "lowPrice": 0.0,
      "impliedVolatility": 0.0,
      "delta": 0.0,
      "effectiveLeverage": 0.0
    }, ... {
      "stock": {
        "market": 1,
        "code": "11047"
      },
      "owner": {
        "market": 1,
        "code": "01211"
      },
      "type": 2,
      "issuer": 21,
      "maturityTime": "2021-11-26",
      "maturityTimestamp": 1.637856E9,
      "listTime": "2021-05-17",
      "listTimestamp": 1.6211808E9,
      "lastTradeTime": "2021-11-22",
      "lastTradeTimestamp": 1.6375104E9,
      "conversionRatio": 50.0,
      "lotSize": 25000,
      "strikePrice": 121.0,
      "lastClosePrice": 0.026,
      "name": "VT-BYD @EP2111A",
      "curPrice": 0.026,
      "priceChangeVal": 0.0,
      "changeRate": 0.0,
      "status": 1,
      "bidPrice": 0.026,
      "askPrice": 0.029,
      "bidVol": "125000",
      "askVol": "600000",
      "volume": "0",
      "turnover": 0.0,
      "score": 0.008,
      "premium": 47.407,
      "breakEvenPoint": 119.7,
      "leverage": 175.076,
      "ipop": -88.099,
      "conversionPrice": 1.3,
      "streetRate": 2.25,
      "streetVol": "900000",
      "amplitude": 0.0,
      "issueSize": "40000000",
      "highPrice": 0.0,
      "lowPrice": 0.0,
      "impliedVolatility": 58.629,
      "delta": -0.032,
      "effectiveLeverage": -5.602
    }]
  }
}
```









`moomoo::u32_t GetWarrant(const Qot_GetWarrant::Request &stReq);`  
`virtual void OnReply_GetWarrant(moomoo::u32_t nSerialNo, const Qot_GetWarrant::Response &stRsp) = 0;`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
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
        Qot_GetWarrant::Request req;
        Qot_GetWarrant::C2S *c2s = req.mutable_c2s();
        c2s->set_begin(0);
        c2s->set_num(50);
        c2s->set_sortfield(1);
        c2s->set_ascend(false);

        m_GetWarrantSerialNo = m_pQotApi->GetWarrant(req);
        cout << "Request GetWarrant SerialNo: " << m_GetWarrantSerialNo << endl;
    }

    virtual void OnReply_GetWarrant(moomoo::u32_t nSerialNo, const Qot_GetWarrant::Response &stRsp){
        if(nSerialNo == m_GetWarrantSerialNo)
        {
            cout << "OnReply_GetWarrant SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetWarrantSerialNo;
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
Request GetWarrant SerialNo: 4
OnReply_GetWarrant SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "lastPage": false,
  "allCount": 15685,
  "warrantDataList": [
   {
    "stock": {
     "market": 1,
     "code": "69999"
    },
    "owner": {
     "market": 1,
     "code": "01211"
    },
    "type": 3,
    "issuer": 1,
    "maturityTime": "2022-02-28",
    "maturityTimestamp": 1645977600,
    "listTime": "2021-06-11",
    "listTimestamp": 1623340800,
    "lastTradeTime": "2022-02-25",
    "lastTradeTimestamp": 1645718400,
    "recoveryPrice": 193,
    "conversionRatio": 500,
    "lotSize": 25000,
    "strikePrice": 189,
    "lastClosePrice": 0,
    "name": "SG#BYD  RC2202P",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 4,
    "bidPrice": 0,
    "askPrice": 0,
    "bidVol": "0",
    "askVol": "0",
    "volume": "0",
    "turnover": 0,
    "score": 0,
    "premium": -5.12,
    "breakEvenPoint": 189,
    "leverage": 0,
    "ipop": 5.396,
    "priceRecoveryRatio": 3.2124352331606163,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "150000000",
    "highPrice": 0,
    "lowPrice": 0,
    "effectiveLeverage": 0
   },
...
   {
    "stock": {
     "market": 1,
     "code": "69897"
    },
    "owner": {
     "market": 1,
     "code": "00700"
    },
    "type": 4,
    "issuer": 3,
    "maturityTime": "2021-12-30",
    "maturityTimestamp": 1640793600,
    "listTime": "2021-06-11",
    "listTimestamp": 1623340800,
    "lastTradeTime": "2021-12-29",
    "lastTradeTimestamp": 1640707200,
    "recoveryPrice": 608,
    "conversionRatio": 500,
    "lotSize": 5000,
    "strikePrice": 610.8,
    "lastClosePrice": 0,
    "name": "CS#TENCTRP2112G",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 4,
    "bidPrice": 0,
    "askPrice": 0,
    "bidVol": "0",
    "askVol": "0",
    "volume": "0",
    "turnover": 0,
    "score": 0,
    "premium": -1.715,
    "breakEvenPoint": 610.8,
    "leverage": 0,
    "ipop": 1.686,
    "priceRecoveryRatio": -1.2335526315789473,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "100000000",
    "highPrice": 0,
    "lowPrice": 0,
    "effectiveLeverage": 0
   }
  ]
 }
}
```









`GetWarrant(req);`

- **Description**

  Get Filtered Warrant (for HK market only)

- **Parameters**



``` protobuf
message C2S
{
    required int32 begin = 1; //Data starting point
    required int32 num = 2; //The number of requested data, the maximum is 200
    required int32 sortField = 3;//Qot_Common. SortField, according to which field to sort
    required bool ascend = 4;//True: ascending order, False: descending order

    //The following are filter conditions, optional fields, not filling in means no restrictions
    optional Qot_Common.Security owner = 5; //The underlying stock
    repeated int32 typeList = 6; //Qot_Common. WarrantType, Warrant type filter list
    repeated int32 issuerList = 7; //Qot_Common. Issuer, issuer filter list
    optional string maturityTimeMin = 8; //The start time of the maturity date filter range
    optional string maturityTimeMax = 9; //The end time of the maturity date filter range
    optional int32 ipoPeriod = 10; //Qot_Common.IpoPeriod. Listing period
    optional int32 priceType = 11; //Qot_Common.PriceType. In/out of the money. (The Inline Warrant is not currently supported.)
    optional int32 status = 12; //Qot_Common.WarrantStatus. Warrant Status
    optional double curPriceMin = 13; //The filter lower limit (closed interval) of the latest price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double curPriceMax = 14; //The filter upper limit (closed interval) of the latest price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMin = 15; //The lower filter limit (closed interval) of the strike price. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double strikePriceMax = 16; //The upper filter limit (closed interval) of the strike price. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double streetMin = 17; //The lower limit (closed interval) of Outstanding percentage. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double streetMax = 18; //The upper limit (closed interval) of Outstanding percentage. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMin = 19; //The lower filter limit (closed interval) of the conversion ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double conversionMax = 20; //The upper filter limit (closed interval) of the conversion ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional uint64 volMin = 21; //The lower filter limit (closed interval) of the volume. If not passed, the lower limit is -∞
    optional uint64 volMax = 22; //The upper filter limit (closed interval) of the volume. If not passed, the upper limit is +∞
    optional double premiumMin = 23; //The lower filter limit (closed interval) of premium value. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double premiumMax = 24; //The upper filter limit (closed interval) of premium value. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMin = 25; //The lower filter limit (closed interval) of the leverage ratio. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double leverageRatioMax = 26; //The upper filter limit (closed interval) of the leverage ratio. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMin = 27;//The lower filter limit (closed interval) of the hedge value Delta. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 28;//The upper filter limit (closed interval) of the hedge value Delta. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMin = 29; //The lower filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double impliedMax = 30; //The upper filter limit (closed interval) of the implied volatility. Only calls and puts support this filtering field. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMin = 31; //The lower filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the lower limit is -∞(3 decimal place accuracy, the excess part is discarded)
    optional double recoveryPriceMax = 32; //The upper filter limit (closed interval) of the recovery price. only CBBCs support this field to filter. If not passed, the upper limit is +∞(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMin = 33;//The lower filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the lower limit is -∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
    optional double priceRecoveryRatioMax = 34;//The upper filter limit (closed interval) of the price recovery ratio. Only CBBCs support this field. If not passed, the upper limit is +∞ (This field is in percentage form, so 20 is equivalent to 20%.)(3 decimal place accuracy, the excess part is discarded)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For IPO period, refer to
>   [IpoPeriod](/moomoo-api-doc/en/quote/quote.html#2961)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)

- **Return**



``` protobuf
message WarrantData
{
    //Static data item
    required Qot_Common.Security stock = 1; //Security
    required Qot_Common.Security owner = 2; //The underlying stock
    required int32 type = 3; //Qot_Common.WarrantType. Warrant Type
    required int32 issuer = 4; //Qot_Common.Issuer. Issuer
    required string maturityTime = 5; //Maturity date
    optional double maturityTimestamp = 6; //Maturity date timestamp
    required string listTime = 7; //Listing time (Format: yyyy-MM-dd)
    optional double listTimestamp = 8; //Listing timestamp
    required string lastTradeTime = 9; //Last trading day
    optional double lastTradeTimestamp = 10; //Last trading day timestamp
    optional double recoveryPrice = 11; //Recovery price, only CBBC supports this field
    required double conversionRatio = 12; //Share conversion ratio
    required int32 lotSize = 13; //Quantity per lot
    required double strikePrice = 14; //Strike price
    required double lastClosePrice = 15; //Yesterday's close
    required string name = 16; //Name

    //Dynamic data item
    required double curPrice = 17; //Current price
    required double priceChangeVal = 18; //Change amount
    required double changeRate = 19; //Change rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required int32 status = 20; //Qot_Common.WarrantStatus. Warrant Status
    required double bidPrice = 21; //Bid price
    required double askPrice = 22; //Ask price
    required int64 bidVol = 23; //Bid volume
    required int64 askVol = 24; //Ask volume
    required int64 volume = 25; //Volume
    required double turnover = 26; //Turnover
    required double score = 27; //Comprehensive score
    required double premium = 28; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double breakEvenPoint = 29; //Break point
    required double leverage = 30; //Leverage ratio (times)
    required double ipop = 31; //In/out of the money, positive number means in the money, negative number means out of the money (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double priceRecoveryRatio = 32; //Price recovery ratio of the underlying stock distance, only the CBBC supports this field (This field is in percentage form, so 20 is equivalent to 20%.)
    required double conversionPrice = 33; //Conversion price
    required double streetRate = 34; //Outstanding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 streetVol = 35; //Outstanding quantity
    required double amplitude = 36; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    required int64 issueSize = 37; //Issuance
    required double highPrice = 39; //High
    required double lowPrice = 40; //Low
    optional double impliedVolatility = 41; //Implied volatility, only calls and puts support this field
    optional double delta = 42; //Hedging value, only calls and puts support this field
    required double effectiveLeverage = 43; //Effective leverage
    optional double upperStrikePrice = 44; //Upper bound price, only Inline Warrants support this field
    optional double lowerStrikePrice = 45; //Lower bound price, only Inline Warrants support this field
    optional int32 inLinePriceStatus = 46; //Qot_Common.PriceType, in/out of bounds status, only Inline Warrants support this field
}

message S2C
{
    required bool lastPage = 1; //Is it the last page, false: not the last page, and remaining warrant record has not been returned; true: it is the last page
    required int32 allCount = 2; //The number of all data requested by this condition
    repeated WarrantData warrantDataList = 3; //Warrant data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the warrant types, refer to
>   [WarrantType](/moomoo-api-doc/en/quote/quote.html#2421)
> - For the issuer filter list, refer to
>   [Issuer](/moomoo-api-doc/en/quote/quote.html#5122)
> - For in/out of bound, refer to
>   [PriceType](/moomoo-api-doc/en/quote/quote.html#9794)
> - For warrant status, refer to
>   [WarrantStatus](/moomoo-api-doc/en/quote/quote.html#5892)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetWarrant(){
    const { RetType } = Common
    const { SortField, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    begin: 0,
                    num: 2,
                    sortField: SortField.SortField_CurPrice,
                    ascend: true,

                    owner:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                },
            };

            websocket.GetWarrant(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("Warrant: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Warrant: errCode 0, retMsg , retType 0
{
  "lastPage": false,
  "allCount": 1380,
  "warrantDataList": [{
    "stock": {
      "market": 1,
      "code": "26508"
    },
    "owner": {
      "market": 1,
      "code": "00700"
    },
    "type": 1,
    "issuer": 6,
    "maturityTime": "2022-01-26",
    "maturityTimestamp": 1643126400,
    "listTime": "2021-09-14",
    "listTimestamp": 1631548800,
    "lastTradeTime": "2022-01-20",
    "lastTradeTimestamp": 1642608000,
    "conversionRatio": 100,
    "lotSize": 10000,
    "strikePrice": 575.5,
    "lastClosePrice": 0,
    "name": "GSTENCT@EC2201M",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 1,
    "bidPrice": 0.179,
    "askPrice": 0.18,
    "bidVol": "10280000",
    "askVol": "10280000",
    "volume": "0",
    "turnover": 0,
    "score": 52.327,
    "premium": 19.596,
    "breakEvenPoint": 575.5,
    "leverage": 0,
    "ipop": -16.385,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "120000000",
    "highPrice": 0,
    "lowPrice": 0,
    "impliedVolatility": 0,
    "delta": 0,
    "effectiveLeverage": 0
  }, {
    "stock": {
      "market": 1,
      "code": "52325"
    },
    "owner": {
      "market": 1,
      "code": "00700"
    },
    "type": 3,
    "issuer": 7,
    "maturityTime": "2022-04-29",
    "maturityTimestamp": 1651161600,
    "listTime": "2021-09-14",
    "listTimestamp": 1631548800,
    "lastTradeTime": "2022-04-28",
    "lastTradeTimestamp": 1651075200,
    "recoveryPrice": 492.88,
    "conversionRatio": 500,
    "lotSize": 50000,
    "strikePrice": 488.88,
    "lastClosePrice": 0,
    "name": "HS#TENCTRC2204E",
    "curPrice": 0,
    "priceChangeVal": 0,
    "changeRate": 0,
    "status": 3,
    "bidPrice": 0,
    "askPrice": 0,
    "bidVol": "0",
    "askVol": "0",
    "volume": "0",
    "turnover": 0,
    "score": 0.24,
    "premium": 1.596,
    "breakEvenPoint": 488.88,
    "leverage": 0,
    "ipop": -1.57,
    "priceRecoveryRatio": -2.3697451712384368,
    "conversionPrice": 0,
    "streetRate": 0,
    "streetVol": "0",
    "amplitude": 0,
    "issueSize": "100000000",
    "highPrice": 0,
    "lowPrice": 0,
    "effectiveLeverage": 0
  }]
}
stop
```











Interface Limitations

- Hong Kong stock BMP permission does not support calling this API
- A maximum of 60 requests per 30 seconds
- The maximum number of data per request is 200













