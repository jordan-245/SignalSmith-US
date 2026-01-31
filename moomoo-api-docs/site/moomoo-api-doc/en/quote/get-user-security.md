



# <a href="#1776" class="header-anchor">#</a> Get The Watchlist









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_user_security(group_name)`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**

  | Parameter  | Type | Description                                     |
  |:-----------|:-----|:------------------------------------------------|
  | group_name | str  | The name of the specified group from watchlist. |

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
  <td>If ret == RET_OK, watchlist is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Watchlist data format as follows:
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
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of shares per lot, number of shares
    per contract for options, contract multiplier for futures.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Stock type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_child_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
    <td style="text-align: left;">Warrant type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The code of the underlying stock to which
    the warrant belongs, or the code of the underlying stock of the
    option.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
    <td style="text-align: left;">Option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The option exercise date.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Option strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the option is suspended.
    
      
    
    
     
    
    True: suspension
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date.
    
      
    
    
     
    
    Format: yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Stock ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">delisting</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether is delisted.</td>
    </tr>
    <tr>
    <td style="text-align: left;">main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether is future main contract.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.
    
      
    
    
     
    
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_user_security("A")
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the user security list is not empty
        print(data['code'][0]) # Take the first stock code
        print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code    name  lot_size stock_type stock_child_type stock_owner option_type strike_time strike_price suspension listing_date        stock_id  delisting  main_contract last_trade_time
0  HK.HSImain  HSI Future Main(NOV0)        50     FUTURE              N/A                                              N/A        N/A                     71000662      False           True                
1  HK.00700    Tencent Holdings       100      STOCK              N/A                                              N/A        N/A   2004-06-16  54047868453564      False          False                
HK.HSImain
['HK.HSImain', 'HK.00700']
```









## <a href="#2143" class="header-anchor">#</a> Qot_GetUserSecurity.proto

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3213





`uint GetUserSecurity(QotGetUserSecurity.Request req);`  
`virtual void OnReply_GetUserSecurity(FTAPI_Conn client, uint nSerialNo, QotGetUserSecurity.Response rsp);`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
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

        QotGetUserSecurity.C2S c2s = QotGetUserSecurity.C2S.CreateBuilder()
                .SetGroupName("some_group")
            .Build();
        QotGetUserSecurity.Request req = QotGetUserSecurity.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetUserSecurity(req);
        Console.Write("Send QotGetUserSecurity: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetUserSecurity(FTAPI_Conn client, uint nSerialNo, QotGetUserSecurity.Response rsp)
    {
        Console.Write("Reply: QotGetUserSecurity: {0}\n", nSerialNo);
        if(rsp.S2C.StaticInfoListCount > 0)
        {
            Console.Write("name: {0} \n", rsp.S2C.StaticInfoListList[0].Basic.Name);
        }            
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
Qot onInitConnect: ret=0 desc= connID=6826787829878316131
Send QotGetUserSecurity: 3
Reply: QotGetUserSecurity: 3
name: Tencent Holdings
```









`int getUserSecurity(QotGetUserSecurity.Request req);`  
`void onReply_GetUserSecurity(FTAPI_Conn client, int nSerialNo, QotGetUserSecurity.Response rsp);`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
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

        QotGetUserSecurity.C2S c2s = QotGetUserSecurity.C2S.newBuilder()
                .setGroupName("some_group")
            .build();
        QotGetUserSecurity.Request req = QotGetUserSecurity.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getUserSecurity(req);
        System.out.printf("Send QotGetUserSecurity: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetUserSecurity(FTAPI_Conn client, int nSerialNo, QotGetUserSecurity.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetUserSecurity failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetUserSecurity: %s\n", json);
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
Send QotGetUserSecurity: 2
Receive QotGetUserSecurity: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "09626"
        },
        "id": "80328773346714",
        "lotSize": 20,
        "secType": 3,
        "name": "Bilibili Inc.",
        "listTime": "2021-03-29",
        "delisting": false,
        "listTimestamp": 1.6169472E9
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "800000"
        },
        "id": "800000",
        "lotSize": 0,
        "secType": 6,
        "name": "Hang Seng Index",
        "listTime": "1970-01-01",
        "delisting": false,
        "listTimestamp": 0.0
      }
    }]
  }
}
```









`Futu::u32_t GetUserSecurity(const Qot_GetUserSecurity::Request &stReq);`  
`virtual void OnReply_GetUserSecurity(Futu::u32_t nSerialNo, const Qot_GetUserSecurity::Response &stRsp) = 0;`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
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
        Qot_GetUserSecurity::Request req;
        Qot_GetUserSecurity::C2S *c2s = req.mutable_c2s();
        c2s->set_groupname("some_group");

        m_GetUserSecuritySerialNo = m_pQotApi->GetUserSecurity(req);
        cout << "Request GetUserSecurity SerialNo: " << m_GetUserSecuritySerialNo << endl;
    }

    virtual void OnReply_GetUserSecurity(Futu::u32_t nSerialNo, const Qot_GetUserSecurity::Response &stRsp){
        if(nSerialNo == m_GetUserSecuritySerialNo)
        {
            cout << "OnReply_GetUserSecurity SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetUserSecuritySerialNo;
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
Request GetUserSecurity SerialNo: 4
OnReply_GetUserSecurity SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "staticInfoList": [
   {
    "basic": {
     "security": {
      "market": 11,
      "code": "FUTU"
     },
     "id": "78103980495165",
     "lotSize": 1,
     "secType": 3,
     "name": "Futu Holdings Limited",
     "listTime": "2019-03-08",
     "delisting": false,
     "listTimestamp": 1552021200
    }
   },
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "00700"
     },
     "id": "54047868453564",
     "lotSize": 100,
     "secType": 3,
     "name": "Tencent",
     "listTime": "2004-06-16",
     "delisting": false,
     "listTimestamp": 1087315200
    }
   }
  ]
 }
}
```









`GetUserSecurity(req);`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetUserSecurity(){
    const { RetType } = Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    groupName: "港股",
                },
            };
            
            websocket.GetUserSecurity(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("UserSecurity: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
UserSecurity: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "800000"
      },
      "id": "800000",
      "lotSize": 0,
      "secType": 6,
      "name": "Hang Seng Index",
      "listTime": "1970-01-01",
      "delisting": false,
      "listTimestamp": 0
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "09988"
      },
      "id": "78224239372036",
      "lotSize": 100,
      "secType": 3,
      "name": "BABA-SW",
      "listTime": "2019-11-26",
      "delisting": false,
      "listTimestamp": 1574697600
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "00700"
      },
      "id": "54047868453564",
      "lotSize": 100,
      "secType": 3,
      "name": "Tencent",
      "listTime": "2004-06-16",
      "delisting": false,
      "listTimestamp": 1087315200
    }
  }]
}
stop
```











Tips

The corresponding Chinese and English names of the system group are as
follows

| Chinese  | English    |
|:---------|:-----------|
| 全部     | All        |
| 沪深     | CN         |
| 港股     | HK         |
| 美股     | US         |
| 期权     | Options    |
| 港股期权 | HK options |
| 美股期权 | US options |
| 特别关注 | Starred    |
| 期货     | Futures    |





Interface Limitations

- A maximum of 10 requests per 30 seconds
- Does not support position (Positions), fund treasure (Mutual Fund),
  foreign exchange (Forex) group query











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_user_security(group_name)`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**

  | Parameter  | Type | Description                                     |
  |:-----------|:-----|:------------------------------------------------|
  | group_name | str  | The name of the specified group from watchlist. |

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
  <td>If ret == RET_OK, watchlist is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Watchlist data format as follows:
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
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of shares per lot, number of shares
    per contract for options, contract multiplier for futures.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
    <td style="text-align: left;">Stock type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_child_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2421">WrtType</a></td>
    <td style="text-align: left;">Warrant type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_owner</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The code of the underlying stock to which
    the warrant belongs, or the code of the underlying stock of the
    option.</td>
    </tr>
    <tr>
    <td style="text-align: left;">option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9598">OptionType</a></td>
    <td style="text-align: left;">Option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The option exercise date.
    
      
    
    
     
    
    Format: yyyy-MM-dd<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Option strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the option is suspended.
    
      
    
    
     
    
    True: suspension
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date.
    
      
    
    
     
    
    Format: yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Stock ID.</td>
    </tr>
    <tr>
    <td style="text-align: left;">delisting</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether is delisted.</td>
    </tr>
    <tr>
    <td style="text-align: left;">main_contract</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether is future main contract.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_trade_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Last trading time.
    
      
    
    
     
    
    Main, current month and next month futures do not have this field.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_user_security("A")
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the user security list is not empty
        print(data['code'][0]) # Take the first stock code
        print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code    name  lot_size stock_type stock_child_type stock_owner option_type strike_time strike_price suspension listing_date        stock_id  delisting  main_contract last_trade_time
0  HK.HSImain  HSI Future Main(NOV0)        50     FUTURE              N/A                                              N/A        N/A                     71000662      False           True                
1  HK.00700    Tencent Holdings       100      STOCK              N/A                                              N/A        N/A   2004-06-16  54047868453564      False          False                
HK.HSImain
['HK.HSImain', 'HK.00700']
```









## <a href="#2143-2" class="header-anchor">#</a> Qot_GetUserSecurity.proto

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3213





`uint GetUserSecurity(QotGetUserSecurity.Request req);`  
`virtual void OnReply_GetUserSecurity(MMAPI_Conn client, uint nSerialNo, QotGetUserSecurity.Response rsp);`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
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

        QotGetUserSecurity.C2S c2s = QotGetUserSecurity.C2S.CreateBuilder()
                .SetGroupName("some_group")
            .Build();
        QotGetUserSecurity.Request req = QotGetUserSecurity.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetUserSecurity(req);
        Console.Write("Send QotGetUserSecurity: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetUserSecurity(MMAPI_Conn client, uint nSerialNo, QotGetUserSecurity.Response rsp)
    {
        Console.Write("Reply: QotGetUserSecurity: {0}\n", nSerialNo);
        if(rsp.S2C.StaticInfoListCount > 0)
        {
            Console.Write("name: {0} \n", rsp.S2C.StaticInfoListList[0].Basic.Name);
        }            
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
Qot onInitConnect: ret=0 desc= connID=6826787829878316131
Send QotGetUserSecurity: 3
Reply: QotGetUserSecurity: 3
name: Tencent Holdings
```









`int getUserSecurity(QotGetUserSecurity.Request req);`  
`void onReply_GetUserSecurity(MMAPI_Conn client, int nSerialNo, QotGetUserSecurity.Response rsp);`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
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

        QotGetUserSecurity.C2S c2s = QotGetUserSecurity.C2S.newBuilder()
                .setGroupName("some_group")
            .build();
        QotGetUserSecurity.Request req = QotGetUserSecurity.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getUserSecurity(req);
        System.out.printf("Send QotGetUserSecurity: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetUserSecurity(MMAPI_Conn client, int nSerialNo, QotGetUserSecurity.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetUserSecurity failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetUserSecurity: %s\n", json);
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
Send QotGetUserSecurity: 2
Receive QotGetUserSecurity: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "09626"
        },
        "id": "80328773346714",
        "lotSize": 20,
        "secType": 3,
        "name": "Bilibili Inc.",
        "listTime": "2021-03-29",
        "delisting": false,
        "listTimestamp": 1.6169472E9
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "800000"
        },
        "id": "800000",
        "lotSize": 0,
        "secType": 6,
        "name": "Hang Seng Index",
        "listTime": "1970-01-01",
        "delisting": false,
        "listTimestamp": 0.0
      }
    }]
  }
}
```









`moomoo::u32_t GetUserSecurity(const Qot_GetUserSecurity::Request &stReq);`  
`virtual void OnReply_GetUserSecurity(moomoo::u32_t nSerialNo, const Qot_GetUserSecurity::Response &stRsp) = 0;`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
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
        Qot_GetUserSecurity::Request req;
        Qot_GetUserSecurity::C2S *c2s = req.mutable_c2s();
        c2s->set_groupname("some_group");

        m_GetUserSecuritySerialNo = m_pQotApi->GetUserSecurity(req);
        cout << "Request GetUserSecurity SerialNo: " << m_GetUserSecuritySerialNo << endl;
    }

    virtual void OnReply_GetUserSecurity(moomoo::u32_t nSerialNo, const Qot_GetUserSecurity::Response &stRsp){
        if(nSerialNo == m_GetUserSecuritySerialNo)
        {
            cout << "OnReply_GetUserSecurity SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetUserSecuritySerialNo;
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
Request GetUserSecurity SerialNo: 4
OnReply_GetUserSecurity SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "staticInfoList": [
   {
    "basic": {
     "security": {
      "market": 11,
      "code": "FUTU"
     },
     "id": "78103980495165",
     "lotSize": 1,
     "secType": 3,
     "name": "Futu Holdings Limited",
     "listTime": "2019-03-08",
     "delisting": false,
     "listTimestamp": 1552021200
    }
   },
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "00700"
     },
     "id": "54047868453564",
     "lotSize": 100,
     "secType": 3,
     "name": "Tencent",
     "listTime": "2004-06-16",
     "delisting": false,
     "listTimestamp": 1087315200
    }
   }
  ]
 }
}
```









`GetUserSecurity(req);`

- **Description**

  Get a list of a specified group from watchlist

- **Parameters**



``` protobuf
message C2S
{
    required string groupName = 1; //Group name, the first one will be returned if multiple groups have the same name
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
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //List of stocks under the watchlist group
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - See for stock static information structure
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetUserSecurity(){
    const { RetType } = Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    groupName: "港股",
                },
            };
            
            websocket.GetUserSecurity(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("UserSecurity: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
UserSecurity: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
    "basic": {
      "security": {
        "market": 1,
        "code": "800000"
      },
      "id": "800000",
      "lotSize": 0,
      "secType": 6,
      "name": "Hang Seng Index",
      "listTime": "1970-01-01",
      "delisting": false,
      "listTimestamp": 0
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "09988"
      },
      "id": "78224239372036",
      "lotSize": 100,
      "secType": 3,
      "name": "BABA-SW",
      "listTime": "2019-11-26",
      "delisting": false,
      "listTimestamp": 1574697600
    }
  }, {
    "basic": {
      "security": {
        "market": 1,
        "code": "00700"
      },
      "id": "54047868453564",
      "lotSize": 100,
      "secType": 3,
      "name": "Tencent",
      "listTime": "2004-06-16",
      "delisting": false,
      "listTimestamp": 1087315200
    }
  }]
}
stop
```











Tips

The corresponding Chinese and English names of the system group are as
follows

| Chinese  | English    |
|:---------|:-----------|
| 全部     | All        |
| 沪深     | CN         |
| 港股     | HK         |
| 美股     | US         |
| 期权     | Options    |
| 港股期权 | HK options |
| 美股期权 | US options |
| 特别关注 | Starred    |
| 期货     | Futures    |





Interface Limitations

- A maximum of 10 requests per 30 seconds
- Does not support position (Positions), fund treasure (Mutual Fund),
  foreign exchange (Forex) group query













