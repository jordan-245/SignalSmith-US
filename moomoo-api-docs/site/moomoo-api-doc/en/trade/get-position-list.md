



# <a href="#5126" class="header-anchor">#</a> Get Positions









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`position_list_query(code='', position_market=TrdMarket.NONE, pl_ratio_min=None, pl_ratio_max=None, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, refresh_cache=False)`

- **Description**

  Query the holding position list of a specific trading account

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
  <td style="text-align: left;">Security symbol.
  
    
  
  
   
  
  <ul>
  <li>Only return orders whose related security symbols correspond to
  these codes. If this parameter is not passed, return all.</li>
  <li>Note: For the code filtering of futures positions, you need to pass
  the contract code with a specific month, and it cannot be filtered by
  the future main contract code.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">position_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter positions by market.
  
    
  
  
   
  
  <ul>
  <li>Return positions for the specified market.</li>
  <li>If this parameter is not passed, return positions for all
  markets.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">pl_ratio_min</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The lower limit of the current gain or
  loss ratio filter.
  
    
  
  
   
  
  The securities account uses profit ratio on the diluted cost price,
  while the futures account uses the profit rate on the average cost
  price.<br />
  For example: when 10 is passed, the positions with gain or loss ratio
  greater than +10% will be returned.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">pl_ratio_max</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The upper limit of the current gain or
  loss ratio filter.
  
    
  
  
   
  
  The securities account uses profit ratio on the diluted cost price,
  while the futures account uses the profit rate on the average cost
  price.<br />
  For example: when 10 is passed, the positions with gain or loss ratio
  less than +10% will be returned.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trd_env</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
  <td style="text-align: left;">Trading environment.</td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_id</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Trading account ID.
  
    
  
  
   
  
  <ul>
  <li>When acc_id is 0, the account specified by acc_index is chosen.</li>
  <li>When acc_id is set the ID number (not 0), the account specified by
  acc_id is chosen.</li>
  <li>Using acc_id to query and trade is strongly recommended, acc_index
  will change when adding/closing an account, result in the account you
  specify is inconsistent with the actual trading account.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_index</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The account number in the trading account
  list.
  
    
  
  
   
  
  The default is 0, which means the first trading account.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">refresh_cache</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to refresh the cache.
  
    
  
  
   
  
  <ul>
  <li>True: Re-request data from the Futu server immediately, without
  using the OpenD cache. At this time, it will be restricted by the
  interface frequency limit.</li>
  <li>False: Use OpenD's cache (The cache needs to be refreshed if it is
  not updated in rare circumstances.</li>
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
  <td rowspan="2">data</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, list of positions is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - List of positions format as follows:
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
    <td style="text-align: left;">position_side</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7930">PositionSide</a></td>
    <td style="text-align: left;">Position direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">position_market</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
    <td style="text-align: left;">Position market.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The number of holdings.
    
      
    
    
     
    
    The unit of options and futures is "contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">can_sell_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Available quantity.
    
      
    
    
     
    
    Available quantity = Holding quantity - Frozen quantity<br />
    The unit of options and futures is "contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">currency</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
    <td style="text-align: left;">Transaction currency.</td>
    </tr>
    <tr>
    <td style="text-align: left;">nominal_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Market price.
    
      
    
    
     
    
    3 decimal place accuracy, excess part will be rounded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cost_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Diluted Cost (for securities account).
    Average Cost (for futures account).
    
      
    
    
     
    
    It is recommended to use the fields of average_cost and diluted_cost to
    obtain the cost price
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cost_price_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the cost price is valid.
    
      
    
    
     
    
    True: valid.<br />
    False: invalid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">average_cost</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average cost price
    
      
    
    
     
    
    Not valid for securities paper trading accounts<br />
    Minimum version requirement: 9.2.5208
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">diluted_cost</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Diluted cost price
    
      
    
    
     
    
    Not valid for futures trading accounts<br />
    Minimum version requirement: 9.2.5208
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Market value.
    
      
    
    
     
    
    3 decimal places accuracy(2 decimal places for A-shares, and 0 decimal
    place for futures).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Proportion of gain or loss(under diluted
    cost price)
    
      
    
    
     
    
    This field is in percentage form, so 20 is equavalent to 20%.<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_ratio_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the gain or loss ratio is valid.
    
      
    
    
     
    
    True: valid.<br />
    False: invalid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_ratio_avg_cost</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Proportion of gain or loss(under average
    cost price)
    
      
    
    
     
    
    This field is in percentage form, so 20 is equavalent to 20%.<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Gain or loss.
    
      
    
    
     
    
    3 decimal places accuracy(2 decimal places for A-shares).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_val_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the gain or loss is valid.
    
      
    
    
     
    
    True: valid.<br />
    False: invalid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_pl_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Gain or loss today.
    
      
    
    
     
    
    3 decimal places accuracy(2 decimal places for A-shares).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_trd_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_buy_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total volume purchased today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_buy_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total amount purchased today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_sell_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total volume sold today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_sell_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total amount sold today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">unrealized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Unrealized gain or loss.
    
      
    
    
     
    
    Not valid for securities paper trading accounts<br />
    It is the unrealized profit and loss under the average cost price, for
    universal securities accounts
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">realized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Realized gain or loss.
    
      
    
    
     
    
    Not valid for securities paper trading accounts<br />
    It is the realized profit and loss under the average cost price, for
    universal securities accounts
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.position_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the position list is not empty
        print(data['stock_name'][0])  # Get the first stock name of the holding position
        print(data['stock_name'].values.tolist())  # Convert to list
else:
    print('position_list_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
       code stock_name position_market    qty  can_sell_qty  cost_price  cost_price_valid average_cost  diluted_cost  market_val  nominal_price  pl_ratio  pl_ratio_valid pl_ratio_avg_cost  pl_val  pl_val_valid today_buy_qty today_buy_val today_pl_val today_trd_val today_sell_qty today_sell_val position_side unrealized_pl realized_pl currency
0  HK.01810   XIAOMI-W              HK  400.0         400.0      53.975              True          53.975        53.975     19760.0           49.4 -8.476146            True            -8.476146    -1830.0          True           0.0           0.0          0.0           0.0            0.0            0.0          LONG           0.0         0.0      HKD
XIAOMI-W
['XIAOMI-W']
```









## <a href="#3557" class="header-anchor">#</a> Trd_GetPositionList.proto

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2102





`uint GetPositionList(TrdGetPositionList.Request req);`  
`virtual void OnReply_GetPositionList(FTAPI_Conn client, uint nSerialNo, TrdGetPositionList.Response rsp);`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdGetPositionList.C2S c2s = TrdGetPositionList.C2S.CreateBuilder()
                .SetHeader(header)
            .Build();
        TrdGetPositionList.Request req = TrdGetPositionList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetPositionList(req);
        Console.Write("Send TrdGetPositionList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetPositionList(FTAPI_Conn client, uint nSerialNo, TrdGetPositionList.Response rsp)
    {
        Console.Write("Reply: TrdGetPositionList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6826813359715968249
Send TrdGetPositionList: 3
Reply: TrdGetPositionList: 3
accID: 281756457888247915
```









`int getPositionList(TrdGetPositionList.Request req);`  
`void onReply_GetPositionList(FTAPI_Conn client, int nSerialNo, TrdGetPositionList.Response rsp);`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
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
        TrdGetPositionList.C2S c2s = TrdGetPositionList.C2S.newBuilder()
                .setHeader(header)
            .build();
        TrdGetPositionList.Request req = TrdGetPositionList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getPositionList(req);
        System.out.printf("Send TrdGetPositionList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPositionList(FTAPI_Conn client, int nSerialNo, TrdGetPositionList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetPositionList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetPositionList: %s\n", json);
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
Send TrdGetPositionList: 2
Receive TrdGetPositionList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "positionList": [{
      "positionID": "804953599703017051",
      "positionSide": 0,
      "code": "00700",
      "name": "Tencent",
      "qty": 100.0,
      "canSellQty": 100.0,
      "price": 594.0,
      "costPrice": 594.0,
      "val": 59400.0,
      "plVal": 0.0,
      "plRatio": 0.0,
      "secMarket": 1,
      "dilutedCostPrice": 594.0,
      "averageCostPrice": 594.0,
      "averagePlRatio": 0.0
    }]
  }
}
```









`Futu::u32_t GetPositionList(const Trd_GetPositionList::Request &stReq);`  
`virtual void OnReply_GetPositionList(Futu::u32_t nSerialNo, const Trd_GetPositionList::Response &stRsp) = 0;`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
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
        Trd_GetPositionList::Request req;
        Trd_GetPositionList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        
        m_GetPositionListSerialNo = m_pTrdApi->GetPositionList(req);
        cout << "Request GetPositionList SerialNo: " << m_GetPositionListSerialNo << endl;
    }

    virtual void OnReply_GetPositionList(Futu::u32_t nSerialNo, const Trd_GetPositionList::Response &stRsp){
        if(nSerialNo == m_GetPositionListSerialNo)
        {
            cout << "OnReply_GetPositionList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetPositionListSerialNo;
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
Request GetPositionList SerialNo: 4
OnReply_GetPositionList SerialNo: 4
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
  "positionList": [
   {
    "positionID": "806833430706896474",
    "positionSide": 0,
    "code": "00700",
    "name": "Tencent",
    "qty": 300,
    "canSellQty": 300,
    "price": 601,
    "costPrice": 611.5,
    "val": 180300,
    "plVal": -3150,
    "plRatio": -0.017170891251022,
    "secMarket": 1,
    "dilutedCostPrice": 611.5,
    "averageCostPrice": 611.5,
    "averagePlRatio": -0.017170891251022
   }
  ]
 }
}
```









`GetPositionList(req);`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetPositionList(){
    const { RetType } = Common
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
                        },
                    };

                    websocket.GetPositionList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetPositionList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetPositionList: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "positionList": [{
    "positionID": "3411713033831199757",
    "positionSide": 0,
    "code": "00700",
    "name": "Tencent",
    "qty": 1900,
    "canSellQty": 1900,
    "price": 477,
    "costPrice": 454.558,
    "val": 906300,
    "plVal": 42640,
    "plRatio": 0.049371280364958,
    "secMarket": 1,
    "dilutedCostPrice": 454.558,
    "averageCostPrice": 5454.558,
    "averagePlRatio": 0.049371280364958
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- Call this interface, only when the cache is refreshed, will it be
  restricted by the frequency limit











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`position_list_query(code='', position_market=TrdMarket.NONE, pl_ratio_min=None, pl_ratio_max=None, trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, refresh_cache=False)`

- **Description**

  Query the holding position list of a specific trading account

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
  <td style="text-align: left;">Security symbol.
  
    
  
  
   
  
  <ul>
  <li>Only return orders whose related security symbols correspond to
  these codes. If this parameter is not passed, return all.</li>
  <li>Note: For the code filtering of futures positions, you need to pass
  the contract code with a specific month, and it cannot be filtered by
  the future main contract code.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">position_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter positions by market.
  
    
  
  
   
  
  <ul>
  <li>Return positions for the specified market.</li>
  <li>If this parameter is not passed, return positions for all
  markets.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">pl_ratio_min</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The lower limit of the current gain or
  loss ratio filter.
  
    
  
  
   
  
  The securities account uses profit ratio on the diluted cost price,
  while the futures account uses the profit rate on the average cost
  price.<br />
  For example: when 10 is passed, the positions with gain or loss ratio
  greater than +10% will be returned.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">pl_ratio_max</td>
  <td style="text-align: left;">float</td>
  <td style="text-align: left;">The upper limit of the current gain or
  loss ratio filter.
  
    
  
  
   
  
  The securities account uses profit ratio on the diluted cost price,
  while the futures account uses the profit rate on the average cost
  price.<br />
  For example: when 10 is passed, the positions with gain or loss ratio
  less than +10% will be returned.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">trd_env</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#48">TrdEnv</a></td>
  <td style="text-align: left;">Trading environment.</td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_id</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">Trading account ID.
  
    
  
  
   
  
  <ul>
  <li>When acc_id is 0, the account specified by acc_index is chosen.</li>
  <li>When acc_id is set the ID number (not 0), the account specified by
  acc_id is chosen.</li>
  <li>Using acc_id to query and trade is strongly recommended, acc_index
  will change when adding/closing an account, result in the account you
  specify is inconsistent with the actual trading account.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">acc_index</td>
  <td style="text-align: left;">int</td>
  <td style="text-align: left;">The account number in the trading account
  list.
  
    
  
  
   
  
  The default is 0, which means the first trading account.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">refresh_cache</td>
  <td style="text-align: left;">bool</td>
  <td style="text-align: left;">Whether to refresh the cache.
  
    
  
  
   
  
  <ul>
  <li>True: Re-request data from the Futu server immediately, without
  using the OpenD cache. At this time, it will be restricted by the
  interface frequency limit.</li>
  <li>False: Use OpenD's cache (The cache needs to be refreshed if it is
  not updated in rare circumstances.</li>
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
  <td rowspan="2">data</td>
  <td>pd.DataFrame</td>
  <td>If ret == RET_OK, list of positions is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - List of positions format as follows:
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
    <td style="text-align: left;">position_side</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#7930">PositionSide</a></td>
    <td style="text-align: left;">Position direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security code.</td>
    </tr>
    <tr>
    <td style="text-align: left;">stock_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Security name.</td>
    </tr>
    <tr>
    <td style="text-align: left;">position_market</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
    <td style="text-align: left;">Position market.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">The number of holdings.
    
      
    
    
     
    
    The unit of options and futures is "contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">can_sell_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Available quantity.
    
      
    
    
     
    
    Available quantity = Holding quantity - Frozen quantity<br />
    The unit of options and futures is "contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">currency</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#1655">Currency</a></td>
    <td style="text-align: left;">Transaction currency.</td>
    </tr>
    <tr>
    <td style="text-align: left;">nominal_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Market price.
    
      
    
    
     
    
    3 decimal place accuracy, excess part will be rounded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cost_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Diluted Cost (for securities account).
    Average Cost (for futures account).
    
      
    
    
     
    
    It is recommended to use the fields of average_cost and diluted_cost to
    obtain the cost price
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">cost_price_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the cost price is valid.
    
      
    
    
     
    
    True: valid.<br />
    False: invalid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">average_cost</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Average cost price
    
      
    
    
     
    
    Not valid for securities paper trading accounts<br />
    Minimum version requirement: 9.2.5208
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">diluted_cost</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Diluted cost price
    
      
    
    
     
    
    Not valid for futures trading accounts<br />
    Minimum version requirement: 9.2.5208
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">market_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Market value.
    
      
    
    
     
    
    3 decimal places accuracy(2 decimal places for A-shares, and 0 decimal
    place for futures).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Proportion of gain or loss(under diluted
    cost price)
    
      
    
    
     
    
    This field is in percentage form, so 20 is equavalent to 20%.<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_ratio_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the gain or loss ratio is valid.
    
      
    
    
     
    
    True: valid.<br />
    False: invalid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_ratio_avg_cost</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Proportion of gain or loss(under average
    cost price)
    
      
    
    
     
    
    This field is in percentage form, so 20 is equavalent to 20%.<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Gain or loss.
    
      
    
    
     
    
    3 decimal places accuracy(2 decimal places for A-shares).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">pl_val_valid</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the gain or loss is valid.
    
      
    
    
     
    
    True: valid.<br />
    False: invalid.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_pl_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Gain or loss today.
    
      
    
    
     
    
    3 decimal places accuracy(2 decimal places for A-shares).
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_trd_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Transaction amount today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_buy_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total volume purchased today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_buy_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total amount purchased today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_sell_qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total volume sold today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">today_sell_val</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total amount sold today.
    
      
    
    
     
    
    Only valid in the real trading environment.<br />
    3 decimal places accuracy(2 decimal places for A-shares).<br />
    Not applicable to futures.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">unrealized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Unrealized gain or loss.
    
      
    
    
     
    
    Not valid for securities paper trading accounts<br />
    It is the unrealized profit and loss under the average cost price, for
    universal securities accounts
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">realized_pl</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Realized gain or loss.
    
      
    
    
     
    
    Not valid for securities paper trading accounts<br />
    It is the realized profit and loss under the average cost price, for
    universal securities accounts
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.position_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the position list is not empty
        print(data['stock_name'][0])  # Get the first stock name of the holding position
        print(data['stock_name'].values.tolist())  # Convert to list
else:
    print('position_list_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
       code stock_name position_market    qty  can_sell_qty  cost_price  cost_price_valid average_cost  diluted_cost  market_val  nominal_price  pl_ratio  pl_ratio_valid pl_ratio_avg_cost  pl_val  pl_val_valid today_buy_qty today_buy_val today_pl_val today_trd_val today_sell_qty today_sell_val position_side unrealized_pl realized_pl currency
0  US.AAPL   Apple Inc.              US  400.0         400.0      53.975              True          53.975        53.975     19760.0           49.4 -8.476146            True            -8.476146    -1830.0          True           0.0           0.0          0.0           0.0            0.0            0.0          LONG           0.0         0.0      USD
Apple Inc.
['Apple Inc.']
```









## <a href="#3557-2" class="header-anchor">#</a> Trd_GetPositionList.proto

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2102





`uint GetPositionList(TrdGetPositionList.Request req);`  
`virtual void OnReply_GetPositionList(FTAPI_Conn client, uint nSerialNo, TrdGetPositionList.Response rsp);`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdGetPositionList.C2S c2s = TrdGetPositionList.C2S.CreateBuilder()
                .SetHeader(header)
            .Build();
        TrdGetPositionList.Request req = TrdGetPositionList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetPositionList(req);
        Console.Write("Send TrdGetPositionList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetPositionList(FTAPI_Conn client, uint nSerialNo, TrdGetPositionList.Response rsp)
    {
        Console.Write("Reply: TrdGetPositionList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6826813359715968249
Send TrdGetPositionList: 3
Reply: TrdGetPositionList: 3
accID: 281756457888247915
```









`int getPositionList(TrdGetPositionList.Request req);`  
`void onReply_GetPositionList(FTAPI_Conn client, int nSerialNo, TrdGetPositionList.Response rsp);`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
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
        TrdGetPositionList.C2S c2s = TrdGetPositionList.C2S.newBuilder()
                .setHeader(header)
            .build();
        TrdGetPositionList.Request req = TrdGetPositionList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getPositionList(req);
        System.out.printf("Send TrdGetPositionList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetPositionList(FTAPI_Conn client, int nSerialNo, TrdGetPositionList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetPositionList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetPositionList: %s\n", json);
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
Send TrdGetPositionList: 2
Receive TrdGetPositionList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 0,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "positionList": [{
      "positionID": "804953599703017051",
      "positionSide": 0,
      "code": "00700",
      "name": "Tencent",
      "qty": 100.0,
      "canSellQty": 100.0,
      "price": 594.0,
      "costPrice": 594.0,
      "val": 59400.0,
      "plVal": 0.0,
      "plRatio": 0.0,
      "secMarket": 1,
      "dilutedCostPrice": 594.0,
      "averageCostPrice": 594.0,
      "averagePlRatio": 0.0
    }]
  }
}
```









`Futu::u32_t GetPositionList(const Trd_GetPositionList::Request &stReq);`  
`virtual void OnReply_GetPositionList(Futu::u32_t nSerialNo, const Trd_GetPositionList::Response &stRsp) = 0;`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
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
        Trd_GetPositionList::Request req;
        Trd_GetPositionList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(3637840);
        header->set_trdenv(0);
        header->set_trdmarket(1);
        
        m_GetPositionListSerialNo = m_pTrdApi->GetPositionList(req);
        cout << "Request GetPositionList SerialNo: " << m_GetPositionListSerialNo << endl;
    }

    virtual void OnReply_GetPositionList(Futu::u32_t nSerialNo, const Trd_GetPositionList::Response &stRsp){
        if(nSerialNo == m_GetPositionListSerialNo)
        {
            cout << "OnReply_GetPositionList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetPositionListSerialNo;
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
Request GetPositionList SerialNo: 4
OnReply_GetPositionList SerialNo: 4
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
  "positionList": [
   {
    "positionID": "806833430706896474",
    "positionSide": 0,
    "code": "00700",
    "name": "Tencent",
    "qty": 300,
    "canSellQty": 300,
    "price": 601,
    "costPrice": 611.5,
    "val": 180300,
    "plVal": -3150,
    "plRatio": -0.017170891251022,
    "secMarket": 1,
    "dilutedCostPrice": 611.5,
    "averageCostPrice": 611.5,
    "averagePlRatio": -0.017170891251022
   }
  ]
 }
}
```









`GetPositionList(req);`

- **Description**

  Query the holding position list of a specific trading account

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    optional Trd_Common.TrdFilterConditions filterConditions = 2; //Filter conditions
    optional double filterPLRatioMin = 3; //the lower limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional double filterPLRatioMax = 4; //the upper limit of the current gain or loss ratio filter. The securities account uses profit ratio on the diluted cost price, while the futures account uses the profit rate on the average cost price.
    optional bool refreshCache = 4; //Refresh the data cached by OpenD immediately, it is not filled by default. True gets the latest data from the server to update the cache and returns. If this field is flase or blank, it returns the data cached by OpenD, and will not request the server.
    //Under normal circumstances,  the cached data of OpenD is in sync with server, so there is no need to force an update. It's faster to use the local cached data, and will not cause any pressure on server.
    //If you encounter packet loss, etc., the cached data may be inconsistent with the server. If the user finds that the data is not the latest, they can set this flag to true to update the cache and get latest data.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)
> - For filter condition structure, refer to
>   [TrdFilterConditions](/moomoo-api-doc/en/trade/trade.html#9070)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.Position positionList = 2; //List of positions
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
> - For position structure, refer to
>   [Position](/moomoo-api-doc/en/trade/trade.html#5027)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetPositionList(){
    const { RetType } = Common
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
                        },
                    };

                    websocket.GetPositionList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetPositionList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetPositionList: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 0,
    "accID": "6684972",
    "trdMarket": 1
  },
  "positionList": [{
    "positionID": "3411713033831199757",
    "positionSide": 0,
    "code": "00700",
    "name": "Tencent",
    "qty": 1900,
    "canSellQty": 1900,
    "price": 477,
    "costPrice": 454.558,
    "val": 906300,
    "plVal": 42640,
    "plRatio": 0.049371280364958,
    "secMarket": 1,
    "dilutedCostPrice": 454.558,
    "averageCostPrice": 5454.558,
    "averagePlRatio": 0.049371280364958
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- Call this interface, only when the cache is refreshed, will it be
  restricted by the frequency limit













