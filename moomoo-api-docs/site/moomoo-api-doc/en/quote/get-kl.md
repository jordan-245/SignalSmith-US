



# <a href="#854" class="header-anchor">#</a> Get Real-time Candlestick









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_cur_kline(code, num, ktype=SubType.K_DAY, autype=AuType.QFQ)`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
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
  <td style="text-align: left;">num</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The number of candlesticks.
  
    
  
  
   
  
  Up to 1000.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">ktype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
  <td style="text-align: left;">Candlestick type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">autype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#7071">AuType</a></td>
  <td style="text-align: left;">Type of adjustment.</td>
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
  <td>If ret == RET_OK, IPO data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - IPO data format as follows:
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
    <td style="text-align: left;">time_key</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.
    
      
    
    
     
    
    This field is in decimal form, so 0.01 is equivalent to 1%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.
    
      
    
    
     
    
    The close of the previous trading day.<br />
    For efficiency reasons, the yesterday's close of the first data may be
    0.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.K_DAY], subscribe_push=False, session=Session.ALL)
# First subscribe to the candlestick type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK:  # Successfully subscribed
    ret, data = quote_ctx.get_cur_kline('US.AAPL', 2, SubType.K_DAY, AuType.QFQ)  # Get the latest 2 candlestick data of US.AAPL
    if ret == RET_OK:
        print(data)
        print(data['turnover_rate'][0])   # Take the first turnover rate
        print(data['turnover_rate'].values.tolist())   # Convert to list
    else:
        print('error:', data)
else:
    print('subscription failed', err_message)
quote_ctx.close()  # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code name             time_key    open   close    high     low     volume      turnover  pe_ratio  turnover_rate  last_close
0  US.AAPL   APPLE  2025-04-03 00:00:00  205.54  203.19  207.49  201.25  103419006  2.111773e+10    33.419        0.00689      223.89
1  US.AAPL   APPLE  2025-04-04 00:00:00  193.89  188.38  199.88  187.34  125910913  2.424473e+10    30.983        0.00838      203.19
0.00689
[0.00689, 0.00838]
```









## <a href="#7451" class="header-anchor">#</a> Qot_GetKL.proto

- **Description**

  To obtain real-time K line data of subscribed stocks, you must first
  subscribe.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3006





`uint GetKL(QotGetKL.Request req);`  
`virtual void OnReply_GetKL(FTAPI_Conn client, uint nSerialNo, QotGetKL.Response rsp);`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Qot, FTSPI_Conn {
    FTAPI_Qot qot = new FTAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1);  //Set client information
        qot.SetConnCallback(this);  //Set connection callback
        qot.SetQotCallback(this);   //Set transaction callback
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_KL_1Min)
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
        QotGetKL.C2S c2s = QotGetKL.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetKlType((int)QotCommon.KLType.KLType_1Min)
                .SetRehabType((int)QotCommon.RehabType.RehabType_Forward)
                .SetReqNum(50)
                .Build();
        QotGetKL.Request req = QotGetKL.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetKL(req);
        Console.Write("Send QotGetKL: {0}\n", seqNo);
    }

    public void OnReply_GetKL(FTAPI_Conn client, uint nSerialNo, QotGetKL.Response rsp)
    {
        Console.Write("Reply: QotGetKL: {0}\n", nSerialNo);
        Console.Write("lastClosePrice: {0}\n", rsp.S2C.KlListList[0].LastClosePrice);
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
Qot onInitConnect: ret=0 desc= connID=6825671203627466268
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetKL: 4
Reply: QotGetKL: 4
lastClosePrice: 458.6
```









`int getKL(QotGetKL.Request req);`  
`void onReply_GetKL(FTAPI_Conn client, int nSerialNo, QotGetKL.Response rsp);`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
                .addSubTypeList(QotCommon.SubType.SubType_KL_1Min_VALUE)
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
        QotGetKL.C2S c2s = QotGetKL.C2S.newBuilder()
                .setSecurity(sec)
                .setKlType(QotCommon.KLType.KLType_1Min_VALUE)
                .setRehabType(QotCommon.RehabType.RehabType_Forward_VALUE)
                .setReqNum(2)
                .build();
        QotGetKL.Request req = QotGetKL.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getKL(req);
        System.out.printf("Send QotGetKL: %d\n", seqNo);
    }

    @Override
    public void onReply_GetKL(FTAPI_Conn client, int nSerialNo, QotGetKL.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetKL failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetKL: %s\n", json);
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
Send QotGetKL: 3
Receive QotGetKL: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "klList": [{
      "time": "2021-06-24 15:59:00",
      "isBlank": false,
      "highPrice": 583.5,
      "openPrice": 583.0,
      "lowPrice": 583.0,
      "closePrice": 583.5,
      "lastClosePrice": 583.5,
      "volume": "37900",
      "turnover": 2.210525E7,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": 0.0,
      "timestamp": 1.62452154E9
    }, {
      "time": "2021-06-24 16:00:00",
      "isBlank": false,
      "highPrice": 583.5,
      "openPrice": 583.0,
      "lowPrice": 582.5,
      "closePrice": 583.0,
      "lastClosePrice": 583.5,
      "volume": "1197900",
      "turnover": 6.98392175E8,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": -0.08568980291345331,
      "timestamp": 1.6245216E9
    }]
  }
}
```









`Futu::u32_t GetKL(const Qot_GetKL::Request &stReq);`  
`virtual void OnReply_GetKL(Futu::u32_t nSerialNo, const Qot_GetKL::Response &stRsp) = 0;`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_KL_1Min);
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
            Qot_GetKL::Request req;
            Qot_GetKL::C2S *c2s = req.mutable_c2s();
            c2s->set_rehabtype(1);
            c2s->set_kltype(Qot_Common::KLType::KLType_1Min);
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            c2s->set_reqnum(10);

            m_GetKLSerialNo = m_pQotApi->GetKL(req);
            cout << "Request GetKL SerialNo: " << m_GetKLSerialNo << endl;
        }
    }

    virtual void OnReply_GetKL(Futu::u32_t nSerialNo, const Qot_GetKL::Response &stRsp){
        if(nSerialNo == m_GetKLSerialNo)
        {
            cout << "OnReply_GetKL SerialNo: " << nSerialNo << endl; 
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
    Futu::u32_t m_GetKLSerialNo;
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
Request GetKL SerialNo: 4
OnReply_GetKL SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "klList": [
   {
    "time": "2021-06-09 14:03:00",
    "isBlank": false,
    "highPrice": 602,
    "openPrice": 602,
    "lowPrice": 601.5,
    "closePrice": 601.5,
    "lastClosePrice": 601.5,
    "volume": "9500",
    "turnover": 5714700,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0,
    "timestamp": 1623218580
   },
...
   {
    "time": "2021-06-09 14:11:00",
    "isBlank": false,
    "highPrice": 601,
    "openPrice": 601,
    "lowPrice": 601,
    "closePrice": 601,
    "lastClosePrice": 601,
    "volume": "0",
    "turnover": 0,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0,
    "timestamp": 1623219060
   }
  ]
 }
}
```









`GetKL(req);`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetKL(){
    const { RetType } = Common
    const { SubType, QotMarket, RehabType, KLType } = Qot_Common
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
                subTypeList: [ SubType.SubType_KL_1Min ], 
                isSubOrUnSub: true,
                isRegOrUnRegPush: true, 
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                        rehabType: RehabType.RehabType_Forward,
                        klType: KLType.KLType_1Min,
                        security: {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                        reqNum: 2,
                    },
                };
                
                websocket.GetKL(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("KL: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
KL: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "klList": [{
    "time": "2021-09-09 15:59:00",
    "isBlank": false,
    "highPrice": 480.4,
    "openPrice": 480.2,
    "lowPrice": 479,
    "closePrice": 479.6,
    "lastClosePrice": 480.2,
    "volume": "1326900",
    "turnover": 636738960,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": -0.12494793835900997,
    "timestamp": 1631174340
  }, {
    "time": "2021-09-09 16:00:00",
    "isBlank": false,
    "highPrice": 481.4,
    "openPrice": 479.6,
    "lowPrice": 479.6,
    "closePrice": 480,
    "lastClosePrice": 479.6,
    "volume": "5134400",
    "turnover": 2464740790,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0.08340283569640894,
    "timestamp": 1631174400
  }]
}
stop
```











Interface Limitations

- This interface is to obtain real-time candlestick, which can obtain
  the nearest 1000 at most. To get historical candlestick, please refer
  to [Get historical
  candlestick](/moomoo-api-doc/en/quote/request-history-kline.html).
- Only a stock of daily timeframe and above have P/E ratio and turnover
  ratio fields.
- **Options** related candlestick data, only supports 1 day, 1 minute, 5
  minutes, 15 minutes and 60 minutes.





Tips

- This API provides the function of obtaining candlestick data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Candlestick
  Callback](/moomoo-api-doc/en/quote/update-kl.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_cur_kline(code, num, ktype=SubType.K_DAY, autype=AuType.QFQ)`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
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
  <td style="text-align: left;">num</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The number of candlesticks.
  
    
  
  
   
  
  Up to 1000.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">ktype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
  <td style="text-align: left;">Candlestick type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">autype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#7071">AuType</a></td>
  <td style="text-align: left;">Type of adjustment.</td>
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
  <td>If ret == RET_OK, IPO data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - IPO data format as follows:
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
    <td style="text-align: left;">time_key</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.
    
      
    
    
     
    
    This field is in decimal form, so 0.01 is equivalent to 1%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.
    
      
    
    
     
    
    The close of the previous trading day.<br />
    For efficiency reasons, the yesterday's close of the first data may be
    0.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.K_DAY], subscribe_push=False, session=Session.ALL)
# First subscribe to the candlestick type. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK:  # Successfully subscribed
    ret, data = quote_ctx.get_cur_kline('US.AAPL', 2, SubType.K_DAY, AuType.QFQ)  # Get the latest 2 candlestick data of US.AAPL
    if ret == RET_OK:
        print(data)
        print(data['turnover_rate'][0])   # Take the first turnover rate
        print(data['turnover_rate'].values.tolist())   # Convert to list
    else:
        print('error:', data)
else:
    print('subscription failed', err_message)
quote_ctx.close()  # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code name             time_key    open   close    high     low     volume      turnover  pe_ratio  turnover_rate  last_close
0  US.AAPL   APPLE  2025-04-03 00:00:00  205.54  203.19  207.49  201.25  103419006  2.111773e+10    33.419        0.00689      223.89
1  US.AAPL   APPLE  2025-04-04 00:00:00  193.89  188.38  199.88  187.34  125910913  2.424473e+10    30.983        0.00838      203.19
0.00689
[0.00689, 0.00838]
```









## <a href="#7451-2" class="header-anchor">#</a> Qot_GetKL.proto

- **Description**

  To obtain real-time K line data of subscribed stocks, you must first
  subscribe.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3006





`uint GetKL(QotGetKL.Request req);`  
`virtual void OnReply_GetKL(MMAPI_Conn client, uint nSerialNo, QotGetKL.Response rsp);`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn {
    MMAPI_Qot qot = new MMAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1);  //Set client information
        qot.SetConnCallback(this);  //Set connection callback
        qot.SetQotCallback(this);   //Set transaction callback
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_KL_1Min)
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
        QotGetKL.C2S c2s = QotGetKL.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetKlType((int)QotCommon.KLType.KLType_1Min)
                .SetRehabType((int)QotCommon.RehabType.RehabType_Forward)
                .SetReqNum(50)
                .Build();
        QotGetKL.Request req = QotGetKL.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetKL(req);
        Console.Write("Send QotGetKL: {0}\n", seqNo);
    }

    public void OnReply_GetKL(MMAPI_Conn client, uint nSerialNo, QotGetKL.Response rsp)
    {
        Console.Write("Reply: QotGetKL: {0}\n", nSerialNo);
        Console.Write("lastClosePrice: {0}\n", rsp.S2C.KlListList[0].LastClosePrice);
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
Qot onInitConnect: ret=0 desc= connID=6825671203627466268
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetKL: 4
Reply: QotGetKL: 4
lastClosePrice: 458.6
```









`int getKL(QotGetKL.Request req);`  
`void onReply_GetKL(MMAPI_Conn client, int nSerialNo, QotGetKL.Response rsp);`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
                .addSubTypeList(QotCommon.SubType.SubType_KL_1Min_VALUE)
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
        QotGetKL.C2S c2s = QotGetKL.C2S.newBuilder()
                .setSecurity(sec)
                .setKlType(QotCommon.KLType.KLType_1Min_VALUE)
                .setRehabType(QotCommon.RehabType.RehabType_Forward_VALUE)
                .setReqNum(2)
                .build();
        QotGetKL.Request req = QotGetKL.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getKL(req);
        System.out.printf("Send QotGetKL: %d\n", seqNo);
    }

    @Override
    public void onReply_GetKL(MMAPI_Conn client, int nSerialNo, QotGetKL.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetKL failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetKL: %s\n", json);
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
Send QotGetKL: 3
Receive QotGetKL: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "klList": [{
      "time": "2021-06-24 15:59:00",
      "isBlank": false,
      "highPrice": 583.5,
      "openPrice": 583.0,
      "lowPrice": 583.0,
      "closePrice": 583.5,
      "lastClosePrice": 583.5,
      "volume": "37900",
      "turnover": 2.210525E7,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": 0.0,
      "timestamp": 1.62452154E9
    }, {
      "time": "2021-06-24 16:00:00",
      "isBlank": false,
      "highPrice": 583.5,
      "openPrice": 583.0,
      "lowPrice": 582.5,
      "closePrice": 583.0,
      "lastClosePrice": 583.5,
      "volume": "1197900",
      "turnover": 6.98392175E8,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": -0.08568980291345331,
      "timestamp": 1.6245216E9
    }]
  }
}
```









`moomoo::u32_t GetKL(const Qot_GetKL::Request &stReq);`  
`virtual void OnReply_GetKL(moomoo::u32_t nSerialNo, const Qot_GetKL::Response &stRsp) = 0;`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_KL_1Min);
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
            Qot_GetKL::Request req;
            Qot_GetKL::C2S *c2s = req.mutable_c2s();
            c2s->set_rehabtype(1);
            c2s->set_kltype(Qot_Common::KLType::KLType_1Min);
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            c2s->set_reqnum(10);

            m_GetKLSerialNo = m_pQotApi->GetKL(req);
            cout << "Request GetKL SerialNo: " << m_GetKLSerialNo << endl;
        }
    }

    virtual void OnReply_GetKL(moomoo::u32_t nSerialNo, const Qot_GetKL::Response &stRsp){
        if(nSerialNo == m_GetKLSerialNo)
        {
            cout << "OnReply_GetKL SerialNo: " << nSerialNo << endl; 
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
    moomoo::u32_t m_GetKLSerialNo;
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
Request GetKL SerialNo: 4
OnReply_GetKL SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "klList": [
   {
    "time": "2021-06-09 14:03:00",
    "isBlank": false,
    "highPrice": 602,
    "openPrice": 602,
    "lowPrice": 601.5,
    "closePrice": 601.5,
    "lastClosePrice": 601.5,
    "volume": "9500",
    "turnover": 5714700,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0,
    "timestamp": 1623218580
   },
...
   {
    "time": "2021-06-09 14:11:00",
    "isBlank": false,
    "highPrice": 601,
    "openPrice": 601,
    "lowPrice": 601,
    "closePrice": 601,
    "lastClosePrice": 601,
    "volume": "0",
    "turnover": 0,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0,
    "timestamp": 1623219060
   }
  ]
 }
}
```









`GetKL(req);`

- **Description**

  Get real-time candlestick data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, types of adjustment
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlesticks
    required Qot_Common.Security security = 3; //Security
    required int32 reqNum = 4; //The number of candlestick requested
}

message Request
{
    required C2S c2s = 1;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For Candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Stock
    optional string name = 3; // stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data struct
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For Stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For Candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetKL(){
    const { RetType } = Common
    const { SubType, QotMarket, RehabType, KLType } = Qot_Common
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
                subTypeList: [ SubType.SubType_KL_1Min ], 
                isSubOrUnSub: true,
                isRegOrUnRegPush: true, 
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                        rehabType: RehabType.RehabType_Forward,
                        klType: KLType.KLType_1Min,
                        security: {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                        reqNum: 2,
                    },
                };
                
                websocket.GetKL(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("KL: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
KL: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "klList": [{
    "time": "2021-09-09 15:59:00",
    "isBlank": false,
    "highPrice": 480.4,
    "openPrice": 480.2,
    "lowPrice": 479,
    "closePrice": 479.6,
    "lastClosePrice": 480.2,
    "volume": "1326900",
    "turnover": 636738960,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": -0.12494793835900997,
    "timestamp": 1631174340
  }, {
    "time": "2021-09-09 16:00:00",
    "isBlank": false,
    "highPrice": 481.4,
    "openPrice": 479.6,
    "lowPrice": 479.6,
    "closePrice": 480,
    "lastClosePrice": 479.6,
    "volume": "5134400",
    "turnover": 2464740790,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0.08340283569640894,
    "timestamp": 1631174400
  }]
}
stop
```











Interface Limitations

- This interface is to obtain real-time candlestick, which can obtain
  the nearest 1000 at most. To get historical candlestick, please refer
  to [Get historical
  candlestick](/moomoo-api-doc/en/quote/request-history-kline.html).
- Only a stock of daily timeframe and above have P/E ratio and turnover
  ratio fields.
- **Options** related candlestick data, only supports 1 day, 1 minute, 5
  minutes, 15 minutes and 60 minutes.





Tips

- This API provides the function of obtaining candlestick data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Candlestick
  Callback](/moomoo-api-doc/en/quote/update-kl.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).













