



# <a href="#306" class="header-anchor">#</a> Price Reminder Callback









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  The price reminder notification callback, asynchronously handles the
  notification push that has been set to the price reminder. After
  receiving the real-time price notification, it will call back to this
  function. You need to override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdatePriceReminder_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
  <td>dict</td>
  <td>If ret == RET_OK, price reminder is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Price reminder format as follows:
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
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Current price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">change_rate</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Current change rate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6578">PriceReminderMarketStatus</a></td>
    <td style="text-align: left;">The time period for triggering.</td>
    </tr>
    <tr>
    <td style="text-align: left;">content</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Text content of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">note</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Note.
    
      
    
    
     
    
    Note supports no more than 20 Chinese characters.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">key</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Price reminder identification.</td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3793">PriceReminderType</a></td>
    <td style="text-align: left;">The type of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">set_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The reminder value set by the user.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The value when the reminder was
    triggered.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
import time
from futu import *

class PriceReminderTest(PriceReminderHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, content = super(PriceReminderTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("PriceReminderTest: error, msg: %s" % content)
            return RET_ERROR, content
        print("PriceReminderTest ", content) # PriceReminderTest's own processing logic
        return RET_OK, content
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = PriceReminderTest()
quote_ctx.set_handler(handler) # Set price reminder notification callback
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
PriceReminderTest  {'code': 'US.AAPL', 'name': 'APPLE', 'price': 185.750, 'change_rate': 0.11, 'market_status': 'US_PRE', 'content': '买一价高于185.500', 'note': '', 'key': 1744022257052794489, 'reminder_type': 'BID_PRICE_UP', 'set_value': 185.500, 'cur_value': 185.750}
```









## <a href="#3227" class="header-anchor">#</a> Qot_UpdatePriceReminder.proto

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3019





`virtual void OnReply_UpdatePriceReminder(FTAPI_Conn client, uint nSerialNo, QotUpdatePriceReminder.Response rsp);`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
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
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }
    
    public void OnReply_UpdatePriceReminder(FTAPI_Conn client, uint nSerialNo, QotUpdatePriceReminder.Response rsp)
    {
        Console.Write("Reply: QotUpdatePriceReminder: {0}\n", nSerialNo);
        Console.Write("code: {0}, content: {1}\n", rsp.S2C.Security.Code, rsp.S2C.Content);
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
Qot onInitConnect: ret=0 desc= connID=6826796032557005979
Reply: QotUpdatePriceReminder: 4
code: VXmain, content: Price rose to20.650
```









`void onPush_UpdatePriceReminder(FTAPI_Conn client, int nSerialNo, QotUpdatePriceReminder.Response rsp);`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
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
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onPush_UpdatePriceReminder(FTAPI_Conn client, QotUpdatePriceReminder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdatePriceReminder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdatePriceReminder: %s\n", json);
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
Receive QotUpdatePriceReminder: {
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 604,
  "changeRate": 0.499,
  "marketStatus": 1,
  "content": "Price rises to 604.000",
  "note": "",
  "key": "162321935858611601",
  "type": 1,
  "setValue": 604,
  "curValue": 604
 }
}
Receive QotUpdatePriceReminder: {
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 603.5,
  "changeRate": 0.415,
  "marketStatus": 1,
  "content": "Price falls under 603.990",
  "note": "",
  "key": "162320791658522901",
  "type": 2,
  "setValue": 603.99,
  "curValue": 603.5
 }
}
```









`virtual void OnPush_UpdatePriceReminder(const Qot_UpdatePriceReminder::Response &stRsp) = 0;`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
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

    }

    virtual void OnPush_UpdatePriceReminder(const Qot_UpdatePriceReminder::Response &stRsp) {
        cout << "OnPush_UpdatePriceReminder: " << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    FTAPI_Qot *m_pQotApi;
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
OnPush_UpdatePriceReminder:
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 604,
  "changeRate": 0.499,
  "marketStatus": 1,
  "content": "Price rises to 604.000",
  "note": "",
  "key": "162321935858611601",
  "type": 1,
  "setValue": 604,
  "curValue": 604
 }
}

OnPush_UpdatePriceReminder:
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 603.5,
  "changeRate": 0.415,
  "marketStatus": 1,
  "content": "Price falls under 603.990",
  "note": "",
  "key": "162320791658522901",
  "type": 2,
  "setValue": 603.99,
  "curValue": 603.5
 }
}
```









`OnPush(cmd,res)`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotUpdatePriceReminder(){
    const { RetType } = Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ec16fde057a2e7a0'];
    let websocket = new ftWebsocket();
    
    // Need a set price reminder

    websocket.onPush = (cmd, res)=>{
        if(ftCmdID.QotUpdatePriceReminder.cmd == cmd){ // PriceReminderTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                let data = beautify(JSON.stringify(s2c), {
                    indent_size: 2,
                    space_in_empty_paren: true,
                });
                console.log("PriceReminderTest:");
                console.log(data);
            } else {
                console.log("PriceReminderTest: error")
            }
        }
    };

    websocket.start(addr, port, enable_ssl, key);

    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 3600 * 1000); // Set the script to receive OpenD push duration to 3600 seconds
```





- **Output**



``` javascript
PriceReminderTest:
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "price": 482.8,
  "changeRate": 1.004,
  "marketStatus": 1,
  "content": "Daily rises more than 1.000%",
  "note": "",
  "key": "163126377342664201",
  "type": 3,
  "setValue": 1,
  "curValue": 1.004
}
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Price Reminder
  List](/moomoo-api-doc/en/quote/get-price-reminder.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505) API.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  The price reminder notification callback, asynchronously handles the
  notification push that has been set to the price reminder. After
  receiving the real-time price notification, it will call back to this
  function. You need to override on_recv_rsp in the derived class.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Qot_UpdatePriceReminder_pb2.Response | This parameter does not need to be processed directly in the derived class. |

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
  <td>dict</td>
  <td>If ret == RET_OK, price reminder is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Price reminder format as follows:
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
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Current price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">change_rate</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Current change rate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">market_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6578">PriceReminderMarketStatus</a></td>
    <td style="text-align: left;">The time period for triggering.</td>
    </tr>
    <tr>
    <td style="text-align: left;">content</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Text content of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">note</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Note.
    
      
    
    
     
    
    Note supports no more than 20 Chinese characters.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">key</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Price reminder identification.</td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3793">PriceReminderType</a></td>
    <td style="text-align: left;">The type of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">set_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The reminder value set by the user.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The value when the reminder was
    triggered.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
import time
from moomoo import *

class PriceReminderTest(PriceReminderHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, content = super(PriceReminderTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("PriceReminderTest: error, msg: %s" % content)
            return RET_ERROR, content
        print("PriceReminderTest ", content) # PriceReminderTest's own processing logic
        return RET_OK, content
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = PriceReminderTest()
quote_ctx.set_handler(handler) # Set price reminder notification callback
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
PriceReminderTest  {'code': 'US.AAPL', 'name': 'APPLE', 'price': 185.750, 'change_rate': 0.11, 'market_status': 'US_PRE', 'content': '买一价高于185.500', 'note': '', 'key': 1744022257052794489, 'reminder_type': 'BID_PRICE_UP', 'set_value': 185.500, 'cur_value': 185.750}
```









## <a href="#3227-2" class="header-anchor">#</a> Qot_UpdatePriceReminder.proto

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3019





`virtual void OnReply_UpdatePriceReminder(MMAPI_Conn client, uint nSerialNo, QotUpdatePriceReminder.Response rsp);`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
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
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }
    
    public void OnReply_UpdatePriceReminder(MMAPI_Conn client, uint nSerialNo, QotUpdatePriceReminder.Response rsp)
    {
        Console.Write("Reply: QotUpdatePriceReminder: {0}\n", nSerialNo);
        Console.Write("code: {0}, content: {1}\n", rsp.S2C.Security.Code, rsp.S2C.Content);
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
Qot onInitConnect: ret=0 desc= connID=6826796032557005979
Reply: QotUpdatePriceReminder: 4
code: VXmain, content: Price rose to20.650
```









`void onPush_UpdatePriceReminder(MMAPI_Conn client, int nSerialNo, QotUpdatePriceReminder.Response rsp);`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
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
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onPush_UpdatePriceReminder(MMAPI_Conn client, QotUpdatePriceReminder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotUpdatePriceReminder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotUpdatePriceReminder: %s\n", json);
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
Receive QotUpdatePriceReminder: {
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 604,
  "changeRate": 0.499,
  "marketStatus": 1,
  "content": "Price rises to 604.000",
  "note": "",
  "key": "162321935858611601",
  "type": 1,
  "setValue": 604,
  "curValue": 604
 }
}
Receive QotUpdatePriceReminder: {
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 603.5,
  "changeRate": 0.415,
  "marketStatus": 1,
  "content": "Price falls under 603.990",
  "note": "",
  "key": "162320791658522901",
  "type": 2,
  "setValue": 603.99,
  "curValue": 603.5
 }
}
```









`virtual void OnPush_UpdatePriceReminder(const Qot_UpdatePriceReminder::Response &stRsp) = 0;`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
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

    }

    virtual void OnPush_UpdatePriceReminder(const Qot_UpdatePriceReminder::Response &stRsp) {
        cout << "OnPush_UpdatePriceReminder: " << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    MMAPI_Qot *m_pQotApi;
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
OnPush_UpdatePriceReminder:
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 604,
  "changeRate": 0.499,
  "marketStatus": 1,
  "content": "Price rises to 604.000",
  "note": "",
  "key": "162321935858611601",
  "type": 1,
  "setValue": 604,
  "curValue": 604
 }
}

OnPush_UpdatePriceReminder:
{
 "retType": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "price": 603.5,
  "changeRate": 0.415,
  "marketStatus": 1,
  "content": "Price falls under 603.990",
  "note": "",
  "key": "162320791658522901",
  "type": 2,
  "setValue": 603.99,
  "curValue": 603.5
 }
}
```









`OnPush(cmd,res)`

- **Description**

  Price alert notification callback, asynchronously process notification
  pushes that have been set to price alert.

- **Parameters**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Trading session
    MarketStatus_USPre = 2; //US stocks pre-market
    MarketStatus_USAfter = 3; //US stocks after-hours
    MarketStatus_USOverNight = 4; //US stocks overnight
}

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 11; // Stock name
    required double price = 2; //Price
    required double changeRate = 3; //Price change rate today
    required int32 marketStatus = 4; //Qot_Common::MarketStatus. Market status
    required string content = 5; //Content
    required string note = 6; //Note supports no more than 20 Chinese characters
    optional int64 key = 7; //Identification of the price reminder
    optional int32 type = 8; //Qot_Common::PriceReminderType, reminder frequency type
    optional double setValue = 9; //Set reminder value
    optional double curValue = 10; //Current value when the set reminder type is triggered
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotUpdatePriceReminder(){
    const { RetType } = Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ec16fde057a2e7a0'];
    let websocket = new mmWebsocket();
    
    // Need a set price reminder

    websocket.onPush = (cmd, res)=>{
        if(mmCmdID.QotUpdatePriceReminder.cmd == cmd){ // PriceReminderTest's own processing logic
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                let data = beautify(JSON.stringify(s2c), {
                    indent_size: 2,
                    space_in_empty_paren: true,
                });
                console.log("PriceReminderTest:");
                console.log(data);
            } else {
                console.log("PriceReminderTest: error")
            }
        }
    };

    websocket.start(addr, port, enable_ssl, key);

    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 3600 * 1000); // Set the script to receive OpenD push duration to 3600 seconds
```





- **Output**



``` javascript
PriceReminderTest:
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "price": 482.8,
  "changeRate": 1.004,
  "marketStatus": 1,
  "content": "Daily rises more than 1.000%",
  "note": "",
  "key": "163126377342664201",
  "type": 3,
  "setValue": 1,
  "curValue": 1.004
}
stop
```











Tips

- This interface provides the function of continuously obtaining pushed
  data. If you need to obtain real-time data at one time, please refer
  to the [Get Price Reminder
  List](/moomoo-api-doc/en/quote/get-price-reminder.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505) API.













