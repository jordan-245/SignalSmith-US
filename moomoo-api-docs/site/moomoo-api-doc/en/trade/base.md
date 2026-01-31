



# <a href="#8155" class="header-anchor">#</a> Transaction Objects









- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#3490" class="header-anchor">#</a> Create the connection

`OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)`

`OpenFutureTradeContext(host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)`

- **Description**

  According to the transaction variaties, select a correct account, and
  create its transaction object.

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th style="text-align: left;">Transaction Objects</th>
  <th style="text-align: left;">Accounts</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="text-align: left;">OpenSecTradeContext</td>
  <td style="text-align: left;">Securities account
  
    
  
  
   
  
  Trading stocks, ETFs, warrants, stock options or index options uses this
  account.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">OpenFutureTradeContext</td>
  <td style="text-align: left;">Futures account
  
    
  
  
   
  
  Trading futures or future options uses this account.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

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
  <td style="text-align: left;">filter_trdmarket</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter accounts according to the
  transaction market authority.
  
    
  
  
   
  
  <ul>
  <li>This parameter is only available for OpenSecTradeContext.</li>
  <li>This parameter is only used to filter accounts and will not affect
  transaction connections.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">host</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">The IP listened by OpenD.</td>
  </tr>
  <tr>
  <td style="text-align: left;">port</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The port listened by OpenD.</td>
  </tr>
  <tr>
  <td style="text-align: left;">is_encrypt</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to enable encryption.
  
    
  
  
   
  
  Default None means: use the setting of <a
  href="/moomoo-api-doc/en/ftapi/init.html#7910">enable_proto_encrypt</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">security_firm</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#9434">SecurityFirm</a></td>
  <td style="text-align: left;">Specified security firm</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)
trd_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





## <a href="#1321" class="header-anchor">#</a> Close the connection

`close()`

- **Description**

  Close the trading object. By default, the threads created inside the
  Futu API will prevent the process from exiting, and the process can
  exit normally only after all Contexts are closed. But through
  [set_all_thread_daemon](/moomoo-api-doc/en/ftapi/init.html#5242), all
  internal threads can be set as daemon threads. At this time, even if
  close of Context is not called, the process can exit normally.

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111)
trd_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```









## <a href="#7613" class="header-anchor">#</a> InitConnect.proto

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
     //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, see the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
    optional string programmingLanguage = 6; //Interface programming language, used for statistical language preference
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
    required int32 serverVer = 1; //OpenD version number
    required uint64 loginUserID = 2; //OpenD login user ID
    required uint64 connID = 3; //The connection ID of this connection, the unique identifier of the connection
    required string connAESKey = 4; //The key for subsequent AES encrypted communication of this connection is fixed as a 16-byte long string
    required int32 keepAliveInterval = 5; //Heartbeat keepalive interval
    optional string aesCBCiv = 6; //The iv of AES encrypted communication CBC encryption mode is fixed as a 16-byte long string
}

message Response
{
    required int32 retType = 1 [default = -400]; //Returned result, see the enumeration definition of Common.RetType
    optional string retMsg = 2; //Description of returned result 
    optional int32 errCode = 3; //Error code. The client usually uses retType and retMsg to judge the results and details. ErrCode only logs and accounts only when individual protocols fail.
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  1001





## <a href="#1433" class="header-anchor">#</a> Create and initialize the connection

`bool InitConnect(String ip, short port, bool isEnableEncrypt)`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | ip             | str  | OpenD listening address.      |
  | port           | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Return**

  - ret: Whether the execution is started, it does not represent the
    connection result, and the result is called back through
    OnInitConnect

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1);  //Set client information
        trd.SetConnCallback(this);  //Set connection callback
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }
    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
    }
    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
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
Trd onInitConnect: ret=0 desc= connID=6826804060126078029
```





## <a href="#5637" class="header-anchor">#</a> Destroy the connection

`void Close()`

- **Description**

  Destroy connection

- **Example**



``` cs
FTAPI_Trd trd = new FTAPI_Trd();
trd.InitConnect("127.0.0.1", (ushort)11111, false);
trd.Close();
```









## <a href="#1433-2" class="header-anchor">#</a> Create and initialize the connection

`boolean initConnect(String ip, short port, boolean isEnableEncrypt)`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | ip             | str  | OpenD listening address.      |
  | port           | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Return**

  - ret: Whether to start execution. Does not represent the connection
    result, the result is called back through onInitConnect

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
    }

    public void start() throws IOException {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
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





## <a href="#5637-2" class="header-anchor">#</a> Destroy the connection

`void close()`

- **Description**

  Destroy connection

- **Example**



``` java
FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();
trd.initConnect("127.0.0.1", (short)11111, false);
trd.close();
```









## <a href="#1433-3" class="header-anchor">#</a> Create and initialize the connection

`FTAPI_Trd* CreateTrdApi();`
`bool InitConnect(const char* szIPAddr, Futu::u16_t nPort, bool bEnableEncrypt);`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | szIPAddr       | str  | OpenD listening address.      |
  | nPort          | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Example**



``` cpp
FTAPI_Trd *m_pTrdApi = FTAPI::CreateTrdApi();
m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
FTAPI::ReleaseTrdApi(m_pTrdApi);
```





## <a href="#5637-3" class="header-anchor">#</a> Destroy the connection

`void ReleaseTrdApi(FTAPI_Trd* pTrd);`

- **Description**

  Destroy connection

- **Return**

  - pTrd: Connection example

- **Example**



``` cpp
FTAPI_Trd *m_pTrdApi = FTAPI::CreateTrdApi();
m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
FTAPI::ReleaseTrdApi(m_pTrdApi);
```









## <a href="#1433-4" class="header-anchor">#</a> Create and initialize the connection

`start(ip, port, ssl, key)`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | ip | str | OpenD listening WebSocket address. |
  | port | int | OpenD listening WebSocket port. |
  | ssl | bool | Whether to enable SSL encryption, refer to [WebSocket related](/moomoo-api-doc/en/qa/other.html#5728). |
  | key | str | The connection private key, otherwise the connection will time out. The key is configurable in OpenD, and the visualization version will randomly specify one if the key is not specified. |

- **Example**



``` js
import ftWebSocket from "@/components/ft-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
    }
}
```





## <a href="#1321-2" class="header-anchor">#</a> Close the connection

`close()`

- **Description**

  Close the connection

- **Example**



``` js
import ftWebSocket from "@/components/ft-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.close();
    }
}
```

















- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#3490-2" class="header-anchor">#</a> Create the connection

`OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUINC)`

`OpenFutureTradeContext(host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUINC)`

- **Description**

  According to the transaction variaties, select a correct account, and
  create its transaction object.

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th style="text-align: left;">Transaction Objects</th>
  <th style="text-align: left;">Accounts</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td style="text-align: left;">OpenSecTradeContext</td>
  <td style="text-align: left;">Securities account
  
    
  
  
   
  
  Trading stocks, ETFs, warrants, stock options or index options uses this
  account.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">OpenFutureTradeContext</td>
  <td style="text-align: left;">Futures account
  
    
  
  
   
  
  Trading futures or future options uses this account.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

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
  <td style="text-align: left;">filter_trdmarket</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter accounts according to the
  transaction market authority.
  
    
  
  
   
  
  <ul>
  <li>This parameter is only available for OpenSecTradeContext.</li>
  <li>This parameter is only used to filter accounts and will not affect
  transaction connections.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">host</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">The IP listened by OpenD.</td>
  </tr>
  <tr>
  <td style="text-align: left;">port</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The port listened by OpenD.</td>
  </tr>
  <tr>
  <td style="text-align: left;">is_encrypt</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to enable encryption.
  
    
  
  
   
  
  Default None means: use the setting of <a
  href="/moomoo-api-doc/en/ftapi/init.html#7910">enable_proto_encrypt</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">security_firm</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#9434">SecurityFirm</a></td>
  <td style="text-align: left;">Specified security firm</td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUINC)
trd_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





## <a href="#1321-3" class="header-anchor">#</a> Close the connection

`close()`

- **Description**

  Close the trading object. By default, the threads created inside the
  moomoo API will prevent the process from exiting, and the process can
  exit normally only after all Contexts are closed. But through
  [set_all_thread_daemon](/moomoo-api-doc/en/ftapi/init.html#5242), all
  internal threads can be set as daemon threads. At this time, even if
  close of Context is not called, the process can exit normally.

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUINC)
trd_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```









## <a href="#7613-2" class="header-anchor">#</a> InitConnect.proto

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**



``` protobuf
message C2S
{
    required int32 clientVer = 1; //Client version number. clientVer = number before "." * 100 + number after ".". For example: clientVer = 1 * 100 + 1 = 101 for version 1.1 , and clientVer = 2 * 100 + 21 = 221 for version 2.21.
    required string clientID = 2; //The unique identifier for client, no specific generation rules, the client can guarantee the uniqueness
    optional bool recvNotify = 3; //Whether this connection receives notifications of market status or events that transaction needs to be re-unlocked. If True, OpenD will push these notifications to this connection, otherwise false means not receiving or pushing
    //If the communication is to be encrypted, you must first configure the RSA key in both OpenD and the client. If it is not configured, it will not be encrypted.
     //It will be encrypted if the RSA key is configured and the specified encryption algorithm is not PacketEncAlgo_None. (Even if it is not set here and the RSA key is configured, the default encryption method will be used), and the FTAES_ECB algorithm is used by default
    optional int32 packetEncAlgo = 4; //Specify the packet encryption algorithm, see the enumeration definition of Common.PacketEncAlgo
    optional int32 pushProtoFmt = 5; //Specify the push protocol format on this connection, if not specified, use the push_proto_type configuration item
    optional string programmingLanguage = 6; //Interface programming language, used for statistical language preference
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
    required int32 serverVer = 1; //OpenD version number
    required uint64 loginUserID = 2; //OpenD login user ID
    required uint64 connID = 3; //The connection ID of this connection, the unique identifier of the connection
    required string connAESKey = 4; //The key for subsequent AES encrypted communication of this connection is fixed as a 16-byte long string
    required int32 keepAliveInterval = 5; //Heartbeat keepalive interval
    optional string aesCBCiv = 6; //The iv of AES encrypted communication CBC encryption mode is fixed as a 16-byte long string
}

message Response
{
    required int32 retType = 1 [default = -400]; //Returned result, see the enumeration definition of Common.RetType
    optional string retMsg = 2; //Description of returned result 
    optional int32 errCode = 3; //Error code. The client usually uses retType and retMsg to judge the results and details. ErrCode only logs and accounts only when individual protocols fail.
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  1001





## <a href="#1433-5" class="header-anchor">#</a> Create and initialize the connection

`bool InitConnect(String ip, short port, bool isEnableEncrypt)`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | ip             | str  | OpenD listening address.      |
  | port           | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Return**

  - ret: Whether the execution is started, it does not represent the
    connection result, and the result is called back through
    OnInitConnect

- **Example**



``` cs
public class Program : MMSPI_Trd, MMSPI_Conn {
    MMAPI_Trd trd = new MMAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1);  //Set client information
        trd.SetConnCallback(this);  //Set connection callback
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }
    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
    }
    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
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
Trd onInitConnect: ret=0 desc= connID=6826804060126078029
```





## <a href="#5637-4" class="header-anchor">#</a> Destroy the connection

`void Close()`

- **Description**

  Destroy connection

- **Example**



``` cs
MMAPI_Trd trd = new MMAPI_Trd();
trd.InitConnect("127.0.0.1", (ushort)11111, false);
trd.Close();
```









## <a href="#1433-6" class="header-anchor">#</a> Create and initialize the connection

`boolean initConnect(String ip, short port, boolean isEnableEncrypt)`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | ip             | str  | OpenD listening address.      |
  | port           | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Return**

  - ret: Whether to start execution. Does not represent the connection
    result, the result is called back through onInitConnect

- **Example**



``` java
public class TrdDemo implements MMSPI_Trd, MMSPI_Conn {
    MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
    }

    public void start() throws IOException {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    public static void main(String[] args) throws IOException {
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





## <a href="#5637-5" class="header-anchor">#</a> Destroy the connection

`void close()`

- **Description**

  Destroy connection

- **Example**



``` java
MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();
trd.initConnect("127.0.0.1", (short)11111, false);
trd.close();
```









## <a href="#1433-7" class="header-anchor">#</a> Create and initialize the connection

`MMAPI_Trd* CreateTrdApi();`
`bool InitConnect(const char* szIPAddr, moomoo::u16_t nPort, bool bEnableEncrypt);`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | szIPAddr       | str  | OpenD listening address.      |
  | nPort          | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Example**



``` cpp
MMAPI_Trd *m_pTrdApi = MMAPI::CreateTrdApi();
m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
MMAPI::ReleaseTrdApi(m_pTrdApi);
```





## <a href="#5637-6" class="header-anchor">#</a> Destroy the connection

`void ReleaseTrdApi(MMAPI_Trd* pTrd);`

- **Description**

  Destroy connection

- **Return**

  - pTrd: Connection example

- **Example**



``` cpp
MMAPI_Trd *m_pTrdApi = MMAPI::CreateTrdApi();
m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
MMAPI::ReleaseTrdApi(m_pTrdApi);
```









## <a href="#1433-8" class="header-anchor">#</a> Create and initialize the connection

`start(ip, port, ssl, key)`

- **Description**

  Create transaction object and initialize transaction connection

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | ip | str | OpenD listening WebSocket address. |
  | port | int | OpenD listening WebSocket port. |
  | ssl | bool | Whether to enable SSL encryption, refer to [WebSocket related](/moomoo-api-doc/en/qa/other.html#5728). |
  | key | str | The connection private key, otherwise the connection will time out. The key is configurable in OpenD, and the visualization version will randomly specify one if the key is not specified. |

- **Example**



``` js
import mmWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new mmWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
    }
}
```





## <a href="#1321-4" class="header-anchor">#</a> Close the connection

`close()`

- **Description**

  Close the connection

- **Example**



``` js
import mmWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new mmWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.close();
    }
}
```



















