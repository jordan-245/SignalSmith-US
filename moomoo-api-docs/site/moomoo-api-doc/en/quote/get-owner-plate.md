



# <a href="#9528" class="header-anchor">#</a> Get Plates of Stocks









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_owner_plate(code_list)`

- **Description**

  Get the information of plates to which the stocks belong

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
  <td style="text-align: left;">Stock code list.
  
    
  
  
   
  
  Only supports underlying stocks and indexes.<br />
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
  <td>If ret == RET_OK, data of the sector is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data of the sector format as follows:
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
    <td style="text-align: left;">Securities code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Plate code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Plate name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#978">Plate</a></td>
    <td style="text-align: left;">Plate type.
    
      
    
    
     
    
    industry or conceptual.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

code_list = ['HK.00001']
ret, data = quote_ctx.get_owner_plate(code_list)
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['plate_code'].values.tolist()) # Convert plate code to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code          name          plate_code                            plate_name plate_type
0   HK.00001  CKH HOLDINGS  HK.HSI Constituent  ConstituentStocks in Hang Seng Index      OTHER
..       ...           ...                 ...                                   ...        ...
8   HK.00001  CKH HOLDINGS           HK.BK1983                                HK ADR      OTHER

[9 rows x 5 columns]
HK.00001
['HK.HSI Constituent', 'HK.GangGuTong', 'HK.BK1000', 'HK.BK1061', 'HK.BK1107', 'HK.BK1331', 'HK.BK1600', 'HK.BK1922', 'HK.BK1983']
```









## <a href="#1138" class="header-anchor">#</a> Qot_GetOwnerPlate.proto

- **Description**

  Get information about the sector of the stock

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message SecurityOwnerPlate
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated Qot_Common.PlateInfo plateInfoList = 2; //Plate to which it belongs
}

message S2C
{
    repeated SecurityOwnerPlate ownerPlateList = 1; //Plate information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the structure of plate information refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3207





`uint GetOwnerPlate(QotGetOwnerPlate.Request req);`  
`virtual void OnReply_GetOwnerPlate(FTAPI_Conn client, uint nSerialNo, QotGetOwnerPlate.Response rsp);`

- **Description**

  Get the information of plates to which the stocks belong

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message SecurityOwnerPlate
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated Qot_Common.PlateInfo plateInfoList = 2; //Plate to which it belongs
}

message S2C
{
    repeated SecurityOwnerPlate ownerPlateList = 1; //Plate information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the structure of plate information refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
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
        QotGetOwnerPlate.C2S c2s = QotGetOwnerPlate.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetOwnerPlate.Request req = QotGetOwnerPlate.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetOwnerPlate(req);
        Console.Write("Send QotGetOwnerPlate: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetOwnerPlate(FTAPI_Conn client, uint nSerialNo, QotGetOwnerPlate.Response rsp)
    {
        Console.Write("Reply: QotGetOwnerPlate: {0}\n", nSerialNo);
        Console.Write("Code: {0}, name: {1},  plateType: {2} \n",
            rsp.S2C.OwnerPlateListList[0].PlateInfoListList[0].Plate.Code,
            rsp.S2C.OwnerPlateListList[0].PlateInfoListList[0].Name,
            rsp.S2C.OwnerPlateListList[0].PlateInfoListList[0].PlateType);
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
Qot onInitConnect: ret=0 desc= connID=6825684997241406142
Send QotGetOwnerPlate: 3
Reply: QotGetOwnerPlate: 3
Code: HSI Constituent, name: ConstituentStocks in Hang Seng Index,  plateType: 4
```









`int getOwnerPlate(QotGetOwnerPlate.Request req);`  
`void onReply_GetOwnerPlate(FTAPI_Conn client, int nSerialNo, QotGetOwnerPlate.Response rsp);`

- **Description**

  Get the information of plates to which the stocks belong

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message SecurityOwnerPlate
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated Qot_Common.PlateInfo plateInfoList = 2; //Plate to which it belongs
}

message S2C
{
    repeated SecurityOwnerPlate ownerPlateList = 1; //Plate information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the structure of plate information refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
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
        QotGetOwnerPlate.C2S c2s = QotGetOwnerPlate.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetOwnerPlate.Request req = QotGetOwnerPlate.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getOwnerPlate(req);
        System.out.printf("Send QotGetOwnerPlate: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOwnerPlate(FTAPI_Conn client, int nSerialNo, QotGetOwnerPlate.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetOwnerPlate failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetOwnerPlate: %s\n", json);
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
Send QotGetOwnerPlate: 2
Receive QotGetOwnerPlate: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "ownerPlateList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "plateInfoList": [{
        "plate": {
          "market": 1,
          "code": "HSI Constituent"
        },
        "name": "ConstituentStocks in Hang Seng Index",
        "plateType": 4
      }, ... {
        "plate": {
          "market": 1,
          "code": "BK1995"
        },
        "name": "Blockchain",
        "plateType": 3
      }]
    }]
  }
}
```









`Futu::u32_t GetOwnerPlate(const Qot_GetOwnerPlate::Request &stReq);`  
`virtual void OnReply_GetOwnerPlate(Futu::u32_t nSerialNo, const Qot_GetOwnerPlate::Response &stRsp) = 0;`

- **Description**

  Get the information of plates to which the stocks belong

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message SecurityOwnerPlate
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated Qot_Common.PlateInfo plateInfoList = 2; //Plate to which it belongs
}

message S2C
{
    repeated SecurityOwnerPlate ownerPlateList = 1; //Plate information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the structure of plate information refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
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
        Qot_GetOwnerPlate::Request req;
        Qot_GetOwnerPlate::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetOwnerPlateSerialNo = m_pQotApi->GetOwnerPlate(req);
        cout << "Request GetOwnerPlate SerialNo: " << m_GetOwnerPlateSerialNo << endl;
    }

    virtual void OnReply_GetOwnerPlate(Futu::u32_t nSerialNo, const Qot_GetOwnerPlate::Response &stRsp){
        if(nSerialNo == m_GetOwnerPlateSerialNo)
        {
            cout << "OnReply_GetOwnerPlate SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetOwnerPlateSerialNo;
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
Request GetOwnerPlate SerialNo: 4
OnReply_GetOwnerPlate SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "ownerPlateList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "plateInfoList": [
     {
      "plate": {
       "market": 1,
       "code": "HSI Constituent"
      },
      "name": "ConstituentStocks in Hang Seng Index",
      "plateType": 4
     },
...
     {
      "plate": {
       "market": 1,
       "code": "BK1995"
      },
      "name": "Blockchain",
      "plateType": 3
     }
    ]
   }
  ]
 }
}
```









`GetOwnerPlate(req);`

- **Description**

  Get the information of plates to which the stocks belong

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message SecurityOwnerPlate
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated Qot_Common.PlateInfo plateInfoList = 2; //Plate to which it belongs
}

message S2C
{
    repeated SecurityOwnerPlate ownerPlateList = 1; //Plate information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For the structure of plate information refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetOwnerPlate(){
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
            websocket.GetOwnerPlate(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("OwnerPlate: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
OwnerPlate: errCode 0, retMsg , retType 0
{
  "ownerPlateList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "plateInfoList": [{
      "plate": {
        "market": 1,
        "code": "HSI Constituent"
      },
      "name": "ConstituentStocks in Hang Seng Index",
      "plateType": 4
    }, {
      "plate": {
        "market": 1,
        "code": "HSCEI Stock"
      },
      "name": "ConstituentStocks in HS China Enterprises Index",
      "plateType": 4
    }, ..., {
      "plate": {
        "market": 1,
        "code": "BK1995"
      },
      "name": "Blockchain",
      "plateType": 3
    }]
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds
- The maximum number of stocks of each request list is 200
- Only supports stocks and indices







`get_owner_plate(code_list)`

- **Description**

  Get the information of plates to which the stocks belong

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
  <td style="text-align: left;">Stock code list.
  
    
  
  
   
  
  Only supports underlying stocks and indexes.<br />
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
  <td>If ret == RET_OK, data of the sector is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data of the sector format as follows:
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
    <td style="text-align: left;">Securities code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Plate code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Plate name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">plate_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#978">Plate</a></td>
    <td style="text-align: left;">Plate type.
    
      
    
    
     
    
    industry or conceptual.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

code_list = ['HK.00001']
ret, data = quote_ctx.get_owner_plate(code_list)
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['plate_code'].values.tolist()) # Convert plate code to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code          name          plate_code                            plate_name plate_type
0   HK.00001  CKH HOLDINGS  HK.HSI Constituent  ConstituentStocks in Hang Seng Index      OTHER
..       ...           ...                 ...                                   ...        ...
8   HK.00001  CKH HOLDINGS           HK.BK1983                                HK ADR      OTHER

[9 rows x 5 columns]
HK.00001
['HK.HSI Constituent', 'HK.GangGuTong', 'HK.BK1000', 'HK.BK1061', 'HK.BK1107', 'HK.BK1331', 'HK.BK1600', 'HK.BK1922', 'HK.BK1983']
```















