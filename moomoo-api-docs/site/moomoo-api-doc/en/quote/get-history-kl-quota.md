



# <a href="#4645" class="header-anchor">#</a> Get Details of Historical Candlestick Quota









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_history_kl_quota(get_detail=False)`

- **Description**

  Get usage details of historical candlestick quota

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
  <td style="text-align: left;">get_detail</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to return the detailed record of
  historical candlestick pulled.
  
    
  
  
   
  
  True: return.<br />
  False: not return.
  
  
  
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
  <td rowspan="2">data</td>
  <td>tuple</td>
  <td>If ret == RET_OK, historical candlestick quota is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Historical candlestick quota format as follows:

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
    <td style="text-align: left;">used_quota</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Used quota.
    
      
    
    
     
    
    How many stocks have been downloaded in the current period.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">remain_quota</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Remaining quota.</td>
    </tr>
    <tr>
    <td style="text-align: left;">detail_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Detailed records of historical candlestick
    data pulled, including stock code and pulling time.
    
      
    
    
     
    
    Data type of elements in the list is dict.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    - detail_list, the data column format is as follows
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
      <td style="text-align: left;">request_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">The time string of the last pull.
      
        
      
      
       
      
      yyyy-MM-dd HH:mm:ss.
      
      
      
      </td>
      </tr>
      </tbody>
      </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_history_kl_quota(get_detail=True)  # Setting True means that you need to return the detailed record of historical candlestick pulled
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
(2, 98,  {'code': 'HK.00123', 'name': 'YUEXIU PROPERTY', 'request_time': '2023-06-20 19:59:00'}, {'code': 'HK.00700', 'name': 'TENCENT', 'request_time': '2023-07-19 16:44:14'}])
```









## <a href="#4658" class="header-anchor">#</a> Qot_RequestHistoryKLQuota.proto

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3104





`uint RequestHistoryKLQuota(QotRequestHistoryKLQuota.Request req);`  
`virtual void OnReply_RequestHistoryKLQuota(FTAPI_Conn client, uint nSerialNo, QotRequestHistoryKLQuota.Response rsp);`

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Qot, FTSPI_Conn {
    FTAPI_Qot qot = new FTAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1);  //Set client information
        qot.SetConnCallback(this);  //Set connection callback
        qot.SetQotCallback(this);   //Set transaction callback
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        QotRequestHistoryKLQuota.C2S c2s = QotRequestHistoryKLQuota.C2S.CreateBuilder()
            .Build();
        QotRequestHistoryKLQuota.Request req = QotRequestHistoryKLQuota.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestHistoryKLQuota(req);
        Console.Write("Send QotRequestHistoryKLQuota: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_RequestHistoryKLQuota(FTAPI_Conn client, uint nSerialNo, QotRequestHistoryKLQuota.Response rsp) {
        Console.Write("Reply: QotRequestHistoryKLQuota: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("usedQuota: {0} \n", rsp.S2C.UsedQuota);
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
Qot onInitConnect: ret=0 desc= connID=6826782079934349591
Send QotRequestHistoryKLQuota: 3
Reply: QotRequestHistoryKLQuota: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  usedQuota: 4
  remainQuota: 296
}

usedQuota: 4
```









`int requestHistoryKLQuota(QotRequestHistoryKLQuota.Request req);`  
`void onReply_RequestHistoryKLQuota(FTAPI_Conn client, int nSerialNo, QotRequestHistoryKLQuota.Response rsp);`

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements FTSPI_Qot, FTSPI_Conn {
    FTAPI_Conn_Qot qot = new FTAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1);  //Set client information
        qot.setConnSpi(this);  //Set connection callback
        qot.setQotSpi(this);   //Set transaction callback
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

        QotRequestHistoryKLQuota.C2S c2s = QotRequestHistoryKLQuota.C2S.newBuilder()
            .build();
        QotRequestHistoryKLQuota.Request req = QotRequestHistoryKLQuota.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestHistoryKLQuota(req);
        System.out.printf("Send QotRequestHistoryKLQuota: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestHistoryKLQuota(FTAPI_Conn client, int nSerialNo, QotRequestHistoryKLQuota.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestHistoryKLQuota failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestHistoryKLQuota: %s\n", json);
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
Send QotRequestHistoryKLQuota: 2
Receive QotRequestHistoryKLQuota: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "usedQuota": 0,
    "remainQuota": 300
  }
}
```









`Futu::u32_t RequestHistoryKLQuota(const Qot_RequestHistoryKLQuota::Request &stReq);`  
`virtual void OnReply_RequestHistoryKLQuota(Futu::u32_t nSerialNo, const Qot_RequestHistoryKLQuota::Response &stRsp) = 0;`

- **Description**

  Get usage details of historical candlestick quota, that is, how many
  stocks have been downloaded in the current period

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
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
        Qot_RequestHistoryKLQuota::Request req;
        Qot_RequestHistoryKLQuota::C2S *c2s = req.mutable_c2s();

        m_RequestHistoryKLQuotaSerialNo = m_pQotApi->RequestHistoryKLQuota(req);
        cout << "Request RequestHistoryKLQuota SerialNo: " << m_RequestHistoryKLQuotaSerialNo << endl;
    }

    virtual void OnReply_RequestHistoryKLQuota(Futu::u32_t nSerialNo, const Qot_RequestHistoryKLQuota::Response &stRsp){
        if(nSerialNo == m_RequestHistoryKLQuotaSerialNo)
        {
            cout << "OnReply_RequestHistoryKLQuota SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_RequestHistoryKLQuotaSerialNo;
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
Request RequestHistoryKLQuota SerialNo: 4
OnReply_RequestHistoryKLQuota SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "usedQuota": 4,
  "remainQuota": 296
 }
}
```









`RequestHistoryKLQuota(req);`

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotRequestHistoryKLQuota(){
    const { RetType } = Common
    const {  } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    bGetDetail: true,
                },
            };

            websocket.RequestHistoryKLQuota(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("HistoryKLQuota: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
HistoryKLQuota: errCode 0, retMsg , retType 0
{
  "usedQuota": 1,
  "remainQuota": 99,
  "detailList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "requestTime": "2021-09-10 14:17:17",
    "requestTimeStamp": "1631254637"
  }]
}
stop
```











Interface Restrictions

- We will issue historical candlestick quotas based on the assets and
  tradings of your account. Therefore, you can only obtain historical
  candlestick data for a limited number of stocks within 30 days. For
  specific rules, please refer to [Subscription Quota & Historical
  Candlestick Quota](/moomoo-api-doc/en/intro/authority.html#9123).
- The historical candlestick quota you consume on that day will be
  automatically released after 30 days.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_history_kl_quota(get_detail=False)`

- **Description**

  Get usage details of historical candlestick quota

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
  <td style="text-align: left;">get_detail</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to return the detailed record of
  historical candlestick pulled.
  
    
  
  
   
  
  True: return.<br />
  False: not return.
  
  
  
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
  <td rowspan="2">data</td>
  <td>tuple</td>
  <td>If ret == RET_OK, historical candlestick quota is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Historical candlestick quota format as follows:

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
    <td style="text-align: left;">used_quota</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Used quota.
    
      
    
    
     
    
    How many stocks have been downloaded in the current period.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">remain_quota</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Remaining quota.</td>
    </tr>
    <tr>
    <td style="text-align: left;">detail_list</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Detailed records of historical candlestick
    data pulled, including stock code and pulling time.
    
      
    
    
     
    
    Data type of elements in the list is dict.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    - detail_list, the data column format is as follows
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
      <td style="text-align: left;">request_time</td>
      <td style="text-align: left;">str</td>
      <td style="text-align: left;">The time string of the last pull.
      
        
      
      
       
      
      yyyy-MM-dd HH:mm:ss.
      
      
      
      </td>
      </tr>
      </tbody>
      </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_history_kl_quota(get_detail=True)  # Setting True means that you need to return the detailed record of historical candlestick pulled
if ret == RET_OK:
    print(data)
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
(2, 98,  {'code': 'HK.00123', 'name': 'YUEXIU PROPERTY', 'request_time': '2023-06-20 19:59:00'}, {'code': 'HK.00700', 'name': 'TENCENT', 'request_time': '2023-07-19 16:44:14'}])
```









## <a href="#4658-2" class="header-anchor">#</a> Qot_RequestHistoryKLQuota.proto

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3104





`uint RequestHistoryKLQuota(QotRequestHistoryKLQuota.Request req);`  
`virtual void OnReply_RequestHistoryKLQuota(MMAPI_Conn client, uint nSerialNo, QotRequestHistoryKLQuota.Response rsp);`

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf

message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Qot, MMSPI_Conn {
    MMAPI_Qot qot = new MMAPI_Qot();

    public Program() {
        qot.SetClientInfo("csharp", 1);  //Set client information
        qot.SetConnCallback(this);  //Set connection callback
        qot.SetQotCallback(this);   //Set transaction callback
    }

    public void Start() {
        qot.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Qot onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        QotRequestHistoryKLQuota.C2S c2s = QotRequestHistoryKLQuota.C2S.CreateBuilder()
            .Build();
        QotRequestHistoryKLQuota.Request req = QotRequestHistoryKLQuota.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestHistoryKLQuota(req);
        Console.Write("Send QotRequestHistoryKLQuota: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_RequestHistoryKLQuota(MMAPI_Conn client, uint nSerialNo, QotRequestHistoryKLQuota.Response rsp) {
        Console.Write("Reply: QotRequestHistoryKLQuota: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("usedQuota: {0} \n", rsp.S2C.UsedQuota);
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
Qot onInitConnect: ret=0 desc= connID=6826782079934349591
Send QotRequestHistoryKLQuota: 3
Reply: QotRequestHistoryKLQuota: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  usedQuota: 4
  remainQuota: 296
}

usedQuota: 4
```









`int requestHistoryKLQuota(QotRequestHistoryKLQuota.Request req);`  
`void onReply_RequestHistoryKLQuota(MMAPI_Conn client, int nSerialNo, QotRequestHistoryKLQuota.Response rsp);`

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class QotDemo implements MMSPI_Qot, MMSPI_Conn {
    MMAPI_Conn_Qot qot = new MMAPI_Conn_Qot();

    public QotDemo() {
        qot.setClientInfo("javaclient", 1);  //Set client information
        qot.setConnSpi(this);  //Set connection callback
        qot.setQotSpi(this);   //Set transaction callback
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

        QotRequestHistoryKLQuota.C2S c2s = QotRequestHistoryKLQuota.C2S.newBuilder()
            .build();
        QotRequestHistoryKLQuota.Request req = QotRequestHistoryKLQuota.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestHistoryKLQuota(req);
        System.out.printf("Send QotRequestHistoryKLQuota: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestHistoryKLQuota(MMAPI_Conn client, int nSerialNo, QotRequestHistoryKLQuota.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestHistoryKLQuota failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestHistoryKLQuota: %s\n", json);
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
Send QotRequestHistoryKLQuota: 2
Receive QotRequestHistoryKLQuota: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "usedQuota": 0,
    "remainQuota": 300
  }
}
```









`moomoo::u32_t RequestHistoryKLQuota(const Qot_RequestHistoryKLQuota::Request &stReq);`  
`virtual void OnReply_RequestHistoryKLQuota(moomoo::u32_t nSerialNo, const Qot_RequestHistoryKLQuota::Response &stRsp) = 0;`

- **Description**

  Get usage details of historical candlestick quota, that is, how many
  stocks have been downloaded in the current period

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
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
        Qot_RequestHistoryKLQuota::Request req;
        Qot_RequestHistoryKLQuota::C2S *c2s = req.mutable_c2s();

        m_RequestHistoryKLQuotaSerialNo = m_pQotApi->RequestHistoryKLQuota(req);
        cout << "Request RequestHistoryKLQuota SerialNo: " << m_RequestHistoryKLQuotaSerialNo << endl;
    }

    virtual void OnReply_RequestHistoryKLQuota(moomoo::u32_t nSerialNo, const Qot_RequestHistoryKLQuota::Response &stRsp){
        if(nSerialNo == m_RequestHistoryKLQuotaSerialNo)
        {
            cout << "OnReply_RequestHistoryKLQuota SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_RequestHistoryKLQuotaSerialNo;
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
Request RequestHistoryKLQuota SerialNo: 4
OnReply_RequestHistoryKLQuota SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "usedQuota": 4,
  "remainQuota": 296
 }
}
```









`RequestHistoryKLQuota(req);`

- **Description**

  Get usage details of historical candlestick quota

- **Parameters**



``` protobuf
message C2S
{
    optional bool bGetDetail = 2;    //Whether to return the detailed record of historical candlestick pulled
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message DetailItem
{
    required Qot_Common.Security security = 1; //Pulled stocks
    optional string name = 4; //Stock name
    required string requestTime = 2; //Pulled time string (Format: yyyy-MM-dd HH:mm:ss)
    optional int64 requestTimeStamp = 3; //Pulled timestamp
}

message S2C
{
    required int32 usedQuota = 1;          //The used quota, how many stocks have been downloaded in the current period.
    required int32 remainQuota = 2;       //Remaining quota
    repeated DetailItem detailList = 3;   //The download time of each pulled stock
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotRequestHistoryKLQuota(){
    const { RetType } = Common
    const {  } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    bGetDetail: true,
                },
            };

            websocket.RequestHistoryKLQuota(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("HistoryKLQuota: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
HistoryKLQuota: errCode 0, retMsg , retType 0
{
  "usedQuota": 1,
  "remainQuota": 99,
  "detailList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "requestTime": "2021-09-10 14:17:17",
    "requestTimeStamp": "1631254637"
  }]
}
stop
```











Interface Restrictions

- We will issue historical candlestick quotas based on the assets and
  tradings of your account. Therefore, you can only obtain historical
  candlestick data for a limited number of stocks within 30 days. For
  specific rules, please refer to [Subscription Quota & Historical
  Candlestick Quota](/moomoo-api-doc/en/intro/authority.html#9123).
- The historical candlestick quota you consume on that day will be
  automatically released after 30 days.













