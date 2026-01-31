



# <a href="#5974" class="header-anchor">#</a> Get Historical Orders









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`history_order_list_query(status_filter_list=[], code='', order_market=TrdMarket.NONE, start='', end='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0)`

- **Description**

  Query the historical order list of a specified trading account

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
  <td style="text-align: left;">status_filter_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Order status filter conditions.
  
    
  
  
   
  
  Only return the data of the specified Order ID. No filtering by default,
  return all.<br />
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
  <td style="text-align: left;">order_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter orders by security market.
  
    
  
  
   
  
  <ul>
  <li>Return historical orders for the specified market.</li>
  <li>If this parameter is not passed or the default NONE is used, return
  historical orders for all markets.</li>
  </ul>
  
  
  
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
  <td style="text-align: left;">End time
  
    
  
  
   
  
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
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 90 days before ***end***. |
    | str | None | ***end*** is 90 days after ***start***. |
    | None | None | ***start*** is 90 days before, ***end*** is the current date. |

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
ret, data = trd_ctx.history_order_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the order list is not empty
        print(data['order_id'][0])  # Get Order ID of the first holding position
        print(data['order_id'].values.tolist())  # Convert to list
else:
    print('history_order_list_query error: ', data)
trd_ctx.close()
```





- **Output**



``` python
        code stock_name order_market   trd_side           order_type   order_status             order_id    qty  price              create_time             updated_time  dealt_qty  dealt_avg_price last_err_msg      remark time_in_force fill_outside_rth session aux_price trail_type trail_value trail_spread currency
0   HK.00700                 HK          BUY           NORMAL  CANCELLED_ALL  6644468615272262086  100.0  520.0  2021-09-06 10:17:52.465  2021-09-07 16:10:22.806        0.0              0.0               asdfg+=@@@           GTC              N/A     N/A    560        N/A         N/A          N/A      HKD
6644468615272262086
['6644468615272262086']
```









## <a href="#5878" class="header-anchor">#</a> Trd_GetHistoryOrderList.proto

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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

  2221





`uint GetHistoryOrderList(TrdGetHistoryOrderList.Request req);`  
`virtual void OnReply_GetHistoryOrderList(FTAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderList.Response rsp);`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.CreateBuilder().Build();
        TrdGetHistoryOrderList.C2S c2s = TrdGetHistoryOrderList.C2S.CreateBuilder()
                .SetHeader(header)
                .SetFilterConditions(filter)
                .Build();
        TrdGetHistoryOrderList.Request req = TrdGetHistoryOrderList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetHistoryOrderList(req);
        Console.Write("Send TrdGetHistoryOrderList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetHistoryOrderList(FTAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderList.Response rsp)
    {
        Console.Write("Reply: TrdGetHistoryOrderList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827794279500987418
Send TrdGetHistoryOrderList: 3
Reply: TrdGetHistoryOrderList: 3
accID: 281756457888247915
```









`int getHistoryOrderList(TrdGetHistoryOrderList.Request req);`  
`void onReply_GetHistoryOrderList(FTAPI_Conn client, int nSerialNo, TrdGetHistoryOrderList.Response rsp);`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.newBuilder().build();
        TrdGetHistoryOrderList.C2S c2s = TrdGetHistoryOrderList.C2S.newBuilder()
                .setHeader(header)
                .setFilterConditions(filter)
                .build();
        TrdGetHistoryOrderList.Request req = TrdGetHistoryOrderList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getHistoryOrderList(req);
        System.out.printf("Send TrdGetHistoryOrderList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetHistoryOrderList(FTAPI_Conn client, int nSerialNo, TrdGetHistoryOrderList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetHistoryOrderList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetHistoryOrderList: %s\n", json);
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
Send TrdGetHistoryOrderList: 2
Receive TrdGetHistoryOrderList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 2
    },
    "orderList": [{
      "trdSide": 1,
      "orderType": 2,
      "orderStatus": 11,
      "orderID": "6664320708369556828",
      "orderIDEx": "20210330_15680495_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1",
      "code": "FUTU",
      "name": "Futu Holdings Limited",
      "qty": 234.0,
      "price": 0.0,
      "createTime": "2021-03-30 09:34:23.628",
      "updateTime": "2021-03-30 09:34:24.016",
      "fillQty": 234.0,
      "fillAvgPrice": 127.635726495,
      "secMarket": 2,
      "createTimestamp": 1.617111263627814E9,
      "updateTimestamp": 1.617111264016447E9,
      "remark": "",
      "timeInForce": 0,
      "fillOutsideRTH": false,
      "session": RTH
    }]
  }
}
```









`Futu::u32_t GetHistoryOrderList(const Trd_GetHistoryOrderList::Request &stReq);`  
`virtual void OnReply_GetHistoryOrderList(Futu::u32_t nSerialNo, const Trd_GetHistoryOrderList::Response &stRsp) = 0;`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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
        Trd_GetHistoryOrderList::Request req;
        Trd_GetHistoryOrderList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        Trd_Common::TrdFilterConditions *filter = c2s->mutable_filterconditions();
        filter->set_begintime("2021-05-01 00:00:00");
        filter->set_endtime("2021-06-01 00:00:00");
        auto filterStatusList = c2s->mutable_filterstatuslist();
        filterStatusList->Add(Trd_Common::OrderStatus::OrderStatus_Filled_All);

        m_GetHistoryOrderListSerialNo = m_pTrdApi->GetHistoryOrderList(req);
        cout << "Request GetHistoryOrderList SerialNo: " << m_GetHistoryOrderListSerialNo << endl;
    }

    virtual void OnReply_GetHistoryOrderList(Futu::u32_t nSerialNo, const Trd_GetHistoryOrderList::Response &stRsp){
        if(nSerialNo == m_GetHistoryOrderListSerialNo)
        {
            cout << "OnReply_GetHistoryOrderList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetHistoryOrderListSerialNo;
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
Request GetHistoryOrderList SerialNo: 4
OnReply_GetHistoryOrderList SerialNo: 4
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
  "orderList": [
   {
    "trdSide": 1,
    "orderType": 5,
    "orderStatus": 11,
    "orderID": "200810789995260636",
    "orderIDEx": "1689799",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 649.5,
    "createTime": "2021-05-31 21:01:21",
    "updateTime": "2021-06-01 09:30:07",
    "fillQty": 100,
    "fillAvgPrice": 618.5,
    "secMarket": 1,
    "createTimestamp": 1622466081,
    "updateTimestamp": 1622511007,
    "remark": "buy00700",
    "timeInForce": 0
   },
...
   {
    "trdSide": 1,
    "orderType": 5,
    "orderStatus": 11,
    "orderID": "8091353323268200353",
    "orderIDEx": "1672200",
    "code": "00700",
    "name": "Tencent",
    "qty": 400,
    "price": 605,
    "createTime": "2021-05-27 12:29:38",
    "updateTime": "2021-05-27 13:00:08",
    "fillQty": 400,
    "fillAvgPrice": 605,
    "secMarket": 1,
    "createTimestamp": 1622089778,
    "updateTimestamp": 1622091608,
    "remark": "",
    "timeInForce": 0
   }
  ]
 }
}
```









`GetHistoryOrderList(req);`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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

function TrdGetHistoryOrderList(){
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
                            filterConditions:{
                                beginTime:"2021-09-01 00:00:00",
                                endTime:"2021-09-30 00:00:00",
                            },
                        },
                    };

                    websocket.GetHistoryOrderList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetHistoryOrderList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetHistoryOrderList: errCode 0, retMsg , retType 0
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





Tips

- Historical orders are arranged in reverse chronological order: later
  orders return first, followed by earlier orders.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`history_order_list_query(status_filter_list=[], code='', order_market=TrdMarket.NONE, start='', end='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0)`

- **Description**

  Query the historical order list of a specified trading account

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
  <td style="text-align: left;">status_filter_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Order status filter conditions.
  
    
  
  
   
  
  Only return the data of the specified Order ID. No filtering by default,
  return all.<br />
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
  <td style="text-align: left;">order_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter orders by security market.
  
    
  
  
   
  
  <ul>
  <li>Return historical orders for the specified market.</li>
  <li>If this parameter is not passed or the default NONE is used, return
  historical orders for all markets.</li>
  </ul>
  
  
  
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
  <td style="text-align: left;">End time
  
    
  
  
   
  
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
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 90 days before ***end***. |
    | str | None | ***end*** is 90 days after ***start***. |
    | None | None | ***start*** is 90 days before, ***end*** is the current date. |

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
ret, data = trd_ctx.history_order_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the order list is not empty
        print(data['order_id'][0])  # Get Order ID of the first holding position
        print(data['order_id'].values.tolist())  # Convert to list
else:
    print('history_order_list_query error: ', data)
trd_ctx.close()
```





- **Output**



``` python
        code stock_name  order_market  trd_side           order_type   order_status             order_id    qty  price              create_time             updated_time  dealt_qty  dealt_avg_price last_err_msg      remark time_in_force fill_outside_rth session aux_price trail_type trail_value trail_spread currency
0   US.AAPL                  US          BUY           NORMAL  CANCELLED_ALL  6644468615272262086  100.0  520.0  2021-09-06 10:17:52.465  2021-09-07 16:10:22.806        0.0              0.0               asdfg+=@@@           GTC              N/A       N/A      560        N/A         N/A          N/A      USD
6644468615272262086
['6644468615272262086']
```









## <a href="#5878-2" class="header-anchor">#</a> Trd_GetHistoryOrderList.proto

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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

  2221





`uint GetHistoryOrderList(TrdGetHistoryOrderList.Request req);`  
`virtual void OnReply_GetHistoryOrderList(MMAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderList.Response rsp);`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.CreateBuilder().Build();
        TrdGetHistoryOrderList.C2S c2s = TrdGetHistoryOrderList.C2S.CreateBuilder()
                .SetHeader(header)
                .SetFilterConditions(filter)
                .Build();
        TrdGetHistoryOrderList.Request req = TrdGetHistoryOrderList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetHistoryOrderList(req);
        Console.Write("Send TrdGetHistoryOrderList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetHistoryOrderList(MMAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderList.Response rsp)
    {
        Console.Write("Reply: TrdGetHistoryOrderList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827794279500987418
Send TrdGetHistoryOrderList: 3
Reply: TrdGetHistoryOrderList: 3
accID: 281756457888247915
```









`int getHistoryOrderList(TrdGetHistoryOrderList.Request req);`  
`void onReply_GetHistoryOrderList(MMAPI_Conn client, int nSerialNo, TrdGetHistoryOrderList.Response rsp);`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.newBuilder().build();
        TrdGetHistoryOrderList.C2S c2s = TrdGetHistoryOrderList.C2S.newBuilder()
                .setHeader(header)
                .setFilterConditions(filter)
                .build();
        TrdGetHistoryOrderList.Request req = TrdGetHistoryOrderList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getHistoryOrderList(req);
        System.out.printf("Send TrdGetHistoryOrderList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetHistoryOrderList(MMAPI_Conn client, int nSerialNo, TrdGetHistoryOrderList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetHistoryOrderList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetHistoryOrderList: %s\n", json);
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
Send TrdGetHistoryOrderList: 2
Receive TrdGetHistoryOrderList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 2
    },
    "orderList": [{
      "trdSide": 1,
      "orderType": 2,
      "orderStatus": 11,
      "orderID": "6664320708369556828",
      "orderIDEx": "20210330_15680495_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1",
      "code": "FUTU",
      "name": "Futu Holdings Limited",
      "qty": 234.0,
      "price": 0.0,
      "createTime": "2021-03-30 09:34:23.628",
      "updateTime": "2021-03-30 09:34:24.016",
      "fillQty": 234.0,
      "fillAvgPrice": 127.635726495,
      "secMarket": 2,
      "createTimestamp": 1.617111263627814E9,
      "updateTimestamp": 1.617111264016447E9,
      "remark": "",
      "timeInForce": 0,
      "fillOutsideRTH": false,
      "session": RTH
    }]
  }
}
```









`moomoo::u32_t GetHistoryOrderList(const Trd_GetHistoryOrderList::Request &stReq);`  
`virtual void OnReply_GetHistoryOrderList(moomoo::u32_t nSerialNo, const Trd_GetHistoryOrderList::Response &stRsp) = 0;`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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
        Trd_GetHistoryOrderList::Request req;
        Trd_GetHistoryOrderList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        Trd_Common::TrdFilterConditions *filter = c2s->mutable_filterconditions();
        filter->set_begintime("2021-05-01 00:00:00");
        filter->set_endtime("2021-06-01 00:00:00");
        auto filterStatusList = c2s->mutable_filterstatuslist();
        filterStatusList->Add(Trd_Common::OrderStatus::OrderStatus_Filled_All);

        m_GetHistoryOrderListSerialNo = m_pTrdApi->GetHistoryOrderList(req);
        cout << "Request GetHistoryOrderList SerialNo: " << m_GetHistoryOrderListSerialNo << endl;
    }

    virtual void OnReply_GetHistoryOrderList(moomoo::u32_t nSerialNo, const Trd_GetHistoryOrderList::Response &stRsp){
        if(nSerialNo == m_GetHistoryOrderListSerialNo)
        {
            cout << "OnReply_GetHistoryOrderList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetHistoryOrderListSerialNo;
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
Request GetHistoryOrderList SerialNo: 4
OnReply_GetHistoryOrderList SerialNo: 4
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
  "orderList": [
   {
    "trdSide": 1,
    "orderType": 5,
    "orderStatus": 11,
    "orderID": "200810789995260636",
    "orderIDEx": "1689799",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 649.5,
    "createTime": "2021-05-31 21:01:21",
    "updateTime": "2021-06-01 09:30:07",
    "fillQty": 100,
    "fillAvgPrice": 618.5,
    "secMarket": 1,
    "createTimestamp": 1622466081,
    "updateTimestamp": 1622511007,
    "remark": "buy00700",
    "timeInForce": 0
   },
...
   {
    "trdSide": 1,
    "orderType": 5,
    "orderStatus": 11,
    "orderID": "8091353323268200353",
    "orderIDEx": "1672200",
    "code": "00700",
    "name": "Tencent",
    "qty": 400,
    "price": 605,
    "createTime": "2021-05-27 12:29:38",
    "updateTime": "2021-05-27 13:00:08",
    "fillQty": 400,
    "fillAvgPrice": 605,
    "secMarket": 1,
    "createTimestamp": 1622089778,
    "updateTimestamp": 1622091608,
    "remark": "",
    "timeInForce": 0
   }
  ]
 }
}
```









`GetHistoryOrderList(req);`

- **Description**

  Query the historical order list of a specified trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    repeated int32 filterStatusList = 3; //Trd_Common::OrderStatus. Order status list to be filtered
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)
> - For order status enumeration, refer to
>   [OrderStatus](/moomoo-api-doc/en/trade/trade.html#8074)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Order orderList = 2; //list of historical orders
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

function TrdGetHistoryOrderList(){
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
                            filterConditions:{
                                beginTime:"2021-09-01 00:00:00",
                                endTime:"2021-09-30 00:00:00",
                            },
                        },
                    };

                    websocket.GetHistoryOrderList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetHistoryOrderList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetHistoryOrderList: errCode 0, retMsg , retType 0
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





Tips

- Historical orders are arranged in reverse chronological order: later
  orders return first, followed by earlier orders.













