



# <a href="#3809" class="header-anchor">#</a> Get Real-time Time Frame Data









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_rt_data(code)`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**

  | Parameter | Type | Description |
  |:----------|:-----|:------------|
  | code      | str  | Stock code. |

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
  <td>If ret == RET_OK, Time Frame data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Time Frame data format as follows:
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
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_blank</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Data status.
    
      
    
    
     
    
    False: normal data.<br />
    True: forged data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">opened_mins</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">How many minutes have passed from 0
    o'clock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Current price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average price.
    
      
    
    
     
    
    For options, this field is N/A.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.RT_DATA], subscribe_push=False, session=Session.ALL)
# Subscribe to the Time Frame data type first. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK:   # Successfully subscribed
    ret, data = quote_ctx.get_rt_data('US.AAPL')   # Get Time Frame data once
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
else:
    print('subscription failed', err_message)
quote_ctx.close()   # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code  name                 time  is_blank  opened_mins  cur_price  last_close   avg_price   volume     turnover
0    US.AAPL   APPLE  2025-04-06 20:01:00     False         1201     183.00      188.38  181.643916    9463  1718896.38
..      ...    ...                  ...       ...          ...        ...         ...         ...      ...          ...
586  US.AAPL   APPLE  2025-04-07 05:47:00     False          347     181.26      188.38  180.555673     661   119859.75

[587 rows x 10 columns]
```









## <a href="#4930" class="header-anchor">#</a> Qot_GetRT.proto

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3008





`uint GetRT(QotGetRT.Request req);`  
`virtual void OnReply_GetRT(FTAPI_Conn client, uint nSerialNo, QotGetRT.Response rsp);`

- **Description**

  To obtain real-time Time Frame data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_RT)
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

        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
            return;

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetRT.C2S c2s = QotGetRT.C2S.CreateBuilder()
                .SetSecurity(sec)
                .Build();
        QotGetRT.Request req = QotGetRT.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetRT(req);
        Console.Write("Send QotGetRT: {0}\n", seqNo);
    }

    public void OnReply_GetRT(FTAPI_Conn client, uint nSerialNo, QotGetRT.Response rsp)
    {
        Console.Write("Reply: QotGetRT: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.RtListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825673513534857375
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetRT: 4
Reply: QotGetRT: 4
price: 465.4
```









`int getRT(QotGetRT.Request req);`  
`void onReply_GetRT(FTAPI_Conn client, int nSerialNo, QotGetRT.Response rsp);`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
        QotSub.C2S c2s = QotSub.C2S.newBuilder()
                .addSecurityList(sec)
                .addSubTypeList(QotCommon.SubType.SubType_RT_VALUE)
                .setIsSubOrUnSub(true)
                .build();
        QotSub.Request req = QotSub.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.sub(req);
        System.out.printf("Send QotSub: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_Sub(FTAPI_Conn client, int nSerialNo, QotSub.Response rsp) {
        System.out.printf("Reply: QotSub: %d  %s\n", nSerialNo, rsp.toString());

        if (rsp.getRetType() != Common.RetType.RetType_Succeed_VALUE)
            return;

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetRT.C2S c2s = QotGetRT.C2S.newBuilder()
                .setSecurity(sec)
                .build();
        QotGetRT.Request req = QotGetRT.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getRT(req);
        System.out.printf("Send QotGetRT: %d\n", seqNo);
    }

    @Override
    public void onReply_GetRT(FTAPI_Conn client, int nSerialNo, QotGetRT.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetRT failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetRT: %s\n", json);
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
Send QotGetRT: 3
Receive QotGetRT: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "rtList": [{
      "time": "2021-06-24 09:30:00",
      "minute": 570,
      "isBlank": false,
      "price": 584.0,
      "lastClosePrice": 582.5,
      "avgPrice": 584.0,
      "volume": "431600",
      "turnover": 2.520544E8,
      "timestamp": 1.6244982E9
    }, ... {
      "time": "2021-06-24 16:00:00",
      "minute": 960,
      "isBlank": false,
      "price": 583.0,
      "lastClosePrice": 582.5,
      "avgPrice": 583.4658532703611,
      "volume": "1197900",
      "turnover": 6.98392175E8,
      "timestamp": 1.6245216E9
    }]
  }
}
```









`Futu::u32_t GetRT(const Qot_GetRT::Request &stReq);`  
`virtual void OnReply_GetRT(Futu::u32_t nSerialNo, const Qot_GetRT::Response &stRsp) = 0;`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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

        // subscribe first
        Qot_Sub::Request req;
        Qot_Sub::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->add_subtypelist(Qot_Common::SubType::SubType_RT);
        c2s->set_isregorunregpush(true);
        c2s->set_issuborunsub(true);
        
        m_SubSerialNo = m_pQotApi->Sub(req);
        cout << "Request Sub SerialNo: " << m_SubSerialNo << endl;
    }

    virtual void OnReply_Sub(Futu::u32_t nSerialNo, const Qot_Sub::Response &stRsp)
    {
        if(nSerialNo == m_SubSerialNo)
        {
            cout << "OnReply_Sub SerialNo: " << nSerialNo << endl;
            if(stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }        

            // construct request message
            Qot_GetRT::Request req;
            Qot_GetRT::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

            m_GetRTSerialNo = m_pQotApi->GetRT(req);
            cout << "Request GetRT SerialNo: " << m_GetRTSerialNo << endl;
        }
    }

    virtual void OnReply_GetRT(Futu::u32_t nSerialNo, const Qot_GetRT::Response &stRsp){
        if(nSerialNo == m_GetRTSerialNo)
        {
            cout << "OnReply_GetRT SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_SubSerialNo;
    Futu::u32_t m_GetRTSerialNo;
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
Request Sub SerialNo: 3
OnReply_Sub SerialNo: 3
Request GetRT SerialNo: 4
OnReply_GetRT SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "rtList": [
   {
    "time": "2021-06-09 09:30:00",
    "minute": 570,
    "isBlank": false,
    "price": 600,
    "lastClosePrice": 601,
    "avgPrice": 600,
    "volume": "255100",
    "turnover": 153060000,
    "timestamp": 1623202200
   },
   {
    "time": "2021-06-09 09:31:00",
    "minute": 571,
    "isBlank": false,
    "price": 599.5,
    "lastClosePrice": 601,
    "avgPrice": 599.41146019278824,
    "volume": "305100",
    "turnover": 182730300,
    "timestamp": 1623202260
   },
...
   {
    "time": "2021-06-09 14:13:00",
    "minute": 853,
    "isBlank": false,
    "price": 600.5,
    "lastClosePrice": 601,
    "avgPrice": 602.188546883593,
    "volume": "1600",
    "turnover": 960850,
    "timestamp": 1623219180
   }
  ]
 }
}
```









`GetRT(req);`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetRT(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();
    
    websocket.onlogin = (ret, msg)=>{
        if (ret) {
            websocket.Sub({
                c2s: {
                securityList: [
                    {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                ],
                subTypeList: [ SubType.SubType_RT ], 
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                        security: {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                    },
                };
                
                websocket.GetRT(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("RT: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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

            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("sub error:", error.retMsg);
                }
            });
        } else {
            console.log("start error", msg);
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
RT: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "rtList": [{
    "time": "2021-09-09 09:30:00",
    "minute": 570,
    "isBlank": false,
    "price": 509,
    "lastClosePrice": 524.5,
    "avgPrice": 509,
    "volume": "941800",
    "turnover": 479376200,
    "timestamp": 1631151000
  }, {
    "time": "2021-09-09 09:31:00",
    "minute": 571,
    "isBlank": false,
    "price": 506.5,
    "lastClosePrice": 524.5,
    "avgPrice": 507.88588572919383,
    "volume": "974700",
    "turnover": 493987100,
    "timestamp": 1631151060
  }, ..., {
    "time": "2021-09-09 09:32:00",
    "minute": 572,
    "isBlank": false,
    "price": 504,
    "lastClosePrice": 524.5,
    "avgPrice": 507.3999031165602,
    "volume": "416200",
    "turnover": 210248454,
    "timestamp": 1631151120
  },],
}
stop
```











Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Time Frame
  Callback](/moomoo-api-doc/en/quote/update-rt.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_rt_data(code)`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**

  | Parameter | Type | Description |
  |:----------|:-----|:------------|
  | code      | str  | Stock code. |

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
  <td>If ret == RET_OK, Time Frame data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Time Frame data format as follows:
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
    <td style="text-align: left;">time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time.
    
      
    
    
     
    
    yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">is_blank</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Data status.
    
      
    
    
     
    
    False: normal data.<br />
    True: forged data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">opened_mins</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">How many minutes have passed from 0
    o'clock.</td>
    </tr>
    <tr>
    <td style="text-align: left;">cur_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Current price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">avg_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average price.
    
      
    
    
     
    
    For options, this field is N/A.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.RT_DATA], subscribe_push=False, session=Session.ALL)
# Subscribe to the Time Frame data type first. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK:   # Successfully subscribed
    ret, data = quote_ctx.get_rt_data('US.AAPL')   # Get Time Frame data once
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
else:
    print('subscription failed', err_message)
quote_ctx.close()   # Close the current link, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code  name                 time  is_blank  opened_mins  cur_price  last_close   avg_price   volume     turnover
0    US.AAPL   APPLE  2025-04-06 20:01:00     False         1201     183.00      188.38  181.643916    9463  1718896.38
..      ...    ...                  ...       ...          ...        ...         ...         ...      ...          ...
586  US.AAPL   APPLE  2025-04-07 05:47:00     False          347     181.26      188.38  180.555673     661   119859.75

[587 rows x 10 columns]
```









## <a href="#4930-2" class="header-anchor">#</a> Qot_GetRT.proto

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3008





`uint GetRT(QotGetRT.Request req);`  
`virtual void OnReply_GetRT(MMAPI_Conn client, uint nSerialNo, QotGetRT.Response rsp);`

- **Description**

  To obtain real-time Time Frame data of subscribed stocks, you must
  subscribe first.

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
        QotSub.C2S c2s = QotSub.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .AddSubTypeList((int)QotCommon.SubType.SubType_RT)
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

        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
            return;

        QotCommon.Security sec = QotCommon.Security.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_HK_Security)
                .SetCode("00700")
                .Build();
        QotGetRT.C2S c2s = QotGetRT.C2S.CreateBuilder()
                .SetSecurity(sec)
                .Build();
        QotGetRT.Request req = QotGetRT.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetRT(req);
        Console.Write("Send QotGetRT: {0}\n", seqNo);
    }

    public void OnReply_GetRT(MMAPI_Conn client, uint nSerialNo, QotGetRT.Response rsp)
    {
        Console.Write("Reply: QotGetRT: {0}\n", nSerialNo);
        Console.Write("price: {0}\n", rsp.S2C.RtListList[0].Price);
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
Qot onInitConnect: ret=0 desc= connID=6825673513534857375
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetRT: 4
Reply: QotGetRT: 4
price: 465.4
```









`int getRT(QotGetRT.Request req);`  
`void onReply_GetRT(MMAPI_Conn client, int nSerialNo, QotGetRT.Response rsp);`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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
        QotSub.C2S c2s = QotSub.C2S.newBuilder()
                .addSecurityList(sec)
                .addSubTypeList(QotCommon.SubType.SubType_RT_VALUE)
                .setIsSubOrUnSub(true)
                .build();
        QotSub.Request req = QotSub.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.sub(req);
        System.out.printf("Send QotSub: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_Sub(MMAPI_Conn client, int nSerialNo, QotSub.Response rsp) {
        System.out.printf("Reply: QotSub: %d  %s\n", nSerialNo, rsp.toString());

        if (rsp.getRetType() != Common.RetType.RetType_Succeed_VALUE)
            return;

        QotCommon.Security sec = QotCommon.Security.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .setCode("00700")
                .build();
        QotGetRT.C2S c2s = QotGetRT.C2S.newBuilder()
                .setSecurity(sec)
                .build();
        QotGetRT.Request req = QotGetRT.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getRT(req);
        System.out.printf("Send QotGetRT: %d\n", seqNo);
    }

    @Override
    public void onReply_GetRT(MMAPI_Conn client, int nSerialNo, QotGetRT.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetRT failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetRT: %s\n", json);
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
Send QotGetRT: 3
Receive QotGetRT: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "rtList": [{
      "time": "2021-06-24 09:30:00",
      "minute": 570,
      "isBlank": false,
      "price": 584.0,
      "lastClosePrice": 582.5,
      "avgPrice": 584.0,
      "volume": "431600",
      "turnover": 2.520544E8,
      "timestamp": 1.6244982E9
    }, ... {
      "time": "2021-06-24 16:00:00",
      "minute": 960,
      "isBlank": false,
      "price": 583.0,
      "lastClosePrice": 582.5,
      "avgPrice": 583.4658532703611,
      "volume": "1197900",
      "turnover": 6.98392175E8,
      "timestamp": 1.6245216E9
    }]
  }
}
```









`moomoo::u32_t GetRT(const Qot_GetRT::Request &stReq);`  
`virtual void OnReply_GetRT(moomoo::u32_t nSerialNo, const Qot_GetRT::Response &stRsp) = 0;`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
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

        // subscribe first
        Qot_Sub::Request req;
        Qot_Sub::C2S *c2s = req.mutable_c2s();
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->add_subtypelist(Qot_Common::SubType::SubType_RT);
        c2s->set_isregorunregpush(true);
        c2s->set_issuborunsub(true);
        
        m_SubSerialNo = m_pQotApi->Sub(req);
        cout << "Request Sub SerialNo: " << m_SubSerialNo << endl;
    }

    virtual void OnReply_Sub(moomoo::u32_t nSerialNo, const Qot_Sub::Response &stRsp)
    {
        if(nSerialNo == m_SubSerialNo)
        {
            cout << "OnReply_Sub SerialNo: " << nSerialNo << endl;
            if(stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }        

            // construct request message
            Qot_GetRT::Request req;
            Qot_GetRT::C2S *c2s = req.mutable_c2s();
            Qot_Common::Security *sec = c2s->mutable_security();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

            m_GetRTSerialNo = m_pQotApi->GetRT(req);
            cout << "Request GetRT SerialNo: " << m_GetRTSerialNo << endl;
        }
    }

    virtual void OnReply_GetRT(moomoo::u32_t nSerialNo, const Qot_GetRT::Response &stRsp){
        if(nSerialNo == m_GetRTSerialNo)
        {
            cout << "OnReply_GetRT SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_SubSerialNo;
    moomoo::u32_t m_GetRTSerialNo;
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
Request Sub SerialNo: 3
OnReply_Sub SerialNo: 3
Request GetRT SerialNo: 4
OnReply_GetRT SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "rtList": [
   {
    "time": "2021-06-09 09:30:00",
    "minute": 570,
    "isBlank": false,
    "price": 600,
    "lastClosePrice": 601,
    "avgPrice": 600,
    "volume": "255100",
    "turnover": 153060000,
    "timestamp": 1623202200
   },
   {
    "time": "2021-06-09 09:31:00",
    "minute": 571,
    "isBlank": false,
    "price": 599.5,
    "lastClosePrice": 601,
    "avgPrice": 599.41146019278824,
    "volume": "305100",
    "turnover": 182730300,
    "timestamp": 1623202260
   },
...
   {
    "time": "2021-06-09 14:13:00",
    "minute": 853,
    "isBlank": false,
    "price": 600.5,
    "lastClosePrice": 601,
    "avgPrice": 602.188546883593,
    "volume": "1600",
    "turnover": 960850,
    "timestamp": 1623219180
   }
  ]
 }
}
```









`GetRT(req);`

- **Description**

  Obtain real-time tick-by-tick data for a specified stock. (Require
  real-time data subscription.)

- **Parameters**



``` protobuf
message C2S
{
    required Qot_Common.Security security = 1; //Security
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 3; //Stock name
    repeated Qot_Common.TimeShare rtList = 2; //Time Frame data struct
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
> - For Time Frame structure, refer to
>   [TimeShare](/moomoo-api-doc/en/quote/quote.html#3690)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetRT(){
    const { RetType } = Common
    const { SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();
    
    websocket.onlogin = (ret, msg)=>{
        if (ret) {
            websocket.Sub({
                c2s: {
                securityList: [
                    {
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                ],
                subTypeList: [ SubType.SubType_RT ], 
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true, 
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                        security: {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                    },
                };
                
                websocket.GetRT(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("RT: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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

            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("sub error:", error.retMsg);
                }
            });
        } else {
            console.log("start error", msg);
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
RT: errCode 0, retMsg , retType 0
{
  "security": {
    "market": 1,
    "code": "00700"
  },
  "rtList": [{
    "time": "2021-09-09 09:30:00",
    "minute": 570,
    "isBlank": false,
    "price": 509,
    "lastClosePrice": 524.5,
    "avgPrice": 509,
    "volume": "941800",
    "turnover": 479376200,
    "timestamp": 1631151000
  }, {
    "time": "2021-09-09 09:31:00",
    "minute": 571,
    "isBlank": false,
    "price": 506.5,
    "lastClosePrice": 524.5,
    "avgPrice": 507.88588572919383,
    "volume": "974700",
    "turnover": 493987100,
    "timestamp": 1631151060
  }, ..., {
    "time": "2021-09-09 09:32:00",
    "minute": 572,
    "isBlank": false,
    "price": 504,
    "lastClosePrice": 524.5,
    "avgPrice": 507.3999031165602,
    "volume": "416200",
    "turnover": 210248454,
    "timestamp": 1631151120
  },],
}
stop
```











Tips

- This API provides the function of obtaining real-time data at one
  time. If you need to obtain pushed data continuously, please refer to
  the [Real-time Time Frame
  Callback](/moomoo-api-doc/en/quote/update-rt.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).













