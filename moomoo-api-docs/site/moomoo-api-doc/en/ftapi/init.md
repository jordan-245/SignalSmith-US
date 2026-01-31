



# <a href="#2007" class="header-anchor">#</a> Basic Functions





- Python
- Proto
- C#
- Java
- C++
- JavaScript









| Protocol ID | Protobuf File | Description |
|:---|:---|:---|
| 1001 | [InitConnect](/moomoo-api-doc/en/quote/base.html) | Connection Initializationaa |
| 1002 | [GetGlobalState](/moomoo-api-doc/en/quote/get-global-state.html) | Get Global Status |
| 1003 | [Notify](/moomoo-api-doc/en/ftapi/init.html#787) | Event Notification Callback |
| 1004 | [KeepAlive](/moomoo-api-doc/en/ftapi/protocol.html#7390) | Heartbeat Keep Alive |





















## <a href="#7621" class="header-anchor">#</a> Set Interface Information(deprecated)





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_client_info(client_id, client_ver)`

- **Introduction**

  Set calling interface information (unnecessary).

- **Parameters**

  - client_id: the identification of the client
  - client_ver: the version number of the client





- **Example**



``` python
from futu import *
SysConfig.set_client_info("MyFutuAPI", 0)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```











``` python
from moomoo import *
SysConfig.set_client_info("MymoomooAPI", 0)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```

















InitConnect.proto



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
    //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, refer to the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
}
```









InitConnect.proto



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
    //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, refer to the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
}
```









- **Introduction**

  Set the clientVer and clientID fields in the initial connection
  protocol.





`void SetClientInfo(String clientID, int clientVer);`

- **Introduction**

  Set calling interface information, unnecessary interface

- **Parameters**

  - clientID: the identification of the client
  - clientVer: the version number of the client







``` cs
FTAPI_Qot qot = new FTAPI_Qot();
qot.SetClientInfo("FTAPI4NET_Sample", 1); //Set client information
```











``` cs
MMAPI_Qot qot = new MMAPI_Qot();
qot.SetClientInfo("MMAPI4NET_Sample", 1); //Set client information
```









- **Example**





`void setClientInfo(String clientID, int clientVer);`

- **Introduction**

  Set calling interface information, unnecessary interface

- **Parameters**

  - clientID: the identification of the client
  - clientVer: the version number of the client





- **Example**



``` java
FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();
qot.setClientInfo("javaclient", 1); //Set client information
```









- **Example**



``` java
MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();
qot.setClientInfo("javaclient", 1); //Set client information
```













`void SetClientInfo(const char* szClientID, moomoo::i32_t nClientVer);`

- **Introduction**

  Set calling interface information, unnecessary interface

- **Parameters**

  - szClientID: the identification of the client
  - nClientVer: client version number





- **Example**



``` cpp
FTAPI_Qot *m_pQotApi = FTAPI::CreateQotApi();
m_pQotApi->SetClientInfo('cpp', 1);
FTAPI::ReleaseQotApi(m_pQotApi);
```









- **Example**



``` cpp
MMAPI_Qot *m_pQotApi = MMAPI::CreateQotApi();
m_pQotApi->SetClientInfo('cpp', 1);
MMAPI::ReleaseQotApi(m_pQotApi);
```

















## <a href="#6650" class="header-anchor">#</a> Set Protocol Format





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_proto_fmt(proto_fmt)`

- **Introduction**

  Set the communication protocol body format, Protobuf and Json formats
  are currently supported , default ProtoBuf, unnecessary interface

- **Parameters**

  - proto_fmt: protocol format, refer to
    [ProtoFMT](/moomoo-api-doc/en/ftapi/common.html#4358)





- **Example**



``` python
from futu import *
SysConfig.set_proto_fmt(ProtoFMT.Protobuf)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```









- **Example**



``` python
from moomoo import *
SysConfig.set_proto_fmt(ProtoFMT.Protobuf)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```

















InitConnect.proto



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
    //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, refer to the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
}
```









InitConnect.proto



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
    //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, refer to the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
}
```









- **Introduction**

  The pushProtoFmt field in the initial connection protocol specifies
  the format of the data pushed on the connection. For the request data
  format, please refer to the nProtoFmtType field in [Protocol
  header](/moomoo-api-doc/en/ftapi/protocol.html#218).





















## <a href="#7910" class="header-anchor">#</a> Set Protocol Encryption Globally





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`Enable_proto_encrypt(is_encrypt)`

- **Introduction** Setting protocol encryption can help users protect
  their requests and returned contents globally. For more information
  about Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  | Parameter  | Type | Description               |
  |:-----------|:-----|:--------------------------|
  | is_encrypt | bool | Enable encryption or not. |





- **Example**



``` python
from futu import *
SysConfig.enable_proto_encrypt(True)
SysConfig.set_init_rsa_file("conn_key.txt")   # rsa private key file path
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```









- **Example**



``` python
from moomoo import *
SysConfig.enable_proto_encrypt(True)
SysConfig.set_init_rsa_file("conn_key.txt")   # rsa private key file path
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```





























`start(ip, port, ssl, key)`

- **Introduction**

  Initialize connection, connect and initialize





- **Parameters**

  - ip: WebSocket address listened by OpenD
  - port: the WebSocket port listened by OpenD
  - ssl: Whether to enable SSL encryption, refer to [WebSocket
    related](/moomoo-api-doc/en/qa/other.html#5728)
  - key: The private key of the connection. If it is not set, a
    connection timeout may occur. The key is configurable in OpenD, and
    the private key of Visualization OpenD will be randomly specified if
    it is not set.

- **Example**



``` js
import ftWebSocket from "@/components/ft-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, true, '123456');
    }
}
```









- **Parameters**

  - ip: WebSocket address listened by OpenD
  - port: the WebSocket port listened by OpenD
  - ssl: Whether to enable SSL encryption, refer to [WebSocket
    related](/moomoo-api-doc/en/qa/other.html#5728)
  - key: The private key of the connection. If it is not set, a
    connection timeout may occur. The key is configurable in OpenD, and
    the private key of Visualization OpenD will be randomly specified if
    it is not set.

- **Example**



``` js
import mmWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, true, '123456');
    }
}
```













## <a href="#6187" class="header-anchor">#</a> Set the Path of Private Key





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_init_rsa_file(file)`





- **Introduction**

  Set the Path of Private Key in Futu API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  | Parameter | Type | Description            |
  |:----------|:-----|:-----------------------|
  | file      | str  | Private key file path. |

- **Example**



``` python
from futu import *
SysConfig.enable_proto_encrypt(True)
SysConfig.set_init_rsa_file("conn_key.txt")   # rsa private key file path
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```









- **Introduction**

  Set the Path of Private Key in moomoo API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  | Parameter | Type | Description            |
  |:----------|:-----|:-----------------------|
  | file      | str  | Private key file path. |

- **Example**



``` python
from moomoo import *
SysConfig.enable_proto_encrypt(True)
SysConfig.set_init_rsa_file("conn_key.txt")   # rsa private key file path
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close()
```

















InitConnect.proto



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
    //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, refer to the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
}
```









InitConnect.proto



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
    //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, refer to the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
}
```









- **Introduction**

  The packetEncAlgo field in the initialization connection protocol
  specifies the encryption algorithm of the connection. For details of
  protocol encryption, refer to [Encrypted Communication
  Process](/moomoo-api-doc/en/ftapi/protocol.html#4573).





`void SetRSAPrivateKey(string key)`





- **Introduction**

  Set the Path of Private Key in Futu API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  - key: private key content

- **Example**



``` cs
public class Program : FTSPI_Qot, FTSPI_Conn {
    FTAPI_Qot qot = new FTAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
        qot.SetQotCallback(this); //Set transaction callback
        qot.SetRSAPrivateKey(System.IO.File.ReadAllText(@"d:\rsa1024", Encoding.UTF8)); //Set rsa key
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, true); //Connection encryption
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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_Basic)
                .SetIsSubOrUnSub(true)
                .Build();
        QotSub.Request req = QotSub.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.Sub(req);
        Console.Write("Send QotSub: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_Sub(FTAPI_Conn client, uint nSerialNo, QotSub.Response rsp) {
        Console.Write("Reply: QotSub: {0}  {1}\n", nSerialNo, rsp.ToString());
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









- **Introduction**

  Set the Path of Private Key in moomoo API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  - key: private key content

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn {
    MMAPI_Qot qot = new MMAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
        qot.SetQotCallback(this); //Set transaction callback
        qot.SetRSAPrivateKey(System.IO.File.ReadAllText(@"d:\rsa1024", Encoding.UTF8)); //Set rsa key
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, true); //Connection encryption
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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_Basic)
                .SetIsSubOrUnSub(true)
                .Build();
        QotSub.Request req = QotSub.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.Sub(req);
        Console.Write("Send QotSub: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_Sub(MMAPI_Conn client, uint nSerialNo, QotSub.Response rsp) {
        Console.Write("Reply: QotSub: {0}  {1}\n", nSerialNo, rsp.ToString());
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
Qot onInitConnect: ret=0 desc= connID=6827935070720340213
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0
```









`void setRSAPrivateKey(String key)`





- **Introduction**

  Set the Path of Private Key in Futu API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  - key: private key content

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
    }

    public void start() throws IOException {
        String rsaKey = "";
        byte[] buf = java.nio.file.Files.readAllBytes(Paths.get("c:\\rsa1024"));
        rsaKey = new String(buf, Charset.forName("UTF-8"));
        qot.setRSAPrivateKey(rsaKey);
    }

    public static void main(String[] args) throws IOException {
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









- **Introduction**

  Set the Path of Private Key in moomoo API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  - key: private key content

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
    }

    public void start() throws IOException {
        String rsaKey = "";
        byte[] buf = java.nio.file.Files.readAllBytes(Paths.get("c:\\rsa1024"));
        rsaKey = new String(buf, Charset.forName("UTF-8"));
        qot.setRSAPrivateKey(rsaKey);
    }

    public static void main(String[] args) throws IOException {
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













`void SetRSAPrivateKey(const char* szRSAPrivateKey);`





- **Introduction**

  Set the Path of Private Key in Futu API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  - strRSAPrivateKey: private key content

- **Example**



``` cpp
string strKey;
ifstream file("key");
file >> strKey;
file.close();
FTAPI_Qot *m_pQotApi = FTAPI::CreateQotApi();
m_pQotApi->SetRSAPrivateKey(strKey.c_str());
m_pQotApi->InitConnect("127.0.0.1", 11111, true);
FTAPI::ReleaseQotApi(m_pQotApi);
```









- **Introduction**

  Set the Path of Private Key in moomoo API. For more information about
  Protocol Encryption Process, please check
  [here](/moomoo-api-doc/en/qa/other.html#1479).

- **Parameters**

  - strRSAPrivateKey: private key content

- **Example**



``` cpp
string strKey;
ifstream file("key");
file >> strKey;
file.close();
MMAPI_Qot *m_pQotApi = MMAPI::CreateQotApi();
m_pQotApi->SetRSAPrivateKey(strKey.c_str());
m_pQotApi->InitConnect("127.0.0.1", 11111, true);
MMAPI::ReleaseQotApi(m_pQotApi);
```













`start(ip, port, ssl, key)`

- **Introduction**

  Initialize connection, connect and initialize





- **Parameters**

  - ip: WebSocket address listened by OpenD
  - port: the WebSocket port listened by OpenD
  - ssl: Whether to enable SSL encryption, refer to [WebSocket
    related](/moomoo-api-doc/en/qa/other.html#5728)
  - key: The private key of the connection. If it is not set, a
    connection timeout may occur. The key is configurable in OpenD, and
    the Visualization OpenD will be randomly assigned if it is not
    specified.

- **Example**



``` js
import ftWebSocket from "@/components/ft-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, true, '123456');
    }
}
```









- **Parameters**

  - ip: WebSocket address listened by OpenD
  - port: the WebSocket port listened by OpenD
  - ssl: Whether to enable SSL encryption, refer to [WebSocket
    related](/moomoo-api-doc/en/qa/other.html#5728)
  - key: The private key of the connection. If it is not set, a
    connection timeout may occur. The key is configurable in OpenD, and
    the Visualization OpenD will be randomly assigned if it is not
    specified.

- **Example**



``` js
import ftWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new mmWebSocket();
        this.websocket.start("127.0.0.1", 33333, true, '123456');
    }
}
```













## <a href="#5242" class="header-anchor">#</a> Set Thread Mode





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_all_thread_daemon(all_daemon)`

- **Introduction** Whether to set all internally threads to be daemon
  threads.

  - If it is set to be daemon threads, then after the main thread exits,
    the process also exits.  
    For example, when using the real-time callback API, you need to make
    sure the main thread survives by yourself. Otherwise, when the main
    thread exits, the process also exits and you will no longer receive
    the push data.
  - If it is set to a non-daemon thread, the process will not exit after
    the main thread exits. For example, if you do not call close() to
    close the connection after creating a quote or trade object, the
    process will not exit even if the main thread exits.

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
  <td style="text-align: left;">all_daemon</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to set threads to be daemon
  threads.
  
    
  
  
   
  
  <ul>
  <li>True：set to daemon threads</li>
  <li>False：set to non-daemon threads</li>
  <li>Default is False</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>





- **Example**



``` python
from futu import *
SysConfig.set_all_thread_daemon(True)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
# the process will exit without calling quote_ctx.close(), 
```









- **Example**



``` python
from moomoo import *
SysConfig.set_all_thread_daemon(True)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
# the process will exit without calling quote_ctx.close(), 
```

































## <a href="#8418" class="header-anchor">#</a> Set Callback





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_handler(handler)`

- **Introduction**

  Set asynchronous callback processing object





- **Parameters**

  - handler: callback processing object
    | Class | Description |
    |:---|:---|
    | SysNotifyHandlerBase | [OpenD notification processing base class](/moomoo-api-doc/en/ftapi/init.html#787) |
    | StockQuoteHandlerBase | [Quote processing base class](/moomoo-api-doc/en/quote/update-stock-quote.html) |
    | OrderBookHandlerBase | [Order book processing base class](/moomoo-api-doc/en/quote/update-order-book.html) |
    | CurKlineHandlerBase | [Real-time candlestick processing base class](/moomoo-api-doc/en/quote/update-kl.html) |
    | TickerHandlerBase | [Tick-By-Tick processing base class](/moomoo-api-doc/en/quote/update-ticker.html) |
    | RTDataHandlerBase | [Time Frame data processing base class](/moomoo-api-doc/en/quote/update-rt.html) |
    | BrokerHandlerBase | [Broker queue processing base class](/moomoo-api-doc/en/quote/update-broker.html) |
    | PriceReminderHandlerBase | [Price reminder processing base class](/moomoo-api-doc/en/quote/update-price-reminder.html) |
    | TradeOrderHandlerBase | [Order processing base class](/moomoo-api-doc/en/trade/update-order.html) |
    | TradeDealHandlerBase | [Order fill processing base class](/moomoo-api-doc/en/trade/update-order-fill.html) |

- **Example**



``` python
import time
from futu import *
class OrderBookTest(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s" % data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBookTest()
quote_ctx.set_handler(handler) # Setting real-time order book callback
quote_ctx.subscribe(['HK.00700'], [SubType.ORDER_BOOK]) # Subscribe to the order book type, OpenD starts to receive pushed data from the server continuously
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the subscription of the corresponding stock in 1 minute
```









- **Parameters**

  - handler: callback processing object
    | Class | Description |
    |:---|:---|
    | SysNotifyHandlerBase | [OpenD notification processing base class](/moomoo-api-doc/en/ftapi/init.html#787) |
    | StockQuoteHandlerBase | [Quote processing base class](/moomoo-api-doc/en/quote/update-stock-quote.html) |
    | OrderBookHandlerBase | [Order book processing base class](/moomoo-api-doc/en/quote/update-order-book.html) |
    | CurKlineHandlerBase | [Real-time candlestick processing base class](/moomoo-api-doc/en/quote/update-kl.html) |
    | TickerHandlerBase | [Tick-By-Tick processing base class](/moomoo-api-doc/en/quote/update-ticker.html) |
    | RTDataHandlerBase | [Time Frame data processing base class](/moomoo-api-doc/en/quote/update-rt.html) |
    | BrokerHandlerBase | [Broker queue processing base class](/moomoo-api-doc/en/quote/update-broker.html) |
    | PriceReminderHandlerBase | [Price reminder processing base class](/moomoo-api-doc/en/quote/update-price-reminder.html) |
    | TradeOrderHandlerBase | [Order processing base class](/moomoo-api-doc/en/trade/update-order.html) |
    | TradeDealHandlerBase | [Order fill processing base class](/moomoo-api-doc/en/trade/update-order-fill.html) |

- **Example**



``` python
import time
from moomoo import *
class OrderBookTest(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBookTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s" % data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBookTest()
quote_ctx.set_handler(handler) # Setting real-time order book callback
quote_ctx.subscribe(['HK.00700'], [SubType.ORDER_BOOK]) # Subscribe to the order book type, OpenD starts to receive pushed data from the server continuously
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the subscription of the corresponding stock in 1 minute
```





















`void SetConnCallback(FTSPI_Conn connCallback)`  
`void SetQotCallback(FTSPI_Qot callback)`  
`void SetTrdCallback(FTSPI_Trd callback)`

- **Introduction**

  Callback setting

- **Parameters**

  - callback: callback function

- **Example**



``` cs
public class Program: FTSPI_Qot, FTSPI_Conn
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
            qot.InitConnect("127.0.0.1", (ushort)11111, false); //Connection encryption
        }


        public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
        {
            Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
            if (errCode != 0)
                return;
        }


        public void OnDisconnect(FTAPI_Conn client, long errCode)
        {
            Console.Write("Qot onDisConnect: {0}\n", errCode);
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









`void SetConnCallback(MMSPI_Conn connCallback)`  
`void SetQotCallback(MMSPI_Qot callback)`  
`void SetTrdCallback(MMSPI_Trd callback)`

- **Introduction**

  Callback setting

- **Parameters**

  - callback: callback function

- **Example**



``` cs
public class Program: MMSPI_Qot, MMSPI_Conn
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
            qot.InitConnect("127.0.0.1", (ushort)11111, false); //Connection encryption
        }


        public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
        {
            Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
            if (errCode != 0)
                return;
        }


        public void OnDisconnect(MMAPI_Conn client, long errCode)
        {
            Console.Write("Qot onDisConnect: {0}\n", errCode);
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
Qot onInitConnect: ret=0 desc= connID=6827937191858660334
```













`setConnSpi(FTSPI_Conn callback);`  
`void setQotSpi(FTSPI_Qot callback);`  
`void setTrdSpi(FTSPI_Trd callback);`

- **Introduction**

  Callback setting

- **Parameters**

  - callback: callback function

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
        qot.setQotSpi(this); //Set the market callback
    }

    public void start() throws IOException {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
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













`setConnSpi(MMSPI_Conn callback);`  
`void setQotSpi(MMSPI_Qot callback);`  
`void setTrdSpi(MMSPI_Trd callback);`

- **Introduction**

  Callback setting

- **Parameters**

  - callback: callback function

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
        qot.setQotSpi(this); //Set the market callback
    }

    public void start() throws IOException {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
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













`void RegisterConnSpi(FTSPI_Qot* pSpi);`  
`void RegisterQotSpi(FTSPI_Qot* pSpi);`  
`void RegisterTrdSpi(FTSPI_Qot* pSpi);`

- **Introduction**

  Callback setting

- **Parameters**

  - pSpi: callback function

- **Example**



``` cpp
FTAPI_Qot *m_pQotApi = FTAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
m_pQotApi->RegisterQotSpi(this);
m_pQotApi->RegisterConnSpi(this);
FTAPI::ReleaseQotApi(m_pQotApi);
```









`void RegisterConnSpi(MMSPI_Qot* pSpi);`  
`void RegisterQotSpi(MMSPI_Qot* pSpi);`  
`void RegisterTrdSpi(MMSPI_Qot* pSpi);`

- **Introduction**

  Callback setting

- **Parameters**

  - pSpi: callback function

- **Example**



``` cpp
MMAPI_Qot *m_pQotApi = MMAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
m_pQotApi->RegisterQotSpi(this);
m_pQotApi->RegisterConnSpi(this);
MMAPI::ReleaseQotApi(m_pQotApi);
```













`onPush(cmd, res)`  
`onlogin(ret, msg)`

- **Introduction**

  Login callback and push callback

- **Return**

  - cmd: Pushed protocol ID
  - res: Pushed agreement content
  - ret: whether the initialization is successful
  - msg: failure description





- **Example**



``` js
import ftWebSocket from "@/components/ft-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.onPush = this.onPush.bind(this);
        this.websocket.onlogin = this.onLogin.bind(this);
    },
    onPush(cmd, res) {
    const obj = ftWebSocket.findCmdObj(cmd);
        if (obj && obj.description) {
            console.log(res);
        }
    },
    onLogin(ret, msg) {
        if (ret) {
            console.log(this.websocket.getConnID());
        }
    }
}
```









- **Example**



``` js
import mmWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new mmWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.onPush = this.onPush.bind(this);
        this.websocket.onlogin = this.onLogin.bind(this);
    },
    onPush(cmd, res) {
    const obj = ftWebSocket.findCmdObj(cmd);
        if (obj && obj.description) {
            console.log(res);
        }
    },
    onLogin(ret, msg) {
        if (ret) {
            console.log(this.websocket.getConnID());
        }
    }
}
```













## <a href="#7571" class="header-anchor">#</a> Get Connection ID





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_sync_conn_id()`

- **Introduction**

  Get the connection ID, the value will be available after the
  connection is successfully initialized

- **Return**

  - conn_id: connection ID





- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.get_sync_conn_id()
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```









- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.get_sync_conn_id()
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```













InitConnect.proto







``` protobuf
message S2C
{
    required int32 serverVer = 1; //OpenD version number
    required uint64 loginUserID = 2; //OpenD login user ID
    required uint64 connID = 3; //The connection ID of this connection, the unique identifier of the connection
    required string connAESKey = 4; //The key for subsequent AES encrypted communication of this connection is fixed as a 16-byte long string
    required int32 keepAliveInterval = 5; //Heartbeat keepalive interval
    optional string aesCBCiv = 6; //The iv of AES encrypted communication CBC encryption mode is fixed as a 16-byte long string
}
```











``` protobuf
message S2C
{
    required int32 serverVer = 1; //OpenD version number
    required uint64 loginUserID = 2; //OpenD login user ID
    required uint64 connID = 3; //The connection ID of this connection, the unique identifier of the connection
    required string connAESKey = 4; //The key for subsequent AES encrypted communication of this connection is fixed as a 16-byte long string
    required int32 keepAliveInterval = 5; //Heartbeat keepalive interval
    optional string aesCBCiv = 6; //The iv of AES encrypted communication CBC encryption mode is fixed as a 16-byte long string
}
```









- **Introduction**

  The connID field in the InitConnect protocol return packet





`uint GetConnectID();`

- **Introduction**

  Get the connection ID, the value will be available after the
  connection is successfully initialized

- **Return**

  - connID: connection ID





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
            qot.InitConnect("127.0.0.1", (ushort)11111, false); //Connection encryption
        }


        public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
        {
            Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
            if (errCode != 0)
                return;
        }


        public void OnDisconnect(FTAPI_Conn client, long errCode)
        {
            Console.Write("Qot onDisConnect: {0}\n", errCode);
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
            qot.InitConnect("127.0.0.1", (ushort)11111, false); //Connection encryption
        }


        public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
        {
            Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
            if (errCode != 0)
                return;
        }


        public void OnDisconnect(MMAPI_Conn client, long errCode)
        {
            Console.Write("Qot onDisConnect: {0}\n", errCode);
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
Qot onInitConnect: ret=0 desc= connID=6827937791149892052
```









`long getConnectID();`

- **Introduction**

  Get the connection ID, the value will be available after the
  connection is successfully initialized

- **Return**

  - connID: connection ID





- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
        qot.setQotSpi(this); //Set the market callback
    }

    public void start() throws IOException {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
        FTAPI.init();
        QotDemo qot = new QotDemo();
        qot.start();

        while (true) {
            try {
                Thread.sleep(1000 * 60);
            } catch (InterruptedException exc) {

            }
        }
    }
}
```









- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
        qot.setQotSpi(this); //Set the market callback
    }

    public void start() throws IOException {
        qot.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Qot onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
        MMAPI.init();
        QotDemo qot = new QotDemo();
        qot.start();

        while (true) {
            try {
                Thread.sleep(1000 * 60);
            } catch (InterruptedException exc) {

            }
        }
    }
}
```

















`Futu::u64_t GetConnectID()`

- **Introduction**

  Get the connection ID, the value will be available after the
  connection is successfully initialized

- **Return**

  - nConnID: Connection ID

- **Example**



``` cpp
FTAPI_Qot *m_pQotApi = FTAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
m_pQotApi->GetConnectID();
FTAPI::ReleaseQotApi(m_pQotApi);
```









`moomoo::u64_t GetConnectID()`

- **Introduction**

  Get the connection ID, the value will be available after the
  connection is successfully initialized

- **Return**

  - nConnID: Connection ID

- **Example**



``` cpp
MMAPI_Qot *m_pQotApi = MMAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
m_pQotApi->GetConnectID();
MMAPI::ReleaseQotApi(m_pQotApi);
```













`getConnID()`

- **Introduction**

  Get the connection ID, the value will be available after the
  connection is successfully initialized

- **Return**

  - connID: connection ID





- **Example**



``` js
import ftWebSocket from "@/components/ft-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.onlogin = this.onLogin.bind(this);
    },
    onLogin(ret, msg) {
    if (ret) {
        this.websocket.getConnID();
    }
}
```









- **Example**



``` js
import mmWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new mmWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.onlogin = this.onLogin.bind(this);
    },
    onLogin(ret, msg) {
    if (ret) {
        this.websocket.getConnID();
    }
}
```













## <a href="#787" class="header-anchor">#</a> Event Notification Callback





- Python
- Proto
- C#
- Java
- C++
- JavaScript





`SysNotifyHandlerBase`





- **Introduction**

  Notify OpenD of some important news, such as disconnection, etc.





- **Introduction**

  Notify OpenD of some important news, such as disconnection, etc.





- **Protocol ID**

  1003

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
  <td>int</td>
  <td>Returned value. On success, ret == RET_OK. On error, ret !=
  RET_OK.</td>
  </tr>
  <tr>
  <td rowspan="2">data</td>
  <td>tuple</td>
  <td>If ret == RET_OK, <strong>event notification data</strong> is
  returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - The format of **event notification** data is as follows:

    Field









