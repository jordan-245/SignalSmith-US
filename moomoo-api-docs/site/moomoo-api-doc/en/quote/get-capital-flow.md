



# <a href="#7876" class="header-anchor">#</a> Get Capital Flow









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_capital_flow(stock_code, period_type = PeriodType.INTRADAY, start=None, end=None)`

- **Description**

  Get the flow of a specific stock

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
  <td style="text-align: left;">stock_code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">period_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#2884">PeriodType</a></td>
  <td style="text-align: left;">Period Type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  Fotmat：yyyy-MM-dd<br />
  For example: "2017-06-20".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  Fotmat：yyyy-MM-dd<br />
  For example: "2017-06-20".
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | start type | end type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 365 days before ***end***. |
    | str | None | ***end*** is 365 days after ***start***. |
    | None | None | ***end*** is the current date, ***start*** is 365 days before. |

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
  <td>If ret == RET_OK, capital flow data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Capital flow data format as follows:
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
    <td style="text-align: left;">in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Net inflow of capital.</td>
    </tr>
    <tr>
    <td style="text-align: left;">main_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Block Orders Net Inflow.
    
      
    
    
     
    
    Only applicable to historical period (Day, Week, Month).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">super_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Extra-large Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">big_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Large Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">mid_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Medium Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">sml_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Small Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_flow_item_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Start time string.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    Unit: minute.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_valid_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last valid time string of data.
    
      
    
    
     
    
    Only applicable to intraday period.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_capital_flow("HK.00700", period_type = PeriodType.INTRADAY)
if ret == RET_OK:
    print(data)
    print(data['in_flow'][0]) # Take the first net inflow of capital
    print(data['in_flow'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    last_valid_time       in_flow  ...  main_in_flow  capital_flow_item_time
0               N/A -1.857915e+08  ... -1.066828e+08     2021-06-08 00:00:00
..              ...           ...  ...           ...                     ...
245             N/A  2.179240e+09  ...  2.143345e+09     2022-06-08 00:00:00

[246 rows x 8 columns]
-185791500.0
[-185791500.0, -18315000.0, -672100100.0, -714394350.0, -698391950.0, -818886750.0, 304827400.0, 73026200.0, -2078217500.0, 
..                   ...           ...                    ...
2031460.0, 638067040.0, 622466600.0, -351788160.0, -328529240.0, 715415020.0, 76749700.0, 2179240320.0]
```









## <a href="#2370" class="header-anchor">#</a> Qot_GetCapitalFlow.proto

- **Description**

  Get funding flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3211





`uint GetCapitalFlow(QotGetCapitalFlow.Request req);`  
`virtual void OnReply_GetCapitalFlow(FTAPI_Conn client, uint nSerialNo, QotGetCapitalFlow.Response rsp);`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Qot, FTSPI_Conn
{
    FTAPI_Qot qot = new FTAPI_Qot();

    public Program()
    {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
        qot.SetQotCallback(this); //Set transaction callback
    }

    public void Start()
    {
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
        QotGetCapitalFlow.C2S c2s = QotGetCapitalFlow.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetPeriodType((int)QotCommon.PeriodType.PeriodType_INTRADAY)
                .Build();
        QotGetCapitalFlow.Request req = QotGetCapitalFlow.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetCapitalFlow(req);
        Console.Write("Send QotGetCapitalFlow: {0}\n", seqNo);
    }


    public void OnDisconnect(FTAPI_Conn client, long errCode)
    {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetCapitalFlow(FTAPI_Conn client, uint nSerialNo, QotGetCapitalFlow.Response rsp)
    {
        Console.Write("Reply: QotGetCapitalFlow: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("inFlow: {0}\n", rsp.S2C.FlowItemListList[0].InFlow);
    }

    public static void Main(String[] args)
    {
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
Qot onInitConnect: ret=0 desc= connID=6939768707708965532
Send QotGetCapitalFlow: 3
Reply: QotGetCapitalFlow: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  flowItemList {
    inFlow: 0
    time: "2022-06-07 09:30:00"
    timestamp: 1654565400
    superInFlow: 0
    bigInFlow: 0
    midInFlow: 0
    smlInFlow: 0
  }
  flowItemList {
    inFlow: -48348560
    time: "2022-06-07 09:31:00"
    timestamp: 1654565460
    superInFlow: -32509240
    bigInFlow: -3675200
    midInFlow: -7317740
    smlInFlow: -4846380
  }
  flowItemList {
    inFlow: -21132380
    time: "2022-06-07 09:32:00"
    timestamp: 1654565520
    superInFlow: -32509240
    bigInFlow: -4001600
    midInFlow: 13582880
    smlInFlow: 1795580
  }
  flowItemList {
    inFlow: 44127520
    time: "2022-06-07 09:33:00"
    timestamp: 1654565580
    superInFlow: -9580000
    bigInFlow: 21937100
    midInFlow: 19888960
    smlInFlow: 11881460
  }
// ... 
  flowItemList {
    inFlow: 22462640
    time: "2022-06-07 10:43:00"
    timestamp: 1654569780
    superInFlow: -56322820
    bigInFlow: -27898060
    midInFlow: 45435080
    smlInFlow: 61248440
  }
  flowItemList {
    inFlow: 15506920
    time: "2022-06-07 10:44:00"
    timestamp: 1654569840
    superInFlow: -56322820
    bigInFlow: -32338060
    midInFlow: 44214740
    smlInFlow: 59953060
  }
  lastValidTime: "2022-06-07 10:43:44"
}

inFlow: 0
```









`int getCapitalFlow(QotGetCapitalFlow.Request req);`  
`void onReply_GetCapitalFlow(FTAPI_Conn client, int nSerialNo, QotGetCapitalFlow.Response rsp);`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
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
                .setCode("00700")
                .build();
        QotGetCapitalFlow.C2S c2s = QotGetCapitalFlow.C2S.newBuilder()
                .setSecurity(sec)
            .build();
        QotGetCapitalFlow.Request req = QotGetCapitalFlow.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getCapitalFlow(req);
        System.out.printf("Send QotGetCapitalFlow: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetCapitalFlow(FTAPI_Conn client, int nSerialNo, QotGetCapitalFlow.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetCapitalFlow failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetCapitalFlow: %s\n", json);
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
Send QotGetCapitalFlow: 2
Receive QotGetCapitalFlow: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "flowItemList": [{
      "inFlow": 0.0,
      "time": "2022-06-08 09:30:00",
      "timestamp": 1.6546518E9,
      "superInFlow": 0.0,
      "bigInFlow": 0.0,
      "midInFlow": 0.0,
      "smlInFlow": 0.0
    }, {
      "inFlow": -4960940.0,
      "time": "2022-06-08 09:31:00",
      "timestamp": 1.65465186E9,
      "superInFlow": 0.0,
      "bigInFlow": -4857400.0,
      "midInFlow": -1.004904E7,
      "smlInFlow": 9945500.0
    }, {
      "inFlow": -3260340.0,
      "time": "2022-06-08 09:32:00",
      "timestamp": 1.65465192E9,
      "superInFlow": -8140120.0,
      "bigInFlow": -4857400.0,
      "midInFlow": -7800660.0,
      "smlInFlow": 1.753784E7
    }, {
      "inFlow": 5.715794E7,
      "time": "2022-06-08 09:33:00",
      "timestamp": 1.65465198E9,
      "superInFlow": 3.382238E7,
      "bigInFlow": 3508240.0,
      "midInFlow": 337820.0,
      "smlInFlow": 1.94895E7
    }, {
      "inFlow": 6.58145E7,
      "time": "2022-06-08 09:34:00",
      "timestamp": 1.65465204E9,
      "superInFlow": 4.114658E7,
      "bigInFlow": -1.335444E7,
      "midInFlow": 1.37937E7,
      "smlInFlow": 2.422866E7
    }, {
      "inFlow": 3.258944E7,
      "time": "2022-06-08 09:35:00",
      "timestamp": 1.6546521E9,
      "superInFlow": 4.114658E7,
      "bigInFlow": -2.083698E7,
      "midInFlow": 8570020.0,
      "smlInFlow": 3709820.0
    }, 
    //...
    {
      "inFlow": 1.4041278E9,
      "time": "2022-06-08 10:46:00",
      "timestamp": 1.65465636E9,
      "superInFlow": 5.3349552E8,
      "bigInFlow": 4.287602E8,
      "midInFlow": 2.4805104E8,
      "smlInFlow": 1.9382104E8
    }, {
      "inFlow": 1.38049732E9,
      "time": "2022-06-08 10:47:00",
      "timestamp": 1.65465642E9,
      "superInFlow": 5.1425064E8,
      "bigInFlow": 4.287602E8,
      "midInFlow": 2.4901564E8,
      "smlInFlow": 1.8847084E8
    }],
    "lastValidTime": "2022-06-08 10:47:25"
  }
}
```









`Futu::u32_t GetCapitalFlow(const Qot_GetCapitalFlow::Request &stReq);`  
`virtual void OnReply_GetCapitalFlow(Futu::u32_t nSerialNo, const Qot_GetCapitalFlow::Response &stRsp) = 0;`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
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
        Qot_GetCapitalFlow::Request req;
        Qot_GetCapitalFlow::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_periodtype(Qot_Common::PeriodType::PeriodType_INTRADAY);
        m_pQotApi->GetCapitalFlow(req);
        cout << "GetCapitalFlow" << endl;
    }

    virtual void OnReply_GetCapitalFlow(Futu::u32_t nSerialNo, const Qot_GetCapitalFlow::Response &stRsp){
        cout << "OnReply_GetCapitalFlow:" << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    FTAPI_Qot *m_pQotApi; 
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
GetCapitalFlow
OnReply_GetCapitalFlow:
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "flowItemList": [
   {
    "inFlow": 0,
    "time": "2022-06-08 09:30:00",
    "timestamp": 1654651800,
    "superInFlow": 0,
    "bigInFlow": 0,
    "midInFlow": 0,
    "smlInFlow": 0
   },
   {
    "inFlow": -4960940,
    "time": "2022-06-08 09:31:00",
    "timestamp": 1654651860,
    "superInFlow": 0,
    "bigInFlow": -4857400,
    "midInFlow": -10049040,
    "smlInFlow": 9945500
   },
   {
    "inFlow": -3260340,
    "time": "2022-06-08 09:32:00",
    "timestamp": 1654651920,
    "superInFlow": -8140120,
    "bigInFlow": -4857400,
    "midInFlow": -7800660,
    "smlInFlow": 17537840
   },
// ...
   {
    "inFlow": 1404127800,
    "time": "2022-06-08 10:46:00",
    "timestamp": 1654656360,
    "superInFlow": 533495520,
    "bigInFlow": 428760200,
    "midInFlow": 248051040,
    "smlInFlow": 193821040
   },
   {
    "inFlow": 1387351340,
    "time": "2022-06-08 10:47:00",
    "timestamp": 1654656420,
    "superInFlow": 514250640,
    "bigInFlow": 428760200,
    "midInFlow": 253136620,
    "smlInFlow": 191203880
   }
  ],
  "lastValidTime": "2022-06-08 10:47:00"
 }
}
```









`GetCapitalFlow(req);`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
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
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetCapitalFlow(){
    const { RetType } = Common
    const { PeriodType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security: {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    periodType: PeriodType.PeriodType_INTRADAY,
                },
            };
            websocket.GetCapitalFlow(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("CapitalFlow: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
CapitalFlow: errCode 0, retMsg , retType 0
{
  "flowItemList": [{
    "inFlow": -4960940,
    "time": "2022-06-08 09:30:00",
    "timestamp": 1654651800,
    "superInFlow": 0.0,
    "bigInFlow": -4857400.0,
    "midInFlow": -1004904.0,
    "smlInFlow": 9945500.0
  }, ..., {
    "inFlow": 944752820,
    "time": "2022-06-08 10:24:00",
    "timestamp": 1654655040,
    "superInFlow": 53349552.0,
    "bigInFlow": 4287602.0,
    "midInFlow": 24805104.0,
    "smlInFlow": 19382104.0
  }],
  "lastValidTime": "2022-06-08 10:24:00"
}
stop
```











Interface Limitations

- A maximum of 30 requests per 30 seconds
- Supported for stocks, warrants and funds only
- Historical period (day, month, year) Only provides data for the latest
  1 year; Intraday period only provides data for the latest day.
- Data with historical period (day, month, year), is only supported for
  the last 2 years. While Data with intraday period is only supported
  for the latest day.
- Output data only includes tha data during Regular Trading Hours, not
  the data during Pre and Post-Market Hours.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_capital_flow(stock_code, period_type = PeriodType.INTRADAY, start=None, end=None)`

- **Description**

  Get the flow of a specific stock

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
  <td style="text-align: left;">stock_code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">period_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#2884">PeriodType</a></td>
  <td style="text-align: left;">Period Type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  Fotmat：yyyy-MM-dd<br />
  For example: "2017-06-20".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  Fotmat：yyyy-MM-dd<br />
  For example: "2017-06-20".
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | start type | end type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 365 days before ***end***. |
    | str | None | ***end*** is 365 days after ***start***. |
    | None | None | ***end*** is the current date, ***start*** is 365 days before. |

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
  <td>If ret == RET_OK, capital flow data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Capital flow data format as follows:
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
    <td style="text-align: left;">in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Net inflow of capital.</td>
    </tr>
    <tr>
    <td style="text-align: left;">main_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Block Orders Net Inflow.
    
      
    
    
     
    
    Only applicable to historical period (Day, Week, Month).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">super_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Extra-large Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">big_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Large Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">mid_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Medium Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">sml_in_flow</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Small Orders Net Inflow.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_flow_item_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Start time string.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    Unit: minute.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_valid_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last valid time string of data.
    
      
    
    
     
    
    Only applicable to intraday period.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_capital_flow("HK.00700", period_type = PeriodType.INTRADAY)
if ret == RET_OK:
    print(data)
    print(data['in_flow'][0]) # Take the first net inflow of capital
    print(data['in_flow'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    last_valid_time       in_flow  ...  main_in_flow  capital_flow_item_time
0               N/A -1.857915e+08  ... -1.066828e+08     2021-06-08 00:00:00
..              ...           ...  ...           ...                     ...
245             N/A  2.179240e+09  ...  2.143345e+09     2022-06-08 00:00:00

[246 rows x 8 columns]
-185791500.0
[-185791500.0, -18315000.0, -672100100.0, -714394350.0, -698391950.0, -818886750.0, 304827400.0, 73026200.0, -2078217500.0, 
..                   ...           ...                    ...
2031460.0, 638067040.0, 622466600.0, -351788160.0, -328529240.0, 715415020.0, 76749700.0, 2179240320.0]
```









## <a href="#2370-2" class="header-anchor">#</a> Qot_GetCapitalFlow.proto

- **Description**

  Get funding flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3211





`uint GetCapitalFlow(QotGetCapitalFlow.Request req);`  
`virtual void OnReply_GetCapitalFlow(FTAPI_Conn client, uint nSerialNo, QotGetCapitalFlow.Response rsp);`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn
{
    MMAPI_Qot qot = new MMAPI_Qot();

    public Program()
    {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
        qot.SetQotCallback(this); //Set transaction callback
    }

    public void Start()
    {
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
        QotGetCapitalFlow.C2S c2s = QotGetCapitalFlow.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetPeriodType((int)QotCommon.PeriodType.PeriodType_INTRADAY)
                .Build();
        QotGetCapitalFlow.Request req = QotGetCapitalFlow.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetCapitalFlow(req);
        Console.Write("Send QotGetCapitalFlow: {0}\n", seqNo);
    }


    public void OnDisconnect(MMAPI_Conn client, long errCode)
    {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetCapitalFlow(MMAPI_Conn client, uint nSerialNo, QotGetCapitalFlow.Response rsp)
    {
        Console.Write("Reply: QotGetCapitalFlow: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("inFlow: {0}\n", rsp.S2C.FlowItemListList[0].InFlow);
    }

    public static void Main(String[] args)
    {
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
Qot onInitConnect: ret=0 desc= connID=6939768707708965532
Send QotGetCapitalFlow: 3
Reply: QotGetCapitalFlow: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  flowItemList {
    inFlow: 0
    time: "2022-06-07 09:30:00"
    timestamp: 1654565400
    superInFlow: 0
    bigInFlow: 0
    midInFlow: 0
    smlInFlow: 0
  }
  flowItemList {
    inFlow: -48348560
    time: "2022-06-07 09:31:00"
    timestamp: 1654565460
    superInFlow: -32509240
    bigInFlow: -3675200
    midInFlow: -7317740
    smlInFlow: -4846380
  }
  flowItemList {
    inFlow: -21132380
    time: "2022-06-07 09:32:00"
    timestamp: 1654565520
    superInFlow: -32509240
    bigInFlow: -4001600
    midInFlow: 13582880
    smlInFlow: 1795580
  }
  flowItemList {
    inFlow: 44127520
    time: "2022-06-07 09:33:00"
    timestamp: 1654565580
    superInFlow: -9580000
    bigInFlow: 21937100
    midInFlow: 19888960
    smlInFlow: 11881460
  }
// ... 
  flowItemList {
    inFlow: 22462640
    time: "2022-06-07 10:43:00"
    timestamp: 1654569780
    superInFlow: -56322820
    bigInFlow: -27898060
    midInFlow: 45435080
    smlInFlow: 61248440
  }
  flowItemList {
    inFlow: 15506920
    time: "2022-06-07 10:44:00"
    timestamp: 1654569840
    superInFlow: -56322820
    bigInFlow: -32338060
    midInFlow: 44214740
    smlInFlow: 59953060
  }
  lastValidTime: "2022-06-07 10:43:44"
}

inFlow: 0
```









`int getCapitalFlow(QotGetCapitalFlow.Request req);`  
`void onReply_GetCapitalFlow(MMAPI_Conn client, int nSerialNo, QotGetCapitalFlow.Response rsp);`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
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
                .setCode("00700")
                .build();
        QotGetCapitalFlow.C2S c2s = QotGetCapitalFlow.C2S.newBuilder()
                .setSecurity(sec)
            .build();
        QotGetCapitalFlow.Request req = QotGetCapitalFlow.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getCapitalFlow(req);
        System.out.printf("Send QotGetCapitalFlow: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetCapitalFlow(MMAPI_Conn client, int nSerialNo, QotGetCapitalFlow.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetCapitalFlow failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetCapitalFlow: %s\n", json);
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
Send QotGetCapitalFlow: 2
Receive QotGetCapitalFlow: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "flowItemList": [{
      "inFlow": 0.0,
      "time": "2022-06-08 09:30:00",
      "timestamp": 1.6546518E9,
      "superInFlow": 0.0,
      "bigInFlow": 0.0,
      "midInFlow": 0.0,
      "smlInFlow": 0.0
    }, {
      "inFlow": -4960940.0,
      "time": "2022-06-08 09:31:00",
      "timestamp": 1.65465186E9,
      "superInFlow": 0.0,
      "bigInFlow": -4857400.0,
      "midInFlow": -1.004904E7,
      "smlInFlow": 9945500.0
    }, {
      "inFlow": -3260340.0,
      "time": "2022-06-08 09:32:00",
      "timestamp": 1.65465192E9,
      "superInFlow": -8140120.0,
      "bigInFlow": -4857400.0,
      "midInFlow": -7800660.0,
      "smlInFlow": 1.753784E7
    }, {
      "inFlow": 5.715794E7,
      "time": "2022-06-08 09:33:00",
      "timestamp": 1.65465198E9,
      "superInFlow": 3.382238E7,
      "bigInFlow": 3508240.0,
      "midInFlow": 337820.0,
      "smlInFlow": 1.94895E7
    }, {
      "inFlow": 6.58145E7,
      "time": "2022-06-08 09:34:00",
      "timestamp": 1.65465204E9,
      "superInFlow": 4.114658E7,
      "bigInFlow": -1.335444E7,
      "midInFlow": 1.37937E7,
      "smlInFlow": 2.422866E7
    }, {
      "inFlow": 3.258944E7,
      "time": "2022-06-08 09:35:00",
      "timestamp": 1.6546521E9,
      "superInFlow": 4.114658E7,
      "bigInFlow": -2.083698E7,
      "midInFlow": 8570020.0,
      "smlInFlow": 3709820.0
    }, 
    //...
    {
      "inFlow": 1.4041278E9,
      "time": "2022-06-08 10:46:00",
      "timestamp": 1.65465636E9,
      "superInFlow": 5.3349552E8,
      "bigInFlow": 4.287602E8,
      "midInFlow": 2.4805104E8,
      "smlInFlow": 1.9382104E8
    }, {
      "inFlow": 1.38049732E9,
      "time": "2022-06-08 10:47:00",
      "timestamp": 1.65465642E9,
      "superInFlow": 5.1425064E8,
      "bigInFlow": 4.287602E8,
      "midInFlow": 2.4901564E8,
      "smlInFlow": 1.8847084E8
    }],
    "lastValidTime": "2022-06-08 10:47:25"
  }
}
```









`moomoo::u32_t GetCapitalFlow(const Qot_GetCapitalFlow::Request &stReq);`  
`virtual void OnReply_GetCapitalFlow(moomoo::u32_t nSerialNo, const Qot_GetCapitalFlow::Response &stRsp) = 0;`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
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
        Qot_GetCapitalFlow::Request req;
        Qot_GetCapitalFlow::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_periodtype(Qot_Common::PeriodType::PeriodType_INTRADAY);
        m_pQotApi->GetCapitalFlow(req);
        cout << "GetCapitalFlow" << endl;
    }

    virtual void OnReply_GetCapitalFlow(moomoo::u32_t nSerialNo, const Qot_GetCapitalFlow::Response &stRsp){
        cout << "OnReply_GetCapitalFlow:" << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    MMAPI_Qot *m_pQotApi; 
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
GetCapitalFlow
OnReply_GetCapitalFlow:
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "flowItemList": [
   {
    "inFlow": 0,
    "time": "2022-06-08 09:30:00",
    "timestamp": 1654651800,
    "superInFlow": 0,
    "bigInFlow": 0,
    "midInFlow": 0,
    "smlInFlow": 0
   },
   {
    "inFlow": -4960940,
    "time": "2022-06-08 09:31:00",
    "timestamp": 1654651860,
    "superInFlow": 0,
    "bigInFlow": -4857400,
    "midInFlow": -10049040,
    "smlInFlow": 9945500
   },
   {
    "inFlow": -3260340,
    "time": "2022-06-08 09:32:00",
    "timestamp": 1654651920,
    "superInFlow": -8140120,
    "bigInFlow": -4857400,
    "midInFlow": -7800660,
    "smlInFlow": 17537840
   },
// ...
   {
    "inFlow": 1404127800,
    "time": "2022-06-08 10:46:00",
    "timestamp": 1654656360,
    "superInFlow": 533495520,
    "bigInFlow": 428760200,
    "midInFlow": 248051040,
    "smlInFlow": 193821040
   },
   {
    "inFlow": 1387351340,
    "time": "2022-06-08 10:47:00",
    "timestamp": 1654656420,
    "superInFlow": 514250640,
    "bigInFlow": 428760200,
    "midInFlow": 253136620,
    "smlInFlow": 191203880
   }
  ],
  "lastValidTime": "2022-06-08 10:47:00"
 }
}
```









`GetCapitalFlow(req);`

- **Description**

  Get capital flow

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
    optional int32 periodType = 2; // Qot_Common.PeriodType Period Type
    optional string beginTime = 3; // Start time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
    optional string endTime = 4; // End time (Fotmat：yyyy-MM-dd). Only applicable to historical period (Day, Week, Month)
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For period type, refer to
>   [PeriodType](/moomoo-api-doc/en/quote/quote.html#2884)

- **Return**



``` protobuf
message CapitalFlowItem
{
    required double inFlow = 1; //Net inflow of capital, a positive number means capital inflow and a negative number means capital outflow
    optional string time = 2; //Start time string, in minutes (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 3; //Start timestamp
    optional double mainInFlow = 4; // Block Orders Net Inflow. Only applicable to historical period (Day, Week, Month)
    optional double superInFlow = 5; // Extra-large Orders Net Inflow.
    optional double bigInFlow = 6; // Big Orders Net Inflow.
    optional double midInFlow = 7; // Medium Orders Net Inflow.
    optional double smlInFlow = 8; // Small Orders Net Inflow.
}

message S2C
{
    repeated CapitalFlowItem flowItemList = 1; //Capital flow direction
    optional string lastValidTime = 2; //Data last valid time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double lastValidTimestamp = 3; //The last valid timestamp of the data
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
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
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetCapitalFlow(){
    const { RetType } = Common
    const { PeriodType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security: {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    periodType: PeriodType.PeriodType_INTRADAY,
                },
            };
            websocket.GetCapitalFlow(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("CapitalFlow: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
CapitalFlow: errCode 0, retMsg , retType 0
{
  "flowItemList": [{
    "inFlow": -4960940,
    "time": "2022-06-08 09:30:00",
    "timestamp": 1654651800,
    "superInFlow": 0.0,
    "bigInFlow": -4857400.0,
    "midInFlow": -1004904.0,
    "smlInFlow": 9945500.0
  }, ..., {
    "inFlow": 944752820,
    "time": "2022-06-08 10:24:00",
    "timestamp": 1654655040,
    "superInFlow": 53349552.0,
    "bigInFlow": 4287602.0,
    "midInFlow": 24805104.0,
    "smlInFlow": 19382104.0
  }],
  "lastValidTime": "2022-06-08 10:24:00"
}
stop
```











Interface Limitations

- A maximum of 30 requests per 30 seconds
- Supported for stocks, warrants and funds only
- Historical period (day, month, year) Only provides data for the latest
  1 year; Intraday period only provides data for the latest day.
- Data with historical period (day, month, year), is only supported for
  the last 2 years. While Data with intraday period is only supported
  for the latest day.
- Output data only includes tha data during Regular Trading Hours, not
  the data during Pre and Post-Market Hours.













