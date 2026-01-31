



# <a href="#870" class="header-anchor">#</a> Get Stock Basic Information









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_stock_basicinfo(market, stock_type=SecurityType.STOCK, code_list=None)`

- **Description**

  Get Stock Basic Information

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
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Market type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">stock_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
  <td style="text-align: left;">Stock type. It does not support
  SecurityType.DRVT.</td>
  </tr>
  <tr>
  <td style="text-align: left;">code_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Stock list.
  
    
  
  
   
  
  <ul>
  <li>The default is None, which means to get the static information of
  the stocks in the whole market.</li>
  <li>If the stock list is passed in, only the information of the
  specified stocks will be returned.</li>
  <li>Data type of elements in the list is str.</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  Note: when both *market* and *code_list* exist, *market* is ignored
  and only *code_list* is effective.

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
  <td>If ret == RET_OK, stock static data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock static data format as follows:
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
    per contract for options
    
      
    
    
     
    
    Index options do not have this field.
    
    
    
    
    , contract multipliers for futures.</td>
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
    
      
    
    
     
    
    True: suspension.<br />
    False: not suspended.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing time.
    
      
    
    
     
    
    This field is deprecated.<br />
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
    <td style="text-align: left;">Whether is delisted or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Index option type.</td>
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
    
      
    
    
     
    
    Main, current month and next month futures etc. do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">exchange_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#7268">ExchType</a></td>
    <td style="text-align: left;">Exchange Type.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK)
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
print('******************************************')
ret, data = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK, ['HK.06998', 'HK.00700'])
if ret == RET_OK:
    print(data)
    print(data['name'][0]) # Take the first stock name
    print(data['name'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
        code             name  lot_size stock_type stock_child_type stock_owner option_type strike_time strike_price suspension listing_date        stock_id  delisting index_option_type  main_contract last_trade_time exchange_type
0      HK.00001     CK Hutchison       500      STOCK              N/A                                              N/A        N/A   2015-03-18   4440996184065      False               N/A          False                  HK_MAINBOARD 
...         ...              ...       ...        ...              ...         ...         ...         ...          ...        ...          ...             ...        ...               ...            ...             ...
2592   HK.09979     GREENTOWN MANAGEMENT HOLDINGS COMPANY LIMITED      1000      STOCK              N/A                                              N/A        N/A   2020-07-10  79203491915515      False               N/A          False                  HK_MAINBOARD               

[2593 rows x 16 columns]
******************************************
        code            name  lot_size stock_type stock_child_type stock_owner option_type strike_time strike_price suspension listing_date        stock_id  delisting index_option_type  main_contract last_trade_time exchange_type
0  HK.06998     JHBP       500      STOCK              N/A                                              N/A        N/A   2020-10-07  79572859099990      False               N/A          False                  HK_MAINBOARD               
1  HK.00700     Tencent       100      STOCK              N/A                                              N/A        N/A   2004-06-16  54047868453564      False               N/A          False                  HK_MAINBOARD               
JHBP
['JHBP', 'Tencent']
```









## <a href="#9277" class="header-anchor">#</a> Qot_GetStaticInfo.proto

- **Description**

  Get static data

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3202





`uint GetStaticInfo(QotGetStaticInfo.Request req);`  
`virtual void OnReply_GetStaticInfo(FTAPI_Conn client, uint nSerialNo, QotGetStaticInfo.Response rsp);`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetStaticInfo.C2S c2s = QotGetStaticInfo.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetStaticInfo.Request req = QotGetStaticInfo.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetStaticInfo(req);
        Console.Write("Send QotGetStaticInfo: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetStaticInfo(FTAPI_Conn client, uint nSerialNo, QotGetStaticInfo.Response rsp)
    {
        Console.Write("Reply: QotGetStaticInfo: {0}\n", nSerialNo);
        Console.Write("name: {0}, listTime: {1}\n", rsp.S2C.StaticInfoListList[0].Basic.Name,
            rsp.S2C.StaticInfoListList[0].Basic.ListTime);
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
Qot onInitConnect: ret=0 desc= connID=6825962957633551611
Send QotGetStaticInfo: 3
Reply: QotGetStaticInfo: 3
name: Tencent, listTime: 2004-06-16
```









`int getStaticInfo(QotGetStaticInfo.Request req);`  
`void onReply_GetStaticInfo(FTAPI_Conn client, int nSerialNo, QotGetStaticInfo.Response rsp);`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
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

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetStaticInfo.C2S c2s = QotGetStaticInfo.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetStaticInfo.Request req = QotGetStaticInfo.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getStaticInfo(req);
        System.out.printf("Send QotGetStaticInfo: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetStaticInfo(FTAPI_Conn client, int nSerialNo, QotGetStaticInfo.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetStaticInfo failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetStaticInfo: %s\n", json);
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
Send QotGetStaticInfo: 2
Receive QotGetStaticInfo: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
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
        "listTimestamp": 1.0873152E9,
        "exchType": 1
      }
    }]
  }
}
```









`Futu::u32_t GetStaticInfo(const Qot_GetStaticInfo::Request &stReq);`  
`virtual void OnReply_GetStaticInfo(Futu::u32_t nSerialNo, const Qot_GetStaticInfo::Response &stRsp) = 0;`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
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
        Qot_GetStaticInfo::Request req;
        Qot_GetStaticInfo::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetStaticInfoSerialNo = m_pQotApi->GetStaticInfo(req);
        cout << "Request GetStaticInfo SerialNo: " << m_GetStaticInfoSerialNo << endl;
    }

    virtual void OnReply_GetStaticInfo(Futu::u32_t nSerialNo, const Qot_GetStaticInfo::Response &stRsp){
        if(nSerialNo == m_GetStaticInfoSerialNo)
        {
            cout << "OnReply_GetStaticInfo SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_StockFilterSerialNo;
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
Request GetStaticInfo SerialNo: 4
OnReply_GetStaticInfo SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "staticInfoList": [
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
     "listTimestamp": 1087315200,
     "exchType": 1
    }
   }
  ]
 }
}
```









`GetStaticInfo(req);`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetStaticInfo(){
    const { RetType } = Common
    const { QotMarket, PlateSetType } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    securityList: [{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },],
                },
            };

            websocket.GetStaticInfo(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("StaticInfo: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
StaticInfo: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
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

- When input stocks are not recognized by the program (including stocks
  that have been delisted a long time ago and non-existent stocks), this
  interface still returns stock information. The "delisted" field is
  used to indicate that the stock does exist or not. The unified
  processing is: the code is displayed normally, the stock name is
  displayed as "unknown stock", and the other fields are default values
  (The integer type defaults to 0, and the string defaults to an empty
  string.).
- This interface is different from other market information interfaces.
  When other interfaces get input stocks that the program cannot
  recognize, they will reject the request and return the error
  description "unknown stock".











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_stock_basicinfo(market, stock_type=SecurityType.STOCK, code_list=None)`

- **Description**

  Get Stock Basic Information

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
  <td style="text-align: left;">market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#456">Market</a></td>
  <td style="text-align: left;">Market type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">stock_type</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#9767">SecurityType</a></td>
  <td style="text-align: left;">Stock type. It does not support
  SecurityType.DRVT.</td>
  </tr>
  <tr>
  <td style="text-align: left;">code_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Stock list.
  
    
  
  
   
  
  <ul>
  <li>The default is None, which means to get the static information of
  the stocks in the whole market.</li>
  <li>If the stock list is passed in, only the information of the
  specified stocks will be returned.</li>
  <li>Data type of elements in the list is str.</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  Note: when both *market* and *code_list* exist, *market* is ignored
  and only *code_list* is effective.

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
  <td>If ret == RET_OK, stock static data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Stock static data format as follows:
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
    per contract for options
    
      
    
    
     
    
    Index options do not have this field.
    
    
    
    
    , contract multipliers for futures.</td>
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
    
      
    
    
     
    
    True: suspension.<br />
    False: not suspended.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing time.
    
      
    
    
     
    
    This field is deprecated.<br />
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
    <td style="text-align: left;">Whether is delisted or not.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Index option type.</td>
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
    
      
    
    
     
    
    Main, current month and next month futures etc. do not have this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">exchange_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#7268">ExchType</a></td>
    <td style="text-align: left;">Exchange Type.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK)
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
print('******************************************')
ret, data = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK, ['HK.06998', 'HK.00700'])
if ret == RET_OK:
    print(data)
    print(data['name'][0]) # Take the first stock name
    print(data['name'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
        code             name  lot_size stock_type stock_child_type stock_owner option_type strike_time strike_price suspension listing_date        stock_id  delisting index_option_type  main_contract last_trade_time exchange_type
0      HK.00001     CK Hutchison       500      STOCK              N/A                                              N/A        N/A   2015-03-18   4440996184065      False               N/A          False                  HK_MAINBOARD 
...         ...              ...       ...        ...              ...         ...         ...         ...          ...        ...          ...             ...        ...               ...            ...             ...
2592   HK.09979     GREENTOWN MANAGEMENT HOLDINGS COMPANY LIMITED      1000      STOCK              N/A                                              N/A        N/A   2020-07-10  79203491915515      False               N/A          False                  HK_MAINBOARD               

[2593 rows x 16 columns]
******************************************
        code            name  lot_size stock_type stock_child_type stock_owner option_type strike_time strike_price suspension listing_date        stock_id  delisting index_option_type  main_contract last_trade_time exchange_type
0  HK.06998     JHBP       500      STOCK              N/A                                              N/A        N/A   2020-10-07  79572859099990      False               N/A          False                  HK_MAINBOARD               
1  HK.00700     Tencent       100      STOCK              N/A                                              N/A        N/A   2004-06-16  54047868453564      False               N/A          False                  HK_MAINBOARD               
JHBP
['JHBP', 'Tencent']
```









## <a href="#9277-2" class="header-anchor">#</a> Qot_GetStaticInfo.proto

- **Description**

  Get static data

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3202





`uint GetStaticInfo(QotGetStaticInfo.Request req);`  
`virtual void OnReply_GetStaticInfo(MMAPI_Conn client, uint nSerialNo, QotGetStaticInfo.Response rsp);`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
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

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetStaticInfo.C2S c2s = QotGetStaticInfo.C2S.CreateBuilder()
                .AddSecurityList(sec)
            .Build();
        QotGetStaticInfo.Request req = QotGetStaticInfo.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetStaticInfo(req);
        Console.Write("Send QotGetStaticInfo: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetStaticInfo(MMAPI_Conn client, uint nSerialNo, QotGetStaticInfo.Response rsp)
    {
        Console.Write("Reply: QotGetStaticInfo: {0}\n", nSerialNo);
        Console.Write("name: {0}, listTime: {1}\n", rsp.S2C.StaticInfoListList[0].Basic.Name,
            rsp.S2C.StaticInfoListList[0].Basic.ListTime);
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
Qot onInitConnect: ret=0 desc= connID=6825962957633551611
Send QotGetStaticInfo: 3
Reply: QotGetStaticInfo: 3
name: Tencent, listTime: 2004-06-16
```









`int getStaticInfo(QotGetStaticInfo.Request req);`  
`void onReply_GetStaticInfo(MMAPI_Conn client, int nSerialNo, QotGetStaticInfo.Response rsp);`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
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

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetStaticInfo.C2S c2s = QotGetStaticInfo.C2S.newBuilder()
                .addSecurityList(sec)
            .build();
        QotGetStaticInfo.Request req = QotGetStaticInfo.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getStaticInfo(req);
        System.out.printf("Send QotGetStaticInfo: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetStaticInfo(MMAPI_Conn client, int nSerialNo, QotGetStaticInfo.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetStaticInfo failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetStaticInfo: %s\n", json);
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
Send QotGetStaticInfo: 2
Receive QotGetStaticInfo: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "staticInfoList": [{
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
        "listTimestamp": 1.0873152E9,
        "exchType": 1
      }
    }]
  }
}
```









`moomoo::u32_t GetStaticInfo(const Qot_GetStaticInfo::Request &stReq);`  
`virtual void OnReply_GetStaticInfo(moomoo::u32_t nSerialNo, const Qot_GetStaticInfo::Response &stRsp) = 0;`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
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
        Qot_GetStaticInfo::Request req;
        Qot_GetStaticInfo::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetStaticInfoSerialNo = m_pQotApi->GetStaticInfo(req);
        cout << "Request GetStaticInfo SerialNo: " << m_GetStaticInfoSerialNo << endl;
    }

    virtual void OnReply_GetStaticInfo(moomoo::u32_t nSerialNo, const Qot_GetStaticInfo::Response &stRsp){
        if(nSerialNo == m_GetStaticInfoSerialNo)
        {
            cout << "OnReply_GetStaticInfo SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_StockFilterSerialNo;
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
Request GetStaticInfo SerialNo: 4
OnReply_GetStaticInfo SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "staticInfoList": [
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
     "listTimestamp": 1087315200,
     "exchType": 1
    }
   }
  ]
 }
}
```









`GetStaticInfo(req);`

- **Description**

  Get Stock Basic Information

- **Parameters**



``` protobuf
message C2S
{
    // when both market and code_list exist, market is ignored and only code_list is effective.
    optional int32 market = 1; //Qot_Common.QotMarket, stock market
    optional int32 secType = 2; //Qot_Common.SecurityType, stock type
    repeated Qot_Common.Security securityList = 3; //Stock, if this field exists, ignore other fields, and only return the static information of the stocks in this field
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)
> - For stock type, refer to
>   [SecurityType](/moomoo-api-doc/en/quote/quote.html#9767)

- **Return**



``` protobuf
message S2C
{
    repeated Qot_Common.SecurityStaticInfo staticInfoList = 1; //Static information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock static information structure, refer to
>   [SecurityStaticInfo](/moomoo-api-doc/en/quote/quote.html#5588)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetStaticInfo(){
    const { RetType } = Common
    const { QotMarket, PlateSetType } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    securityList: [{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },],
                },
            };

            websocket.GetStaticInfo(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("StaticInfo: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
StaticInfo: errCode 0, retMsg , retType 0
{
  "staticInfoList": [{
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

- When input stocks are not recognized by the program (including stocks
  that have been delisted a long time ago and non-existent stocks), this
  interface still returns stock information. The "delisted" field is
  used to indicate that the stock does exist or not. The unified
  processing is: the code is displayed normally, the stock name is
  displayed as "unknown stock", and the other fields are default values
  (The integer type defaults to 0, and the string defaults to an empty
  string.).
- This interface is different from other market information interfaces.
  When other interfaces get input stocks that the program cannot
  recognize, they will reject the request and return the error
  description "unknown stock".













