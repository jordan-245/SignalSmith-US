



# <a href="#1938" class="header-anchor">#</a> Get Adjustment Factor









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_rehab(code)`

- **Description**

  Get the stock adjustment factor

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
  <td>If ret == RET_OK, data for adjustment is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data for adjustment format as follows:

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
    <td style="text-align: left;">ex_div_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Ex-dividend date.</td>
    </tr>
    <tr>
    <td style="text-align: left;">split_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Split numerator.
    
      
    
    
     
    
    split_ratio= split numerator / split denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">split_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Split dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">join_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Joint numerator.
    
      
    
    
     
    
    split_ratio= joint numerator / joint denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">join_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Joint dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">split_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Split ratio.
    
      
    
    
     
    
    - When 5 shares are joined into 1 share, the joint numerator = 5, the
    joint denominator = 1, split_ratio = joint numerator / joint
    denominator= 5/1.<br />
    - When 1 share is split into 5 shares, the split numerator =1, the split
    denominator =5, split_ratio= split numerator /split denominator =1/5.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">per_cash_div</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend per share.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bounce_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bounce numerator.
    
      
    
    
     
    
    per_share_div_ratio= bounce numerator / bounce denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">bounce_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bounce dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">per_share_div_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bounce ratio.
    
      
    
    
     
    
    - When the company has bonus shares and 1 share gives 5 shares, the
    bounce numerator = 1, the bounce denominator = 5, per_share_div_ratio =
    bounce numerator / bounce denominator = 1/5.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">transfer_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion numerator.
    
      
    
    
     
    
    per_share_trans_ratio= transfer_base / bounce denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">transfer_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">per_share_trans_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion ratio.
    
      
    
    
     
    
    - When 10 share is converted into 3 shares, the conversion numerator =
    10, the conversion denominator = 3, per_share_trans_ratio = conversion
    numerator / conversion numerator = 10/3.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">allot_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Allotment numerator.
    
      
    
    
     
    
    allotment ratio = allotment numerator / allotment denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">allot_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Allotment dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">allotment_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Allotment ratio.
    
      
    
    
     
    
    - When 5 shares are allocated to 1 share, the allotment numerator = 5,
    the allotment denominator = 1, allotment_ratio = allotment numerator /
    allotment denominator = 5/1.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">allotment_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Issuance price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">add_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance numerator.
    
      
    
    
     
    
    stk_spo_ratio = additional issuance numerator / additional issuance
    denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">add_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stk_spo_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance ratio.
    
      
    
    
     
    
    - When 1 additional share issues 5 shares, the additional issuance
    numerator = 1, the additional issuance denominator = 5, stk_spo_ratio =
    additional issuance numerator / additional issuance denominator = 1/5.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stk_spo_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">spin_off_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spin-off numerator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">spin_off_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spin-off dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">spin_off_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spin-off ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">forward_adj_factorA</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Forward adjustment factor A.</td>
    </tr>
    <tr>
    <td style="text-align: left;">forward_adj_factorB</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Forward adjustment factor B.</td>
    </tr>
    <tr>
    <td style="text-align: left;">backward_adj_factorA</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Backward adjustment factor A.</td>
    </tr>
    <tr>
    <td style="text-align: left;">backward_adj_factorB</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Backward adjustment factor B.</td>
    </tr>
    </tbody>
    </table>

    Price after forward adjustment = price before forward adjustment \*
    Forward adjustment factor A + Forward adjustment factor B  
    Price after backward adjustment = price before backward adjustment
    \* Backward adjustment factor A + Backward adjustment factor B

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_rehab("HK.00700")
if ret == RET_OK:
    print(data)
    print(data['ex_div_date'][0]) # Take the first ex-dividend date
    print(data['ex_div_date'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    ex_div_date  split_ratio  per_cash_div  per_share_div_ratio  per_share_trans_ratio  allotment_ratio  allotment_price  stk_spo_ratio  stk_spo_price  spin_off_base     spin_off_ert     spin_off_ratio    forward_adj_factorA  forward_adj_factorB  backward_adj_factorA  backward_adj_factorB
0   2005-04-19          NaN          0.07                  NaN                    NaN              NaN              NaN            NaN            NaN          NaN      NaN        NaN        1.0                -0.07                   1.0                  0.07
..         ...          ...           ...                  ...                    ...              ...              ...            ...            ...                  ...                  ...                   ...                   ...
15  2019-05-17          NaN          1.00                  NaN                    NaN              NaN              NaN            NaN            NaN         NaN        NaN           NaN         1.0                -1.00                   1.0                  1.00

[16 rows x 16 columns]
2005-04-19
['2005-04-19', '2006-05-15', '2007-05-09', '2008-05-06', '2009-05-06', '2010-05-05', '2011-05-03', '2012-05-18', '2013-05-20', '2014-05-15', '2014-05-16', '2015-05-15', '2016-05-20', '2017-05-19', '2018-05-18', '2019-05-17']
```









## <a href="#6618" class="header-anchor">#</a> Qot_RequestRehab.proto

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3105





`uint RequestRehab(QotRequestRehab.Request req);`  
`virtual void OnReply_RequestRehab(FTAPI_Conn client, uint nSerialNo, QotRequestRehab.Response rsp);`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
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
        QotRequestRehab.C2S c2s = QotRequestRehab.C2S.CreateBuilder()
                .SetSecurity(sec)
            .Build();
        QotRequestRehab.Request req = QotRequestRehab.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestRehab(req);
        Console.Write("Send QotRequestRehab: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_RequestRehab(FTAPI_Conn client, uint nSerialNo, QotRequestRehab.Response rsp) {
        Console.Write("Reply: QotRequestRehab: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("fwdFactorA: {0}\n",
            rsp.S2C.RehabListList[0].FwdFactorA);
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
Qot onInitConnect: ret=0 desc= connID=6819078887638898428
Send QotRequestRehab: 3
Reply: QotRequestRehab: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  rehabList {
    time: "2005-04-19"
    companyActFlag: 64
    fwdFactorA: 1
    fwdFactorB: -0.07
    bwdFactorA: 1
    bwdFactorB: 0.07
    dividend: 0.07
    timestamp: 1113840000
  }
  ...
  rehabList {
    time: "2021-05-24"
    companyActFlag: 64
    fwdFactorA: 1
    fwdFactorB: -1.6
    bwdFactorA: 1
    bwdFactorB: 1.6
    dividend: 1.6
    timestamp: 1621785600
  }
}

fwdFactorA: 1
```









`int requestRehab(QotRequestRehab.Request req);`  
`void onReply_RequestRehab(FTAPI_Conn client, int nSerialNo, QotRequestRehab.Response rsp);`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
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
        QotRequestRehab.C2S c2s = QotRequestRehab.C2S.newBuilder()
                .setSecurity(sec)
            .build();
        QotRequestRehab.Request req = QotRequestRehab.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestRehab(req);
        System.out.printf("Send QotRequestRehab: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestRehab(FTAPI_Conn client, int nSerialNo, QotRequestRehab.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestRehab failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestRehab: %s\n", json);
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
Send QotRequestRehab: 2
Receive QotRequestRehab: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "rehabList": [{
      "time": "2005-04-19",
      "companyActFlag": "64",
      "fwdFactorA": 1.0,
      "fwdFactorB": -0.07,
      "bwdFactorA": 1.0,
      "bwdFactorB": 0.07,
      "dividend": 0.07,
      "timestamp": 1.11384E9
    }, ... {
      "time": "2021-05-24",
      "companyActFlag": "64",
      "fwdFactorA": 1.0,
      "fwdFactorB": -1.6,
      "bwdFactorA": 1.0,
      "bwdFactorB": 1.6,
      "dividend": 1.6,
      "timestamp": 1.6217856E9
    }]
  }
}
```









`Futu::u32_t RequestRehab(const Qot_RequestRehab::Request &stReq);`  
`virtual void OnReply_RequestRehab(Futu::u32_t nSerialNo, const Qot_RequestRehab::Response &stRsp) = 0;`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
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
        Qot_RequestRehab::Request req;
        Qot_RequestRehab::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_RequestRehabSerialNo = m_pQotApi->RequestRehab(req);
        cout << "Request RequestRehab SerialNo: " << m_RequestRehabSerialNo << endl;
    }

    virtual void OnReply_RequestRehab(Futu::u32_t nSerialNo, const Qot_RequestRehab::Response &stRsp){
        if(nSerialNo == m_RequestRehabSerialNo)
        {
            cout << "OnReply_RequestRehab SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_RequestRehabSerialNo;
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
Request RequestRehab SerialNo: 4
OnReply_RequestRehab SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "rehabList": [
   {
    "time": "2005-04-19",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -0.07,
    "bwdFactorA": 1,
    "bwdFactorB": 0.07,
    "dividend": 0.07,
    "timestamp": 1113840000
   },
...
   {
    "time": "2021-05-24",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -1.6,
    "bwdFactorA": 1,
    "bwdFactorB": 1.6,
    "dividend": 1.6,
    "timestamp": 1621785600
   }
  ]
 }
}
```









`RequestRehab(req);`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotRequestRehab(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                },
            };

            websocket.RequestRehab(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("OwnerPlate: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
OwnerPlate: errCode 0, retMsg , retType 0
{
  "rehabList": [{
    "time": "2005-04-19",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -0.07,
    "bwdFactorA": 1,
    "bwdFactorB": 0.07,
    "dividend": 0.07,
    "timestamp": 1113840000
  }, {
    "time": "2006-05-15",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -0.08,
    "bwdFactorA": 1,
    "bwdFactorB": 0.08,
    "dividend": 0.08,
    "timestamp": 1147622400
  }, ..., {
    "time": "2021-05-24",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -1.6,
    "bwdFactorA": 1,
    "bwdFactorB": 1.6,
    "dividend": 1.6,
    "timestamp": 1621785600
  }]
}
stop
```











Interface Limitations

- A maximum of 60 requests per 30 seconds











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_rehab(code)`

- **Description**

  Get the stock adjustment factor

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
  <td>If ret == RET_OK, data for adjustment is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Data for adjustment format as follows:

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
    <td style="text-align: left;">ex_div_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Ex-dividend date.</td>
    </tr>
    <tr>
    <td style="text-align: left;">split_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Split numerator.
    
      
    
    
     
    
    split_ratio= split numerator / split denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">split_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Split dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">join_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Joint numerator.
    
      
    
    
     
    
    split_ratio= joint numerator / joint denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">join_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Joint dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">split_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Split ratio.
    
      
    
    
     
    
    - When 5 shares are joined into 1 share, the joint numerator = 5, the
    joint denominator = 1, split_ratio = joint numerator / joint
    denominator= 5/1.<br />
    - When 1 share is split into 5 shares, the split numerator =1, the split
    denominator =5, split_ratio= split numerator /split denominator =1/5.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">per_cash_div</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Dividend per share.</td>
    </tr>
    <tr>
    <td style="text-align: left;">bounce_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bounce numerator.
    
      
    
    
     
    
    per_share_div_ratio= bounce numerator / bounce denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">bounce_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bounce dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">per_share_div_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Bounce ratio.
    
      
    
    
     
    
    - When the company has bonus shares and 1 share gives 5 shares, the
    bounce numerator = 1, the bounce denominator = 5, per_share_div_ratio =
    bounce numerator / bounce denominator = 1/5.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">transfer_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion numerator.
    
      
    
    
     
    
    per_share_trans_ratio= transfer_base / bounce denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">transfer_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">per_share_trans_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Conversion ratio.
    
      
    
    
     
    
    - When 10 share is converted into 3 shares, the conversion numerator =
    10, the conversion denominator = 3, per_share_trans_ratio = conversion
    numerator / conversion numerator = 10/3.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">allot_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Allotment numerator.
    
      
    
    
     
    
    allotment ratio = allotment numerator / allotment denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">allot_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Allotment dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">allotment_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Allotment ratio.
    
      
    
    
     
    
    - When 5 shares are allocated to 1 share, the allotment numerator = 5,
    the allotment denominator = 1, allotment_ratio = allotment numerator /
    allotment denominator = 5/1.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">allotment_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Issuance price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">add_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance numerator.
    
      
    
    
     
    
    stk_spo_ratio = additional issuance numerator / additional issuance
    denominator
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">add_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stk_spo_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance ratio.
    
      
    
    
     
    
    - When 1 additional share issues 5 shares, the additional issuance
    numerator = 1, the additional issuance denominator = 5, stk_spo_ratio =
    additional issuance numerator / additional issuance denominator = 1/5.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">stk_spo_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Additional issuance price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">spin_off_base</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spin-off numerator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">spin_off_ert</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spin-off dominator.</td>
    </tr>
    <tr>
    <td style="text-align: left;">spin_off_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spin-off ratio.</td>
    </tr>
    <tr>
    <td style="text-align: left;">forward_adj_factorA</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Forward adjustment factor A.</td>
    </tr>
    <tr>
    <td style="text-align: left;">forward_adj_factorB</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Forward adjustment factor B.</td>
    </tr>
    <tr>
    <td style="text-align: left;">backward_adj_factorA</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Backward adjustment factor A.</td>
    </tr>
    <tr>
    <td style="text-align: left;">backward_adj_factorB</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Backward adjustment factor B.</td>
    </tr>
    </tbody>
    </table>

    Price after forward adjustment = price before forward adjustment \*
    Forward adjustment factor A + Forward adjustment factor B  
    Price after backward adjustment = price before backward adjustment
    \* Backward adjustment factor A + Backward adjustment factor B

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_rehab("HK.00700")
if ret == RET_OK:
    print(data)
    print(data['ex_div_date'][0]) # Take the first ex-dividend date
    print(data['ex_div_date'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    ex_div_date  split_ratio  per_cash_div  per_share_div_ratio  per_share_trans_ratio  allotment_ratio  allotment_price  stk_spo_ratio  stk_spo_price  spin_off_base      spin_off_ert     spin_off_ratio   forward_adj_factorA  forward_adj_factorB  backward_adj_factorA  backward_adj_factorB
0   2005-04-19          NaN          0.07                  NaN                    NaN              NaN              NaN            NaN            NaN          NaN       NaN       NaN        1.0                -0.07                   1.0                  0.07
..         ...          ...           ...                  ...                    ...              ...              ...            ...            ...                  ...                  ...                   ...                   ...
15  2019-05-17          NaN          1.00                  NaN                    NaN              NaN              NaN            NaN            NaN         NaN         NaN         NaN         1.0                -1.00                   1.0                  1.00

[16 rows x 16 columns]
2005-04-19
['2005-04-19', '2006-05-15', '2007-05-09', '2008-05-06', '2009-05-06', '2010-05-05', '2011-05-03', '2012-05-18', '2013-05-20', '2014-05-15', '2014-05-16', '2015-05-15', '2016-05-20', '2017-05-19', '2018-05-18', '2019-05-17']
```









## <a href="#6618-2" class="header-anchor">#</a> Qot_RequestRehab.proto

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3105





`uint RequestRehab(QotRequestRehab.Request req);`  
`virtual void OnReply_RequestRehab(MMAPI_Conn client, uint nSerialNo, QotRequestRehab.Response rsp);`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
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
        QotRequestRehab.C2S c2s = QotRequestRehab.C2S.CreateBuilder()
                .SetSecurity(sec)
            .Build();
        QotRequestRehab.Request req = QotRequestRehab.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestRehab(req);
        Console.Write("Send QotRequestRehab: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    
    public void OnReply_RequestRehab(MMAPI_Conn client, uint nSerialNo, QotRequestRehab.Response rsp) {
        Console.Write("Reply: QotRequestRehab: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("fwdFactorA: {0}\n",
            rsp.S2C.RehabListList[0].FwdFactorA);
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
Qot onInitConnect: ret=0 desc= connID=6819078887638898428
Send QotRequestRehab: 3
Reply: QotRequestRehab: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  rehabList {
    time: "2005-04-19"
    companyActFlag: 64
    fwdFactorA: 1
    fwdFactorB: -0.07
    bwdFactorA: 1
    bwdFactorB: 0.07
    dividend: 0.07
    timestamp: 1113840000
  }
  ...
  rehabList {
    time: "2021-05-24"
    companyActFlag: 64
    fwdFactorA: 1
    fwdFactorB: -1.6
    bwdFactorA: 1
    bwdFactorB: 1.6
    dividend: 1.6
    timestamp: 1621785600
  }
}

fwdFactorA: 1
```









`int requestRehab(QotRequestRehab.Request req);`  
`void onReply_RequestRehab(MMAPI_Conn client, int nSerialNo, QotRequestRehab.Response rsp);`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
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
        QotRequestRehab.C2S c2s = QotRequestRehab.C2S.newBuilder()
                .setSecurity(sec)
            .build();
        QotRequestRehab.Request req = QotRequestRehab.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestRehab(req);
        System.out.printf("Send QotRequestRehab: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestRehab(MMAPI_Conn client, int nSerialNo, QotRequestRehab.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestRehab failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestRehab: %s\n", json);
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
Send QotRequestRehab: 2
Receive QotRequestRehab: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "rehabList": [{
      "time": "2005-04-19",
      "companyActFlag": "64",
      "fwdFactorA": 1.0,
      "fwdFactorB": -0.07,
      "bwdFactorA": 1.0,
      "bwdFactorB": 0.07,
      "dividend": 0.07,
      "timestamp": 1.11384E9
    }, ... {
      "time": "2021-05-24",
      "companyActFlag": "64",
      "fwdFactorA": 1.0,
      "fwdFactorB": -1.6,
      "bwdFactorA": 1.0,
      "bwdFactorB": 1.6,
      "dividend": 1.6,
      "timestamp": 1.6217856E9
    }]
  }
}
```









`moomoo::u32_t RequestRehab(const Qot_RequestRehab::Request &stReq);`  
`virtual void OnReply_RequestRehab(moomoo::u32_t nSerialNo, const Qot_RequestRehab::Response &stRsp) = 0;`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
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
        Qot_RequestRehab::Request req;
        Qot_RequestRehab::C2S *c2s = req.mutable_c2s();
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_RequestRehabSerialNo = m_pQotApi->RequestRehab(req);
        cout << "Request RequestRehab SerialNo: " << m_RequestRehabSerialNo << endl;
    }

    virtual void OnReply_RequestRehab(moomoo::u32_t nSerialNo, const Qot_RequestRehab::Response &stRsp){
        if(nSerialNo == m_RequestRehabSerialNo)
        {
            cout << "OnReply_RequestRehab SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_RequestRehabSerialNo;
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
Request RequestRehab SerialNo: 4
OnReply_RequestRehab SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "rehabList": [
   {
    "time": "2005-04-19",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -0.07,
    "bwdFactorA": 1,
    "bwdFactorB": 0.07,
    "dividend": 0.07,
    "timestamp": 1113840000
   },
...
   {
    "time": "2021-05-24",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -1.6,
    "bwdFactorA": 1,
    "bwdFactorB": 1.6,
    "dividend": 1.6,
    "timestamp": 1621785600
   }
  ]
 }
}
```









`RequestRehab(req);`

- **Description**

  Get the stock adjustment factor

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
    repeated Qot_Common.Rehab rehabList = 1; //adjustment information
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For adjustment struct, refer to
>   [Rehab](/moomoo-api-doc/en/quote/quote.html#7728)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotRequestRehab(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    security:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                },
            };

            websocket.RequestRehab(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("OwnerPlate: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
OwnerPlate: errCode 0, retMsg , retType 0
{
  "rehabList": [{
    "time": "2005-04-19",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -0.07,
    "bwdFactorA": 1,
    "bwdFactorB": 0.07,
    "dividend": 0.07,
    "timestamp": 1113840000
  }, {
    "time": "2006-05-15",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -0.08,
    "bwdFactorA": 1,
    "bwdFactorB": 0.08,
    "dividend": 0.08,
    "timestamp": 1147622400
  }, ..., {
    "time": "2021-05-24",
    "companyActFlag": "64",
    "fwdFactorA": 1,
    "fwdFactorB": -1.6,
    "bwdFactorA": 1,
    "bwdFactorB": 1.6,
    "dividend": 1.6,
    "timestamp": 1621785600
  }]
}
stop
```











Interface Limitations

- A maximum of 60 requests per 30 seconds













