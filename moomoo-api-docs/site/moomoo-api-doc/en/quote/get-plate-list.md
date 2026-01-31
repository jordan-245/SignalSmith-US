



# <a href="#6513" class="header-anchor">#</a> Get Plate List









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_plate_list(market, plate_class)`

- **Description**

  Obtain a list of stock sectors

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
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Market identification.
  
    
  
  
   
  
  Note: Shanghai and Shenzhen are not distinguished here. Entering
  Shanghai or Shenzhen will return to the sub-plates of the Shanghai and
  Shenzhen markets.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">plate_class</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#978">Plate</a></td>
  <td style="text-align: left;">Plate classification.</td>
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
  <td>If ret == RET_OK, data of the plate list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data of the plate list format as follows:
    | Field      | Type | Description |
    |:-----------|:-----|:------------|
    | code       | str  | Plate code. |
    | plate_name | str  | Plate name. |
    | plate_id   | str  | Plate ID.   |

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_plate_list(Market.HK, Plate.CONCEPT)
if ret == RET_OK:
    print(data)
    print(data['plate_name'][0]) # Take the first plate name
    print(data['plate_name'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code plate_name plate_id
0   HK.BK1000      Short Collection   BK1000
..        ...        ...      ...
77  HK.BK1999      Funeral Concept    BK1999

[78 rows x 3 columns]
Short Collection
['Short Collection','Ali concept stocks','Xiongan concept stocks','Apple concept','One Belt One Road', '5G concept','Nightclub stocks','Guangdong-Hong Kong-Macao Greater Bay Area','Tes Pull concept stocks','beer','suspected financial technology stocks','sports goods','rare earth concept','renminbi appreciation concept','anti-epidemic concept','new stocks and sub-new stocks','Tencent concept', 'Cloud Office','SaaS Concept','Online Education','Auto Dealer','Norwegian Government Global Pension Fund Holding','Wuhan Local Concept Stock','Nuclear Power','Mainland Pharmaceutical Stock','Makeup and Beauty Stocks','Technology Internet Stocks','Utilities Stocks','Oil Stocks','Telecom Equipment','Power Stocks','Mobile Games Stocks','Baby and Children’s Products Stocks','Department Stocks', ' Rent collection stocks','port transportation stocks','telecommunications stocks','environmental protection','coal stocks','automotive stocks','battery stocks','logistics','mainland property management stocks','agricultural stocks', 'Golden stocks','luxury stocks','power equipment stocks','fast food chain stores','heavy machinery stocks','food stocks','insurance stocks','paper stocks','water affairs stocks' ,'Dairy products stocks','PV solar stocks','Chinese real estate stocks','Mainland education stocks','Home appliances stocks','Wind power stocks','Blue chip real estate stocks','Chinese banking stocks','Aviation stocks' ,'Petrochemical stocks','Building materials and cement stocks','Chinese brokerage stocks','High-speed rail infrastructure stocks','Gas stocks','Highway and railway stocks','Steel and metal stocks','Huawei concept','OLED Concept','Industrial hemp','Hong Kong local stocks','Hong Kong retail stocks','blockchain','pork concept','holiday concept','Funeral Concept']
```









## <a href="#5574" class="header-anchor">#</a> Qot_GetPlateSet.proto

- **Description**

  Obtain a list of stock sectors

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common.QotMarket, market identification
    required int32 plateSetType = 2; //Qot_Common.PlateSetType, the type of plate set
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For enumeration of plate set types, refer to
>   [PlateSetType](/moomoo-api-doc/en/quote/quote.html#978)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.PlateInfo plateInfoList = 1; //Plate information of the plate set
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of plate information, refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3204





`uint GetPlateSet(QotGetPlateSet.Request req);`  
`virtual void OnReply_GetPlateSet(FTAPI_Conn client, uint nSerialNo, QotGetPlateSet.Response rsp);`

- **Description**

  Obtain a list of stock sectors

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common.QotMarket, market identification
    required int32 plateSetType = 2; //Qot_Common.PlateSetType, the type of plate set
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For enumeration of plate set types, refer to
>   [PlateSetType](/moomoo-api-doc/en/quote/quote.html#978)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.PlateInfo plateInfoList = 1; //Plate information of the plate set
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of plate information, refer to
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

        QotGetPlateSet.C2S c2s = QotGetPlateSet.C2S.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetPlateSetType((int)QotCommon.PlateSetType.PlateSetType_Industry)
            .Build();
        QotGetPlateSet.Request req = QotGetPlateSet.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetPlateSet(req);
        Console.Write("Send QotGetPlateSet: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetPlateSet(FTAPI_Conn client, uint nSerialNo, QotGetPlateSet.Response rsp)
    {
        Console.Write("Reply: QotGetPlateSet: {0}\n", nSerialNo);
        Console.Write("code: {0},  name: {1} \n", rsp.S2C.PlateInfoListList[0].Plate.Code,
            rsp.S2C.PlateInfoListList[0].Name);
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
Qot onInitConnect: ret=0 desc= connID=6825726015499136889
Send QotGetPlateSet: 3
Reply: QotGetPlateSet: 3
code: BK1001,  name: Dairy Products
```









`int getPlateSet(QotGetPlateSet.Request req);`  
`void onReply_GetPlateSet(FTAPI_Conn client, int nSerialNo, QotGetPlateSet.Response rsp);`

- **Description**

  Obtain a list of stock sectors

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common.QotMarket, market identification
    required int32 plateSetType = 2; //Qot_Common.PlateSetType, the type of plate set
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For enumeration of plate set types, refer to
>   [PlateSetType](/moomoo-api-doc/en/quote/quote.html#978)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.PlateInfo plateInfoList = 1; //Plate information of the plate set
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of plate information, refer to
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

        QotGetPlateSet.C2S c2s = QotGetPlateSet.C2S.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setPlateSetType(QotCommon.PlateSetType.PlateSetType_Industry_VALUE)
            .build();
        QotGetPlateSet.Request req = QotGetPlateSet.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getPlateSet(req);
        System.out.printf("Send QotGetPlateSet: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPlateSet(FTAPI_Conn client, int nSerialNo, QotGetPlateSet.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetPlateSet failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetPlateSet: %s\n", json);
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
Send QotGetPlateSet: 2
Receive QotGetPlateSet: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "plateInfoList": [{
      "plate": {
        "market": 1,
        "code": "BK1001"
      },
      "name": "Dairy Products"
    }, ... {
      "plate": {
        "market": 1,
        "code": "BK1284"
      },
      "name": "traditional Chinese medicine"
    }]
  }
}
```









`Futu::u32_t GetPlateSet(const Qot_GetPlateSet::Request &stReq);`  
`virtual void OnReply_GetPlateSet(Futu::u32_t nSerialNo, const Qot_GetPlateSet::Response &stRsp) = 0;`

- **Description**

  Obtain a list of stock sectors

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common.QotMarket, market identification
    required int32 plateSetType = 2; //Qot_Common.PlateSetType, the type of plate set
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For enumeration of plate set types, refer to
>   [PlateSetType](/moomoo-api-doc/en/quote/quote.html#978)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.PlateInfo plateInfoList = 1; //Plate information of the plate set
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of plate information, refer to
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
        Qot_GetPlateSet::Request req;
        Qot_GetPlateSet::C2S *c2s = req.mutable_c2s();
        c2s->set_market(1);
        c2s->set_platesettype(0);

        m_GetPlateSetSerialNo = m_pQotApi->GetPlateSet(req);
        cout << "Request GetPlateSet SerialNo: " << m_GetPlateSetSerialNo << endl;
    }

    virtual void OnReply_GetPlateSet(Futu::u32_t nSerialNo, const Qot_GetPlateSet::Response &stRsp){
        if(nSerialNo == m_GetPlateSetSerialNo)
        {
            cout << "OnReply_GetPlateSet SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetPlateSetSerialNo;
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
Request GetPlateSet SerialNo: 4
OnReply_GetPlateSet SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "plateInfoList": [
   {
    "plate": {
     "market": 1,
     "code": "BK1000"
    },
    "name": "Most Shorted Stocks"
   },
...
   {
    "plate": {
     "market": 1,
     "code": "BK1999"
    },
    "name": "Funeral Concept"
   }
  ]
 }
}
```









`GetPlateSet(req);`

- **Description**

  Obtain a list of stock sectors

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common.QotMarket, market identification
    required int32 plateSetType = 2; //Qot_Common.PlateSetType, the type of plate set
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For enumeration of plate set types, refer to
>   [PlateSetType](/moomoo-api-doc/en/quote/quote.html#978)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.PlateInfo plateInfoList = 1; //Plate information of the plate set
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the structure of plate information, refer to
>   [PlateInfo](/moomoo-api-doc/en/quote/quote.html#3203)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetPlateSet(){
    const { RetType } = Common
    const { QotMarket, PlateSetType } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    market: QotMarket.QotMarket_HK_Security,
                    plateSetType: PlateSetType.PlateSetType_All,
                },
            };

            websocket.GetPlateSet(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("PlateSet: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
PlateSet: errCode 0, retMsg , retType 0
{
  "plateInfoList": [{
    "plate": {
      "market": 1,
      "code": "BK1000"
    },
    "name": "Most Shorted Stocks"
  }, {
    "plate": {
      "market": 1,
      "code": "BK1001"
    },
    "name": "Dairy Products"
  }, ..., {
    "plate": {
      "market": 1,
      "code": "BK1999"
    },
    "name": "Funeral Concept"
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds







`get_plate_list(market, plate_class)`

- **Description**

  Obtain a list of stock sectors

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
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Market identification.
  
    
  
  
   
  
  Note: Shanghai and Shenzhen are not distinguished here. Entering
  Shanghai or Shenzhen will return to the sub-plates of the Shanghai and
  Shenzhen markets.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">plate_class</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#978">Plate</a></td>
  <td style="text-align: left;">Plate classification.</td>
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
  <td>If ret == RET_OK, data of the plate list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data of the plate list format as follows:
    | Field      | Type | Description |
    |:-----------|:-----|:------------|
    | code       | str  | Plate code. |
    | plate_name | str  | Plate name. |
    | plate_id   | str  | Plate ID.   |

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_plate_list(Market.HK, Plate.CONCEPT)
if ret == RET_OK:
    print(data)
    print(data['plate_name'][0]) # Take the first plate name
    print(data['plate_name'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code plate_name plate_id
0   HK.BK1000      Short Collection   BK1000
..        ...        ...      ...
77  HK.BK1999      Funeral Concept    BK1999

[78 rows x 3 columns]
Short Collection
['Short Collection','Ali concept stocks','Xiongan concept stocks','Apple concept','One Belt One Road', '5G concept','Nightclub stocks','Guangdong-Hong Kong-Macao Greater Bay Area','Tes Pull concept stocks','beer','suspected financial technology stocks','sports goods','rare earth concept','renminbi appreciation concept','anti-epidemic concept','new stocks and sub-new stocks','Tencent concept', 'Cloud Office','SaaS Concept','Online Education','Auto Dealer','Norwegian Government Global Pension Fund Holding','Wuhan Local Concept Stock','Nuclear Power','Mainland Pharmaceutical Stock','Makeup and Beauty Stocks','Technology Internet Stocks','Utilities Stocks','Oil Stocks','Telecom Equipment','Power Stocks','Mobile Games Stocks','Baby and Children’s Products Stocks','Department Stocks', ' Rent collection stocks','port transportation stocks','telecommunications stocks','environmental protection','coal stocks','automotive stocks','battery stocks','logistics','mainland property management stocks','agricultural stocks', 'Golden stocks','luxury stocks','power equipment stocks','fast food chain stores','heavy machinery stocks','food stocks','insurance stocks','paper stocks','water affairs stocks' ,'Dairy products stocks','PV solar stocks','Chinese real estate stocks','Mainland education stocks','Home appliances stocks','Wind power stocks','Blue chip real estate stocks','Chinese banking stocks','Aviation stocks' ,'Petrochemical stocks','Building materials and cement stocks','Chinese brokerage stocks','High-speed rail infrastructure stocks','Gas stocks','Highway and railway stocks','Steel and metal stocks','Huawei concept','OLED Concept','Industrial hemp','Hong Kong local stocks','Hong Kong retail stocks','blockchain','pork concept','holiday concept','Funeral Concept']
```















