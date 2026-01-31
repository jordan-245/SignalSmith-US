



# <a href="#7360" class="header-anchor">#</a> Real-time Time Frame Callback









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks. After receiving the real-time
  Time Frame data push, it will call back to this function. You need to
  override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdateRT_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
  <td>If ret == RET_OK, Time Frame data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Time Frame data format as follows:
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
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_blank</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Data status.
    
      
    
    
     
    
    False: normal data.<br />
    True: forged data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">opened_mins</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">How many minutes have passed from 0
    o'clock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Current price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average price.
    
      
    
    
     
    
    For options, this field is None.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
import time
from futu import *

class RTDataTest(RTDataHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(RTDataTest, self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("RTDataTest: error, msg: %s"% data)
            return RET_ERROR, data
        print("RTDataTest ", data) # RTDataTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = RTDataTest()
quote_ctx.set_handler(handler) # Set real-time Time Frame push callback
ret, data = quote_ctx.subscribe(['US.AAPL'], [SubType.RT_DATA], session=Session.ALL) # Subscribe to the Time Frame type, OpenD starts to continuously receive pushes from the server
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute   
```





- **Output**



``` python
RTDataTest        code name                 time  is_blank  opened_mins  cur_price  last_close   avg_price   turnover  volume
0  US.AAPL   APPLE  2025-04-07 05:24:00     False          324     179.53      188.38  180.465762  651262.42    3624
```









## <a href="#7747" class="header-anchor">#</a> Qot_UpdateRT.proto

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3009





`virtual void OnReply_UpdateRT(FTAPI_Conn client, QotUpdateRT.Response rsp);`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_RT)
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
    
    public void OnReply_UpdateRT(FTAPI_Conn client, uint nSerialNo, QotUpdateRT.Response rsp)
    {
        Console.Write("Push: UpdateRT: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.RtListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825406853696994420
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Push: UpdateRT: 6
price: 490
...
```









`void onPush_UpdateRT(FTAPI_Conn client, QotUpdateRT.Response rsp);`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
                .addSubTypeList(QotCommon.SubType.SubType_RT_VALUE)
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
    public void onPush_UpdateRT(FTAPI_Conn client, QotUpdateRT.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdateRT failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdateRT: %s\n", json);
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
Receive QotUpdateRT: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "rtList": [{
      "time": "2021-06-25 10:22:00",
      "minute": 622,
      "isBlank": false,
      "price": 587.5,
      "lastClosePrice": 583.0,
      "avgPrice": 587.0746400046605,
      "volume": "21100",
      "turnover": 1.2402E7,
      "timestamp": 1.62458772E9
    }]
  }
}
Receive QotUpdateRT: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "rtList": [{
      "time": "2021-06-25 10:22:00",
      "minute": 622,
      "isBlank": false,
      "price": 587.5,
      "lastClosePrice": 583.5,
      "avgPrice": 587.0746400046610,
      "volume": "16300",
      "turnover": 1.2402E7,
      "timestamp": 1.62458772E9
    }]
  }
}
```









`virtual void OnPush_UpdateRT(const Qot_UpdateRT::Response &stRsp) = 0;`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_RT);
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

    virtual void OnPush_UpdateRT(const Qot_UpdateRT::Response &stRsp) {
        cout << "OnPush_UpdateRT: " << endl;
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
OnPush_UpdateRT: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "rtList": [
   {
    "time": "2021-06-09 15:41:00",
    "minute": 941,
    "isBlank": false,
    "price": 602.5,
    "lastClosePrice": 601,
    "avgPrice": 602.074756891773,
    "volume": "12700",
    "turnover": 7652950,
    "timestamp": 1623224460
   }
  ]
 }
}

OnPush_UpdateRT: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "rtList": [
   {
    "time": "2021-06-09 15:41:00",
    "minute": 941,
    "isBlank": false,
    "price": 603,
    "lastClosePrice": 601,
    "avgPrice": 602.07498717395617,
    "volume": "14200",
    "turnover": 8557450,
    "timestamp": 1623224460
   }
  ]
 }
}
```









`OnPush(cmd,res)`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";

function QotUpdateRT(){
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
                subTypeList: [ SubType.SubType_RT ], // Subscribe to the Time Frame type
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            };

            websocket.Sub(req) // Subscribe to the Time Frame type, OpenD starts to continuously receive pushes from the server
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
        if(ftCmdID.QotUpdateRT.cmd == cmd){ // RTDataTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("RTDataTest", JSON.stringify(s2c));
            } else {
                console.log("RTDataTest: error")
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
RTDataTest {"security":{"market":1,"code":"00700"},"rtList":[{"time":"2021-09-09 16:00:00","minute":960,"isBlank":false,"price":480,"lastClosePrice":524.5,"avgPrice":493.8398248240191,"volume":"5134400","turnover":2464740790,"timestamp":1631174400}]}
RTDataTest { ... }
 ...
 ...
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Real-time Time Frame
  Data](/moomoo-api-doc/en/quote/get-rt.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks. After receiving the real-time
  Time Frame data push, it will call back to this function. You need to
  override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdateRT_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
  <td>If ret == RET_OK, Time Frame data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Time Frame data format as follows:
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
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_blank</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Data status.
    
      
    
    
     
    
    False: normal data.<br />
    True: forged data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">opened_mins</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">How many minutes have passed from 0
    o'clock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Current price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average price.
    
      
    
    
     
    
    For options, this field is None.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
import time
from moomoo import *

class RTDataTest(RTDataHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(RTDataTest, self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("RTDataTest: error, msg: %s"% data)
            return RET_ERROR, data
        print("RTDataTest ", data) # RTDataTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = RTDataTest()
quote_ctx.set_handler(handler) # Set real-time Time Frame push callback
ret, data = quote_ctx.subscribe(['US.AAPL'], [SubType.RT_DATA], session=Session.ALL) # Subscribe to the Time Frame type, OpenD starts to continuously receive pushes from the server
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute   
```





- **Output**



``` python
RTDataTest        code name                 time  is_blank  opened_mins  cur_price  last_close   avg_price   turnover  volume
0  US.AAPL   APPLE  2025-04-07 05:24:00     False          324     179.53      188.38  180.465762  651262.42    3624
```









## <a href="#7747-2" class="header-anchor">#</a> Qot_UpdateRT.proto

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3009





`virtual void OnReply_UpdateRT(MMAPI_Conn client, QotUpdateRT.Response rsp);`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_RT)
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
    
    public void OnReply_UpdateRT(MMAPI_Conn client, uint nSerialNo, QotUpdateRT.Response rsp)
    {
        Console.Write("Push: UpdateRT: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.RtListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825406853696994420
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Push: UpdateRT: 6
price: 490
...
```









`void onPush_UpdateRT(MMAPI_Conn client, QotUpdateRT.Response rsp);`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
                .addSubTypeList(QotCommon.SubType.SubType_RT_VALUE)
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
    public void onPush_UpdateRT(MMAPI_Conn client, QotUpdateRT.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdateRT failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdateRT: %s\n", json);
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
Receive QotUpdateRT: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "rtList": [{
      "time": "2021-06-25 10:22:00",
      "minute": 622,
      "isBlank": false,
      "price": 587.5,
      "lastClosePrice": 583.0,
      "avgPrice": 587.0746400046605,
      "volume": "21100",
      "turnover": 1.2402E7,
      "timestamp": 1.62458772E9
    }]
  }
}
Receive QotUpdateRT: {
  "retType": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "rtList": [{
      "time": "2021-06-25 10:22:00",
      "minute": 622,
      "isBlank": false,
      "price": 587.5,
      "lastClosePrice": 583.5,
      "avgPrice": 587.0746400046610,
      "volume": "16300",
      "turnover": 1.2402E7,
      "timestamp": 1.62458772E9
    }]
  }
}
```









`virtual void OnPush_UpdateRT(const Qot_UpdateRT::Response &stRsp) = 0;`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_RT);
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

    virtual void OnPush_UpdateRT(const Qot_UpdateRT::Response &stRsp) {
        cout << "OnPush_UpdateRT: " << endl;
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
OnPush_UpdateRT: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "rtList": [
   {
    "time": "2021-06-09 15:41:00",
    "minute": 941,
    "isBlank": false,
    "price": 602.5,
    "lastClosePrice": 601,
    "avgPrice": 602.074756891773,
    "volume": "12700",
    "turnover": 7652950,
    "timestamp": 1623224460
   }
  ]
 }
}

OnPush_UpdateRT: 
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "rtList": [
   {
    "time": "2021-06-09 15:41:00",
    "minute": 941,
    "isBlank": false,
    "price": 603,
    "lastClosePrice": 601,
    "avgPrice": 602.07498717395617,
    "volume": "14200",
    "turnover": 8557450,
    "timestamp": 1623224460
   }
  ]
 }
}
```









`OnPush(cmd,res)`

- **Description**

  Real-time Time Frame callback, asynchronous processing of real-time
  Time Frame push of subscribed stocks.

- **Parameters**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Pushed Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";

function QotUpdateRT(){
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
                subTypeList: [ SubType.SubType_RT ], // Subscribe to the Time Frame type
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            };

            websocket.Sub(req) // Subscribe to the Time Frame type, OpenD starts to continuously receive pushes from the server
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
        if(mmCmdID.QotUpdateRT.cmd == cmd){ // RTDataTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                console.log("RTDataTest", JSON.stringify(s2c));
            } else {
                console.log("RTDataTest: error")
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
RTDataTest {"security":{"market":1,"code":"00700"},"rtList":[{"time":"2021-09-09 16:00:00","minute":960,"isBlank":false,"price":480,"lastClosePrice":524.5,"avgPrice":493.8398248240191,"volume":"5134400","turnover":2464740790,"timestamp":1631174400}]}
RTDataTest { ... }
 ...
 ...
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Real-time Time Frame
  Data](/moomoo-api-doc/en/quote/get-rt.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).













