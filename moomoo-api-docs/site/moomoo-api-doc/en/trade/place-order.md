



# <a href="#3634" class="header-anchor">#</a> Place Orders









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`place_order(price, qty, code, trd_side, order_type=OrderType.NORMAL, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, remark=None, time_in_force=TimeInForce.DAY, fill_outside_rth=False, aux_price=None, trail_type=None, trail_value=None, trail_spread=None, session=Session.NONE)`

- **Description**

  Place order

  

  Tips

  The Python API is synchronous, but the network transport is
  asynchronous. When the receiving time interval is very short between
  the response packet of place_order and [Order Fill Push
  Callback](/moomoo-api-doc/en/trade/update-order-fill.html) or [Order
  Push Callback](/moomoo-api-doc/en/trade/update-order.html), it may
  happen that the response packet of place_order returns first, but the
  callback function is called first. For example: [Order Push
  Callback](/moomoo-api-doc/en/trade/update-order.html) may be called
  first, and then the place_order interface returns.

  

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
  <td style="text-align: left;">price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Order price.
  
    
  
  
   
  
  <ul>
  <li>When the order is a market order or auction order type, you still
  need to pass parameters, and price can be passed any value.</li>
  <li>Precision:
  <ul>
  <li>Futures: 8 integer digits, 9 decimal places, supporting negative
  prices.</li>
  <li>US stock options: 2 decimal places.</li>
  <li>US stocks: up to $1, allowing 4 decimal places.</li>
  <li>Others: 3 decimal places, round off excess digits.</li>
  </ul></li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">qty</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Order quantity.
  
    
  
  
   
  
  The unit of options and futures is "contract".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Code.
  
    
  
  
   
  
  If it is the future main code, it will be automatically converted to the
  actual corresponding contract code.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trd_side</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#832">TrdSide</a></td>
  <td style="text-align: left;">Transaction direction.</td>
  </tr>
  <tr>
  <td style="text-align: left;">order_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#245">OrderType</a></td>
  <td style="text-align: left;">Order type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">adjust_limit</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Price adjustment range.
  
    
  
  
   
  
  OpenD will automatically adjust the incoming price to the legal price.
  <ul>
  <li>Positive numbers represent upward adjustments, and negative numbers
  represent downward adjustments.</li>
  <li>For example: 0.015 means upward adjustment and the amplitude does
  not exceed 1.5%; -0.01 means downward adjustment and the amplitude does
  not exceed 1%. The default 0 means no adjustment.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trd_env</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
  <td style="text-align: left;">Trading environment.</td>
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
  <td style="text-align: left;">remark</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Remark.
  
    
  
  
   
  
  The maximum length after converting to utf8 is 64 bytes.<br />
  This remark field will be attached to the order to facilitate you to
  identify the order.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">time_in_force</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#7678">TimeInForce</a></td>
  <td style="text-align: left;">Valid period.
  
    
  
  
   
  
  Market orders of HK market, A-share market or global futures, only
  support <em>Day</em>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">fill_outside_rth</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether allow to execute the order during
  pre-market or after-hours market trades.
  
    
  
  
   
  
  For HK pre-opening market and US pre/post-market. And market orders are
  only supported in regular trading hours.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">aux_price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Trigger price.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Stop</strong>, <strong>Stop Limit</strong>,
  <strong>Market if Touched</strong>, or <strong>Limit if
  Touched</strong>, aux_price must be set.</li>
  <li>Same as price, round off excess digits.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trail_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#12">TrailType</a></td>
  <td style="text-align: left;">Trailing type.
  
    
  
  
   
  
  If order type is <strong>Trailing Stop</strong>, or <strong>Trailing
  Stop Limit</strong>, trail_type must be set.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trail_value</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Trailing amount/ratio.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Trailing Stop</strong>, or <strong>Trailing
  Stop Limit</strong>, trail_value must be set.</li>
  <li>If the trail type is PERCENTAGE, this field is in percentage form,
  so 20 is equivalent to 20%.</li>
  <li>If the trail type is PRICE, same as price for integer places. For US
  stock options is fixed to 2 decimal places, while for US stocks it is 4;
  for others, same as price. Round off excess digits.</li>
  <li>If the trail type is PERCENTAGE, this value will be rounded to 2
  decimals. The integer places are same as price.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trail_spread</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Specify spread.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Trailing Stop Limit</strong>, trail_spread
  must be set.</li>
  <li>The price will be rounded to 3 decimals for securities account, and
  9 decimals for futures account.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">session</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
  <td style="text-align: left;">US stocks Trading Session
  
    
  
  
   
  
  Applied to US stocks, <strong>RTH</strong>, <strong>ETH</strong>,
  <strong>OVERNIGHT</strong>, <strong>ALL</strong> can
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  be allowed.

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
  <td>If ret == RET_OK, order list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Order list format as follows:
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
    <td style="text-align: left;">trd_side</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#832">TrdSide</a></td>
    <td style="text-align: left;">Trading direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#245">OrderType</a></td>
    <td style="text-align: left;">Order type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#8074">OrderStatus</a></td>
    <td style="text-align: left;">Order status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Order ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Order quantity.
    
      
    
    
     
    
    Option futures unit is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Order price.
    
      
    
    
     
    
    3 decimal place accuracy, excess part will be rounded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">create_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Create time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">updated_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last update time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.<br />
    The unit of option futures is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Deal quantity
    
      
    
    
     
    
    Option futures unit is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average deal price.
    
      
    
    
     
    
    No precision limit.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_err_msg</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The last error description.
    
      
    
    
     
    
    If there is an error, the cause of the last error will be
    returned.<br />
    If there is no error, an empty string will be returned.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">remark</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Identification of remarks when placing an
    order.
    
      
    
    
     
    
    Refer to remark in the <a
    href="/moomoo-api-doc/en/trade/place-order.html"
    class="router-link-exact-active router-link-active"
    aria-current="page">place_order</a> interface parameters for details.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">time_in_force</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7678">TimeInForce</a></td>
    <td style="text-align: left;">Valid period.</td>
    </tr>
    <tr>
    <td style="text-align: left;">fill_outside_rth</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether pre-market and after-hours are
    needed.
    
      
    
    
     
    
    For HK pre-opening market and US pre/post-market.<br />
    True: need.<br />
    False: not need.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">session</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
    <td style="text-align: left;">Order session (Only applied to US
    stocks)</td>
    </tr>
    <tr>
    <td style="text-align: left;">aux_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Traget price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trail_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#12">TrailType</a></td>
    <td style="text-align: left;">Trailing type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trail_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Trailing amount/ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trail_spread</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Specify spread.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.unlock_trade(pwd_unlock)  # If you use a live trading account to place an order, you need to unlock the account first. The example here is to place an order on a paper trading account, and unlocking is not necessary.
if ret == RET_OK:
    ret, data = trd_ctx.place_order(price=510.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE, session=Session.NONE)
    if ret == RET_OK:
        print(data)
        print(data['order_id'][0])  # Get the order ID of the placed order
        print(data['order_id'].values.tolist())  # Convert to list
    else:
        print('place_order error: ', data)
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python

       code stock_name trd_side order_type order_status           order_id    qty  price          create_time         updated_time  dealt_qty  dealt_avg_price last_err_msg remark time_in_force fill_outside_rth session aux_price trail_type trail_value trail_spread currency
0  HK.00700       Tencent      BUY     NORMAL   SUBMITTING  38196006548709500  100.0  420.0  2021-11-04 11:38:19  2021-11-04 11:38:19        0.0              0.0                               DAY              N/A       N/A     N/A     N/A         N/A          N/A      HKD
38196006548709500
['38196006548709500']
```









## <a href="#8194" class="header-anchor">#</a> Trd_PlaceOrder.proto

- **Description**

  Place an order

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition(Market orders of HK market, A-share market or global futures, only support Day).
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade (Only for US stocks. And market orders are only supported in regular trading hours). Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2202





`uint PlaceOrder(TrdPlaceOrder.Request req);`  
`virtual void OnReply_PlaceOrder(FTAPI_Conn client, uint nSerialNo, TrdPlaceOrder.Response rsp);`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
                .SetAccID(281756457888247915L)
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Simulate)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdPlaceOrder.C2S c2s = TrdPlaceOrder.C2S.CreateBuilder()
                .SetPacketID(trd.NextPacketID())
                .SetHeader(header)
                .SetTrdSide((int)TrdCommon.TrdSide.TrdSide_Buy)
                .SetOrderType((int)TrdCommon.OrderType.OrderType_Normal)
                .SetCode("00700")
                .SetQty(100)
                .SetPrice(520)
                .SetSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK)
            .Build();
        TrdPlaceOrder.Request req = TrdPlaceOrder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.PlaceOrder(req);
        Console.Write("Send TrdPlaceOrder: {0}\n", seqNo);
    }

    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_PlaceOrder(FTAPI_Conn client, uint nSerialNo, TrdPlaceOrder.Response rsp)
    {
        Console.Write("Reply: TrdPlaceOrder: {0}\n", nSerialNo);
        Console.Write("accID: {0}\n", rsp.S2C.Header.AccID);
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
Trd onInitConnect: ret=0 desc= connID=6827788355222092042
Send TrdPlaceOrder: 3
Reply: TrdPlaceOrder: 3
accID: 281756457888247915
```









`int placeOrder(TrdPlaceOrder.Request req);`  
`void onReply_PlaceOrder(FTAPI_Conn client, int nSerialNo, TrdPlaceOrder.Response rsp);`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
                .setAccID(281756457888247915L)
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Simulate_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        TrdPlaceOrder.C2S c2s = TrdPlaceOrder.C2S.newBuilder()
                .setPacketID(trd.nextPacketID())
                .setHeader(header)
                .setTrdSide(TrdCommon.TrdSide.TrdSide_Buy_VALUE)
                .setOrderType(TrdCommon.OrderType.OrderType_Normal_VALUE)
                .setSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK_VALUE)
                .setCode("00700")
                .setQty(100)
                .setPrice(580)
            .build();
        TrdPlaceOrder.Request req = TrdPlaceOrder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.placeOrder(req);
        System.out.printf("Send TrdPlaceOrder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_PlaceOrder(FTAPI_Conn client, int nSerialNo, TrdPlaceOrder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdPlaceOrder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdPlaceOrder: %s\n", json);
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
Send TrdPlaceOrder: 2
Receive TrdPlaceOrder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "orderID": "5185481028427965890"
  }
}
```









`Futu::u32_t PlaceOrder(const Trd_PlaceOrder::Request &stReq);`  
`virtual void OnReply_PlaceOrder(Futu::u32_t nSerialNo, const Trd_PlaceOrder::Response &stRsp) = 0;`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
        Trd_PlaceOrder::Request req;
        Trd_PlaceOrder::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        c2s->set_trdside(1);
        c2s->set_ordertype(1);
        c2s->set_code("00700");
        c2s->set_qty(100);
        c2s->set_price(1);
        c2s->set_secmarket(Trd_Common::TrdMarket::TrdMarket_HK);

        m_PlaceOrderSerialNo = m_pTrdApi->PlaceOrder(req);
        cout << "Request PlaceOrder SerialNo: " << m_PlaceOrderSerialNo << endl;
    }

    virtual void OnReply_PlaceOrder(Futu::u32_t nSerialNo, const Trd_PlaceOrder::Response &stRsp){
        if(nSerialNo == m_PlaceOrderSerialNo)
        {
            cout << "OnReply_PlaceOrder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_PlaceOrderSerialNo;
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
Request PlaceOrder SerialNo: 4
OnReply_PlaceOrder SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "orderID": "3954832860392428914"
 }
}
```









`PlaceOrder(req);`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdPlaceOrder(){
    const { RetType, PacketID } = Common
    const { TrdEnv, TrdSide, OrderType, SecurityFirm, TrdMarket, TrdSecMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    let tradeSerialNo = 0;
    websocket.onlogin = async ()=>{
        try{
            let { errCode, retMsg, retType } = await websocket.UnlockTrade({
                c2s: {
                    unlock: true,
                    securityFirm: SecurityFirm.SecurityFirm_FutuSecurities,
                    pwdMD5: "d0970714757783e6cf17b26fb8e2298f", // Set as the transaction password MD5 of your account
                },
            });
            if(retType == RetType.RetType_Succeed && errCode == 0) { // Successful unlock transaction
                let { errCode, retMsg, retType, s2c: { accList } } = await websocket.GetAccList({
                    c2s: {
                        userID: 0,
                    },
                });
                if(retType == RetType.RetType_Succeed && errCode == 0) { // Successfully obtained account
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK paper trading environment account
                    
                    const req = {
                        c2s: {
                            packetID:{
                                connID: websocket.getConnID(),
                                serialNo: tradeSerialNo++,
                            },
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            trdSide: TrdSide.TrdSide_Buy,
                            orderType: OrderType.OrderType_Normal,
                            code: "00700",
                            qty: 100,
                            price: 150,
                            secMarket: TrdSecMarket.TrdSecMarket_HK,
                        },
                    };
                    let { errCode, retMsg, retType, s2c } = await websocket.PlaceOrder(req);
                    console.log("PlaceOrder: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                    if(retType == RetType.RetType_Succeed){
                        let data = beautify(JSON.stringify(s2c), {
                            indent_size: 2,
                            space_in_empty_paren: true,
                        });
                        console.log(data);
                    }
                }
            }
        }
        catch(err){
            console.log(err)
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
PlaceOrder: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "orderID": "5870498377428972628"
}
stop
```











Interface Limitations

- A maximum of 15 requests per 30 seconds under a single account ID
  (acc_id), and the interval between two consecutive requests cannot be
  less than 0.02 seconds.
- When using live trading accounts, you need to [unlock
  trade](/moomoo-api-doc/en/trade/unlock.html) **before** calling *Place
  Order* interface, but when using paper trading accounts, you do not
  need to [unlock trade](/moomoo-api-doc/en/trade/unlock.html).





Tips

- Required parameters for each order type: [Click
  here](/moomoo-api-doc/en/qa/trade.html#8229) to learn more.
- Each broker sets limits on shares or amounts for single orders of
  various trading products. Exceeding these limits may result in order
  failures: [Click here](/moomoo-api-doc/en/qa/trade.html#8229) to learn
  more.
- Locking position is not supported for **shortable securities**, that
  means you can not hold a long position and a short position at the
  same time.
- If you want to **close out position** of a **shortable securities**,
  you need to get the direction of the position and send an opposite
  order with the same quantity.
- If you want to **reversing trade** of a **shortable securities**,
  there are 2 steps: 1. you need to get the direction of the position
  and send an opposite order with the same quantity. 2. Send an opposite
  order again to open the reverse trade. For example: If you want to
  reverse trade of 1 long position of HK.HSI2012, you need to close the
  long position first and then sell short the contract.
- Only limit orders can be allowed during US stocks 24 Hour Trading
  Hour. You can choose Day, Good-Till-Cancelled (GTC) as the
  time-in-force. 24-hour order runs from Sunday 8:00 PM to Friday 8:00
  PM ET, covering regular trading hours plus pre-market, post-market,
  and overnight trading sessions. You can place orders anytime during
  this period.
- Paper trading of US stocks does not support irregular trading hours
  (including pre/post-market and overnight).











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`place_order(price, qty, code, trd_side, order_type=OrderType.NORMAL, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, remark=None, time_in_force=TimeInForce.DAY, fill_outside_rth=False, aux_price=None, trail_type=None, trail_value=None, trail_spread=None, session=Session.NONE)`

- **Description**

  Place order

  

  Tips

  The Python API is synchronous, but the network transport is
  asynchronous. When the receiving time interval is very short between
  the response packet of place_order and [Order Fill Push
  Callback](/moomoo-api-doc/en/trade/update-order-fill.html) or [Order
  Push Callback](/moomoo-api-doc/en/trade/update-order.html), it may
  happen that the response packet of place_order returns first, but the
  callback function is called first. For example: [Order Push
  Callback](/moomoo-api-doc/en/trade/update-order.html) may be called
  first, and then the place_order interface returns.

  

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
  <td style="text-align: left;">price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Order price.
  
    
  
  
   
  
  <ul>
  <li>When the order is a market order or auction order type, you still
  need to pass parameters, and price can be passed any value.</li>
  <li>Precision:
  <ul>
  <li>Futures: 8 integer digits, 9 decimal places, supporting negative
  prices.</li>
  <li>US stock options: 2 decimal places.</li>
  <li>US stocks: up to $1, allowing 4 decimal places.</li>
  <li>Others: 3 decimal places, round off excess digits.</li>
  </ul></li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">qty</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Order quantity.
  
    
  
  
   
  
  The unit of options and futures is "contract".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Code.
  
    
  
  
   
  
  If it is the future main code, it will be automatically converted to the
  actual corresponding contract code.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trd_side</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#832">TrdSide</a></td>
  <td style="text-align: left;">Transaction direction.</td>
  </tr>
  <tr>
  <td style="text-align: left;">order_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#245">OrderType</a></td>
  <td style="text-align: left;">Order type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">adjust_limit</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Price adjustment range.
  
    
  
  
   
  
  OpenD will automatically adjust the incoming price to the legal price.
  <ul>
  <li>Positive numbers represent upward adjustments, and negative numbers
  represent downward adjustments.</li>
  <li>For example: 0.015 means upward adjustment and the amplitude does
  not exceed 1.5%; -0.01 means downward adjustment and the amplitude does
  not exceed 1%. The default 0 means no adjustment.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trd_env</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
  <td style="text-align: left;">Trading environment.</td>
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
  <td style="text-align: left;">remark</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Remark.
  
    
  
  
   
  
  The maximum length after converting to utf8 is 64 bytes.<br />
  This remark field will be attached to the order to facilitate you to
  identify the order.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">time_in_force</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#7678">TimeInForce</a></td>
  <td style="text-align: left;">Valid period.
  
    
  
  
   
  
  Market orders of HK market, A-share market or global futures, only
  support <em>Day</em>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">fill_outside_rth</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether allow to execute the order during
  pre-market or after-hours market trades.
  
    
  
  
   
  
  For HK pre-opening market and US pre/post-market. And market orders are
  only supported in regular trading hours.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">aux_price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Trigger price.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Stop</strong>, <strong>Stop Limit</strong>,
  <strong>Market if Touched</strong>, or <strong>Limit if
  Touched</strong>, aux_price must be set.</li>
  <li>Same as price. Round off excess digits.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trail_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#12">TrailType</a></td>
  <td style="text-align: left;">Trailing type.
  
    
  
  
   
  
  If order type is <strong>Trailing Stop</strong>, or <strong>Trailing
  Stop Limit</strong>, trail_type must be set.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trail_value</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Trailing amount/ratio.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Trailing Stop</strong>, or <strong>Trailing
  Stop Limit</strong>, trail_value must be set.</li>
  <li>If the trail type is PERCENTAGE, this field is in percentage form,
  so 20 is equivalent to 20%.</li>
  <li>If the trail type is PRICE, same as price for integer places. For US
  stock options is fixed to 2 decimal places, while for US stocks it is 4;
  for others, same as price. Round off excess digits.</li>
  <li>If the trail type is PERCENTAGE, this value will be rounded to 2
  decimals. The integer places are same as price.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trail_spread</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Specify spread.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Trailing Stop Limit</strong>, trail_spread
  must be set.</li>
  <li>The price will be rounded to 3 decimals for securities account, and
  9 decimals for futures account.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">session</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
  <td style="text-align: left;">US stocks Trading Session
  
    
  
  
   
  
  Applied to US stocks, <strong>RTH</strong>, <strong>ETH</strong>,
  <strong>OVERNIGHT</strong>, <strong>ALL</strong> can be allowed.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

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
  <td>If ret == RET_OK, order list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Order list format as follows:
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
    <td style="text-align: left;">trd_side</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#832">TrdSide</a></td>
    <td style="text-align: left;">Trading direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#245">OrderType</a></td>
    <td style="text-align: left;">Order type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#8074">OrderStatus</a></td>
    <td style="text-align: left;">Order status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Order ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Order quantity.
    
      
    
    
     
    
    Option futures unit is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Order price.
    
      
    
    
     
    
    3 decimal place accuracy, excess part will be rounded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">create_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Create time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">updated_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last update time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.<br />
    The unit of option futures is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Deal quantity
    
      
    
    
     
    
    Option futures unit is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average deal price.
    
      
    
    
     
    
    No precision limit.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_err_msg</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The last error description.
    
      
    
    
     
    
    If there is an error, the cause of the last error will be
    returned.<br />
    If there is no error, an empty string will be returned.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">remark</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Identification of remarks when placing an
    order.
    
      
    
    
     
    
    Refer to remark in the <a
    href="/moomoo-api-doc/en/trade/place-order.html"
    class="router-link-exact-active router-link-active"
    aria-current="page">place_order</a> interface parameters for details.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">time_in_force</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7678">TimeInForce</a></td>
    <td style="text-align: left;">Valid period.</td>
    </tr>
    <tr>
    <td style="text-align: left;">fill_outside_rth</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether pre-market and after-hours are
    needed.
    
      
    
    
     
    
    For HK pre-opening market and US pre/post-market.<br />
    True: need.<br />
    False: not need.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">session</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
    <td style="text-align: left;">Order session (Only applied to US
    stocks)</td>
    </tr>
    <tr>
    <td style="text-align: left;">aux_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Traget price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trail_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#12">TrailType</a></td>
    <td style="text-align: left;">Trailing type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trail_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Trailing amount/ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trail_spread</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Specify spread.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.unlock_trade(pwd_unlock)  # If you use a live trading account to place an order, you need to unlock the account first. The example here is to place an order on a paper trading account, and unlocking is not necessary.
if ret == RET_OK:
    ret, data = trd_ctx.place_order(price=510.0, qty=100, code="US.AAPL", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE, session=Session.NONE)
    if ret == RET_OK:
        print(data)
        print(data['order_id'][0])  # Get the order ID of the placed order
        print(data['order_id'].values.tolist())  # Convert to list
    else:
        print('place_order error: ', data)
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python

       code stock_name trd_side order_type order_status           order_id    qty  price          create_time         updated_time  dealt_qty  dealt_avg_price last_err_msg remark time_in_force fill_outside_rth session aux_price trail_type trail_value trail_spread currency
0  US.AAPL       Apple Inc.      BUY     NORMAL   SUBMITTING  38196006548709500  100.0  420.0  2021-11-04 11:38:19  2021-11-04 11:38:19        0.0              0.0                               DAY              N/A       N/A    N/A      N/A         N/A          N/A      USD
38196006548709500
['38196006548709500']
```









## <a href="#8194-2" class="header-anchor">#</a> Trd_PlaceOrder.proto

- **Description**

  Place an order

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition(Market orders of HK market, A-share market or global futures, only support Day).
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade (Only for US stocks. And market orders are only supported in regular trading hours). Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2202





`uint PlaceOrder(TrdPlaceOrder.Request req);`  
`virtual void OnReply_PlaceOrder(MMAPI_Conn client, uint nSerialNo, TrdPlaceOrder.Response rsp);`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
                .SetAccID(281756457888247915L)
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Simulate)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdPlaceOrder.C2S c2s = TrdPlaceOrder.C2S.CreateBuilder()
                .SetPacketID(trd.NextPacketID())
                .SetHeader(header)
                .SetTrdSide((int)TrdCommon.TrdSide.TrdSide_Buy)
                .SetOrderType((int)TrdCommon.OrderType.OrderType_Normal)
                .SetCode("00700")
                .SetQty(100)
                .SetPrice(520)
                .SetSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK)
            .Build();
        TrdPlaceOrder.Request req = TrdPlaceOrder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.PlaceOrder(req);
        Console.Write("Send TrdPlaceOrder: {0}\n", seqNo);
    }

    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_PlaceOrder(MMAPI_Conn client, uint nSerialNo, TrdPlaceOrder.Response rsp)
    {
        Console.Write("Reply: TrdPlaceOrder: {0}\n", nSerialNo);
        Console.Write("accID: {0}\n", rsp.S2C.Header.AccID);
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
Trd onInitConnect: ret=0 desc= connID=6827788355222092042
Send TrdPlaceOrder: 3
Reply: TrdPlaceOrder: 3
accID: 281756457888247915
```









`int placeOrder(TrdPlaceOrder.Request req);`  
`void onReply_PlaceOrder(MMAPI_Conn client, int nSerialNo, TrdPlaceOrder.Response rsp);`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
                .setAccID(281756457888247915L)
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Simulate_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        TrdPlaceOrder.C2S c2s = TrdPlaceOrder.C2S.newBuilder()
                .setPacketID(trd.nextPacketID())
                .setHeader(header)
                .setTrdSide(TrdCommon.TrdSide.TrdSide_Buy_VALUE)
                .setOrderType(TrdCommon.OrderType.OrderType_Normal_VALUE)
                .setSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK_VALUE)
                .setCode("00700")
                .setQty(100)
                .setPrice(580)
            .build();
        TrdPlaceOrder.Request req = TrdPlaceOrder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.placeOrder(req);
        System.out.printf("Send TrdPlaceOrder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_PlaceOrder(MMAPI_Conn client, int nSerialNo, TrdPlaceOrder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdPlaceOrder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdPlaceOrder: %s\n", json);
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
Send TrdPlaceOrder: 2
Receive TrdPlaceOrder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "orderID": "5185481028427965890"
  }
}
```









`moomoo::u32_t PlaceOrder(const Trd_PlaceOrder::Request &stReq);`  
`virtual void OnReply_PlaceOrder(moomoo::u32_t nSerialNo, const Trd_PlaceOrder::Response &stRsp) = 0;`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
        Trd_PlaceOrder::Request req;
        Trd_PlaceOrder::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        c2s->set_trdside(1);
        c2s->set_ordertype(1);
        c2s->set_code("00700");
        c2s->set_qty(100);
        c2s->set_price(1);
        c2s->set_secmarket(Trd_Common::TrdMarket::TrdMarket_HK);

        m_PlaceOrderSerialNo = m_pTrdApi->PlaceOrder(req);
        cout << "Request PlaceOrder SerialNo: " << m_PlaceOrderSerialNo << endl;
    }

    virtual void OnReply_PlaceOrder(moomoo::u32_t nSerialNo, const Trd_PlaceOrder::Response &stRsp){
        if(nSerialNo == m_PlaceOrderSerialNo)
        {
            cout << "OnReply_PlaceOrder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_PlaceOrderSerialNo;
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
Request PlaceOrder SerialNo: 4
OnReply_PlaceOrder SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "orderID": "3954832860392428914"
 }
}
```









`PlaceOrder(req);`

- **Description**

  Place an order

- **Parameters**



``` protobuf

message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required int32 trdSide = 3; //Trading direction, see the enumeration definition of Trd_Common.TrdSide
    required int32 orderType = 4; //Order type, see Trd_Common.OrderType enumeration definition
    required string code = 5; //Code, 5 decimal places for HK stocks, 6 decimal places for A-shares, and no restrictions for US stocks
    required double qty = 6; //Quantity, option unit is "contract" (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    optional double price = 7; //Price, (0 decimal place accuracy, the excess part is discarded. The unit of options and futures is "contract")
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment.. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 10; //Market to whitch securities belong, see the enumeration definition of TrdSecMarket
    optional string remark = 11; //User remark string, up to 64 bytes can be transferred. It can be used to identify the unique information of the order, etc., fill in the order, and the order structure will be brought.
    optional int32 timeInForce = 12; //How long the order remains in effect, see TrdCommon.TimeInForce enumeration definition
    optional bool fillOutsideRTH = 13; //Whether to allow pre-market and after-hours market trade. Only applicable to US stock limit orders. Default false
    optional double auxPrice = 14; //Trigger price
    optional int32 trailType = 15; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 16; //Trailing amount / ratio
    optional double trailSpread = 17; //Specify spread
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet ID, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For transaction direction, refer to
>   [TrdSide](/moomoo-api-doc/en/trade/trade.html#832)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)
> - For how long the order remains in effect, refer to
>   [TimeInForce](/moomoo-api-doc/en/trade/trade.html#7678)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional uint64 orderID = 2; //Order number
    optional string orderIDEx = 3; //The server order id, which can be used instead of orderID, or choose one from orderID   
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdPlaceOrder(){
    const { RetType, PacketID } = Common
    const { TrdEnv, TrdSide, OrderType, SecurityFirm, TrdMarket, TrdSecMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    let tradeSerialNo = 0;
    websocket.onlogin = async ()=>{
        try{
            let { errCode, retMsg, retType } = await websocket.UnlockTrade({
                c2s: {
                    unlock: true,
                    securityFirm: SecurityFirm.SecurityFirm_FutuSecurities,
                    pwdMD5: "d0970714757783e6cf17b26fb8e2298f", // Set as the transaction password MD5 of your account
                },
            });
            if(retType == RetType.RetType_Succeed && errCode == 0) { // Successful unlock transaction
                let { errCode, retMsg, retType, s2c: { accList } } = await websocket.GetAccList({
                    c2s: {
                        userID: 0,
                    },
                });
                if(retType == RetType.RetType_Succeed && errCode == 0) { // Successfully obtained account
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK paper trading environment account
                    
                    const req = {
                        c2s: {
                            packetID:{
                                connID: websocket.getConnID(),
                                serialNo: tradeSerialNo++,
                            },
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            trdSide: TrdSide.TrdSide_Buy,
                            orderType: OrderType.OrderType_Normal,
                            code: "00700",
                            qty: 100,
                            price: 150,
                            secMarket: TrdSecMarket.TrdSecMarket_HK,
                        },
                    };
                    let { errCode, retMsg, retType, s2c } = await websocket.PlaceOrder(req);
                    console.log("PlaceOrder: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                    if(retType == RetType.RetType_Succeed){
                        let data = beautify(JSON.stringify(s2c), {
                            indent_size: 2,
                            space_in_empty_paren: true,
                        });
                        console.log(data);
                    }
                }
            }
        }
        catch(err){
            console.log(err)
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
PlaceOrder: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "orderID": "5870498377428972628"
}
stop
```











Interface Limitations

- A maximum of 15 requests per 30 seconds under a single account ID
  (acc_id), and the interval between two consecutive requests cannot be
  less than 0.02 seconds.
- When using live trading accounts, you need to [unlock
  trade](/moomoo-api-doc/en/trade/unlock.html) **before** calling *Place
  Order* interface, but when using paper trading accounts, you do not
  need to [unlock trade](/moomoo-api-doc/en/trade/unlock.html).





Tips

- Required parameters for each order type: [Click
  here](/moomoo-api-doc/en/qa/trade.html#8229) to learn more.
- Each broker sets limits on shares or amounts for single orders of
  various trading products. Exceeding these limits may result in order
  failures: [Click here](/moomoo-api-doc/en/qa/trade.html#8229) to learn
  more.
- Locking position is not supported for **shortable securities**, that
  means you can not hold a long position and a short position at the
  same time.
- If you want to **close out position** of a **shortable securities**,
  you need to get the direction of the position and send an opposite
  order with the same quantity.
- If you want to **reversing trade** of a **shortable securities**,
  there are 2 steps: 1. you need to get the direction of the position
  and send an opposite order with the same quantity. 2. Send an opposite
  order again to open the reverse trade. For example: If you want to
  reverse trade of 1 long position of HK.HSI2012, you need to close the
  long position first and then sell short the contract.
- Only limit orders can be allowed during US stocks 24 Hour Trading
  Hour. You can choose Day, Good-Till-Cancelled (GTC) as the
  time-in-force. 24-hour order runs from Sunday 8:00 PM to Friday 8:00
  PM ET, covering regular trading hours plus pre-market, post-market,
  and overnight trading sessions. You can place orders anytime during
  this period.
- Paper trading of US stocks does not support irregular trading hours
  (including pre/post-market and overnight).













