



# <a href="#5713" class="header-anchor">#</a> Unlock Trade









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`unlock_trade(password=None, password_md5=None, is_unlock=True)`

- **Description**

  Lock or unlock trade

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
  <td style="text-align: left;">password</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Transaction password.
  
    
  
  
   
  
  If password_md5 is not empty, use the passed password_md5 to
  unlock.<br />
  Otherwise, MD5 calculated from password is used for password_md5 and
  then unlock.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">password_md5</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">32-bit MD5 encryption of transaction
  password (all lowercase).
  
    
  
  
   
  
  A password must be filled in to unlock a transaction, and a locked
  transaction is ignored.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">is_unlock</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Lock or unlock.
  
    
  
  
   
  
  True: unlock.<br />
  False: lock.
  
  
  
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
  <td rowspan="2">msg</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from futu import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.unlock_trade(pwd_unlock)
if ret == RET_OK:
    print('unlock success!')
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python
unlock success!
```









## <a href="#661" class="header-anchor">#</a> Trd_UnlockTrade.proto

- **Description**

  Unlock or lock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2005





`uint UnlockTrade(TrdUnlockTrade.Request req);`  
`virtual void OnReply_UnlockTrade(FTAPI_Conn client, uint nSerialNo, TrdUnlockTrade.Response rsp);`

- **Description**

  Unlock or lock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: FTSPI_Trd, FTSPI_Conn {
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
        
        TrdUnlockTrade.C2S c2s = TrdUnlockTrade.C2S.CreateBuilder()
                .SetPwdMD5("e10adc3949ba59abbe56e057f20f883e")
                .SetUnlock(true)
                .SetSecurityFirm((int)TrdCommon.SecurityFirm.SecurityFirm_FutuSecurities)
                .Build();
        TrdUnlockTrade.Request req = TrdUnlockTrade.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.UnlockTrade(req);
        Console.Write("Send TrdUnlockTrade: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_UnlockTrade(FTAPI_Conn client, uint nSerialNo, TrdUnlockTrade.Response rsp)
    {
        Console.Write("Reply: TrdUnlockTrade: {0}\n", nSerialNo);
        Console.Write("retMsg: {0}\n", rsp.RetMsg);
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
Trd onInitConnect: ret=0 desc= connID=6826809697310867898
Send TrdUnlockTrade: 3
Reply: TrdUnlockTrade: 3
retMsg: 
```









`int unlockTrade(TrdUnlockTrade.Request req);`  
`void onReply_UnlockTrade(FTAPI_Conn client, int nSerialNo, TrdUnlockTrade.Response rsp);`

- **Description**

  Unlock or lock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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
        
        TrdUnlockTrade.C2S c2s = TrdUnlockTrade.C2S.newBuilder()
                .setPwdMD5("e10adc3949ba59abbe56e057f20f883e")
                .setUnlock(true)
                .setSecurityFirm(TrdCommon.SecurityFirm.SecurityFirm_FutuSecurities_VALUE)
                .build();
        TrdUnlockTrade.Request req = TrdUnlockTrade.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.unlockTrade(req);
        System.out.printf("Send TrdUnlockTrade: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_UnlockTrade(FTAPI_Conn client, int nSerialNo, TrdUnlockTrade.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdUnlockTrade failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdUnlockTrade: %s\n", json);
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
Send TrdUnlockTrade: 2
Receive TrdUnlockTrade: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0
}
```









`Futu::u32_t UnlockTrade(const Trd_UnlockTrade::Request &stReq);`  
`virtual void OnReply_UnlockTrade(Futu::u32_t nSerialNo, const Trd_UnlockTrade::Response &stRsp) = 0;`

- **Description**

  Lock or unlock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
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
        Trd_UnlockTrade::Request req;
        Trd_UnlockTrade::C2S *c2s = req.mutable_c2s();
        c2s->set_pwdmd5("e10adc3949ba59abbe56e057f20f883e");
        c2s->set_unlock(true);
        c2s->set_securityfirm(Trd_Common::SecurityFirm::SecurityFirm_FutuSecurities);

        m_UnlockTradeSerialNo = m_pTrdApi->UnlockTrade(req);
        cout << "Request UnlockTrade SerialNo: " << m_UnlockTradeSerialNo << endl;
    }

    virtual void OnReply_UnlockTrade(Futu::u32_t nSerialNo, const Trd_UnlockTrade::Response &stRsp){
        if(nSerialNo == m_UnlockTradeSerialNo)
        {
            cout << "OnReply_UnlockTrade SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }
    
protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_UnlockTradeSerialNo;
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
Request UnlockTrade SerialNo: 4
OnReply_UnlockTrade SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0
}
```









`UnlockTrade(req);`

- **Description**

  Lock or unlock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
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
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdUnlockTrade(){
    const { RetType } = Common
    const { SecurityFirm } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    unlock: true,
                    securityFirm: SecurityFirm.SecurityFirm_FutuSecurities,
                    pwdMD5: "d0970714757783e6cf17b26fb8e2298f", // Set as the transaction password MD5 of your account
                },
            };
            websocket.UnlockTrade(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("UnlockTrade: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
UnlockTrade: errCode 0, retMsg , retType 0
null
stop
```











TIP

- When using live trading accounts, you need to **unlock trade**
  **before** calling *Place Order* or *Modify or Cancel Orders*
  interface, but when using paper trading accounts, you do not need to
  **unlock trade**.
- Locking or unlocking the transaction is an operation on OpenD. As long
  as one connection is unlocked, all other connections can call the
  transaction interface
- It is strongly recommended that customers who connect to OpenD via the
  external network for live trading use encrypted channels, refer to
  [Enable protocol encryption](/moomoo-api-doc/en/ftapi/init.html#7910)
- OpenAPI does not support Futu token. If you have activated Futu token,
  it will fail to unlock. You need to turn off the token and then use
  OpenAPI to unlock.





Interface Limitations

- A maximum of 10 requests per 30 seconds under a single user ID.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`unlock_trade(password=None, password_md5=None, is_unlock=True)`

- **Description**

  Lock or unlock trade

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
  <td style="text-align: left;">password</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Transaction password.
  
    
  
  
   
  
  If password_md5 is not empty, use the passed password_md5 to
  unlock.<br />
  Otherwise, MD5 calculated from password is used for password_md5 and
  then unlock.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">password_md5</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">32-bit MD5 encryption of transaction
  password (all lowercase).
  
    
  
  
   
  
  A password must be filled in to unlock a transaction, and a locked
  transaction is ignored.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">is_unlock</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Lock or unlock.
  
    
  
  
   
  
  True: unlock.<br />
  False: lock.
  
  
  
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
  <td rowspan="2">msg</td>
  <td>NoneType</td>
  <td>If ret == RET_OK, None is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from moomoo import *
pwd_unlock = '123456'
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.unlock_trade(pwd_unlock)
if ret == RET_OK:
    print('unlock success!')
else:
    print('unlock_trade failed: ', data)
trd_ctx.close()
```





- **Output**



``` python
unlock success!
```









## <a href="#661-2" class="header-anchor">#</a> Trd_UnlockTrade.proto

- **Description**

  Unlock or lock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2005





`uint UnlockTrade(TrdUnlockTrade.Request req);`  
`virtual void OnReply_UnlockTrade(MMAPI_Conn client, uint nSerialNo, TrdUnlockTrade.Response rsp);`

- **Description**

  Unlock or lock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: MMSPI_Trd, MMSPI_Conn {
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
        
        TrdUnlockTrade.C2S c2s = TrdUnlockTrade.C2S.CreateBuilder()
                .SetPwdMD5("e10adc3949ba59abbe56e057f20f883e")
                .SetUnlock(true)
                .SetSecurityFirm((int)TrdCommon.SecurityFirm.SecurityFirm_FutuSecurities)
                .Build();
        TrdUnlockTrade.Request req = TrdUnlockTrade.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.UnlockTrade(req);
        Console.Write("Send TrdUnlockTrade: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_UnlockTrade(MMAPI_Conn client, uint nSerialNo, TrdUnlockTrade.Response rsp)
    {
        Console.Write("Reply: TrdUnlockTrade: {0}\n", nSerialNo);
        Console.Write("retMsg: {0}\n", rsp.RetMsg);
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
Trd onInitConnect: ret=0 desc= connID=6826809697310867898
Send TrdUnlockTrade: 3
Reply: TrdUnlockTrade: 3
retMsg: 
```









`int unlockTrade(TrdUnlockTrade.Request req);`  
`void onReply_UnlockTrade(MMAPI_Conn client, int nSerialNo, TrdUnlockTrade.Response rsp);`

- **Description**

  Unlock or lock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;

    optional S2C s2c = 4;
}
```





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
        
        TrdUnlockTrade.C2S c2s = TrdUnlockTrade.C2S.newBuilder()
                .setPwdMD5("e10adc3949ba59abbe56e057f20f883e")
                .setUnlock(true)
                .setSecurityFirm(TrdCommon.SecurityFirm.SecurityFirm_FutuSecurities_VALUE)
                .build();
        TrdUnlockTrade.Request req = TrdUnlockTrade.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.unlockTrade(req);
        System.out.printf("Send TrdUnlockTrade: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_UnlockTrade(MMAPI_Conn client, int nSerialNo, TrdUnlockTrade.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdUnlockTrade failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdUnlockTrade: %s\n", json);
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
Send TrdUnlockTrade: 2
Receive TrdUnlockTrade: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0
}
```









`moomoo::u32_t UnlockTrade(const Trd_UnlockTrade::Request &stReq);`  
`virtual void OnReply_UnlockTrade(moomoo::u32_t nSerialNo, const Trd_UnlockTrade::Response &stRsp) = 0;`

- **Description**

  Lock or unlock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
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
        Trd_UnlockTrade::Request req;
        Trd_UnlockTrade::C2S *c2s = req.mutable_c2s();
        c2s->set_pwdmd5("e10adc3949ba59abbe56e057f20f883e");
        c2s->set_unlock(true);
        c2s->set_securityfirm(Trd_Common::SecurityFirm::SecurityFirm_FutuSecurities);

        m_UnlockTradeSerialNo = m_pTrdApi->UnlockTrade(req);
        cout << "Request UnlockTrade SerialNo: " << m_UnlockTradeSerialNo << endl;
    }

    virtual void OnReply_UnlockTrade(moomoo::u32_t nSerialNo, const Trd_UnlockTrade::Response &stRsp){
        if(nSerialNo == m_UnlockTradeSerialNo)
        {
            cout << "OnReply_UnlockTrade SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }
    
protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_UnlockTradeSerialNo;
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
Request UnlockTrade SerialNo: 4
OnReply_UnlockTrade SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0
}
```









`UnlockTrade(req);`

- **Description**

  Lock or unlock transaction

- **Parameters**



``` protobuf
message C2S
{
    required bool unlock = 1; //true to unlock the transaction, false to lock the transaction
    optional string pwdMD5 = 2; //32-bit MD5 encryption of transaction password (all lowercase). The password must be filled in to unlock the transaction, and the verification password is not required to lock the transaction.
    optional int32 securityFirm = 3; //Specified security firm, see Trd_Common.SecurityFirm
}

message Request
{
    required C2S c2s = 1;
}
```





> - For the security firm structure, refer to
>   [SecurityFirm](/moomoo-api-doc/en/trade/trade.html#9434)

- **Return**



``` protobuf
message S2C
{

}

message Response
{
    // The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
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
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdUnlockTrade(){
    const { RetType } = Common
    const { SecurityFirm } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    unlock: true,
                    securityFirm: SecurityFirm.SecurityFirm_FutuSecurities,
                    pwdMD5: "d0970714757783e6cf17b26fb8e2298f", // Set as the transaction password MD5 of your account
                },
            };
            websocket.UnlockTrade(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("UnlockTrade: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
UnlockTrade: errCode 0, retMsg , retType 0
null
stop
```











TIP

- When using live trading accounts, you need to **unlock trade**
  **before** calling *Place Order* or *Modify or Cancel Orders*
  interface, but when using paper trading accounts, you do not need to
  **unlock trade**.
- Locking or unlocking the transaction is an operation on OpenD. As long
  as one connection is unlocked, all other connections can call the
  transaction interface
- It is strongly recommended that customers who connect to OpenD via the
  external network for live trading use encrypted channels, refer to
  [Enable protocol encryption](/moomoo-api-doc/en/ftapi/init.html#7910)
- OpenAPI does not support moomoo token. If you have activated moomoo
  token, it will fail to unlock. You need to turn off the token and then
  use OpenAPI to unlock.





Interface Limitations

- A maximum of 10 requests per 30 seconds under a single user ID.













