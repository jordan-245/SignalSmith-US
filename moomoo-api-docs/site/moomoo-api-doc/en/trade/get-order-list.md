



# <a href="#6833" class="header-anchor">#</a> Get open Orders









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`order_list_query(order_id="", order_market=TrdMarket.NONE, status_filter_list=[], code='', start='', end='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, refresh_cache=False)`

- **Description**

  Query the open order list of the specified trading account

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
  <td style="text-align: left;">order_id</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Order id.
  
    
  
  
   
  
  If specified, only return data for the specified order.<br />
  No filtering by default, return all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">order_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter orders by security market.
  
    
  
  
   
  
  <ul>
  <li>Return open orders for the specified market.</li>
  <li>If this parameter is not passed or the default NONE is used, return
  open orders for all markets.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">status_filter_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Order status filter conditions.
  
    
  
  
   
  
  Only return data for the specified order.<br />
  No filtering by default, return all.<br />
  Data type of elements in the list is <a
  href="/moomoo-api-doc/en/trade/trade.html#8074">OrderStatus</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Security symbol.
  
    
  
  
   
  
  Only return orders whose related security symbols correspond to these
  codes.<br />
  If this parameter is not passed, return all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
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
    <td style="text-align: left;">order_market</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
    <td style="text-align: left;">Order market.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Order quantity.
    
      
    
    
     
    
    Option futures unit is "Contract"
    
    
    
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
    <td style="text-align: left;">currency</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
    <td style="text-align: left;">Transaction currency.</td>
    </tr>
    <tr>
    <td style="text-align: left;">create_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Create time.
    
      
    
    
     
    
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">updated_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last update time.
    
      
    
    
     
    
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.<br />
    The unit of option futures is "Contract"
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Deal quantity
    
      
    
    
     
    
    Option futures unit is "Contract"
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average deal price.
    
      
    
    
     
    
    No precision limit
    
    
    
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
    href="/moomoo-api-doc/en/trade/place-order.html">place_order</a>
    interface parameters for details.
    
    
    
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
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.order_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the order list is not empty
        print(data['order_id'][0])  # Get the first order ID of the order list today
        print(data['order_id'].values.tolist())  # Convert to list
else:
    print('order_list_query error: ', data)
trd_ctx.close()
```





- **Output**



``` python
        code stock_name   order_market   trd_side           order_type   order_status             order_id    qty  price              create_time             updated_time  dealt_qty  dealt_avg_price last_err_msg      remark time_in_force fill_outside_rth session aux_price trail_type trail_value trail_spread currency
0   HK.00700                     HK         BUY           NORMAL  CANCELLED_ALL  6644468615272262086  100.0  520.0  2021-09-06 10:17:52.465  2021-09-07 16:10:22.806        0.0              0.0               asdfg+=@@@           GTC      N/A         N/A       560        N/A         N/A          N/A      HKD
6644468615272262086
['6644468615272262086']
```









## <a href="#8225" class="header-anchor">#</a> Trd_GetOrderList.proto

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2201





`uint GetOrderList(TrdGetOrderList.Request req);`  
`virtual void OnReply_GetOrderList(FTAPI_Conn client, uint nSerialNo, TrdGetOrderList.Response rsp);`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdGetOrderList.C2S c2s = TrdGetOrderList.C2S.CreateBuilder()
                .SetHeader(header)
            .Build();
        TrdGetOrderList.Request req = TrdGetOrderList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetOrderList(req);
        Console.Write("Send TrdGetOrderList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetOrderList(FTAPI_Conn client, uint nSerialNo, TrdGetOrderList.Response rsp)
    {
        Console.Write("Reply: TrdGetOrderList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827793030286254504
Send TrdGetOrderList: 3
Reply: TrdGetOrderList: 3
accID: 281756457888247915
```









`int getOrderList(TrdGetOrderList.Request req);`  
`void onReply_GetOrderList(FTAPI_Conn client, int nSerialNo, TrdGetOrderList.Response rsp);`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
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
        TrdGetOrderList.C2S c2s = TrdGetOrderList.C2S.newBuilder()
                .setHeader(header)
            .build();
        TrdGetOrderList.Request req = TrdGetOrderList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getOrderList(req);
        System.out.printf("Send TrdGetOrderList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOrderList(FTAPI_Conn client, int nSerialNo, TrdGetOrderList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetOrderList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetOrderList: %s\n", json);
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
Send TrdGetOrderList: 2
Receive TrdGetOrderList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "3450309",
      "trdMarket": 1
    },
    "orderList": [{
      "trdSide": 1,
      "orderType": 5,
      "orderStatus": 11,
      "orderID": "5185261023022402893",
      "orderIDEx": "2691191",
      "code": "00700",
      "name": "Tencent",
      "qty": 100.0,
      "price": 594.0,
      "createTime": "2021-06-25 11:38:30",
      "updateTime": "2021-06-25 11:38:30",
      "fillQty": 100.0,
      "fillAvgPrice": 594.0,
      "secMarket": 1,
      "createTimestamp": 1.62459231E9,
      "updateTimestamp": 1.62459231E9,
      "remark": "",
      "timeInForce": 0
    }]
  }
}
```









`Futu::u32_t GetOrderList(const Trd_GetOrderList::Request &stReq);`  
`virtual void OnReply_GetOrderList(Futu::u32_t nSerialNo, const Trd_GetOrderList::Response &stRsp) = 0;`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
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
        Trd_GetOrderList::Request req;
        Trd_GetOrderList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        auto filterStatusList = c2s->mutable_filterstatuslist();
        filterStatusList->Add(Trd_Common::OrderStatus::OrderStatus_Filled_All);

        m_GetOrderListSerialNo = m_pTrdApi->GetOrderList(req);
        cout << "Request GetOrderList SerialNo: " << m_GetOrderListSerialNo << endl;
    }

    virtual void OnReply_GetOrderList(Futu::u32_t nSerialNo, const Trd_GetOrderList::Response &stRsp){
        if(nSerialNo == m_GetOrderListSerialNo)
        {
            cout << "OnReply_GetOrderList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetOrderListSerialNo;
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
Request GetOrderList SerialNo: 4
OnReply_GetOrderList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  }
 }
}
```









`GetOrderList(req);`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetOrderList(){
    const { RetType } = Common
    const { TrdEnv, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ec16fde057a2e7a0'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) {  
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType,s2c: { accList } } = res
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
                        },
                    };

                    websocket.GetOrderList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetOrderList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetOrderList: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "orderList": [{
    "trdSide": 1,
    "orderType": 5,
    "orderStatus": 11,
    "orderID": "3425188649181383443",
    "orderIDEx": "2509214",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-14 11:41:49",
    "updateTime": "2021-09-14 11:41:52",
    "fillQty": 100,
    "fillAvgPrice": 478.2,
    "secMarket": 1,
    "createTimestamp": 1631590909,
    "updateTimestamp": 1631590912,
    "remark": "",
    "timeInForce": 0
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- It will be restricted by the frequency limit for this interface only
  when the cache is refreshed





Tips

- Open orders are arranged in chronological order: earlier orders return
  first, followed by later orders.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`order_list_query(order_id="", order_market=TrdMarket.NONE, status_filter_list=[], code='', start='', end='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, refresh_cache=False)`

- **Description**

  Query the open order list of the specified trading account

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
  <td style="text-align: left;">order_id</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Order id.
  
    
  
  
   
  
  If specified, only return data for the specified order.<br />
  No filtering by default, return all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">order_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter orders by security market.
  
    
  
  
   
  
  <ul>
  <li>Return open orders for the specified market.</li>
  <li>If this parameter is not passed or the default NONE is used, return
  open orders for all markets.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">status_filter_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Order status filter conditions.
  
    
  
  
   
  
  Only return data for the specified order.<br />
  No filtering by default, return all.<br />
  Data type of elements in the list is <a
  href="/moomoo-api-doc/en/trade/trade.html#8074">OrderStatus</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Security symbol.
  
    
  
  
   
  
  Only return orders whose related security symbols correspond to these
  codes.<br />
  If this parameter is not passed, return all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
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
    <td style="text-align: left;">order_market</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
    <td style="text-align: left;">Order market.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Order quantity.
    
      
    
    
     
    
    Option futures unit is "Contract"
    
    
    
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
    <td style="text-align: left;">currency</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
    <td style="text-align: left;">Transaction currency.</td>
    </tr>
    <tr>
    <td style="text-align: left;">create_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Create time.
    
      
    
    
     
    
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">updated_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last update time.
    
      
    
    
     
    
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.<br />
    The unit of option futures is "Contract"
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Deal quantity
    
      
    
    
     
    
    Option futures unit is "Contract"
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">dealt_avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average deal price.
    
      
    
    
     
    
    No precision limit
    
    
    
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
    href="/moomoo-api-doc/en/trade/place-order.html">place_order</a>
    interface parameters for details.
    
    
    
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
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.order_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the order list is not empty
        print(data['order_id'][0])  # Get the first order ID of the order list today
        print(data['order_id'].values.tolist())  # Convert to list
else:
    print('order_list_query error: ', data)
trd_ctx.close()
```





- **Output**



``` python
        code stock_name order_market    trd_side           order_type   order_status             order_id    qty  price              create_time             updated_time  dealt_qty  dealt_avg_price last_err_msg      remark time_in_force fill_outside_rth session aux_price trail_type trail_value trail_spread currency
0   US.AAPL                    US         BUY           NORMAL  CANCELLED_ALL  6644468615272262086  100.0  520.0  2021-09-06 10:17:52.465  2021-09-07 16:10:22.806        0.0              0.0               asdfg+=@@@           GTC        N/A      N/A       560        N/A         N/A          N/A      USD
6644468615272262086
['6644468615272262086']
```









## <a href="#8225-2" class="header-anchor">#</a> Trd_GetOrderList.proto

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2201





`uint GetOrderList(TrdGetOrderList.Request req);`  
`virtual void OnReply_GetOrderList(MMAPI_Conn client, uint nSerialNo, TrdGetOrderList.Response rsp);`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdGetOrderList.C2S c2s = TrdGetOrderList.C2S.CreateBuilder()
                .SetHeader(header)
            .Build();
        TrdGetOrderList.Request req = TrdGetOrderList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetOrderList(req);
        Console.Write("Send TrdGetOrderList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetOrderList(MMAPI_Conn client, uint nSerialNo, TrdGetOrderList.Response rsp)
    {
        Console.Write("Reply: TrdGetOrderList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827793030286254504
Send TrdGetOrderList: 3
Reply: TrdGetOrderList: 3
accID: 281756457888247915
```









`int getOrderList(TrdGetOrderList.Request req);`  
`void onReply_GetOrderList(MMAPI_Conn client, int nSerialNo, TrdGetOrderList.Response rsp);`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
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
        TrdGetOrderList.C2S c2s = TrdGetOrderList.C2S.newBuilder()
                .setHeader(header)
            .build();
        TrdGetOrderList.Request req = TrdGetOrderList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getOrderList(req);
        System.out.printf("Send TrdGetOrderList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOrderList(MMAPI_Conn client, int nSerialNo, TrdGetOrderList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetOrderList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetOrderList: %s\n", json);
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
Send TrdGetOrderList: 2
Receive TrdGetOrderList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "3450309",
      "trdMarket": 1
    },
    "orderList": [{
      "trdSide": 1,
      "orderType": 5,
      "orderStatus": 11,
      "orderID": "5185261023022402893",
      "orderIDEx": "2691191",
      "code": "00700",
      "name": "Tencent",
      "qty": 100.0,
      "price": 594.0,
      "createTime": "2021-06-25 11:38:30",
      "updateTime": "2021-06-25 11:38:30",
      "fillQty": 100.0,
      "fillAvgPrice": 594.0,
      "secMarket": 1,
      "createTimestamp": 1.62459231E9,
      "updateTimestamp": 1.62459231E9,
      "remark": "",
      "timeInForce": 0
    }]
  }
}
```









`moomoo::u32_t GetOrderList(const Trd_GetOrderList::Request &stReq);`  
`virtual void OnReply_GetOrderList(moomoo::u32_t nSerialNo, const Trd_GetOrderList::Response &stRsp) = 0;`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
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
        Trd_GetOrderList::Request req;
        Trd_GetOrderList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        auto filterStatusList = c2s->mutable_filterstatuslist();
        filterStatusList->Add(Trd_Common::OrderStatus::OrderStatus_Filled_All);

        m_GetOrderListSerialNo = m_pTrdApi->GetOrderList(req);
        cout << "Request GetOrderList SerialNo: " << m_GetOrderListSerialNo << endl;
    }

    virtual void OnReply_GetOrderList(moomoo::u32_t nSerialNo, const Trd_GetOrderList::Response &stRsp){
        if(nSerialNo == m_GetOrderListSerialNo)
        {
            cout << "OnReply_GetOrderList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetOrderListSerialNo;
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
Request GetOrderList SerialNo: 4
OnReply_GetOrderList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  }
 }
}
```









`GetOrderList(req);`

- **Description**

  Query the open order list of the specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //Order list
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
> - For order structure, refer to
>   [Order](/moomoo-api-doc/en/trade/trade.html#6192)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdGetOrderList(){
    const { RetType } = Common
    const { TrdEnv, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ec16fde057a2e7a0'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) {  
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType,s2c: { accList } } = res
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
                        },
                    };

                    websocket.GetOrderList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetOrderList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetOrderList: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "orderList": [{
    "trdSide": 1,
    "orderType": 5,
    "orderStatus": 11,
    "orderID": "3425188649181383443",
    "orderIDEx": "2509214",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-14 11:41:49",
    "updateTime": "2021-09-14 11:41:52",
    "fillQty": 100,
    "fillAvgPrice": 478.2,
    "secMarket": 1,
    "createTimestamp": 1631590909,
    "updateTimestamp": 1631590912,
    "remark": "",
    "timeInForce": 0
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- It will be restricted by the frequency limit for this interface only
  when the cache is refreshed





Tips

- Open orders are arranged in chronological order: earlier orders return
  first, followed by later orders.













