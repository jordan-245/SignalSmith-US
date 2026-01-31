



# <a href="#6265" class="header-anchor">#</a> Get Historical Candlesticks









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`request_history_kline(code, start=None, end=None, ktype=KLType.K_DAY, autype=AuType.QFQ, fields=[KL_FIELD.ALL], max_count=1000, page_req_key=None, extended_time=False)`

- **Description**

  Get historical candlesticks

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
  <td style="text-align: left;">Stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2017-06-20".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2017-07-20".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">ktype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
  <td style="text-align: left;">Candlestick type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">autype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#7071">AuType</a></td>
  <td style="text-align: left;">Type of adjustment.</td>
  </tr>
  <tr>
  <td style="text-align: left;">fields</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#5803">KL_FIELD</a></td>
  <td style="text-align: left;">List of fields to be returned.</td>
  </tr>
  <tr>
  <td style="text-align: left;">max_count</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The maximum number of candlesticks
  returned in this request.
  
    
  
  
   
  
  <ul>
  <li>Sending None indicates that all data between start and end is
  returned.</li>
  <li>Note: OpenD requests all the data and then sends it to the script.
  If the number of candlesticks you want to obtain is more than 1000, it
  is recommended to select paging to prevent from timeout.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">page_req_key</td>
  <td style="text-align: left;">bytes</td>
  <td style="text-align: left;">The key of the page request. If the number
  of candlesticks between start and end is more than max_count, then None
  should be passed at the first time you call this interface, and the
  page_req_key returned by the last call must be passed in the subsequent
  pagerequests.</td>
  </tr>
  <tr>
  <td style="text-align: left;">extended_time</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Need pre-market and after-hours data for
  US stocks or not. False: not need, True: need.</td>
  </tr>
  <tr>
  <td style="text-align: left;">session</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
  <td style="text-align: left;">Get US stocks historical k-line in session
  
    
  
  
   
  
  <ul>
  <li>Only used to get historical k-line for US stocks in session.</li>
  </ul>
  <ul>
  <li>If you want to get 24H historical k-line data of US stocks, please
  use 'ALL'. The 'OVERNIGHT' is not allowed.</li>
  </ul>
  <ul>
  <li>Minimum version requirements: 9.2.4207</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 365 days before ***end***. |
    | str | None | ***end*** is 365 days after ***start***. |
    | None | None | ***end*** is the current date, ***start*** is 365 days before. |

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
  <td>If ret == RET_OK, historical candlestick data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  <tr>
  <td>page_req_key</td>
  <td>bytes</td>
  <td>The key of the next page request.</td>
  </tr>
  </tbody>
  </table>

  - Historical candlestick data format as follows:
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
    <td style="text-align: left;">time_key</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Candlestick time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Change rate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data, page_req_key = quote_ctx.request_history_kline('US.AAPL', start='2019-09-11', end='2019-09-18', max_count=5) # 5 per page, request the first page
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['close'].values.tolist()) # The closing price of the first page is converted to a list
else:
    print('error:', data)
while page_req_key != None: # Request all results after
    print('*************************************')
    ret, data, page_req_key = quote_ctx.request_history_kline('US.AAPL', start='2019-09-11', end='2019-09-18', max_count=5,page_req_key=page_req_key) # Request the page after turning data
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
print('All pages are finished!')
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
code  name             time_key       open      close       high        low  pe_ratio  turnover_rate    volume      turnover  change_rate  last_close
0  US.AAPL   APPLE  2019-09-11 00:00:00  52.631194  53.963447  53.992409  52.549135    18.773        0.01039  177158584  9.808562e+09     3.179511   52.300545
..       ...   ...                  ...        ...        ...        ...        ...       ...            ...       ...           ...          ...         ...
4  US.AAPL   APPLE  2019-09-17 00:00:00  53.087346  53.265945  53.294907  52.884612    18.530        0.00432   73545872  4.046314e+09     0.363802   53.072865

[5 rows x 13 columns]
US.AAPL
[53.9634465, 53.84156475, 52.7953125, 53.072865, 53.265945]
*************************************
       code  name             time_key       open      close       high        low  pe_ratio  turnover_rate   volume      turnover  change_rate  last_close
0  US.AAPL   APPLE  2019-09-18 00:00:00  53.352831  53.76554  53.784847  52.961844    18.704        0.00602  102572372  5.682068e+09     0.937925   53.265945
All pages are finished!
```









## <a href="#4609" class="header-anchor">#</a> Qot_RequestHistoryKL.proto

- **Description**

  Get historical candlestics

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3103





`uint RequestHistoryKL(QotRequestHistoryKL.Request req);`  
`virtual void OnReply_RequestHistoryKL(FTAPI_Conn client, uint nSerialNo, QotRequestHistoryKL.Response rsp);`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        QotRequestHistoryKL.C2S c2s = QotRequestHistoryKL.C2S.CreateBuilder()
                .SetRehabType((int)QotCommon.RehabType.RehabType_Forward)
                .SetKlType((int)QotCommon.KLType.KLType_1Min)
                .SetSecurity(sec)
                .SetBeginTime("2020-09-01")
                .SetEndTime("2020-09-10")
            .Build();
        QotRequestHistoryKL.Request req = QotRequestHistoryKL.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestHistoryKL(req);
        Console.Write("Send QotRequestHistoryKL: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }
    
    public void OnReply_RequestHistoryKL(FTAPI_Conn client, uint nSerialNo, QotRequestHistoryKL.Response rsp) {
        Console.Write("Reply: QotRequestHistoryKL: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("Code: {0},  lastClosePrice: {1} \n",
            rsp.S2C.Security.Code,
            rsp.S2C.KlListList[0].LastClosePrice);
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
Qot onInitConnect: ret=0 desc= connID=6819076272648767075
Send QotRequestHistoryKL: 3
Reply: QotRequestHistoryKL: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  security {
    market: 1
    code: "00700"
  }
  klList {
    time: "2020-09-01 09:30:00"
    isBlank: false
    highPrice: 535.9
    openPrice: 535.9
    lowPrice: 535.9
    closePrice: 535.9
    lastClosePrice: 528.9
    volume: 665000
    turnover: 357437500
    turnoverRate: 0
    pe: 0
    changeRate: 1.3235016071090944
    timestamp: 1598923800
  }
  ...
  klList {
    time: "2020-09-09 16:00:00"
    isBlank: false
    highPrice: 503.9
    openPrice: 502.4
    lowPrice: 501.9
    closePrice: 502.4
    lastClosePrice: 502.9
    volume: 1504800
    turnover: 758472600
    turnoverRate: 0
    pe: 0
    changeRate: -0.0994233446013124
    timestamp: 1599638400
  }
}

Code: 00700,  lastClosePrice: 528.9
```









`int requestHistoryKL(QotRequestHistoryKL.Request req);`  
`void onReply_RequestHistoryKL(FTAPI_Conn client, int nSerialNo, QotRequestHistoryKL.Response rsp);`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        QotRequestHistoryKL.C2S c2s = QotRequestHistoryKL.C2S.newBuilder()
                .setRehabType(QotCommon.RehabType.RehabType_Forward_VALUE)
                .setKlType(QotCommon.KLType.KLType_1Min_VALUE)
                .setSecurity(sec)
                .setBeginTime("2020-09-01")
                .setEndTime("2020-09-02")
            .build();
        QotRequestHistoryKL.Request req = QotRequestHistoryKL.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestHistoryKL(req);
        System.out.printf("Send QotRequestHistoryKL: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestHistoryKL(FTAPI_Conn client, int nSerialNo, QotRequestHistoryKL.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestHistoryKL failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestHistoryKL: %s\n", json);
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
Send QotRequestHistoryKL: 2
Receive QotRequestHistoryKL: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "klList": [{
      "time": "2020-09-01 09:30:00",
      "isBlank": false,
      "highPrice": 535.9,
      "openPrice": 535.9,
      "lowPrice": 535.9,
      "closePrice": 535.9,
      "lastClosePrice": 528.9,
      "volume": "665000",
      "turnover": 3.574375E8,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": 1.3235016071090944,
      "timestamp": 1.5989238E9
    }, ... {
      "time": "2020-09-01 16:00:00",
      "isBlank": false,
      "highPrice": 542.4,
      "openPrice": 542.4,
      "lowPrice": 537.4,
      "closePrice": 537.4,
      "lastClosePrice": 542.4,
      "volume": "1303900",
      "turnover": 7.0309225E8,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": -0.9218289085545722,
      "timestamp": 1.5989472E9
    }]
  }
}
```









`Futu::u32_t RequestHistoryKL(const Qot_RequestHistoryKL::Request &stReq);`  
`virtual void OnReply_RequestHistoryKL(Futu::u32_t nSerialNo, const Qot_RequestHistoryKL::Response &stRsp) = 0;`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        Qot_RequestHistoryKL::Request req;
        Qot_RequestHistoryKL::C2S *c2s = req.mutable_c2s();
        c2s->set_rehabtype(1);
        c2s->set_kltype(Qot_Common::KLType::KLType_1Min);
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_begintime("2021-06-07");
        c2s->set_endtime("2021-07-01");
        
        m_RequestHistoryKLSerialNo = m_pQotApi->RequestHistoryKL(req);
        cout << "Request RequestHistoryKL SerialNo: " << m_RequestHistoryKLSerialNo << endl;
    }

    virtual void OnReply_RequestHistoryKL(Futu::u32_t nSerialNo, const Qot_RequestHistoryKL::Response &stRsp){
        if(nSerialNo == m_RequestHistoryKLSerialNo)
        {
            cout << "OnReply_RequestHistoryKL SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;
    
    Futu::u32_t m_RequestHistoryKLSerialNo;
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
Request RequestHistoryKL SerialNo: 3
OnReply_RequestHistoryKL SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "klList": [
   {
    "time": "2021-06-07 09:30:00",
    "isBlank": false,
    "highPrice": 611,
    "openPrice": 611,
    "lowPrice": 611,
    "closePrice": 611,
    "lastClosePrice": 611.5,
    "volume": "250100",
    "turnover": 152811100,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": -0.081766148814390843,
    "timestamp": 1623029400
   },
   {
    "time": "2021-06-07 09:31:00",
    "isBlank": false,
    "highPrice": 611.5,
    "openPrice": 611,
    "lowPrice": 609,
    "closePrice": 609.5,
    "lastClosePrice": 611,
    "volume": "230700",
    "turnover": 140792100,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": -0.24549918166939444,
    "timestamp": 1623029460
   },
...
   {
    "time": "2021-06-09 14:14:00",
    "isBlank": false,
    "highPrice": 601,
    "openPrice": 600.5,
    "lowPrice": 600,
    "closePrice": 601,
    "lastClosePrice": 600,
    "volume": "19300",
    "turnover": 11589150,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0.16666666666666669,
    "timestamp": 1623219240
   }
  ]
 }
}
```









`RequestHistoryKL(req);`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotRequestHistoryKL(){
    const { RetType } = Common
    const { RehabType, KLType, SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    rehabType: RehabType.RehabType_None, 
                    klType: KLType.KLType_Day,
                    security:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    beginTime: "2021-08-05",
                    endTime: "2021-08-10",
                },
            };
            
            websocket.RequestHistoryKL(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("HistoryKL: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
  "security": {
    "market": 1,
    "code": "00700"
  },
  "klList": [{
    "time": "2021-08-05 00:00:00",
    "isBlank": false,
    "highPrice": 464.4,
    "openPrice": 452.6,
    "lowPrice": 432.6,
    "closePrice": 439,
    "lastClosePrice": 456.8,
    "volume": "58625939",
    "turnover": 26193545519,
    "turnoverRate": 0.00611,
    "pe": 22.137,
    "changeRate": -3.896672504378286,
    "timestamp": 1628092800
  }, {
    "time": "2021-08-06 00:00:00",
    "isBlank": false,
    "highPrice": 460.4,
    "openPrice": 444.8,
    "lowPrice": 440,
    "closePrice": 453.6,
    "lastClosePrice": 439,
    "volume": "42946505",
    "turnover": 19468783995,
    "turnoverRate": 0.00447,
    "pe": 22.873,
    "changeRate": 3.3257403189066106,
    "timestamp": 1628179200
  }, {
    "time": "2021-08-09 00:00:00",
    "isBlank": false,
    "highPrice": 472.4,
    "openPrice": 447.8,
    "lowPrice": 442.6,
    "closePrice": 461.6,
    "lastClosePrice": 453.6,
    "volume": "40956433",
    "turnover": 18847164570,
    "turnoverRate": 0.00427,
    "pe": 23.276,
    "changeRate": 1.763668430335097,
    "timestamp": 1628438400
  }, {
    "time": "2021-08-10 00:00:00",
    "isBlank": false,
    "highPrice": 493,
    "openPrice": 478,
    "lowPrice": 473.2,
    "closePrice": 486.2,
    "lastClosePrice": 461.6,
    "volume": "40881986",
    "turnover": 19749306230,
    "turnoverRate": 0.00426,
    "pe": 24.517,
    "changeRate": 5.329289428076249,
    "timestamp": 1628524800
  }]
}
stop
```











Interface Restrictions

- Candlestick data with timeframes of **60 minutes and below**, is only
  supported for the last 8 years. **Daily** candlestick data is
  supported for the last 20 years. **Daily above** candlestick data is
  not restricted.
- We will issue historical candlestick quota based on your account
  assets and transaction conditions. Therefore, you can only obtain
  historical candlestick data for a limited number of stocks within 30
  days. For specific rules, please refer to [Subscription Quota &
  Historical Candlestick
  Quota](/moomoo-api-doc/en/intro/authority.html#9123). The historical
  candlestick quota you consume on that day will be automatically
  released after 30 days.
- A maximum of 60 requests per 30 seconds. Note: If you obtain data by
  page, this frequency limit rule is only applicable to the first time
  calling the interface, and subsequent pages request frequency is
  unlimited.
- *Change rate*, only supports timeframes of daily and above.
- **Options** related candlestick data, only supports 1 day, 1 minute, 5
  minutes, 15 minutes and 60 minutes.
- The pre-market, after-hours and overnight candlestick of US stocks,
  only supports timeframes of 60 minutes and below. Since the
  pre-market, after-hours and overnight session of the US stock market
  are irregular trading hours, the candlestick data for this period may
  be less than 2 years.
- *Turnover* of US stocks, only supports data after 2015-10-12.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`request_history_kline(code, start=None, end=None, ktype=KLType.K_DAY, autype=AuType.QFQ, fields=[KL_FIELD.ALL], max_count=1000, page_req_key=None, extended_time=False)`

- **Description**

  Get historical candlesticks

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
  <td style="text-align: left;">Stock code.</td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2017-06-20".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  Format: yyyy-MM-dd<br />
  For example: "2017-07-20".
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">ktype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#66">KLType</a></td>
  <td style="text-align: left;">Candlestick type.</td>
  </tr>
  <tr>
  <td style="text-align: left;">autype</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#7071">AuType</a></td>
  <td style="text-align: left;">Type of adjustment.</td>
  </tr>
  <tr>
  <td style="text-align: left;">fields</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#5803">KL_FIELD</a></td>
  <td style="text-align: left;">List of fields to be returned.</td>
  </tr>
  <tr>
  <td style="text-align: left;">max_count</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The maximum number of candlesticks
  returned in this request.
  
    
  
  
   
  
  <ul>
  <li>Sending None indicates that all data between start and end is
  returned.</li>
  <li>Note: OpenD requests all the data and then sends it to the script.
  If the number of candlesticks you want to obtain is more than 1000, it
  is recommended to select paging to prevent from timeout.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">page_req_key</td>
  <td style="text-align: left;">bytes</td>
  <td style="text-align: left;">The key of the page request. If the number
  of candlesticks between start and end is more than max_count, then None
  should be passed at the first time you call this interface, and the
  page_req_key returned by the last call must be passed in the subsequent
  pagerequests.</td>
  </tr>
  <tr>
  <td style="text-align: left;">extended_time</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Need pre-market and after-hours data for
  US stocks or not. False: not need, True: need.</td>
  </tr>
  <tr>
  <td style="text-align: left;">session</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/quote/quote.html#8688">Session</a></td>
  <td style="text-align: left;">Get US stocks historical k-line in session
  
    
  
  
   
  
  <ul>
  <li>Only used to get historical k-line for US stocks in session.</li>
  </ul>
  <ul>
  <li>If you want to get 24H historical k-line data of US stocks, please
  use 'ALL'. The 'OVERNIGHT' is not allowed.</li>
  </ul>
  <ul>
  <li>Minimum version requirements: 9.2.4207</li>
  </ul>
  
  
  
  </td>
  </tr>
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 365 days before ***end***. |
    | str | None | ***end*** is 365 days after ***start***. |
    | None | None | ***end*** is the current date, ***start*** is 365 days before. |

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
  <td>If ret == RET_OK, historical candlestick data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  <tr>
  <td>page_req_key</td>
  <td>bytes</td>
  <td>The key of the next page request.</td>
  </tr>
  </tbody>
  </table>

  - Historical candlestick data format as follows:
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
    <td style="text-align: left;">time_key</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Candlestick time.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">open</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Close.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pe_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">P/E ratio.
    
      
    
    
     
    
    This field is a ratio field, and % is not displayed.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Change rate.</td>
    </tr>
    <tr>
    <td style="text-align: left;">last_close</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data, page_req_key = quote_ctx.request_history_kline('US.AAPL', start='2019-09-11', end='2019-09-18', max_count=5) # 5 per page, request the first page
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['close'].values.tolist()) # The closing price of the first page is converted to a list
else:
    print('error:', data)
while page_req_key != None: # Request all results after
    print('*************************************')
    ret, data, page_req_key = quote_ctx.request_history_kline('US.AAPL', start='2019-09-11', end='2019-09-18', max_count=5,page_req_key=page_req_key) # Request the page after turning data
    if ret == RET_OK:
        print(data)
    else:
        print('error:', data)
print('All pages are finished!')
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
code  name             time_key       open      close       high        low  pe_ratio  turnover_rate    volume      turnover  change_rate  last_close
0  US.AAPL   APPLE  2019-09-11 00:00:00  52.631194  53.963447  53.992409  52.549135    18.773        0.01039  177158584  9.808562e+09     3.179511   52.300545
..       ...   ...                  ...        ...        ...        ...        ...       ...            ...       ...           ...          ...         ...
4  US.AAPL   APPLE  2019-09-17 00:00:00  53.087346  53.265945  53.294907  52.884612    18.530        0.00432   73545872  4.046314e+09     0.363802   53.072865

[5 rows x 13 columns]
US.AAPL
[53.9634465, 53.84156475, 52.7953125, 53.072865, 53.265945]
*************************************
       code  name             time_key       open      close       high        low  pe_ratio  turnover_rate   volume      turnover  change_rate  last_close
0  US.AAPL   APPLE  2019-09-18 00:00:00  53.352831  53.76554  53.784847  52.961844    18.704        0.00602  102572372  5.682068e+09     0.937925   53.265945
All pages are finished!
```









## <a href="#4609-2" class="header-anchor">#</a> Qot_RequestHistoryKL.proto

- **Description**

  Get historical candlestics

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3103





`uint RequestHistoryKL(QotRequestHistoryKL.Request req);`  
`virtual void OnReply_RequestHistoryKL(MMAPI_Conn client, uint nSerialNo, QotRequestHistoryKL.Response rsp);`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        QotRequestHistoryKL.C2S c2s = QotRequestHistoryKL.C2S.CreateBuilder()
                .SetRehabType((int)QotCommon.RehabType.RehabType_Forward)
                .SetKlType((int)QotCommon.KLType.KLType_1Min)
                .SetSecurity(sec)
                .SetBeginTime("2020-09-01")
                .SetEndTime("2020-09-10")
            .Build();
        QotRequestHistoryKL.Request req = QotRequestHistoryKL.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.RequestHistoryKL(req);
        Console.Write("Send QotRequestHistoryKL: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }
    
    public void OnReply_RequestHistoryKL(MMAPI_Conn client, uint nSerialNo, QotRequestHistoryKL.Response rsp) {
        Console.Write("Reply: QotRequestHistoryKL: {0}  {1}\n", nSerialNo, rsp.ToString());
        Console.Write("Code: {0},  lastClosePrice: {1} \n",
            rsp.S2C.Security.Code,
            rsp.S2C.KlListList[0].LastClosePrice);
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
Qot onInitConnect: ret=0 desc= connID=6819076272648767075
Send QotRequestHistoryKL: 3
Reply: QotRequestHistoryKL: 3  retType: 0
retMsg: ""
errCode: 0
s2c {
  security {
    market: 1
    code: "00700"
  }
  klList {
    time: "2020-09-01 09:30:00"
    isBlank: false
    highPrice: 535.9
    openPrice: 535.9
    lowPrice: 535.9
    closePrice: 535.9
    lastClosePrice: 528.9
    volume: 665000
    turnover: 357437500
    turnoverRate: 0
    pe: 0
    changeRate: 1.3235016071090944
    timestamp: 1598923800
  }
  ...
  klList {
    time: "2020-09-09 16:00:00"
    isBlank: false
    highPrice: 503.9
    openPrice: 502.4
    lowPrice: 501.9
    closePrice: 502.4
    lastClosePrice: 502.9
    volume: 1504800
    turnover: 758472600
    turnoverRate: 0
    pe: 0
    changeRate: -0.0994233446013124
    timestamp: 1599638400
  }
}

Code: 00700,  lastClosePrice: 528.9
```









`int requestHistoryKL(QotRequestHistoryKL.Request req);`  
`void onReply_RequestHistoryKL(MMAPI_Conn client, int nSerialNo, QotRequestHistoryKL.Response rsp);`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        QotRequestHistoryKL.C2S c2s = QotRequestHistoryKL.C2S.newBuilder()
                .setRehabType(QotCommon.RehabType.RehabType_Forward_VALUE)
                .setKlType(QotCommon.KLType.KLType_1Min_VALUE)
                .setSecurity(sec)
                .setBeginTime("2020-09-01")
                .setEndTime("2020-09-02")
            .build();
        QotRequestHistoryKL.Request req = QotRequestHistoryKL.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.requestHistoryKL(req);
        System.out.printf("Send QotRequestHistoryKL: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_RequestHistoryKL(MMAPI_Conn client, int nSerialNo, QotRequestHistoryKL.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotRequestHistoryKL failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotRequestHistoryKL: %s\n", json);
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
Send QotRequestHistoryKL: 2
Receive QotRequestHistoryKL: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "security": {
      "market": 1,
      "code": "00700"
    },
    "klList": [{
      "time": "2020-09-01 09:30:00",
      "isBlank": false,
      "highPrice": 535.9,
      "openPrice": 535.9,
      "lowPrice": 535.9,
      "closePrice": 535.9,
      "lastClosePrice": 528.9,
      "volume": "665000",
      "turnover": 3.574375E8,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": 1.3235016071090944,
      "timestamp": 1.5989238E9
    }, ... {
      "time": "2020-09-01 16:00:00",
      "isBlank": false,
      "highPrice": 542.4,
      "openPrice": 542.4,
      "lowPrice": 537.4,
      "closePrice": 537.4,
      "lastClosePrice": 542.4,
      "volume": "1303900",
      "turnover": 7.0309225E8,
      "turnoverRate": 0.0,
      "pe": 0.0,
      "changeRate": -0.9218289085545722,
      "timestamp": 1.5989472E9
    }]
  }
}
```









`moomoo::u32_t RequestHistoryKL(const Qot_RequestHistoryKL::Request &stReq);`  
`virtual void OnReply_RequestHistoryKL(moomoo::u32_t nSerialNo, const Qot_RequestHistoryKL::Response &stRsp) = 0;`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
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
        Qot_RequestHistoryKL::Request req;
        Qot_RequestHistoryKL::C2S *c2s = req.mutable_c2s();
        c2s->set_rehabtype(1);
        c2s->set_kltype(Qot_Common::KLType::KLType_1Min);
        Qot_Common::Security *sec = c2s->mutable_security();
        sec->set_code("00700");
        sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
        c2s->set_begintime("2021-06-07");
        c2s->set_endtime("2021-07-01");
        
        m_RequestHistoryKLSerialNo = m_pQotApi->RequestHistoryKL(req);
        cout << "Request RequestHistoryKL SerialNo: " << m_RequestHistoryKLSerialNo << endl;
    }

    virtual void OnReply_RequestHistoryKL(moomoo::u32_t nSerialNo, const Qot_RequestHistoryKL::Response &stRsp){
        if(nSerialNo == m_RequestHistoryKLSerialNo)
        {
            cout << "OnReply_RequestHistoryKL SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;
    
    moomoo::u32_t m_RequestHistoryKLSerialNo;
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
Request RequestHistoryKL SerialNo: 3
OnReply_RequestHistoryKL SerialNo: 3
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "security": {
   "market": 1,
   "code": "00700"
  },
  "klList": [
   {
    "time": "2021-06-07 09:30:00",
    "isBlank": false,
    "highPrice": 611,
    "openPrice": 611,
    "lowPrice": 611,
    "closePrice": 611,
    "lastClosePrice": 611.5,
    "volume": "250100",
    "turnover": 152811100,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": -0.081766148814390843,
    "timestamp": 1623029400
   },
   {
    "time": "2021-06-07 09:31:00",
    "isBlank": false,
    "highPrice": 611.5,
    "openPrice": 611,
    "lowPrice": 609,
    "closePrice": 609.5,
    "lastClosePrice": 611,
    "volume": "230700",
    "turnover": 140792100,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": -0.24549918166939444,
    "timestamp": 1623029460
   },
...
   {
    "time": "2021-06-09 14:14:00",
    "isBlank": false,
    "highPrice": 601,
    "openPrice": 600.5,
    "lowPrice": 600,
    "closePrice": 601,
    "lastClosePrice": 600,
    "volume": "19300",
    "turnover": 11589150,
    "turnoverRate": 0,
    "pe": 0,
    "changeRate": 0.16666666666666669,
    "timestamp": 1623219240
   }
  ]
 }
}
```









`RequestHistoryKL(req);`

- **Description**

  Get historical candlesticks

- **Parameters**



``` protobuf

message C2S
{
    required int32 rehabType = 1; //Qot_Common.RehabType, rehabilitation type
    required int32 klType = 2; //Qot_Common.KLType, timeframe of candlestick
    required Qot_Common.Security security = 3; //Security code
    required string beginTime = 4; //Start time string (Format: yyyy-MM-dd)
    required string endTime = 5; //End time string (Format: yyyy-MM-dd)
    optional int32 maxAckKLNum = 6; //How many candlesticks can be returned at most, if not specified, it means no limit
    optional int64 needKLFieldsFlag = 7; //Specific fields of candlestick structure to return. A combination of KLFields enumeratio. If not specified, return all fields
    optional bytes nextReqKey = 8; //Paging request key
    optional bool extendedTime = 9; //Whether to get the pre-market and after-hours currently only supports timeframes of 60-minutes and below.
    optional int32 session = 10; //Get non-regular data of US stocks, currently only supports timeframes of 60-minutes and below.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For stock adjustment type, refer to
>   [RehabType](/moomoo-api-doc/en/quote/quote.html#7071)
> - For candlestick type, refer to
>   [KLType](/moomoo-api-doc/en/quote/quote.html#66)
> - For candlestick structure, refer to
>   [KLFields](/moomoo-api-doc/en/quote/quote.html#5803)

- **Return**



``` protobuf

message S2C
{
    required Qot_Common.Security security = 1; //Security
    optional string name = 4; // Stock name
    repeated Qot_Common.KLine klList = 2; //Candlestick data
    optional bytes nextReqKey = 3; //Paging request key.
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For stock structure refer to
>   [Security](/moomoo-api-doc/en/quote/quote.html#5792)
> - For candlestick structure, refer to
>   [KLine](/moomoo-api-doc/en/quote/quote.html#500)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotRequestHistoryKL(){
    const { RetType } = Common
    const { RehabType, KLType, SubType, QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    rehabType: RehabType.RehabType_None, 
                    klType: KLType.KLType_Day,
                    security:{
                        market: QotMarket.QotMarket_HK_Security,
                        code: "00700",
                    },
                    beginTime: "2021-08-05",
                    endTime: "2021-08-10",
                },
            };
            
            websocket.RequestHistoryKL(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("HistoryKL: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
  "security": {
    "market": 1,
    "code": "00700"
  },
  "klList": [{
    "time": "2021-08-05 00:00:00",
    "isBlank": false,
    "highPrice": 464.4,
    "openPrice": 452.6,
    "lowPrice": 432.6,
    "closePrice": 439,
    "lastClosePrice": 456.8,
    "volume": "58625939",
    "turnover": 26193545519,
    "turnoverRate": 0.00611,
    "pe": 22.137,
    "changeRate": -3.896672504378286,
    "timestamp": 1628092800
  }, {
    "time": "2021-08-06 00:00:00",
    "isBlank": false,
    "highPrice": 460.4,
    "openPrice": 444.8,
    "lowPrice": 440,
    "closePrice": 453.6,
    "lastClosePrice": 439,
    "volume": "42946505",
    "turnover": 19468783995,
    "turnoverRate": 0.00447,
    "pe": 22.873,
    "changeRate": 3.3257403189066106,
    "timestamp": 1628179200
  }, {
    "time": "2021-08-09 00:00:00",
    "isBlank": false,
    "highPrice": 472.4,
    "openPrice": 447.8,
    "lowPrice": 442.6,
    "closePrice": 461.6,
    "lastClosePrice": 453.6,
    "volume": "40956433",
    "turnover": 18847164570,
    "turnoverRate": 0.00427,
    "pe": 23.276,
    "changeRate": 1.763668430335097,
    "timestamp": 1628438400
  }, {
    "time": "2021-08-10 00:00:00",
    "isBlank": false,
    "highPrice": 493,
    "openPrice": 478,
    "lowPrice": 473.2,
    "closePrice": 486.2,
    "lastClosePrice": 461.6,
    "volume": "40881986",
    "turnover": 19749306230,
    "turnoverRate": 0.00426,
    "pe": 24.517,
    "changeRate": 5.329289428076249,
    "timestamp": 1628524800
  }]
}
stop
```











Interface Restrictions

- Candlestick data with timeframes of **60 minutes and below**, is only
  supported for the last 8 years. **Daily** candlestick data is
  supported for the last 20 years. **Daily above** candlestick data is
  not restricted.
- We will issue historical candlestick quota based on your account
  assets and transaction conditions. Therefore, you can only obtain
  historical candlestick data for a limited number of stocks within 30
  days. For specific rules, please refer to [Subscription Quota &
  Historical Candlestick
  Quota](/moomoo-api-doc/en/intro/authority.html#9123). The historical
  candlestick quota you consume on that day will be automatically
  released after 30 days.
- A maximum of 60 requests per 30 seconds. Note: If you obtain data by
  page, this frequency limit rule is only applicable to the first time
  calling the interface, and subsequent pages request frequency is
  unlimited.
- *Change rate*, only supports timeframes of daily and above.
- **Options** related candlestick data, only supports 1 day, 1 minute, 5
  minutes, 15 minutes and 60 minutes.
- The pre-market, after-hours and overnight candlestick of US stocks,
  only supports timeframes of 60 minutes and below. Since the
  pre-market, after-hours and overnight session of the US stock market
  are irregular trading hours, the candlestick data for this period may
  be less than 2 years.
- *Turnover* of US stocks, only supports data after 2015-10-12.













