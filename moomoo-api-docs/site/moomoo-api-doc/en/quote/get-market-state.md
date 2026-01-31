



# <a href="#1718" class="header-anchor">#</a> Get Market Status of Securities









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_market_state(code_list)`

- **Description**

  Get market status of underlying security

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
  <td style="text-align: left;">A list of security codes that need to
  query for market status.
  
    
  
  
   
  
  Data type of elements in the list is str.
  
  
  
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
  <td>If ret == RET_OK, market status data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Market status data format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | code | str | Security code. |
    | stock_name | str | Security name. |
    | market_state | [MarketState](/moomoo-api-doc/en/quote/quote.html#8663) | Market state. |

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_market_state(['SZ.000001', 'HK.00700'])
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code         stock_name   market_state
0  SZ.000001    Ping An Bank  AFTERNOON
1  HK.00700     Tencent       AFTERNOON
```









## <a href="#5873" class="header-anchor">#</a> Qot_GetMarketState.proto

- **Description**

  Get the market status of the specified target

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3223





`uint GetMarketState(QotGetMarketState.Request req);`  
`virtual void OnReply_GetMarketState(FTAPI_Conn client, uint nSerialNo, QotGetMarketState.Response rsp);`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
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
        QotGetMarketState.C2S c2s = QotGetMarketState.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetMarketState.Request req = QotGetMarketState.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetMarketState(req);
        Console.Write("Send QotGetMarketState: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetMarketState(FTAPI_Conn client, uint nSerialNo, QotGetMarketState.Response rsp)
    {
        Console.Write("Reply: QotGetMarketState: {0}\n", nSerialNo);
        Console.Write("code: {0} , name: {1}\n", rsp.S2C.MarketInfoListList[0].Security.Code,
            rsp.S2C.MarketInfoListList[0].Name);
        Console.Write("marketState: {0}\n", rsp.S2C.MarketInfoListList[0].MarketState);
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
Qot onInitConnect: ret=0 desc= connID=6825681116823902476
Send QotGetMarketState: 3
Reply: QotGetMarketState: 3
code: 00700 , name: Tencent
marketState: 5
```









`int getMarketState(QotGetMarketState.Request req);`  
`void onReply_GetMarketState(FTAPI_Conn client, int nSerialNo, QotGetMarketState.Response rsp);`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
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
        QotGetMarketState.C2S c2s = QotGetMarketState.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetMarketState.Request req = QotGetMarketState.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getMarketState(req);
        System.out.printf("Send QotGetMarketState: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetMarketState(FTAPI_Conn client, int nSerialNo, QotGetMarketState.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetMarketState failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetMarketState: %s\n", json);
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
Send QotGetMarketState: 2
Receive QotGetMarketState: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "marketInfoList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "name": "Tencent",
      "marketState": 6
    }]
  }
}
```









`Futu::u32_t GetMarketState(const Qot_GetMarketState::Request &stReq);`  
`virtual void OnReply_GetMarketState(Futu::u32_t nSerialNo, const Qot_GetMarketState::Response &stRsp) = 0;`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
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
        Qot_GetMarketState::Request req;
        Qot_GetMarketState::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetMarketStateSerialNo = m_pQotApi->GetMarketState(req);
        cout << "Request GetMarketState SerialNo: " << m_GetMarketStateSerialNo << endl;
    }

    virtual void OnReply_GetMarketState(Futu::u32_t nSerialNo, const Qot_GetMarketState::Response &stRsp){
        if(nSerialNo == m_GetMarketStateSerialNo)
        {
            cout << "OnReply_GetMarketState SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetMarketStateSerialNo;
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
Request GetMarketState SerialNo: 4
OnReply_GetMarketState SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "marketInfoList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "name": "Tencent",
    "marketState": 5
   }
  ]
 }
}
```









`GetMarketState(req);`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetMarketState(){
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
                },
            };
            websocket.GetMarketState(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("MarketState: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
MarketState: errCode 0, retMsg , retType 0
{
  "marketInfoList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "name": "Tencent",
    "marketState": 3
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- The maximum number of stock codes for each request is 400.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_market_state(code_list)`

- **Description**

  Get market status of underlying security

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
  <td style="text-align: left;">A list of security codes that need to
  query for market status.
  
    
  
  
   
  
  Data type of elements in the list is str.
  
  
  
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
  <td>If ret == RET_OK, market status data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Market status data format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | code | str | Security code. |
    | stock_name | str | Security name. |
    | market_state | [MarketState](/moomoo-api-doc/en/quote/quote.html#8663) | Market state. |

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_market_state(['SZ.000001', 'HK.00700'])
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code         stock_name   market_state
0  SZ.000001    Ping An Bank  AFTERNOON
1  HK.00700     Tencent       AFTERNOON
```









## <a href="#5873-2" class="header-anchor">#</a> Qot_GetMarketState.proto

- **Description**

  Get the market status of the specified target

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3223





`uint GetMarketState(QotGetMarketState.Request req);`  
`virtual void OnReply_GetMarketState(FTAPI_Conn client, uint nSerialNo, QotGetMarketState.Response rsp);`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
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
        QotGetMarketState.C2S c2s = QotGetMarketState.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetMarketState.Request req = QotGetMarketState.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetMarketState(req);
        Console.Write("Send QotGetMarketState: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetMarketState(MMAPI_Conn client, uint nSerialNo, QotGetMarketState.Response rsp)
    {
        Console.Write("Reply: QotGetMarketState: {0}\n", nSerialNo);
        Console.Write("code: {0} , name: {1}\n", rsp.S2C.MarketInfoListList[0].Security.Code,
            rsp.S2C.MarketInfoListList[0].Name);
        Console.Write("marketState: {0}\n", rsp.S2C.MarketInfoListList[0].MarketState);
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
Qot onInitConnect: ret=0 desc= connID=6825681116823902476
Send QotGetMarketState: 3
Reply: QotGetMarketState: 3
code: 00700 , name: Tencent
marketState: 5
```









`int getMarketState(QotGetMarketState.Request req);`  
`void onReply_GetMarketState(MMAPI_Conn client, int nSerialNo, QotGetMarketState.Response rsp);`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
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
        QotGetMarketState.C2S c2s = QotGetMarketState.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetMarketState.Request req = QotGetMarketState.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getMarketState(req);
        System.out.printf("Send QotGetMarketState: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetMarketState(MMAPI_Conn client, int nSerialNo, QotGetMarketState.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetMarketState failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetMarketState: %s\n", json);
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
Send QotGetMarketState: 2
Receive QotGetMarketState: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "marketInfoList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "name": "Tencent",
      "marketState": 6
    }]
  }
}
```









`moomoo::u32_t GetMarketState(const Qot_GetMarketState::Request &stReq);`  
`virtual void OnReply_GetMarketState(moomoo::u32_t nSerialNo, const Qot_GetMarketState::Response &stRsp) = 0;`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
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
        Qot_GetMarketState::Request req;
        Qot_GetMarketState::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetMarketStateSerialNo = m_pQotApi->GetMarketState(req);
        cout << "Request GetMarketState SerialNo: " << m_GetMarketStateSerialNo << endl;
    }

    virtual void OnReply_GetMarketState(moomoo::u32_t nSerialNo, const Qot_GetMarketState::Response &stRsp){
        if(nSerialNo == m_GetMarketStateSerialNo)
        {
            cout << "OnReply_GetMarketState SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetMarketStateSerialNo;
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
Request GetMarketState SerialNo: 4
OnReply_GetMarketState SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "marketInfoList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "name": "Tencent",
    "marketState": 5
   }
  ]
 }
}
```









`GetMarketState(req);`

- **Description**

  Get market status of underlying security

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security list
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
message MarketInfo
{
    required Qot_Common.Security security = 1; //Security code
    required string name = 2; //Security name
    required int32 marketState = 3; //Qot_Common.QotMarketState, market state
}

message S2C
{
    repeated MarketInfo marketInfoList = 1; //Market status information
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
> - For enumeration of market status, refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "fmoomoo-api/proto";
import beautify from "js-beautify";

function QotGetMarketState(){
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
                },
            };
            websocket.GetMarketState(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("MarketState: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
MarketState: errCode 0, retMsg , retType 0
{
  "marketInfoList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "name": "Tencent",
    "marketState": 3
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- The maximum number of stock codes for each request is 400.













