



# <a href="#9665" class="header-anchor">#</a> Get the List of Trading Accounts









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_acc_list()`

- **Description**

  Get a list of trading accounts. Before calling other trading
  interfaces, please obtain this list first and confirm that the trading
  account to be operated is correct.

- **Parameters**

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
  <td>If ret == RET_OK, trading account list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Trading account list format as follows:
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
    <td style="text-align: left;">acc_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Trading account.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trd_env</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
    <td style="text-align: left;">Trading environment.</td>
    </tr>
    <tr>
    <td style="text-align: left;">acc_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7166">TrdAccType</a></td>
    <td style="text-align: left;">Account type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">uni_card_num</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Universal account number, same as the
    display in the mobile terminal.</td>
    </tr>
    <tr>
    <td style="text-align: left;">card_num</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Trading account number
    
      
    
    
     
    
    Under the Universal Account System, an Universal account contains one or
    more trading accounts(universal securities, universal futures, etc.),
    which is related to financing types.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sim_acc_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7358">SimAccType</a></td>
    <td style="text-align: left;">Simulate account type.
    
      
    
    
     
    
    For simulated accounts only.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">security_firm</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#9434">SecurityFirm</a></td>
    <td style="text-align: left;">Securities firm to which the account
    belongs.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trdmarket_auth</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Transaction market authority.
    
      
    
    
     
    
    Data type of elements in the list is <a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">acc_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#8311">TrdAccStatus</a></td>
    <td style="text-align: left;">Account status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">acc_role</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#121">TrdAccRole</a></td>
    <td style="text-align: left;">Account Structure
    
      
    
    
     
    
    Used to distinguish between master and normal account
    <ul>
    <li>MASTER: Master Account</li>
    <li>NORMAL: Normal Account</li>
    </ul>
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Description**

  After the paper trading of HK/US stock options is opened, this
  function will return 2 paper trading accounts when obtaining the list
  of HK/US trading accounts. The first one is the original account, and
  the second one is the option paper trading account. Currently, the US
  paper trading accounts from OpenAPI are different with those showed on
  the mobile app. Click [here](/moomoo-api-doc/en/qa/trade.html#732) for
  more details.

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_list()
if ret == RET_OK:
    print(data)
    print(data['acc_id'][0])  # Get the first account ID
    print(data['acc_id'].values.tolist())  # convert to list
else:
    print('get_acc_list error: ', data)
trd_ctx.close()
```





- **Output**



``` python
               acc_id   trd_env acc_type      uni_card_num          card_num   security_firm sim_acc_type            trdmarket_auth acc_status    acc_role
0  281756479345015383      REAL   MARGIN  1001289516908051  1001329805025007  FUTUSECURITIES          N/A  [HK, US, HKCC, SG, HKFUND, USFUND, JP]     ACTIVE     NORMAL
1             8377516  SIMULATE     CASH               N/A               N/A             N/A        STOCK                      [HK]     ACTIVE        N/A
2            10741586  SIMULATE   MARGIN               N/A               N/A             N/A       OPTION                      [HK]     ACTIVE        N/A
3  281756455983234027      REAL   MARGIN               N/A  1001100321720699  FUTUSECURITIES          N/A                      [HK]   DISABLED        NORMAL
281756479345015383
[281756479345015383, 8377516, 10741586, 281756455983234027]
```









## <a href="#3852" class="header-anchor">#</a> Trd_GetAccList.proto

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2001





`uint GetAccList(TrdGetAccList.Request req);`  
`virtual void OnReply_GetAccList(FTAPI_Conn client, uint nSerialNo, TrdGetAccList.Response rsp);`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        TrdGetAccList.C2S c2s = TrdGetAccList.C2S.CreateBuilder().SetUserID(5972312)
                .SetTrdCategory((int)TrdCommon.TrdCategory.TrdCategory_Security)
                .SetNeedGeneralSecAccount(true)
                .Build();
        TrdGetAccList.Request req = TrdGetAccList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetAccList(req);
        Console.Write("Send TrdGetAccList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetAccList(FTAPI_Conn client, uint nSerialNo, TrdGetAccList.Response rsp)
    {
        Console.Write("Reply: TrdGetAccList: {0}\n", nSerialNo);
        Console.Write("accID: {0}\n", rsp.S2C.AccListList[0].AccID);
    }

    public static void Main(String[] args) {
        FTAPI.Init();
        Program trd = new Program();
        trd.Start();


        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
Trd onInitConnect: ret=0 desc= connID=6826806647571888999
Send TrdGetAccList: 3
Reply: TrdGetAccList: 3
accID: 281756455989723220
```









`int getAccList(TrdGetAccList.Request req);`  
`void onReply_GetAccList(FTAPI_Conn client, int nSerialNo, TrdGetAccList.Response rsp);`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdGetAccList.C2S c2s = TrdGetAccList.C2S.newBuilder().setUserID(900053)
                .setTrdCategory(TrdCommon.TrdCategory.TrdCategory_Security_VALUE)
                .setNeedGeneralSecAccount(true)
                .build();
        TrdGetAccList.Request req = TrdGetAccList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getAccList(req);
        System.out.printf("Send TrdGetAccList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetAccList(FTAPI_Conn client, int nSerialNo, TrdGetAccList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetAccList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetAccList: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        FTAPI.init();
        TrdDemo trd = new TrdDemo();
        trd.start();

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
Send TrdGetAccList: 2
Receive TrdGetAccList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "accList": [{
      "trdEnv": 1,
      "accID": "281756466778014447",
      "trdMarketAuthList": [1],
      "accType": 2,
      "uniCardNum":"1001263856121256"
      "cardNum": "1002233560482767",
      "securityFirm": 1
    }, ... {
      "trdEnv": 0,
      "accID": "3547832",
      "trdMarketAuthList": [2],
      "accType": 2,
      "securityFirm": 0,
      "simAccType": 2
    }]
  }
}
```









`Futu::u32_t GetAccList(const Trd_GetAccList::Request &stReq);`  
`virtual void OnReply_GetAccList(Futu::u32_t nSerialNo, const Trd_GetAccList::Response &stRsp) = 0;`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cpp
class Program : public FTSPI_Qot, public FTSPI_Trd, public FTSPI_Conn
{
public:

    Program() {
        m_pTrdApi = FTAPI::CreateTrdApi();
        m_pTrdApi->RegisterTrdSpi(this);
        m_pTrdApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pTrdApi != nullptr)
        {
            m_pTrdApi->UnregisterTrdSpi();
            m_pTrdApi->UnregisterConnSpi();
            FTAPI::ReleaseTrdApi(m_pTrdApi);
            m_pTrdApi = nullptr;
        }
    }

    void Start() {
        m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(FTAPI_Conn* pConn, Futu::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Trd_GetAccList::Request req;
        Trd_GetAccList::C2S *c2s = req.mutable_c2s();
        c2s->set_userid(12345678);
        c2s->set_trdcategory(Trd_Common::TrdCategory::TrdCategory_Security);
        c2s->set_needgeneralsecaccount(true);

        m_GetAccListSerialNo = m_pTrdApi->GetAccList(req);
        cout << "Request GetAccList SerialNo: " << m_GetAccListSerialNo << endl;
    }

    virtual void OnReply_GetAccList(Futu::u32_t nSerialNo, const Trd_GetAccList::Response &stRsp){
        if(nSerialNo == m_GetAccListSerialNo)
        {
            cout << "OnReply_GetAccList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetAccListSerialNo;
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
Request GetAccList SerialNo: 4
OnReply_GetAccList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "accList": [
   {
    "trdEnv": 1,
    "accID": "281756456003951537",
    "trdMarketAuthList": [
     1
    ],
    "accType": 2,
    "uniCardNum":"1001263856121256"
    "cardNum": "1001100320714209",
    "securityFirm": 1
   },
...
   {
    "trdEnv": 0,
    "accID": "3637844",
    "trdMarketAuthList": [
     2
    ],
    "accType": 2,
    "securityFirm": 0,
    "simAccType": 2
   }
  ]
 }
}
```









`GetAccList(req);`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetAccList(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    const { TrdCategory } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 
            const req = {
                c2s: {
                    userID: 0,
                    trdCategory: TrdCategory.TrdCategory_Security,
                    needGeneralSecAccount: true,
                },
            };
            websocket.GetAccList(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("AccList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
AccList: errCode 0, retMsg , retType 0
{
  "accList": [{
    "trdEnv": 1,
    "accID": "281756456008357727",
    "trdMarketAuthList": [1],
    "accType": 2,
    "uniCardNum":"1001263856121256"
    "cardNum": "1001100321506782",
    "securityFirm": 1
  }, {
    "trdEnv": 1,
    "accID": "281756460303325023",
    "trdMarketAuthList": [2],
    "accType": 2,
    "uniCardNum":"1001256386562384"
    "cardNum": "1001100521938385",
    "securityFirm": 1
  }, ..., {
    "trdEnv": 0,
    "accID": "6684976",
    "trdMarketAuthList": [2],
    "accType": 2,
    "securityFirm": 0,
    "simAccType": 2
  }]
}
stop
```

















- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_acc_list()`

- **Description**

  Get a list of trading accounts. Before calling other trading
  interfaces, please obtain this list first and confirm that the trading
  account to be operated is correct.

- **Parameters**

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
  <td>If ret == RET_OK, trading account list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Trading account list format as follows:
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
    <td style="text-align: left;">acc_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Trading account.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trd_env</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
    <td style="text-align: left;">Trading environment.</td>
    </tr>
    <tr>
    <td style="text-align: left;">acc_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7166">TrdAccType</a></td>
    <td style="text-align: left;">Account type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">uni_card_num</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Universal account number, same as the
    display in the mobile terminal.</td>
    </tr>
    <tr>
    <td style="text-align: left;">card_num</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Trading account number
    
      
    
    
     
    
    Under the Universal Account System, an Universal account contains one or
    more trading accounts(universal securities, universal futures, etc.),
    which is related to financing types.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">sim_acc_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7358">SimAccType</a></td>
    <td style="text-align: left;">Simulate account type.
    
      
    
    
     
    
    For simulated accounts only.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">security_firm</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#9434">SecurityFirm</a></td>
    <td style="text-align: left;">Securities firm to which the account
    belongs.</td>
    </tr>
    <tr>
    <td style="text-align: left;">trdmarket_auth</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Transaction market authority.
    
      
    
    
     
    
    Data type of elements in the list is <a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">acc_role</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#121">TrdAccRole</a></td>
    <td style="text-align: left;">Account Structure
    
      
    
    
     
    
    Used to distinguish between master and normal account
    <ul>
    <li>MASTER: Master Account</li>
    <li>NORMAL: Normal Account</li>
    </ul>
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Description**

  After the paper trading of HK/US stock options is opened, this
  function will return 2 paper trading accounts when obtaining the list
  of HK/US trading accounts. The first one is the original account, and
  the second one is the option paper trading account. Currently, the US
  paper trading accounts from OpenAPI are different with those showed on
  the mobile app. Click [here](/moomoo-api-doc/en/qa/trade.html#732) for
  more details.

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.get_acc_list()
if ret == RET_OK:
    print(data)
    print(data['acc_id'][0])  # Get the first account ID
    print(data['acc_id'].values.tolist())  # convert to list
else:
    print('get_acc_list error: ', data)
trd_ctx.close()
```





- **Output**



``` python
               acc_id   trd_env acc_type        uni_card_num           card_num    security_firm   sim_acc_type   trdmarket_auth    acc_role
0  281756420273981734      REAL   MARGIN  10018561211263256   1001100530724347          FUTUINC            N/A          [HK, US, HKCC, SG, HKFUND, USFUND, JP]     NORMAL
1             3450310  SIMULATE     CASH                N/A                N/A              N/A          STOCK             [HK]        N/A
2             3548732  SIMULATE   MARGIN                N/A                N/A              N/A         OPTION             [HK]        N/A
281756420273981734
[281756420273981734, 3450310, 3548732]
```









## <a href="#3852-2" class="header-anchor">#</a> Trd_GetAccList.proto

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2001





`uint GetAccList(TrdGetAccList.Request req);`  
`virtual void OnReply_GetAccList(MMAPI_Conn client, uint nSerialNo, TrdGetAccList.Response rsp);`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Trd, MMSPI_Conn {
    MMAPI_Trd trd = new MMAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        TrdGetAccList.C2S c2s = TrdGetAccList.C2S.CreateBuilder().SetUserID(5972312)
                .SetTrdCategory((int)TrdCommon.TrdCategory.TrdCategory_Security)
                .SetNeedGeneralSecAccount(true) 
                .Build();
        TrdGetAccList.Request req = TrdGetAccList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetAccList(req);
        Console.Write("Send TrdGetAccList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetAccList(MMAPI_Conn client, uint nSerialNo, TrdGetAccList.Response rsp)
    {
        Console.Write("Reply: TrdGetAccList: {0}\n", nSerialNo);
        Console.Write("accID: {0}\n", rsp.S2C.AccListList[0].AccID);
    }

    public static void Main(String[] args) {
        MMAPI.Init();
        Program trd = new Program();
        trd.Start();


        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
Trd onInitConnect: ret=0 desc= connID=6826806647571888999
Send TrdGetAccList: 3
Reply: TrdGetAccList: 3
accID: 281756455989723220
```









`int getAccList(TrdGetAccList.Request req);`  
`void onReply_GetAccList(MMAPI_Conn client, int nSerialNo, TrdGetAccList.Response rsp);`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements MMSPI_Trd, MMSPI_Conn {
    MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdGetAccList.C2S c2s = TrdGetAccList.C2S.newBuilder().setUserID(900053)
                .setTrdCategory(TrdCommon.TrdCategory.TrdCategory_Security_VALUE)
                .setNeedGeneralSecAccount(true)
                .build();
        TrdGetAccList.Request req = TrdGetAccList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getAccList(req);
        System.out.printf("Send TrdGetAccList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetAccList(MMAPI_Conn client, int nSerialNo, TrdGetAccList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetAccList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetAccList: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        MMAPI.init();
        TrdDemo trd = new TrdDemo();
        trd.start();

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
Send TrdGetAccList: 2
Receive TrdGetAccList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "accList": [{
      "trdEnv": 1,
      "accID": "281756466778014447",
      "trdMarketAuthList": [1],
      "accType": 2,
      "uniCardNum":"1001263856121256"
      "cardNum": "1002233560482767",
      "securityFirm": 1
    }, ... {
      "trdEnv": 0,
      "accID": "3547832",
      "trdMarketAuthList": [2],
      "accType": 2,
      "securityFirm": 0,
      "simAccType": 2
    }]
  }
}
```









`moomoo::u32_t GetAccList(const Trd_GetAccList::Request &stReq);`  
`virtual void OnReply_GetAccList(moomoo::u32_t nSerialNo, const Trd_GetAccList::Response &stRsp) = 0;`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cpp
class Program : public MMSPI_Qot, public MMSPI_Trd, public MMSPI_Conn
{
public:

    Program() {
        m_pTrdApi = MMAPI::CreateTrdApi();
        m_pTrdApi->RegisterTrdSpi(this);
        m_pTrdApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pTrdApi != nullptr)
        {
            m_pTrdApi->UnregisterTrdSpi();
            m_pTrdApi->UnregisterConnSpi();
            MMAPI::ReleaseTrdApi(m_pTrdApi);
            m_pTrdApi = nullptr;
        }
    }

    void Start() {
        m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(MMAPI_Conn* pConn, moomoo::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Trd_GetAccList::Request req;
        Trd_GetAccList::C2S *c2s = req.mutable_c2s();
        c2s->set_userid(12345678);
        c2s->set_trdcategory(Trd_Common::TrdCategory::TrdCategory_Security);
        c2s->set_needgeneralsecaccount(true);

        m_GetAccListSerialNo = m_pTrdApi->GetAccList(req);
        cout << "Request GetAccList SerialNo: " << m_GetAccListSerialNo << endl;
    }

    virtual void OnReply_GetAccList(moomoo::u32_t nSerialNo, const Trd_GetAccList::Response &stRsp){
        if(nSerialNo == m_GetAccListSerialNo)
        {
            cout << "OnReply_GetAccList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetAccListSerialNo;
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
Request GetAccList SerialNo: 4
OnReply_GetAccList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "accList": [
   {
    "trdEnv": 1,
    "accID": "281756456003951537",
    "trdMarketAuthList": [
     1
    ],
    "accType": 2,
    "uniCardNum":"1001263856121256"
    "cardNum": "1001100320714209",
    "securityFirm": 1
   },
...
   {
    "trdEnv": 0,
    "accID": "3637844",
    "trdMarketAuthList": [
     2
    ],
    "accType": 2,
    "securityFirm": 0,
    "simAccType": 2
   }
  ]
 }
}
```









`GetAccList(req);`

- **Description**

  Get a list of trading accounts

- **Parameters**



``` protobuf
message C2S
{
    required uint64 userID = 1; //For historical reasons, it is currently deprecated, just fill in 0
    optional int32 trdCategory = 2; //Transaction Category, refer to Trd_Common.TrdCategory
    optional bool needGeneralSecAccount = 3; //Whether to return to the general securities accounts. (Applicable for HK/US/SG/AU universal account)
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
    repeated Trd_Common.TrdAcc accList = 1; //List of trading accounts
}

message Response
{
    //The following 3 fields are available for all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For the Transaction Category, please refer to
>   [TrdCategory](/moomoo-api-doc/en/trade/trade.html#9120)
> - For the trading account structure, please refer to
>   [TrdAcc](/moomoo-api-doc/en/trade/trade.html#2879)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdGetAccList(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    const { TrdCategory } = Trd_Common    
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 
            const req = {
                c2s: {
                    userID: 0,
                    trdCategory: TrdCategory.TrdCategory_Security,
                    needGeneralSecAccount: true,
                },
            };
            websocket.GetAccList(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("AccList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
AccList: errCode 0, retMsg , retType 0
{
  "accList": [{
    "trdEnv": 1,
    "accID": "281756456008357727",
    "trdMarketAuthList": [1],
    "accType": 2,
    "uniCardNum":"1001263856121256"
    "cardNum": "1001100321506782",
    "securityFirm": 1
  }, {
    "trdEnv": 1,
    "accID": "281756460303325023",
    "trdMarketAuthList": [2],
    "accType": 2,
    "uniCardNum":"1001256386562384"
    "cardNum": "1001100521938385",
    "securityFirm": 1
  }, ..., {
    "trdEnv": 0,
    "accID": "6684976",
    "trdMarketAuthList": [2],
    "accType": 2,
    "securityFirm": 0,
    "simAccType": 2
  }]
}
stop
```



















