



# <a href="#5589" class="header-anchor">#</a> Get Trading Calendar









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`request_trading_days(market=None, start=None, end=None, code=None)`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

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
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#6587">TradeDateMarket</a></td>
  <td style="text-align: left;">Market type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start date.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2018-01-01".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End date.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2018-01-01".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Security code.</td>
  </tr>
  </tbody>
  </table>

  Note: when both *market* and *code* exist, *market* is ignored and
  only *code* is effective.

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 365 days before ***end***. |
    | str | None | ***end*** is 365 days after ***start***. |
    | None | None | ***start*** is 365 days before, ***end*** is the current date. |

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
  <td>list</td>
  <td>If ret == RET_OK, data of the trading day is returned. Data type of
  elements in the list is dict.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data of the trading day's format as follows:
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
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    Format: yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trade_date_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8930">TradeDateType</a></td>
    <td style="text-align: left;">Trading day type.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.request_trading_days(TradeDateMarket.HK, start='2020-04-01', end='2020-04-10')
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
[{'time': '2020-04-01', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-02', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-03', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-06', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-07', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-08', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-09', 'trade_date_type': 'WHOLE'}]
```









## <a href="#6520" class="header-anchor">#</a> Qot_RequestTradeDate.proto

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3219





`uint RequestTradeDate(QotRequestTradeDate.Request req);`  
`virtual void OnReply_RequestTradeDate(FTAPI_Conn client, uint nSerialNo, QotRequestTradeDate.Response rsp);`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
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
        QotRequestTradeDate.C2S c2s = QotRequestTradeDate.C2S.CreateBuilder()
            .SetMarket((int)QotCommon.TradeDateMarket.TradeDateMarket_HK)
            .SetBeginTime("2021-07-01")
            .SetEndTime("2021-07-05")
            .SetSecurity(sec)
            .Build();
        QotRequestTradeDate.Request req = QotRequestTradeDate.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestTradeDate(req);
        Console.Write("Send QotRequestTradeDate: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_RequestTradeDate(FTAPI_Conn client, uint nSerialNo, QotRequestTradeDate.Response rsp) {
        Console.Write("Reply: QotRequestTradeDate: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("time: {0}, tradeDateType: {1} \n", rsp.S2C.TradeDateListList[0].Time, rsp.S2C.TradeDateListList[0].TradeDateType);
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
Qot onInitConnect: ret=0 desc= connID=6826779607624163711
Send QotRequestTradeDate: 3
Reply: QotRequestTradeDate: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  tradeDateList {
    time: "2021-07-02"
    timestamp: 1625155200
    tradeDateType: 0
  }
  tradeDateList {
    time: "2021-07-05"
    timestamp: 1625414400
    tradeDateType: 0
  }
}

time: 2021-07-02, tradeDateType: 0
```









`int requestTradeDate(QotRequestTradeDate.Request req);`  
`void onReply_RequestTradeDate(FTAPI_Conn client, int nSerialNo, QotRequestTradeDate.Response rsp);`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
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
        QotRequestTradeDate.C2S c2s = QotRequestTradeDate.C2S.newBuilder()
            .setMarket(QotCommon.TradeDateMarket.TradeDateMarket_HK)
            .setBeginTime("2020-08-01")
            .setEndTime("2020-09-01")
            .setSecurity(sec)
            .build();
        QotRequestTradeDate.Request req = QotRequestTradeDate.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestTradeDate(req);
        System.out.printf("Send QotRequestTradeDate: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestTradeDate(FTAPI_Conn client, int nSerialNo, QotRequestTradeDate.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestTradeDate failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestTradeDate: %s\n", json);
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
Send QotRequestTradeDate: 2
Receive QotRequestTradeDate: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "tradeDateList": [{
      "time": "2020-08-03",
      "timestamp": 1.596384E9,
      "tradeDateType": 0
    }, ... {
      "time": "2020-09-01",
      "timestamp": 1.5988896E9,
      "tradeDateType": 0
    }]
  }
}
```









`Futu::u32_t RequestTradeDate(const Qot_RequestTradeDate::Request &stReq);`  
`virtual void OnReply_RequestTradeDate(Futu::u32_t nSerialNo, const Qot_RequestTradeDate::Response &stRsp) = 0;`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
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
        Qot_RequestTradeDate::Request req;
        Qot_RequestTradeDate::C2S *c2s = req.mutable_c2s();
        c2s->set_market((int)Qot_Common::TradeDateMarket::TradeDateMarket_HK);
        c2s->set_begintime("2021-07-01");
        c2s->set_endtime("2021-07-05");
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market((int)Qot_Common::QotMarket::QotMarket_HK_Security);
        
        m_RequestTradeDateSerialNo = m_pQotApi->RequestTradeDate(req);
        cout << "Request RequestTradeDate SerialNo: " << m_RequestTradeDateSerialNo << endl;
    }

    virtual void OnReply_RequestTradeDate(Futu::u32_t nSerialNo, const Qot_RequestTradeDate::Response &stRsp){
        if(nSerialNo == m_RequestTradeDateSerialNo)
        {
            cout << "OnReply_RequestTradeDate SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;
    
    Futu::u32_t m_RequestTradeDateSerialNo;
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



``` cpp
connect
Request RequestTradeDate SerialNo: 3
OnReply_RequestTradeDate SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "tradeDateList": [
   {
    "time": "2021-07-02",
    "timestamp": 1625155200,
    "tradeDateType": 0
   },
   {
    "time": "2021-07-05",
    "timestamp": 1625414400,
    "tradeDateType": 0
   }
  ]
 }
}
```









`RequestTradeDate(req);`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotRequestTradeDate(){
    const { RetType } = Common
    const { TradeDateMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    market: TradeDateMarket.TradeDateMarket_HK,
                    beginTime: "2021-08-05",
                    endTime: "2021-08-10",
                },
            };

            websocket.RequestTradeDate(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("TradeDate: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
TradeDate: errCode 0, retMsg , retType 0
{
  "tradeDateList": [{
    "time": "2021-08-05",
    "timestamp": 1628092800,
    "tradeDateType": 0
  }, {
    "time": "2021-08-06",
    "timestamp": 1628179200,
    "tradeDateType": 0
  }, {
    "time": "2021-08-09",
    "timestamp": 1628438400,
    "tradeDateType": 0
  }, {
    "time": "2021-08-10",
    "timestamp": 1628524800,
    "tradeDateType": 0
  }]
}
stop
```











Interface Limitations

- A maximum of 30 requests per 30 seconds
- The historical trading calendar provides data for the past 10 years,
  and the future trading calendar is available until December 31 this
  year.
  

  
  

  

  
  
  

  For example: today's date is July 6, 2021, and the period only from
  2011-07-06 to 2021-12-31 is provided.

  

  

  

  

  。











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`request_trading_days(market=None, start=None, end=None, code=None)`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

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
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#6587">TradeDateMarket</a></td>
  <td style="text-align: left;">Market type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start date.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2018-01-01".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End date.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2018-01-01".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Security code.</td>
  </tr>
  </tbody>
  </table>

  Note: when both *market* and *code* exist, *market* is ignored and
  only *code* is effective.

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 365 days before ***end***. |
    | str | None | ***end*** is 365 days after ***start***. |
    | None | None | ***start*** is 365 days before, ***end*** is the current date. |

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
  <td>list</td>
  <td>If ret == RET_OK, data of the trading day is returned. Data type of
  elements in the list is dict.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data of the trading day's format as follows:
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
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    Format: yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trade_date_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8930">TradeDateType</a></td>
    <td style="text-align: left;">Trading day type.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.request_trading_days(TradeDateMarket.HK, start='2020-04-01', end='2020-04-10')
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
[{'time': '2020-04-01', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-02', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-03', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-06', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-07', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-08', 'trade_date_type': 'WHOLE'}, {'time': '2020-04-09', 'trade_date_type': 'WHOLE'}]
```









## <a href="#6520-2" class="header-anchor">#</a> Qot_RequestTradeDate.proto

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3219





`uint RequestTradeDate(QotRequestTradeDate.Request req);`  
`virtual void OnReply_RequestTradeDate(MMAPI_Conn client, uint nSerialNo, QotRequestTradeDate.Response rsp);`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
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
        QotRequestTradeDate.C2S c2s = QotRequestTradeDate.C2S.CreateBuilder()
            .SetMarket((int)QotCommon.TradeDateMarket.TradeDateMarket_HK)
            .SetBeginTime("2021-07-01")
            .SetEndTime("2021-07-05")
            .SetSecurity(sec)
            .Build();
        QotRequestTradeDate.Request req = QotRequestTradeDate.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestTradeDate(req);
        Console.Write("Send QotRequestTradeDate: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_RequestTradeDate(MMAPI_Conn client, uint nSerialNo, QotRequestTradeDate.Response rsp) {
        Console.Write("Reply: QotRequestTradeDate: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("time: {0}, tradeDateType: {1} \n", rsp.S2C.TradeDateListList[0].Time, rsp.S2C.TradeDateListList[0].TradeDateType);
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
Qot onInitConnect: ret=0 desc= connID=6826779607624163711
Send QotRequestTradeDate: 3
Reply: QotRequestTradeDate: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  tradeDateList {
    time: "2021-07-02"
    timestamp: 1625155200
    tradeDateType: 0
  }
  tradeDateList {
    time: "2021-07-05"
    timestamp: 1625414400
    tradeDateType: 0
  }
}

time: 2021-07-02, tradeDateType: 0
```









`int requestTradeDate(QotRequestTradeDate.Request req);`  
`void onReply_RequestTradeDate(MMAPI_Conn client, int nSerialNo, QotRequestTradeDate.Response rsp);`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
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
        QotRequestTradeDate.C2S c2s = QotRequestTradeDate.C2S.newBuilder()
            .setMarket(QotCommon.TradeDateMarket.TradeDateMarket_HK)
            .setBeginTime("2020-08-01")
            .setEndTime("2020-09-01")
            .setSecurity(sec)
            .build();
        QotRequestTradeDate.Request req = QotRequestTradeDate.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestTradeDate(req);
        System.out.printf("Send QotRequestTradeDate: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestTradeDate(MMAPI_Conn client, int nSerialNo, QotRequestTradeDate.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestTradeDate failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestTradeDate: %s\n", json);
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
Send QotRequestTradeDate: 2
Receive QotRequestTradeDate: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "tradeDateList": [{
      "time": "2020-08-03",
      "timestamp": 1.596384E9,
      "tradeDateType": 0
    }, ... {
      "time": "2020-09-01",
      "timestamp": 1.5988896E9,
      "tradeDateType": 0
    }]
  }
}
```









`moomoo::u32_t RequestTradeDate(const Qot_RequestTradeDate::Request &stReq);`  
`virtual void OnReply_RequestTradeDate(moomoo::u32_t nSerialNo, const Qot_RequestTradeDate::Response &stRsp) = 0;`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
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
        Qot_RequestTradeDate::Request req;
        Qot_RequestTradeDate::C2S *c2s = req.mutable_c2s();
        c2s->set_market((int)Qot_Common::TradeDateMarket::TradeDateMarket_HK);
        c2s->set_begintime("2021-07-01");
        c2s->set_endtime("2021-07-05");
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market((int)Qot_Common::QotMarket::QotMarket_HK_Security);
        
        m_RequestTradeDateSerialNo = m_pQotApi->RequestTradeDate(req);
        cout << "Request RequestTradeDate SerialNo: " << m_RequestTradeDateSerialNo << endl;
    }

    virtual void OnReply_RequestTradeDate(moomoo::u32_t nSerialNo, const Qot_RequestTradeDate::Response &stRsp){
        if(nSerialNo == m_RequestTradeDateSerialNo)
        {
            cout << "OnReply_RequestTradeDate SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;
    
    moomoo::u32_t m_RequestTradeDateSerialNo;
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



``` cpp
connect
Request RequestTradeDate SerialNo: 3
OnReply_RequestTradeDate SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "tradeDateList": [
   {
    "time": "2021-07-02",
    "timestamp": 1625155200,
    "tradeDateType": 0
   },
   {
    "time": "2021-07-05",
    "timestamp": 1625414400,
    "tradeDateType": 0
   }
  ]
 }
}
```









`RequestTradeDate(req);`

- **Description**

  Request trading calendar via market or code.  
  Note that the trading day is obtained by excluding weekends and
  holidays from natural days, and the temporary market closed data is
  not excluded.

- **Parameters**



``` protobuf
message C2S
{
    // When both market and code exist, market is ignored and only code is effective.
    required int32 market = 1; //Qot_Common.TradeDateMarket, the market to be queried
    required string beginTime = 2; //start time string (Format: yyyy-MM-dd)
    required string endTime = 3; //end time string (Format: yyyy-MM-dd)
    optional Qot_Common.Security security = 4; // Security code
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For enumerations of market type, refer to
>   [TradeDateMarket](/moomoo-api-doc/en/quote/quote.html#6587)

- **Return**



``` protobuf
message TradeDate
{
    required string time = 1; //time string (Format: yyyy-MM-dd)
    optional double timestamp = 2; //time stamp
    optional int32 tradeDateType = 3; //Qot_Common.TradeDateType, transaction time type
}

message S2C
{
    repeated TradeDate tradeDateList = 1; //Trading day. Note that the trading day is obtained by excluding weekends and holidays from natural days, and the temporary market closed data is not excluded.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumerations of trading day type, refer to
>   [TradeDateType](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotRequestTradeDate(){
    const { RetType } = Common
    const { TradeDateMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    market: TradeDateMarket.TradeDateMarket_HK,
                    beginTime: "2021-08-05",
                    endTime: "2021-08-10",
                },
            };

            websocket.RequestTradeDate(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("TradeDate: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
TradeDate: errCode 0, retMsg , retType 0
{
  "tradeDateList": [{
    "time": "2021-08-05",
    "timestamp": 1628092800,
    "tradeDateType": 0
  }, {
    "time": "2021-08-06",
    "timestamp": 1628179200,
    "tradeDateType": 0
  }, {
    "time": "2021-08-09",
    "timestamp": 1628438400,
    "tradeDateType": 0
  }, {
    "time": "2021-08-10",
    "timestamp": 1628524800,
    "tradeDateType": 0
  }]
}
stop
```











Interface Limitations

- A maximum of 30 requests per 30 seconds
- The historical trading calendar provides data for the past 10 years,
  and the future trading calendar is available until December 31 this
  year.
  

  
  

  

  
  
  

  For example: today's date is July 6, 2021, and the period only from
  2011-07-06 to 2021-12-31 is provided.

  

  

  

  

  。













