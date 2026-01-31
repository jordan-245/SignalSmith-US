



# <a href="#4931" class="header-anchor">#</a> Get the List of Stocks in The Plate









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_plate_stock(plate_code, sort_field=SortField.CODE, ascend=True)`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

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
  <td style="text-align: left;">plate_code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Plate code.
  
    
  
  
   
  
  You can use <a href="/moomoo-api-doc/en/quote/get-plate-list.html">Get
  plate list</a> to get other plates code.<br />
  For example, "SH.BK0001", "SH.BK0002".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">sort_field</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#5823">SortField</a></td>
  <td style="text-align: left;">Sort field.</td>
  </tr>
  <tr>
  <td style="text-align: left;">ascend</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Sort direction.
  
    
  
  
   
  
  True: ascending order.<br />
  False: descending order.
  
  
  
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
  <td>If ret == RET_OK, stock data of the plate is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock data of the plate format as follows:
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
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of shares per lot, or contract
    multiplier for futures.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Stock type.</td>
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
    <td style="text-align: left;">stock_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Stock ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether future main contract.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.
    
      
    
    
     
    
    The field is unique to futures. Main, current month and next month
    futures do not have this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_plate_stock('HK.BK1001')
if ret == RET_OK:
    print(data)
    print(data['stock_name'][0]) # Take the first stock name
    print(data['stock_name'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code  lot_size stock_name  stock_owner  stock_child_type stock_type   list_time        stock_id  main_contract last_trade_time
0   HK.00462      4000       Natural dairy          NaN               NaN      STOCK  2005-06-10  55589761712590          False                
..       ...       ...        ...          ...               ...        ...         ...             ...            ...             ...
9   HK.06186      1000           China Feihe Limited          NaN               NaN      STOCK  2019-11-13  78159814858794          False                

[10 rows x 10 columns]
Natural Dairy
['Natural Dairy', 'China Modern Dairy', 'Yashili International', 'YuanShengTai Dairy Farm', 'China Shengmu Organic Milk', 'China ZhongDi Dairy Holdings', 'Lanzhou Zhuangyuan Pasture', 'Ausnutria Dairy Corporation', 'China Mengniu Dairy', 'China Feihe Limited']
```









## <a href="#5662" class="header-anchor">#</a> Qot_GetPlateSecurity.proto

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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

- **Protocol ID**

  3205





`uint GetPlateSecurity(QotGetPlateSecurity.Request req);`  
`virtual void OnReply_GetPlateSecurity(FTAPI_Conn client, uint nSerialNo, QotGetPlateSecurity.Response rsp);`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
                .SetCode("BK1001")
                .Build();
        QotGetPlateSecurity.C2S c2s = QotGetPlateSecurity.C2S.CreateBuilder()
                .SetPlate(sec)
            .Build();
        QotGetPlateSecurity.Request req = QotGetPlateSecurity.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetPlateSecurity(req);
        Console.Write("Send QotGetPlateSecurity: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }
    
    public void OnReply_GetPlateSecurity(FTAPI_Conn client, uint nSerialNo, QotGetPlateSecurity.Response rsp)
    {
        Console.Write("Reply: QotGetPlateSecurity: {0}\n", nSerialNo);
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
Qot onInitConnect: ret=0 desc= connID=6825732202242203206
Send QotGetPlateSecurity: 3
Reply: QotGetPlateSecurity: 3
name: Natural Dairy, secType: 3
```









`int getPlateSecurity(QotGetPlateSecurity.Request req);`  
`void onReply_GetPlateSecurity(FTAPI_Conn client, int nSerialNo, QotGetPlateSecurity.Response rsp);`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
                .setCode("BK1001")
                .build();
        QotGetPlateSecurity.C2S c2s = QotGetPlateSecurity.C2S.newBuilder()
                .setPlate(sec)
            .build();
        QotGetPlateSecurity.Request req = QotGetPlateSecurity.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getPlateSecurity(req);
        System.out.printf("Send QotGetPlateSecurity: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPlateSecurity(FTAPI_Conn client, int nSerialNo, QotGetPlateSecurity.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetPlateSecurity failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetPlateSecurity: %s\n", json);
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
Send QotGetPlateSecurity: 2
Receive QotGetPlateSecurity: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "00462"
        },
        "id": "55589761712590",
        "lotSize": 4000,
        "secType": 3,
        "name": "Natural Dairy",
        "listTime": "2005-06-10",
        "delisting": false,
        "listTimestamp": 1.1183328E9
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "09858"
        },
        "id": "80676665697922",
        "lotSize": 1000,
        "secType": 3,
        "name": "China Youran Dairy",
        "listTime": "2021-06-18",
        "delisting": false,
        "listTimestamp": 1.6239456E9
      }
    }]
  }
}
```









`Futu::u32_t GetPlateSecurity(const Qot_GetPlateSecurity::Request &stReq);`  
`virtual void OnReply_GetPlateSecurity(Futu::u32_t nSerialNo, const Qot_GetPlateSecurity::Response &stRsp) = 0;`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
        Qot_GetPlateSecurity::Request req;
        Qot_GetPlateSecurity::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_plate();
        sec->set_code("BK1001");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetPlateSecuritySerialNo = m_pQotApi->GetPlateSecurity(req);
        cout << "Request GetPlateSecurity SerialNo: " << m_GetPlateSecuritySerialNo << endl;
    }

    virtual void OnReply_GetPlateSecurity(Futu::u32_t nSerialNo, const Qot_GetPlateSecurity::Response &stRsp){
        if(nSerialNo == m_GetPlateSecuritySerialNo)
        {
            cout << "OnReply_GetPlateSecurity SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetPlateSecuritySerialNo;
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
Request GetPlateSecurity SerialNo: 4
OnReply_GetPlateSecurity SerialNo: 4
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
      "code": "00462"
     },
     "id": "55589761712590",
     "lotSize": 4000,
     "secType": 3,
     "name": "Natural Dairy",
     "listTime": "2005-06-10",
     "delisting": false,
     "listTimestamp": 1118332800
    }
   },
...
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "06186"
     },
     "id": "78159814858794",
     "lotSize": 1000,
     "secType": 3,
     "name": "China Feihe Limited",
     "listTime": "2019-11-13",
     "delisting": false,
     "listTimestamp": 1573574400
    }
   }
  ]
 }
}
```









`GetPlateSecurity(req);`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetPlateSecurity(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    plate:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "Motherboard",
                    },
                },
            };

            websocket.GetPlateSecurity(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("PlateSecurity: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
PlateSecurity: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "00001"
      },
      "id": "4440996184065",
      "lotSize": 500,
      "secType": 3,
      "name": "CK Hutchison",
      "listTime": "2015-03-18",
      "delisting": false,
      "listTimestamp": 1426608000
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "00002"
      },
      "id": "2",
      "lotSize": 500,
      "secType": 3,
      "name": "CLP Holdings Limited",
      "listTime": "1970-01-01",
      "delisting": false,
      "listTimestamp": 0
    }
  }, ..., {
    "basic": {
      "security": {
        "market": 1,
        "code": "87001"
      },
      "id": "64819646518233",
      "lotSize": 1000,
      "secType": 4,
      "name": "Hui Xian Real Estate Investment Trust",
      "listTime": "2011-04-29",
      "delisting": false,
      "listTimestamp": 1304006400
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds



Commonly used sectors and index codes

| Code                      | Description                                    |
|:--------------------------|:-----------------------------------------------|
| HK.HSI Constituent Stocks | HSI constituent stocks                         |
| HK.HSCEI Stock            | HSCEI constituent stocks                       |
| HK.Motherboard            | Main Plate of Hong Kong Stocks                 |
| HK.GEM                    | GEM(Growth Enterprise Market) Hong Kong Stocks |
| HK.LIST1910               | All Hong Kong stocks                           |
| HK.LIST1911               | Main Plate H shares                            |
| HK.LIST1912               | GEM H shares                                   |
| HK.Fund                   | ETF (Hong Kong Stock Fund)                     |
| HK.LIST1600               | Hot List (Hong Kong)                           |
| HK.LIST1921               | Listed new shares-Hong Kong stocks             |
| SH.LIST3000000            | Shanghai Main Plate                            |
| SH.LIST0901               | Shanghai Stock Exchange B shares               |
| SH.LIST0902               | Shenzhen Stock Exchange B shares               |
| SH.LIST3000002            | Shanghai and Shenzhen Index                    |
| SH.LIST3000005            | All A-shares (Shanghai and Shenzhen)           |
| SH.LIST0600               | Hot List (Shanghai and Shenzhen)               |
| SH.LIST0992               | Science Innovation Plate                       |
| SH.LIST0921               | Listed New Shares - A-shares                   |
| SZ.LIST3000001            | SZSE Main Plate                                |
| SZ.LIST3000003            | Small and Medium Plate                         |
| SZ.LIST3000004            | The Growth Enterprise Market (Deep)            |
| US.USAALL                 | All US stocks                                  |









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_plate_stock(plate_code, sort_field=SortField.CODE, ascend=True)`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

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
  <td style="text-align: left;">plate_code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Plate code.
  
    
  
  
   
  
  You can use <a href="/moomoo-api-doc/en/quote/get-plate-list.html">Get
  plate list</a> to get other plates code.<br />
  For example, "SH.BK0001", "SH.BK0002".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">sort_field</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#5823">SortField</a></td>
  <td style="text-align: left;">Sort field.</td>
  </tr>
  <tr>
  <td style="text-align: left;">ascend</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Sort direction.
  
    
  
  
   
  
  True: ascending order.<br />
  False: descending order.
  
  
  
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
  <td>If ret == RET_OK, stock data of the plate is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock data of the plate format as follows:
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
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of shares per lot, or contract
    multiplier for futures.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Stock name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Stock type.</td>
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
    <td style="text-align: left;">stock_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Stock ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether future main contract.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.
    
      
    
    
     
    
    The field is unique to futures. Main, current month and next month
    futures do not have this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_plate_stock('HK.BK1001')
if ret == RET_OK:
    print(data)
    print(data['stock_name'][0]) # Take the first stock name
    print(data['stock_name'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code  lot_size stock_name  stock_owner  stock_child_type stock_type   list_time        stock_id  main_contract last_trade_time
0   HK.00462      4000       Natural dairy          NaN               NaN      STOCK  2005-06-10  55589761712590          False                
..       ...       ...        ...          ...               ...        ...         ...             ...            ...             ...
9   HK.06186      1000           China Feihe Limited          NaN               NaN      STOCK  2019-11-13  78159814858794          False                

[10 rows x 10 columns]
Natural Dairy
['Natural Dairy', 'China Modern Dairy', 'Yashili International', 'YuanShengTai Dairy Farm', 'China Shengmu Organic Milk', 'China ZhongDi Dairy Holdings', 'Lanzhou Zhuangyuan Pasture', 'Ausnutria Dairy Corporation', 'China Mengniu Dairy', 'China Feihe Limited']
```









## <a href="#5662-2" class="header-anchor">#</a> Qot_GetPlateSecurity.proto

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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

- **Protocol ID**

  3205





`uint GetPlateSecurity(QotGetPlateSecurity.Request req);`  
`virtual void OnReply_GetPlateSecurity(MMAPI_Conn client, uint nSerialNo, QotGetPlateSecurity.Response rsp);`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
                .SetCode("BK1001")
                .Build();
        QotGetPlateSecurity.C2S c2s = QotGetPlateSecurity.C2S.CreateBuilder()
                .SetPlate(sec)
            .Build();
        QotGetPlateSecurity.Request req = QotGetPlateSecurity.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetPlateSecurity(req);
        Console.Write("Send QotGetPlateSecurity: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }
    
    public void OnReply_GetPlateSecurity(MMAPI_Conn client, uint nSerialNo, QotGetPlateSecurity.Response rsp)
    {
        Console.Write("Reply: QotGetPlateSecurity: {0}\n", nSerialNo);
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
Qot onInitConnect: ret=0 desc= connID=6825732202242203206
Send QotGetPlateSecurity: 3
Reply: QotGetPlateSecurity: 3
name: Natural Dairy, secType: 3
```









`int getPlateSecurity(QotGetPlateSecurity.Request req);`  
`void onReply_GetPlateSecurity(MMAPI_Conn client, int nSerialNo, QotGetPlateSecurity.Response rsp);`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
                .setCode("BK1001")
                .build();
        QotGetPlateSecurity.C2S c2s = QotGetPlateSecurity.C2S.newBuilder()
                .setPlate(sec)
            .build();
        QotGetPlateSecurity.Request req = QotGetPlateSecurity.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getPlateSecurity(req);
        System.out.printf("Send QotGetPlateSecurity: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPlateSecurity(MMAPI_Conn client, int nSerialNo, QotGetPlateSecurity.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetPlateSecurity failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetPlateSecurity: %s\n", json);
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
Send QotGetPlateSecurity: 2
Receive QotGetPlateSecurity: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "00462"
        },
        "id": "55589761712590",
        "lotSize": 4000,
        "secType": 3,
        "name": "Natural Dairy",
        "listTime": "2005-06-10",
        "delisting": false,
        "listTimestamp": 1.1183328E9
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "09858"
        },
        "id": "80676665697922",
        "lotSize": 1000,
        "secType": 3,
        "name": "China Youran Dairy",
        "listTime": "2021-06-18",
        "delisting": false,
        "listTimestamp": 1.6239456E9
      }
    }]
  }
}
```









`moomoo::u32_t GetPlateSecurity(const Qot_GetPlateSecurity::Request &stReq);`  
`virtual void OnReply_GetPlateSecurity(moomoo::u32_t nSerialNo, const Qot_GetPlateSecurity::Response &stRsp) = 0;`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
        Qot_GetPlateSecurity::Request req;
        Qot_GetPlateSecurity::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_plate();
        sec->set_code("BK1001");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetPlateSecuritySerialNo = m_pQotApi->GetPlateSecurity(req);
        cout << "Request GetPlateSecurity SerialNo: " << m_GetPlateSecuritySerialNo << endl;
    }

    virtual void OnReply_GetPlateSecurity(moomoo::u32_t nSerialNo, const Qot_GetPlateSecurity::Response &stRsp){
        if(nSerialNo == m_GetPlateSecuritySerialNo)
        {
            cout << "OnReply_GetPlateSecurity SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetPlateSecuritySerialNo;
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
Request GetPlateSecurity SerialNo: 4
OnReply_GetPlateSecurity SerialNo: 4
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
      "code": "00462"
     },
     "id": "55589761712590",
     "lotSize": 4000,
     "secType": 3,
     "name": "Natural Dairy",
     "listTime": "2005-06-10",
     "delisting": false,
     "listTimestamp": 1118332800
    }
   },
...
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "06186"
     },
     "id": "78159814858794",
     "lotSize": 1000,
     "secType": 3,
     "name": "China Feihe Limited",
     "listTime": "2019-11-13",
     "delisting": false,
     "listTimestamp": 1573574400
    }
   }
  ]
 }
}
```









`GetPlateSecurity(req);`

- **Description**

  Get the list of stocks in the plate, or get the constituent stocks of
  the stock index

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security plate = 1; //Plate
    optional int32 sortField = 2;//Qot_Common.SortField, according to which field to sort, sort by stock code by default
    optional bool ascend = 3;//True for ascending order, false for descending order, ascending by default

}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For sorting type, refer to
>   [SortField](/moomoo-api-doc/en/quote/quote.html#5823)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information of stocks under the plate
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
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetPlateSecurity(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    plate:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "Motherboard",
                    },
                },
            };

            websocket.GetPlateSecurity(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("PlateSecurity: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
PlateSecurity: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "00001"
      },
      "id": "4440996184065",
      "lotSize": 500,
      "secType": 3,
      "name": "CK Hutchison",
      "listTime": "2015-03-18",
      "delisting": false,
      "listTimestamp": 1426608000
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "00002"
      },
      "id": "2",
      "lotSize": 500,
      "secType": 3,
      "name": "CLP Holdings Limited",
      "listTime": "1970-01-01",
      "delisting": false,
      "listTimestamp": 0
    }
  }, ..., {
    "basic": {
      "security": {
        "market": 1,
        "code": "87001"
      },
      "id": "64819646518233",
      "lotSize": 1000,
      "secType": 4,
      "name": "Hui Xian Real Estate Investment Trust",
      "listTime": "2011-04-29",
      "delisting": false,
      "listTimestamp": 1304006400
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds



Commonly used sectors and index codes

| Code                      | Description                                    |
|:--------------------------|:-----------------------------------------------|
| HK.HSI Constituent Stocks | HSI constituent stocks                         |
| HK.HSCEI Stock            | HSCEI constituent stocks                       |
| HK.Motherboard            | Main Plate of Hong Kong Stocks                 |
| HK.GEM                    | GEM(Growth Enterprise Market) Hong Kong Stocks |
| HK.LIST1910               | All Hong Kong stocks                           |
| HK.LIST1911               | Main Plate H shares                            |
| HK.LIST1912               | GEM H shares                                   |
| HK.Fund                   | ETF (Hong Kong Stock Fund)                     |
| HK.LIST1600               | Hot List (Hong Kong)                           |
| HK.LIST1921               | Listed new shares-Hong Kong stocks             |
| SH.LIST3000000            | Shanghai Main Plate                            |
| SH.LIST0901               | Shanghai Stock Exchange B shares               |
| SH.LIST0902               | Shenzhen Stock Exchange B shares               |
| SH.LIST3000002            | Shanghai and Shenzhen Index                    |
| SH.LIST3000005            | All A-shares (Shanghai and Shenzhen)           |
| SH.LIST0600               | Hot List (Shanghai and Shenzhen)               |
| SH.LIST0992               | Science Innovation Plate                       |
| SH.LIST0921               | Listed New Shares - A-shares                   |
| SZ.LIST3000001            | SZSE Main Plate                                |
| SZ.LIST3000003            | Small and Medium Plate                         |
| SZ.LIST3000004            | The Growth Enterprise Market (Deep)            |
| US.USAALL                 | All US stocks                                  |











