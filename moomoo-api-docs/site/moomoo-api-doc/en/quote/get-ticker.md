



# <a href="#4601" class="header-anchor">#</a> Get Real-time Tick-by-Tick









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_rt_ticker(code, num=500)`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**

  | Parameter | Type | Description                    |
  |:----------|:-----|:-------------------------------|
  | code      | str  | Stock code.                    |
  | num       | int  | Number of recent tick-by-tick. |

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
  <td>If ret == RET_OK, tick-by-tick data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Tick-by-tick data format as follows:
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
    <td style="text-align: left;">sequence</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Sequence number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Transaction time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss:xxx<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.
    
      
    
    
     
    
    shares
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ticker_direction</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#832">TickerDirect</a></td>
    <td style="text-align: left;">Tick-By-Tick direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9844">TickerType</a></td>
    <td style="text-align: left;">Tick-By-Tick type.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.TICKER], subscribe_push=False, session=Session.ALL)
# First subscribe to each type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
     ret, data = quote_ctx.get_rt_ticker('US.AAPL', 2) # Get the last 2 transactions of Hong Kong stocks 00700
     if ret == RET_OK:
         print(data)
         print(data['turnover'][0]) # Take the first transaction amount
         print(data['turnover'].values.tolist()) # Convert to list
     else:
         print('error:', data)
else:
     print('subscription failed', err_message)
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code name                     time   price  volume  turnover ticker_direction             sequence     type
0  US.AAPL   APPLE  2025-04-07 05:50:23.745  181.70       2    363.40          NEUTRAL  7490506385373790208  ODD_LOT
1  US.AAPL   APPLE  2025-04-07 05:50:24.170  181.73       1    181.73          NEUTRAL  7490506389668757504  ODD_LOT
363.4
[363.4, 181.73]
```









## <a href="#1113" class="header-anchor">#</a> Qot_GetTicker.proto

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3010





`uint GetTicker(QotGetTicker.Request req);`  
`virtual void OnReply_GetTicker(FTAPI_Conn client, uint nSerialNo, QotGetTicker.Response rsp);`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Ticker)
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
        QotGetTicker.C2S c2s = QotGetTicker.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetMaxRetNum(10)
                .Build();
        QotGetTicker.Request req = QotGetTicker.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetTicker(req);
        Console.Write("Send QotGetTicker: {0}\n", seqNo);
    }

    public void OnReply_GetTicker(FTAPI_Conn client, uint nSerialNo, QotGetTicker.Response rsp)
    {
        Console.Write("Reply: QotGetTicker: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.TickerListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825674961091539442
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetTicker: 4
Reply: QotGetTicker: 4
price: 456
```









`int getTicker(QotGetTicker.Request req);`  
`void onReply_GetTicker(FTAPI_Conn client, int nSerialNo, QotGetTicker.Response rsp);`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
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
                .addSubTypeList(QotCommon.SubType.SubType_Ticker_VALUE)
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
        QotGetTicker.C2S c2s = QotGetTicker.C2S.newBuilder()
                .setSecurity(sec)
                .setMaxRetNum(10)
                .build();
        QotGetTicker.Request req = QotGetTicker.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getTicker(req);
        System.out.printf("Send QotGetTicker: %d\n", seqNo);
    }

    @Override
    public void onReply_GetTicker(FTAPI_Conn client, int nSerialNo, QotGetTicker.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetTicker failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetTicker: %s\n", json);
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
Send QotGetTicker: 3
Receive QotGetTicker: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "tickerList": [{
      "time": "2021-06-24 15:59:55",
      "sequence": "6977267122170775380",
      "dir": 1,
      "price": 583.5,
      "volume": "100",
      "turnover": 58350.0,
      "recvTime": 0.0,
      "type": 1,
      "typeSign": 32,
      "timestamp": 1.624521595E9
    }, ... {
      "time": "2021-06-24 16:08:10",
      "sequence": "6977269248179586909",
      "dir": 3,
      "price": 583.0,
      "volume": "1131400",
      "turnover": 6.596062E8,
      "recvTime": 0.0,
      "type": 7,
      "typeSign": 85,
      "timestamp": 1.62452209E9
    }]
  }
}
```









`Futu::u32_t GetTicker(const Qot_GetTicker::Request &stReq);`  
`virtual void OnReply_GetTicker(Futu::u32_t nSerialNo, const Qot_GetTicker::Response &stRsp) = 0;`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Ticker);
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
            Qot_GetTicker::Request req;
            Qot_GetTicker::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            c2s->set_maxretnum(10);

            m_GetTickerSerialNo = m_pQotApi->GetTicker(req);
            cout << "Request GetTicker SerialNo: " << m_GetTickerSerialNo << endl;
        }
    }

    virtual void OnReply_GetTicker(Futu::u32_t nSerialNo, const Qot_GetTicker::Response &stRsp){
        if(nSerialNo == m_GetTickerSerialNo)
        {
            cout << "OnReply_GetTicker SerialNo: " << nSerialNo << endl; 
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
    Futu::u32_t m_GetTickerSerialNo;
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
Request GetTicker SerialNo: 4
OnReply_GetTicker SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "tickerList": [
   {
    "time": "2021-06-09 14:13:11",
    "sequence": "6971673339584584057",
    "dir": 3,
    "price": 602.5,
    "volume": "15",
    "turnover": 9037.5,
    "recvTime": 0,
    "type": 6,
    "typeSign": 68,
    "timestamp": 1623219191
   },
...
   {
    "time": "2021-06-09 14:13:20",
    "sequence": "6971673378239289730",
    "dir": 1,
    "price": 600.5,
    "volume": "1000",
    "turnover": 600500,
    "recvTime": 0,
    "type": 1,
    "typeSign": 32,
    "timestamp": 1623219200
   }
  ]
 }
}
```









`GetTicker(req);`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetTicker(){
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
                subTypeList: [ SubType.SubType_Ticker ], 
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
                        maxRetNum: 3,
                    },
                };
                
                websocket.GetTicker(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("Ticker: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Ticker: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "tickerList": [{
    "time": "2021-09-09 15:59:59",
    "sequence": "7005840697777510727",
    "dir": 2,
    "price": 481.2,
    "volume": "100",
    "turnover": 48120,
    "recvTime": 0,
    "type": 1,
    "typeSign": 32,
    "timestamp": 1631174399
  }, {
    "time": "2021-09-09 16:05:24",
    "sequence": "7005842093641881928",
    "dir": 3,
    "price": 476,
    "volume": "42",
    "turnover": 19992,
    "recvTime": 0,
    "type": 6,
    "typeSign": 68,
    "timestamp": 1631174724
  }, {
    "time": "2021-09-09 16:08:12",
    "sequence": "7005842815196387657",
    "dir": 3,
    "price": 480,
    "volume": "4561200",
    "turnover": 2189376000,
    "recvTime": 0,
    "type": 7,
    "typeSign": 85,
    "timestamp": 1631174892
  }]
}
stop
```











Interface Limitations

- You can get up to the latest 1000 tick-by-tick data, more historical
  tick-by-tick data is not yet available
- Under the authority of LV1 HK futures and options market, tick-by-tick
  data is not available





Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Tick-By-Tick
  Callback](/moomoo-api-doc/en/quote/update-ticker.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_rt_ticker(code, num=500)`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**

  | Parameter | Type | Description                    |
  |:----------|:-----|:-------------------------------|
  | code      | str  | Stock code.                    |
  | num       | int  | Number of recent tick-by-tick. |

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
  <td>If ret == RET_OK, tick-by-tick data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Tick-by-tick data format as follows:
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
    <td style="text-align: left;">sequence</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Sequence number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Transaction time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.
    
      
    
    
     
    
    shares
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount.</td>
    </tr>
    <tr>
    <td style="text-align: left;">ticker_direction</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#832">TickerDirect</a></td>
    <td style="text-align: left;">Tick-By-Tick direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9844">TickerType</a></td>
    <td style="text-align: left;">Tick-By-Tick type.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.TICKER], subscribe_push=False, session=Session.ALL)
# First subscribe to each type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
     ret, data = quote_ctx.get_rt_ticker('US.AAPL', 2) # Get the last 2 transactions of Hong Kong stocks 00700
     if ret == RET_OK:
         print(data)
         print(data['turnover'][0]) # Take the first transaction amount
         print(data['turnover'].values.tolist()) # Convert to list
     else:
         print('error:', data)
else:
     print('subscription failed', err_message)
quote_ctx.close() # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code name                     time   price  volume  turnover ticker_direction             sequence     type
0  US.AAPL   APPLE  2025-04-07 05:50:23.745  181.70       2    363.40          NEUTRAL  7490506385373790208  ODD_LOT
1  US.AAPL   APPLE  2025-04-07 05:50:24.170  181.73       1    181.73          NEUTRAL  7490506389668757504  ODD_LOT
363.4
[363.4, 181.73]
```









## <a href="#1113-2" class="header-anchor">#</a> Qot_GetTicker.proto

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3010





`uint GetTicker(QotGetTicker.Request req);`  
`virtual void OnReply_GetTicker(MMAPI_Conn client, uint nSerialNo, QotGetTicker.Response rsp);`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Ticker)
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
        QotGetTicker.C2S c2s = QotGetTicker.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetMaxRetNum(10)
                .Build();
        QotGetTicker.Request req = QotGetTicker.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetTicker(req);
        Console.Write("Send QotGetTicker: {0}\n", seqNo);
    }

    public void OnReply_GetTicker(MMAPI_Conn client, uint nSerialNo, QotGetTicker.Response rsp)
    {
        Console.Write("Reply: QotGetTicker: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.TickerListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825674961091539442
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetTicker: 4
Reply: QotGetTicker: 4
price: 456
```









`int getTicker(QotGetTicker.Request req);`  
`void onReply_GetTicker(MMAPI_Conn client, int nSerialNo, QotGetTicker.Response rsp);`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
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
                .addSubTypeList(QotCommon.SubType.SubType_Ticker_VALUE)
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
        QotGetTicker.C2S c2s = QotGetTicker.C2S.newBuilder()
                .setSecurity(sec)
                .setMaxRetNum(10)
                .build();
        QotGetTicker.Request req = QotGetTicker.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getTicker(req);
        System.out.printf("Send QotGetTicker: %d\n", seqNo);
    }

    @Override
    public void onReply_GetTicker(MMAPI_Conn client, int nSerialNo, QotGetTicker.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetTicker failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetTicker: %s\n", json);
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
Send QotGetTicker: 3
Receive QotGetTicker: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "tickerList": [{
      "time": "2021-06-24 15:59:55",
      "sequence": "6977267122170775380",
      "dir": 1,
      "price": 583.5,
      "volume": "100",
      "turnover": 58350.0,
      "recvTime": 0.0,
      "type": 1,
      "typeSign": 32,
      "timestamp": 1.624521595E9
    }, ... {
      "time": "2021-06-24 16:08:10",
      "sequence": "6977269248179586909",
      "dir": 3,
      "price": 583.0,
      "volume": "1131400",
      "turnover": 6.596062E8,
      "recvTime": 0.0,
      "type": 7,
      "typeSign": 85,
      "timestamp": 1.62452209E9
    }]
  }
}
```









`moomoo::u32_t GetTicker(const Qot_GetTicker::Request &stReq);`  
`virtual void OnReply_GetTicker(moomoo::u32_t nSerialNo, const Qot_GetTicker::Response &stRsp) = 0;`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Ticker);
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

            // construct request message
            Qot_GetTicker::Request req;
            Qot_GetTicker::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            c2s->set_maxretnum(10);

            m_GetTickerSerialNo = m_pQotApi->GetTicker(req);
            cout << "Request GetTicker SerialNo: " << m_GetTickerSerialNo << endl;
        }
    }

    virtual void OnReply_GetTicker(moomoo::u32_t nSerialNo, const Qot_GetTicker::Response &stRsp){
        if(nSerialNo == m_GetTickerSerialNo)
        {
            cout << "OnReply_GetTicker SerialNo: " << nSerialNo << endl; 
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
    moomoo::u32_t m_GetTickerSerialNo;
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
Request GetTicker SerialNo: 4
OnReply_GetTicker SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "tickerList": [
   {
    "time": "2021-06-09 14:13:11",
    "sequence": "6971673339584584057",
    "dir": 3,
    "price": 602.5,
    "volume": "15",
    "turnover": 9037.5,
    "recvTime": 0,
    "type": 6,
    "typeSign": 68,
    "timestamp": 1623219191
   },
...
   {
    "time": "2021-06-09 14:13:20",
    "sequence": "6971673378239289730",
    "dir": 1,
    "price": 600.5,
    "volume": "1000",
    "turnover": 600500,
    "recvTime": 0,
    "type": 1,
    "typeSign": 32,
    "timestamp": 1623219200
   }
  ]
 }
}
```









`GetTicker(req);`

- **Description**

  To get real-time tick-by-tick of subscribed stocks. (Require real-time
  data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 maxRetNum = 2; //Maximum number of items returned, the actual number of returns may not as much as the maximium number, up to 1000
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
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // Stock name
    repeated Qot_Common.Ticker tickerList = 2; //Tick-by-tick data struct
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
> - For the structure of each transaction, refer to
>   [Ticker](/moomoo-api-doc/en/quote/quote.html#2975)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetTicker(){
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
                subTypeList: [ SubType.SubType_Ticker ], 
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
                        maxRetNum: 3,
                    },
                };
                
                websocket.GetTicker(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("Ticker: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Ticker: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "tickerList": [{
    "time": "2021-09-09 15:59:59",
    "sequence": "7005840697777510727",
    "dir": 2,
    "price": 481.2,
    "volume": "100",
    "turnover": 48120,
    "recvTime": 0,
    "type": 1,
    "typeSign": 32,
    "timestamp": 1631174399
  }, {
    "time": "2021-09-09 16:05:24",
    "sequence": "7005842093641881928",
    "dir": 3,
    "price": 476,
    "volume": "42",
    "turnover": 19992,
    "recvTime": 0,
    "type": 6,
    "typeSign": 68,
    "timestamp": 1631174724
  }, {
    "time": "2021-09-09 16:08:12",
    "sequence": "7005842815196387657",
    "dir": 3,
    "price": 480,
    "volume": "4561200",
    "turnover": 2189376000,
    "recvTime": 0,
    "type": 7,
    "typeSign": 85,
    "timestamp": 1631174892
  }]
}
stop
```











Interface Limitations

- You can get up to the latest 1000 tick-by-tick data, more historical
  tick-by-tick data is not yet available
- Under the authority of LV1 HK futures and options market, tick-by-tick
  data is not available





Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Tick-By-Tick
  Callback](/moomoo-api-doc/en/quote/update-ticker.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).













