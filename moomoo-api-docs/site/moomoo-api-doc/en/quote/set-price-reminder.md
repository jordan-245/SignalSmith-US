



# <a href="#1847" class="header-anchor">#</a> Set Price Reminder









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_price_reminder(code, op, key=None, reminder_type=None, reminder_freq=None, value=None, note=None, reminder_session_list=NONE)`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

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
  <td style="text-align: left;">Stock code</td>
  </tr>
  <tr>
  <td style="text-align: left;">op</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8810">SetPriceReminderOp</a></td>
  <td style="text-align: left;">Operation type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">key</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Identification, do not need to fill in the
  case of adding all or deleting all.</td>
  </tr>
  <tr>
  <td style="text-align: left;">reminder_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#3793">PriceReminderType</a></td>
  <td style="text-align: left;">The type of price reminder, this input
  parameter will be ignored when delete, enable, or disable.</td>
  </tr>
  <tr>
  <td style="text-align: left;">reminder_freq</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9918">PriceReminderFreq</a></td>
  <td style="text-align: left;">The frequency of price reminder, this
  input parameter will be ignored when delete, enabled, or disable.</td>
  </tr>
  <tr>
  <td style="text-align: left;">value</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Reminder value, the input parameter will
  be ignored when delete, enable, or disable.
  
    
  
  
   
  
  3 decimal place accuracy, the excess part is discarded.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">note</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">The note set by the user, note supports no
  more than 20 Chinese characters, the input parameter will be ignored
  when delete, enable, or disable.</td>
  </tr>
  <tr>
  <td style="text-align: left;">reminder_session_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">The session for US stocks price reminder,
  this input parameter will be ignored when delete, enable, or disable.
  
    
  
  
   
  
  <ul>
  <li>The parameter type in list is <a
  href="/moomoo-api-doc/en/quote/quote.html#6578">PriceReminderMarketStatus</a>.</li>
  <li>The default price reminder session for US stocks is
  pre/post+RTH.</li>
  </ul>
  
  
  
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
  <td rowspan="2">key</td>
  <td>int</td>
  <td>If ret == RET_OK, The price reminder key of the operation is
  returned. When deleting all reminders of a specific stock, 0 is
  returned.</td>
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
import time
class PriceReminderTest(PriceReminderHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, content = super(PriceReminderTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("PriceReminderTest: error, msg: %s" % content)
            return RET_ERROR, content
        print("PriceReminderTest ", content)
        return RET_OK, content
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = PriceReminderTest()
quote_ctx.set_handler(handler)
ret, data = quote_ctx.get_market_snapshot(['US.AAPL'])
if ret == RET_OK:
    bid_price = data['bid_price'][0] # Get real-time bid price
    ask_price = data['ask_price'][0] # Get real-time selling price
    # Set a reminder for AAPL(24H) when the selling price is lower than (ask_price-1)
    ret_ask, ask_data = quote_ctx.set_price_reminder(code='US.AAPL', op=SetPriceReminderOp.ADD, key=None, reminder_type=PriceReminderTypeASK_PRICE_DOWN, reminder_freq=PriceReminderFreq.ALWAYS, value=(ask_price-1), note='123', reminder_session_list=[PriceReminderMarketStatus.US_PRE, PriceReminderMarketStatus.OPEN, PriceReminderMarketStatus.US_AFTER, PriceReminderMarketStatus.US_OVERNIGHT])
    if ret_ask == RET_OK:
        print('When the selling price is lower than (ask_price-1), remind that the setting is successful:', ask_data)
    else:
        print('error:', ask_data)
    # Set a reminder for AAPL(24H) when the bid price is higher than (bid_price+1)
    ret_bid, bid_data = quote_ctx.set_price_reminder(code='US.AAPL', op=SetPriceReminderOp.ADD, key=None, reminder_type=PriceReminderType.BID_PRICE_UP, reminder_freq=PriceReminderFreq.ALWAYS, value=(bid_price+1), note='456', reminder_session_list=[PriceReminderMarketStatus.US_PRE, PriceReminderMarketStatus.OPEN, PriceReminderMarketStatus.US_AFTER, PriceReminderMarketStatus.US_OVERNIGHT])
    if ret_bid == RET_OK:
        print('When the bid price is higher than (bid_price+1), the reminder is set successfully: ', bid_data)
    else:
        print('error:', bid_data)
time.sleep(15)
quote_ctx.close()
```





- **Output**



``` python
When the selling price is lower than (ask_price-1), the reminder is set successfully: 158815356110052101
When the bid price is higher than (bid_price+1), the reminder is set successfully: 158815356129980801
```









## <a href="#2552" class="header-anchor">#</a> Qot_SetPriceReminder.proto

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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

  3220





`uint SetPriceReminder(QotSetPriceReminder.Request req);`  
`virtual void OnReply_SetPriceReminder(FTAPI_Conn client, uint nSerialNo, QotSetPriceReminder.Response rsp);`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotSetPriceReminder.C2S c2s = QotSetPriceReminder.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetOp(QotSetPriceReminder.SetPriceReminderOp.SetPriceReminderOp_Add)
                .SetType((int)QotCommon.PriceReminderType.PriceReminderType_PriceUp)
                .SetFreq((int)QotCommon.PriceReminderFreq.PriceReminderFreq_OnlyOnce)
                .SetValue(5)
            .Build();
        QotSetPriceReminder.Request req = QotSetPriceReminder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.SetPriceReminder(req);
        Console.Write("Send QotSetPriceReminder: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_SetPriceReminder(FTAPI_Conn client, uint nSerialNo, QotSetPriceReminder.Response rsp)
    {
        Console.Write("Reply: QotSetPriceReminder: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("key: {0} \n", rsp.S2C.Key);
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
Qot onInitConnect: ret=0 desc= connID=6826782725947038940
Send QotSetPriceReminder: 3
Reply: QotSetPriceReminder: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  key: 162763183755472101
}

key: 162763183755472101
```









`int setPriceReminder(QotSetPriceReminder.Request req);`  
`void onReply_SetPriceReminder(FTAPI_Conn client, int nSerialNo, QotSetPriceReminder.Response rsp);`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotSetPriceReminder.C2S c2s = QotSetPriceReminder.C2S.newBuilder()
                .setSecurity(sec)
                .setOp(QotSetPriceReminder.SetPriceReminderOp.SetPriceReminderOp_Add_VALUE)
                .setType(QotCommon.PriceReminderType.PriceReminderType_PriceUp_VALUE)
                .setFreq(QotCommon.PriceReminderFreq.PriceReminderFreq_OnlyOnce_VALUE)
                .setValue(5)
            .build();
        QotSetPriceReminder.Request req = QotSetPriceReminder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.setPriceReminder(req);
        System.out.printf("Send QotSetPriceReminder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_SetPriceReminder(FTAPI_Conn client, int nSerialNo, QotSetPriceReminder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotSetPriceReminder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotSetPriceReminder: %s\n", json);
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
Send QotSetPriceReminder: 2
Receive QotSetPriceReminder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "key": "162452649832682701"
  }
}
```









`Futu::u32_t SetPriceReminder(const Qot_SetPriceReminder::Request &stReq);`  
`virtual void OnReply_SetPriceReminder(Futu::u32_t nSerialNo, const Qot_SetPriceReminder::Response &stRsp) = 0;`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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
        Qot_SetPriceReminder::Request req;
        Qot_SetPriceReminder::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_op(1);
        c2s->set_type(Qot_Common::PriceReminderType::PriceReminderType_PriceUp);
        c2s->set_freq(Qot_Common::PriceReminderFreq::PriceReminderFreq_OnlyOnce);
        c2s->set_value(5);
        
        m_SetPriceReminderSerialNo = m_pQotApi->SetPriceReminder(req);
        cout << "Request SetPriceReminder SerialNo: " << m_SetPriceReminderSerialNo << endl;
    }

    virtual void OnReply_SetPriceReminder(Futu::u32_t nSerialNo, const Qot_SetPriceReminder::Response &stRsp){
        if(nSerialNo == m_SetPriceReminderSerialNo)
        {
            cout << "OnReply_SetPriceReminder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;
    
    Futu::u32_t m_SetPriceReminderSerialNo;
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
Request SetPriceReminder SerialNo: 3
OnReply_SetPriceReminder SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "key": "162321935858611601"
 }
}
```









`SetPriceReminder(req);`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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
import { Common, Qot_Common, Qot_SetPriceReminder } from "futu-api/proto";
import beautify from "js-beautify";

function QotSetPriceReminder(){
    const { RetType } = Common
    const { PriceReminderType, PriceReminderFreq, QotMarket } = Qot_Common
    const { SetPriceReminderOp } = Qot_SetPriceReminder
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
                    op: SetPriceReminderOp.SetPriceReminderOp_Add,
                    type: PriceReminderType.PriceReminderType_PriceUp,
                    freq: PriceReminderFreq.PriceReminderFreq_Always,
                    value: 600,
                },
            };
            websocket.SetPriceReminder(req)
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
  "key": "163126377342664201"
}
stop
```











Tips

- Trading volume in API is based on shares. A-shares are shown in lots
  in Futubull Client.

- The type of price alert has minimum precision, as follows:

  TURNOVER_UP: The minimum precision of the turnover is 10 (Yuan, Hong
  Kong dollar, US dollar). The value passed in will be automatically
  rounded down to an integer multiple of the minimum precision. If you
  set 00700 transaction volume 102 yuan reminder, you will get 00700
  transaction volume 100 yuan reminder. After setting; if you set 00700
  transaction volume 8 yuan reminder, you will get 00700 transaction
  volume 0 yuan reminder after setting.

  VOLUME_UP: The minimum accuracy of A-share trading volume is 1000
  shares, and the minimum accuracy of other market stock trading volume
  is 10 shares. The value passed in will be automatically rounded down
  to an integer multiple of the minimum precision.

  BID_VOL_UP, ASK_VOL_UP: The minimum precision for buying and selling
  of A-shares is 100 shares. The value passed in will be automatically
  rounded down to an integer multiple of the minimum precision.

  The precision of the remaining price alert types supports up to 3
  decimal places





Interface Limitations

- A maximum of 60 requests per 30 seconds
- The upper limit of reminders that can be set for each type of each
  stock is 10











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`set_price_reminder(code, op, key=None, reminder_type=None, reminder_freq=None, value=None, note=None, reminder_session_list=NONE)`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

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
  <td style="text-align: left;">Stock code</td>
  </tr>
  <tr>
  <td style="text-align: left;">op</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8810">SetPriceReminderOp</a></td>
  <td style="text-align: left;">Operation type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">key</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Identification, do not need to fill in the
  case of adding all or deleting all.</td>
  </tr>
  <tr>
  <td style="text-align: left;">reminder_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#3793">PriceReminderType</a></td>
  <td style="text-align: left;">The type of price reminder, this input
  parameter will be ignored when delete, enable, or disable.</td>
  </tr>
  <tr>
  <td style="text-align: left;">reminder_freq</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9918">PriceReminderFreq</a></td>
  <td style="text-align: left;">The frequency of price reminder, this
  input parameter will be ignored when delete, enabled, or disable.</td>
  </tr>
  <tr>
  <td style="text-align: left;">value</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">Reminder value, the input parameter will
  be ignored when delete, enable, or disable.
  
    
  
  
   
  
  3 decimal place accuracy, the excess part is discarded.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">note</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">The note set by the user, note supports no
  more than 20 Chinese characters, the input parameter will be ignored
  when delete, enable, or disable.</td>
  </tr>
  <tr>
  <td style="text-align: left;">reminder_session_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">The session for US stocks price reminder,
  this input parameter will be ignored when delete, enable, or disable.
  
    
  
  
   
  
  <ul>
  <li>The parameter type in list is <a
  href="/moomoo-api-doc/en/quote/quote.html#6578">PriceReminderMarketStatus</a>.</li>
  <li>The default price reminder session for US stocks is
  pre/post+RTH.</li>
  </ul>
  
  
  
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
  <td rowspan="2">key</td>
  <td>int</td>
  <td>If ret == RET_OK, The price reminder key of the operation is
  returned. When deleting all reminders of a specific stock, 0 is
  returned.</td>
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
import time
class PriceReminderTest(PriceReminderHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, content = super(PriceReminderTest,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("PriceReminderTest: error, msg: %s" % content)
            return RET_ERROR, content
        print("PriceReminderTest ", content)
        return RET_OK, content
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = PriceReminderTest()
quote_ctx.set_handler(handler)
ret, data = quote_ctx.get_market_snapshot(['US.AAPL'])
if ret == RET_OK:
    bid_price = data['bid_price'][0] # Get real-time bid price
    ask_price = data['ask_price'][0] # Get real-time selling price
    # Set a reminder for AAPL(24H) when the selling price is lower than (ask_price-1)
    ret_ask, ask_data = quote_ctx.set_price_reminder(code='US.AAPL', op=SetPriceReminderOp.ADD, key=None, reminder_type=PriceReminderTypeASK_PRICE_DOWN, reminder_freq=PriceReminderFreq.ALWAYS, value=(ask_price-1), note='123', reminder_session_list=[PriceReminderMarketStatus.US_PRE, PriceReminderMarketStatus.OPEN, PriceReminderMarketStatus.US_AFTER, PriceReminderMarketStatus.US_OVERNIGHT])
    if ret_ask == RET_OK:
        print('When the selling price is lower than (ask_price-1), remind that the setting is successful:', ask_data)
    else:
        print('error:', ask_data)
    # Set a reminder for AAPL(24H) when the bid price is higher than (bid_price+1)
    ret_bid, bid_data = quote_ctx.set_price_reminder(code='US.AAPL', op=SetPriceReminderOp.ADD, key=None, reminder_type=PriceReminderType.BID_PRICE_UP, reminder_freq=PriceReminderFreq.ALWAYS, value=(bid_price+1), note='456', reminder_session_list=[PriceReminderMarketStatus.US_PRE, PriceReminderMarketStatus.OPEN, PriceReminderMarketStatus.US_AFTER, PriceReminderMarketStatus.US_OVERNIGHT])
    if ret_bid == RET_OK:
        print('When the bid price is higher than (bid_price+1), the reminder is set successfully: ', bid_data)
    else:
        print('error:', bid_data)
time.sleep(15)
quote_ctx.close()
```





- **Output**



``` python
When the selling price is lower than (ask_price-1), the reminder is set successfully: 158815356110052101
When the bid price is higher than (bid_price+1), the reminder is set successfully: 158815356129980801
```









## <a href="#2552-2" class="header-anchor">#</a> Qot_SetPriceReminder.proto

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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

  3220





`uint SetPriceReminder(QotSetPriceReminder.Request req);`  
`virtual void OnReply_SetPriceReminder(MMAPI_Conn client, uint nSerialNo, QotSetPriceReminder.Response rsp);`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotSetPriceReminder.C2S c2s = QotSetPriceReminder.C2S.CreateBuilder()
                .SetSecurity(sec)
                .SetOp(QotSetPriceReminder.SetPriceReminderOp.SetPriceReminderOp_Add)
                .SetType((int)QotCommon.PriceReminderType.PriceReminderType_PriceUp)
                .SetFreq((int)QotCommon.PriceReminderFreq.PriceReminderFreq_OnlyOnce)
                .SetValue(5)
            .Build();
        QotSetPriceReminder.Request req = QotSetPriceReminder.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.SetPriceReminder(req);
        Console.Write("Send QotSetPriceReminder: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_SetPriceReminder(MMAPI_Conn client, uint nSerialNo, QotSetPriceReminder.Response rsp)
    {
        Console.Write("Reply: QotSetPriceReminder: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("key: {0} \n", rsp.S2C.Key);
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
Qot onInitConnect: ret=0 desc= connID=6826782725947038940
Send QotSetPriceReminder: 3
Reply: QotSetPriceReminder: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  key: 162763183755472101
}

key: 162763183755472101
```









`int setPriceReminder(QotSetPriceReminder.Request req);`  
`void onReply_SetPriceReminder(MMAPI_Conn client, int nSerialNo, QotSetPriceReminder.Response rsp);`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotSetPriceReminder.C2S c2s = QotSetPriceReminder.C2S.newBuilder()
                .setSecurity(sec)
                .setOp(QotSetPriceReminder.SetPriceReminderOp.SetPriceReminderOp_Add_VALUE)
                .setType(QotCommon.PriceReminderType.PriceReminderType_PriceUp_VALUE)
                .setFreq(QotCommon.PriceReminderFreq.PriceReminderFreq_OnlyOnce_VALUE)
                .setValue(5)
            .build();
        QotSetPriceReminder.Request req = QotSetPriceReminder.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.setPriceReminder(req);
        System.out.printf("Send QotSetPriceReminder: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_SetPriceReminder(MMAPI_Conn client, int nSerialNo, QotSetPriceReminder.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotSetPriceReminder failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotSetPriceReminder: %s\n", json);
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
Send QotSetPriceReminder: 2
Receive QotSetPriceReminder: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "key": "162452649832682701"
  }
}
```









`moomoo::u32_t SetPriceReminder(const Qot_SetPriceReminder::Request &stReq);`  
`virtual void OnReply_SetPriceReminder(moomoo::u32_t nSerialNo, const Qot_SetPriceReminder::Response &stRsp) = 0;`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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
        Qot_SetPriceReminder::Request req;
        Qot_SetPriceReminder::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_op(1);
        c2s->set_type(Qot_Common::PriceReminderType::PriceReminderType_PriceUp);
        c2s->set_freq(Qot_Common::PriceReminderFreq::PriceReminderFreq_OnlyOnce);
        c2s->set_value(5);
        
        m_SetPriceReminderSerialNo = m_pQotApi->SetPriceReminder(req);
        cout << "Request SetPriceReminder SerialNo: " << m_SetPriceReminderSerialNo << endl;
    }

    virtual void OnReply_SetPriceReminder(moomoo::u32_t nSerialNo, const Qot_SetPriceReminder::Response &stRsp){
        if(nSerialNo == m_SetPriceReminderSerialNo)
        {
            cout << "OnReply_SetPriceReminder SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;
    
    moomoo::u32_t m_SetPriceReminderSerialNo;
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
Request SetPriceReminder SerialNo: 3
OnReply_SetPriceReminder SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "key": "162321935858611601"
 }
}
```









`SetPriceReminder(req);`

- **Description**

  Add, delete, modify, enable, and disable price reminders for specified
  stocks

- **Parameters**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all price reminders under this stock
}

message C2S
{
    required Qot_Common.Security security = 1; //Security
    required int32 op = 2; //SetPriceReminderOp, operation type
    optional int64 key = 3; //The identifier of the price reminder, is available through the GetPriceReminder protocol. It is used to specify the price reminder item to be operated. It is not necessary to fill in when add
    optional int32 type = 4; //Qot_Common::PriceReminderType, reminder type, this field will be ignored when delete, enable, or disable
    optional int32 freq = 7; //Qot_Common::PriceReminderFreq, the type of reminder frequency, this field will be ignored when delete, enable, or disable
    optional double value = 5; //Reminder value, this field will be ignored when delete, enable, or disable(3 decimal place accuracy, the excess part is discarded)
    optional string note = 6; //The note when the user sets the price reminder, note supports no more than 20 Chinese characters, this field will be ignored when delete,  enable, or disable
    repeated int32 reminderSessionList = 8; // reminder session list，this field will be ignored when delete, enable, or disable, Qot_Common::PriceReminderMarketStatus
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For reminder type enumeration, refer to
>   [PriceReminderType](/moomoo-api-doc/en/quote/quote.html#3793)
> - For enumeration of reminder frequency, refer to
>   [PriceReminderFreq](/moomoo-api-doc/en/quote/quote.html#9918)

- **Return**



``` protobuf
message S2C
{
    required int64 key = 1; //If the setting is successful, the corresponding key will be returned, otherwise 0
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
import { Common, Qot_Common, Qot_SetPriceReminder } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotSetPriceReminder(){
    const { RetType } = Common
    const { PriceReminderType, PriceReminderFreq, QotMarket } = Qot_Common
    const { SetPriceReminderOp } = Qot_SetPriceReminder
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
                    op: SetPriceReminderOp.SetPriceReminderOp_Add,
                    type: PriceReminderType.PriceReminderType_PriceUp,
                    freq: PriceReminderFreq.PriceReminderFreq_Always,
                    value: 600,
                },
            };
            websocket.SetPriceReminder(req)
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
  "key": "163126377342664201"
}
stop
```











Tips

- Trading volume in API is based on shares. A-shares are shown in lots
  in moomoo Client.

- The type of price alert has minimum precision, as follows:

  TURNOVER_UP: The minimum precision of the turnover is 10 (Yuan, Hong
  Kong dollar, US dollar). The value passed in will be automatically
  rounded down to an integer multiple of the minimum precision. If you
  set 00700 transaction volume 102 yuan reminder, you will get 00700
  transaction volume 100 yuan reminder. After setting; if you set 00700
  transaction volume 8 yuan reminder, you will get 00700 transaction
  volume 0 yuan reminder after setting.

  VOLUME_UP: The minimum accuracy of A-share trading volume is 1000
  shares, and the minimum accuracy of other market stock trading volume
  is 10 shares. The value passed in will be automatically rounded down
  to an integer multiple of the minimum precision.

  BID_VOL_UP, ASK_VOL_UP: The minimum precision for buying and selling
  of A-shares is 100 shares. The value passed in will be automatically
  rounded down to an integer multiple of the minimum precision.

  The precision of the remaining price alert types supports up to 3
  decimal places





Interface Limitations

- A maximum of 60 requests per 30 seconds
- The upper limit of reminders that can be set for each type of each
  stock is 10













