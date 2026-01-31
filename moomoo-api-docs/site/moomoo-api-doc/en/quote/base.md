



# <a href="#2335" class="header-anchor">#</a> Quote Object









- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#1433" class="header-anchor">#</a> Create and Initialize the Connection

`OpenQuoteContext(host='127.0.0.1', port=11111, is_encrypt=None)`

- **Introduction**

  Create and initialize market connection

- **Parameters**

Parameter\|Type\|Description 😐:-\|:- host\|str\|OpenD listening
address. port\|int\|OpenD listening port. is_encrypt\|bool\|Whether to
enable encryption.









 



- The default is None, which means the setting of
  [enable_proto_encrypt](/moomoo-api-doc/en/ftapi/init.html#7910) is
  used.
- True: mandatory encryption.  
  False: mandatory no encryption.









- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111, is_encrypt=False)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





## <a href="#8837" class="header-anchor">#</a> Close Connection

`close()`

- **Introduction**

Close the interface quotation object. By default, the threads created
inside the Futu API will prevent the process from exiting, and the
process can exit normally only after all Contexts are closed. But
through
[set_all_thread_daemon](/moomoo-api-doc/en/ftapi/init.html#5242), all
internal threads can be set as daemon threads. At this time, even if the
close of Context is not called, the process can exit normally.

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





## <a href="#6929" class="header-anchor">#</a> Start-up

`start()`

- **Introduction**

  Start to receive push data asynchronously

## <a href="#1109" class="header-anchor">#</a> Stop

`stop()`

- **Introduction**

  Stop receiving push data asynchronously





## <a href="#7613" class="header-anchor">#</a> InitConnect.proto

- **Introduction**

  Initialize the connection protocol

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





## <a href="#1433-2" class="header-anchor">#</a> Create and Initialize the Connection

`bool InitConnect(String ip, short port, bool isEnableEncrypt)`

- **Introduction**

  Initialize connection, connect and initialize

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
public class Program : FTSPI_Qot, FTSPI_Conn {
    FTAPI_Qot qot = new FTAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
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
Qot onInitConnect: ret=0 desc= connID=6825319780708742248
```





## <a href="#5913" class="header-anchor">#</a> Destroy Connection

`void Close()`

- **Introduction**

  Destroy connection

- **Example**



``` cs
FTAPI_Qot qot = new FTAPI_Qot();
qot.InitConnect("127.0.0.1", (ushort)11111, false);
qot.Close();
```









## <a href="#1433-3" class="header-anchor">#</a> Create and Initialize the Connection

`boolean initConnect(String ip, short port, boolean isEnableEncrypt)`

- **Introduction**

  Initialize connection, connect and initialize

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | ip             | str  | OpenD listening address.      |
  | port           | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Return**

  - ret: Whether the execution is started, it does not represent the
    connection result, and the result is called back through
    onInitConnect

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
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





## <a href="#5637" class="header-anchor">#</a> Destroy the Connection

`void close()`

- **Introduction**

  Destroy connection

- **Example**



``` java
FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();
qot.initConnect("127.0.0.1", (short)11111, false);
qot.close();
```









## <a href="#1433-4" class="header-anchor">#</a> Create and Initialize the Connection

`FTAPI_Qot* CreateQotApi();`  
`bool InitConnect(const char* szIPAddr, Futu::u16_t nPort, bool bEnableEncrypt);`

- **Introduction**

  Create, initialize connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | szIPAddr       | str  | OpenD listening address.      |
  | nPort          | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Example**



``` cpp
FTAPI_Qot *m_pQotApi = FTAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
FTAPI::ReleaseQotApi(m_pQotApi);
```





## <a href="#5637-2" class="header-anchor">#</a> Destroy the Connection

`void ReleaseTrdApi(FTAPI_Qot* pTrd);`

- **Introduction**

  Destroy connection

- **Return**

  - pQot: connection example

- **Example**



``` cpp
FTAPI_Qot *m_pQotApi = FTAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
FTAPI::ReleaseQotApi(m_pQotApi);
```









## <a href="#1433-5" class="header-anchor">#</a> Create and Initialize the Connection

`start(ip, port, ssl, key)`

- **Introduction**

  Initialize connection, connect and initialize

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





## <a href="#8837-2" class="header-anchor">#</a> Close Connection

`close()`

- **Introduction**

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





## <a href="#1433-6" class="header-anchor">#</a> Create and Initialize the Connection

`OpenQuoteContext(host='127.0.0.1', port=11111, is_encrypt=None)`

- **Introduction**

  Create and initialize market connection

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
  <td style="text-align: left;">host</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">OpenD listening address.</td>
  </tr>
  <tr>
  <td style="text-align: left;">port</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">OpenD listening port.</td>
  </tr>
  <tr>
  <td style="text-align: left;">is_encrypt</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to enable encryption.
  
    
  
  
   
  
  <ul>
  <li>The default is None, which means the setting of <a
  href="/moomoo-api-doc/en/ftapi/init.html#7910">enable_proto_encrypt</a>
  is used.</li>
  <li>True: mandatory encryption.<br />
  False: mandatory no encryption.</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111, is_encrypt=False)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





## <a href="#8837-3" class="header-anchor">#</a> Close Connection

`close()`

- **Introduction**

Close the interface quotation object. By default, the threads created
inside the moomoo API will prevent the process from exiting, and the
process can exit normally only after all Contexts are closed. But
through
[set_all_thread_daemon](/moomoo-api-doc/en/ftapi/init.html#5242), all
internal threads can be set as daemon threads. At this time, even if the
close of Context is not called, the process can exit normally.

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





## <a href="#6929-2" class="header-anchor">#</a> Start-up

`start()`

- **Introduction**

  Start to receive push data asynchronously

## <a href="#1109-2" class="header-anchor">#</a> Stop

`stop()`

- **Introduction**

  Stop receiving push data asynchronously





## <a href="#7613-2" class="header-anchor">#</a> InitConnect.proto

- **Introduction**

  Initialize the connection protocol

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





## <a href="#1433-7" class="header-anchor">#</a> Create and Initialize the Connection

`bool InitConnect(String ip, short port, bool isEnableEncrypt)`

- **Introduction**

  Initialize connection, connect and initialize

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
public class Program : MMSPI_Qot, MMSPI_Conn {
    MMAPI_Qot qot = new MMAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1); //Set client information
        qot.SetConnCallback(this); //Set connection callback
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
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
Qot onInitConnect: ret=0 desc= connID=6825319780708742248
```





## <a href="#5913-2" class="header-anchor">#</a> Destroy Connection

`void Close()`

- **Introduction**

  Destroy connection

- **Example**



``` cs
MMAPI_Qot qot = new FTAPI_Qot();
qot.InitConnect("127.0.0.1", (ushort)11111, false);
qot.Close();
```









## <a href="#1433-8" class="header-anchor">#</a> Create and Initialize the Connection

`boolean initConnect(String ip, short port, boolean isEnableEncrypt)`

- **Introduction**

  Initialize connection, connect and initialize

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | ip             | str  | OpenD listening address.      |
  | port           | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Return**

  - ret: Whether the execution is started, it does not represent the
    connection result, and the result is called back through
    onInitConnect

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1); //Set client information
        qot.setConnSpi(this); //Set connection callback
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





## <a href="#5637-3" class="header-anchor">#</a> Destroy the Connection

`void close()`

- **Introduction**

  Destroy connection

- **Example**



``` java
MMAPI_Conn_Qot qot = new FTAPI_Conn_Qot();
qot.initConnect("127.0.0.1", (short)11111, false);
qot.close();
```









## <a href="#1433-9" class="header-anchor">#</a> Create and Initialize the Connection

`MMAPI_Qot* CreateQotApi();`  
`bool InitConnect(const char* szIPAddr, moomoo::u16_t nPort, bool bEnableEncrypt);`

- **Introduction**

  Create, initialize connection

- **Parameters**

  | Parameter      | Type | Description                   |
  |:---------------|:-----|:------------------------------|
  | szIPAddr       | str  | OpenD listening address.      |
  | nPort          | int  | OpenD listening port.         |
  | bEnableEncrypt | bool | Whether to enable encryption. |

- **Example**



``` cpp
MMAPI_Qot *m_pQotApi = MMAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
MMAPI::ReleaseQotApi(m_pQotApi);
```





## <a href="#5637-4" class="header-anchor">#</a> Destroy the Connection

`void ReleaseTrdApi(FTAPI_Qot* pTrd);`

- **Introduction**

  Destroy connection

- **Return**

  - pQot: connection example

- **Example**



``` cpp
MMAPI_Qot *m_pQotApi = MMAPI::CreateQotApi();
m_pQotApi->InitConnect("127.0.0.1", 11111, false);
MMAPI::ReleaseQotApi(m_pQotApi);
```









## <a href="#1433-10" class="header-anchor">#</a> Create and Initialize the Connection

`start(ip, port, ssl, key)`

- **Introduction**

  Initialize connection, connect and initialize

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | ip | str | OpenD listening WebSocket address. |
  | port | int | OpenD listening WebSocket port. |
  | ssl | bool | Whether to enable SSL encryption, refer to [WebSocket related](/moomoo-api-doc/en/qa/other.html#5728). |
  | key | str | The connection private key, otherwise the connection will time out. The key is configurable in OpenD, and the visualization version will randomly specify one if the key is not specified. |

- **Example**



``` js
import ftWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
    }
}
```





## <a href="#8837-4" class="header-anchor">#</a> Close Connection

`close()`

- **Introduction**

  Close the connection

- **Example**



``` js
import ftWebSocket from "@/components/mm-websocket/main.js";
class Example {
    example() {
        this.websocket = new ftWebSocket();
        this.websocket.start("127.0.0.1", 33333, false, null);
        this.websocket.close();
    }
}
```



















