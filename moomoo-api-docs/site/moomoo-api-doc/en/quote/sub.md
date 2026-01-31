



# <a href="#2733" class="header-anchor">#</a> Subscribe and Unsubscribe









- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#4206" class="header-anchor">#</a> Subscribe to Real-Time Market Data

`subscribe(code_list, subtype_list, is_first_push=True, subscribe_push=True, is_detailed_orderbook=False, extended_time=False, session=Session.NONE)`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

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
  <td style="text-align: left;">A list of stock codes that need to be
  subscribed.
  
    
  
  
   
  
  Data type of elements in the list is str.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">subtype_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">List of data types that need to be
  subscribed.
  
    
  
  
   
  
  Data type of elements in the list is <a
  href="/moomoo-api-doc/en/quote/quote.html#7721">SubType</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">is_first_push</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to push the cached data
  immediately after a successful subscription.
  
    
  
  
   
  
  <ul>
  <li>True: Push the cached data. When there is a disconnection and
  reconnection between scripts and OpenD, the last data before the
  disconnection will be pushed again if it is set to True when
  resubscribing.</li>
  <li>False: Do not push the cached data. Wait for the latest data to be
  pushed from Futu server.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">subscribe_push</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to push data after subscription.
  
    
  
  
   
  
  After subscription, OpenD provides <a
  href="/moomoo-api-doc/en/qa/quote.html#5505">two methods to obtain
  data</a>. If you only use the method of <strong>Get Real-time
  Data</strong> , setting to False can save part of the performance cost.
  <ul>
  <li>True: Push data. It must be set to True if the <strong>Real-time
  data Callback</strong> method is used.</li>
  <li>False: Do not push data. It is recommended to set to False if
  <strong>only</strong> using the <strong>Get Real-time
  Data</strong>.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">is_detailed_orderbook</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to subscribe to the detailed order
  book.
  
    
  
  
   
  
  <ul>
  <li>Only for Hong Kong stocks ORDER_BOOK type under the authority of
  Hong Kong stocks SF market.</li>
  <li>Under the authority of US stocks &amp; futures LV2, the detailed
  order book is not provided.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">extended_time</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to allow pre-market and
  after-hours data of US stocks.
  
    
  
  
   
  
  Only used for subscribing to real-time candlestick and real-time Time
  Frame and real-time tick-by-tick of US stocks.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">session</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
  <td style="text-align: left;">US stocks quotes session
  
    
  
  
   
  
  <ul>
  <li>Only used for subscribing to real-time candlestick and real-time
  Time Frame and real-time tick-by-tick of US stocks.</li>
  <li>Please choose 'ALL' to subscribe 24H quotes for US stocks. The
  'OVERNIGHT' is not allowed.</li>
  <li>Minimum version requirements: 9.2.4207</li>
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
  <td rowspan="2">err_message</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
import time
from futu import *
class OrderBookTest(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s"% data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBookTest()
quote_ctx.set_handler(handler) # Set real-time swing callback
quote_ctx.subscribe(['US.AAPL'], [SubType.ORDER_BOOK]) # Subscribe to the order type, OpenD starts to receive continuous push from the server
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
OrderBookTest  {'code': 'US.AAPL', 'name': 'Apple', 'svr_recv_time_bid': '2025-04-07 05:00:52.266', 'svr_recv_time_ask': '2025-04-07 05:00:53.973', 'Bid': [(180.2, 15, 3, {}), (180.19, 1, 1, {}), (180.18, 11, 2, {}), (180.14, 200, 1, {}), (180.13, 3, 2, {}), (180.1, 99, 3, {}), (180.05, 3, 1, {}), (180.03, 400, 1, {}), (180.02, 10, 1, {}), (180.01, 100, 1, {}), (180.0, 441, 24, {})], 'Ask': [(180.3, 100, 1, {}), (180.38, 4, 2, {}), (180.4, 100, 1, {}), (180.42, 200, 1, {}), (180.46, 29, 1, {}), (180.5, 1019, 2, {}), (180.6, 1000, 1, {}), (180.8, 2001, 3, {}), (180.84, 15, 2, {}), (181.0, 2036, 4, {}), (181.2, 2000, 2, {}), (181.3, 3, 1, {}), (181.4, 2021, 3, {}), (181.5, 59, 2, {}), (181.79, 9, 1, {}), (181.8, 20, 1, {}), (181.9, 94, 4, {}), (181.98, 20, 1, {}), (182.0, 150, 7, {})]}
```





## <a href="#5742" class="header-anchor">#</a> Cancel Market Data Subscription

`unsubscribe(code_list, subtype_list, unsubscribe_all=False)`

- **Description**

  unsubscribe

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
  <td style="text-align: left;">A list of stock codes to unsubscribe.
  
    
  
  
   
  
  Data type of elements in the list is str.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">subtype_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">List of data types that need to be
  subscribed.
  
    
  
  
   
  
  Data type of elements in the list is <a
  href="/moomoo-api-doc/en/quote/quote.html#7721">SubType</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">unsubscribe_all</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Cancel all subscriptions.
  
    
  
  
   
  
  Ignore other parameters when it is True.
  
  
  
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
  <td rowspan="2">err_message</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from futu import *
import time
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

print('current subscription status :', quote_ctx.query_subscription()) # Query the initial subscription status
ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.QUOTE, SubType.TICKER], subscribe_push=False, session=Session.ALL)
# First subscribed to the two types of QUOTE and TICKER. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
    print('subscribe successfully! current subscription status :', quote_ctx.query_subscription()) # Query subscription status after successful subscription
    time.sleep(60) # You can unsubscribe at least 1 minute after subscribing
    ret_unsub, err_message_unsub = quote_ctx.unsubscribe(['US.AAPL'], [SubType.QUOTE])
    if ret_unsub == RET_OK:
        print('unsubscribe successfully! current subscription status:', quote_ctx.query_subscription()) # Query the subscription status after canceling the subscription
    else:
        print('unsubscription failed!', err_message_unsub)
else:
    print('subscription failed', err_message)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
current subscription status : (0, {'total_used': 0, 'remain': 1000, 'own_used': 0, 'sub_list': {}})
subscribe successfully！current subscription status : (0, {'total_used': 2, 'remain': 998, 'own_used': 2, 'sub_list': {'QUOTE': ['US.AAPL'], 'TICKER': ['US.AAPL']}})
unsubscribe successfully！current subscription status: (0, {'total_used': 1, 'remain': 999, 'own_used': 1, 'sub_list': {'TICKER': ['US.AAPL']}})
```





## <a href="#7612" class="header-anchor">#</a> Cancel All Market Data Subscriptions

`unsubscribe_all()`

- **Description**

  Unsubscribe all subscriptions

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
  <td rowspan="2">err_message</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from futu import *
import time
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

print('current subscription status :', quote_ctx.query_subscription()) # Query the initial subscription status
ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.QUOTE, SubType.TICKER], subscribe_push=False, session=Session.ALL)
# First subscribed to the two types of QUOTE and TICKER. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
    print('subscribe successfully! current subscription status :', quote_ctx.query_subscription()) # Query subscription status after successful subscription
    time.sleep(60) # You can unsubscribe at least 1 minute after subscribing
    ret_unsub, err_message_unsub = quote_ctx.unsubscribe_all() # Cancel all subscriptions
    if ret_unsub == RET_OK:
        print('unsubscribe all successfully! current subscription status:', quote_ctx.query_subscription()) # Query the subscription status after canceling the subscription
    else:
        print('Failed to cancel all subscriptions！', err_message_unsub)
else:
    print('subscription failed', err_message)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
current subscription status : (0, {'total_used': 0, 'remain': 1000, 'own_used': 0, 'sub_list': {}})
subscribe successfully！current subscription status : (0, {'total_used': 2, 'remain': 998, 'own_used': 2, 'sub_list': {'QUOTE': ['US.AAPL'], 'TICKER': ['US.AAPL']}})
unsubscribe all successfully！current subscription status: (0, {'total_used': 0, 'remain': 1000, 'own_used': 0, 'sub_list': {}})
```









## <a href="#3789" class="header-anchor">#</a> Qot_Sub.proto

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3001





## <a href="#4159" class="header-anchor">#</a> Sub

`uint Sub(QotSub.Request req);`  
`virtual void OnReply_Sub(FTAPI_Conn client, uint nSerialNo, QotSub.Response rsp);`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_Basic)
                .SetIsSubOrUnSub(true)
                .Build();
        QotSub.Request req = QotSub.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.Sub(req);
        Console.Write("Send QotSub: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_Sub(FTAPI_Conn client, uint nSerialNo, QotSub.Response rsp) {
        Console.Write("Reply: QotSub: {0}  {1}\n", nSerialNo, rsp.ToString());
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
Qot onInitConnect: ret=0 desc= connID=6819171983431767818
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0
```









## <a href="#4159-2" class="header-anchor">#</a> sub

`int sub(QotSub.Request req);`  
`void onReply_Sub(FTAPI_Conn client, int nSerialNo, QotSub.Response rsp);`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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
        QotSub.C2S c2s = QotSub.C2S.newBuilder()
                .addSecurityList(sec)
                .addSubTypeList(QotCommon.SubType.SubType_Basic_VALUE)
                .setIsSubOrUnSub(true)
                .build();
        QotSub.Request req = QotSub.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.sub(req);
        System.out.printf("Send QotSub: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_Sub(FTAPI_Conn client, int nSerialNo, QotSub.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotSub failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotSub: %s\n", json);
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
Send QotSub: 2
Receive QotSub: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0
}
```









## <a href="#4159-3" class="header-anchor">#</a> Sub

`Futu::u32_t Sub(const Qot_Sub::Request &stReq);`  
`virtual void OnReply_Sub(Futu::u32_t nSerialNo, const Qot_Sub::Response &stRsp) = 0;`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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

        // subscribe first
        Qot_Sub::Request req;
        Qot_Sub::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Basic);
        c2s->set_isregorunregpush(true);
        c2s->set_issuborunsub(true);

        m_SubSerialNo = m_pQotApi->Sub(req);
        cout << "Request Sub SerialNo: " << m_SubSerialNo << endl;
    }

    virtual void OnReply_Sub(Futu::u32_t nSerialNo, const Qot_Sub::Response &stRsp)
    {
        if(nSerialNo == m_SubSerialNo)
        {
            cout << "OnReply_Sub SerialNo: " << nSerialNo << endl;
            if(stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }        

            // construct request message
            Qot_GetBasicQot::Request req;
            Qot_GetBasicQot::C2S *c2s = req.mutable_c2s();
            auto secList = c2s->mutable_securitylist();
            Qot_Common::Security *sec = secList->Add();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

            m_GetBasicQotSerialNo = m_pQotApi->GetBasicQot(req);
            cout << "Request GetBasicQot SerialNo: " << m_GetBasicQotSerialNo << endl;
        }
    }

    virtual void OnReply_GetBasicQot(Futu::u32_t nSerialNo, const Qot_GetBasicQot::Response &stRsp){
        if(nSerialNo == m_GetBasicQotSerialNo)
        {
            cout << "OnReply_GetBasicQot SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_SubSerialNo;
    Futu::u32_t m_GetBasicQotSerialNo;
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
Request Sub SerialNo: 3
OnReply_Sub SerialNo: 3
Request GetBasicQot SerialNo: 4
OnReply_GetBasicQot SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "basicQotList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "isSuspended": false,
    "listTime": "2004-06-16",
    "priceSpread": 0.5,
    "updateTime": "2021-06-09 14:08:24",
    "highPrice": 606,
    "openPrice": 600,
    "lowPrice": 597.5,
    "curPrice": 601.5,
    "lastClosePrice": 601,
    "volume": "4283211",
    "turnover": 2579419163,
    "turnoverRate": 0.045,
    "amplitude": 1.414,
    "darkStatus": 0,
    "listTimestamp": 1087315200,
    "updateTimestamp": 1623218904,
    "secStatus": 1
   }
  ]
 }
}
```









## <a href="#4159-4" class="header-anchor">#</a> Sub

`Sub(req);`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";

function Sub(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'XXXXX'];
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
                subTypeList: [ SubType.SubType_OrderBook ], // Subscription OrderBook data
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true,
                },
            }; 

            websocket.Sub(req) //# Subscribe to the order type, OpenD starts to receive continuous push from the server
            .then((res) => { 
                let { errCode, retMsg, retType } = res
                console.log("subscribe: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("error:", error.retMsg);
                }
            });
        } else {
            console.log("error", msg);
        }
    };

    websocket.onPush = (cmd, res)=>{
        if(ftCmdID.QotUpdateOrderBook.cmd == cmd){
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("OrderBookTest", s2c);
            } else {
                console.log("OrderBookTest: error")
            }
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
subscribe: errCode 0, retMsg , retType 0
OrderBookTest {"security":{"market":1,"code":"00700"},"orderBookAskList":[{"price":492.6,"volume":"32300","orederCount":55},{"price":492.8,"volume":"14100","orederCount":16},{"price":493,"volume":"25200","orederCount":30},{"price":493.2,"volume":"12300","orederCount":11},{"price":493.4,"volume":"9000","orederCount":7},{"price":493.6,"volume":"13500","orederCount":10},{"price":493.8,"volume":"9800","orederCount":12},{"price":494,"volume":"10500","orederCount":18},{"price":494.2,"volume":"6100","orederCount":6},{"price":494.4,"volume":"11400","orederCount":5}],"orderBookBidList":[{"price":492.4,"volume":"30600","orederCount":59},{"price":492.2,"volume":"29800","orederCount":49},{"price":492,"volume":"97900","orederCount":120},{"price":491.8,"volume":"24700","orederCount":55},{"price":491.6,"volume":"35300","orederCount":50},{"price":491.4,"volume":"11200","orederCount":18},{"price":491.2,"volume":"29300","orederCount":39},{"price":491,"volume":"77900","orederCount":229},{"price":490.8,"volume":"14100","orederCount":39},{"price":490.6,"volume":"22800","orederCount":34}]}
OrderBookTest { ... }
...
...
stop
```











Interface Limitations

- Supports subscriptions of multiple real-time data types, refer to
  [SubType](/moomoo-api-doc/en/quote/quote.html#7721), each stock
  subscription for one one quota.
- Please refer to [Subscription Quota & Historical Candlestick
  Quota](/moomoo-api-doc/en/intro/authority.html#9123) for Subscription
  Quota rules.
- You can unsubscribe after subscribing after at least one minute.
- Due to the large amount of SF market data in Hong Kong stocks, in
  order to ensure the speed of the SF market and the processing
  performance of OpenD, currently SF authorized users are limited to
  subscribing to 50 security products (including hkex stocks, warrants,
  bulls and bears) at the same time, the remaining subscription quota
  can still be used to subscribe to other types, such as: tickers and
  brokerage etc.
- HK options and futures do not support subscription to *TICKER* type
  under LV1 authority.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#5009" class="header-anchor">#</a> subscribe

`subscribe(code_list, subtype_list, is_first_push=True, subscribe_push=True, is_detailed_orderbook=False, extended_time=False, session=Session.NONE)`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.  
  HK market (including underlying stocks, warrants, CBBCs, options,
  futures) subscriptions require LV1 and above permissions.
  Subscriptions are not supported under BMP permissions.  
  US market (including underlying stocks, ETFs) subscriptions for
  overnight quotes require LV1 and above permissions. Subscriptions are
  not supported under BMP permissions.

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
  <td style="text-align: left;">A list of stock codes that need to be
  subscribed.
  
    
  
  
   
  
  Data type of elements in the list is str.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">subtype_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">List of data types that need to be
  subscribed.
  
    
  
  
   
  
  Data type of elements in the list is <a
  href="/moomoo-api-doc/en/quote/quote.html#7721">SubType</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">is_first_push</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to push the cached data
  immediately after a successful subscription.
  
    
  
  
   
  
  <ul>
  <li>True: Push the cached data. When there is a disconnection and
  reconnection between scripts and OpenD, the last data before the
  disconnection will be pushed again if it is set to True when
  resubscribing.</li>
  <li>False: Do not push the cached data. Wait for the latest data to be
  pushed from moomoo server.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">subscribe_push</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to push data after subscription.
  
    
  
  
   
  
  After subscription, OpenD provides <a
  href="/moomoo-api-doc/en/qa/quote.html#5505">two methods to obtain
  data</a>. If you only use the method of <strong>Get Real-time
  Data</strong> , setting to False can save part of the performance cost.
  <ul>
  <li>True: Push data. It must be set to True if the <strong>Real-time
  data Callback</strong> method is used.</li>
  <li>False: Do not push data. It is recommended to set to False if
  <strong>only</strong> using the <strong>Get Real-time
  Data</strong>.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">is_detailed_orderbook</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to subscribe to the detailed order
  book.
  
    
  
  
   
  
  <ul>
  <li>Only for Hong Kong stocks ORDER_BOOK type under the authority of
  Hong Kong stocks SF market.</li>
  <li>Under the authority of US stocks &amp; futures LV2, the detailed
  order book is not provided.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">extended_time</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to allow pre-market and
  after-hours data of US stocks.
  
    
  
  
   
  
  Only used for subscribing to real-time candlestick and real-time Time
  Frame and real-time tick-by-tick of US stocks.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">session</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
  <td style="text-align: left;">US stocks quotes session
  
    
  
  
   
  
  <ul>
  <li>Only used for subscribing to real-time candlestick and real-time
  Time Frame and real-time tick-by-tick of US stocks.</li>
  <li>Please choose 'ALL' to subscribe 24H quotes for US stocks. The
  'OVERNIGHT' is not allowed.</li>
  <li>Minimum version requirements: 9.2.4207</li>
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
  <td rowspan="2">err_message</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
import time
from moomoo import *
class OrderBookTest(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s"% data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBookTest()
quote_ctx.set_handler(handler) # Set real-time swing callback
quote_ctx.subscribe(['US.AAPL'], [SubType.ORDER_BOOK]) # Subscribe to the order type, OpenD starts to receive continuous push from the server
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
OrderBookTest  {'code': 'US.AAPL', 'name': 'Apple', 'svr_recv_time_bid': '2025-04-07 05:00:52.266', 'svr_recv_time_ask': '2025-04-07 05:00:53.973', 'Bid': [(180.2, 15, 3, {}), (180.19, 1, 1, {}), (180.18, 11, 2, {}), (180.14, 200, 1, {}), (180.13, 3, 2, {}), (180.1, 99, 3, {}), (180.05, 3, 1, {}), (180.03, 400, 1, {}), (180.02, 10, 1, {}), (180.01, 100, 1, {}), (180.0, 441, 24, {})], 'Ask': [(180.3, 100, 1, {}), (180.38, 4, 2, {}), (180.4, 100, 1, {}), (180.42, 200, 1, {}), (180.46, 29, 1, {}), (180.5, 1019, 2, {}), (180.6, 1000, 1, {}), (180.8, 2001, 3, {}), (180.84, 15, 2, {}), (181.0, 2036, 4, {}), (181.2, 2000, 2, {}), (181.3, 3, 1, {}), (181.4, 2021, 3, {}), (181.5, 59, 2, {}), (181.79, 9, 1, {}), (181.8, 20, 1, {}), (181.9, 94, 4, {}), (181.98, 20, 1, {}), (182.0, 150, 7, {})]}
```





## <a href="#1052" class="header-anchor">#</a> unsubscribe

`unsubscribe(code_list, subtype_list, unsubscribe_all=False)`

- **Description**

  unsubscribe

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
  <td style="text-align: left;">A list of stock codes to unsubscribe.
  
    
  
  
   
  
  Data type of elements in the list is str.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">subtype_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">List of data types that need to be
  subscribed.
  
    
  
  
   
  
  Data type of elements in the list is <a
  href="/moomoo-api-doc/en/quote/quote.html#7721">SubType</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">unsubscribe_all</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Cancel all subscriptions.
  
    
  
  
   
  
  Ignore other parameters when it is True.
  
  
  
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
  <td rowspan="2">err_message</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from moomoo import *
import time
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

print('current subscription status :', quote_ctx.query_subscription()) # Query the initial subscription status
ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.QUOTE, SubType.TICKER], subscribe_push=False, session=Session.ALL)
# First subscribed to the two types of QUOTE and TICKER. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
    print('subscribe successfully! current subscription status :', quote_ctx.query_subscription()) # Query subscription status after successful subscription
    time.sleep(60) # You can unsubscribe at least 1 minute after subscribing
    ret_unsub, err_message_unsub = quote_ctx.unsubscribe(['US.AAPL'], [SubType.QUOTE])
    if ret_unsub == RET_OK:
        print('unsubscribe successfully! current subscription status:', quote_ctx.query_subscription()) # Query the subscription status after canceling the subscription
    else:
        print('unsubscription failed!', err_message_unsub)
else:
    print('subscription failed', err_message)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
current subscription status : (0, {'total_used': 0, 'remain': 1000, 'own_used': 0, 'sub_list': {}})
subscribe successfully！current subscription status : (0, {'total_used': 2, 'remain': 998, 'own_used': 2, 'sub_list': {'QUOTE': ['US.AAPL'], 'TICKER': ['US.AAPL']}})
unsubscribe successfully！current subscription status: (0, {'total_used': 1, 'remain': 999, 'own_used': 1, 'sub_list': {'TICKER': ['US.AAPL']}})
```





## <a href="#771" class="header-anchor">#</a> unsubscribe_all

`unsubscribe_all()`

- **Description**

  Unsubscribe all subscriptions

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
  <td rowspan="2">err_message</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from moomoo import *
import time
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

print('current subscription status :', quote_ctx.query_subscription()) # Query the initial subscription status
ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.QUOTE, SubType.TICKER], subscribe_push=False, session=Session.ALL)
# First subscribed to the two types of QUOTE and TICKER. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
    print('subscribe successfully! current subscription status :', quote_ctx.query_subscription()) # Query subscription status after successful subscription
    time.sleep(60) # You can unsubscribe at least 1 minute after subscribing
    ret_unsub, err_message_unsub = quote_ctx.unsubscribe_all() # Cancel all subscriptions
    if ret_unsub == RET_OK:
        print('unsubscribe all successfully! current subscription status:', quote_ctx.query_subscription()) # Query the subscription status after canceling the subscription
    else:
        print('Failed to cancel all subscriptions！', err_message_unsub)
else:
    print('subscription failed', err_message)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
current subscription status : (0, {'total_used': 0, 'remain': 1000, 'own_used': 0, 'sub_list': {}})
subscribe successfully！current subscription status : (0, {'total_used': 2, 'remain': 998, 'own_used': 2, 'sub_list': {'QUOTE': ['US.AAPL'], 'TICKER': ['US.AAPL']}})
unsubscribe all successfully！current subscription status: (0, {'total_used': 0, 'remain': 1000, 'own_used': 0, 'sub_list': {}})
```









## <a href="#3789-2" class="header-anchor">#</a> Qot_Sub.proto

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3001





## <a href="#4159-5" class="header-anchor">#</a> Sub

`uint Sub(QotSub.Request req);`  
`virtual void OnReply_Sub(MMAPI_Conn client, uint nSerialNo, QotSub.Response rsp);`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_Basic)
                .SetIsSubOrUnSub(true)
                .Build();
        QotSub.Request req = QotSub.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.Sub(req);
        Console.Write("Send QotSub: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_Sub(MMAPI_Conn client, uint nSerialNo, QotSub.Response rsp) {
        Console.Write("Reply: QotSub: {0}  {1}\n", nSerialNo, rsp.ToString());
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
Qot onInitConnect: ret=0 desc= connID=6819171983431767818
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0
```









## <a href="#4159-6" class="header-anchor">#</a> sub

`int sub(QotSub.Request req);`  
`void onReply_Sub(MMAPI_Conn client, int nSerialNo, QotSub.Response rsp);`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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
        QotSub.C2S c2s = QotSub.C2S.newBuilder()
                .addSecurityList(sec)
                .addSubTypeList(QotCommon.SubType.SubType_Basic_VALUE)
                .setIsSubOrUnSub(true)
                .build();
        QotSub.Request req = QotSub.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.sub(req);
        System.out.printf("Send QotSub: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_Sub(MMAPI_Conn client, int nSerialNo, QotSub.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotSub failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotSub: %s\n", json);
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
Send QotSub: 2
Receive QotSub: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0
}
```









## <a href="#4159-7" class="header-anchor">#</a> Sub

`moomoo::u32_t Sub(const Qot_Sub::Request &stReq);`  
`virtual void OnReply_Sub(moomoo::u32_t nSerialNo, const Qot_Sub::Response &stRsp) = 0;`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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

        // subscribe first
        Qot_Sub::Request req;
        Qot_Sub::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Basic);
        c2s->set_isregorunregpush(true);
        c2s->set_issuborunsub(true);

        m_SubSerialNo = m_pQotApi->Sub(req);
        cout << "Request Sub SerialNo: " << m_SubSerialNo << endl;
    }

    virtual void OnReply_Sub(moomoo::u32_t nSerialNo, const Qot_Sub::Response &stRsp)
    {
        if(nSerialNo == m_SubSerialNo)
        {
            cout << "OnReply_Sub SerialNo: " << nSerialNo << endl;
            if(stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }        

            // construct request message
            Qot_GetBasicQot::Request req;
            Qot_GetBasicQot::C2S *c2s = req.mutable_c2s();
            auto secList = c2s->mutable_securitylist();
            Qot_Common::Security *sec = secList->Add();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

            m_GetBasicQotSerialNo = m_pQotApi->GetBasicQot(req);
            cout << "Request GetBasicQot SerialNo: " << m_GetBasicQotSerialNo << endl;
        }
    }

    virtual void OnReply_GetBasicQot(moomoo::u32_t nSerialNo, const Qot_GetBasicQot::Response &stRsp){
        if(nSerialNo == m_GetBasicQotSerialNo)
        {
            cout << "OnReply_GetBasicQot SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_SubSerialNo;
    moomoo::u32_t m_GetBasicQotSerialNo;
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
Request Sub SerialNo: 3
OnReply_Sub SerialNo: 3
Request GetBasicQot SerialNo: 4
OnReply_GetBasicQot SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "basicQotList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "isSuspended": false,
    "listTime": "2004-06-16",
    "priceSpread": 0.5,
    "updateTime": "2021-06-09 14:08:24",
    "highPrice": 606,
    "openPrice": 600,
    "lowPrice": 597.5,
    "curPrice": 601.5,
    "lastClosePrice": 601,
    "volume": "4283211",
    "turnover": 2579419163,
    "turnoverRate": 0.045,
    "amplitude": 1.414,
    "darkStatus": 0,
    "listTimestamp": 1087315200,
    "updateTimestamp": 1623218904,
    "secStatus": 1
   }
  ]
 }
}
```









## <a href="#4159-8" class="header-anchor">#</a> Sub

`Sub(req);`

- **Description**

  To subscribe to the real-time information required for registration,
  specify the stock and subscription data types.

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; // List of security
    repeated int32 subTypeList = 2; //Qot_Common.SubType, list of subscription data type
    required bool isSubOrUnSub = 3; //true means subscribe, false means unsubscribe
    optional bool isRegOrUnRegPush = 4; //Whether to register or unregister the push of the market quotation above the link, this parameter does not specify that no registration or unregistration operation will be performed
    repeated int32 regPushRehabTypeList = 5; //Qot_Common.RehabType, the type of adjustment, it takes effect when registered push and candlestick type, other subscription types ignore this parameter. This parameter does not specify the default adjust forward when registering candlestick push
    optional bool isFirstPush = 6; //After registration, if the local data is the first push of the existing data, the default is true if this parameter is not specified
    optional bool isUnsubAll = 7; //One-click cancel all subscriptions currently connected, and ignore other parameters when it is set to True.
    optional bool isSubOrderBookDetail = 8; //Subscription display is available, whether to subscribe to display details, only supports SF market, the default is false if this parameter is not specified
    optional bool extendedTime = 9; // Whether to allow pre-market and after-hours data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
    optional int32 session = 10; // Whether to allow outside regular trading data of US stocks (only used to subscribe to real-time candlestick and real-time Time Frame of US stocks)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the subscription data type, refer to
>   [SubType](/moomoo-api-doc/en/quote/quote.html#7721)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)

- **Return**



``` protobuf

message S2C
{
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";

function Sub(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'XXXXX'];
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
                subTypeList: [ SubType.SubType_OrderBook ], // Subscription OrderBook data
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true,
                },
            }; 

            websocket.Sub(req) //# Subscribe to the order type, OpenD starts to receive continuous push from the server
            .then((res) => { 
                let { errCode, retMsg, retType } = res
                console.log("subscribe: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("error:", error.retMsg);
                }
            });
        } else {
            console.log("error", msg);
        }
    };

    websocket.onPush = (cmd, res)=>{
        if(mmCmdID.QotUpdateOrderBook.cmd == cmd){
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("OrderBookTest", s2c);
            } else {
                console.log("OrderBookTest: error")
            }
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
subscribe: errCode 0, retMsg , retType 0
OrderBookTest {"security":{"market":1,"code":"00700"},"orderBookAskList":[{"price":492.6,"volume":"32300","orederCount":55},{"price":492.8,"volume":"14100","orederCount":16},{"price":493,"volume":"25200","orederCount":30},{"price":493.2,"volume":"12300","orederCount":11},{"price":493.4,"volume":"9000","orederCount":7},{"price":493.6,"volume":"13500","orederCount":10},{"price":493.8,"volume":"9800","orederCount":12},{"price":494,"volume":"10500","orederCount":18},{"price":494.2,"volume":"6100","orederCount":6},{"price":494.4,"volume":"11400","orederCount":5}],"orderBookBidList":[{"price":492.4,"volume":"30600","orederCount":59},{"price":492.2,"volume":"29800","orederCount":49},{"price":492,"volume":"97900","orederCount":120},{"price":491.8,"volume":"24700","orederCount":55},{"price":491.6,"volume":"35300","orederCount":50},{"price":491.4,"volume":"11200","orederCount":18},{"price":491.2,"volume":"29300","orederCount":39},{"price":491,"volume":"77900","orederCount":229},{"price":490.8,"volume":"14100","orederCount":39},{"price":490.6,"volume":"22800","orederCount":34}]}
OrderBookTest { ... }
...
...
stop
```











Interface Limitations

- Supports subscriptions of multiple real-time data types, refer to
  [SubType](/moomoo-api-doc/en/quote/quote.html#7721), each stock
  subscription for one one quota.
- Please refer to [Subscription Quota & Historical Candlestick
  Quota](/moomoo-api-doc/en/intro/authority.html#9123) for Subscription
  Quota rules.
- You can unsubscribe after subscribing after at least one minute.
- Due to the large amount of SF market data in Hong Kong stocks, in
  order to ensure the speed of the SF market and the processing
  performance of OpenD, currently SF authorized users are restricted to
  subscribing to the order book and broker queue of only 50 securities
  products (including hkex stocks, warrants, bulls and bears) at the
  same time, the remaining subscription quota can still be used to
  subscribe to other types, such as: tickers and brokerage etc.
- HK options and futures do not support subscription to *TICKER* type
  under LV1 authority.













