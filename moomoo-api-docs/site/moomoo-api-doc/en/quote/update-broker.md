



# <a href="#5111" class="header-anchor">#</a> Real-time Broker Queue Callback









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  Real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks. After receiving the real-time
  broker queue data push, it will call back to this function. You need
  to override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdateBroker_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
  <td>tuple</td>
  <td>If ret == RET_OK, broker queue data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Broker queue data format as follows:

    | Field           | Type         | Description    |
    |:----------------|:-------------|:---------------|
    | stock_code      | str          | Stock code.    |
    | bid_frame_table | pd.DataFrame | Data from bid. |
    | ask_frame_table | pd.DataFrame | Data from ask. |

    - Bid_frame_table format as follows:
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
    - Ask_frame_table format as follows:
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
import time
from futu import *
    
class BrokerTest(BrokerHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, err_or_stock_code, data = super(BrokerTest, self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("BrokerTest: error, msg: {}".format(err_or_stock_code))
            return RET_ERROR, data
        print("BrokerTest: stock: {} data: {} ".format(err_or_stock_code, data)) # BrokerTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = BrokerTest()
quote_ctx.set_handler(handler) # Set real-time broker push callback
ret, data = quote_ctx.subscribe(['HK.00700'], [SubType.BROKER]) # Subscribe to the broker type, OpenD starts to receive continuous push from the server
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
BrokerTest: stock: HK.00700 data: [        code     name  bid_broker_id                                    bid_broker_name  bid_broker_pos order_id order_volume
0   HK.00700  TENCENT           5338            J.P. Morgan Broking (Hong Kong) Limited               1      N/A          N/A
..       ...      ...            ...                                                ...             ...      ...          ...
36  HK.00700  TENCENT           8305  Futu Securities International (Hong Kong) Limited               4      N/A          N/A

[37 rows x 7 columns],         code     name  ask_broker_id                                ask_broker_name  ask_broker_pos order_id order_volume
0   HK.00700  TENCENT           1179  Huatai Financial Holdings (Hong Kong) Limited               1      N/A          N/A
..       ...      ...            ...                                            ...             ...      ...          ...
39  HK.00700  TENCENT           6996  China Investment Information Services Limited               1      N/A          N/A

[40 rows x 7 columns]] 
```









## <a href="#2655" class="header-anchor">#</a> Qot_UpdateBroker.proto

- **Description**

  Real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3015





`virtual void OnReply_UpdateBroker(FTAPI_Conn client, QotUpdateBroker.Response rsp);`

- **Description**

  Real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Broker)
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
    
    public void OnReply_UpdateBroker(FTAPI_Conn client, uint nSerialNo, QotUpdateBroker.Response rsp)
    {
        Console.Write("Push: UpdateBroker: {0}\n", nSerialNo);
        Console.Write("id: {0} , name: {1}\n", rsp.S2C.BrokerAskListList[0].Id, rsp.S2C.BrokerAskListList[0].Name);
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
Qot onInitConnect: ret=0 desc= connID=6825611828715002257
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Push: UpdateBroker: 1
id: 696 , name: Futu Securities International (Hong Kong) Limited
...
```









`void onPush_UpdateBroker(FTAPI_Conn client, QotUpdateBroker.Response rsp);`

- **Description**

real-time broker queue callback, asynchronous processing of real-time
broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
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
                .addSubTypeList(QotCommon.SubType.SubType_Broker_VALUE)
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
    public void onPush_UpdateBroker(FTAPI_Conn client, QotUpdateBroker.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdateBroker failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdateBroker: %s\n", json);
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
Receive QotUpdateBroker: {
  "retType": 0,
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
Receive QotGetBroker: {
  "retType": 0,
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









`virtual void OnPush_UpdateBroker(const Qot_UpdateBroker::Response &stRsp) = 0;`

- **Description**

  real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
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
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }
        }
    }

    virtual void OnPush_UpdateBroker(const Qot_UpdateBroker::Response &stRsp) {
        cout << "OnPush_UpdateBroker: " << endl;
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
OnPush_UpdateBroker: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "brokerAskList": [
   {
    "id": "5336",
    "name": "J.P. Morgan Broking (Hong Kong) Limited",
    "pos": 1
   },
...
   {
    "id": "6996",
    "name": "China Investment Information Services Limited",
    "pos": 2
   }
  ],
  "brokerBidList": [
   {
    "id": "6100",
    "name": "Guotai Junan Securities (Hong Kong) Limited",
    "pos": 1
   },
...
   {
    "id": "747",
    "name": "IMC Asia Pacific Limited",
    "pos": 3
   }
  ]
 }
}
```









`OnPush(cmd,res)`

- **Description**

  real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
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

function QotUpdateBroker(){
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
                subTypeList: [ SubType.SubType_Broker ], // Subscribe to the broker type
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            }; 

            websocket.Sub(req) // Subscribe to the broker type, OpenD starts to receive continuous push from the server
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
        if(ftCmdID.QotUpdateBroker.cmd == cmd){ // BrokerTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("BrokerTest", JSON.stringify(s2c));
            } else {
                console.log("BrokerTest: error")
            }
        }
    };

    websocket.start(addr, port, enable_ssl, key);

    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 5000); // Set the script to receive OpenD push duration to 5 seconds
```





- **Output**



``` javascript
BrokerTest {"security":{"market":1,"code":"00700"},"brokerAskList":[{"id":"6996","name":"China Investment Information Services Limited","pos":1},{"id":"8463","name":"Futu Securities International (Hong Kong) Limited","pos":1},{"id":"7389","name":"Citigroup Global Markets Asia Limited","pos":1},{"id":"6997","name":"China Investment Information Services Limited","pos":2},{"id":"1799","name":"Bright Smart Securities International (H.K.) Limited","pos":3},{"id":"1048","name":"IMC Asia Pacific Limited","pos":3},{"id":"8305","name":"Futu Securities International (Hong Kong) Limited","pos":3},{"id":"1978","name":"Hafoo Securities Limited","pos":4},{"id":"747","name":"IMC Asia Pacific Limited","pos":4},{"id":"8301","name":"Futu Securities International (Hong Kong) Limited","pos":4},{"id":"518","name":"Eclipse Options (HK) Limited","pos":4},{"id":"4978","name":"SG Securities (HK) Limited","pos":4},{"id":"6699","name":"Interactive Brokers Hong Kong Limited","pos":4},{"id":"746","name":"IMC Asia Pacific Limited","pos":5},{"id":"5467","name":"Morgan Stanley Hong Kong Securities Limited","pos":5},{"id":"518","name":"Eclipse Options (HK) Limited","pos":5},{"id":"5468","name":"Morgan Stanley Hong Kong Securities Limited","pos":5},{"id":"4978","name":"SG Securities (HK) Limited","pos":5},{"id":"1049","name":"IMC Asia Pacific Limited","pos":6},{"id":"4973","name":"SG Securities (HK) Limited","pos":6},{"id":"8020","name":"CLSA Limited","pos":6},{"id":"4978","name":"SG Securities (HK) Limited","pos":6},{"id":"518","name":"Eclipse Options (HK) Limited","pos":6},{"id":"6996","name":"China Investment Information Services Limited","pos":7},{"id":"746","name":"IMC Asia Pacific Limited","pos":7},{"id":"2425","name":"Barclays Capital Asia Limited","pos":7},{"id":"5465","name":"Morgan Stanley Hong Kong Securities Limited","pos":7},{"id":"747","name":"IMC Asia Pacific Limited","pos":8},{"id":"2245","name":"Futu Securities International (Hong Kong) Limited","pos":8},{"id":"8033","name":"CLSA Limited","pos":8},{"id":"6036","name":"Flow Traders Hong Kong Limited","pos":8},{"id":"1049","name":"IMC Asia Pacific Limited","pos":9}],"brokerBidList":[{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"3289","name":"Merrill Lynch Far East Limited","pos":1},{"id":"6999","name":"China Investment Information Services Limited","pos":1},{"id":"8465","name":"Futu Securities International (Hong Kong) Limited","pos":1},{"id":"5528","name":"Sun Hung Kai Investment Services Limited","pos":1},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"6997","name":"China Investment Information Services Limited","pos":1},{"id":"2846","name":"Macquarie Capital Limited","pos":1},{"id":"6998","name":"China Investment Information Services Limited","pos":1},{"id":"6997","name":"China Investment Information Services Limited","pos":1},{"id":"2645","name":"Maven Asia (Hong Kong) Limited","pos":2},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":2},{"id":"3609","name":"Orient Securities Limited","pos":2},{"id":"6699","name":"Interactive Brokers Hong Kong Limited","pos":2},{"id":"5339","name":"J.P. Morgan Broking (Hong Kong) Limited","pos":2},{"id":"8301","name":"Futu Securities International (Hong Kong) Limited","pos":2},{"id":"8308","name":"Futu Securities International (Hong Kong) Limited","pos":2},{"id":"6997","name":"China Investment Information Services Limited","pos":2},{"id":"4098","name":"Credit Suisse Securities (Hong Kong) Limited","pos":2},{"id":"1049","name":"IMC Asia Pacific Limited","pos":2},{"id":"8574","name":"HSBC Securities Brokers (Asia) Limited","pos":2},{"id":"5999","name":"China Innovation Market Service Company Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"5998","name":"China Innovation Market Service Company Limited","pos":3},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3}]}
BrokerTest { ... }
 ...
 ...
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Real-time
  Orderbook](/moomoo-api-doc/en/quote/get-broker.html) API.
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





`on_recv_rsp(self, rsp_pb)`

- **Description**

  Real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks. After receiving the real-time
  broker queue data push, it will call back to this function. You need
  to override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdateBroker_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
  <td>tuple</td>
  <td>If ret == RET_OK, broker queue data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Broker queue data format as follows:

    | Field           | Type         | Description    |
    |:----------------|:-------------|:---------------|
    | stock_code      | str          | Stock code.    |
    | bid_frame_table | pd.DataFrame | Data from bid. |
    | ask_frame_table | pd.DataFrame | Data from ask. |

    - Bid_frame_table format as follows:
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
    - Ask_frame_table format as follows:
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
import time
from moomoo import *
    
class BrokerTest(BrokerHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, err_or_stock_code, data = super(BrokerTest, self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("BrokerTest: error, msg: {}".format(err_or_stock_code))
            return RET_ERROR, data
        print("BrokerTest: stock: {} data: {} ".format(err_or_stock_code, data)) # BrokerTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = BrokerTest()
quote_ctx.set_handler(handler) # Set real-time broker push callback
ret, data = quote_ctx.subscribe(['HK.00700'], [SubType.BROKER]) # Subscribe to the broker type, OpenD starts to receive continuous push from the server
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
BrokerTest: stock: HK.00700 data: [        code     name  bid_broker_id                                    bid_broker_name  bid_broker_pos order_id order_volume
0   HK.00700  TENCENT           5338            J.P. Morgan Broking (Hong Kong) Limited               1      N/A          N/A
..       ...      ...            ...                                                ...             ...      ...          ...
36  HK.00700  TENCENT           8305  Futu Securities International (Hong Kong) Limited               4      N/A          N/A

[37 rows x 7 columns],         code     name  ask_broker_id                                ask_broker_name  ask_broker_pos order_id order_volume
0   HK.00700  TENCENT           1179  Huatai Financial Holdings (Hong Kong) Limited               1      N/A          N/A
..       ...      ...            ...                                            ...             ...      ...          ...
39  HK.00700  TENCENT           6996  China Investment Information Services Limited               1      N/A          N/A

[40 rows x 7 columns]] 
```









## <a href="#2655-2" class="header-anchor">#</a> Qot_UpdateBroker.proto

- **Description**

  Real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3015





`virtual void OnReply_UpdateBroker(MMAPI_Conn client, QotUpdateBroker.Response rsp);`

- **Description**

  Real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the broker queue structure, refer to
>   [Broker](/moomoo-api-doc/en/quote/quote.html#9607)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Broker)
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
    
    public void OnReply_UpdateBroker(MMAPI_Conn client, uint nSerialNo, QotUpdateBroker.Response rsp)
    {
        Console.Write("Push: UpdateBroker: {0}\n", nSerialNo);
        Console.Write("id: {0} , name: {1}\n", rsp.S2C.BrokerAskListList[0].Id, rsp.S2C.BrokerAskListList[0].Name);
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
Qot onInitConnect: ret=0 desc= connID=6825611828715002257
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Push: UpdateBroker: 1
id: 696 , name: Futu Securities International (Hong Kong) Limited
...
```









`void onPush_UpdateBroker(MMAPI_Conn client, QotUpdateBroker.Response rsp);`

- **Description**

real-time broker queue callback, asynchronous processing of real-time
broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
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
                .addSubTypeList(QotCommon.SubType.SubType_Broker_VALUE)
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
    public void onPush_UpdateBroker(MMAPI_Conn client, QotUpdateBroker.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdateBroker failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdateBroker: %s\n", json);
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
Receive QotUpdateBroker: {
  "retType": 0,
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
Receive QotGetBroker: {
  "retType": 0,
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









`virtual void OnPush_UpdateBroker(const Qot_UpdateBroker::Response &stRsp) = 0;`

- **Description**

  real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
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
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }
        }
    }

    virtual void OnPush_UpdateBroker(const Qot_UpdateBroker::Response &stRsp) {
        cout << "OnPush_UpdateBroker: " << endl;
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
OnPush_UpdateBroker: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "brokerAskList": [
   {
    "id": "5336",
    "name": "J.P. Morgan Broking (Hong Kong) Limited",
    "pos": 1
   },
...
   {
    "id": "6996",
    "name": "China Investment Information Services Limited",
    "pos": 2
   }
  ],
  "brokerBidList": [
   {
    "id": "6100",
    "name": "Guotai Junan Securities (Hong Kong) Limited",
    "pos": 1
   },
...
   {
    "id": "747",
    "name": "IMC Asia Pacific Limited",
    "pos": 3
   }
  ]
 }
}
```









`OnPush(cmd,res)`

- **Description**

  real-time broker queue callback, asynchronous processing of real-time
  broker queue push of subscribed stocks.

- **Parameters**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.Broker brokerAskList = 2; //Broker Ask (selling) order
    repeated Qot_Common.Broker brokerBidList = 3; //Broker Bid (buy) order
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For security structure, refer to
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

function QotUpdateBroker(){
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
                subTypeList: [ SubType.SubType_Broker ], // Subscribe to the broker type
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            }; 

            websocket.Sub(req) // Subscribe to the broker type, OpenD starts to receive continuous push from the server
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
        if(mmCmdID.QotUpdateBroker.cmd == cmd){ // BrokerTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("BrokerTest", JSON.stringify(s2c));
            } else {
                console.log("BrokerTest: error")
            }
        }
    };

    websocket.start(addr, port, enable_ssl, key);

    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 5000); // Set the script to receive OpenD push duration to 5 seconds
```





- **Output**



``` javascript
BrokerTest {"security":{"market":1,"code":"00700"},"brokerAskList":[{"id":"6996","name":"China Investment Information Services Limited","pos":1},{"id":"8463","name":"Futu Securities International (Hong Kong) Limited","pos":1},{"id":"7389","name":"Citigroup Global Markets Asia Limited","pos":1},{"id":"6997","name":"China Investment Information Services Limited","pos":2},{"id":"1799","name":"Bright Smart Securities International (H.K.) Limited","pos":3},{"id":"1048","name":"IMC Asia Pacific Limited","pos":3},{"id":"8305","name":"Futu Securities International (Hong Kong) Limited","pos":3},{"id":"1978","name":"Hafoo Securities Limited","pos":4},{"id":"747","name":"IMC Asia Pacific Limited","pos":4},{"id":"8301","name":"Futu Securities International (Hong Kong) Limited","pos":4},{"id":"518","name":"Eclipse Options (HK) Limited","pos":4},{"id":"4978","name":"SG Securities (HK) Limited","pos":4},{"id":"6699","name":"Interactive Brokers Hong Kong Limited","pos":4},{"id":"746","name":"IMC Asia Pacific Limited","pos":5},{"id":"5467","name":"Morgan Stanley Hong Kong Securities Limited","pos":5},{"id":"518","name":"Eclipse Options (HK) Limited","pos":5},{"id":"5468","name":"Morgan Stanley Hong Kong Securities Limited","pos":5},{"id":"4978","name":"SG Securities (HK) Limited","pos":5},{"id":"1049","name":"IMC Asia Pacific Limited","pos":6},{"id":"4973","name":"SG Securities (HK) Limited","pos":6},{"id":"8020","name":"CLSA Limited","pos":6},{"id":"4978","name":"SG Securities (HK) Limited","pos":6},{"id":"518","name":"Eclipse Options (HK) Limited","pos":6},{"id":"6996","name":"China Investment Information Services Limited","pos":7},{"id":"746","name":"IMC Asia Pacific Limited","pos":7},{"id":"2425","name":"Barclays Capital Asia Limited","pos":7},{"id":"5465","name":"Morgan Stanley Hong Kong Securities Limited","pos":7},{"id":"747","name":"IMC Asia Pacific Limited","pos":8},{"id":"2245","name":"Futu Securities International (Hong Kong) Limited","pos":8},{"id":"8033","name":"CLSA Limited","pos":8},{"id":"6036","name":"Flow Traders Hong Kong Limited","pos":8},{"id":"1049","name":"IMC Asia Pacific Limited","pos":9}],"brokerBidList":[{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"3289","name":"Merrill Lynch Far East Limited","pos":1},{"id":"6999","name":"China Investment Information Services Limited","pos":1},{"id":"8465","name":"Futu Securities International (Hong Kong) Limited","pos":1},{"id":"5528","name":"Sun Hung Kai Investment Services Limited","pos":1},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":1},{"id":"1194","name":"Credit Suisse Securities (Hong Kong) Limited","pos":1},{"id":"6997","name":"China Investment Information Services Limited","pos":1},{"id":"2846","name":"Macquarie Capital Limited","pos":1},{"id":"6998","name":"China Investment Information Services Limited","pos":1},{"id":"6997","name":"China Investment Information Services Limited","pos":1},{"id":"2645","name":"Maven Asia (Hong Kong) Limited","pos":2},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":2},{"id":"3609","name":"Orient Securities Limited","pos":2},{"id":"6699","name":"Interactive Brokers Hong Kong Limited","pos":2},{"id":"5339","name":"J.P. Morgan Broking (Hong Kong) Limited","pos":2},{"id":"8301","name":"Futu Securities International (Hong Kong) Limited","pos":2},{"id":"8308","name":"Futu Securities International (Hong Kong) Limited","pos":2},{"id":"6997","name":"China Investment Information Services Limited","pos":2},{"id":"4098","name":"Credit Suisse Securities (Hong Kong) Limited","pos":2},{"id":"1049","name":"IMC Asia Pacific Limited","pos":2},{"id":"8574","name":"HSBC Securities Brokers (Asia) Limited","pos":2},{"id":"5999","name":"China Innovation Market Service Company Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"5998","name":"China Innovation Market Service Company Limited","pos":3},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8564","name":"ABN AMRO Clearing Hong Kong Limited","pos":3},{"id":"8565","name":"ABN AMRO Clearing Hong Kong Limited","pos":3}]}
BrokerTest { ... }
 ...
 ...
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Real-time
  Orderbook](/moomoo-api-doc/en/quote/get-broker.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).
- Under the LV1 HK market quotes, the broker queue market data is not
  supported.













