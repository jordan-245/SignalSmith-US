



# <a href="#775" class="header-anchor">#</a> Get Real-time Order Book









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_order_book(code, num=10)`

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

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
  <td style="text-align: left;">Stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">name</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Stock name.</td>
  </tr>
  <tr>
  <td style="text-align: left;">num</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The requested number of price levels.
  
    
  
  
   
  
  For the upper limit of the number of price levels, please refer to <a
  href="/moomoo-api-doc/en/qa/quote.html#2126">Details of price
  levels</a>.
  
  
  
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
  <td>dict</td>
  <td>If ret == RET_OK, plate data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Order Book format as follows：

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
    <td style="text-align: left;">svr_recv_time_bid</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The time when Futu server receives order
    book of bid from the exchange.
    
      
    
    
     
    
    Sometimes the time is zero, e.g. server reboot or first push of cached
    data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">svr_recv_time_ask</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The time when Futu server receives order
    book of ask from the exchange.
    
      
    
    
     
    
    Sometimes the time is zero, e.g. server reboot or first push of cached
    data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">Bid</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Each tuple contains the following
    information：Bid price, bid volume, order qty of bid, order details of
    bid.
    
      
    
    
     
    
    Order details of ask
    <ul>
    <li>Details: Exchange order ID. Order volume.</li>
    <li>Up to 1000 order details of ask with HK SF market quotes.</li>
    <li>Other quote rights does not support access to such details.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">Ask</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Each tuple contains the following
    information：Ask price, ask volume, order qty of ask, order details of
    ask.
    
      
    
    
     
    
    Order details of ask
    <ul>
    <li>Details: Exchange order ID. Order volume.</li>
    <li>Up to 1000 order details of ask with HK SF market quotes.</li>
    <li>Other quote rights does not support access to such details.</li>
    </ul>
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    The format of Bid and Ask fields as follows：

    

        'Bid': [ (bid_price1, bid_volume1, order_num, {'orderid1': order_volume1, 'orderid2': order_volume2, …… }), (bid_price2, bid_volume2, order_num,  {'orderid1': order_volume1, 'orderid2': order_volume2, …… }),…]
        'Ask': [ (ask_price1, ask_volume1，order_num, {'orderid1': order_volume1, 'orderid2': order_volume2, …… }), (ask_price2, ask_volume2, order_num, {'orderid1': order_volume1, 'orderid2': order_volume2, …… }),…] 

    

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub = quote_ctx.subscribe(['US.AAPL'], [SubType.ORDER_BOOK], subscribe_push=False)[0]
# First subscribe to the order type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK:  # Successfully subscribed
    ret, data = quote_ctx.get_order_book('US.AAPL', num=3)  # Get 3 files of real-time panning data once
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
else:
    print('subscription failed')
quote_ctx.close()  # Close the current connection, OpenD will automatically cancel the subscription of the corresponding stock in 1 minute
```





- **Output**



``` python
{'code': 'US.AAPL', 'name': 'APPLE', 'svr_recv_time_bid': '2025-04-07 05:39:20.352', 'svr_recv_time_ask': '2025-04-07 05:39:20.352', 'Bid': [(181.17, 227, 2, {}), (181.15, 2, 2, {}), (181.12, 100, 1, {})], 'Ask': [(181.71, 200, 1, {}), (181.79, 9, 1, {}), (181.9, 616, 3, {})]}
```









## <a href="#2297" class="header-anchor">#</a> Qot_GetOrderBook.proto

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    required int32 num = 2; //Number of requested order book
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //List of buy orders
    repeated Qot_Common.OrderBook orderBookBidList = 3; //List of sell orders
    optional string svrRecvTimeBid = 4; // The time when Futu server receives data from the exchange (for bid). The receiving time of some data is zero, such as server restart or cached data pushed for the first time. This field currently supports Hong Kong stocks only.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when Futu server receives data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the Futu server from the exchange (for ask)
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order structure, please refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3012





`uint GetOrderBook(QotGetOrderBook.Request req);`  
`virtual void OnReply_GetOrderBook(FTAPI_Conn client, uint nSerialNo, QotGetOrderBook.Response rsp);`

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    required int32 num = 2; //Number of requested order book
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //List of buy orders
    repeated Qot_Common.OrderBook orderBookBidList = 3; //List of sell orders
    optional string svrRecvTimeBid = 4; // The time when Futu server receives data from the exchange (for bid). The receiving time of some data is zero, such as server restart or cached data pushed for the first time. This field currently supports Hong Kong stocks only.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when Futu server receives data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the Futu server from the exchange (for ask)
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order structure, please refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_OrderBook)
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

        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
            return;

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetOrderBook.C2S c2s = QotGetOrderBook.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetNum(10)
                .Build();
        QotGetOrderBook.Request req = QotGetOrderBook.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetOrderBook(req);
        Console.Write("Send QotGetOrderBook: {0}\n", seqNo);
    }

    public void OnReply_GetOrderBook(FTAPI_Conn client, uint nSerialNo, QotGetOrderBook.Response rsp)
    {
        Console.Write("Reply: QotGetOrderBook: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.OrderBookAskListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825669765086569309
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetOrderBook: 4
Reply: QotGetOrderBook: 4
price: 457
```









`int getOrderBook(QotGetOrderBook.Request req);`  
`void onReply_GetOrderBook(FTAPI_Conn client, int nSerialNo, QotGetOrderBook.Response rsp);`

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    required int32 num = 2; //Number of requested order book
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //List of buy orders
    repeated Qot_Common.OrderBook orderBookBidList = 3; //List of sell orders
    optional string svrRecvTimeBid = 4; // The time when Futu server receives data from the exchange (for bid). The receiving time of some data is zero, such as server restart or cached data pushed for the first time. This field currently supports Hong Kong stocks only.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when Futu server receives data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the Futu server from the exchange (for ask)
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order structure, please refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
                .addSubTypeList(QotCommon.SubType.SubType_OrderBook_VALUE)
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
        System.out.printf("Reply: QotSub: %d  %s\n", nSerialNo, rsp.toString());

        if (rsp.getRetType() != Common.RetType.RetType_Succeed_VALUE)
            return;

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetOrderBook.C2S c2s = QotGetOrderBook.C2S.newBuilder()
                .setSecurity(sec)
                .setNum(10)
                .build();
        QotGetOrderBook.Request req = QotGetOrderBook.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getOrderBook(req);
        System.out.printf("Send QotGetOrderBook: %d\n", seqNo);
    }

    @Override
    public void onReply_GetOrderBook(FTAPI_Conn client, int nSerialNo, QotGetOrderBook.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetOrderBook failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetOrderBook: %s\n", json);
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
Send QotGetOrderBook: 3
Receive QotGetOrderBook: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "orderBookAskList": [{
      "price": 583.5,
      "volume": "142300",
      "orederCount": 25
    }, {
      "price": 584.0,
      "volume": "56600",
      "orederCount": 45
    }, ... {
      "price": 578.5,
      "volume": "61300",
      "orederCount": 27
    }]
  }
}
```









`Futu::u32_t GetOrderBook(const Qot_GetOrderBook::Request &stReq);`  
`virtual void OnReply_GetOrderBook(Futu::u32_t nSerialNo, const Qot_GetOrderBook::Response &stRsp) = 0;`

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    required int32 num = 2; //Number of requested order book
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //List of buy orders
    repeated Qot_Common.OrderBook orderBookBidList = 3; //List of sell orders
    optional string svrRecvTimeBid = 4; // The time when Futu server receives data from the exchange (for bid). The receiving time of some data is zero, such as server restart or cached data pushed for the first time. This field currently supports Hong Kong stocks only.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when Futu server receives data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the Futu server from the exchange (for ask)
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order structure, please refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_OrderBook);
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
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }

            // construct request message
            Qot_GetOrderBook::Request req;
            Qot_GetOrderBook::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            c2s->set_num(5);

            m_GetOrderBookSerialNo = m_pQotApi->GetOrderBook(req);
            cout << "Request GetOrderBook SerialNo: " << m_GetOrderBookSerialNo << endl;
        }
    }

    virtual void OnReply_GetOrderBook(Futu::u32_t nSerialNo, const Qot_GetOrderBook::Response &stRsp){
        if(nSerialNo == m_GetOrderBookSerialNo)
        {
            cout << "OnReply_GetOrderBook SerialNo: " << nSerialNo << endl; 
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
    Futu::u32_t m_GetOrderBookSerialNo;
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
Request GetOrderBook SerialNo: 4
OnReply_GetOrderBook SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "orderBookAskList": [
   {
    "price": 601,
    "volume": "20400",
    "orederCount": 27
   },
   {
    "price": 601.5,
    "volume": "15300",
    "orederCount": 27
   },
   {
    "price": 602,
    "volume": "28000",
    "orederCount": 22
   },
   {
    "price": 602.5,
    "volume": "10000",
    "orederCount": 15
   },
   {
    "price": 603,
    "volume": "14300",
    "orederCount": 23
   }
  ],
  "orderBookBidList": [
   {
    "price": 600.5,
    "volume": "600",
    "orederCount": 1
   },
   {
    "price": 600,
    "volume": "93500",
    "orederCount": 290
   },
   {
    "price": 599.5,
    "volume": "15300",
    "orederCount": 29
   },
   {
    "price": 599,
    "volume": "36000",
    "orederCount": 79
   },
   {
    "price": 598.5,
    "volume": "24700",
    "orederCount": 59
   }
  ]
 }
}
```









`GetOrderBook(req);`

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    required int32 num = 2; //Number of requested order book
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //List of buy orders
    repeated Qot_Common.OrderBook orderBookBidList = 3; //List of sell orders
    optional string svrRecvTimeBid = 4; // The time when Futu server receives data from the exchange (for bid). The receiving time of some data is zero, such as server restart or cached data pushed for the first time. This field currently supports Hong Kong stocks only.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when Futu server receives data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the Futu server from the exchange (for ask)
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order structure, please refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetOrderBook(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) {
            websocket.Sub({
                c2s: {
                securityList: [
                    {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                ],
                subTypeList: [ SubType.SubType_OrderBook ], 
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                        security: {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                        num: 2,
                    },
                };
                websocket.GetOrderBook(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("OrderBook: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                    if(retType == RetType.RetType_Succeed){
                        let data = beautify(JSON.stringify(s2c), {
                            indent_size: 2,
                            space_in_empty_paren: true,
                        });
                        console.log(data);
                    }
                })
                .catch((error) => {
                    console.log("getorderbook error:", error);
                });

            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("sub error:", error.retMsg);
                }
            });
        } else {
            console.log("start error", msg);
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
OrderBook: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "orderBookAskList": [{
    "price": 480.4,
    "volume": "700",
    "orederCount": 2
  }, {
    "price": 480.6,
    "volume": "385900",
    "orederCount": 14
  }],
  "orderBookBidList": [{
    "price": 480,
    "volume": "55300",
    "orederCount": 39
  }, {
    "price": 479.8,
    "volume": "92400",
    "orederCount": 61
  }]
}
stop
```











Interface Limitations

- The time field in which the Futu server receives data from the
  exchange. Only supports A-share Market stocks, HK stocks, ETFs,
  warrants, bulls and bears, and this data is only available at the
  opening time.
- The time field in which the Futu server receives data from the
  exchange. The receiving time of some data is zero, such as server
  restart or cached data pushed for the first time.





Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time OrderBook
  Callback](/moomoo-api-doc/en/quote/update-order-book.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).
- The real-time order book data will be returned during the current
  trading session for US stocks, with no need to set the session
  parameter.







`get_order_book(code, num=10)`

- **Description**

  To get the real-time order book of subscribed stocks, you must
  subscribe first.

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
  <td style="text-align: left;">Stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">name</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Stock name.</td>
  </tr>
  <tr>
  <td style="text-align: left;">num</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The requested number of price levels.
  
    
  
  
   
  
  For the upper limit of the number of price levels, please refer to <a
  href="/moomoo-api-doc/en/qa/quote.html#2126">Details of price
  levels</a>.
  
  
  
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
  <td>dict</td>
  <td>If ret == RET_OK, plate data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Order Book format as follows：

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
    <td style="text-align: left;">svr_recv_time_bid</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The time when moomoo server receives order
    book of bid from the exchange.
    
      
    
    
     
    
    Sometimes the time is zero, e.g. server reboot or first push of cached
    data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">svr_recv_time_ask</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The time when moomoo server receives order
    book of ask from the exchange.
    
      
    
    
     
    
    Sometimes the time is zero, e.g. server reboot or first push of cached
    data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">Bid</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Each tuple contains the following
    information：Bid price, bid volume, order qty of bid, order details of
    bid.
    
      
    
    
     
    
    Order details of ask
    <ul>
    <li>Details: Exchange order ID. Order volume.</li>
    <li>Up to 1000 order details of ask with HK SF market quotes.</li>
    <li>Other quote rights does not support access to such details.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">Ask</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Each tuple contains the following
    information：Ask price, ask volume, order qty of ask, order details of
    ask.
    
      
    
    
     
    
    Order details of ask
    <ul>
    <li>Details: Exchange order ID. Order volume.</li>
    <li>Up to 1000 order details of ask with HK SF market quotes.</li>
    <li>Other quote rights does not support access to such details.</li>
    </ul>
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    The format of Bid and Ask fields as follows：

    

        'Bid': [ (bid_price1, bid_volume1, order_num, {'orderid1': order_volume1, 'orderid2': order_volume2, …… }), (bid_price2, bid_volume2, order_num,  {'orderid1': order_volume1, 'orderid2': order_volume2, …… }),…]
        'Ask': [ (ask_price1, ask_volume1，order_num, {'orderid1': order_volume1, 'orderid2': order_volume2, …… }), (ask_price2, ask_volume2, order_num, {'orderid1': order_volume1, 'orderid2': order_volume2, …… }),…] 

    

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub = quote_ctx.subscribe(['US.AAPL'], [SubType.ORDER_BOOK], subscribe_push=False)[0]
# First subscribe to the order type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK:  # Successfully subscribed
    ret, data = quote_ctx.get_order_book('US.AAPL', num=3)  # Get 3 files of real-time panning data once
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
else:
    print('subscription failed')
quote_ctx.close()  # Close the current connection, OpenD will automatically cancel the subscription of the corresponding stock in 1 minute
```





- **Output**



``` python
{'code': 'US.AAPL', 'name': 'APPLE', 'svr_recv_time_bid': '2025-04-07 05:39:20.352', 'svr_recv_time_ask': '2025-04-07 05:39:20.352', 'Bid': [(181.17, 227, 2, {}), (181.15, 2, 2, {}), (181.12, 100, 1, {})], 'Ask': [(181.71, 200, 1, {}), (181.79, 9, 1, {}), (181.9, 616, 3, {})]}
```















