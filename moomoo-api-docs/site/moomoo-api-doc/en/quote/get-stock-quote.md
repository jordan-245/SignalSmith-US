



# <a href="#7720" class="header-anchor">#</a> Get Real-time Quote









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_stock_quote(code_list)`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**

  | Parameter | Type | Description                                           |
  |:----------|:-----|:------------------------------------------------------|
  | code_list | list | Stock list. Data type of elements in the list is str. |

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
  <td>If ret == RET_OK, quotation data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - quotation data format as follows:
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
    <td style="text-align: left;">data_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Date.</td>
    </tr>
    <tr>
    <td style="text-align: left;">data_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time of latest price.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Latest price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">open_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">prev_close_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
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
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">amplitude</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether trading is suspended.
    
      
    
    
     
    
    True: suspension
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date.
    
      
    
    
     
    
    yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price_spread</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spread.</td>
    </tr>
    <tr>
    <td style="text-align: left;">dark_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6341">DarkStatus</a></td>
    <td style="text-align: left;">Grey market transaction status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">sec_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#4415">SecurityStatus</a></td>
    <td style="text-align: left;">Stock status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">contract_size</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract size.</td>
    </tr>
    <tr>
    <td style="text-align: left;">open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of open positions.</td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_volatility</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Implied volatility.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Premium.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Delta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">gamma</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Gamma.</td>
    </tr>
    <tr>
    <td style="text-align: left;">vega</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Vega.</td>
    </tr>
    <tr>
    <td style="text-align: left;">theta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Theta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">rho</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Rho.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
    <td style="text-align: left;">Index option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">net_open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net open contract number.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">expiry_date_distance</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of days from the expiry date.
    
      
    
    
     
    
    a negative number means it has expired.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">contract_nominal_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract nominal amount.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">owner_lot_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Equal number of underlying stocks.
    
      
    
    
     
    
    Index options do not have this field , only HK options support this
    field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_area_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3628">OptionAreaType</a></td>
    <td style="text-align: left;">Option type (by exercise time).</td>
    </tr>
    <tr>
    <td style="text-align: left;">contract_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract multiplier.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Pre-market volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">After-hours volume.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">After_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours turnover.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Overnight volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_settle_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">position</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Holding position.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">position_change</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Daily position change.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(['US.AAPL'], [SubType.QUOTE], subscribe_push=False)
# Subscribe to the K line type first. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
     ret, data = quote_ctx.get_stock_quote(['US.AAPL']) # Get real-time data of subscription stock quotes
     if ret == RET_OK:
         print(data)
         print(data['code'][0]) # Take the first stock code
         print(data['code'].values.tolist()) # Convert to list
     else:
         print('error:', data)
else:
     print('subscription failed', err_message)
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code name   data_date     data_time  last_price  open_price  high_price  low_price  prev_close_price     volume      turnover  turnover_rate  amplitude  suspension listing_date  price_spread dark_status sec_status strike_price contract_size open_interest implied_volatility premium delta gamma vega theta  rho net_open_interest expiry_date_distance contract_nominal_value owner_lot_multiplier option_area_type contract_multiplier last_settle_price position position_change index_option_type  pre_price  pre_high_price  pre_low_price  pre_volume  pre_turnover  pre_change_val  pre_change_rate  pre_amplitude  after_price  after_high_price  after_low_price  after_volume  after_turnover  after_change_val  after_change_rate  after_amplitude  overnight_price  overnight_high_price  overnight_low_price  overnight_volume  overnight_turnover  overnight_change_val  overnight_change_rate  overnight_amplitude
0  US.AAPL   APPLE  2025-04-07  05:37:21.794      188.38      193.89      199.88     187.34            203.19  125910913  2.424473e+10          0.838      6.172       False   1980-12-12          0.01         N/A     NORMAL          N/A           N/A           N/A                N/A     N/A   N/A   N/A  N/A   N/A  N/A               N/A                  N/A                    N/A                  N/A              N/A                 N/A               N/A      N/A             N/A               N/A     181.43          181.98         177.47      288853   52132735.18           -6.95           -3.689          2.394        186.6           188.639           186.44       3151311    5.930968e+08             -1.78             -0.944           1.1673           176.94                 186.5                174.4            533115         94944250.56                -11.44                 -6.072               6.4231
US.AAPL
['US.AAPL']
```









## <a href="#5740" class="header-anchor">#</a> Qot_GetBasicQot.proto

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3004





`uint GetBasicQot(QotGetBasicQot.Request req);`  
`virtual void OnReply_GetBasicQot(FTAPI_Conn client, uint nSerialNo, QotGetBasicQot.Response rsp);`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Basic)
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
        QotGetBasicQot.C2S c2s = QotGetBasicQot.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .Build();
        QotGetBasicQot.Request req = QotGetBasicQot.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetBasicQot(req);
        Console.Write("Send QotGetBasicQot: {0}\n", seqNo);
    }

    public void OnReply_GetBasicQot(FTAPI_Conn client, uint nSerialNo, QotGetBasicQot.Response rsp)
    {
        Console.Write("Reply: QotGetBasicQot: {0}\n", nSerialNo);
        Console.Write("curPrice: {0}\n", rsp.S2C.BasicQotListList[0].CurPrice);
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
Qot onInitConnect: ret=0 desc= connID=6825668646977718703
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetBasicQot: 4
Reply: QotGetBasicQot: 4
curPrice: 459
```









`int getBasicQot(QotGetBasicQot.Request req);`  
`void onReply_GetBasicQot(FTAPI_Conn client, int nSerialNo, QotGetBasicQot.Response rsp);`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
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
                .addSubTypeList(QotCommon.SubType.SubType_Basic_VALUE)
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
        QotGetBasicQot.C2S c2s = QotGetBasicQot.C2S.newBuilder()
                .addSecurityList(sec)
                .build();
        QotGetBasicQot.Request req = QotGetBasicQot.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getBasicQot(req);
        System.out.printf("Send QotGetBasicQot: %d\n", seqNo);
    }

    @Override
    public void onReply_GetBasicQot(FTAPI_Conn client, int nSerialNo, QotGetBasicQot.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetBasicQot failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetBasicQot: %s\n", json);
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
Send QotGetBasicQot: 3
Receive QotGetBasicQot: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "basicQotList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "isSuspended": false,
      "listTime": "2004-06-16",
      "priceSpread": 0.5,
      "updateTime": "2021-06-24 16:08:14",
      "highPrice": 587.5,
      "openPrice": 584.0,
      "lowPrice": 580.0,
      "curPrice": 583.0,
      "lastClosePrice": 582.5,
      "volume": "10947302",
      "turnover": 6.387238277E9,
      "turnoverRate": 0.114,
      "amplitude": 1.288,
      "darkStatus": 0,
      "listTimestamp": 1.0873152E9,
      "updateTimestamp": 1.624522094E9,
      "secStatus": 1
    }]
  }
}
```









`Futu::u32_t GetBasicQot(const Qot_GetBasicQot::Request &stReq);`  
`virtual void OnReply_GetBasicQot(Futu::u32_t nSerialNo, const Qot_GetBasicQot::Response &stRsp) = 0;`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Basic);
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
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }

            // construct request message
            Qot_GetBasicQot::Request req;
            Qot_GetBasicQot::C2S *c2s = req.mutable_c2s();
            auto secList = c2s->mutable_securitylist();
            Qot_Common::Security *sec = secList->Add();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            
            m_GetBasicQotSerialNo = m_pQotApi->GetBasicQot(req);
            cout << "Request GetBasicQot SerialNo: " << m_GetBasicQotSerialNo << endl;
        }
    }

    virtual void OnReply_GetBasicQot(Futu::u32_t nSerialNo, const Qot_GetBasicQot::Response &stRsp){
        if(nSerialNo == m_GetBasicQotSerialNo)
        {
            cout << "OnReply_GetBasicQot SerialNo: " << nSerialNo << endl; 
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
    Futu::u32_t m_GetBasicQotSerialNo;
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
Request GetBasicQot SerialNo: 4
OnReply_GetBasicQot SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "basicQotList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "isSuspended": false,
    "listTime": "2004-06-16",
    "priceSpread": 0.5,
    "updateTime": "2021-06-09 14:08:24",
    "highPrice": 606,
    "openPrice": 600,
    "lowPrice": 597.5,
    "curPrice": 601.5,
    "lastClosePrice": 601,
    "volume": "4283211",
    "turnover": 2579419163,
    "turnoverRate": 0.045,
    "amplitude": 1.414,
    "darkStatus": 0,
    "listTimestamp": 1087315200,
    "updateTimestamp": 1623218904,
    "secStatus": 1
   }
  ]
 }
}
```









`GetBasicQot(req);`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetBasicQot(){
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
                subTypeList: [ SubType.SubType_Basic ], 
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true,
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                    securityList: [
                        {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                    ],
                    },
                };
                websocket.GetBasicQot(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("BasicQot: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                    if(retType == RetType.RetType_Succeed){
                        let s2c = beautify(JSON.stringify(s2c), {
                            indent_size: 2,
                            space_in_empty_paren: true,
                        });
                        console.log(s2c);
                    }
                })
                .catch((error) => {
                    console.log("error:", error);
                });

            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("error:", error.retMsg);
                }
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
BasicQot: errCode 0, retMsg , retType 0
{
  "basicQotList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "isSuspended": false,
    "listTime": "2004-06-16",
    "priceSpread": 0.2,
    "updateTime": "2021-09-09 16:08:17",
    "highPrice": 511.5,
    "openPrice": 509,
    "lowPrice": 479,
    "curPrice": 480,
    "lastClosePrice": 524.5,
    "volume": "54090872",
    "turnover": 26716845932,
    "turnoverRate": 0.563,
    "amplitude": 6.196,
    "darkStatus": 0,
    "listTimestamp": 1087315200,
    "updateTimestamp": 1631174897,
    "secStatus": 1
  }]
}
stop
```











Tips

- This API provides the function to obtain real-time data at one time.
  If you need to obtain pushed data continuously, please refer to the
  [Real-time Quote
  Callback](/moomoo-api-doc/en/quote/update-stock-quote.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_stock_quote(code_list)`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**

  | Parameter | Type | Description                                           |
  |:----------|:-----|:------------------------------------------------------|
  | code_list | list | Stock list. Data type of elements in the list is str. |

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
  <td>If ret == RET_OK, quotation data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - quotation data format as follows:
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
    <td style="text-align: left;">data_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Date.</td>
    </tr>
    <tr>
    <td style="text-align: left;">data_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time of latest price.
    
      
    
    
     
    
    Format: yyyy-MM-dd HH:mm:ss<br />
    The default of HK stock market and A-share market is Beijing time, while
    that of US stock market is US Eastern time.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Latest price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">open_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Open.</td>
    </tr>
    <tr>
    <td style="text-align: left;">high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">High.</td>
    </tr>
    <tr>
    <td style="text-align: left;">low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">prev_close_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.</td>
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
    <td style="text-align: left;">turnover_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Turnover rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">amplitude</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">suspension</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether trading is suspended.
    
      
    
    
     
    
    True: suspension
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">listing_date</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date.
    
      
    
    
     
    
    yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price_spread</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Spread.</td>
    </tr>
    <tr>
    <td style="text-align: left;">dark_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#6341">DarkStatus</a></td>
    <td style="text-align: left;">Grey market transaction status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">sec_status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#4415">SecurityStatus</a></td>
    <td style="text-align: left;">Stock status.</td>
    </tr>
    <tr>
    <td style="text-align: left;">strike_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Strike price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">contract_size</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract size.</td>
    </tr>
    <tr>
    <td style="text-align: left;">open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of open positions.</td>
    </tr>
    <tr>
    <td style="text-align: left;">implied_volatility</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Implied volatility.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">premium</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Premium.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">delta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Delta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">gamma</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Gamma.</td>
    </tr>
    <tr>
    <td style="text-align: left;">vega</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Vega.</td>
    </tr>
    <tr>
    <td style="text-align: left;">theta</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Theta.</td>
    </tr>
    <tr>
    <td style="text-align: left;">rho</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Greek value Rho.</td>
    </tr>
    <tr>
    <td style="text-align: left;">index_option_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#2866">IndexOptionType</a></td>
    <td style="text-align: left;">Index option type.</td>
    </tr>
    <tr>
    <td style="text-align: left;">net_open_interest</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Net open contract number.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">expiry_date_distance</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The number of days from the expiry date.
    
      
    
    
     
    
    a negative number means it has expired.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">contract_nominal_value</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract nominal amount.
    
      
    
    
     
    
    Only HK options support this field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">owner_lot_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Equal number of underlying stocks.
    
      
    
    
     
    
    Index options do not have this field , only HK options support this
    field.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">option_area_type</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/quote/quote.html#3628">OptionAreaType</a></td>
    <td style="text-align: left;">Option type (by exercise time).</td>
    </tr>
    <tr>
    <td style="text-align: left;">contract_multiplier</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Contract multiplier.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Pre-market volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pre_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Pre-market amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">After-hours volume.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">After_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours turnover.
    
      
    
    
     
    
    The Sci-tech Innovation Board supports this data.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">after_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">after_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">After-hours amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight price.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_high_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight high.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_low_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight low.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_volume</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Overnight volume.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_turnover</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight turnover.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change.</td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_change_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight change rate.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">overnight_amplitude</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Overnight amplitude.
    
      
    
    
     
    
    This field is in percentage form, so 20 is equivalent to 20%.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">last_settle_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Yesterday's close.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">position</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Holding position.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">position_change</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Daily position change.
    
      
    
    
     
    
    Specific field for futures.
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret_sub, err_message = quote_ctx.subscribe(['US.AAPLE'], [SubType.QUOTE], subscribe_push=False)
# Subscribe to the K line type first. After the subscription is successful, OpenD will continue to receive pushes from the server, False means that there is no need to push to the script temporarily
if ret_sub == RET_OK: # Subscription successful
     ret, data = quote_ctx.get_stock_quote(['US.AAPL']) # Get real-time data of subscription stock quotes
     if ret == RET_OK:
         print(data)
         print(data['code'][0]) # Take the first stock code
         print(data['code'].values.tolist()) # Convert to list
     else:
         print('error:', data)
else:
     print('subscription failed', err_message)
quote_ctx.close() # Close the current connection, OpenD will automatically cancel the corresponding type of subscription for the corresponding stock after 1 minute
```





- **Output**



``` python
code name   data_date     data_time  last_price  open_price  high_price  low_price  prev_close_price     volume      turnover  turnover_rate  amplitude  suspension listing_date  price_spread dark_status sec_status strike_price contract_size open_interest implied_volatility premium delta gamma vega theta  rho net_open_interest expiry_date_distance contract_nominal_value owner_lot_multiplier option_area_type contract_multiplier last_settle_price position position_change index_option_type  pre_price  pre_high_price  pre_low_price  pre_volume  pre_turnover  pre_change_val  pre_change_rate  pre_amplitude  after_price  after_high_price  after_low_price  after_volume  after_turnover  after_change_val  after_change_rate  after_amplitude  overnight_price  overnight_high_price  overnight_low_price  overnight_volume  overnight_turnover  overnight_change_val  overnight_change_rate  overnight_amplitude
0  US.AAPL   APPLE  2025-04-07  05:37:21.794      188.38      193.89      199.88     187.34            203.19  125910913  2.424473e+10          0.838      6.172       False   1980-12-12          0.01         N/A     NORMAL          N/A           N/A           N/A                N/A     N/A   N/A   N/A  N/A   N/A  N/A               N/A                  N/A                    N/A                  N/A              N/A                 N/A               N/A      N/A             N/A               N/A     181.43          181.98         177.47      288853   52132735.18           -6.95           -3.689          2.394        186.6           188.639           186.44       3151311    5.930968e+08             -1.78             -0.944           1.1673           176.94                 186.5                174.4            533115         94944250.56                -11.44                 -6.072               6.4231
US.AAPL
['US.AAPL']
```









## <a href="#5740-2" class="header-anchor">#</a> Qot_GetBasicQot.proto

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3004





`uint GetBasicQot(QotGetBasicQot.Request req);`  
`virtual void OnReply_GetBasicQot(MMAPI_Conn client, uint nSerialNo, QotGetBasicQot.Response rsp);`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
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
                .AddSubTypeList((int)QotCommon.SubType.SubType_Basic)
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
        QotGetBasicQot.C2S c2s = QotGetBasicQot.C2S.CreateBuilder()
                .AddSecurityList(sec)
                .Build();
        QotGetBasicQot.Request req = QotGetBasicQot.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetBasicQot(req);
        Console.Write("Send QotGetBasicQot: {0}\n", seqNo);
    }

    public void OnReply_GetBasicQot(MMAPI_Conn client, uint nSerialNo, QotGetBasicQot.Response rsp)
    {
        Console.Write("Reply: QotGetBasicQot: {0}\n", nSerialNo);
        Console.Write("curPrice: {0}\n", rsp.S2C.BasicQotListList[0].CurPrice);
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
Qot onInitConnect: ret=0 desc= connID=6825668646977718703
Send QotSub: 3
Reply: QotSub: 3  retType: 0
retMsg: ""
errCode: 0

Send QotGetBasicQot: 4
Reply: QotGetBasicQot: 4
curPrice: 459
```









`int getBasicQot(QotGetBasicQot.Request req);`  
`void onReply_GetBasicQot(MMAPI_Conn client, int nSerialNo, QotGetBasicQot.Response rsp);`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
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
                .addSubTypeList(QotCommon.SubType.SubType_Basic_VALUE)
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
        QotGetBasicQot.C2S c2s = QotGetBasicQot.C2S.newBuilder()
                .addSecurityList(sec)
                .build();
        QotGetBasicQot.Request req = QotGetBasicQot.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getBasicQot(req);
        System.out.printf("Send QotGetBasicQot: %d\n", seqNo);
    }

    @Override
    public void onReply_GetBasicQot(MMAPI_Conn client, int nSerialNo, QotGetBasicQot.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetBasicQot failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetBasicQot: %s\n", json);
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
Send QotGetBasicQot: 3
Receive QotGetBasicQot: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "basicQotList": [{
      "security": {
        "market": 1,
        "code": "00700"
      },
      "isSuspended": false,
      "listTime": "2004-06-16",
      "priceSpread": 0.5,
      "updateTime": "2021-06-24 16:08:14",
      "highPrice": 587.5,
      "openPrice": 584.0,
      "lowPrice": 580.0,
      "curPrice": 583.0,
      "lastClosePrice": 582.5,
      "volume": "10947302",
      "turnover": 6.387238277E9,
      "turnoverRate": 0.114,
      "amplitude": 1.288,
      "darkStatus": 0,
      "listTimestamp": 1.0873152E9,
      "updateTimestamp": 1.624522094E9,
      "secStatus": 1
    }]
  }
}
```









`moomoo::u32_t GetBasicQot(const Qot_GetBasicQot::Request &stReq);`  
`virtual void OnReply_GetBasicQot(moomoo::u32_t nSerialNo, const Qot_GetBasicQot::Response &stRsp) = 0;`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
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
        c2s->add_subtypelist(Qot_Common::SubType::SubType_Basic);
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
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "Sub Failed" << endl;
                return;
            }

            // construct request message
            Qot_GetBasicQot::Request req;
            Qot_GetBasicQot::C2S *c2s = req.mutable_c2s();
            auto secList = c2s->mutable_securitylist();
            Qot_Common::Security *sec = secList->Add();
            sec->set_code("00700");
            sec->set_market(Qot_Common::QotMarket::QotMarket_HK_Security);
            
            m_GetBasicQotSerialNo = m_pQotApi->GetBasicQot(req);
            cout << "Request GetBasicQot SerialNo: " << m_GetBasicQotSerialNo << endl;
        }
    }

    virtual void OnReply_GetBasicQot(moomoo::u32_t nSerialNo, const Qot_GetBasicQot::Response &stRsp){
        if(nSerialNo == m_GetBasicQotSerialNo)
        {
            cout << "OnReply_GetBasicQot SerialNo: " << nSerialNo << endl; 
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
    moomoo::u32_t m_GetBasicQotSerialNo;
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
Request GetBasicQot SerialNo: 4
OnReply_GetBasicQot SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "basicQotList": [
   {
    "security": {
     "market": 1,
     "code": "00700"
    },
    "isSuspended": false,
    "listTime": "2004-06-16",
    "priceSpread": 0.5,
    "updateTime": "2021-06-09 14:08:24",
    "highPrice": 606,
    "openPrice": 600,
    "lowPrice": 597.5,
    "curPrice": 601.5,
    "lastClosePrice": 601,
    "volume": "4283211",
    "turnover": 2579419163,
    "turnoverRate": 0.045,
    "amplitude": 1.414,
    "darkStatus": 0,
    "listTimestamp": 1087315200,
    "updateTimestamp": 1623218904,
    "secStatus": 1
   }
  ]
 }
}
```









`GetBasicQot(req);`

- **Description**

  To get real-time quotes of subscribed securities, you must subscribe
  first.

- **Parameters**



``` protobuf
message C2S
{
    repeated Qot_Common.Security securityList = 1; //Security
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
    repeated Qot_Common.BasicQot basicQotList = 1; //Basic stock market
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType,returned value
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For basic quotation structure, refer to
>   [BasicQot](/moomoo-api-doc/en/quote/quote.html#8930)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetBasicQot(){
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
                subTypeList: [ SubType.SubType_Basic ], 
                isSubOrUnSub: true, 
                isRegOrUnRegPush: true,
                },
            })
            .then((res) => { 

                const req = {
                    c2s: {
                    securityList: [
                        {
                            market: QotMarket.QotMarket_HK_Security,
                            code: "00700",
                        },
                    ],
                    },
                };
                websocket.GetBasicQot(req)
                .then((res) => {
                    let { errCode, retMsg, retType,s2c } = res
                    console.log("BasicQot: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
                    if(retType == RetType.RetType_Succeed){
                        let s2c = beautify(JSON.stringify(s2c), {
                            indent_size: 2,
                            space_in_empty_paren: true,
                        });
                        console.log(s2c);
                    }
                })
                .catch((error) => {
                    console.log("error:", error);
                });

            })
            .catch((error) => {
                if ("retMsg" in error) {
                    console.log("error:", error.retMsg);
                }
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
BasicQot: errCode 0, retMsg , retType 0
{
  "basicQotList": [{
    "security": {
      "market": 1,
      "code": "00700"
    },
    "isSuspended": false,
    "listTime": "2004-06-16",
    "priceSpread": 0.2,
    "updateTime": "2021-09-09 16:08:17",
    "highPrice": 511.5,
    "openPrice": 509,
    "lowPrice": 479,
    "curPrice": 480,
    "lastClosePrice": 524.5,
    "volume": "54090872",
    "turnover": 26716845932,
    "turnoverRate": 0.563,
    "amplitude": 6.196,
    "darkStatus": 0,
    "listTimestamp": 1087315200,
    "updateTimestamp": 1631174897,
    "secStatus": 1
  }]
}
stop
```











Tips

- This API provides the function to obtain real-time data at one time.
  If you need to obtain pushed data continuously, please refer to the
  [Real-time Quote
  Callback](/moomoo-api-doc/en/quote/update-stock-quote.html) API.
- For the difference between get real-time data and real-time data
  callback, please refer to [How to Get Real-time Quotes Through
  Subscription Interface](/moomoo-api-doc/en/qa/quote.html#5505).













