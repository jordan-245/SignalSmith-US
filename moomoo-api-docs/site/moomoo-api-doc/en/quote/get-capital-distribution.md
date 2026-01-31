



# <a href="#2346" class="header-anchor">#</a> Get Capital Distribution









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_capital_distribution(stock_code)`

- **Description**

  Access to capital distribution

- **Parameters**

  | Parameter  | Type | Description |
  |:-----------|:-----|:------------|
  | stock_code | str  | Stock code. |

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
  <td>If ret == RET_OK, stock fund distribution data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock fund distribution data format as follows:
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
    <td style="text-align: left;">capital_in_super</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, extra-large
    order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_in_big</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, large order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_in_mid</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, midium order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_in_small</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, small order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_super</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, extra-large
    order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_big</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, large order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_mid</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, midium order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_small</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, small order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">update_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Updated time string.
    
      
    
    
     
    
    Fotmat：yyyy-MM-dd HH:mm:ss
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_capital_distribution("HK.00700")
if ret == RET_OK:
    print(data)
    print(data['capital_in_big'][0]) # Take the amount of inflow capital of the first article, big order
    print(data['capital_in_big'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
   capital_in_super  capital_in_big  ...  capital_out_small          update_time
0      2.261085e+09    2.141964e+09  ...       2.887413e+09  2022-06-08 15:59:59

[1 rows x 9 columns]
2141963720.0
[2141963720.0]
```









## <a href="#753" class="header-anchor">#</a> Qot_GetCapitalDistribution.proto

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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

  3212





`uint GetCapitalDistribution(QotGetCapitalDistribution.Request req);`  
`virtual void OnReply_GetCapitalDistribution(FTAPI_Conn client, uint nSerialNo, QotGetCapitalDistribution.Response rsp);`

- **Description**

  Access to funds distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
        QotGetCapitalDistribution.C2S c2s = QotGetCapitalDistribution.C2S.CreateBuilder()
                .SetSecurity(sec)
                .Build();
        QotGetCapitalDistribution.Request req = QotGetCapitalDistribution.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetCapitalDistribution(req);
        Console.Write("Send QotGetCapitalDistribution: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetCapitalDistribution(FTAPI_Conn client, uint nSerialNo, QotGetCapitalDistribution.Response rsp)
    {
        Console.Write("Reply: QotGetCapitalDistribution: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("inFlow: {0}\n", rsp.S2C.CapitalInBig);
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
Qot onInitConnect: ret=0 desc= connID=6825683696684969514
Send QotGetCapitalDistribution: 3
Reply: QotGetCapitalDistribution: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  capitalInBig: 299700820
  capitalInMid: 521403800
  capitalInSmall: 740895620
  capitalOutBig: 332038880
  capitalOutMid: 483401260
  capitalOutSmall: 682124080
  updateTime: "2022-06-07 10:46:02"
  updateTimestamp: 1654569962
  capitalInSuper: 230158560
  capitalOutSuper: 286481380
}

inFlow: 299700820
```









`int getCapitalDistribution(QotGetCapitalDistribution.Request req);`  
`void onReply_GetCapitalDistribution(FTAPI_Conn client, int nSerialNo, QotGetCapitalDistribution.Response rsp);`

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
        QotGetCapitalDistribution.C2S c2s = QotGetCapitalDistribution.C2S.newBuilder()
                .setSecurity(sec)
                .build();
        QotGetCapitalDistribution.Request req = QotGetCapitalDistribution.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getCapitalDistribution(req);
        System.out.printf("Send QotGetCapitalDistribution: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetCapitalDistribution(FTAPI_Conn client, int nSerialNo, QotGetCapitalDistribution.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetCapitalDistribution failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetCapitalDistribution: %s\n", json);
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
Send QotGetCapitalDistribution: 2
Receive QotGetCapitalDistribution: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "capitalInBig": 8.6653274E8,
    "capitalInMid": 7.6876998E8,
    "capitalInSmall": 1.02038782E9,
    "capitalOutBig": 4.4806512E8,
    "capitalOutMid": 5.0682792E8,
    "capitalOutSmall": 8.1260248E8,
    "updateTime": "2022-06-08 10:44:34",
    "updateTimestamp": 1.654656274E9,
    "capitalInSuper": 8.2496766E8,
    "capitalOutSuper": 2.6721714E8
  }
}
```









`Futu::u32_t GetCapitalDistribution(const Qot_GetCapitalDistribution::Request &stReq);`  
`virtual void OnReply_GetCapitalDistribution(Futu::u32_t nSerialNo, const Qot_GetCapitalDistribution::Response &stRsp) = 0;`

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
        Qot_GetCapitalDistribution::Request req;
        Qot_GetCapitalDistribution::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetCapitalDistributionSerialNo = m_pQotApi->GetCapitalDistribution(req);
        cout << "Request GetCapitalDistribution SerialNo: " << m_GetCapitalDistributionSerialNo << endl;
    }

    virtual void OnReply_GetCapitalDistribution(Futu::u32_t nSerialNo, const Qot_GetCapitalDistribution::Response &stRsp){
        if(nSerialNo == m_GetCapitalDistributionSerialNo)
        {
            cout << "OnReply_GetCapitalDistribution SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetCapitalDistributionSerialNo;
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
Request GetCapitalDistribution SerialNo: 3
OnReply_GetCapitalDistribution SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "capitalInBig": 859479380,
  "capitalInMid": 763181580,
  "capitalInSmall": 1011289940,
  "capitalOutBig": 444405720,
  "capitalOutMid": 503977520,
  "capitalOutSmall": 807438760,
  "updateTime": "2022-06-08 10:44:21",
  "updateTimestamp": 1654656261,
  "capitalInSuper": 824967660,
  "capitalOutSuper": 252818140
 }
}
```









`GetCapitalDistribution(req);`

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetCapitalDistribution(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
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
                },
            };
            websocket.GetCapitalDistribution(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("CapitalDistribution: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
CapitalDistribution: errCode 0, retMsg , retType 0
{
  "capitalInBig": 1586950080,
  "capitalInMid": 2861135060,
  "capitalInSmall": 879906120,
  "capitalOutBig": 890005200,
  "capitalOutMid": 2423820040,
  "capitalOutSmall": 799307540,
  "updateTime": "2021-09-10 11:57:30",
  "updateTimestamp": 1631246250,
  "capitalInSuper": 230158560,
  "capitalOutSuper": 286481380
}
stop
```











Interface Limitations

- A maximum of 30 requests per 30 seconds
- Only support stocks, warrants and funds.
- For more capital flow introduction, please refer to
  <a href="https://support.futunn.com/en-us/topic498?lang=en-US"
  target="_blank" rel="noopener noreferrer">here</a>.
- Output data only includes tha data during Regular Trading Hours, not
  the data during Pre and Post-Market Hours.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_capital_distribution(stock_code)`

- **Description**

  Access to capital distribution

- **Parameters**

  | Parameter  | Type | Description |
  |:-----------|:-----|:------------|
  | stock_code | str  | Stock code. |

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
  <td>If ret == RET_OK, stock fund distribution data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock fund distribution data format as follows:
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
    <td style="text-align: left;">capital_in_super</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, extra-large
    order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_in_big</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, large order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_in_mid</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, midium order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_in_small</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Inflow capital quota, small order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_super</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, extra-large
    order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_big</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, large order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_mid</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, midium order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">capital_out_small</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Outflow capital quota, small order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">update_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Updated time string.
    
      
    
    
     
    
    Fotmat：yyyy-MM-dd HH:mm:ss
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_capital_distribution("HK.00700")
if ret == RET_OK:
    print(data)
    print(data['capital_in_big'][0]) # Take the amount of inflow capital of the first article, big order
    print(data['capital_in_big'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
   capital_in_super  capital_in_big  ...  capital_out_small          update_time
0      2.261085e+09    2.141964e+09  ...       2.887413e+09  2022-06-08 15:59:59

[1 rows x 9 columns]
2141963720.0
[2141963720.0]
```









## <a href="#753-2" class="header-anchor">#</a> Qot_GetCapitalDistribution.proto

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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

  3212





`uint GetCapitalDistribution(QotGetCapitalDistribution.Request req);`  
`virtual void OnReply_GetCapitalDistribution(MMAPI_Conn client, uint nSerialNo, QotGetCapitalDistribution.Response rsp);`

- **Description**

  Access to funds distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
        QotGetCapitalDistribution.C2S c2s = QotGetCapitalDistribution.C2S.CreateBuilder()
                .SetSecurity(sec)
                .Build();
        QotGetCapitalDistribution.Request req = QotGetCapitalDistribution.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetCapitalDistribution(req);
        Console.Write("Send QotGetCapitalDistribution: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetCapitalDistribution(MMAPI_Conn client, uint nSerialNo, QotGetCapitalDistribution.Response rsp)
    {
        Console.Write("Reply: QotGetCapitalDistribution: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("inFlow: {0}\n", rsp.S2C.CapitalInBig);
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
Qot onInitConnect: ret=0 desc= connID=6825683696684969514
Send QotGetCapitalDistribution: 3
Reply: QotGetCapitalDistribution: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  capitalInBig: 299700820
  capitalInMid: 521403800
  capitalInSmall: 740895620
  capitalOutBig: 332038880
  capitalOutMid: 483401260
  capitalOutSmall: 682124080
  updateTime: "2022-06-07 10:46:02"
  updateTimestamp: 1654569962
  capitalInSuper: 230158560
  capitalOutSuper: 286481380
}

inFlow: 299700820
```









`int getCapitalDistribution(QotGetCapitalDistribution.Request req);`  
`void onReply_GetCapitalDistribution(MMAPI_Conn client, int nSerialNo, QotGetCapitalDistribution.Response rsp);`

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
        QotGetCapitalDistribution.C2S c2s = QotGetCapitalDistribution.C2S.newBuilder()
                .setSecurity(sec)
                .build();
        QotGetCapitalDistribution.Request req = QotGetCapitalDistribution.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getCapitalDistribution(req);
        System.out.printf("Send QotGetCapitalDistribution: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetCapitalDistribution(MMAPI_Conn client, int nSerialNo, QotGetCapitalDistribution.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetCapitalDistribution failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetCapitalDistribution: %s\n", json);
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
Send QotGetCapitalDistribution: 2
Receive QotGetCapitalDistribution: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "capitalInBig": 8.6653274E8,
    "capitalInMid": 7.6876998E8,
    "capitalInSmall": 1.02038782E9,
    "capitalOutBig": 4.4806512E8,
    "capitalOutMid": 5.0682792E8,
    "capitalOutSmall": 8.1260248E8,
    "updateTime": "2022-06-08 10:44:34",
    "updateTimestamp": 1.654656274E9,
    "capitalInSuper": 8.2496766E8,
    "capitalOutSuper": 2.6721714E8
  }
}
```









`moomoo::u32_t GetCapitalDistribution(const Qot_GetCapitalDistribution::Request &stReq);`  
`virtual void OnReply_GetCapitalDistribution(moomoo::u32_t nSerialNo, const Qot_GetCapitalDistribution::Response &stRsp) = 0;`

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
        Qot_GetCapitalDistribution::Request req;
        Qot_GetCapitalDistribution::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetCapitalDistributionSerialNo = m_pQotApi->GetCapitalDistribution(req);
        cout << "Request GetCapitalDistribution SerialNo: " << m_GetCapitalDistributionSerialNo << endl;
    }

    virtual void OnReply_GetCapitalDistribution(moomoo::u32_t nSerialNo, const Qot_GetCapitalDistribution::Response &stRsp){
        if(nSerialNo == m_GetCapitalDistributionSerialNo)
        {
            cout << "OnReply_GetCapitalDistribution SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetCapitalDistributionSerialNo;
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
Request GetCapitalDistribution SerialNo: 3
OnReply_GetCapitalDistribution SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "capitalInBig": 859479380,
  "capitalInMid": 763181580,
  "capitalInSmall": 1011289940,
  "capitalOutBig": 444405720,
  "capitalOutMid": 503977520,
  "capitalOutSmall": 807438760,
  "updateTime": "2022-06-08 10:44:21",
  "updateTimestamp": 1654656261,
  "capitalInSuper": 824967660,
  "capitalOutSuper": 252818140
 }
}
```









`GetCapitalDistribution(req);`

- **Description**

  Access to capital distribution

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Stock
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
    // According to the historical transaction records, the tick-by-tick transactions are divided into large orders, medium orders and small orders. Take the average turnover of each transaction in the previous month (or in the past three days for warrants) as the reference value. Transactions whose turnover is less than the average value are called small orders. Transactions whose turnover is more than or equal to 10 times of the average value are called large orders. Transactions beside small orders and large orders are called midium orders.
    optional double capitalInSuper = 9; // Inflow capital order, extra-large order.
    required double capitalInBig = 1; //Inflow capital order, large order
    required double capitalInMid = 2; //Inflow capital order, midium order
    required double capitalInSmall = 3; //Inflow capital order, small order
    optional double capitalOutSuper = 10; // Outflow capital order, extra-large order.
    required double capitalOutBig = 4; //Outflow capital order, large order
    required double capitalOutMid = 5; //Outflow capital order, midium order
    required double capitalOutSmall = 6; //Outflow capital order, small order
    optional string updateTime = 7; //Updates time string (Format: yyyy-MM-dd HH:mm:ss)
    optional double updateTimestamp = 8; //Updates timestamp
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
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetCapitalDistribution(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
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
                },
            };
            websocket.GetCapitalDistribution(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("CapitalDistribution: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
CapitalDistribution: errCode 0, retMsg , retType 0
{
  "capitalInBig": 1586950080,
  "capitalInMid": 2861135060,
  "capitalInSmall": 879906120,
  "capitalOutBig": 890005200,
  "capitalOutMid": 2423820040,
  "capitalOutSmall": 799307540,
  "updateTime": "2021-09-10 11:57:30",
  "updateTimestamp": 1631246250,
  "capitalInSuper": 230158560,
  "capitalOutSuper": 286481380
}
stop
```











Interface Limitations

- A maximum of 30 requests per 30 seconds
- Only support stocks, warrants and funds.
- For more capital flow introduction, please refer to
  <a href="https://support.futunn.com/en-us/topic498?lang=en-US"
  target="_blank" rel="noopener noreferrer">here</a>.
- Output data only includes tha data during Regular Trading Hours, not
  the data during Pre and Post-Market Hours.













