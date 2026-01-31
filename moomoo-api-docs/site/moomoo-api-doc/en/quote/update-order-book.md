



# <a href="#5312" class="header-anchor">#</a> Real-time Order Book Callback









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks. It will call back to this
  function after receiving the push of real-time disk data. You need to
  override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdateOrderBook_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
    <li>&gt;Other quote rights does not support access to such details.</li>
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
import time
from futu import *
class OrderBookTest(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s" % data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBookTest()
quote_ctx.set_handler(handler) # Set real-time swing callback
ret, data = quote_ctx.subscribe(['US.AAPL'], [SubType.ORDER_BOOK]) # Subscribe to the order type, OpenD starts to receive continuous push from the server
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
OrderBookTest  {'code': 'US.AAPL', 'name': 'Apple', 'svr_recv_time_bid': '', 'svr_recv_time_ask': '', 'Bid': [(179.77, 100, 1, {}), (179.68, 200, 1, {}), (179.65, 2, 2, {}), (179.64, 27, 1, {}), (179.6, 9, 2, {}), (179.58, 39, 2, {}), (179.5, 13, 4, {}), (179.48, 331, 2, {}), (179.4, 1002, 2, {}), (179.38, 330, 1, {}), (179.37, 2, 1, {}), (179.3, 47, 1, {}), (179.28, 330, 1, {}), (179.21, 2, 1, {}), (179.2, 1000, 1, {}), (179.18, 330, 1, {}), (179.17, 100, 1, {}), (179.16, 1, 1, {}), (179.13, 400, 1, {}), (179.1, 3000, 1, {}), (179.08, 330, 1, {}), (179.05, 125, 2, {}), (179.01, 17, 2, {}), (179.0, 81, 7, {})], 'Ask': [(179.95, 400, 2, {}), (180.0, 360, 2, {}), (180.05, 20, 1, {}), (180.1, 246, 4, {}), (180.18, 20, 1, {}), (180.2, 2030, 3, {}), (180.23, 20, 1, {}), (180.3, 23, 1, {}), (180.33, 15, 1, {}), (180.4, 2000, 2, {}), (180.49, 5, 1, {}), (180.59, 253, 1, {}), (180.6, 2000, 2, {}), (180.8, 2010, 3, {}), (181.0, 2018, 4, {}), (181.08, 1, 1, {}), (181.2, 1009, 2, {}), (181.3, 17, 3, {}), (181.4, 1, 1, {}), (181.5, 50, 1, {}), (181.79, 9, 1, {}), (181.9, 66, 2, {})]}
```









## <a href="#4825" class="header-anchor">#</a> Qot_UpdateOrderBook.proto

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the Futu server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the Futu server received data from the exchange (for ask)
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





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3013





`virtual void OnReply_UpdateOrderBook(FTAPI_Conn client, QotUpdateOrderBook.Response rsp);`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the Futu server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the Futu server received data from the exchange (for ask)
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





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_OrderBook)
                .SetIsSubOrUnSub(true)
                .SetIsRegOrUnRegPush(true)
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
    
    public void OnReply_UpdateOrderBook(FTAPI_Conn client, uint nSerialNo, QotUpdateOrderBook.Response rsp) {
        Console.Write("Push: UpdateOrderBook: {0}\n", nSerialNo);
        Console.Write("price : {0}\n", rsp.S2C.OrderBookAskListList[0].Price);
        Console.Write("volume : {0}\n", rsp.S2C.OrderBookAskListList[0].Volume);        
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
Qot onInitConnect: ret=0 desc= connID=6825335709542277011
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Push: UpdateOrderBook: 1
price : 490
volume : 3228700
...
```









`void onPush_UpdateOrderBook(FTAPI_Conn client, QotUpdateOrderBook.Response rsp);`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the Futu server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the Futu server received data from the exchange (for ask)
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





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order book structure, refer to
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
                .setIsRegOrUnRegPush(true)
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

    @Override
    public void onPush_UpdateOrderBook(FTAPI_Conn client, QotUpdateOrderBook.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdateOrderBook failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdateOrderBook: %s\n", json);
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
Receive QotUpdateOrderBook: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "orderBookAskList": [{
      "price": 587.5,
      "volume": "200",
      "orederCount": 2
    }, ... {
      "price": 582.5,
      "volume": "2600",
      "orederCount": 13
    }],
    "svrRecvTimeBid": "2021-06-25 10:07:32.841",
    "svrRecvTimeBidTimestamp": 1.624586852841E9,
    "svrRecvTimeAsk": "2021-06-25 10:07:32.841",
    "svrRecvTimeAskTimestamp": 1.624586852841E9
  }
}
Receive QotUpdateOrderBook: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "orderBookAskList": [{
      "price": 587.5,
      "volume": "200",
      "orederCount": 2
    }, ... {
      "price": 582.5,
      "volume": "2600",
      "orederCount": 13
    }],
    "svrRecvTimeBid": "2021-06-25 10:07:32.941",
    "svrRecvTimeBidTimestamp": 1.624586852941E9,
    "svrRecvTimeAsk": "2021-06-25 10:07:32.941",
    "svrRecvTimeAskTimestamp": 1.624586852941E9
  }
}
```









`virtual void OnPush_UpdateOrderBook(const Qot_UpdateOrderBook::Response &stRsp) = 0;`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the Futu server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the Futu server received data from the exchange (for ask)
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





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order book structure, refer to
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
        }
    }

    virtual void OnPush_UpdateOrderBook(const Qot_UpdateOrderBook::Response &stRsp) {
        cout << "OnPush_UpdateOrderBook: " << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    FTAPI_Qot *m_pQotApi;
    
    Futu::u32_t m_SubSerialNo;
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
OnPush_UpdateOrderBook: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "orderBookAskList": [
   {
    "price": 603,
    "volume": "17900",
    "orederCount": 25
   },
...
   {
    "price": 607.5,
    "volume": "17100",
    "orederCount": 24
   }
  ],
  "orderBookBidList": [
   {
    "price": 602.5,
    "volume": "24500",
    "orederCount": 16
   },
...
   {
    "price": 598,
    "volume": "94600",
    "orederCount": 387
   }
  ],
  "svrRecvTimeBid": "2021-06-09 15:40:01.825",
  "svrRecvTimeBidTimestamp": 1623224401.825,
  "svrRecvTimeAsk": "2021-06-09 15:40:01.825",
  "svrRecvTimeAskTimestamp": 1623224401.825
 }
}
```









`OnPush(cmd,res)`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the Futu server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the Futu server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the Futu server received data from the exchange (for ask)
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





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";

function UpdateOrderBook(){
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
                subTypeList: [ SubType.SubType_OrderBook ], // Subscribe to the order type
                isSubOrUnSub: true,
                isRegOrUnRegPush: true,
                },
            };

            websocket.Sub(req) // Subscribe to the order type, OpenD starts to receive continuous push from the server
            .then((res) => { })
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
        if(ftCmdID.QotUpdateOrderBook.cmd == cmd){ // OrderBookTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("OrderBookTest", JSON.stringify(s2c));
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
OrderBookTest {"security":{"market":1,"code":"00700"},"orderBookAskList":[{"price":480.4,"volume":"700","orederCount":2},{"price":480.6,"volume":"385900","orederCount":14},{"price":480.8,"volume":"4200","orederCount":3},{"price":481,"volume":"15000","orederCount":14},{"price":481.2,"volume":"4600","orederCount":5},{"price":481.4,"volume":"13400","orederCount":4},{"price":481.6,"volume":"1800","orederCount":6},{"price":481.8,"volume":"3000","orederCount":8},{"price":482,"volume":"23700","orederCount":25},{"price":482.2,"volume":"1200","orederCount":3}],"orderBookBidList":[{"price":480,"volume":"55300","orederCount":39},{"price":479.8,"volume":"92400","orederCount":61},{"price":479.6,"volume":"106100","orederCount":41},{"price":479.4,"volume":"85900","orederCount":48},{"price":479.2,"volume":"78100","orederCount":34},{"price":479,"volume":"50200","orederCount":150},{"price":478.8,"volume":"51300","orederCount":44},{"price":478.6,"volume":"92700","orederCount":33},{"price":478.4,"volume":"5400","orederCount":16},{"price":478.2,"volume":"102500","orederCount":66}]}
OrderBookTest { ... }
 ...
 ...
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Real-time
  Orderbook](/moomoo-api-doc/en/quote/get-order-book.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).
- Real-time order book callback for US stocks, will continuously update
  data during the current trading session, with no need to set the
  session parameter.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks. It will call back to this
  function after receiving the push of real-time disk data. You need to
  override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdateOrderBook_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
import time
from moomoo import *
class OrderBookTest(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s" % data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBookTest()
quote_ctx.set_handler(handler) # Set real-time swing callback
ret, data = quote_ctx.subscribe(['US.AAPL'], [SubType.ORDER_BOOK]) # Subscribe to the order type, OpenD starts to receive continuous push from the server
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
OrderBookTest  {'code': 'US.AAPL', 'name': 'Apple', 'svr_recv_time_bid': '', 'svr_recv_time_ask': '', 'Bid': [(179.77, 100, 1, {}), (179.68, 200, 1, {}), (179.65, 2, 2, {}), (179.64, 27, 1, {}), (179.6, 9, 2, {}), (179.58, 39, 2, {}), (179.5, 13, 4, {}), (179.48, 331, 2, {}), (179.4, 1002, 2, {}), (179.38, 330, 1, {}), (179.37, 2, 1, {}), (179.3, 47, 1, {}), (179.28, 330, 1, {}), (179.21, 2, 1, {}), (179.2, 1000, 1, {}), (179.18, 330, 1, {}), (179.17, 100, 1, {}), (179.16, 1, 1, {}), (179.13, 400, 1, {}), (179.1, 3000, 1, {}), (179.08, 330, 1, {}), (179.05, 125, 2, {}), (179.01, 17, 2, {}), (179.0, 81, 7, {})], 'Ask': [(179.95, 400, 2, {}), (180.0, 360, 2, {}), (180.05, 20, 1, {}), (180.1, 246, 4, {}), (180.18, 20, 1, {}), (180.2, 2030, 3, {}), (180.23, 20, 1, {}), (180.3, 23, 1, {}), (180.33, 15, 1, {}), (180.4, 2000, 2, {}), (180.49, 5, 1, {}), (180.59, 253, 1, {}), (180.6, 2000, 2, {}), (180.8, 2010, 3, {}), (181.0, 2018, 4, {}), (181.08, 1, 1, {}), (181.2, 1009, 2, {}), (181.3, 17, 3, {}), (181.4, 1, 1, {}), (181.5, 50, 1, {}), (181.79, 9, 1, {}), (181.9, 66, 2, {})]}
```









## <a href="#4825-2" class="header-anchor">#</a> Qot_UpdateOrderBook.proto

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the moomoo server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the moomoo server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the moomoo server received data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the moomoo server from the exchange (for ask)
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
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3013





`virtual void OnReply_UpdateOrderBook(MMAPI_Conn client, QotUpdateOrderBook.Response rsp);`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the moomoo server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the moomoo server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the moomoo server received data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the moomoo server from the exchange (for ask)
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
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_OrderBook)
                .SetIsSubOrUnSub(true)
                .SetIsRegOrUnRegPush(true)
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
    
    public void OnReply_UpdateOrderBook(MMAPI_Conn client, uint nSerialNo, QotUpdateOrderBook.Response rsp) {
        Console.Write("Push: UpdateOrderBook: {0}\n", nSerialNo);
        Console.Write("price : {0}\n", rsp.S2C.OrderBookAskListList[0].Price);
        Console.Write("volume : {0}\n", rsp.S2C.OrderBookAskListList[0].Volume);        
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
Qot onInitConnect: ret=0 desc= connID=6825335709542277011
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Push: UpdateOrderBook: 1
price : 490
volume : 3228700
...
```









`void onPush_UpdateOrderBook(MMAPI_Conn client, QotUpdateOrderBook.Response rsp);`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the moomoo server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the moomoo server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the moomoo server received data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the moomoo server from the exchange (for ask)
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
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
                .addSubTypeList(QotCommon.SubType.SubType_OrderBook_VALUE)
                .setIsSubOrUnSub(true)
                .setIsRegOrUnRegPush(true)
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

    @Override
    public void onPush_UpdateOrderBook(MMAPI_Conn client, QotUpdateOrderBook.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdateOrderBook failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdateOrderBook: %s\n", json);
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
Receive QotUpdateOrderBook: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "orderBookAskList": [{
      "price": 587.5,
      "volume": "200",
      "orederCount": 2
    }, ... {
      "price": 582.5,
      "volume": "2600",
      "orederCount": 13
    }],
    "svrRecvTimeBid": "2021-06-25 10:07:32.841",
    "svrRecvTimeBidTimestamp": 1.624586852841E9,
    "svrRecvTimeAsk": "2021-06-25 10:07:32.841",
    "svrRecvTimeAskTimestamp": 1.624586852841E9
  }
}
Receive QotUpdateOrderBook: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "orderBookAskList": [{
      "price": 587.5,
      "volume": "200",
      "orederCount": 2
    }, ... {
      "price": 582.5,
      "volume": "2600",
      "orederCount": 13
    }],
    "svrRecvTimeBid": "2021-06-25 10:07:32.941",
    "svrRecvTimeBidTimestamp": 1.624586852941E9,
    "svrRecvTimeAsk": "2021-06-25 10:07:32.941",
    "svrRecvTimeAskTimestamp": 1.624586852941E9
  }
}
```









`virtual void OnPush_UpdateOrderBook(const Qot_UpdateOrderBook::Response &stRsp) = 0;`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the moomoo server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the moomoo server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the moomoo server received data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the moomoo server from the exchange (for ask)
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
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_OrderBook);
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
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }
        }
    }

    virtual void OnPush_UpdateOrderBook(const Qot_UpdateOrderBook::Response &stRsp) {
        cout << "OnPush_UpdateOrderBook: " << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    MMAPI_Qot *m_pQotApi;
    
    moomoo::u32_t m_SubSerialNo;
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
OnPush_UpdateOrderBook: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "orderBookAskList": [
   {
    "price": 603,
    "volume": "17900",
    "orederCount": 25
   },
...
   {
    "price": 607.5,
    "volume": "17100",
    "orederCount": 24
   }
  ],
  "orderBookBidList": [
   {
    "price": 602.5,
    "volume": "24500",
    "orederCount": 16
   },
...
   {
    "price": 598,
    "volume": "94600",
    "orederCount": 387
   }
  ],
  "svrRecvTimeBid": "2021-06-09 15:40:01.825",
  "svrRecvTimeBidTimestamp": 1623224401.825,
  "svrRecvTimeAsk": "2021-06-09 15:40:01.825",
  "svrRecvTimeAskTimestamp": 1623224401.825
 }
}
```









`OnPush(cmd,res)`

- **Description**

  Real-time quotation callback, asynchronous processing of real-time
  quotation push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 8; //Stock name
    repeated Qot_Common.OrderBook orderBookAskList = 2; //Ask order list
    repeated Qot_Common.OrderBook orderBookBidList = 3; //Bid order list
    optional string svrRecvTimeBid = 4; // The time when the moomoo server receives data from the exchange (for bid) The receiving time of part of the data is zero, such as server restart or cached data pushed for the first time. This field only supports Hong Kong stocks for the time being.
    optional double svrRecvTimeBidTimestamp = 5; // The timestamp of the data received by the moomoo server from the exchange (for bid)
    optional string svrRecvTimeAsk = 6; // The time when the moomoo server received data from the exchange (for ask)
    optional double svrRecvTimeAskTimestamp = 7; // The timestamp of the data received by the moomoo server from the exchange (for ask)
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
> - For order book structure, refer to
>   [OrderBook](/moomoo-api-doc/en/quote/quote.html#3557)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";

function UpdateOrderBook(){
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
                subTypeList: [ SubType.SubType_OrderBook ], // Subscribe to the order type
                isSubOrUnSub: true,
                isRegOrUnRegPush: true,
                },
            };

            websocket.Sub(req) // Subscribe to the order type, OpenD starts to receive continuous push from the server
            .then((res) => { })
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
        if(mmCmdID.QotUpdateOrderBook.cmd == cmd){ // OrderBookTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("OrderBookTest", JSON.stringify(s2c));
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
OrderBookTest {"security":{"market":1,"code":"00700"},"orderBookAskList":[{"price":480.4,"volume":"700","orederCount":2},{"price":480.6,"volume":"385900","orederCount":14},{"price":480.8,"volume":"4200","orederCount":3},{"price":481,"volume":"15000","orederCount":14},{"price":481.2,"volume":"4600","orederCount":5},{"price":481.4,"volume":"13400","orederCount":4},{"price":481.6,"volume":"1800","orederCount":6},{"price":481.8,"volume":"3000","orederCount":8},{"price":482,"volume":"23700","orederCount":25},{"price":482.2,"volume":"1200","orederCount":3}],"orderBookBidList":[{"price":480,"volume":"55300","orederCount":39},{"price":479.8,"volume":"92400","orederCount":61},{"price":479.6,"volume":"106100","orederCount":41},{"price":479.4,"volume":"85900","orederCount":48},{"price":479.2,"volume":"78100","orederCount":34},{"price":479,"volume":"50200","orederCount":150},{"price":478.8,"volume":"51300","orederCount":44},{"price":478.6,"volume":"92700","orederCount":33},{"price":478.4,"volume":"5400","orederCount":16},{"price":478.2,"volume":"102500","orederCount":66}]}
OrderBookTest { ... }
 ...
 ...
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Real-time
  Orderbook](/moomoo-api-doc/en/quote/get-order-book.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).
- Real-time order book callback for US stocks, will continuously update
  data during the current trading session, with no need to set the
  session parameter.













