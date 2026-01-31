



# <a href="#2943" class="header-anchor">#</a> Get Real-time Broker Queue











- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#2943-2" class="header-anchor">#</a> Get Real-time Broker Queue

`get_broker_queue(code)`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**

  | Parameter | Type | Description |
  |:----------|:-----|:------------|
  | code      | str  | Stock code. |

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
  <td rowspan="2">bid_frame_table</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, queue of bid brokers is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  <tr>
  <td rowspan="2">ask_frame_table</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, queue of ask brokers is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Queue of bid brokers format as follows:
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
    <td style="text-align: left;">bid_broker_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Bid broker ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_broker_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Bid broker name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_broker_pos</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Broker level.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Exchange order ID.
    
      
    
    
     
    
    <ul>
    <li>Not the order ID returned by the order interface.</li>
    <li>Only HK SF market quotes support returning this field.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">order_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Order volume.
    
      
    
    
     
    
    Only HK SF market quotes support returning this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>
  - Queue of ask brokers format as follows:
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
    <td style="text-align: left;">ask_broker_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Ask Broker ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_broker_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Ask Broker name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_broker_pos</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Broker level.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Exchange order ID.
    
      
    
    
     
    
    <ul>
    <li>Not the order ID returned by the order interface.</li>
    <li>Only HK SF market quotes support returning this field.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">order_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Order volume.
    
      
    
    
     
    
    Only HK SF market quotes support returning this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub, err_message = quote_ctx.subscribe(['HK.00700'], [SubType.BROKER], subscribe_push=False)
# First subscribe to the broker queue type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push the data to the script temporarily
if ret_sub == RET_OK: # Subscription successful
     ret, bid_frame_table, ask_frame_table = quote_ctx.get_broker_queue('HK.00700') # Get a broker queue data
     if ret == RET_OK:
         print(bid_frame_table)
     else:
         print('error:', bid_frame_table)
else:
     print(err_message)
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
    code     name  bid_broker_id                                    bid_broker_name  bid_broker_pos order_id order_volume
0   HK.00700  TENCENT           5338            J.P. Morgan Broking (Hong Kong) Limited               1      N/A          N/A
..       ...      ...            ...                                                ...             ...      ...          ...
36  HK.00700  TENCENT           8305  Futu Securities International (Hong Kong) Limited               4      N/A          N/A

[37 rows x 7 columns]
```









## <a href="#2229" class="header-anchor">#</a> Qot_GetBroker.proto

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3014





## <a href="#1532" class="header-anchor">#</a> GetBroker

`uint GetBroker(QotGetBroker.Request req);`  
`virtual void OnReply_GetBroker(FTAPI_Conn client, uint nSerialNo, QotGetBroker.Response rsp);`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Broker)
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
        QotGetBroker.C2S c2s = QotGetBroker.C2S.CreateBuilder()
                .SetSecurity(sec)
                .Build();
        QotGetBroker.Request req = QotGetBroker.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetBroker(req);
        Console.Write("Send QotGetBroker: {0}\n", seqNo);
    }

    public void OnReply_GetBroker(FTAPI_Conn client, uint nSerialNo, QotGetBroker.Response rsp)
    {
        Console.Write("Reply: QotGetBroker: {0}\n", nSerialNo);
        Console.Write("id: {0}, name: {1}\n", rsp.S2C.BrokerAskListList[0].Id, rsp.S2C.BrokerAskListList[0].Name);
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
Qot onInitConnect: ret=0 desc= connID=6825676366648053042
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetBroker: 4
Reply: QotGetBroker: 4
id: 5465, name: Futu Securities International (Hong Kong) Limited
```









## <a href="#1532-2" class="header-anchor">#</a> getBroker

`int getBroker(QotGetBroker.Request req);`  
`void onReply_GetBroker(FTAPI_Conn client, int nSerialNo, QotGetBroker.Response rsp);`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1);  //Set client information
        qot.setConnSpi(this);  //Set connection callback
        qot.setQotSpi(this);   //Set transaction callback
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
                .addSubTypeList(QotCommon.SubType.SubType_Broker_VALUE)
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
        QotGetBroker.C2S c2s = QotGetBroker.C2S.newBuilder()
                .setSecurity(sec)
                .build();
        QotGetBroker.Request req = QotGetBroker.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getBroker(req);
        System.out.printf("Send QotGetBroker: %d\n", seqNo);
    }

    @Override
    public void onReply_GetBroker(FTAPI_Conn client, int nSerialNo, QotGetBroker.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetBroker failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetBroker: %s\n", json);
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
Send QotGetBroker: 3
Receive QotGetBroker: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "brokerAskList": [{
      "id": "3440",
      "name": "Goldman Sachs (Asia) Securities Limited",
      "pos": 1
    }, ... {
      "id": "141",
      "name": "Haitong International Securities Company Limited",
      "pos": 1
    }],
    "brokerBidList": [{
      "id": "1450",
      "name": "IMC Asia Pacific Limited",
      "pos": 1
    }, ... {
      "id": "3440",
      "name": "Goldman Sachs (Asia) Securities Limited",
      "pos": 1
    }]
  }
}
```









## <a href="#1532-3" class="header-anchor">#</a> GetBroker

`Futu::u32_t GetBroker(const Qot_GetBroker::Request &stReq);`  
`virtual void OnReply_GetBroker(Futu::u32_t nSerialNo, const Qot_GetBroker::Response &stRsp) = 0;`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf

message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Broker);
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
            Qot_GetBroker::Request req;
            Qot_GetBroker::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

            m_GetBrokerSerialNo = m_pQotApi->GetBroker(req);
            cout << "Request GetBroker SerialNo: " << m_GetBrokerSerialNo << endl;
        }
    }

    virtual void OnReply_GetBroker(Futu::u32_t nSerialNo, const Qot_GetBroker::Response &stRsp){
        if(nSerialNo == m_GetBrokerSerialNo)
        {
            cout << "OnReply_GetBroker SerialNo: " << nSerialNo << endl;
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
    Futu::u32_t m_GetBrokerSerialNo;
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
Request GetBroker SerialNo: 4
OnReply_GetBroker SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "brokerAskList": [
   {
    "id": "696",
    "name": "I-Access Investors Limited",
    "pos": 1
   },
   {
    "id": "8026",
    "name": "CLSA Limited",
    "pos": 1
   },
...
   {
    "id": "8948",
    "name": "BOCI Securities Limited",
    "pos": 2
   }
  ]
 }
}
```









## <a href="#1532-4" class="header-anchor">#</a> GetBroker

`GetBroker(req);`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf

message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetBroker(){
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
                subTypeList: [ SubType.SubType_Broker ],  
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
                    },
                };
                
                websocket.GetBroker(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("Broker: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Broker: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "brokerAskList": [{
    "id": "1049",
    "name": "IMC Asia Pacific Limited",
    "pos": 1
  }, {
    "id": "5199",
    "name": "Guotai Junan Securities (Hong Kong) Limited",
    "pos": 1
  }, ..., {
    "id": "4086",
    "name": "Credit Suisse Securities (Hong Kong) Limited",
    "pos": 5
  }],
  "brokerBidList": [{
    "id": "5882",
    "name": "Cinda International Securities Limited",
    "pos": 1
  }, {
    "id": "8564",
    "name": "ABN AMRO Clearing Hong Kong Limited",
    "pos": 1
  }, ..., {
    "id": "6997",
    "name": "China Investment Information Services Limited",
    "pos": 4
  }]
}
stop
```











Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Broker Queue
  Callback](/moomoo-api-doc/en/quote/update-broker.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).
- Under the BMP & LV1 HK market quotes, the broker queue market data is
  not supported.













- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#4493" class="header-anchor">#</a> get_broker_queue

`get_broker_queue(code)`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**

  | Parameter | Type | Description |
  |:----------|:-----|:------------|
  | code      | str  | Stock code. |

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
  <td rowspan="2">bid_frame_table</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, queue of bid brokers is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  <tr>
  <td rowspan="2">ask_frame_table</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, queue of ask brokers is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Queue of bid brokers format as follows:
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
    <td style="text-align: left;">bid_broker_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Bid broker ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_broker_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Bid broker name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bid_broker_pos</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Broker level.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Exchange order ID.
    
      
    
    
     
    
    <ul>
    <li>Not the order ID returned by the order interface.</li>
    <li>Only HK SF market quotes support returning this field.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">order_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Order volume.
    
      
    
    
     
    
    Only HK SF market quotes support returning this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>
  - Queue of ask brokers format as follows:
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
    <td style="text-align: left;">ask_broker_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Ask Broker ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_broker_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Ask Broker name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ask_broker_pos</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Broker level.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Exchange order ID.
    
      
    
    
     
    
    <ul>
    <li>Not the order ID returned by the order interface.</li>
    <li>Only HK SF market quotes support returning this field.</li>
    </ul>
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">order_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Order volume.
    
      
    
    
     
    
    Only HK SF market quotes support returning this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub, err_message = quote_ctx.subscribe(['HK.00700'], [SubType.BROKER], subscribe_push=False)
# First subscribe to the broker queue type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push the data to the script temporarily
if ret_sub == RET_OK: # Subscription successful
     ret, bid_frame_table, ask_frame_table = quote_ctx.get_broker_queue('HK.00700') # Get a broker queue data
     if ret == RET_OK:
         print(bid_frame_table)
     else:
         print('error:', bid_frame_table)
else:
     print(err_message)
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
    code     name  bid_broker_id                                    bid_broker_name  bid_broker_pos order_id order_volume
0   HK.00700  TENCENT           5338            J.P. Morgan Broking (Hong Kong) Limited               1      N/A          N/A
..       ...      ...            ...                                                ...             ...      ...          ...
36  HK.00700  TENCENT           8305  Futu Securities International (Hong Kong) Limited               4      N/A          N/A

[37 rows x 7 columns]
```









## <a href="#2229-2" class="header-anchor">#</a> Qot_GetBroker.proto

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3014





## <a href="#1532-5" class="header-anchor">#</a> GetBroker

`uint GetBroker(QotGetBroker.Request req);`  
`virtual void OnReply_GetBroker(MMAPI_Conn client, uint nSerialNo, QotGetBroker.Response rsp);`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn {
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Broker)
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

        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
            return;

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetBroker.C2S c2s = QotGetBroker.C2S.CreateBuilder()
                .SetSecurity(sec)
                .Build();
        QotGetBroker.Request req = QotGetBroker.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetBroker(req);
        Console.Write("Send QotGetBroker: {0}\n", seqNo);
    }

    public void OnReply_GetBroker(MMAPI_Conn client, uint nSerialNo, QotGetBroker.Response rsp)
    {
        Console.Write("Reply: QotGetBroker: {0}\n", nSerialNo);
        Console.Write("id: {0}, name: {1}\n", rsp.S2C.BrokerAskListList[0].Id, rsp.S2C.BrokerAskListList[0].Name);
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
Qot onInitConnect: ret=0 desc= connID=6825676366648053042
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetBroker: 4
Reply: QotGetBroker: 4
id: 5465, name: Futu Securities International (Hong Kong) Limited
```









## <a href="#1532-6" class="header-anchor">#</a> getBroker

`int getBroker(QotGetBroker.Request req);`  
`void onReply_GetBroker(MMAPI_Conn client, int nSerialNo, QotGetBroker.Response rsp);`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1);  //Set client information
        qot.setConnSpi(this);  //Set connection callback
        qot.setQotSpi(this);   //Set transaction callback
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
                .addSubTypeList(QotCommon.SubType.SubType_Broker_VALUE)
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
        System.out.printf("Reply: QotSub: %d  %s\n", nSerialNo, rsp.toString());

        if (rsp.getRetType() != Common.RetType.RetType_Succeed_VALUE)
            return;

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetBroker.C2S c2s = QotGetBroker.C2S.newBuilder()
                .setSecurity(sec)
                .build();
        QotGetBroker.Request req = QotGetBroker.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getBroker(req);
        System.out.printf("Send QotGetBroker: %d\n", seqNo);
    }

    @Override
    public void onReply_GetBroker(MMAPI_Conn client, int nSerialNo, QotGetBroker.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetBroker failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetBroker: %s\n", json);
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
Send QotGetBroker: 3
Receive QotGetBroker: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "brokerAskList": [{
      "id": "3440",
      "name": "Goldman Sachs (Asia) Securities Limited",
      "pos": 1
    }, ... {
      "id": "141",
      "name": "Haitong International Securities Company Limited",
      "pos": 1
    }],
    "brokerBidList": [{
      "id": "1450",
      "name": "IMC Asia Pacific Limited",
      "pos": 1
    }, ... {
      "id": "3440",
      "name": "Goldman Sachs (Asia) Securities Limited",
      "pos": 1
    }]
  }
}
```









## <a href="#1532-7" class="header-anchor">#</a> GetBroker

`moomoo::u32_t GetBroker(const Qot_GetBroker::Request &stReq);`  
`virtual void OnReply_GetBroker(moomoo::u32_t nSerialNo, const Qot_GetBroker::Response &stRsp) = 0;`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf

message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Broker);
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
            Qot_GetBroker::Request req;
            Qot_GetBroker::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

            m_GetBrokerSerialNo = m_pQotApi->GetBroker(req);
            cout << "Request GetBroker SerialNo: " << m_GetBrokerSerialNo << endl;
        }
    }

    virtual void OnReply_GetBroker(moomoo::u32_t nSerialNo, const Qot_GetBroker::Response &stRsp){
        if(nSerialNo == m_GetBrokerSerialNo)
        {
            cout << "OnReply_GetBroker SerialNo: " << nSerialNo << endl;
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
    moomoo::u32_t m_GetBrokerSerialNo;
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
Request GetBroker SerialNo: 4
OnReply_GetBroker SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "brokerAskList": [
   {
    "id": "696",
    "name": "I-Access Investors Limited",
    "pos": 1
   },
   {
    "id": "8026",
    "name": "CLSA Limited",
    "pos": 1
   },
...
   {
    "id": "8948",
    "name": "BOCI Securities Limited",
    "pos": 2
   }
  ]
 }
}
```









## <a href="#1532-8" class="header-anchor">#</a> GetBroker

`GetBroker(req);`

- **Description**

  Obtain real-time data of market participants on the order book.
  (Require real-time data subscription.)

- **Parameters**



``` protobuf

message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    optional string name = 4; // stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, Interface result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetBroker(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();
    
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
                subTypeList: [ SubType.SubType_Broker ],  
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
                    },
                };
                
                websocket.GetBroker(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("Broker: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Broker: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "brokerAskList": [{
    "id": "1049",
    "name": "IMC Asia Pacific Limited",
    "pos": 1
  }, {
    "id": "5199",
    "name": "Guotai Junan Securities (Hong Kong) Limited",
    "pos": 1
  }, ..., {
    "id": "4086",
    "name": "Credit Suisse Securities (Hong Kong) Limited",
    "pos": 5
  }],
  "brokerBidList": [{
    "id": "5882",
    "name": "Cinda International Securities Limited",
    "pos": 1
  }, {
    "id": "8564",
    "name": "ABN AMRO Clearing Hong Kong Limited",
    "pos": 1
  }, ..., {
    "id": "6997",
    "name": "China Investment Information Services Limited",
    "pos": 4
  }]
}
stop
```











Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Broker Queue
  Callback](/moomoo-api-doc/en/quote/update-broker.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).
- Under the LV1 HK market quotes, the broker queue market data is not
  supported.













