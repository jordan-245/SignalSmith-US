



# <a href="#9606" class="header-anchor">#</a> Get Related Data of a Specific Security









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_referencestock_list(code, reference_type)`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contracts related to futures

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | code | str | Stock code. |
  | reference_type | [SecurityReferenceType](/moomoo-api-doc/en/quote/quote.html#8136) | Related data type to be obtained. |

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
  <td>If ret == RET_OK, related data of security is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Related data of security fotmat as follows:
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
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of shares per lot, contract
    multiplier for futures.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Security type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">list_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time of listing.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether it is a warrant.
    
      
    
    
     
    
    If it is True, the following field start with 'wrt' is valid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
    <td style="text-align: left;">Warrant type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The underlying stock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether it is a future.
    
      
    
    
     
    
    If it is True, the following field start with 'future' is valid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">future_main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the future main contract.
    
      
    
    
     
    
    Special field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">future_last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.
    
      
    
    
     
    
    The field is unique to futures.<br />
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

# Get warrants related to the underlying stock
ret, data = quote_ctx.get_referencestock_list('HK.00700', SecurityReferenceType.WARRANT)
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
print('******************************************')
# Port related contracts
ret, data = quote_ctx.get_referencestock_list('HK.A50main', SecurityReferenceType.FUTURE)
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
        code  lot_size stock_type stock_name   list_time  wrt_valid wrt_type  wrt_code  future_valid  future_main_contract  future_last_trade_time
0     HK.24719      1000    WARRANT     TENGXUNDONGYAJIUSIGUA  2018-07-20       True      PUT  HK.00700         False                   NaN                     NaN
...        ...       ...        ...        ...         ...        ...      ...       ...           ...                   ...                     ...
1617  HK.63402     10000    WARRANT     GS#TENCTRC2108Y  2020-11-26       True     BULL  HK.00700         False                   NaN                     NaN

[1618 rows x 11 columns]
HK.24719
['HK.24719', 'HK.27886', 'HK.28621', 'HK.14339', 'HK.27952', 'HK.18693', 'HK.20306', 'HK.53635', 'HK.47269', 'HK.27227', 
...        ...       ...        ...        ...         ...        ...      ...       ... 
'HK.63402']
******************************************
        code  lot_size stock_type         stock_name list_time  wrt_valid  wrt_type  wrt_code  future_valid  future_main_contract future_last_trade_time
0  HK.A50main      5000     FUTURE      A50 Future Main(DEC0)                False       NaN       NaN          True                  True                        
..         ...       ...        ...                ...       ...        ...       ...       ...           ...                   ...                    ...
5  HK.A502106      5000     FUTURE      A50 JUN1                False       NaN       NaN          True                 False             2021-06-29

[6 rows x 11 columns]
HK.A50main
['HK.A50main', 'HK.A502011', 'HK.A502012', 'HK.A502101', 'HK.A502103', 'HK.A502106']
```









## <a href="#6602" class="header-anchor">#</a> Qot_GetReference.proto

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Protocol ID**

  3206

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Proto ID**

  3206





`uint GetReference(QotGetReference.Request req);`  
`virtual void OnReply_GetReference(FTAPI_Conn client, uint nSerialNo, QotGetReference.Response rsp);`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        QotGetReference.C2S c2s = QotGetReference.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetReferenceType(QotGetReference.ReferenceType.ReferenceType_Warrant)
            .Build();
        QotGetReference.Request req = QotGetReference.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetReference(req);
        Console.Write("Send QotGetReference: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetReference(FTAPI_Conn client, uint nSerialNo, QotGetReference.Response rsp)
    {
        Console.Write("Reply: QotGetReference: {0}\n", nSerialNo);
        Console.Write("name: {0}, secType: {1} \n", rsp.S2C.StaticInfoListList[0].Basic.Name,
            rsp.S2C.StaticInfoListList[0].Basic.SecType);
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
Qot onInitConnect: ret=0 desc= connID=6825716009073059706
Send QotGetReference: 3
Reply: QotGetReference: 3
name: TENGXUNDONGYAJIUSIGUA, secType: 5
```









`int getReference(QotGetReference.Request req);`  
`void onReply_GetReference(FTAPI_Conn client, int nSerialNo, QotGetReference.Response rsp);`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        QotGetReference.C2S c2s = QotGetReference.C2S.newBuilder()
                .setSecurity(sec)
                .setReferenceType(QotGetReference.ReferenceType.ReferenceType_Warrant_VALUE)
            .build();
        QotGetReference.Request req = QotGetReference.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getReference(req);
        System.out.printf("Send QotGetReference: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetReference(FTAPI_Conn client, int nSerialNo, QotGetReference.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetReference failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetReference: %s\n", json);
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
Send QotGetReference: 2
Receive QotGetReference: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "24719"
        },
        "id": "76128295346319",
        "lotSize": 1000,
        "secType": 5,
        "name": "TENGXUNDONGYAJIUSIGUA",
        "listTime": "2018-07-20",
        "delisting": false,
        "listTimestamp": 1.532016E9
      },
      "warrantExData": {
        "type": 2,
        "owner": {
          "market": 1,
          "code": "00700"
        }
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "55592"
        },
        "id": "80753975154984",
        "lotSize": 5000,
        "secType": 5,
        "name": "SG#TENCTRC2202S",
        "listTime": "2021-06-29",
        "delisting": false,
        "listTimestamp": 1.624896E9
      },
      "warrantExData": {
        "type": 3,
        "owner": {
          "market": 1,
          "code": "00700"
        }
      }
    }]
  }
}
```









`Futu::u32_t GetReference(const Qot_GetReference::Request &stReq);`  
`virtual void OnReply_GetReference(Futu::u32_t nSerialNo, const Qot_GetReference::Response &stRsp) = 0;`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        Qot_GetReference::Request req;
        Qot_GetReference::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_referencetype(1);

        m_GetReferenceSerialNo = m_pQotApi->GetReference(req);
        cout << "Request GetReference SerialNo: " << m_GetReferenceSerialNo << endl;
    }

    virtual void OnReply_GetReference(Futu::u32_t nSerialNo, const Qot_GetReference::Response &stRsp){
        if(nSerialNo == m_GetReferenceSerialNo)
        {
            cout << "OnReply_GetReference SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

  Futu::u32_t m_GetReferenceSerialNo;
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
Request GetReference SerialNo: 4
OnReply_GetReference SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "staticInfoList": [
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "24719"
     },
     "id": "76128295346319",
     "lotSize": 1000,
     "secType": 5,
     "name": "TENGXUNDONGYAJIUSIGUA",
     "listTime": "2018-07-20",
     "delisting": false,
     "listTimestamp": 1532016000
    },
    "warrantExData": {
     "type": 2,
     "owner": {
      "market": 1,
      "code": "00700"
     }
    }
   },
...
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "69950"
     },
     "id": "80685255692606",
     "lotSize": 5000,
     "secType": 5,
     "name": "MS#TENCTRP2202B",
     "listTime": "2021-06-11",
     "delisting": false,
     "listTimestamp": 1623340800
    },
    "warrantExData": {
     "type": 4,
     "owner": {
      "market": 1,
      "code": "00700"
     }
    }
   }
  ]
 }
}
```









`GetReference(req);`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Qot_GetReference } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetReference(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    const { ReferenceType } = Qot_GetReference
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    referenceType: ReferenceType.ReferenceType_Warrant,
                },
            };

            websocket.GetReference(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("Reference: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Reference: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "24719"
      },
      "id": "76128295346319",
      "lotSize": 1000,
      "secType": 5,
      "name": "TENGXUNDONGYAJIUSIGUA",
      "listTime": "2018-07-20",
      "delisting": false,
      "listTimestamp": 1532016000
    },
    "warrantExData": {
      "type": 2,
      "owner": {
        "market": 1,
        "code": "00700"
      }
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "27227"
      },
      "id": "77919296711259",
      "lotSize": 10000,
      "secType": 5,
      "name": "MBTENCT@EC2109A",
      "listTime": "2019-09-10",
      "delisting": false,
      "listTimestamp": 1568044800
    },
    "warrantExData": {
      "type": 1,
      "owner": {
        "market": 1,
        "code": "00700"
      }
    }
  }, ..., {
    "basic": {
      "security": {
        "market": 1,
        "code": "57696"
      },
      "id": "81101867508064",
      "lotSize": 5000,
      "secType": 5,
      "name": "UB#TENCTRP2203P",
      "listTime": "2021-09-16",
      "delisting": false,
      "listTimestamp": 1631721600
    },
    "warrantExData": {
      "type": 4,
      "owner": {
        "market": 1,
        "code": "00700"
      }
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- When obtaining warrants related to the underlying stock, it is not
  subject to the above frequency restriction











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_referencestock_list(code, reference_type)`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contracts related to futures

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | code | str | Stock code. |
  | reference_type | [SecurityReferenceType](/moomoo-api-doc/en/quote/quote.html#8136) | Related data type to be obtained. |

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
  <td>If ret == RET_OK, related data of security is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Related data of security fotmat as follows:
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
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of shares per lot, contract
    multiplier for futures.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Security type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">list_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time of listing.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether it is a warrant.
    
      
    
    
     
    
    If it is True, the following field start with 'wrt' is valid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
    <td style="text-align: left;">Warrant type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">wrt_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The underlying stock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">future_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether it is a future.
    
      
    
    
     
    
    If it is True, the following field start with 'future' is valid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">future_main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the future main contract.
    
      
    
    
     
    
    Special field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">future_last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.
    
      
    
    
     
    
    The field is unique to futures.<br />
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

# Get warrants related to the underlying stock
ret, data = quote_ctx.get_referencestock_list('HK.00700', SecurityReferenceType.WARRANT)
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
print('******************************************')
# Port related contracts
ret, data = quote_ctx.get_referencestock_list('HK.A50main', SecurityReferenceType.FUTURE)
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
        code  lot_size stock_type stock_name   list_time  wrt_valid wrt_type  wrt_code  future_valid  future_main_contract  future_last_trade_time
0     HK.24719      1000    WARRANT     TENGXUNDONGYAJIUSIGUA  2018-07-20       True      PUT  HK.00700         False                   NaN                     NaN
...        ...       ...        ...        ...         ...        ...      ...       ...           ...                   ...                     ...
1617  HK.63402     10000    WARRANT     GS#TENCTRC2108Y  2020-11-26       True     BULL  HK.00700         False                   NaN                     NaN

[1618 rows x 11 columns]
HK.24719
['HK.24719', 'HK.27886', 'HK.28621', 'HK.14339', 'HK.27952', 'HK.18693', 'HK.20306', 'HK.53635', 'HK.47269', 'HK.27227', 
...        ...       ...        ...        ...         ...        ...      ...       ... 
'HK.63402']
******************************************
        code  lot_size stock_type         stock_name list_time  wrt_valid  wrt_type  wrt_code  future_valid  future_main_contract future_last_trade_time
0  HK.A50main      5000     FUTURE      A50 Future Main(DEC0)                False       NaN       NaN          True                  True                        
..         ...       ...        ...                ...       ...        ...       ...       ...           ...                   ...                    ...
5  HK.A502106      5000     FUTURE      A50 JUN1                False       NaN       NaN          True                 False             2021-06-29

[6 rows x 11 columns]
HK.A50main
['HK.A50main', 'HK.A502011', 'HK.A502012', 'HK.A502101', 'HK.A502103', 'HK.A502106']
```









## <a href="#6602-2" class="header-anchor">#</a> Qot_GetReference.proto

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Protocol ID**

  3206

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Proto ID**

  3206





`uint GetReference(QotGetReference.Request req);`  
`virtual void OnReply_GetReference(MMAPI_Conn client, uint nSerialNo, QotGetReference.Response rsp);`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        QotGetReference.C2S c2s = QotGetReference.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetReferenceType(QotGetReference.ReferenceType.ReferenceType_Warrant)
            .Build();
        QotGetReference.Request req = QotGetReference.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetReference(req);
        Console.Write("Send QotGetReference: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetReference(MMAPI_Conn client, uint nSerialNo, QotGetReference.Response rsp)
    {
        Console.Write("Reply: QotGetReference: {0}\n", nSerialNo);
        Console.Write("name: {0}, secType: {1} \n", rsp.S2C.StaticInfoListList[0].Basic.Name,
            rsp.S2C.StaticInfoListList[0].Basic.SecType);
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
Qot onInitConnect: ret=0 desc= connID=6825716009073059706
Send QotGetReference: 3
Reply: QotGetReference: 3
name: TENGXUNDONGYAJIUSIGUA, secType: 5
```









`int getReference(QotGetReference.Request req);`  
`void onReply_GetReference(MMAPI_Conn client, int nSerialNo, QotGetReference.Response rsp);`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        QotGetReference.C2S c2s = QotGetReference.C2S.newBuilder()
                .setSecurity(sec)
                .setReferenceType(QotGetReference.ReferenceType.ReferenceType_Warrant_VALUE)
            .build();
        QotGetReference.Request req = QotGetReference.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getReference(req);
        System.out.printf("Send QotGetReference: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetReference(MMAPI_Conn client, int nSerialNo, QotGetReference.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetReference failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetReference: %s\n", json);
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
Send QotGetReference: 2
Receive QotGetReference: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "24719"
        },
        "id": "76128295346319",
        "lotSize": 1000,
        "secType": 5,
        "name": "TENGXUNDONGYAJIUSIGUA",
        "listTime": "2018-07-20",
        "delisting": false,
        "listTimestamp": 1.532016E9
      },
      "warrantExData": {
        "type": 2,
        "owner": {
          "market": 1,
          "code": "00700"
        }
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "55592"
        },
        "id": "80753975154984",
        "lotSize": 5000,
        "secType": 5,
        "name": "SG#TENCTRC2202S",
        "listTime": "2021-06-29",
        "delisting": false,
        "listTimestamp": 1.624896E9
      },
      "warrantExData": {
        "type": 3,
        "owner": {
          "market": 1,
          "code": "00700"
        }
      }
    }]
  }
}
```









`moomoo::u32_t GetReference(const Qot_GetReference::Request &stReq);`  
`virtual void OnReply_GetReference(moomoo::u32_t nSerialNo, const Qot_GetReference::Response &stRsp) = 0;`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
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
        Qot_GetReference::Request req;
        Qot_GetReference::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_referencetype(1);

        m_GetReferenceSerialNo = m_pQotApi->GetReference(req);
        cout << "Request GetReference SerialNo: " << m_GetReferenceSerialNo << endl;
    }

    virtual void OnReply_GetReference(moomoo::u32_t nSerialNo, const Qot_GetReference::Response &stRsp){
        if(nSerialNo == m_GetReferenceSerialNo)
        {
            cout << "OnReply_GetReference SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

  moomoo::u32_t m_GetReferenceSerialNo;
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
Request GetReference SerialNo: 4
OnReply_GetReference SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "staticInfoList": [
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "24719"
     },
     "id": "76128295346319",
     "lotSize": 1000,
     "secType": 5,
     "name": "TENGXUNDONGYAJIUSIGUA",
     "listTime": "2018-07-20",
     "delisting": false,
     "listTimestamp": 1532016000
    },
    "warrantExData": {
     "type": 2,
     "owner": {
      "market": 1,
      "code": "00700"
     }
    }
   },
...
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "69950"
     },
     "id": "80685255692606",
     "lotSize": 5000,
     "secType": 5,
     "name": "MS#TENCTRP2202B",
     "listTime": "2021-06-11",
     "delisting": false,
     "listTimestamp": 1623340800
    },
    "warrantExData": {
     "type": 4,
     "owner": {
      "market": 1,
      "code": "00700"
     }
    }
   }
  ]
 }
}
```









`GetReference(req);`

- **Description**

  Get related data of securities, such as: obtaining warrants related to
  underlying stocks, obtaining contradts related to futures

- **Parameters**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 referenceType = 2; // ReferenceType, related type
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 2; //Related stock list
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Qot_GetReference } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetReference(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    const { ReferenceType } = Qot_GetReference
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    referenceType: ReferenceType.ReferenceType_Warrant,
                },
            };

            websocket.GetReference(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("Reference: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
Reference: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "24719"
      },
      "id": "76128295346319",
      "lotSize": 1000,
      "secType": 5,
      "name": "TENGXUNDONGYAJIUSIGUA",
      "listTime": "2018-07-20",
      "delisting": false,
      "listTimestamp": 1532016000
    },
    "warrantExData": {
      "type": 2,
      "owner": {
        "market": 1,
        "code": "00700"
      }
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "27227"
      },
      "id": "77919296711259",
      "lotSize": 10000,
      "secType": 5,
      "name": "MBTENCT@EC2109A",
      "listTime": "2019-09-10",
      "delisting": false,
      "listTimestamp": 1568044800
    },
    "warrantExData": {
      "type": 1,
      "owner": {
        "market": 1,
        "code": "00700"
      }
    }
  }, ..., {
    "basic": {
      "security": {
        "market": 1,
        "code": "57696"
      },
      "id": "81101867508064",
      "lotSize": 5000,
      "secType": 5,
      "name": "UB#TENCTRP2203P",
      "listTime": "2021-09-16",
      "delisting": false,
      "listTimestamp": 1631721600
    },
    "warrantExData": {
      "type": 4,
      "owner": {
        "market": 1,
        "code": "00700"
      }
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- When obtaining warrants related to the underlying stock, it is not
  subject to the above frequency restriction













