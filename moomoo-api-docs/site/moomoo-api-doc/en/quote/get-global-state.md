



# <a href="#2345" class="header-anchor">#</a> Get global market status









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_global_state()`

- **Description**

  Get global status

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
  <td>If ret == RET_OK, global status is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Global status format as follows:
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
    <td style="text-align: left;">market_sz</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Shenzhen market state.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_sh</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Shanghai market state.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_hk</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Hong Kong market status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_hkfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Hong Kong futures market status.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the US futures market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_usfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">US futures market status.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the US futures market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_us</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">United States market state.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the US market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_sgfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Singapore futures market status.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the Singapore futures market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_jpfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Japanese futures market status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">server_ver</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">OpenD version number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trd_logined</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">True: Logged into the trading server,
    False: Not logged into the trading server.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qot_logined</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">True: logged into the market server,
    False: Not logged into the market server.</td>
    </tr>
    <tr>
    <td style="text-align: left;">timestamp</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Current Greenwich timestamp.
    
      
    
    
     
    
    unit: second
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">local_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Local timestamp for OpenD.
    
      
    
    
     
    
    unit: second
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">program_status_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/ftapi/common.html#9803">ProgramStatusType</a></td>
    <td style="text-align: left;">Current status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">program_status_desc</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Additional description.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
print(quote_ctx.get_global_state())
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
(0, {'market_sz': 'REST', 'market_us': 'AFTER_HOURS_END', 'market_sh': 'REST', 'market_hk': 'MORNING', 'market_hkfuture': 'FUTURE_DAY_OPEN', 'market_usfuture': 'FUTURE_OPEN', 'market_sgfuture': 'FUTURE_DAY_OPEN', 'market_jpfuture': 'FUTURE_DAY_OPEN', 'server_ver': '504', 'trd_logined': True, 'timestamp': '1620963064', 'qot_logined': True, 'local_timestamp': 1620963064.124152, 'program_status_type': 'READY', 'program_status_desc': ''})
```









## <a href="#4500" class="header-anchor">#</a> GetGlobalState.proto

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  1002





`uint GetGlobalState(GetGlobalState.Request req)`  
`void OnReply_GetGlobalState(FTAPI_Conn client, uint nSerialNo, GetGlobalState.Response rsp)`

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Qot, FTSPI_Conn
    {
        FTAPI_Qot qot = new FTAPI_Qot();

        public Program()
        {
            qot.SetClientInfo("FTAPI4NET_Sample", 1);  //Set client information
            qot.SetConnCallback(this);  //Set connection callback
            qot.SetQotCallback(this);   //Set transaction callback
        }

        public void Start()
        {
            qot.InitConnect("127.0.0.1", (ushort)11111, false); //Start to connect to OpenD, the connection result is processed through OnInitConnect
        }


        public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
        {
            Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
            if (errCode != 0) //Connection failed
                return;

            //Connection is successful, you can make requests
            GetGlobalState.C2S c2s = GetGlobalState.C2S.CreateBuilder()
                    .SetUserID(0)
                    .Build();
            GetGlobalState.Request req = GetGlobalState.Request.CreateBuilder().SetC2S(c2s).Build();
            uint seqNo = qot.GetGlobalState(req);
            Console.WriteLine("Send GetGlobalState: {0}", seqNo1);
        }

        //This callback will be called after disconnection
        public void OnDisconnect(FTAPI_Conn client, long errCode)
        {
            Console.Write("Qot onDisConnect: {0}\n", errCode);
            qot.Close(); //Release the underlying resources
        }

        public void OnReply_GetGlobalState(FTAPI_Conn client, uint nSerialNo, GetGlobalState.Response rsp)
        {
            Console.Write("Reply: GetGlobalState: {0}\n", nSerialNo);
            Console.Write("marketHK: {0}, programStatus: {1} \n", rsp.S2C.MarketHK, rsp.S2C.ProgramStatus);
        }

        public static void Main(String[] args)
        {
            FTAPI.Init(); //Initialize the environment, call once when the program starts
            Program qot = new Program();
            qot.Start();

            while (true)
                Thread.Sleep(1000 * 600);
        }
    }
```





**Output**



``` cs
Qot onInitConnect: ret=0 desc= connID=6826777317655602340
Send GetGlobalState: 3
Reply: GetGlobalState: 3
marketHK: 5, programStatus: type: ProgramStatusType_Ready
```









`int getGlobalState(GetGlobalState.Request req);`  
`void onReply_GetGlobalState(FTAPI_Conn client, int nSerialNo, GetGlobalState.Response rsp)`

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1);  //Set client information
        qot.setConnSpi(this);  //Set connection callback
        qot.setQotSpi(this);   //Set market callback
    }

    public void start() throws IOException {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        GetGlobalState.C2S c2s = GetGlobalState.C2S.newBuilder()
                .setUserID(0)
                .build();
        GetGlobalState.Request req = GetGlobalState.Request.newBuilder().setC2S(c2s).build();
        qot.getGlobalState(req);
    }

    @Override
    public void onReply_GetGlobalState(FTAPI_Conn client, int nSerialNo, GetGlobalState.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetGlobalState failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetGlobalState: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
        FTAPI.init();
        QotDemo qot = new QotDemo();
        qot.start();

        while (true) {
            try {
                Thread.sleep(1000 * 60);
            } catch (InterruptedException exc) {

            }
        }
    }
}
```





- **Output**



``` text
Send QotGetGlobalState: 2
Receive QotGetGlobalState: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "marketHK": 6,
    "marketUS": 8,
    "marketSH": 6,
    "marketSZ": 6,
    "marketHKFuture": 17,
    "qotLogined": true,
    "trdLogined": true,
    "serverVer": 505,
    "serverBuildNo": 1707,
    "time": "1624523642",
    "localTime": 1.624523642858697E9,
    "programStatus": {
      "type": "ProgramStatusType_Ready"
    },
    "qotSvrIpAddr": "119.29.43.101",
    "trdSvrIpAddr": "119.29.43.101",
    "marketUSFuture": 23,
    "connID": "6813746013095493825",
    "marketSGFuture": 13,
    "marketJPFuture": 13
  }
}
```









`Futu::u32_t GetGlobalState(const GetGlobalState::Request &stReq);`  
`virtual void OnReply_GetGlobalState(Futu::u32_t nSerialNo, const GetGlobalState::Response &stRsp) = 0;`

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
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
        GetGlobalState::Request req;
        GetGlobalState::C2S *c2s = req.mutable_c2s();
        c2s->set_userid(0);

        m_GetGlobalStateSerialNo = m_pQotApi->GetGlobalState(req);
        cout << "Request GetGlobalState SerialNo: " << m_GetGlobalStateSerialNo << endl;
    }

    virtual void OnReply_GetGlobalState(Futu::u32_t nSerialNo, const GetGlobalState::Response &stRsp){
        if(nSerialNo == m_GetGlobalStateSerialNo)
        {
            cout << "OnReply_GetGlobalState SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }
protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetGlobalStateSerialNo;
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
Request GetGlobalState SerialNo: 4
OnReply_GetGlobalState SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "marketHK": 6,
  "marketUS": 8,
  "marketSH": 6,
  "marketSZ": 6,
  "marketHKFuture": 15,
  "qotLogined": true,
  "trdLogined": true,
  "serverVer": 504,
  "serverBuildNo": 1608,
  "time": "1623226833",
  "localTime": 1623226833.8509541,
  "programStatus": {
   "type": 10
  },
  "qotSvrIpAddr": "106.55.66.8",
  "trdSvrIpAddr": "106.55.66.8",
  "marketUSFuture": 23,
  "connID": "6808306802122125817",
  "marketSGFuture": 13,
  "marketJPFuture": 13
 }
}
```









`GetGlobalState(req);`

- **Description**

  Get global status

- **Parameters**



``` protobuf

message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function GetGlobalState(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    userID: 0,
                },
            };

            websocket.GetGlobalState(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("GlobalState: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GlobalState: errCode 0, retMsg , retType 0
{
  "marketHK": 6,
  "marketUS": 8,
  "marketSH": 6,
  "marketSZ": 6,
  "marketHKFuture": 15,
  "qotLogined": true,
  "trdLogined": true,
  "serverVer": 507,
  "serverBuildNo": 1908,
  "time": "1631261759",
  "localTime": 1631261759.095172,
  "programStatus": {
    "type": "ProgramStatusType_Ready"
  },
  "qotSvrIpAddr": "119.29.48.17",
  "trdSvrIpAddr": "106.55.66.8",
  "marketUSFuture": 23,
  "connID": "6842007721202028582",
  "marketSGFuture": 13,
  "marketJPFuture": 13
}
stop
```

















- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_global_state()`

- **Description**

  Get global status

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
  <td>If ret == RET_OK, global status is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Global status format as follows:
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
    <td style="text-align: left;">market_sz</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Shenzhen market state.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_sh</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Shanghai market state.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_hk</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Hong Kong market status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_hkfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Hong Kong futures market status.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the US futures market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_usfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">US futures market status.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the US futures market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_us</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">United States market state.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the US market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_sgfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Singapore futures market status.
    
      
    
    
     
    
    Due to there are differences in the trading time of different varieties
    in the Singapore futures market, it is recommended to use <a
    href="/moomoo-api-doc/en/quote/get-market-state.html">get_market_state</a>
    interface to get the market state of the specified variety.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_jpfuture</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#8663">MarketState</a></td>
    <td style="text-align: left;">Japanese futures market status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">server_ver</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">OpenD version number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trd_logined</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">True: Logged into the trading server,
    False: Not logged into the trading server.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qot_logined</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">True: logged into the market server,
    False: Not logged into the market server.</td>
    </tr>
    <tr>
    <td style="text-align: left;">timestamp</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Current Greenwich timestamp.
    
      
    
    
     
    
    unit: second
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">local_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Local timestamp for OpenD.
    
      
    
    
     
    
    unit: second
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">program_status_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/ftapi/common.html#9803">ProgramStatusType</a></td>
    <td style="text-align: left;">Current status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">program_status_desc</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Additional description.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
print(quote_ctx.get_global_state())
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
(0, {'market_sz': 'REST', 'market_us': 'AFTER_HOURS_END', 'market_sh': 'REST', 'market_hk': 'MORNING', 'market_hkfuture': 'FUTURE_DAY_OPEN', 'market_usfuture': 'FUTURE_OPEN', 'market_sgfuture': 'FUTURE_DAY_OPEN', 'market_jpfuture': 'FUTURE_DAY_OPEN', 'server_ver': '504', 'trd_logined': True, 'timestamp': '1620963064', 'qot_logined': True, 'local_timestamp': 1620963064.124152, 'program_status_type': 'READY', 'program_status_desc': ''})
```









## <a href="#4500-2" class="header-anchor">#</a> GetGlobalState.proto

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  1002





`uint GetGlobalState(GetGlobalState.Request req)`  
`void OnReply_GetGlobalState(MMAPI_Conn client, uint nSerialNo, GetGlobalState.Response rsp)`

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn
    {
        MMAPI_Qot qot = new MMAPI_Qot();

        public Program()
        {
            qot.SetClientInfo("MMAPI4NET_Sample", 1);  //Set client information
            qot.SetConnCallback(this);  //Set connection callback
            qot.SetQotCallback(this);   //Set transaction callback
        }

        public void Start()
        {
            qot.InitConnect("127.0.0.1", (ushort)11111, false); //Start to connect to OpenD, the connection result is processed through OnInitConnect
        }


        public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
        {
            Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
            if (errCode != 0) //Connection failed
                return;

            //Connection is successful, you can make requests
            GetGlobalState.C2S c2s = GetGlobalState.C2S.CreateBuilder()
                    .SetUserID(0)
                    .Build();
            GetGlobalState.Request req = GetGlobalState.Request.CreateBuilder().SetC2S(c2s).Build();
            uint seqNo = qot.GetGlobalState(req);
            Console.WriteLine("Send GetGlobalState: {0}", seqNo1);
        }

        //This callback will be called after disconnection
        public void OnDisconnect(MMAPI_Conn client, long errCode)
        {
            Console.Write("Qot onDisConnect: {0}\n", errCode);
            qot.Close(); //Release the underlying resources
        }

        public void OnReply_GetGlobalState(MMAPI_Conn client, uint nSerialNo, GetGlobalState.Response rsp)
        {
            Console.Write("Reply: GetGlobalState: {0}\n", nSerialNo);
            Console.Write("marketHK: {0}, programStatus: {1} \n", rsp.S2C.MarketHK, rsp.S2C.ProgramStatus);
        }

        public static void Main(String[] args)
        {
            MMAPI.Init(); //Initialize the environment, call once when the program starts
            Program qot = new Program();
            qot.Start();

            while (true)
                Thread.Sleep(1000 * 600);
        }
    }
```





**Output**



``` cs
Qot onInitConnect: ret=0 desc= connID=6826777317655602340
Send GetGlobalState: 3
Reply: GetGlobalState: 3
marketHK: 5, programStatus: type: ProgramStatusType_Ready
```









`int getGlobalState(GetGlobalState.Request req);`  
`void onReply_GetGlobalState(MMAPI_Conn client, int nSerialNo, GetGlobalState.Response rsp)`

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1);  //Set client information
        qot.setConnSpi(this);  //Set connection callback
        qot.setQotSpi(this);   //Set market callback
    }

    public void start() throws IOException {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        GetGlobalState.C2S c2s = GetGlobalState.C2S.newBuilder()
                .setUserID(0)
                .build();
        GetGlobalState.Request req = GetGlobalState.Request.newBuilder().setC2S(c2s).build();
        qot.getGlobalState(req);
    }

    @Override
    public void onReply_GetGlobalState(MMAPI_Conn client, int nSerialNo, GetGlobalState.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetGlobalState failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetGlobalState: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
        MMAPI.init();
        QotDemo qot = new QotDemo();
        qot.start();

        while (true) {
            try {
                Thread.sleep(1000 * 60);
            } catch (InterruptedException exc) {

            }
        }
    }
}
```





- **Output**



``` text
Send QotGetGlobalState: 2
Receive QotGetGlobalState: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "marketHK": 6,
    "marketUS": 8,
    "marketSH": 6,
    "marketSZ": 6,
    "marketHKFuture": 17,
    "qotLogined": true,
    "trdLogined": true,
    "serverVer": 505,
    "serverBuildNo": 1707,
    "time": "1624523642",
    "localTime": 1.624523642858697E9,
    "programStatus": {
      "type": "ProgramStatusType_Ready"
    },
    "qotSvrIpAddr": "119.29.43.101",
    "trdSvrIpAddr": "119.29.43.101",
    "marketUSFuture": 23,
    "connID": "6813746013095493825",
    "marketSGFuture": 13,
    "marketJPFuture": 13
  }
}
```









`moomoo::u32_t GetGlobalState(const GetGlobalState::Request &stReq);`  
`virtual void OnReply_GetGlobalState(moomoo::u32_t nSerialNo, const GetGlobalState::Response &stRsp) = 0;`

- **Description**

  Get global status

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
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
        GetGlobalState::Request req;
        GetGlobalState::C2S *c2s = req.mutable_c2s();
        c2s->set_userid(0);

        m_GetGlobalStateSerialNo = m_pQotApi->GetGlobalState(req);
        cout << "Request GetGlobalState SerialNo: " << m_GetGlobalStateSerialNo << endl;
    }

    virtual void OnReply_GetGlobalState(moomoo::u32_t nSerialNo, const GetGlobalState::Response &stRsp){
        if(nSerialNo == m_GetGlobalStateSerialNo)
        {
            cout << "OnReply_GetGlobalState SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }
protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetGlobalStateSerialNo;
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
Request GetGlobalState SerialNo: 4
OnReply_GetGlobalState SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "marketHK": 6,
  "marketUS": 8,
  "marketSH": 6,
  "marketSZ": 6,
  "marketHKFuture": 15,
  "qotLogined": true,
  "trdLogined": true,
  "serverVer": 504,
  "serverBuildNo": 1608,
  "time": "1623226833",
  "localTime": 1623226833.8509541,
  "programStatus": {
   "type": 10
  },
  "qotSvrIpAddr": "106.55.66.8",
  "trdSvrIpAddr": "106.55.66.8",
  "marketUSFuture": 23,
  "connID": "6808306802122125817",
  "marketSGFuture": 13,
  "marketJPFuture": 13
 }
}
```









`GetGlobalState(req);`

- **Description**

  Get global status

- **Parameters**



``` protobuf

message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
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
    required int32 marketHK = 1; //Qot_Common.QotMarketState, the status of Hong Kong main-board market
    required int32 marketUS = 2; //Qot_Common.QotMarketState, the status of US Nasdaq market
    required int32 marketSH = 3; //Qot_Common.QotMarketState, the status of Shanghai stock market
    required int32 marketSZ = 4; //Qot_Common.QotMarketState, the status of Shenzhen market
    required int32 marketHKFuture = 5; //Qot_Common.QotMarketState, the status of the HK futures market
    optional int32 marketUSFuture = 15; //Qot_Common.QotMarketState, the status of the US futures market
    optional int32 marketSGFuture = 17; //Qot_Common.QotMarketState, the status of the SG futures market
    optional int32 marketJPFuture = 18; //Qot_Common.QotMarketState, the status of the JP futures market
    required bool qotLogined = 6; //Whether to log in to the market server
    required bool trdLogined = 7; //Whether to log in to the trading server
    required int32 serverVer = 8; //Version number
    required int32 serverBuildNo = 9; //buildNo
    required int64 time = 10; //Current server time
    optional double localTime = 11; //Current local time
    optional Common.ProgramStatus programStatus = 12; //Current status of program
    optional string qotSvrIpAddr = 13;
    optional string trdSvrIpAddr = 14;
    optional uint64 connID = 16; //Connection ID, the unique identifier of the connection
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For enumeration of market status, please refer to
>   [QotMarketState](/moomoo-api-doc/en/quote/quote.html#8663)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function GetGlobalState(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    userID: 0,
                },
            };

            websocket.GetGlobalState(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("GlobalState: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GlobalState: errCode 0, retMsg , retType 0
{
  "marketHK": 6,
  "marketUS": 8,
  "marketSH": 6,
  "marketSZ": 6,
  "marketHKFuture": 15,
  "qotLogined": true,
  "trdLogined": true,
  "serverVer": 507,
  "serverBuildNo": 1908,
  "time": "1631261759",
  "localTime": 1631261759.095172,
  "programStatus": {
    "type": "ProgramStatusType_Ready"
  },
  "qotSvrIpAddr": "119.29.48.17",
  "trdSvrIpAddr": "106.55.66.8",
  "marketUSFuture": 23,
  "connID": "6842007721202028582",
  "marketSGFuture": 13,
  "marketJPFuture": 13
}
stop
```



















