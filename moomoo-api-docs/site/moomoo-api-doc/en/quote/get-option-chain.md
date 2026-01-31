



# <a href="#8520" class="header-anchor">#</a> Get Option Chain









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_option_chain(code, index_option_type=IndexOptionType.NORMAL, start=None, end=None, option_type=OptionType.ALL, option_cond_type=OptionCondType.ALL, data_filter=None)`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

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
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Code of underlying stock.</td>
  </tr>
  <tr>
  <td style="text-align: left;">index_option_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
  <td style="text-align: left;">Index option type.
  
    
  
  
   
  
  Only valid for HK index options. Ignore this parameter for stocks, ETFs,
  and US index options.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start date, for expiration date.
  
    
  
  
   
  
  For example: "2017-08-01".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End date (including this day), for
  expiration date.
  
    
  
  
   
  
  For example: "2017-08-30".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">option_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
  <td style="text-align: left;">Option type for call/put.
  
    
  
  
   
  
  Default all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">option_cond_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9027">OptionCondType</a></td>
  <td style="text-align: left;">Option type for in/out of the money.
  
    
  
  
   
  
  Default all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">data_filter</td>
  <td style="text-align: left;"><em>OptionDataFilter</em></td>
  <td style="text-align: left;">Data filter condition.
  
    
  
  
   
  
  No filter by default.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows:

    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 30 days before ***end***. |
    | str | None | ***end*** is 30 days after ***start***. |
    | None | None | ***start*** is the current date, ***end*** is 30 days later. |

  - *OptionDataFilter* fields are as follows

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
    <td style="text-align: left;">implied_volatility_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of implied volatility.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_volatility_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of implied volatility.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Delta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Delta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">gamma_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Gamma.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">gamma_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Gamma.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vega_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Vega.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vega_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Vega.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">theta_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Theta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">theta_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Theta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">rho_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Rho.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">rho_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Rho.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_open_interest_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of net open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_open_interest_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of net open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open_interest_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open_interest_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Volume.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Volume.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
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
  <td>If ret == RET_OK, option chain data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Option chain data format as follows:
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
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of shares per lot, number of shares
    per contract for options.
    
      
    
    
     
    
    Index options do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Stock type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
    <td style="text-align: left;">Option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Underlying stock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Exercise date.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether is suspended.
    
      
    
    
     
    
    True: suspended.<br />
    False: not suspended
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Stock ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
    <td style="text-align: left;">Index option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">expiration_cycle</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#5181">ExpirationCycle</a></td>
    <td style="text-align: left;">Expiration cycle type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_standard_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8553">OptionStandardType</a></td>
    <td style="text-align: left;">Option standard type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_settlement_mode</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6656">OptionSettlementMode</a></td>
    <td style="text-align: left;">Option settlement mode.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
import time
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret1, data1 = quote_ctx.get_option_expiration_date(code='HK.00700')

filter1 = OptionDataFilter()
filter1.delta_min = 0
filter1.delta_max = 0.1

if ret1 == RET_OK:
    expiration_date_list = data1['strike_time'].values.tolist()
    for date in expiration_date_list:
        ret2, data2 = quote_ctx.get_option_chain(code='HK.00700', start=date, end=date, data_filter=filter1)
        if ret2 == RET_OK:
            print(data2)
            print(data2['code'][0])  # Take the first stock code
            print(data2['code'].values.tolist())  # Convert to list
        else:
            print('error:', data2)
        time.sleep(3)
else:
    print('error:', data1)
quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
                     code                 name  lot_size stock_type option_type stock_owner strike_time  strike_price  suspension  stock_id index_option_type expiration_cycle option_standard_type option_settlement_mode
0     HK.TCH210429C350000   腾讯 210429 350.00 购       100       DRVT        CALL    HK.00700  2021-04-29         350.0       False  80235167               N/A        WEEK        STANDARD          N/A        
1     HK.TCH210429P350000   腾讯 210429 350.00 沽       100       DRVT         PUT    HK.00700  2021-04-29         350.0       False  80235247               N/A        WEEK        STANDARD          N/A        
2     HK.TCH210429C360000   腾讯 210429 360.00 购       100       DRVT        CALL    HK.00700  2021-04-29         360.0       False  80235163               N/A        WEEK        STANDARD          N/A        
3     HK.TCH210429P360000   腾讯 210429 360.00 沽       100       DRVT         PUT    HK.00700  2021-04-29         360.0       False  80235246               N/A        WEEK        STANDARD          N/A        
4     HK.TCH210429C370000   腾讯 210429 370.00 购       100       DRVT        CALL    HK.00700  2021-04-29         370.0       False  80235165               N/A        WEEK        STANDARD          N/A        
5     HK.TCH210429P370000   腾讯 210429 370.00 沽       100       DRVT         PUT    HK.00700  2021-04-29         370.0       False  80235248               N/A        WEEK        STANDARD          N/A        
HK.TCH210429C350000
['HK.TCH210429C350000', 'HK.TCH210429P350000', 'HK.TCH210429C360000', 'HK.TCH210429P360000', 'HK.TCH210429C370000', 'HK.TCH210429P370000']
...
                   code                name  lot_size stock_type option_type stock_owner strike_time  strike_price  suspension  stock_id index_option_type expiration_cycle option_standard_type option_settlement_mode
0   HK.TCH220330C490000  腾讯 220330 490.00 购       100       DRVT        CALL    HK.00700  2022-03-30         490.0       False  80235143               N/A        WEEK        STANDARD         N/A            
1   HK.TCH220330P490000  腾讯 220330 490.00 沽       100       DRVT         PUT    HK.00700  2022-03-30         490.0       False  80235193               N/A        WEEK        STANDARD         N/A            
2   HK.TCH220330C500000  腾讯 220330 500.00 购       100       DRVT        CALL    HK.00700  2022-03-30         500.0       False  80233887               N/A        WEEK        STANDARD         N/A            
3   HK.TCH220330P500000  腾讯 220330 500.00 沽       100       DRVT         PUT    HK.00700  2022-03-30         500.0       False  80233912               N/A        WEEK        STANDARD         N/A            
4   HK.TCH220330C510000  腾讯 220330 510.00 购       100       DRVT        CALL    HK.00700  2022-03-30         510.0       False  80233747               N/A        WEEK        STANDARD             N/A           
5   HK.TCH220330P510000  腾讯 220330 510.00 沽       100       DRVT         PUT    HK.00700  2022-03-30         510.0       False  80233766               N/A        WEEK        STANDARD             N/A           
HK.TCH220330C490000
['HK.TCH220330C490000', 'HK.TCH220330P490000', 'HK.TCH220330C500000', 'HK.TCH220330P500000', 'HK.TCH220330C510000', 'HK.TCH220330P510000']
```









## <a href="#1122" class="header-anchor">#</a> Qot_GetOptionChain.proto

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Protocol ID**

  3209

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}

//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf
message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3209





`uint GetOptionChain(QotGetOptionChain.Request req);`  
`virtual void OnReply_GetOptionChain(FTAPI_Conn client, uint nSerialNo, QotGetOptionChain.Response rsp);`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}

//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf
message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
            .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
            .SetCode("00700")
            .Build();
        QotGetOptionChain.C2S c2s = QotGetOptionChain.C2S.CreateBuilder()
            .SetOwner(sec)
            .SetBeginTime("2020-11-01")
            .SetEndTime("2020-12-01")
            .Build();
        QotGetOptionChain.Request req = QotGetOptionChain.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetOptionChain(req);
        Console.Write("Send QotGetOptionChain: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetOptionChain(FTAPI_Conn client, uint nSerialNo, QotGetOptionChain.Response rsp)
    {
        Console.Write("Reply: QotGetOptionChain: {0}\n", nSerialNo);
        Console.Write("strikeTime: {0}, name: {1} \n", 
            rsp.S2C.OptionChainList[0].StrikeTime,
            rsp.S2C.OptionChainList[0].OptionList[0].Call.Basic.Name);
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
Qot onInitConnect: ret=0 desc= connID=6825705573658441031
Send QotGetOptionChain: 3
Reply: QotGetOptionChain: 3
strikeTime: 2021-07-29, name: TCH 210729 400.00 C
```









`int getOptionChain(QotGetOptionChain.Request req);`  
`void onReply_GetOptionChain(FTAPI_Conn client, int nSerialNo, QotGetOptionChain.Response rsp);`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}

//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf
message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        QotGetOptionChain.C2S c2s = QotGetOptionChain.C2S.newBuilder()
                .setOwner(sec)
                .setBeginTime("2021-06-01")
                .setEndTime("2021-07-01")
            .build();
        QotGetOptionChain.Request req = QotGetOptionChain.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getOptionChain(req);
        System.out.printf("Send QotGetOptionChain: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOptionChain(FTAPI_Conn client, int nSerialNo, QotGetOptionChain.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetOptionChain failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetOptionChain: %s\n", json);
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
Send QotGetOptionChain: 2
Receive QotGetOptionChain: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "optionChain": [{
      "strikeTime": "2021-06-29",
      "option": [{
        "call": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629C295000"
            },
            "id": "80143386",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 295.00 C",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 1,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 295.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        },
        "put": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629P295000"
            },
            "id": "80143074",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 295.00 P",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 2,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 295.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        }
      }, ... {
        "call": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629C1050000"
            },
            "id": "80223489",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 1050.00 C",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 1,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 1050.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        },
        "put": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629P1050000"
            },
            "id": "80223488",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 1050.00 P",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 2,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 1050.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        }
      }],
      "strikeTimestamp": 1.624896E9
    }]
  }
}
```









`Futu::u32_t GetOptionChain(const Qot_GetOptionChain::Request &stReq);`  
`virtual void OnReply_GetOptionChain(Futu::u32_t nSerialNo, const Qot_GetOptionChain::Response &stRsp) = 0;`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}


//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf

message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        Qot_GetOptionChain::Request req;
        Qot_GetOptionChain::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_owner();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_begintime("2021-06-07");
        c2s->set_endtime("2021-07-01");

    m_GetOptionChainSerialNo = m_pQotApi->GetOptionChain(req);
    cout << "Request GetOptionChain SerialNo: " << m_GetOptionChainSerialNo << endl;
    }

    virtual void OnReply_GetOptionChain(Futu::u32_t nSerialNo, const Qot_GetOptionChain::Response &stRsp){
    if(nSerialNo == m_GetOptionChainSerialNo)
    {
        cout << "OnReply_GetOptionChain SerialNo: " << nSerialNo << endl; 
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }
    }

protected:
    FTAPI_Qot *m_pQotApi;

  Futu::u32_t m_GetOptionChainSerialNo;
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
Request GetOptionChain SerialNo: 4
OnReply_GetOptionChain SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "optionChain": [
   {
    "strikeTime": "2021-06-29",
    "option": [
     {
      "call": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629C295000"
        },
        "id": "80143386",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 295.00 C",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 1,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 295,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      },
      "put": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629P295000"
        },
        "id": "80143074",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 295.00 P",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 2,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 295,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      }
     },
...
     {
      "call": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629C1050000"
        },
        "id": "80223489",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 1050.00 C",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 1,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 1050,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      },
      "put": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629P1050000"
        },
        "id": "80223488",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 1050.00 P",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 2,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 1050,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      }
     }
    ],
    "strikeTimestamp": 1624896000
   }
  ]
 }
}
```









`GetOptionChain(req);`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}


//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf

message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetOptionChain(){
    const { RetType } = Common
    const {  QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    owner:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    beginTime: "2021-09-01",
                    endTime: "2021-09-30",
                },
            };

            websocket.GetOptionChain(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("OptionChain: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
OptionChain: errCode 0, retMsg , retType 0
{
  "optionChain": [{
    "strikeTime": "2021-09-29",
    "option": [{
      "call": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929C300000"
          },
          "id": "80287116",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 300.00 C",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 1,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 300,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      },
      "put": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929P300000"
          },
          "id": "80287124",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 300.00 P",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 2,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 300,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      }
    }, {
      "call": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929C310000"
          },
          "id": "80277871",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 310.00 C",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 1,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 310,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      },
      "put": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929P310000"
          },
          "id": "80277826",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 310.00 P",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 2,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 310,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      }
    }, ..., {
      "call": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929C950000"
          },
          "id": "80215136",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 950.00 C",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 1,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 950,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      },
      "put": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929P950000"
          },
          "id": "80215157",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 950.00 P",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 2,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 950,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      }
    }],
    "strikeTimestamp": 1632844800
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- The upper limit of the incoming time span is 30 days





Tips

- This interface does not support the query of expired option chains,
  please enter today or future date to the **End date** parameter.
- Open interest (OI) is updated daily and the specific timing depends on
  the exchange.
  - For U.S. stock options, the data is updated during the PRE_MARKET
    session.
  - For Hong Kong stock options, the data is updated after the Regular
    Trading Hours.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_option_chain(code, index_option_type=IndexOptionType.NORMAL, start=None, end=None, option_type=OptionType.ALL, option_cond_type=OptionCondType.ALL, data_filter=None)`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

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
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Code of underlying stock.</td>
  </tr>
  <tr>
  <td style="text-align: left;">index_option_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
  <td style="text-align: left;">Index option type.
  
    
  
  
   
  
  Only valid for HK index options. Ignore this parameter for stocks, ETFs,
  and US index options.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start date, for expiration date.
  
    
  
  
   
  
  For example: "2017-08-01".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End date (including this day), for
  expiration date.
  
    
  
  
   
  
  For example: "2017-08-30".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">option_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
  <td style="text-align: left;">Option type for call/put.
  
    
  
  
   
  
  Default all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">option_cond_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9027">OptionCondType</a></td>
  <td style="text-align: left;">Option type for in/out of the money.
  
    
  
  
   
  
  Default all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">data_filter</td>
  <td style="text-align: left;"><em>OptionDataFilter</em></td>
  <td style="text-align: left;">Data filter condition.
  
    
  
  
   
  
  No filter by default.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows:

    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 30 days before ***end***. |
    | str | None | ***end*** is 30 days after ***start***. |
    | None | None | ***start*** is the current date, ***end*** is 30 days later. |

  - *OptionDataFilter* fields are as follows

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
    <td style="text-align: left;">implied_volatility_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of implied volatility.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_volatility_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of implied volatility.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Delta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Delta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">gamma_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Gamma.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">gamma_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Gamma.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vega_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Vega.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vega_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Vega.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">theta_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Theta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">theta_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Theta.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">rho_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Greek value Rho.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">rho_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Greek value Rho.
    
      
    
    
     
    
    3 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_open_interest_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of net open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">net_open_interest_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of net open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open_interest_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open_interest_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of open contract number.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Min value of Volume.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">vol_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Max value of Volume.
    
      
    
    
     
    
    0 decimal place accuracy, the excess part is discarded.
    
    
    
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
  <td>If ret == RET_OK, option chain data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Option chain data format as follows:
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
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of shares per lot, number of shares
    per contract for options.
    
      
    
    
     
    
    Index options do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Stock type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
    <td style="text-align: left;">Option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Underlying stock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Exercise date.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether is suspended.
    
      
    
    
     
    
    True: suspended.<br />
    False: not suspended
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Stock ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
    <td style="text-align: left;">Index option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">expiration_cycle</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#5181">ExpirationCycle</a></td>
    <td style="text-align: left;">Expiration cycle type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_standard_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8553">OptionStandardType</a></td>
    <td style="text-align: left;">Option standard type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_settlement_mode</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6656">OptionSettlementMode</a></td>
    <td style="text-align: left;">Option settlement mode.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
import time
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret1, data1 = quote_ctx.get_option_expiration_date(code='HK.00700')

filter1 = OptionDataFilter()
filter1.delta_min = 0
filter1.delta_max = 0.1

if ret1 == RET_OK:
    expiration_date_list = data1['strike_time'].values.tolist()
    for date in expiration_date_list:
        ret2, data2 = quote_ctx.get_option_chain(code='HK.00700', start=date, end=date, data_filter=filter1)
        if ret2 == RET_OK:
            print(data2)
            print(data2['code'][0])  # Take the first stock code
            print(data2['code'].values.tolist())  # Convert to list
        else:
            print('error:', data2)
        time.sleep(3)
else:
    print('error:', data1)
quote_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
                     code                 name  lot_size stock_type option_type stock_owner strike_time  strike_price  suspension  stock_id index_option_type expiration_cycle option_standard_type
0     HK.TCH210429C350000   腾讯 210429 350.00 购       100       DRVT        CALL    HK.00700  2021-04-29         350.0       False  80235167               N/A        WEEK        STANDARD        
1     HK.TCH210429P350000   腾讯 210429 350.00 沽       100       DRVT         PUT    HK.00700  2021-04-29         350.0       False  80235247               N/A        WEEK        STANDARD
2     HK.TCH210429C360000   腾讯 210429 360.00 购       100       DRVT        CALL    HK.00700  2021-04-29         360.0       False  80235163               N/A        WEEK        STANDARD
3     HK.TCH210429P360000   腾讯 210429 360.00 沽       100       DRVT         PUT    HK.00700  2021-04-29         360.0       False  80235246               N/A        WEEK        STANDARD
4     HK.TCH210429C370000   腾讯 210429 370.00 购       100       DRVT        CALL    HK.00700  2021-04-29         370.0       False  80235165               N/A        WEEK        STANDARD
5     HK.TCH210429P370000   腾讯 210429 370.00 沽       100       DRVT         PUT    HK.00700  2021-04-29         370.0       False  80235248               N/A        WEEK        STANDARD
HK.TCH210429C350000
['HK.TCH210429C350000', 'HK.TCH210429P350000', 'HK.TCH210429C360000', 'HK.TCH210429P360000', 'HK.TCH210429C370000', 'HK.TCH210429P370000']
...
                   code                name  lot_size stock_type option_type stock_owner strike_time  strike_price  suspension  stock_id index_option_type expiration_cycle option_standard_type
0   HK.TCH220330C490000  腾讯 220330 490.00 购       100       DRVT        CALL    HK.00700  2022-03-30         490.0       False  80235143               N/A        WEEK        STANDARD    
1   HK.TCH220330P490000  腾讯 220330 490.00 沽       100       DRVT         PUT    HK.00700  2022-03-30         490.0       False  80235193               N/A        WEEK        STANDARD    
2   HK.TCH220330C500000  腾讯 220330 500.00 购       100       DRVT        CALL    HK.00700  2022-03-30         500.0       False  80233887               N/A        WEEK        STANDARD    
3   HK.TCH220330P500000  腾讯 220330 500.00 沽       100       DRVT         PUT    HK.00700  2022-03-30         500.0       False  80233912               N/A        WEEK        STANDARD    
4   HK.TCH220330C510000  腾讯 220330 510.00 购       100       DRVT        CALL    HK.00700  2022-03-30         510.0       False  80233747               N/A        WEEK        STANDARD    
5   HK.TCH220330P510000  腾讯 220330 510.00 沽       100       DRVT         PUT    HK.00700  2022-03-30         510.0       False  80233766               N/A        WEEK        STANDARD    
HK.TCH220330C490000
['HK.TCH220330C490000', 'HK.TCH220330P490000', 'HK.TCH220330C500000', 'HK.TCH220330P500000', 'HK.TCH220330C510000', 'HK.TCH220330P510000']
```









## <a href="#1122-2" class="header-anchor">#</a> Qot_GetOptionChain.proto

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Protocol ID**

  3209

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}

//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf
message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3209





`uint GetOptionChain(QotGetOptionChain.Request req);`  
`virtual void OnReply_GetOptionChain(MMAPI_Conn client, uint nSerialNo, QotGetOptionChain.Response rsp);`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}

//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf
message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
            .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
            .SetCode("00700")
            .Build();
        QotGetOptionChain.C2S c2s = QotGetOptionChain.C2S.CreateBuilder()
            .SetOwner(sec)
            .SetBeginTime("2020-11-01")
            .SetEndTime("2020-12-01")
            .Build();
        QotGetOptionChain.Request req = QotGetOptionChain.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetOptionChain(req);
        Console.Write("Send QotGetOptionChain: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetOptionChain(MMAPI_Conn client, uint nSerialNo, QotGetOptionChain.Response rsp)
    {
        Console.Write("Reply: QotGetOptionChain: {0}\n", nSerialNo);
        Console.Write("strikeTime: {0}, name: {1} \n", 
            rsp.S2C.OptionChainList[0].StrikeTime,
            rsp.S2C.OptionChainList[0].OptionList[0].Call.Basic.Name);
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
Qot onInitConnect: ret=0 desc= connID=6825705573658441031
Send QotGetOptionChain: 3
Reply: QotGetOptionChain: 3
strikeTime: 2021-07-29, name: TCH 210729 400.00 C
```









`int getOptionChain(QotGetOptionChain.Request req);`  
`void onReply_GetOptionChain(MMAPI_Conn client, int nSerialNo, QotGetOptionChain.Response rsp);`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}

//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf
message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        QotGetOptionChain.C2S c2s = QotGetOptionChain.C2S.newBuilder()
                .setOwner(sec)
                .setBeginTime("2021-06-01")
                .setEndTime("2021-07-01")
            .build();
        QotGetOptionChain.Request req = QotGetOptionChain.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getOptionChain(req);
        System.out.printf("Send QotGetOptionChain: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOptionChain(MMAPI_Conn client, int nSerialNo, QotGetOptionChain.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetOptionChain failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetOptionChain: %s\n", json);
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
Send QotGetOptionChain: 2
Receive QotGetOptionChain: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "optionChain": [{
      "strikeTime": "2021-06-29",
      "option": [{
        "call": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629C295000"
            },
            "id": "80143386",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 295.00 C",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 1,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 295.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        },
        "put": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629P295000"
            },
            "id": "80143074",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 295.00 P",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 2,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 295.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        }
      }, ... {
        "call": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629C1050000"
            },
            "id": "80223489",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 1050.00 C",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 1,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 1050.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        },
        "put": {
          "basic": {
            "security": {
              "market": 1,
              "code": "TCH210629P1050000"
            },
            "id": "80223488",
            "lotSize": 100,
            "secType": 8,
            "name": "TCH 210629 1050.00 P",
            "listTime": "",
            "delisting": false
          },
          "optionExData": {
            "type": 2,
            "owner": {
              "market": 1,
              "code": "00700"
            },
            "strikeTime": "2021-06-29",
            "strikePrice": 1050.0,
            "suspend": false,
            "market": "",
            "strikeTimestamp": 1.624896E9,
            "expirationCycle": 1,
            "optionStandardType": 1,
            "optionSettlementMode": 2,
          }
        }
      }],
      "strikeTimestamp": 1.624896E9
    }]
  }
}
```









`moomoo::u32_t GetOptionChain(const Qot_GetOptionChain::Request &stReq);`  
`virtual void OnReply_GetOptionChain(moomoo::u32_t nSerialNo, const Qot_GetOptionChain::Response &stRsp) = 0;`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}


//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf

message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        Qot_GetOptionChain::Request req;
        Qot_GetOptionChain::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_owner();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_begintime("2021-06-07");
        c2s->set_endtime("2021-07-01");

    m_GetOptionChainSerialNo = m_pQotApi->GetOptionChain(req);
    cout << "Request GetOptionChain SerialNo: " << m_GetOptionChainSerialNo << endl;
    }

    virtual void OnReply_GetOptionChain(moomoo::u32_t nSerialNo, const Qot_GetOptionChain::Response &stRsp){
    if(nSerialNo == m_GetOptionChainSerialNo)
    {
        cout << "OnReply_GetOptionChain SerialNo: " << nSerialNo << endl; 
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }
    }

protected:
    MMAPI_Qot *m_pQotApi;

  moomoo::u32_t m_GetOptionChainSerialNo;
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
Request GetOptionChain SerialNo: 4
OnReply_GetOptionChain SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "optionChain": [
   {
    "strikeTime": "2021-06-29",
    "option": [
     {
      "call": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629C295000"
        },
        "id": "80143386",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 295.00 C",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 1,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 295,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      },
      "put": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629P295000"
        },
        "id": "80143074",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 295.00 P",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 2,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 295,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      }
     },
...
     {
      "call": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629C1050000"
        },
        "id": "80223489",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 1050.00 C",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 1,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 1050,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      },
      "put": {
       "basic": {
        "security": {
         "market": 1,
         "code": "TCH210629P1050000"
        },
        "id": "80223488",
        "lotSize": 100,
        "secType": 8,
        "name": "TCH 210629 1050.00 P",
        "listTime": "",
        "delisting": false
       },
       "optionExData": {
        "type": 2,
        "owner": {
         "market": 1,
         "code": "00700"
        },
        "strikeTime": "2021-06-29",
        "strikePrice": 1050,
        "suspend": false,
        "market": "",
        "strikeTimestamp": 1624896000,
        "expirationCycle": 1,
        "optionStandardType": 1,
        "optionSettlementMode": 2,
       }
      }
     }
    ],
    "strikeTimestamp": 1624896000
   }
  ]
 }
}
```









`GetOptionChain(req);`

- **Description**

  Query the option chain from an underlying stock. This interface only
  returns the static information of the option chain. If you need to
  obtain dynamic information such as quotation or trading, please use
  the security code returned by this interface to
  [subscribe](/moomoo-api-doc/en/quote/sub.html) the required security.

- **Parameters**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0;
    OptionCondType_WithIn = 1; //In-the-money
    OptionCondType_Outside = 2; //Out-of-the-money
}


//The following is the data field filtering, optional fields, leave it blank means no filtering
message DataFilter
{
    optional double impliedVolatilityMin = 1; //Min value of implied volatility range(0 decimal place accuracy, the excess part is discarded)
    optional double impliedVolatilityMax = 2; //Max value of implied volatility range(0 decimal place accuracy, the excess part is discarded)

    optional double deltaMin = 3; //Min value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)
    optional double deltaMax = 4; //Max value of Greek value Delta range(3 decimal place accuracy, the excess part is discarded)

    optional double gammaMin = 5; //Min value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)
    optional double gammaMax = 6; //Max value of Greek value Gamma range(3 decimal place accuracy, the excess part is discarded)

    optional double vegaMin = 7; //Min value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)
    optional double vegaMax = 8; //Max value of Greek value Vega range(3 decimal place accuracy, the excess part is discarded)

    optional double thetaMin = 9; //Min value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)
    optional double thetaMax = 10; //Max value of Greek value Theta range(3 decimal place accuracy, the excess part is discarded)

    optional double rhoMin = 11; //Min value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)
    optional double rhoMax = 12; //Max value of Greek value Rho range(3 decimal place accuracy, the excess part is discarded)

    optional double netOpenInterestMin = 13; //Min value of net open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double netOpenInterestMax = 14; //Max value of net open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double openInterestMin = 15; //Min value of open contract number range(0 decimal place accuracy, the excess part is discarded)
    optional double openInterestMax = 16; //Max value of open contract number range(0 decimal place accuracy, the excess part is discarded)

    optional double volMin = 17; //Min value of Volume range(0 decimal place accuracy, the excess part is discarded)
    optional double volMax = 18; //Max value of Volume range(0 decimal place accuracy, the excess part is discarded)
}

message C2S
{
    required Qot_Common.Security owner = 1; //The underlying stock of the option, currently only supports HK stocks, US stocks and index, HSI and HHI
    optional int32 indexOptionType = 6; //Qot_Common.IndexOptionType, the type of index option, only used for HSI and HHI
    optional int32 type = 2; //Qot_Common.OptionType, option type, optional field, if not specified, it means all return
    optional int32 condition = 3; //OptionCondType, in the price and out of the price, optional field, if not specified, it means all return
    required string beginTime = 4; //The start time of the option expiration date (Format: yyyy-MM-dd)
    required string endTime = 5; //The end time of the option expiration date, the time span is at most one month (Format: yyyy-MM-dd)
    optional DataFilter dataFilter = 7; //Data field filtering
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumeration of option types, refer to
>   [OptionType](/moomoo-api-doc/en/quote/quote.html#9598)
> - For the enumeration of index option types, refer to
>   [IndexOptionType](/moomoo-api-doc/en/quote/quote.html#2866)

- **Return**



``` protobuf

message OptionItem
{
    optional Qot_Common.SecurityStaticInfo call = 1; //Call option, this field is not necessarily present, it is determined by the request conditions
    optional Qot_Common.SecurityStaticInfo put = 2; //Put option, this field is not necessarily present, it is determined by the request conditions
}

message OptionChain
{
    required string strikeTime = 1; //Exercise date (Format: yyyy-MM-dd)
    repeated OptionItem option = 2; //Option information
    optional double strikeTimestamp = 3; //Exercise date timestamp
}

message S2C
{
    repeated OptionChain optionChain = 1; //Option chain
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetOptionChain(){
    const { RetType } = Common
    const {  QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    owner:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    beginTime: "2021-09-01",
                    endTime: "2021-09-30",
                },
            };

            websocket.GetOptionChain(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("OptionChain: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
OptionChain: errCode 0, retMsg , retType 0
{
  "optionChain": [{
    "strikeTime": "2021-09-29",
    "option": [{
      "call": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929C300000"
          },
          "id": "80287116",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 300.00 C",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 1,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 300,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      },
      "put": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929P300000"
          },
          "id": "80287124",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 300.00 P",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 2,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 300,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      }
    }, {
      "call": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929C310000"
          },
          "id": "80277871",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 310.00 C",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 1,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 310,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      },
      "put": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929P310000"
          },
          "id": "80277826",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 310.00 P",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 2,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 310,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      }
    }, ..., {
      "call": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929C950000"
          },
          "id": "80215136",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 950.00 C",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 1,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 950,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      },
      "put": {
        "basic": {
          "security": {
            "market": 1,
            "code": "TCH210929P950000"
          },
          "id": "80215157",
          "lotSize": 100,
          "secType": 8,
          "name": "TCH 210929 950.00 P",
          "listTime": "",
          "delisting": false
        },
        "optionExData": {
          "type": 2,
          "owner": {
            "market": 1,
            "code": "00700"
          },
          "strikeTime": "2021-09-29",
          "strikePrice": 950,
          "suspend": false,
          "market": "",
          "strikeTimestamp": 1632844800,
          "expirationCycle": 1,
          "optionStandardType": 1,
          "optionSettlementMode": 2,
        }
      }
    }],
    "strikeTimestamp": 1632844800
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- The upper limit of the incoming time span is 30 days





Tips

- This interface does not support the query of expired option chains,
  please enter today or future date to the **End date** parameter.
- Open interest (OI) is updated daily and the specific timing depends on
  the exchange.
  - For U.S. stock options, the data is updated during the PRE_MARKET
    session.
  - For Hong Kong stock options, the data is updated after the Regular
    Trading Hours.













