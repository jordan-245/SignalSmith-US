



# <a href="#1092" class="header-anchor">#</a> Get Subscription Status









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`query_subscription(is_all_conn=True)`

- **Description**

  Get subscription information

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
  <td style="text-align: left;">is_all_conn</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to return the subscription status
  of all connections.
  
    
  
  
   
  
  True: return the subscription status of all connections.<br />
  False: return only the status of the current connection.
  
  
  
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
  <td>If ret == RET_OK, subscription information data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - subscription information data format as follows:

    

          {
              'total_used': subscription quota used by all connections,
              'own_used': The subscription quota used by the current connection,
              'remain': remaining subscription quota,
              'sub_list': The stock list corresponding to each subscription type,
              {
                  'Subscription type': A list of all subscribed stocks under this subscription type,
                  …
              }
          }

    

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

quote_ctx.subscribe(['HK.00700'], [SubType.QUOTE])
ret, data = quote_ctx.query_subscription()
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
{'total_used': 1, 'remain': 999, 'own_used': 1, 'sub_list': {'QUOTE': ['HK.00700']}}
```









## <a href="#3734" class="header-anchor">#</a> Qot_GetSubInfo.proto

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3003





`uint GetSubInfo(QotGetSubInfo.Request req);`  
`virtual void OnReply_GetSubInfo(FTAPI_Conn client, uint nSerialNo, QotGetSubInfo.Response rsp);`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
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

        QotGetSubInfo.C2S c2s = QotGetSubInfo.C2S.CreateBuilder()
            .Build();
        QotGetSubInfo.Request req = QotGetSubInfo.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetSubInfo(req);
        Console.Write("Send QotGetSubInfo: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_GetSubInfo(FTAPI_Conn client, uint nSerialNo, QotGetSubInfo.Response rsp) {
        Console.Write("Reply: QotGetSubInfo: {0}  {1}\n", nSerialNo, rsp.ToString());
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
Qot onInitConnect: ret=0 desc= connID=6819190992235784251
Send QotGetSubInfo: 3
Reply: QotGetSubInfo: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  connSubInfoList {
    usedQuota: 0
    isOwnConnData: true
  }
  totalUsedQuota: 0
  remainQuota: 1000
}
```









`int getSubInfo(QotGetSubInfo.Request req);`  
`void onReply_GetSubInfo(FTAPI_Conn client, int nSerialNo, QotGetSubInfo.Response rsp);`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
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

        QotGetSubInfo.C2S c2s = QotGetSubInfo.C2S.newBuilder()
            .build();
        QotGetSubInfo.Request req = QotGetSubInfo.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getSubInfo(req);
        System.out.printf("Send QotGetSubInfo: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetSubInfo(FTAPI_Conn client, int nSerialNo, QotGetSubInfo.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetSubInfo failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetSubInfo: %s\n", json);
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
Send QotGetSubInfo: 2
Receive QotGetSubInfo: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "connSubInfoList": [{
      "usedQuota": 0,
      "isOwnConnData": true
    }],
    "totalUsedQuota": 0,
    "remainQuota": 300
  }
}
```









`Futu::u32_t GetSubInfo(const Qot_GetSubInfo::Request &stReq);`  
`virtual void OnReply_GetSubInfo(Futu::u32_t nSerialNo, const Qot_GetSubInfo::Response &stRsp) = 0;`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
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

        // construct request message
        Qot_GetSubInfo::Request req;
        Qot_GetSubInfo::C2S *c2s = req.mutable_c2s();

        m_GetSubInfoSerialNo = m_pQotApi->GetSubInfo(req);
        cout << "Request GetSubInfo SerialNo: " << m_GetSubInfoSerialNo << endl;
    }

    virtual void OnReply_GetSubInfo(Futu::u32_t nSerialNo, const Qot_GetSubInfo::Response &stRsp){
        if(nSerialNo == m_GetSubInfoSerialNo)
        {
            cout << "OnReply_GetSubInfo SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetSubInfoSerialNo;
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
Request GetSubInfo SerialNo: 4
OnReply_GetSubInfo SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "connSubInfoList": [
   {
    "usedQuota": 0,
    "isOwnConnData": true
   }
  ],
  "totalUsedQuota": 1,
  "remainQuota": 299
 }
}
```









`GetSubInfo(req);`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";

function GetSubInfo(){
    const { RetType } = Common;
    const { SubType, QotMarket } = Qot_Common;
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
            }).then((res) => { 

                const req = {
                    c2s: {
                        isReqAllConn: true,
                    },
                };

                websocket.GetSubInfo(req)
                .then((res) => { 
                    let { errCode, retMsg, retType,s2c } = res
                    if(retType == RetType.RetType_Succeed){
                        console.log("GetSubInfo: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                        console.log("GetSubInfo:", JSON.stringify(s2c)); 
                    } else {
                        console.log("GetSubInfo: error")
                    }
                })
                .catch((error) => {
                    console.log(error)
                    if ("retMsg" in error) {
                        console.log("error:", error.retMsg);
                    }
                });

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
GetSubInfo: errCode 0, retMsg , retType 0
GetSubInfo: {"connSubInfoList":[{"subInfoList":[{"subType":2,"securityList":[{"market":1,"code":"00700"}]}],"usedQuota":1,"isOwnConnData":true}],"totalUsedQuota":1,"remainQuota":99}
stop
```

















- Python
- Proto
- C#
- Java
- C++
- JavaScript





`query_subscription(is_all_conn=True)`

- **Description**

  Get subscription information

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
  <td style="text-align: left;">is_all_conn</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to return the subscription status
  of all connections.
  
    
  
  
   
  
  True: return the subscription status of all connections.<br />
  False: return only the status of the current connection.
  
  
  
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
  <td>If ret == RET_OK, subscription information data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - subscription information data format as follows:

    

          {
              'total_used': subscription quota used by all connections,
              'own_used': The subscription quota used by the current connection,
              'remain': remaining subscription quota,
              'sub_list': The stock list corresponding to each subscription type,
              {
                  'Subscription type': A list of all subscribed stocks under this subscription type,
                  …
              }
          }

    

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

quote_ctx.subscribe(['HK.00700'], [SubType.QUOTE])
ret, data = quote_ctx.query_subscription()
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
{'total_used': 1, 'remain': 999, 'own_used': 1, 'sub_list': {'QUOTE': ['HK.00700']}}
```









## <a href="#3734-2" class="header-anchor">#</a> Qot_GetSubInfo.proto

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3003





`uint GetSubInfo(QotGetSubInfo.Request req);`  
`virtual void OnReply_GetSubInfo(MMAPI_Conn client, uint nSerialNo, QotGetSubInfo.Response rsp);`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
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

        QotGetSubInfo.C2S c2s = QotGetSubInfo.C2S.CreateBuilder()
            .Build();
        QotGetSubInfo.Request req = QotGetSubInfo.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetSubInfo(req);
        Console.Write("Send QotGetSubInfo: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_GetSubInfo(MMAPI_Conn client, uint nSerialNo, QotGetSubInfo.Response rsp) {
        Console.Write("Reply: QotGetSubInfo: {0}  {1}\n", nSerialNo, rsp.ToString());
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
Qot onInitConnect: ret=0 desc= connID=6819190992235784251
Send QotGetSubInfo: 3
Reply: QotGetSubInfo: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  connSubInfoList {
    usedQuota: 0
    isOwnConnData: true
  }
  totalUsedQuota: 0
  remainQuota: 1000
}
```









`int getSubInfo(QotGetSubInfo.Request req);`  
`void onReply_GetSubInfo(MMAPI_Conn client, int nSerialNo, QotGetSubInfo.Response rsp);`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
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

        QotGetSubInfo.C2S c2s = QotGetSubInfo.C2S.newBuilder()
            .build();
        QotGetSubInfo.Request req = QotGetSubInfo.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getSubInfo(req);
        System.out.printf("Send QotGetSubInfo: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetSubInfo(MMAPI_Conn client, int nSerialNo, QotGetSubInfo.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetSubInfo failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetSubInfo: %s\n", json);
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
Send QotGetSubInfo: 2
Receive QotGetSubInfo: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "connSubInfoList": [{
      "usedQuota": 0,
      "isOwnConnData": true
    }],
    "totalUsedQuota": 0,
    "remainQuota": 300
  }
}
```









`moomoo::u32_t GetSubInfo(const Qot_GetSubInfo::Request &stReq);`  
`virtual void OnReply_GetSubInfo(moomoo::u32_t nSerialNo, const Qot_GetSubInfo::Response &stRsp) = 0;`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
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

        // construct request message
        Qot_GetSubInfo::Request req;
        Qot_GetSubInfo::C2S *c2s = req.mutable_c2s();

        m_GetSubInfoSerialNo = m_pQotApi->GetSubInfo(req);
        cout << "Request GetSubInfo SerialNo: " << m_GetSubInfoSerialNo << endl;
    }

    virtual void OnReply_GetSubInfo(moomoo::u32_t nSerialNo, const Qot_GetSubInfo::Response &stRsp){
        if(nSerialNo == m_GetSubInfoSerialNo)
        {
            cout << "OnReply_GetSubInfo SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetSubInfoSerialNo;
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
Request GetSubInfo SerialNo: 4
OnReply_GetSubInfo SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "connSubInfoList": [
   {
    "usedQuota": 0,
    "isOwnConnData": true
   }
  ],
  "totalUsedQuota": 1,
  "remainQuota": 299
 }
}
```









`GetSubInfo(req);`

- **Description**

  Get subscription information

- **Parameters**



``` protobuf
message C2S
{
    optional bool isReqAllConn = 1; //Whether to return the subscription status of all connections. Default by False, and return only the information of the current connection.
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message S2C
{
    repeated Qot_Common.ConnSubInfo connSubInfoList = 1; //Single connection subscription information
    required int32 totalUsedQuota = 2; //Subscription quota used by OpenD
    required int32 remainQuota = 3; //Remaining subscription quota from OpenD
}


message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of subscription information, refer to
>   [ConnSubInfo](/moomoo-api-doc/en/quote/quote.html#3216)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmtWebsocket from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";

function GetSubInfo(){
    const { RetType } = Common;
    const { SubType, QotMarket } = Qot_Common;
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
                subTypeList: [ SubType.SubType_OrderBook ],
                isSubOrUnSub: true,
                isRegOrUnRegPush: true, 
                },
            }).then((res) => { 

                const req = {
                    c2s: {
                        isReqAllConn: true,
                    },
                };

                websocket.GetSubInfo(req)
                .then((res) => { 
                    let { errCode, retMsg, retType,s2c } = res
                    if(retType == RetType.RetType_Succeed){
                        console.log("GetSubInfo: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                        console.log("GetSubInfo:", JSON.stringify(s2c)); 
                    } else {
                        console.log("GetSubInfo: error")
                    }
                })
                .catch((error) => {
                    console.log(error)
                    if ("retMsg" in error) {
                        console.log("error:", error.retMsg);
                    }
                });

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
GetSubInfo: errCode 0, retMsg , retType 0
GetSubInfo: {"connSubInfoList":[{"subInfoList":[{"subType":2,"securityList":[{"market":1,"code":"00700"}]}],"usedQuota":1,"isOwnConnData":true}],"totalUsedQuota":1,"remainQuota":99}
stop
```



















