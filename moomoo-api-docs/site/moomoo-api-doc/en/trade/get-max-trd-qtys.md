



# <a href="#334" class="header-anchor">#</a> Query the Maximum Quantity that Can be Bought or Sold









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`acctradinginfo_query(order_type, code, price, order_id=None, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, session=Session.NONE)`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

  Cash account request options are not supported.

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
  <td style="text-align: left;">order_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#245">OrderType</a></td>
  <td style="text-align: left;">Order type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Security code.
  
    
  
  
   
  
  If it is a future main code, it will be automatically converted to the
  corresponding actual contract code.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Quotation.
  
    
  
  
   
  
  <ul>
  <li>Accuracy to 3 decimal places for securities account, and the excess
  part will be discarded.</li>
  <li>Accuracy to 9 decimal places for futures account, and the excess
  part will be discarded.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">order_id</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Order ID.
  
    
  
  
   
  
  <ul>
  <li>The default is None, and the query is the maximum quantity that can
  be bought or sold of the new order.</li>
  <li>If you want to modify order, the order number must be sent. At this
  time, when calculating, the maximum quantity that can be changed for
  this order will be returned.</li>
  <li>If you use this parameter to query the maximum changeable quantity
  of an order, you need to call this interface more than 0.5 seconds after
  the order is placed.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">adjust_limit</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Price adjustment range.
  
    
  
  
   
  
  OpenD will automatically adjust the incoming price to the legal
  price.(Futures will ignore this parameter.)
  <ul>
  <li>A positive number represents an upward adjustment, and a negative
  number represents a downward adjustment.</li>
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
  <td>If ret == RET_OK, account list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Account list format as follows:
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
    <td style="text-align: left;">max_cash_buy</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Buy on cash.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity that can be bought in cash.</li>
    <li>The unit of options is "contract".</li>
    <li>Futures accounts are not applicable.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_cash_and_margin_buy</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Buy on margin.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity that can be bought on margin.</li>
    <li>The unit of options is "contract".</li>
    <li>Futures accounts are not applicable.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_position_sell</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Sell on position.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity can be sold.</li>
    <li>The unit of options is "contract".</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_sell_short</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short sell.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity can be shorted.</li>
    <li>The unit of options is "contract".</li>
    <li>Futures accounts are not applicable.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_buy_back</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short positions.
    
      
    
    
     
    
    <ul>
    <li>Buyback required quantity to close a position. When holding short
    positions, you must first buy back the short positions before you can
    continue to buy long.</li>
    <li>The unit of options and futures is "contract".</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">long_required_im</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Initial margin change when buying one
    contract of an asset.
    
      
    
    
     
    
    <ul>
    <li>Currently only futures and options apply.</li>
    <li>No position: Returns the initial margin needed to buy one contract
    (a positive value).</li>
    <li>Long position: Returns the initial margin required to buy one
    contract (a positive value).</li>
    <li>Short position: Returns the initial margin released for buying back
    one contract (a negative value).</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_required_im</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Initial margin change when selling one
    contract of an asset.
    
      
    
    
     
    
    <ul>
    <li>Currently only futures and options apply.</li>
    <li>No position: Returns the initial margin needed to short one contract
    (a positive value).</li>
    <li>Long position: Returns the initial margin released for selling one
    contract (a negative value).</li>
    <li>Short position: Returns the initial margin needed to short one
    contract (a positive value).</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">session</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
    <td style="text-align: left;">Order session (Only applied to US
    stocks)</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.acctradinginfo_query(order_type=OrderType.NORMAL, code='HK.00700', price=400)
if ret == RET_OK:
    print(data)
    print(data['max_cash_and_margin_buy'][0])  # Get maximum quantity that can be bought on margin
else:
    print('acctradinginfo_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
    max_cash_buy  max_cash_and_margin_buy  max_position_sell  max_sell_short  max_buy_back long_required_im short_required_im  session
0           0.0                   1500.0                0.0             0.0           0.0              N/A               N/A       N/A
1500.0
```









## <a href="#5308" class="header-anchor">#</a> Trd_GetMaxTrdQtys.proto

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2111





`uint GetMaxTrdQtys(TrdGetMaxTrdQtys.Request req);`  
`virtual void OnReply_GetMaxTrdQtys(FTAPI_Conn client, uint nSerialNo, TrdGetMaxTrdQtys.Response rsp);`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
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
        TrdGetMaxTrdQtys.C2S c2s = TrdGetMaxTrdQtys.C2S.CreateBuilder()
                .SetHeader(header)
                .SetOrderType((int)TrdCommon.OrderType.OrderType_Normal)
                .SetCode("00700")
                .SetPrice(520)
                .SetSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK)
            .Build();
        TrdGetMaxTrdQtys.Request req = TrdGetMaxTrdQtys.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetMaxTrdQtys(req);
        Console.Write("Send TrdGetMaxTrdQtys: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetMaxTrdQtys(FTAPI_Conn client, uint nSerialNo, TrdGetMaxTrdQtys.Response rsp)
    {
        Console.Write("Reply: TrdGetMaxTrdQtys: {0} \n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6826812678028044696
Send TrdGetMaxTrdQtys: 3
Reply: TrdGetMaxTrdQtys: 3
accID: 281756457888247915
```









`int getMaxTrdQtys(TrdGetMaxTrdQtys.Request req);`  
`void onReply_GetMaxTrdQtys(FTAPI_Conn client, int nSerialNo, TrdGetMaxTrdQtys.Response rsp);`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
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
        TrdGetMaxTrdQtys.C2S c2s = TrdGetMaxTrdQtys.C2S.newBuilder()
                .setHeader(header)
                .setOrderType(TrdCommon.OrderType.OrderType_Normal_VALUE)
                .setCode("00700")
                .setPrice(520)
                .setSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK_VALUE)
            .build();
        TrdGetMaxTrdQtys.Request req = TrdGetMaxTrdQtys.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getMaxTrdQtys(req);
        System.out.printf("Send TrdGetMaxTrdQtys: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetMaxTrdQtys(FTAPI_Conn client, int nSerialNo, TrdGetMaxTrdQtys.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetMaxTrdQtys failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetMaxTrdQtys: %s\n", json);
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
Send TrdGetMaxTrdQtys: 2
Receive TrdGetMaxTrdQtys: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "maxTrdQtys": {
      "maxCashBuy": 0.0,
      "maxCashAndMarginBuy": 1400.0,
      "maxPositionSell": 0.0,
      "maxSellShort": 0.0,
      "maxBuyBack": 0.0
    }
  }
}
```









`Futu::u32_t GetMaxTrdQtys(const Trd_GetMaxTrdQtys::Request &stReq);`  
`virtual void OnReply_GetMaxTrdQtys(Futu::u32_t nSerialNo, const Trd_GetMaxTrdQtys::Response &stRsp) = 0;`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
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
        Trd_GetMaxTrdQtys::Request req;
        Trd_GetMaxTrdQtys::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        c2s->set_ordertype(1);
        c2s->set_code("00700");
        c2s->set_price(520);
        c2s->set_secmarket(Trd_Common::TrdMarket::TrdMarket_HK);

        m_GetMaxTrdQtysSerialNo = m_pTrdApi->GetMaxTrdQtys(req);
        cout << "Request GetMaxTrdQtys SerialNo: " << m_GetMaxTrdQtysSerialNo << endl;
    }

    virtual void OnReply_GetMaxTrdQtys(Futu::u32_t nSerialNo, const Trd_GetMaxTrdQtys::Response &stRsp){
        if(nSerialNo == m_GetMaxTrdQtysSerialNo)
        {
            cout << "OnReply_GetMaxTrdQtys SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetMaxTrdQtysSerialNo;
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
Request GetMaxTrdQtys SerialNo: 4
OnReply_GetMaxTrdQtys SerialNo: 4
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
  "maxTrdQtys": {
   "maxCashBuy": 1500,
   "maxCashAndMarginBuy": 1500,
   "maxPositionSell": 300
  }
 }
}
```









`GetMaxTrdQtys(req);`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetMaxTrdQtys(){
    const { RetType } = Common
    const { TrdEnv, OrderType, TrdMarket } = Trd_Common
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
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            orderType: OrderType.OrderType_Normal,
                            code: "00700", // The code in the market corresponding to the specified account
                            price: 100,
                            secMarket: TrdSecMarket.TrdSecMarket_HK,
                        },
                    };

                    websocket.GetMaxTrdQtys(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetMaxTrdQtys: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetMaxTrdQtys: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "maxTrdQtys": {
    "maxCashBuy": 1300,
    "maxCashAndMarginBuy": 1300,
    "maxPositionSell": 1900
  }
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).





Tips

- The cash account does not support trading derivatives, so it is
  unsupported to query options through the cash account.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`acctradinginfo_query(order_type, code, price, order_id=None, adjust_limit=0, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, session=Session.NONE)`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

  Cash account request options are not supported.

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
  <td style="text-align: left;">order_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#245">OrderType</a></td>
  <td style="text-align: left;">Order type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Security code.
  
    
  
  
   
  
  If it is a future main code, it will be automatically converted to the
  corresponding actual contract code.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">price</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Quotation.
  
    
  
  
   
  
  <ul>
  <li>Accuracy to 3 decimal places for securities account, and the excess
  part will be discarded.</li>
  <li>Accuracy to 9 decimal places for futures account, and the excess
  part will be discarded.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">order_id</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Order ID.
  
    
  
  
   
  
  <ul>
  <li>The default is None, and the query is the maximum quantity that can
  be bought or sold of the new order.</li>
  <li>If you want to modify order, the order number must be sent. At this
  time, when calculating, the maximum quantity that can be changed for
  this order will be returned.</li>
  <li>If you use this parameter to query the maximum changeable quantity
  of an order, you need to call this interface more than 0.5 seconds after
  the order is placed.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">adjust_limit</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Price adjustment range.
  
    
  
  
   
  
  OpenD will automatically adjust the incoming price to the legal
  price.(Futures will ignore this parameter.)
  <ul>
  <li>A positive number represents an upward adjustment, and a negative
  number represents a downward adjustment.</li>
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
  <td>If ret == RET_OK, account list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Account list format as follows:
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
    <td style="text-align: left;">max_cash_buy</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Buy on cash.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity that can be bought in cash.</li>
    <li>The unit of options is "contract".</li>
    <li>Futures accounts are not applicable.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_cash_and_margin_buy</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Buy on margin.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity that can be bought on margin.</li>
    <li>The unit of options is "contract".</li>
    <li>Futures accounts are not applicable.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_position_sell</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Sell on position.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity can be sold.</li>
    <li>The unit of options is "contract".</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_sell_short</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short sell.
    
      
    
    
     
    
    <ul>
    <li>Maximum quantity can be shorted.</li>
    <li>The unit of options is "contract".</li>
    <li>Futures accounts are not applicable.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">max_buy_back</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short positions.
    
      
    
    
     
    
    <ul>
    <li>Buyback required quantity to close a position. When holding short
    positions, you must first buy back the short positions before you can
    continue to buy long.</li>
    <li>The unit of options and futures is "contract".</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">long_required_im</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Initial margin change when buying one
    contract of an asset.
    
      
    
    
     
    
    <ul>
    <li>Currently only futures and options apply.</li>
    <li>No position: Returns the initial margin needed to buy one contract
    (a positive value).</li>
    <li>Long position: Returns the initial margin required to buy one
    contract (a positive value).</li>
    <li>Short position: Returns the initial margin released for buying back
    one contract (a negative value).</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_required_im</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Initial margin change when selling one
    contract of an asset.
    
      
    
    
     
    
    <ul>
    <li>Currently only futures and options apply.</li>
    <li>No position: Returns the initial margin needed to short one contract
    (a positive value).</li>
    <li>Long position: Returns the initial margin released for selling one
    contract (a negative value).</li>
    <li>Short position: Returns the initial margin needed to short one
    contract (a positive value).</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">session</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
    <td style="text-align: left;">Order session (Only applied to US
    stocks)</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.acctradinginfo_query(order_type=OrderType.NORMAL, code='US.AAPL', price=400)
if ret == RET_OK:
    print(data)
    print(data['max_cash_and_margin_buy'][0])  # Get maximum quantity that can be bought on margin
else:
    print('acctradinginfo_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
    max_cash_buy  max_cash_and_margin_buy  max_position_sell  max_sell_short  max_buy_back long_required_im short_required_im   session
0           0.0                   1500.0                0.0             0.0           0.0              N/A               N/A           N/A 
1500.0
```









## <a href="#5308-2" class="header-anchor">#</a> Trd_GetMaxTrdQtys.proto

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2111





`uint GetMaxTrdQtys(TrdGetMaxTrdQtys.Request req);`  
`virtual void OnReply_GetMaxTrdQtys(MMAPI_Conn client, uint nSerialNo, TrdGetMaxTrdQtys.Response rsp);`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
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
        TrdGetMaxTrdQtys.C2S c2s = TrdGetMaxTrdQtys.C2S.CreateBuilder()
                .SetHeader(header)
                .SetOrderType((int)TrdCommon.OrderType.OrderType_Normal)
                .SetCode("00700")
                .SetPrice(520)
                .SetSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK)
            .Build();
        TrdGetMaxTrdQtys.Request req = TrdGetMaxTrdQtys.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetMaxTrdQtys(req);
        Console.Write("Send TrdGetMaxTrdQtys: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetMaxTrdQtys(MMAPI_Conn client, uint nSerialNo, TrdGetMaxTrdQtys.Response rsp)
    {
        Console.Write("Reply: TrdGetMaxTrdQtys: {0} \n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6826812678028044696
Send TrdGetMaxTrdQtys: 3
Reply: TrdGetMaxTrdQtys: 3
accID: 281756457888247915
```









`int getMaxTrdQtys(TrdGetMaxTrdQtys.Request req);`  
`void onReply_GetMaxTrdQtys(MMAPI_Conn client, int nSerialNo, TrdGetMaxTrdQtys.Response rsp);`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
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
        TrdGetMaxTrdQtys.C2S c2s = TrdGetMaxTrdQtys.C2S.newBuilder()
                .setHeader(header)
                .setOrderType(TrdCommon.OrderType.OrderType_Normal_VALUE)
                .setCode("00700")
                .setPrice(520)
                .setSecMarket(TrdCommon.TrdSecMarket.TrdSecMarket_HK_VALUE)
            .build();
        TrdGetMaxTrdQtys.Request req = TrdGetMaxTrdQtys.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getMaxTrdQtys(req);
        System.out.printf("Send TrdGetMaxTrdQtys: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetMaxTrdQtys(MMAPI_Conn client, int nSerialNo, TrdGetMaxTrdQtys.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetMaxTrdQtys failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetMaxTrdQtys: %s\n", json);
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
Send TrdGetMaxTrdQtys: 2
Receive TrdGetMaxTrdQtys: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "maxTrdQtys": {
      "maxCashBuy": 0.0,
      "maxCashAndMarginBuy": 1400.0,
      "maxPositionSell": 0.0,
      "maxSellShort": 0.0,
      "maxBuyBack": 0.0
    }
  }
}
```









`moomoo::u32_t GetMaxTrdQtys(const Trd_GetMaxTrdQtys::Request &stReq);`  
`virtual void OnReply_GetMaxTrdQtys(moomoo::u32_t nSerialNo, const Trd_GetMaxTrdQtys::Response &stRsp) = 0;`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
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
        Trd_GetMaxTrdQtys::Request req;
        Trd_GetMaxTrdQtys::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        c2s->set_ordertype(1);
        c2s->set_code("00700");
        c2s->set_price(520);
        c2s->set_secmarket(Trd_Common::TrdMarket::TrdMarket_HK);

        m_GetMaxTrdQtysSerialNo = m_pTrdApi->GetMaxTrdQtys(req);
        cout << "Request GetMaxTrdQtys SerialNo: " << m_GetMaxTrdQtysSerialNo << endl;
    }

    virtual void OnReply_GetMaxTrdQtys(moomoo::u32_t nSerialNo, const Trd_GetMaxTrdQtys::Response &stRsp){
        if(nSerialNo == m_GetMaxTrdQtysSerialNo)
        {
            cout << "OnReply_GetMaxTrdQtys SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetMaxTrdQtysSerialNo;
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
Request GetMaxTrdQtys SerialNo: 4
OnReply_GetMaxTrdQtys SerialNo: 4
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
  "maxTrdQtys": {
   "maxCashBuy": 1500,
   "maxCashAndMarginBuy": 1500,
   "maxPositionSell": 300
  }
 }
}
```









`GetMaxTrdQtys(req);`

- **Description**

  Query the maximum quantity that can be bought or sold under a
  specifictrading account, and you can also query the maximum changeable
  quantity of a specific order under a specifictrading account.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required int32 orderType = 2; //Order type, see the enumeration definition of Trd_Common.OrderType
    required string code = 3; //Code, Hong Kong stocks must be 5-digits, A-shares must be 6-digits, and US stocks are not restricted
    required double price = 4; //Price, (Accuracy to 3 decimal places for securities account, 9 decimal places for futures account, and the excess part will be discarded). If it is an auction or market order, please also fill in a current price so that the server can calculate
    optional uint64 orderID = 5; //Order number, not required for new orders. For modifying orders, original order number is required, because the original order quantity counts for the maximum transaction quantity of the modified order.
    //In order to ensure the synchronization with the price of the order, price adjustment options are also provided. The following 2 fields are used for price adjustments, which are meaningful for HK stocks and A-shares, because there is a minimum price change step for HK stocks, and the quotation of A-shares is accurate to 2 decimal places. It is not nessessary for US stocks.
    optional bool adjustPrice = 6; //Whether to adjust the price, if the price is illegal, whether to adjust to the legal price, true adjustment, false no adjustment
    optional double adjustSideAndLimit = 7; //Adjustment direction and adjustment range percentage limit, positive number represents upward adjustment, negative number represents downward adjustment, specific value represents adjustment range limit, such as: 0.015 represents upward adjustment and the range does not exceed 1.5%; -0.01 Represents downward adjustment and the amplitude does not exceed 1%
    optional int32 secMarket = 8; //Market to which the security belongs, see the enumeration definition of TrdSecMarket
    optional string orderIDEx = 9; //The server order id, which can be used instead of orderID, or choose one from orderID   
    optional int32 session = 18; //US Stock session, see Common.Session enumeration definition
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order type, refer to
>   [OrderType](/moomoo-api-doc/en/trade/trade.html#245)
> - For stock market, refer to
>   [TrdSecMarket](/moomoo-api-doc/en/trade/trade.html#4905)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.MaxTrdQtys maxTrdQtys = 2; //Maximum tradable quantity structure
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
> - For the structure of the maximum tradable quantity, refer to
>   [MaxTrdQtys](/moomoo-api-doc/en/trade/trade.html#8387)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdGetMaxTrdQtys(){
    const { RetType } = Common
    const { TrdEnv, OrderType, TrdMarket } = Trd_Common
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
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            orderType: OrderType.OrderType_Normal,
                            code: "00700", // The code in the market corresponding to the specified account
                            price: 100,
                            secMarket: TrdSecMarket.TrdSecMarket_HK,
                        },
                    };

                    websocket.GetMaxTrdQtys(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetMaxTrdQtys: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetMaxTrdQtys: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "maxTrdQtys": {
    "maxCashBuy": 1300,
    "maxCashAndMarginBuy": 1300,
    "maxPositionSell": 1900
  }
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).





Tips

- The cash account does not support trading derivatives, so it is
  unsupported to query options through the cash account.
- Maximum quantity that can be bought for futures should be calculated
  by yourself. The formula is floor(Max buying power/Initial margin
  change when buying one contract of an asset). Max buying power is from
  [Get Account Funds](/moomoo-api-doc/en/trade/get-funds.html).













