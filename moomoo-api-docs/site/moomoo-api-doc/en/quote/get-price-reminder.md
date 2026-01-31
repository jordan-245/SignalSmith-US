



# <a href="#2726" class="header-anchor">#</a> Get Price Reminder List









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_price_reminder(code=None, market=None)`

- **Description**

  Get a list of price reminders set for the specified stock or market

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
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Specified stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Specified market type.
  
    
  
  
   
  
  Note that either Shanghai or Shenzhen will be regarded as the A-share
  market.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  Note: Choose either code or market, and code takes precedence if both
  exist.

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
  <td>If ret == RET_OK, price reminder data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Price reminder data format as follows:
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
    <td style="text-align: left;">key</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Identification, used to modify the price
    reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3793">PriceReminderType</a></td>
    <td style="text-align: left;">The type of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_freq</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9918">PriceReminderFreq</a></td>
    <td style="text-align: left;">The frequency of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Remind value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">enable</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether to enable.</td>
    </tr>
    <tr>
    <td style="text-align: left;">note</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Note.
    
      
    
    
     
    
    Note supports no more than 20 Chinese characters.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_session_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Price reminder session list for US stocks
    
      
    
    
     
    
    The parameter type in list is <a
    href="/moomoo-api-doc/en/quote/quote.html#6578">PriceReminderMarketStatus</a>.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_price_reminder(code='US.AAPL')
if ret == RET_OK:
    print(data)
    print(data['key'].values.tolist())   # Convert to list
else:
    print('error:', data)
print('******************************************')
ret, data = quote_ctx.get_price_reminder(code=None, market=Market.US)
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the price remind list is not empty
        print(data['code'][0])    # Take the first stock code
        print(data['code'].values.tolist())   # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
code name                  key   reminder_type reminder_freq   value  enable note                   reminder_session_list
0  US.AAPL   APPLE  1744021708234288125    BID_PRICE_UP        ALWAYS  184.37    True  456                              [US_AFTER]
1  US.AAPL   APPLE  1744022257052794489    BID_PRICE_UP        ALWAYS  185.50    True  456  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
2  US.AAPL   APPLE  1744021708211891867  ASK_PRICE_DOWN        ALWAYS  182.54    True  123                              [US_AFTER]
3  US.AAPL   APPLE  1744022257023211123  ASK_PRICE_DOWN        ALWAYS  183.70    True  123  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
[1744021708234288125, 1744022257052794489, 1744021708211891867, 1744022257023211123]
******************************************
      code name                  key   reminder_type reminder_freq   value  enable note                   reminder_session_list
0  US.AAPL   APPLE  1744021708234288125    BID_PRICE_UP        ALWAYS  184.37    True  456                              [US_AFTER]
1  US.AAPL   APPLE  1744022257052794489    BID_PRICE_UP        ALWAYS  185.50    True  456  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
2  US.AAPL   APPLE  1744021708211891867  ASK_PRICE_DOWN        ALWAYS  182.54    True  123                              [US_AFTER]
3  US.AAPL   APPLE  1744022257023211123  ASK_PRICE_DOWN        ALWAYS  183.70    True  123  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
4  US.NVDA  NVIDIA  1739697581665326308      PRICE_DOWN        ALWAYS  102.00    True       [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
US.AAPL
['US.AAPL', 'US.AAPL', 'US.AAPL', 'US.AAPL', 'US.NVDA']
```









## <a href="#9077" class="header-anchor">#</a> Qot_GetPriceReminder.proto

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3221





`uint GetPriceReminder(QotGetPriceReminder.Request req);`  
`virtual void OnReply_GetPriceReminder(FTAPI_Conn client, uint nSerialNo, QotGetPriceReminder.Response rsp);`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
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
                .SetCode("00700")
                .Build();
        QotGetPriceReminder.C2S c2s = QotGetPriceReminder.C2S.CreateBuilder()
                .SetSecurity(sec)
            .Build();
        QotGetPriceReminder.Request req = QotGetPriceReminder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetPriceReminder(req);
        Console.Write("Send QotGetPriceReminder: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetPriceReminder(FTAPI_Conn client, uint nSerialNo, QotGetPriceReminder.Response rsp)
    {
        Console.Write("Reply: QotGetPriceReminder: {0}  {1}\n", nSerialNo, rsp.ToString());
        if(rsp.S2C.PriceReminderListCount > 0)
        {
            Console.Write("key: {0} \n", rsp.S2C.PriceReminderListList[0].ItemListList[0].Key);
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
Reply: QotGetPriceReminder: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  priceReminderList {
    security {
      market: 1
      code: "00700"
    }
    itemList {
      key: 162763183755472101
      type: 1
      value: 5
      note: ""
      freq: 3
      isEnable: true
    }
    itemList {
      key: 162763177551063501
      type: 1
      value: 5
      note: ""
      freq: 3
      isEnable: true
    }
  }
}

key: 162763183755472101
```









`int getPriceReminder(QotGetPriceReminder.Request req);`  
`void onReply_GetPriceReminder(FTAPI_Conn client, int nSerialNo, QotGetPriceReminder.Response rsp);`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
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
                .setCode("00700")
                .build();
        QotGetPriceReminder.C2S c2s = QotGetPriceReminder.C2S.newBuilder()
                .setSecurity(sec)
            .build();
        QotGetPriceReminder.Request req = QotGetPriceReminder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getPriceReminder(req);
        System.out.printf("Send QotGetPriceReminder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPriceReminder(FTAPI_Conn client, int nSerialNo, QotGetPriceReminder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetPriceReminder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetPriceReminder: %s\n", json);
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
Send QotGetPriceReminder: 2
Receive QotGetPriceReminder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "priceReminderList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "itemList": [{
        "key": "162452649832682701",
        "type": 1,
        "value": 5.0,
        "note": "",
        "freq": 3,
        "isEnable": true
      }]
    }]
  }
}
```









`Futu::u32_t GetPriceReminder(const Qot_GetPriceReminder::Request &stReq);`  
`virtual void OnReply_GetPriceReminder(Futu::u32_t nSerialNo, const Qot_GetPriceReminder::Response &stRsp) = 0;`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
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
        Qot_GetPriceReminder::Request req;
        Qot_GetPriceReminder::C2S *c2s = req.mutable_c2s();
        c2s->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetPriceReminderSerialNo = m_pQotApi->GetPriceReminder(req);
        cout << "Request GetPriceReminder SerialNo: " << m_GetPriceReminderSerialNo << endl;
    }

    virtual void OnReply_GetPriceReminder(Futu::u32_t nSerialNo, const Qot_GetPriceReminder::Response &stRsp){
        if(nSerialNo == m_GetPriceReminderSerialNo)
        {
            cout << "OnReply_GetPriceReminder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetPriceReminderSerialNo;
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
Request GetPriceReminder SerialNo: 4
OnReply_GetPriceReminder SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "priceReminderList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "itemList": [
     {
      "key": "162320791658522901",
      "type": 1,
      "value": 5,
      "note": "",
      "freq": 3,
      "isEnable": true
     }
    ]
   }
  ]
 }
}
```









`GetPriceReminder(req);`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetPriceReminder(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security: {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                },
            };
            
            websocket.GetPriceReminder(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("PriceReminder: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
PriceReminder: errCode 0, retMsg , retType 0
{
  "priceReminderList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "itemList": [{
      "key": "163126377342664201",
      "type": 1,
      "value": 600,
      "note": "",
      "freq": 1,
      "isEnable": true
    }]
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





`get_price_reminder(code=None, market=None)`

- **Description**

  Get a list of price reminders set for the specified stock or market

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
  <td style="text-align: left;">code</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Specified stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Specified market type.
  
    
  
  
   
  
  Note that either Shanghai or Shenzhen will be regarded as the A-share
  market.
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  Note: Choose either code or market, and code takes precedence if both
  exist.

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
  <td>If ret == RET_OK, price reminder data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Price reminder data format as follows:
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
    <td style="text-align: left;">key</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Identification, used to modify the price
    reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3793">PriceReminderType</a></td>
    <td style="text-align: left;">The type of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_freq</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#9918">PriceReminderFreq</a></td>
    <td style="text-align: left;">The frequency of price reminder.</td>
    </tr>
    <tr>
    <td style="text-align: left;">value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Remind value.</td>
    </tr>
    <tr>
    <td style="text-align: left;">enable</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether to enable.</td>
    </tr>
    <tr>
    <td style="text-align: left;">note</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Note.
    
      
    
    
     
    
    Note supports no more than 20 Chinese characters.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">reminder_session_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Price reminder session list for US stocks
    
      
    
    
     
    
    The parameter type in list is <a
    href="/moomoo-api-doc/en/quote/quote.html#6578">PriceReminderMarketStatus</a>.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_price_reminder(code='US.AAPL')
if ret == RET_OK:
    print(data)
    print(data['key'].values.tolist())   # Convert to list
else:
    print('error:', data)
print('******************************************')
ret, data = quote_ctx.get_price_reminder(code=None, market=Market.US)
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the price remind list is not empty
        print(data['code'][0])    # Take the first stock code
        print(data['code'].values.tolist())   # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
code name                  key   reminder_type reminder_freq   value  enable note                   reminder_session_list
0  US.AAPL   APPLE  1744021708234288125    BID_PRICE_UP        ALWAYS  184.37    True  456                              [US_AFTER]
1  US.AAPL   APPLE  1744022257052794489    BID_PRICE_UP        ALWAYS  185.50    True  456  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
2  US.AAPL   APPLE  1744021708211891867  ASK_PRICE_DOWN        ALWAYS  182.54    True  123                              [US_AFTER]
3  US.AAPL   APPLE  1744022257023211123  ASK_PRICE_DOWN        ALWAYS  183.70    True  123  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
[1744021708234288125, 1744022257052794489, 1744021708211891867, 1744022257023211123]
******************************************
      code name                  key   reminder_type reminder_freq   value  enable note                   reminder_session_list
0  US.AAPL   APPLE  1744021708234288125    BID_PRICE_UP        ALWAYS  184.37    True  456                              [US_AFTER]
1  US.AAPL   APPLE  1744022257052794489    BID_PRICE_UP        ALWAYS  185.50    True  456  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
2  US.AAPL   APPLE  1744021708211891867  ASK_PRICE_DOWN        ALWAYS  182.54    True  123                              [US_AFTER]
3  US.AAPL   APPLE  1744022257023211123  ASK_PRICE_DOWN        ALWAYS  183.70    True  123  [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
4  US.NVDA  NVIDIA  1739697581665326308      PRICE_DOWN        ALWAYS  102.00    True       [OPEN, US_PRE, US_AFTER, US_OVERNIGHT]
US.AAPL
['US.AAPL', 'US.AAPL', 'US.AAPL', 'US.AAPL', 'US.NVDA']
```









## <a href="#9077-2" class="header-anchor">#</a> Qot_GetPriceReminder.proto

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3221





`uint GetPriceReminder(QotGetPriceReminder.Request req);`  
`virtual void OnReply_GetPriceReminder(MMAPI_Conn client, uint nSerialNo, QotGetPriceReminder.Response rsp);`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
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
                .SetCode("00700")
                .Build();
        QotGetPriceReminder.C2S c2s = QotGetPriceReminder.C2S.CreateBuilder()
                .SetSecurity(sec)
            .Build();
        QotGetPriceReminder.Request req = QotGetPriceReminder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetPriceReminder(req);
        Console.Write("Send QotGetPriceReminder: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetPriceReminder(MMAPI_Conn client, uint nSerialNo, QotGetPriceReminder.Response rsp)
    {
        Console.Write("Reply: QotGetPriceReminder: {0}  {1}\n", nSerialNo, rsp.ToString());
        if(rsp.S2C.PriceReminderListCount > 0)
        {
            Console.Write("key: {0} \n", rsp.S2C.PriceReminderListList[0].ItemListList[0].Key);
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
Reply: QotGetPriceReminder: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  priceReminderList {
    security {
      market: 1
      code: "00700"
    }
    itemList {
      key: 162763183755472101
      type: 1
      value: 5
      note: ""
      freq: 3
      isEnable: true
    }
    itemList {
      key: 162763177551063501
      type: 1
      value: 5
      note: ""
      freq: 3
      isEnable: true
    }
  }
}

key: 162763183755472101
```









`int getPriceReminder(QotGetPriceReminder.Request req);`  
`void onReply_GetPriceReminder(MMAPI_Conn client, int nSerialNo, QotGetPriceReminder.Response rsp);`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
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
                .setCode("00700")
                .build();
        QotGetPriceReminder.C2S c2s = QotGetPriceReminder.C2S.newBuilder()
                .setSecurity(sec)
            .build();
        QotGetPriceReminder.Request req = QotGetPriceReminder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getPriceReminder(req);
        System.out.printf("Send QotGetPriceReminder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPriceReminder(MMAPI_Conn client, int nSerialNo, QotGetPriceReminder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetPriceReminder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetPriceReminder: %s\n", json);
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
Send QotGetPriceReminder: 2
Receive QotGetPriceReminder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "priceReminderList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "itemList": [{
        "key": "162452649832682701",
        "type": 1,
        "value": 5.0,
        "note": "",
        "freq": 3,
        "isEnable": true
      }]
    }]
  }
}
```









`moomoo::u32_t GetPriceReminder(const Qot_GetPriceReminder::Request &stReq);`  
`virtual void OnReply_GetPriceReminder(moomoo::u32_t nSerialNo, const Qot_GetPriceReminder::Response &stRsp) = 0;`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
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
        Qot_GetPriceReminder::Request req;
        Qot_GetPriceReminder::C2S *c2s = req.mutable_c2s();
        c2s->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetPriceReminderSerialNo = m_pQotApi->GetPriceReminder(req);
        cout << "Request GetPriceReminder SerialNo: " << m_GetPriceReminderSerialNo << endl;
    }

    virtual void OnReply_GetPriceReminder(moomoo::u32_t nSerialNo, const Qot_GetPriceReminder::Response &stRsp){
        if(nSerialNo == m_GetPriceReminderSerialNo)
        {
            cout << "OnReply_GetPriceReminder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetPriceReminderSerialNo;
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
Request GetPriceReminder SerialNo: 4
OnReply_GetPriceReminder SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "priceReminderList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "itemList": [
     {
      "key": "162320791658522901",
      "type": 1,
      "value": 5,
      "note": "",
      "freq": 3,
      "isEnable": true
     }
    ]
   }
  ]
 }
}
```









`GetPriceReminder(req);`

- **Description**

  Get a list of price reminders set for the specified stock or market

- **Parameters**



``` protobuf
message C2S
{
    //Choose one of security and market, and security will take precedence if both exist.
    optional Qot_Common.Security security = 1; //Specified security
    optional int32 market = 2; //Qot_Common::QotMarket. Specified market, query the price reminder items under the market, does not distinguish between Shanghai and Shenzhen
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market types, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// List of reminders
message PriceReminderItem
{
    required int64 key = 1; //The unique identifier of each reminder
    required int32 type = 2; //Qot_Common::PriceReminderType, reminder type
    required double value = 3; //Reminder parameter value
    required string note = 4; //Note supports no more than 20 Chinese characters
    required int32 freq = 5; //Qot_Common::PriceReminderFreq, reminder frequency type
    required bool isEnable = 6; //Does the reminder setting take effect. False does not take effect, True takes effect
}

message PriceReminder
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; // stock name
    repeated PriceReminderItem itemList = 2; //List of reminder information
}

message S2C
{
    repeated PriceReminder priceReminderList = 1; //Price reminder
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
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetPriceReminder(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security: {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                },
            };
            
            websocket.GetPriceReminder(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("PriceReminder: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
PriceReminder: errCode 0, retMsg , retType 0
{
  "priceReminderList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "itemList": [{
      "key": "163126377342664201",
      "type": 1,
      "value": 600,
      "note": "",
      "freq": 1,
      "isEnable": true
    }]
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds













