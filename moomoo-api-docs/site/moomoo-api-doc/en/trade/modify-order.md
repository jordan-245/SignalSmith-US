



# <a href="#8129" class="header-anchor">#</a> Modify or Cancel Orders









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`modify_order(modify_order_op, order_id, qty, price, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, aux_price=None, trail_type=None, trail_value=None, trail_spread=None)`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

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
  <td style="text-align: left;">modify_order_op</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#3811">ModifyOrderOp</a></td>
  <td style="text-align: left;">Modify order operation type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">order_id</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Order ID.</td>
  </tr>
  <tr>
  <td style="text-align: left;">qty</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The quantity after the order is changed.
  
    
  
  
   
  
  The unit of options and futures is "contract".<br />
  0 decimal place accuracy, the excess part is discarded.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The price after the order is changed.
  
    
  
  
   
  
  Accuracy to 3 decimal places for securities account, and the excess part
  will be discarded.<br />
  Accuracy to 9 decimal places for futures account, and the excess part
  will be discarded.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">adjust_limit</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Price adjustment range.
  
    
  
  
   
  
  OpenD will automatically adjust the incoming price to the legal
  price.(This parameter will be ignored by future contracts.)
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
  <td style="text-align: left;">aux_price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Trigger price.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Stop</strong>, <strong>Stop Limit</strong>,
  <strong>Market if Touched</strong>, or <strong>Limit if
  Touched</strong>, aux_price must be set.</li>
  <li>The price will be rounded to 3 decimals for securities account, and
  9 decimals for futures account.</li>
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
  <li>If the trail type is PRICE, this value will be rounded to 3 decimals
  for securities account, and 9 decimals for futures account.</li>
  <li>If the trail type is PRICE, this value will be rounded to 2
  decimals.</li>
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
  <td>If ret == RET_OK, modification information is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Modification information format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | trd_env | [TrdEnv](/moomoo-api-doc/en/trade/trade.html#48) | Trading environment. |
    | order_id | str | Order ID. |

- **Example**



``` python
from futu import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.unlock_trade(pwd_unlock)  # If you use a live trading account to modify or cancel an order, you need to unlock the account first. The example here is to cancel an order on a paper trading account, and unlocking is not necessary.
if ret == RET_OK:
    order_id = "8851102695472794941"
    ret, data = trd_ctx.modify_order(ModifyOrderOp.CANCEL, order_id, 0, 0)
    if ret == RET_OK:
        print(data)
        print(data['order_id'][0])  # Get the order ID of the modified order
        print(data['order_id'].values.tolist())  # Convert to list
    else:
        print('modify_order error: ', data)
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python
    trd_env             order_id
0    REAL      8851102695472794941
8851102695472794941
['8851102695472794941']
```





`cancel_all_order(trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, trdmarket=TrdMarket.NONE)`

- **Description**

  Cancel all orders. Paper trading and HKCC trading accounts do not
  support all cancellations.

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
  <td style="text-align: left;">Trading environment.</td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_id</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Trading account ID.
  
    
  
  
   
  
  When acc_id is 0, the account specified by acc_index is chosen.<br />
  When acc_id is set the ID number (not 0), the account specified by
  acc_id is chosen.
  
  
  
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
  <td style="text-align: left;">trdmarket</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Transaction market selection.
  
    
  
  
   
  
  Cancel orders in specified markets the given account.<br />
  In the default state, cancel orders in all markets for the given
  account.
  
  
  
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
  <td>int</td>
  <td>Returned value. On success, ret == RET_OK. On error, ret !=
  RET_OK.</td>
  </tr>
  <tr>
  <td rowspan="2">data</td>
  <td rowspan="2">str</td>
  <td>If ret == RET_OK, modification information is returned.</td>
  </tr>
  <tr>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Modification information format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | trd_env | [TrdEnv](/moomoo-api-doc/en/trade/trade.html#48) | Trading environment |
    | order_id | str | Order number |

- **Example**



``` python
from futu import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.unlock_trade(pwd_unlock)  # If you use a live trading account to modify or cancel an order, you need to unlock the account first. The example here is to cancel all orders on a paper trading account, and unlocking is not necessary.
if ret == RET_OK:
    ret, data = trd_ctx.cancel_all_order()
    if ret == RET_OK:
        print(data)
    else:
        print('cancel_all_order error: ', data)
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python
success
```









## <a href="#5781" class="header-anchor">#</a> Trd_ModifyOrder.proto

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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

  2205





`uint ModifyOrder(TrdModifyOrder.Request req);`  
`virtual void OnReply_ModifyOrder(FTAPI_Conn client, uint nSerialNo, TrdModifyOrder.Response rsp);`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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
public class Program : FTSPI_Trd, FTSPI_Conn {
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdModifyOrder.C2S c2s = TrdModifyOrder.C2S.CreateBuilder()
                .SetPacketID(trd.NextPacketID())
                .SetHeader(header)
                .SetOrderID(1167729267926401492L)
                .SetModifyOrderOp((int)TrdCommon.ModifyOrderOp.ModifyOrderOp_Normal)
                .SetPrice(100)
            .Build();
        TrdModifyOrder.Request req = TrdModifyOrder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.ModifyOrder(req);
        Console.Write("Send TrdModifyOrder: {0}\n", seqNo);
    }
    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_ModifyOrder(FTAPI_Conn client, uint nSerialNo, TrdModifyOrder.Response rsp)
    {
        Console.Write("Reply: TrdModifyOrder: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827792005034419980
Send TrdModifyOrder: 3
Reply: TrdModifyOrder: 3
accID: 281756457888247915
```









`int modifyOrder(TrdModifyOrder.Request req);`  
`void onReply_ModifyOrder(FTAPI_Conn client, int nSerialNo, TrdModifyOrder.Response rsp);`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        TrdModifyOrder.C2S c2s = TrdModifyOrder.C2S.newBuilder()
                .setPacketID(trd.nextPacketID())
                .setHeader(header)
                .setOrderID(1167729267926401492L)
                .setModifyOrderOp(TrdCommon.ModifyOrderOp.ModifyOrderOp_Normal_VALUE)
                .setPrice(100)
            .build();
        TrdModifyOrder.Request req = TrdModifyOrder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.modifyOrder(req);
        System.out.printf("Send TrdModifyOrder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_ModifyOrder(FTAPI_Conn client, int nSerialNo, TrdModifyOrder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdModifyOrder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdModifyOrder: %s\n", json);
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
Send TrdModifyOrder: 2
Receive TrdModifyOrder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "orderID": "5185260464676654543"
  }
}
```









`Futu::u32_t ModifyOrder(const Trd_ModifyOrder::Request &stReq);`  
`virtual void OnReply_ModifyOrder(Futu::u32_t nSerialNo, const Trd_ModifyOrder::Response &stRsp) = 0;`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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
        Trd_ModifyOrder::Request req;
        Trd_ModifyOrder::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        c2s->set_orderid(3964270595789502688L);
        c2s->set_modifyorderop(2);

        m_ModifyOrderSerialNo = m_pTrdApi->ModifyOrder(req);
        cout << "Request ModifyOrder SerialNo: " << m_ModifyOrderSerialNo << endl;
    }

    virtual void OnReply_ModifyOrder(Futu::u32_t nSerialNo, const Trd_ModifyOrder::Response &stRsp){
        if(nSerialNo == m_ModifyOrderSerialNo)
        {
            cout << "OnReply_ModifyOrder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_ModifyOrderSerialNo;
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
Request ModifyOrder SerialNo: 4
OnReply_ModifyOrder SerialNo: 4
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
  "orderID": "3964270595789502688"
 }
}
```









`ModifyOrder(req);`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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

function TrdModifyOrder(){
    const { RetType, PacketID } = Common
    const { TrdEnv, TrdSide, OrderType, SecurityFirm, TrdMarket, TrdSecMarket, ModifyOrderOp } = Trd_Common
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
                    
                    let { errCode, retMsg, retType, s2c : { orderID } } = await websocket.PlaceOrder({
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
                    }); 
                    if(retType == RetType.RetType_Succeed && errCode == 0){
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
                                orderID: orderID,
                                modifyOrderOp: ModifyOrderOp.ModifyOrderOp_Normal,
                                qty: 200,
                                price: 100,
                            },
                        };
                        let { errCode, retMsg, retType, s2c } = await websocket.ModifyOrder(req);
                        console.log("ModifyOrder: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
ModifyOrder: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "orderID": "5870570404030790740"
}
stop
```











Interface Limitations

- A maximum of 20 requests per 30 seconds under a single account ID
  (acc_id), and the time interval between two consecutive requests
  should not be less than 0.04 seconds.
- When using live trading accounts, you need to [unlock
  trade](/moomoo-api-doc/en/trade/unlock.html) **before** calling
  *Modify or Cancel Orders* interface, but when using paper trading
  accounts, you do not need to [unlock
  trade](/moomoo-api-doc/en/trade/unlock.html).





Tip

- For the execution of **modify the order**, to learn more about the
  required parameters for each order type, please [click
  here](/moomoo-api-doc/en/qa/trade.html#2440).
- If you want to **modify the quantity of the order**, the parameter
  **qty** should be equal to the total quantity of the expected
  filled.  
  For example:  
  The quantity of an order is *N* shares, with *n* shares filled. For
  the unfilled *(N-n)* shares, if you want to cancel *x* shares, the
  parameter **modify_order_op** should be *NORMAL*, **qty** should be
  *(N-x)*.
  ![order_quantity](/moomoo-api-doc/assets/img/order_quantity_en.f13725f3.png)
- If you want to cancel an order, the parameter **modify_order_op**
  should be *CANCEL*.  
  For example:  
  The quantity of an order is *N* shares, with *n* shares filled. If you
  want to cancel the unfilled *(N-n)* shares, **modify_order_op** should
  be *CANCEL*, and **qty** and **price** will be ignored.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`modify_order(modify_order_op, order_id, qty, price, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, aux_price=None, trail_type=None, trail_value=None, trail_spread=None)`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

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
  <td style="text-align: left;">modify_order_op</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#3811">ModifyOrderOp</a></td>
  <td style="text-align: left;">Modify order operation type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">order_id</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Order ID.</td>
  </tr>
  <tr>
  <td style="text-align: left;">qty</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The quantity after the order is changed.
  
    
  
  
   
  
  The unit of options and futures is "contract".<br />
  0 decimal place accuracy, the excess part is discarded.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The price after the order is changed.
  
    
  
  
   
  
  Accuracy to 3 decimal places for securities account, and the excess part
  will be discarded.<br />
  Accuracy to 9 decimal places for futures account, and the excess part
  will be discarded.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">adjust_limit</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Price adjustment range.
  
    
  
  
   
  
  OpenD will automatically adjust the incoming price to the legal
  price.(This parameter will be ignored by future contracts.)
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
  <td style="text-align: left;">aux_price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Trigger price.
  
    
  
  
   
  
  <ul>
  <li>If order type is <strong>Stop</strong>, <strong>Stop Limit</strong>,
  <strong>Market if Touched</strong>, or <strong>Limit if
  Touched</strong>, aux_price must be set.</li>
  <li>The price will be rounded to 3 decimals for securities account, and
  9 decimals for futures account.</li>
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
  <li>If the trail type is PRICE, this value will be rounded to 3 decimals
  for securities account, and 9 decimals for futures account.</li>
  <li>If the trail type is PRICE, this value will be rounded to 2
  decimals.</li>
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
  <td>If ret == RET_OK, modification information is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Modification information format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | trd_env | [TrdEnv](/moomoo-api-doc/en/trade/trade.html#48) | Trading environment. |
    | order_id | str | Order ID. |

- **Example**



``` python
from moomoo import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.unlock_trade(pwd_unlock)  # If you use a live trading account to modify or cancel an order, you need to unlock the account first. The example here is to cancel an order on a paper trading account, and unlocking is not necessary.
if ret == RET_OK:
    order_id = "8851102695472794941"
    ret, data = trd_ctx.modify_order(ModifyOrderOp.CANCEL, order_id, 0, 0)
    if ret == RET_OK:
        print(data)
        print(data['stock_name'][0])  # Get the order ID of the modified order
        print(data['stock_name'].values.tolist())  # Convert to list
    else:
        print('modify_order error: ', data)
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python
    trd_env             order_id
0    REAL      8851102695472794941
8851102695472794941
['8851102695472794941']
```





`cancel_all_order(trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, trdmarket=TrdMarket.NONE)`

- **Description**

  Cancel all orders. Paper trading and HKCC trading accounts do not
  support all cancellations.

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
  <td style="text-align: left;">Trading environment.</td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_id</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Trading account ID.
  
    
  
  
   
  
  When acc_id is 0, the account specified by acc_index is chosen.<br />
  When acc_id is set the ID number (not 0), the account specified by
  acc_id is chosen.
  
  
  
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
  <td style="text-align: left;">trdmarket</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Transaction market selection.
  
    
  
  
   
  
  Cancel orders in specified markets the given account.<br />
  In the default state, cancel orders in all markets for the given
  account.
  
  
  
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
  <td>int</td>
  <td>Returned value. On success, ret == RET_OK. On error, ret !=
  RET_OK.</td>
  </tr>
  <tr>
  <td rowspan="2">data</td>
  <td rowspan="2">str</td>
  <td>If ret == RET_OK, modification information is returned.</td>
  </tr>
  <tr>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Modification information format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | trd_env | [TrdEnv](/moomoo-api-doc/en/trade/trade.html#48) | Trading environment |
    | order_id | str | Order number |

- **Example**



``` python
from moomoo import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.unlock_trade(pwd_unlock)  # If you use a live trading account to modify or cancel an order, you need to unlock the account first. The example here is to cancel all orders on a paper trading account, and unlocking is not necessary.
if ret == RET_OK:
    ret, data = trd_ctx.cancel_all_order()
    if ret == RET_OK:
        print(data)
    else:
        print('cancel_all_order error: ', data)
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python
success
```









## <a href="#5781-2" class="header-anchor">#</a> Trd_ModifyOrder.proto

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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

  2205





`uint ModifyOrder(TrdModifyOrder.Request req);`  
`virtual void OnReply_ModifyOrder(MMAPI_Conn client, uint nSerialNo, TrdModifyOrder.Response rsp);`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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
public class Program : MMSPI_Trd, MMSPI_Conn {
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdModifyOrder.C2S c2s = TrdModifyOrder.C2S.CreateBuilder()
                .SetPacketID(trd.NextPacketID())
                .SetHeader(header)
                .SetOrderID(1167729267926401492L)
                .SetModifyOrderOp((int)TrdCommon.ModifyOrderOp.ModifyOrderOp_Normal)
                .SetPrice(100)
            .Build();
        TrdModifyOrder.Request req = TrdModifyOrder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.ModifyOrder(req);
        Console.Write("Send TrdModifyOrder: {0}\n", seqNo);
    }
    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_ModifyOrder(MMAPI_Conn client, uint nSerialNo, TrdModifyOrder.Response rsp)
    {
        Console.Write("Reply: TrdModifyOrder: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827792005034419980
Send TrdModifyOrder: 3
Reply: TrdModifyOrder: 3
accID: 281756457888247915
```









`int modifyOrder(TrdModifyOrder.Request req);`  
`void onReply_ModifyOrder(MMAPI_Conn client, int nSerialNo, TrdModifyOrder.Response rsp);`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        TrdModifyOrder.C2S c2s = TrdModifyOrder.C2S.newBuilder()
                .setPacketID(trd.nextPacketID())
                .setHeader(header)
                .setOrderID(1167729267926401492L)
                .setModifyOrderOp(TrdCommon.ModifyOrderOp.ModifyOrderOp_Normal_VALUE)
                .setPrice(100)
            .build();
        TrdModifyOrder.Request req = TrdModifyOrder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.modifyOrder(req);
        System.out.printf("Send TrdModifyOrder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_ModifyOrder(MMAPI_Conn client, int nSerialNo, TrdModifyOrder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdModifyOrder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdModifyOrder: %s\n", json);
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
Send TrdModifyOrder: 2
Receive TrdModifyOrder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "orderID": "5185260464676654543"
  }
}
```









`moomoo::u32_t ModifyOrder(const Trd_ModifyOrder::Request &stReq);`  
`virtual void OnReply_ModifyOrder(moomoo::u32_t nSerialNo, const Trd_ModifyOrder::Response &stRsp) = 0;`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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
        Trd_ModifyOrder::Request req;
        Trd_ModifyOrder::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        c2s->set_orderid(3964270595789502688L);
        c2s->set_modifyorderop(2);

        m_ModifyOrderSerialNo = m_pTrdApi->ModifyOrder(req);
        cout << "Request ModifyOrder SerialNo: " << m_ModifyOrderSerialNo << endl;
    }

    virtual void OnReply_ModifyOrder(moomoo::u32_t nSerialNo, const Trd_ModifyOrder::Response &stRsp){
        if(nSerialNo == m_ModifyOrderSerialNo)
        {
            cout << "OnReply_ModifyOrder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_ModifyOrderSerialNo;
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
Request ModifyOrder SerialNo: 4
OnReply_ModifyOrder SerialNo: 4
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
  "orderID": "3964270595789502688"
 }
}
```









`ModifyOrder(req);`

- **Description**

  Modify the price and quantity of orders, cancel orders, delete orders,
  enable or disable orders, etc.  
  For HKCC market, it is invalid to change orders, except that
  cancelling orders is supported.

- **Parameters**



``` protobuf
message C2S
{
    required Common.PacketID packetID = 1; //packet ID, used to prevent replay attack
    required Trd_Common.TrdHeader header = 2; //Transaction common header
    required uint64 orderID = 3; //Order number, if forAll is true, pass 0
    required int32 modifyOrderOp = 4; //Modify the operation type, see the enumeration definition of Trd_Common.ModifyOrderOp
    optional bool forAll = 5; //Whether to operate all orders for this trading account. true: operate all orders, false:operate a single order(by default if missed). Batch operations only support canceling all orders, but do not support disabling all, enabling all or deleting all.

    //The following fields are only for a single order, and modifyOrderOp is valid for ModifyOrderOp_Normal
    optional double qty = 8; //Quantity, option unit is "contract" (0 decimal place accuracy, the excess part is discarded)
    optional double price = 9; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded)
    //The following are used to adjust the price. You have to pass both fields to make it meaningful. Because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 10; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price. true: make adjustment. false: do not make adjustment. If the price is illegal and adjustment is not allowed, an error may occur.
    optional double adjustSideAndLimit = 11; //Direction and limit in percentage for adjustment. Positive number represents upward adjustment, negative number represents downward adjustment. Specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional double auxPrice = 12; //Trigger price
    optional int32 trailType = 13; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 14; //Trailing amount / ratio
    optional double trailSpread = 15; //Specify spread
    optional string orderIDEx = 16; //The server order id, which can be used instead of orderID, or choose one from orderID  
}

message Request
{
    required C2S c2s = 1;
}
```





> - For request packet identification structure, refer to
>   [PacketID](/moomoo-api-doc/en/ftapi/common.html#1903)
> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For the enumeration of modification operations, refer to
>   [ModifyOrderOp](/moomoo-api-doc/en/trade/trade.html#3811)
> - For trail type, refer to
>   [TrailType](/moomoo-api-doc/en/trade/trade.html#12)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required uint64 orderID = 2; //Order number
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

function TrdModifyOrder(){
    const { RetType, PacketID } = Common
    const { TrdEnv, TrdSide, OrderType, SecurityFirm, TrdMarket, TrdSecMarket, ModifyOrderOp } = Trd_Common
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
                    
                    let { errCode, retMsg, retType, s2c : { orderID } } = await websocket.PlaceOrder({
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
                    }); 
                    if(retType == RetType.RetType_Succeed && errCode == 0){
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
                                orderID: orderID,
                                modifyOrderOp: ModifyOrderOp.ModifyOrderOp_Normal,
                                qty: 200,
                                price: 100,
                            },
                        };
                        let { errCode, retMsg, retType, s2c } = await websocket.ModifyOrder(req);
                        console.log("ModifyOrder: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
ModifyOrder: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "orderID": "5870570404030790740"
}
stop
```











Interface Limitations

- A maximum of 20 requests per 30 seconds under a single account ID
  (acc_id), and the time interval between two consecutive requests
  should not be less than 0.04 seconds.
- When using live trading accounts, you need to [unlock
  trade](/moomoo-api-doc/en/trade/unlock.html) **before** calling
  *Modify or Cancel Orders* interface, but when using paper trading
  accounts, you do not need to [unlock
  trade](/moomoo-api-doc/en/trade/unlock.html).





Tip

- For the execution of **modify the order**, to learn more about the
  required parameters for each order type, please [click
  here](/moomoo-api-doc/en/qa/trade.html#2440).
- If you want to **modify the quantity of the order**, the parameter
  **qty** should be equal to the total quantity of the expected
  filled.  
  For example:  
  The quantity of an order is *N* shares, with *n* shares filled. For
  the unfilled *(N-n)* shares, if you want to cancel *x* shares, the
  parameter **modify_order_op** should be *NORMAL*, **qty** should be
  *(N-x)*.
  ![order_quantity](/moomoo-api-doc/assets/img/order_quantity_en.f13725f3.png)
- If you want to cancel an order, the parameter **modify_order_op**
  should be *CANCEL*.  
  For example:  
  The quantity of an order is *N* shares, with *n* shares filled. If you
  want to cancel the unfilled *(N-n)* shares, **modify_order_op** should
  be *CANCEL*, and **qty** and **price** will be ignored.













