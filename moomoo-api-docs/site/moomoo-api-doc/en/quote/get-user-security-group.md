



# <a href="#6097" class="header-anchor">#</a> Get Groups From Watchlist









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_user_security_group(group_type = UserSecurityGroupType.ALL)`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | group_type | [UserSecurityGroupType](/moomoo-api-doc/en/quote/quote.html#8561) | Group type. |

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
  <td>If ret == RET_OK, group data of watchlist is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Group data of watchlist format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | group_name | str | Group name. |
    | group_type | [UserSecurityGroupType](/moomoo-api-doc/en/quote/quote.html#8561) | Group type. |

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_user_security_group(group_type = UserSecurityGroupType.ALL)
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
        group_name group_type
0          Options     SYSTEM
..         ...        ...
12          C     CUSTOM

[13 rows x 2 columns]
```









## <a href="#2010" class="header-anchor">#</a> Qot_GetUserSecurityGroup.proto

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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

  3222





`uint GetUserSecurityGroup(QotGetUserSecurityGroup.Request req);`  
`virtual void OnReply_GetUserSecurityGroup(FTAPI_Conn client, uint nSerialNo, QotGetUserSecurityGroup.Response rsp);`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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

        QotGetUserSecurityGroup.C2S c2s = QotGetUserSecurityGroup.C2S.CreateBuilder()
                .SetGroupType(QotGetUserSecurityGroup.GroupType.GroupType_All)
            .Build();
        QotGetUserSecurityGroup.Request req = QotGetUserSecurityGroup.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetUserSecurityGroup(req);
        Console.Write("Send QotGetUserSecurityGroup: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetUserSecurityGroup(FTAPI_Conn client, uint nSerialNo, QotGetUserSecurityGroup.Response rsp)
    {
        Console.Write("Reply: QotGetUserSecurityGroup: {0}\n", nSerialNo);
        Console.Write("groupName: {0}, groupType: {1} \n", rsp.S2C.GroupListList[0].GroupName, rsp.S2C.GroupListList[0].GroupType);
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
Qot onInitConnect: ret=0 desc= connID=6826789498578847020
Send QotGetUserSecurityGroup: 3
Reply: QotGetUserSecurityGroup: 3
groupName: All, groupType: 2
```









`int getUserSecurityGroup(QotGetUserSecurityGroup.Request req);`  
`void onReply_GetUserSecurityGroup(FTAPI_Conn client, int nSerialNo, QotGetUserSecurityGroup.Response rsp);`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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

        QotGetUserSecurityGroup.C2S c2s = QotGetUserSecurityGroup.C2S.newBuilder()
                .setGroupType(QotGetUserSecurityGroup.GroupType.GroupType_All_VALUE)
            .build();
        QotGetUserSecurityGroup.Request req = QotGetUserSecurityGroup.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getUserSecurityGroup(req);
        System.out.printf("Send QotGetUserSecurityGroup: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetUserSecurityGroup(FTAPI_Conn client, int nSerialNo, QotGetUserSecurityGroup.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetUserSecurityGroup failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetUserSecurityGroup: %s\n", json);
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
Send QotGetUserSecurityGroup: 2
Receive QotGetUserSecurityGroup: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "groupList": [{
      "groupName": "All",
      "groupType": 2
    }, {
      "groupName": "Starred",
      "groupType": 2
    }, ... {
      "groupName": "Bonds",
      "groupType": 2
    }]
  }
}
```









`Futu::u32_t GetUserSecurityGroup(const Qot_GetUserSecurityGroup::Request &stReq);`  
`virtual void OnReply_GetUserSecurityGroup(Futu::u32_t nSerialNo, const Qot_GetUserSecurityGroup::Response &stRsp) = 0;`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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
        Qot_GetUserSecurityGroup::Request req;
        Qot_GetUserSecurityGroup::C2S *c2s = req.mutable_c2s();
        c2s->set_grouptype(3);

        m_GetUserSecurityGroupSerialNo = m_pQotApi->GetUserSecurityGroup(req);
        cout << "Request GetUserSecurityGroup SerialNo: " << m_GetUserSecurityGroupSerialNo << endl;
    }

    virtual void OnReply_GetUserSecurityGroup(Futu::u32_t nSerialNo, const Qot_GetUserSecurityGroup::Response &stRsp){
        if(nSerialNo == m_GetUserSecurityGroupSerialNo)
        {
            cout << "OnReply_GetUserSecurityGroup SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetUserSecurityGroupSerialNo;
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
Request GetUserSecurityGroup SerialNo: 4
OnReply_GetUserSecurityGroup SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "groupList": [
   {
    "groupName": "All",
    "groupType": 2
   },
...
   {
    "groupName": "Bonds",
    "groupType": 2
   }
  ]
 }
}
```









`GetUserSecurityGroup(req);`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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
import { Common, Qot_Common, Qot_GetUserSecurityGroup } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetUserSecurityGroup(){
    const { RetType } = Common
    const { GroupType } = Qot_GetUserSecurityGroup
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    groupType: GroupType.GroupType_All,
                },
            };
            
            websocket.GetUserSecurityGroup(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("UserSecurityGroup: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
UserSecurityGroup: errCode 0, retMsg , retType 0
{
  "groupList": [{
    "groupName": "All",
    "groupType": 2
  }, {
    "groupName": "Starred",
    "groupType": 2
  }, ..., {
    "groupName": "testgroup",
    "groupType": 1
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_user_security_group(group_type = UserSecurityGroupType.ALL)`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | group_type | [UserSecurityGroupType](/moomoo-api-doc/en/quote/quote.html#8561) | Group type. |

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
  <td>If ret == RET_OK, group data of watchlist is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Group data of watchlist format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | group_name | str | Group name. |
    | group_type | [UserSecurityGroupType](/moomoo-api-doc/en/quote/quote.html#8561) | Group type. |

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_user_security_group(group_type = UserSecurityGroupType.ALL)
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
        group_name group_type
0          Options     SYSTEM
..         ...        ...
12          C     CUSTOM

[13 rows x 2 columns]
```









## <a href="#2010-2" class="header-anchor">#</a> Qot_GetUserSecurityGroup.proto

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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

  3222





`uint GetUserSecurityGroup(QotGetUserSecurityGroup.Request req);`  
`virtual void OnReply_GetUserSecurityGroup(MMAPI_Conn client, uint nSerialNo, QotGetUserSecurityGroup.Response rsp);`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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

        QotGetUserSecurityGroup.C2S c2s = QotGetUserSecurityGroup.C2S.CreateBuilder()
                .SetGroupType(QotGetUserSecurityGroup.GroupType.GroupType_All)
            .Build();
        QotGetUserSecurityGroup.Request req = QotGetUserSecurityGroup.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetUserSecurityGroup(req);
        Console.Write("Send QotGetUserSecurityGroup: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetUserSecurityGroup(MMAPI_Conn client, uint nSerialNo, QotGetUserSecurityGroup.Response rsp)
    {
        Console.Write("Reply: QotGetUserSecurityGroup: {0}\n", nSerialNo);
        Console.Write("groupName: {0}, groupType: {1} \n", rsp.S2C.GroupListList[0].GroupName, rsp.S2C.GroupListList[0].GroupType);
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
Qot onInitConnect: ret=0 desc= connID=6826789498578847020
Send QotGetUserSecurityGroup: 3
Reply: QotGetUserSecurityGroup: 3
groupName: All, groupType: 2
```









`int getUserSecurityGroup(QotGetUserSecurityGroup.Request req);`  
`void onReply_GetUserSecurityGroup(MMAPI_Conn client, int nSerialNo, QotGetUserSecurityGroup.Response rsp);`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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

        QotGetUserSecurityGroup.C2S c2s = QotGetUserSecurityGroup.C2S.newBuilder()
                .setGroupType(QotGetUserSecurityGroup.GroupType.GroupType_All_VALUE)
            .build();
        QotGetUserSecurityGroup.Request req = QotGetUserSecurityGroup.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getUserSecurityGroup(req);
        System.out.printf("Send QotGetUserSecurityGroup: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetUserSecurityGroup(MMAPI_Conn client, int nSerialNo, QotGetUserSecurityGroup.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetUserSecurityGroup failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetUserSecurityGroup: %s\n", json);
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
Send QotGetUserSecurityGroup: 2
Receive QotGetUserSecurityGroup: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "groupList": [{
      "groupName": "All",
      "groupType": 2
    }, {
      "groupName": "Starred",
      "groupType": 2
    }, ... {
      "groupName": "Bonds",
      "groupType": 2
    }]
  }
}
```









`moomoo::u32_t GetUserSecurityGroup(const Qot_GetUserSecurityGroup::Request &stReq);`  
`virtual void OnReply_GetUserSecurityGroup(moomoo::u32_t nSerialNo, const Qot_GetUserSecurityGroup::Response &stRsp) = 0;`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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
        Qot_GetUserSecurityGroup::Request req;
        Qot_GetUserSecurityGroup::C2S *c2s = req.mutable_c2s();
        c2s->set_grouptype(3);

        m_GetUserSecurityGroupSerialNo = m_pQotApi->GetUserSecurityGroup(req);
        cout << "Request GetUserSecurityGroup SerialNo: " << m_GetUserSecurityGroupSerialNo << endl;
    }

    virtual void OnReply_GetUserSecurityGroup(moomoo::u32_t nSerialNo, const Qot_GetUserSecurityGroup::Response &stRsp){
        if(nSerialNo == m_GetUserSecurityGroupSerialNo)
        {
            cout << "OnReply_GetUserSecurityGroup SerialNo:" << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetUserSecurityGroupSerialNo;
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
Request GetUserSecurityGroup SerialNo: 4
OnReply_GetUserSecurityGroup SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "groupList": [
   {
    "groupName": "All",
    "groupType": 2
   },
...
   {
    "groupName": "Bonds",
    "groupType": 2
   }
  ]
 }
}
```









`GetUserSecurityGroup(req);`

- **Description**

  Get a list of groups from the user watchlist

- **Parameters**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message C2S
{
    required int32 groupType = 1; //GroupType, watchlist group type
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
// Type of self-selected stock
enum GroupType
{
    GroupType_Unknown = 0; //Unknown
    GroupType_Custom = 1; //Custom group
    GroupType_System = 2; //System group
    GroupType_All = 3; //All groups
}

message GroupData
{
    required string groupName = 1; //Group name from watchlist
    required int32 groupType = 2; //GroupType, watchlist group type
}

message S2C
{
    repeated GroupData groupList = 1; //Watchlist group list
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
import { Common, Qot_Common, Qot_GetUserSecurityGroup } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetUserSecurityGroup(){
    const { RetType } = Common
    const { GroupType } = Qot_GetUserSecurityGroup
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    groupType: GroupType.GroupType_All,
                },
            };
            
            websocket.GetUserSecurityGroup(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("UserSecurityGroup: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
UserSecurityGroup: errCode 0, retMsg , retType 0
{
  "groupList": [{
    "groupName": "All",
    "groupType": 2
  }, {
    "groupName": "Starred",
    "groupType": 2
  }, ..., {
    "groupName": "testgroup",
    "groupType": 1
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds













