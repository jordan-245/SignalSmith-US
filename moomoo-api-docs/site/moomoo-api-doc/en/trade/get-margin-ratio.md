



# <a href="#5120" class="header-anchor">#</a> Get Margin Data









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_margin_ratio(code_list)`

- **Description**

  Query the margin data of stocks.

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
  <td style="text-align: left;">code_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Stock list.
  
    
  
  
   
  
  Up to 100 targets can be requested each time.<br />
  Data type of elements in the list is str.
  
  
  
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
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, margin data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Margin data format as follows:
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
    <td style="text-align: left;">Stock code</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_long_permit</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is marginable trading allowed.</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_short_permit</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is shortable trading allowed.</td>
    </tr>
    <tr>
    <td style="text-align: left;">short_pool_remain</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short pool remaining.
    
      
    
    
     
    
    unit: shares.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_fee_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Borrow rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">alert_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable alert margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">alert_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Shortable alert margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">im_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable initial margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">im_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Shortable initial margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mcm_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable margin call margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mcm_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Shortable margin call margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mm_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable maintenance margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mm_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable maintenance margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_margin_ratio(code_list=['HK.00700','HK.09988'])  
if ret == RET_OK:
    print(data)
    print(data['is_long_permit'][0])  # Get whether marginable trading allowed for the first stock
    print(data['im_short_ratio'].values.tolist())  # Convert to list
else:
    print('error:', data)
trd_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
       code  is_long_permit  is_short_permit  short_pool_remain  short_fee_rate  alert_long_ratio  alert_short_ratio  im_long_ratio  im_short_ratio  mcm_long_ratio  mcm_short_ratio  mm_long_ratio  mm_short_ratio
0  HK.00700            True             True          1826900.0            0.89              33.0               56.0           35.0            60.0            32.0             53.0           25.0            40.0
1  HK.09988            True             True          1150600.0            0.95              48.0               46.0           50.0            50.0            47.0             43.0           40.0            30.0
True
[60.0, 50.0]
```









## <a href="#4388" class="header-anchor">#</a> Trd_GetMarginRatio.proto

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2223





`uint GetMarginRatio(TrdGetMarginRatio.Request req);`  
`virtual void OnReply_GetMarginRatio(FTAPI_Conn client, uint nSerialNo, TrdGetMarginRatio.Response rsp);`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1);  //设置客户端信息
        trd.SetConnCallback(this);  //设置连接回调
        trd.SetTrdCallback(this);   //设置交易回调
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.CreateBuilder()
                .SetAccID(281756457888247915L)
                .SetTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .SetTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .Build();
        QotCommon.Security security = QotCommon.Security.CreateBuilder()
                .SetCode("00700")
                .SetMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .Build();
        TrdGetMarginRatio.C2S c2s = TrdGetMarginRatio.C2S.CreateBuilder()
                .SetHeader(header)
                .AddSecurityList(security)
                .Build();

        TrdGetMarginRatio.Request req = TrdGetMarginRatio.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetMarginRatio(req);
        Console.Write("Send TrdGetMarginRatio: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetMarginRatio(FTAPI_Conn client, uint nSerialNo, TrdGetMarginRatio.Response rsp)
    {
        Console.Write("Reply: TrdGetMarginRatio: {0}\n", nSerialNo);
        Console.Write("accID: {0}\n", rsp.S2C.Header.AccID);
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
Trd onInitConnect: ret=0 desc= connID=6826814786778581486
Send TrdGetMarginRatio: 3
Reply: TrdGetMarginRatio: 3
accID: 281756457888247915
```









`int getMarginRatio(TrdGetMarginRatio.Request req);`  
`void onReply_GetMarginRatio(FTAPI_Conn client, int nSerialNo, TrdGetMarginRatio.Response rsp);`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1);  //设置客户端信息
        trd.setConnSpi(this);  //设置连接回调
        trd.setTrdSpi(this);   //设置交易回调
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.newBuilder()
                .setAccID(281756457888247915L)
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        QotCommon.Security security = QotCommon.Security.newBuilder()
                .setCode("00700")
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .build();
        TrdGetMarginRatio.C2S c2s = TrdGetMarginRatio.C2S.newBuilder()
                .setHeader(header)
                .addSecurityList(security)
                .build();
        TrdGetMarginRatio.Request req = TrdGetMarginRatio.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getMarginRatio(req);
        System.out.printf("Send TrdGetMarginRatio: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetMarginRatio(FTAPI_Conn client, int nSerialNo, TrdGetMarginRatio.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetMarginRatio failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetMarginRatio: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
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





- **Output**



``` text
Send TrdGetMarginRatio: 2
Receive TrdGetMarginRatio: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "marginRatioInfoList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "isLongPermit": true,
      "isShortPermit": true,
      "shortPoolRemain": 1987700.0,
      "shortFeeRate": 0.9,
      "alertLongRatio": 33.0,
      "alertShortRatio": 56.00000000000001,
      "imLongRatio": 35.0,
      "imShortRatio": 60.0,
      "mcmLongRatio": 32.0,
      "mcmShortRatio": 53.0,
      "mmLongRatio": 25.0,
      "mmShortRatio": 40.0
    }]
  }
}
```









`Futu::u32_t GetMarginRatio(const Trd_GetMarginRatio::Request &stReq);`  
`virtual void OnReply_GetMarginRatio(Futu::u32_t nSerialNo, const Trd_GetMarginRatio::Response &stRsp) = 0;`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
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
        m_pTrdApi = FTAPI::CreateTrdApi();
        m_pTrdApi->RegisterTrdSpi(this);
        m_pTrdApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pTrdApi != nullptr)
        {
            m_pTrdApi->UnregisterTrdSpi();
            m_pTrdApi->UnregisterConnSpi();
            FTAPI::ReleaseTrdApi(m_pTrdApi);
            m_pTrdApi = nullptr;
        }
    }

    void Start() {
        m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(FTAPI_Conn* pConn, Futu::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Trd_GetMarginRatio::Request req;
        Trd_GetMarginRatio::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetMarginRatioSerialNo = m_pTrdApi->GetMarginRatio(req);
        cout << "Request GetMarginRatio SerialNo: " << m_GetMarginRatioSerialNo << endl;
    }

    virtual void OnReply_GetMarginRatio(Futu::u32_t nSerialNo, const Trd_GetMarginRatio::Response &stRsp){
        if(nSerialNo == m_GetMarginRatioSerialNo)
        {
            cout << "OnReply_GetMarginRatio SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_PlaceOrderSerialNo;
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
Request GetMarginRatio SerialNo: 4
OnReply_GetMarginRatio SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "marginRatioInfoList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "isLongPermit": true,
    "isShortPermit": true,
    "shortPoolRemain": 1860000,
    "shortFeeRate": 0.9,
    "alertLongRatio": 33,
    "alertShortRatio": 56.000000000000007,
    "imLongRatio": 35,
    "imShortRatio": 60,
    "mcmLongRatio": 32,
    "mcmShortRatio": 53,
    "mmLongRatio": 25,
    "mmShortRatio": 40
   }
  ]
 }
}
```









`GetMarginRatio(req);`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetMarginRatio(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    const { TrdEnv, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ced92e472b40c92a'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType,s2c: { accList } } = res
                if(retType == RetType.RetType_Succeed){
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK paper trading environment account

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            securityList:[{
                                market: QotMarket.QotMarket_HK_Security,
                                code: "00700",
                            },],
                        },
                    };

                    websocket.GetMarginRatio(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetMarginRatio: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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

                }
            })
            .catch((error) => {
                console.log("GetAccList error:", error);
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
GetMarginRatio: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "marginRatioInfoList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "isLongPermit": true,
    "isShortPermit": true,
    "shortPoolRemain": 3082200,
    "shortFeeRate": 0.88,
    "alertLongRatio": 33,
    "alertShortRatio": 46,
    "imLongRatio": 35,
    "imShortRatio": 50,
    "mcmLongRatio": 32,
    "mcmShortRatio": 43,
    "mmLongRatio": 25,
    "mmShortRatio": 30
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single user ID.
- For each request, the maximum number of stocks supported by the
  parameter is 100.
- Only HK stocks and US stocks are supported.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_margin_ratio(code_list)`

- **Description**

  Query the margin data of stocks.

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
  <td style="text-align: left;">code_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Stock list.
  
    
  
  
   
  
  Up to 100 targets can be requested each time.<br />
  Data type of elements in the list is str.
  
  
  
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
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, margin data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Margin data format as follows:
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
    <td style="text-align: left;">Stock code</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_long_permit</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is marginable trading allowed.</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_short_permit</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is shortable trading allowed.</td>
    </tr>
    <tr>
    <td style="text-align: left;">short_pool_remain</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Short pool remaining.
    
      
    
    
     
    
    unit: shares.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">short_fee_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Borrow rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">alert_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable alert margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">alert_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Shortable alert margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">im_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable initial margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">im_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Shortable initial margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mcm_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable margin call margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mcm_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Shortable margin call margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mm_long_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable maintenance margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">mm_short_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Marginable maintenance margin.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.get_margin_ratio(code_list=['US.AAPL','US.FUTU'])  
if ret == RET_OK:
    print(data)
    print(data['is_long_permit'][0])  # Get whether marginable trading allowed for the first stock
    print(data['im_short_ratio'].values.tolist())  # Convert to list
else:
    print('error:', data)
trd_ctx.close()  # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
       code  is_long_permit  is_short_permit  short_pool_remain  short_fee_rate  alert_long_ratio  alert_short_ratio  im_long_ratio  im_short_ratio  mcm_long_ratio  mcm_short_ratio  mm_long_ratio  mm_short_ratio
0  US.AAPL             True             True          1826900.0            0.89              33.0               56.0           35.0            60.0            32.0             53.0           25.0            40.0
1  US.FUTU            True             True          1150600.0            0.95              48.0               46.0           50.0            50.0            47.0             43.0           40.0            30.0
True
[60.0, 50.0]
```









## <a href="#4388-2" class="header-anchor">#</a> Trd_GetMarginRatio.proto

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2223





`uint GetMarginRatio(TrdGetMarginRatio.Request req);`  
`virtual void OnReply_GetMarginRatio(MMAPI_Conn client, uint nSerialNo, TrdGetMarginRatio.Response rsp);`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Trd, MMSPI_Conn {
    MMAPI_Trd trd = new MMAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1);  //设置客户端信息
        trd.SetConnCallback(this);  //设置连接回调
        trd.SetTrdCallback(this);   //设置交易回调
    }

    public void Start() {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }

    
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.CreateBuilder()
                .SetAccID(281756457888247915L)
                .SetTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .SetTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .Build();
        QotCommon.Security security = QotCommon.Security.CreateBuilder()
                .SetCode("00700")
                .SetMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .Build();
        TrdGetMarginRatio.C2S c2s = TrdGetMarginRatio.C2S.CreateBuilder()
                .SetHeader(header)
                .AddSecurityList(security)
                .Build();

        TrdGetMarginRatio.Request req = TrdGetMarginRatio.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetMarginRatio(req);
        Console.Write("Send TrdGetMarginRatio: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetMarginRatio(MMAPI_Conn client, uint nSerialNo, TrdGetMarginRatio.Response rsp)
    {
        Console.Write("Reply: TrdGetMarginRatio: {0}\n", nSerialNo);
        Console.Write("accID: {0}\n", rsp.S2C.Header.AccID);
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
Trd onInitConnect: ret=0 desc= connID=6826814786778581486
Send TrdGetMarginRatio: 3
Reply: TrdGetMarginRatio: 3
accID: 281756457888247915
```









`int getMarginRatio(TrdGetMarginRatio.Request req);`  
`void onReply_GetMarginRatio(MMAPI_Conn client, int nSerialNo, TrdGetMarginRatio.Response rsp);`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements MMSPI_Trd, MMSPI_Conn {
    MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1);  //设置客户端信息
        trd.setConnSpi(this);  //设置连接回调
        trd.setTrdSpi(this);   //设置交易回调
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.newBuilder()
                .setAccID(281756457888247915L)
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        QotCommon.Security security = QotCommon.Security.newBuilder()
                .setCode("00700")
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .build();
        TrdGetMarginRatio.C2S c2s = TrdGetMarginRatio.C2S.newBuilder()
                .setHeader(header)
                .addSecurityList(security)
                .build();
        TrdGetMarginRatio.Request req = TrdGetMarginRatio.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getMarginRatio(req);
        System.out.printf("Send TrdGetMarginRatio: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetMarginRatio(MMAPI_Conn client, int nSerialNo, TrdGetMarginRatio.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetMarginRatio failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetMarginRatio: %s\n", json);
            } catch (InvalidProtocolBufferException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
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





- **Output**



``` text
Send TrdGetMarginRatio: 2
Receive TrdGetMarginRatio: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "marginRatioInfoList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "isLongPermit": true,
      "isShortPermit": true,
      "shortPoolRemain": 1987700.0,
      "shortFeeRate": 0.9,
      "alertLongRatio": 33.0,
      "alertShortRatio": 56.00000000000001,
      "imLongRatio": 35.0,
      "imShortRatio": 60.0,
      "mcmLongRatio": 32.0,
      "mcmShortRatio": 53.0,
      "mmLongRatio": 25.0,
      "mmShortRatio": 40.0
    }]
  }
}
```









`moomoo::u32_t GetMarginRatio(const Trd_GetMarginRatio::Request &stReq);`  
`virtual void OnReply_GetMarginRatio(moomoo::u32_t nSerialNo, const Trd_GetMarginRatio::Response &stRsp) = 0;`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
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
        m_pTrdApi = MMAPI::CreateTrdApi();
        m_pTrdApi->RegisterTrdSpi(this);
        m_pTrdApi->RegisterConnSpi(this);
    }

    ~Program() {
        if (m_pTrdApi != nullptr)
        {
            m_pTrdApi->UnregisterTrdSpi();
            m_pTrdApi->UnregisterConnSpi();
            MMAPI::ReleaseTrdApi(m_pTrdApi);
            m_pTrdApi = nullptr;
        }
    }

    void Start() {
        m_pTrdApi->InitConnect("127.0.0.1", 11111, false);
    }


    virtual void OnInitConnect(MMAPI_Conn* pConn, moomoo::i64_t nErrCode, const char* strDesc) {
        cout << "connect" << endl;

        // construct request message
        Trd_GetMarginRatio::Request req;
        Trd_GetMarginRatio::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        auto secList = c2s->mutable_securitylist();
        Qot_Common::Security *sec = secList->Add();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);

        m_GetMarginRatioSerialNo = m_pTrdApi->GetMarginRatio(req);
        cout << "Request GetMarginRatio SerialNo: " << m_GetMarginRatioSerialNo << endl;
    }

    virtual void OnReply_GetMarginRatio(moomoo::u32_t nSerialNo, const Trd_GetMarginRatio::Response &stRsp){
        if(nSerialNo == m_GetMarginRatioSerialNo)
        {
            cout << "OnReply_GetMarginRatio SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_PlaceOrderSerialNo;
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
Request GetMarginRatio SerialNo: 4
OnReply_GetMarginRatio SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "marginRatioInfoList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "isLongPermit": true,
    "isShortPermit": true,
    "shortPoolRemain": 1860000,
    "shortFeeRate": 0.9,
    "alertLongRatio": 33,
    "alertShortRatio": 56.000000000000007,
    "imLongRatio": 35,
    "imShortRatio": 60,
    "mcmLongRatio": 32,
    "mcmShortRatio": 53,
    "mmLongRatio": 25,
    "mmShortRatio": 40
   }
  ]
 }
}
```









`GetMarginRatio(req);`

- **Description**

  Query the margin data of stocks.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Qot_Common.Security securityList = 2; //Security list
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)

- **Return**



``` protobuf
message MarginRatioInfo
{
    required Qot_Common.Security security = 1; //Stock code
    optional bool   isLongPermit = 2; //Is marginable trading allowed.
    optional bool   isShortPermit = 3; //Is shortable trading allowed.
    optional double shortPoolRemain = 4; //Short pool remaining (shares).
    optional double shortFeeRate = 5; //Borrow rate (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertLongRatio = 6; //Marginable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double alertShortRatio = 7; //Shortable alert margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imLongRatio = 8; //Marginable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double imShortRatio = 9; //Shortable initial margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmLongRatio = 10; //Marginable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mcmShortRatio = 11; //Shortable margin call margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmLongRatio = 12; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
    optional double mmShortRatio = 13; //Marginable maintenance margin (This field is in percentage form, so 20 is equivalent to 20%.).
}

message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated MarginRatioInfo marginRatioInfoList = 2; //Margin data
}

message Response
{
    //The following 3 fields are available in all protocols, and the notes are in InitConnect.proto
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For stock structure, refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdGetMarginRatio(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    const { TrdEnv, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ced92e472b40c92a'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType,s2c: { accList } } = res
                if(retType == RetType.RetType_Succeed){
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK paper trading environment account

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            securityList:[{
                                market: QotMarket.QotMarket_HK_Security,
                                code: "00700",
                            },],
                        },
                    };

                    websocket.GetMarginRatio(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetMarginRatio: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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

                }
            })
            .catch((error) => {
                console.log("GetAccList error:", error);
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
GetMarginRatio: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "marginRatioInfoList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "isLongPermit": true,
    "isShortPermit": true,
    "shortPoolRemain": 3082200,
    "shortFeeRate": 0.88,
    "alertLongRatio": 33,
    "alertShortRatio": 46,
    "imLongRatio": 35,
    "imShortRatio": 50,
    "mcmLongRatio": 32,
    "mcmShortRatio": 43,
    "mmLongRatio": 25,
    "mmShortRatio": 30
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single user ID.
- For each request, the maximum number of stocks supported by the
  parameter is 100.
- Stocks and ETFs of US, HK and A-share markets are supported.













