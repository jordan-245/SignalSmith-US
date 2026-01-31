



# <a href="#9644" class="header-anchor">#</a> Get Futures Contract Information









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_future_info(code_list)`

- **Description**

  Get futures contract information

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | code_list | list | Futures code list. Data type of elements in the list is str. |

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
  <td>If ret == RET_OK, futures contract data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Futures contract data format as follows:
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
    <td style="text-align: left;">Future code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Future name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subject.</td>
    </tr>
    <tr>
    <td style="text-align: left;">exchange</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Exchange.</td>
    </tr>
    <tr>
    <td style="text-align: left;">type</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Contract type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">size</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract size.</td>
    </tr>
    <tr>
    <td style="text-align: left;">size_unit</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Contract size unit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_currency</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Quote currency.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_unit</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Price unit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">min_change</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Price change step.</td>
    </tr>
    <tr>
    <td style="text-align: left;">min_change_unit</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Unit of price change step.
    
      
    
    
     
    
    Obsolete field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Trading time.</td>
    </tr>
    <tr>
    <td style="text-align: left;">time_zone</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time zone.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The last trading time.
    
      
    
    
     
    
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">exchange_format_url</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Exchange format url address.</td>
    </tr>
    <tr>
    <td style="text-align: left;">origin_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Original future code.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_future_info(["HK.MPImain", "HK.HAImain"])
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code      name       owner exchange  type     size size_unit price_currency price_unit  min_change min_change_unit                        trade_time time_zone last_trade_time                                exchange_format_url           origin_code
0  HK.MPImain  MPI Future Main(NOV0)    Hang Seng Mainland Properties Index     HKEX  Equity Index     50.0  Index Points×HKD            HKD  Index Point        0.50        (09:15 - 12:00), (13:00 - 16:30)       CCT                  https://www.hkex.com.hk/Products/Listed-Deriva...           HK.MPI2112
1  HK.HAImain  HAI Future Main(NOV0)    HK.06837     HKEX  Single Stock  10000.0            shares            HKD  1 share/HKD        0.01                   (09:30 - 12:00), (13:00 - 16:00)       CCT                  https://www.hkex.com.hk/Products/Listed-Deriva...           HK.HAI2112
HK.MPImain
['HK.MPImain', 'HK.HAImain']
```









## <a href="#8538" class="header-anchor">#</a> Qot_GetFutureInfo.proto

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3218





`uint GetFutureInfo(QotGetFutureInfo.Request req);`  
`virtual void OnReply_GetFutureInfo(FTAPI_Conn client, uint nSerialNo, QotGetFutureInfo.Response rsp);`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
                .SetCode("HSImain")
                .Build();
        QotGetFutureInfo.C2S c2s = QotGetFutureInfo.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetFutureInfo.Request req = QotGetFutureInfo.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetFutureInfo(req);
        Console.Write("Send QotGetFutureInfo: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetFutureInfo(FTAPI_Conn client, uint nSerialNo, QotGetFutureInfo.Response rsp)
    {
        Console.Write("Reply: QotGetFutureInfo: {0}\n", nSerialNo);
        Console.Write("name: {0}, exchange: {1} \n", rsp.S2C.FutureInfoListList[0].Name,
            rsp.S2C.FutureInfoListList[0].Exchange);
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
Qot onInitConnect: ret=0 desc= connID=6825719160020953581
Send QotGetFutureInfo: 3
Reply: QotGetFutureInfo: 3
name: HSI Future Main(AUG1), exchange: HKEX
```









`int getFutureInfo(QotGetFutureInfo.Request req);`  
`void onReply_GetFutureInfo(FTAPI_Conn client, int nSerialNo, QotGetFutureInfo.Response rsp);`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
                .setCode("HSImain")
                .build();
        QotGetFutureInfo.C2S c2s = QotGetFutureInfo.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetFutureInfo.Request req = QotGetFutureInfo.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getFutureInfo(req);
        System.out.printf("Send QotGetFutureInfo: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetFutureInfo(FTAPI_Conn client, int nSerialNo, QotGetFutureInfo.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetFutureInfo failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetFutureInfo: %s\n", json);
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
Send QotGetFutureInfo: 2
Receive QotGetFutureInfo: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "futureInfoList": [{
      "name": "HSI Future Main(JUN1)",
      "security": {
        "market": 1,
        "code": "HSImain"
      },
      "lastTradeTime": "",
      "owner": {
        "market": 1,
        "code": "800000"
      },
      "ownerOther": "Hang Seng Index",
      "exchange": "HKEX",
      "contractType": "Equity Index",
      "contractSize": 50.0,
      "contractSizeUnit": "Index Points×HKD",
      "quoteCurrency": "HKD",
      "minVar": 1.0,
      "minVarUnit": "",
      "quoteUnit": "Index Point",
      "tradeTime": [{
        "begin": 555.0,
        "end": 720.0
      }, {
        "begin": 780.0,
        "end": 990.0
      }, {
        "begin": 1035.0,
        "end": 180.0
      }],
      "timeZone": "CCT",
      "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Hang-Seng-Index-(HSI)/Hang-Seng-Index-Futures?sc_lang=en#&product=HSI",
      "origin": {
        "market": 1,
        "code": "HSI2112"
      }
    }]
  }
}
```









`Futu::u32_t GetFutureInfo(const Qot_GetFutureInfo::Request &stReq);`  
`virtual void OnReply_GetFutureInfo(Futu::u32_t nSerialNo, const Qot_GetFutureInfo::Response &stRsp) = 0;`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
        Qot_GetFutureInfo::Request req;
        Qot_GetFutureInfo::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("HSImain");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetFutureInfoSerialNo = m_pQotApi->GetFutureInfo(req);
        cout << "Request GetFutureInfo SerialNo: " << m_GetFutureInfoSerialNo << endl;
    }

    virtual void OnReply_GetFutureInfo(Futu::u32_t nSerialNo, const Qot_GetFutureInfo::Response &stRsp){
        if(nSerialNo == m_GetFutureInfoSerialNo)
        {
            cout << "OnReply_GetFutureInfo SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetFutureInfoSerialNo;
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
Request GetFutureInfo SerialNo: 4
OnReply_GetFutureInfo SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "futureInfoList": [
   {
    "name": "HSI Future Main(JUN1)",
    "security": {
     "market": 1,
     "code": "HSImain"
    },
    "lastTradeTime": "",
    "owner": {
     "market": 1,
     "code": "800000"
    },
    "ownerOther": "Hang Seng Index",
    "exchange": "HKEX",
    "contractType": "Equity Index",
    "contractSize": 50,
    "contractSizeUnit": "Index Points×HKD",
    "quoteCurrency": "HKD",
    "minVar": 1,
    "minVarUnit": "",
    "quoteUnit": "Index Point",
    "tradeTime": [
     {
      "begin": 555,
      "end": 720
     },
     {
      "begin": 780,
      "end": 990
     },
     {
      "begin": 1035,
      "end": 180
     }
    ],
    "timeZone": "CCT",
    "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Hang-Seng-Index-(HSI)/Hang-Seng-Index-Futures?sc_lang=en#&product=HSI",
    "security": {
     "market": 1,
     "code": "HSI2112"
    }
   }
  ]
 }
}
```









`GetFutureInfo(req);`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetFutureInfo(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    securityList:[{
                        market: QotMarket.QotMarket_HK_Future,
                        code: "MPImain",
                    },{
                        market: QotMarket.QotMarket_HK_Future,
                        code: "HAImain",
                    },],
                },
            };

            websocket.GetFutureInfo(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("FutureInfo: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
    // OpenD accepts up to 128 connections
    // In this example, it creates one connection for one request
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 5000); // Set the script to receive OpenD push duration to 5 seconds
}
```





- **Output**



``` javascript
FutureInfo: errCode 0, retMsg , retType 0
{
  "futureInfoList": [{
    "name": "MPI Future Main(SEP1)",
    "security": {
      "market": 1,
      "code": "MPImain"
    },
    "lastTradeTime": "",
    "ownerOther": "Hang Seng Mainland Properties Index",
    "exchange": "HKEX",
    "contractType": "Equity Index",
    "contractSize": 50,
    "contractSizeUnit": "Index Points×HKD",
    "quoteCurrency": "HKD",
    "minVar": 0.5,
    "minVarUnit": "",
    "quoteUnit": "Index Point",
    "tradeTime": [{
      "begin": 555,
      "end": 720
    }, {
      "begin": 780,
      "end": 990
    }],
    "timeZone": "CCT",
    "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Sector-Index/Sector-Index-Futures?sc_lang=en"
  }, {
    "name": "HAI Future Main(SEP1)",
    "security": {
      "market": 1,
      "code": "HAImain"
    },
    "lastTradeTime": "",
    "owner": {
      "market": 1,
      "code": "06837"
    },
    "ownerOther": "Haitong Securities Co. Ltd.",
    "exchange": "HKEX",
    "contractType": "Single Stock",
    "contractSize": 10000,
    "contractSizeUnit": "shares",
    "quoteCurrency": "HKD",
    "minVar": 0.01,
    "minVarUnit": "",
    "quoteUnit": "1 share/HKD",
    "tradeTime": [{
      "begin": 570,
      "end": 720
    }, {
      "begin": 780,
      "end": 960
    }],
    "timeZone": "CCT",
    "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Single-Stock/Stock-Futures?sc_lang=en",
    "security": {
      "market": 1,
      "code": "HAI2112"
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 30 requests for obtaining futures contract data interface
  every 30 seconds
- The maximum number of futures is 200, in the code list for each
  request.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_future_info(code_list)`

- **Description**

  Get futures contract information

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | code_list | list | Futures code list. Data type of elements in the list is str. |

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
  <td>If ret == RET_OK, futures contract data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Futures contract data format as follows:
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
    <td style="text-align: left;">Future code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Future name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subject.</td>
    </tr>
    <tr>
    <td style="text-align: left;">exchange</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Exchange.</td>
    </tr>
    <tr>
    <td style="text-align: left;">type</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Contract type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">size</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract size.</td>
    </tr>
    <tr>
    <td style="text-align: left;">size_unit</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Contract size unit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_currency</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Quote currency.</td>
    </tr>
    <tr>
    <td style="text-align: left;">price_unit</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Price unit.</td>
    </tr>
    <tr>
    <td style="text-align: left;">min_change</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Price change step.</td>
    </tr>
    <tr>
    <td style="text-align: left;">min_change_unit</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Unit of price change step.
    
      
    
    
     
    
    Obsolete field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Trading time.</td>
    </tr>
    <tr>
    <td style="text-align: left;">time_zone</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time zone.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The last trading time.
    
      
    
    
     
    
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">exchange_format_url</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Exchange format url address.</td>
    </tr>
    <tr>
    <td style="text-align: left;">origin_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Original future code.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_future_info(["HK.MPImain", "HK.HAImain"])
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code      name       owner exchange  type     size size_unit price_currency price_unit  min_change min_change_unit                        trade_time time_zone last_trade_time                                exchange_format_url           origin_code
0  HK.MPImain  MPI Future Main(NOV0)    Hang Seng Mainland Properties Index     HKEX  Equity Index     50.0  Index Points×HKD            HKD  Index Point        0.50       (09:15 - 12:00), (13:00 - 16:30)       CCT                  https://www.hkex.com.hk/Products/Listed-Deriva...           HK.MPI2112
1  HK.HAImain  HAI Future Main(NOV0)    HK.06837     HKEX  Single Stock  10000.0            shares            HKD  1 share/HKD        0.01               (09:30 - 12:00), (13:00 - 16:00)       CCT                  https://www.hkex.com.hk/Products/Listed-Deriva...           HK.HAI2112
HK.MPImain
['HK.MPImain', 'HK.HAImain']
```









## <a href="#8538-2" class="header-anchor">#</a> Qot_GetFutureInfo.proto

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3218





`uint GetFutureInfo(QotGetFutureInfo.Request req);`  
`virtual void OnReply_GetFutureInfo(MMAPI_Conn client, uint nSerialNo, QotGetFutureInfo.Response rsp);`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
                .SetCode("HSImain")
                .Build();
        QotGetFutureInfo.C2S c2s = QotGetFutureInfo.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetFutureInfo.Request req = QotGetFutureInfo.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetFutureInfo(req);
        Console.Write("Send QotGetFutureInfo: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetFutureInfo(MMAPI_Conn client, uint nSerialNo, QotGetFutureInfo.Response rsp)
    {
        Console.Write("Reply: QotGetFutureInfo: {0}\n", nSerialNo);
        Console.Write("name: {0}, exchange: {1} \n", rsp.S2C.FutureInfoListList[0].Name,
            rsp.S2C.FutureInfoListList[0].Exchange);
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
Qot onInitConnect: ret=0 desc= connID=6825719160020953581
Send QotGetFutureInfo: 3
Reply: QotGetFutureInfo: 3
name: HSI Future Main(AUG1), exchange: HKEX
```









`int getFutureInfo(QotGetFutureInfo.Request req);`  
`void onReply_GetFutureInfo(MMAPI_Conn client, int nSerialNo, QotGetFutureInfo.Response rsp);`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
                .setCode("HSImain")
                .build();
        QotGetFutureInfo.C2S c2s = QotGetFutureInfo.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetFutureInfo.Request req = QotGetFutureInfo.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getFutureInfo(req);
        System.out.printf("Send QotGetFutureInfo: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetFutureInfo(MMAPI_Conn client, int nSerialNo, QotGetFutureInfo.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetFutureInfo failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetFutureInfo: %s\n", json);
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
Send QotGetFutureInfo: 2
Receive QotGetFutureInfo: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "futureInfoList": [{
      "name": "HSI Future Main(JUN1)",
      "security": {
        "market": 1,
        "code": "HSImain"
      },
      "lastTradeTime": "",
      "owner": {
        "market": 1,
        "code": "800000"
      },
      "ownerOther": "Hang Seng Index",
      "exchange": "HKEX",
      "contractType": "Equity Index",
      "contractSize": 50.0,
      "contractSizeUnit": "Index Points×HKD",
      "quoteCurrency": "HKD",
      "minVar": 1.0,
      "minVarUnit": "",
      "quoteUnit": "Index Point",
      "tradeTime": [{
        "begin": 555.0,
        "end": 720.0
      }, {
        "begin": 780.0,
        "end": 990.0
      }, {
        "begin": 1035.0,
        "end": 180.0
      }],
      "timeZone": "CCT",
      "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Hang-Seng-Index-(HSI)/Hang-Seng-Index-Futures?sc_lang=en#&product=HSI",
      "origin": {
        "market": 1,
        "code": "HSI2112"
      }
    }]
  }
}
```









`moomoo::u32_t GetFutureInfo(const Qot_GetFutureInfo::Request &stReq);`  
`virtual void OnReply_GetFutureInfo(moomoo::u32_t nSerialNo, const Qot_GetFutureInfo::Response &stRsp) = 0;`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
        Qot_GetFutureInfo::Request req;
        Qot_GetFutureInfo::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("HSImain");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetFutureInfoSerialNo = m_pQotApi->GetFutureInfo(req);
        cout << "Request GetFutureInfo SerialNo: " << m_GetFutureInfoSerialNo << endl;
    }

    virtual void OnReply_GetFutureInfo(moomoo::u32_t nSerialNo, const Qot_GetFutureInfo::Response &stRsp){
        if(nSerialNo == m_GetFutureInfoSerialNo)
        {
            cout << "OnReply_GetFutureInfo SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetFutureInfoSerialNo;
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
Request GetFutureInfo SerialNo: 4
OnReply_GetFutureInfo SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "futureInfoList": [
   {
    "name": "HSI Future Main(JUN1)",
    "security": {
     "market": 1,
     "code": "HSImain"
    },
    "lastTradeTime": "",
    "owner": {
     "market": 1,
     "code": "800000"
    },
    "ownerOther": "Hang Seng Index",
    "exchange": "HKEX",
    "contractType": "Equity Index",
    "contractSize": 50,
    "contractSizeUnit": "Index Points×HKD",
    "quoteCurrency": "HKD",
    "minVar": 1,
    "minVarUnit": "",
    "quoteUnit": "Index Point",
    "tradeTime": [
     {
      "begin": 555,
      "end": 720
     },
     {
      "begin": 780,
      "end": 990
     },
     {
      "begin": 1035,
      "end": 180
     }
    ],
    "timeZone": "CCT",
    "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Hang-Seng-Index-(HSI)/Hang-Seng-Index-Futures?sc_lang=en#&product=HSI",
    "security": {
     "market": 1,
     "code": "HSI2112"
    }
   }
  ]
 }
}
```









`GetFutureInfo(req);`

- **Description**

  Get futures contract information

- **Parameters**



``` protobuf

message C2S
{
    repeated Qot_Common.Security securityList = 1; //Stock list
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
//Trading time
message TradeTime
{
    optional double begin = 1; // start time, in minutes
    optional double end = 2; // end time, in minutes
}

//List of futures contract data
message FutureInfo
{
    required string name = 1; // contract name
    required Qot_Common.Security security = 2; // contract code
    required string lastTradeTime = 3; //On the last trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 4; //The last trading day timestamp, only future non-main contracts have this field
    optional Qot_Common.Security owner = 5; //Underlying stock stock futures and stock index futures have this field
    required string ownerOther = 6; //Underlying asset
    required string exchange = 7; //Exchange
    required string contractType = 8; //Contract type
    required double contractSize = 9; //Contract size
    required string contractSizeUnit = 10; //Unit of contract size
    required string quoteCurrency = 11; //Quote currency
    required double minVar = 12; //Price change step
    required string minVarUnit = 13; //Unit of price change step (Obsolete field)
    optional string quoteUnit = 14; //Quote unit
    repeated TradeTime tradeTime = 15; //Trading time
    required string timeZone = 16; //The time zone
    required string exchangeFormatUrl = 17; //Exchange format
    optional Qot_Common.Security origin = 18; //Original future code
}

message S2C
{
    repeated FutureInfo futureInfoList = 1; //List of futures contract information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetFutureInfo(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    securityList:[{
                        market: QotMarket.QotMarket_HK_Future,
                        code: "MPImain",
                    },{
                        market: QotMarket.QotMarket_HK_Future,
                        code: "HAImain",
                    },],
                },
            };

            websocket.GetFutureInfo(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("FutureInfo: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
    // OpenD accepts up to 128 connections
    // In this example, it creates one connection for one request
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 5000); // Set the script to receive OpenD push duration to 5 seconds
}
```





- **Output**



``` javascript
FutureInfo: errCode 0, retMsg , retType 0
{
  "futureInfoList": [{
    "name": "MPI Future Main(SEP1)",
    "security": {
      "market": 1,
      "code": "MPImain"
    },
    "lastTradeTime": "",
    "ownerOther": "Hang Seng Mainland Properties Index",
    "exchange": "HKEX",
    "contractType": "Equity Index",
    "contractSize": 50,
    "contractSizeUnit": "Index Points×HKD",
    "quoteCurrency": "HKD",
    "minVar": 0.5,
    "minVarUnit": "",
    "quoteUnit": "Index Point",
    "tradeTime": [{
      "begin": 555,
      "end": 720
    }, {
      "begin": 780,
      "end": 990
    }],
    "timeZone": "CCT",
    "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Equity-Index/Sector-Index/Sector-Index-Futures?sc_lang=en"
  }, {
    "name": "HAI Future Main(SEP1)",
    "security": {
      "market": 1,
      "code": "HAImain"
    },
    "lastTradeTime": "",
    "owner": {
      "market": 1,
      "code": "06837"
    },
    "ownerOther": "Haitong Securities Co. Ltd.",
    "exchange": "HKEX",
    "contractType": "Single Stock",
    "contractSize": 10000,
    "contractSizeUnit": "shares",
    "quoteCurrency": "HKD",
    "minVar": 0.01,
    "minVarUnit": "",
    "quoteUnit": "1 share/HKD",
    "tradeTime": [{
      "begin": 570,
      "end": 720
    }, {
      "begin": 780,
      "end": 960
    }],
    "timeZone": "CCT",
    "exchangeFormatUrl": "https://www.hkex.com.hk/Products/Listed-Derivatives/Single-Stock/Stock-Futures?sc_lang=en",
    "security": {
      "market": 1,
      "code": "HAI2112"
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 30 requests for obtaining futures contract data interface
  every 30 seconds
- The maximum number of futures is 200, in the code list for each
  request.













