



# <a href="#9404" class="header-anchor">#</a> Get IPO Information









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_ipo_list(market)`

- **Description**

  Get IPO information of a specific market

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
  <td style="text-align: left;">Market identification.
  
    
  
  
   
  
  Note: Shanghai and Shenzhen are not distinguished here. Entering
  Shanghai or Shenzhen will return the stocks in the Shanghai and Shenzhen
  markets.
  
  
  
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
  <td>If ret == RET_OK, IPO data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - IPO data format as follows:
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
    <td style="text-align: left;">list_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date, expected listing date for US
    stocks.
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">list_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Listing date timestamp, expected listing
    date timestamp for US stocks.</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subscription code (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">issue_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total number of issuance (applicable to
    A-shares); Total quantity of issuance (applicable to US stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">online_issue_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Online issuance (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_upper_limit</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Subscription limit (applicable for
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_limit_market_value</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The market value required for maximium
    subscription (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_estimate_ipo_price</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Weather to estimate the issuance price
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Issuance price.
    
      
    
    
     
    
    Estimated value, for reference only, will change due to changes in data
    such as raised funds, issuance quantity, issuance costs, etc. The actual
    data will be updated as soon as it is released.
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">industry_pe_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Industry P/E ratio (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_estimate_winning_ratio</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether to estimate the winning rate
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Winning rate.
    
      
    
    
     
    
    <ul>
    <li>This field is in percentage form, so 20 is equivalent to 20%.</li>
    <li>The estimated value, for reference only, will change due to changes
    in data such as funds raised, issuance quantity, issuance costs, etc.
    The actual data will be updated as soon as it is released.</li>
    </ul>
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">issue_pe_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Issue P/E ratio (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subscription date string
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Subscription date timestamp (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time string of announcement date
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Timestamp of announcement date (applicable
    to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_has_won</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the winning number has been
    announced (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_num_data</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The winning number (applicable to
    A-shares).
    
      
    
    
     
    
    The format is similar:<br />
    The last "five" digits: 12345, 12346.<br />
    The last "six" digits: 123456.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest offer price (applicable to HK
    stocks); lowest issue price (applicable to US stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest offer price (applicable to HK
    stocks); highest issue price (applicable to US stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">list_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">List price (applicable to HK stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of shares per lot.</td>
    </tr>
    <tr>
    <td style="text-align: left;">entrance_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Entrance fee (applicable to HK
    stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_subscribe_status</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is it a subscription status.
    
      
    
    
     
    
    True: is subscribing, False: pending listing.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_end_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subscription deadline string
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    
    (applicable to HK stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_end_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Subscription deadline timestamp.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_ipo_list(Market.HK)
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code      name   list_time  list_timestamp apply_code issue_size online_issue_size apply_upper_limit apply_limit_market_value is_estimate_ipo_price ipo_price industry_pe_rate is_estimate_winning_ratio winning_ratio issue_pe_rate apply_time apply_timestamp winning_time winning_timestamp is_has_won winning_num_data  ipo_price_min  ipo_price_max  list_price  lot_size  entrance_price  is_subscribe_status apply_end_time  apply_end_timestamp
0  HK.06666  Evergrande Property Services Group Limited  2020-12-02    1.606838e+09        N/A        N/A               N/A               N/A                      N/A                   N/A       N/A              N/A                       N/A           N/A           N/A        N/A             N/A          N/A               N/A        N/A              N/A          8.500           9.75         0.0       500         4924.12                 True     2020-11-26         1.606352e+09
1  HK.02110                    Yue Kan Holdings Limited  2020-12-07    1.607270e+09        N/A        N/A               N/A               N/A                      N/A                   N/A       N/A              N/A                       N/A           N/A           N/A        N/A             N/A          N/A               N/A        N/A              N/A          0.225           0.27         0.0     10000         2727.21                 True     2020-11-27         1.606439e+09
HK.06666
['HK.06666', 'HK.02110']
```









## <a href="#4600" class="header-anchor">#</a> Qot_GetIpoList.proto

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, Futu subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3217





`uint GetIpoList(QotGetIpoList.Request req);`  
`virtual void OnReply_GetIpoList(FTAPI_Conn client, uint nSerialNo, QotGetIpoList.Response rsp);`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, Futu subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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

        QotGetIpoList.C2S c2s = QotGetIpoList.C2S.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_CNSH_Security)
                .Build();
        QotGetIpoList.Request req = QotGetIpoList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetIpoList(req);
        Console.Write("Send QotGetIpoList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetIpoList(FTAPI_Conn client, uint nSerialNo, QotGetIpoList.Response rsp)
    {
        Console.Write("Reply: QotGetIpoList: {0}\n", nSerialNo);
        if(rsp.S2C.IpoListCount > 0)
        {
            Console.Write("name: {0} \n", rsp.S2C.IpoListList[0].Basic.Name);
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
Qot onInitConnect: ret=0 desc= connID=6826061149989914129
Send QotGetIpoList: 3
Reply: QotGetIpoList: 3
name: Joy Kie Corporation
```









`int getIpoList(QotGetIpoList.Request req);`  
`void onReply_GetIpoList(FTAPI_Conn client, int nSerialNo, QotGetIpoList.Response rsp);`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, Futu subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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

        QotGetIpoList.C2S c2s = QotGetIpoList.C2S.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .build();
        QotGetIpoList.Request req = QotGetIpoList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getIpoList(req);
        System.out.printf("Send QotGetIpoList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetIpoList(FTAPI_Conn client, int nSerialNo, QotGetIpoList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetIpoList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetIpoList: %s\n", json);
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
Send QotGetIpoList: 2
Receive QotGetIpoList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "ipoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "02155"
        },
        "name": "Morimatsu International Holdings",
        "listTime": "2021-06-28",
        "listTimestamp": 1.6248096E9
      },
      "hkExData": {
        "ipoPriceMin": 2.2,
        "ipoPriceMax": 2.48,
        "listPrice": 2.48,
        "lotSize": 1000,
        "entrancePrice": 2504.98,
        "isSubscribeStatus": false,
        "applyEndTime": "2021-06-18",
        "applyEndTimestamp": 1.623978E9
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "02162"
        },
        "name": "Keymed Biosciences Inc.",
        "listTime": "2021-07-08",
        "listTimestamp": 1.6256736E9
      },
      "hkExData": {
        "ipoPriceMin": 50.5,
        "ipoPriceMax": 53.3,
        "listPrice": 0.0,
        "lotSize": 500,
        "entrancePrice": 26918.55,
        "isSubscribeStatus": true,
        "applyEndTime": "2021-06-30",
        "applyEndTimestamp": 1.6250148E9
      }
    }]
  }
}
```









`Futu::u32_t GetIpoList(const Qot_GetIpoList::Request &stReq);`  
`virtual void OnReply_GetIpoList(Futu::u32_t nSerialNo, const Qot_GetIpoList::Response &stRsp) = 0;`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, Futu subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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
        Qot_GetIpoList::Request req;
        Qot_GetIpoList::C2S *c2s = req.mutable_c2s();
        c2s->set_market(1);

        m_GetIpoListSerialNo = m_pQotApi->GetIpoList(req);
        cout << "Request GetIpoList SerialNo: " << m_GetIpoListSerialNo << endl;
    }

    virtual void OnReply_GetIpoList(Futu::u32_t nSerialNo, const Qot_GetIpoList::Response &stRsp){
        if(nSerialNo == m_GetIpoListSerialNo)
        {
            cout << "OnReply_GetIpoList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Qot *m_pQotApi;

    Futu::u32_t m_GetIpoListSerialNo;
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
Request GetIpoList SerialNo: 4
OnReply_GetIpoList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "ipoList": [
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "06699"
     },
     "name": "Angelalign Technology Inc.",
     "listTime": "2021-06-16",
     "listTimestamp": 1623772800
    },
    "hkExData": {
     "ipoPriceMin": 147,
     "ipoPriceMax": 173,
     "listPrice": 0,
     "lotSize": 200,
     "entrancePrice": 34948.66,
     "isSubscribeStatus": false,
     "applyEndTime": "2021-06-08",
     "applyEndTimestamp": 1623119400
    }
   },
...
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "04246"
     },
     "name": "HKGB c 2406",
     "listTime": "2021-06-24",
     "listTimestamp": 1624464000
    },
    "hkExData": {
     "ipoPriceMin": 100,
     "ipoPriceMax": 100,
     "listPrice": 0,
     "lotSize": 100,
     "entrancePrice": 10000,
     "isSubscribeStatus": true,
     "applyEndTime": "2021-06-11",
     "applyEndTimestamp": 1623378600
    }
   }
  ]
 }
}
```









`GetIpoList(req);`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, Futu subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common } from "futu-api/proto";
import beautify from "js-beautify";

function QotGetIpoList(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    market: QotMarket.QotMarket_US_Security,
                },
            };

            websocket.GetIpoList(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("IpoList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
IpoList: errCode 0, retMsg , retType 0
{
  "ipoList": [{
    "basic": {
      "security": {
        "market": 11,
        "code": "FHLTU"
      },
      "name": "Future Health ESG Corp.",
      "listTime": "2021-09-10",
      "listTimestamp": 1631246400
    },
    "usExData": {
      "ipoPriceMin": 10,
      "ipoPriceMax": 10,
      "issueSize": "20000000"
    }
  }, {
    "basic": {
      "security": {
        "market": 11,
        "code": "FLAG.U"
      },
      "name": "FIRST LIGHT ACQUISITION GROUP, INC.",
      "listTime": "2021-09-10",
      "listTimestamp": 1631246400
    },
    "usExData": {
      "ipoPriceMin": 10,
      "ipoPriceMax": 10,
      "issueSize": "20000000"
    }
  }, ..., {
    "basic": {
      "security": {
        "market": 11,
        "code": "ROXA"
      },
      "name": "ROX FINANCIAL LP",
      "listTime": "2021-09-30",
      "listTimestamp": 1632974400
    },
    "usExData": {
      "ipoPriceMin": 10,
      "ipoPriceMax": 10,
      "issueSize": "8300000"
    }
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





`get_ipo_list(market)`

- **Description**

  Get IPO information of a specific market

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
  <td style="text-align: left;">Market identification.
  
    
  
  
   
  
  Note: Shanghai and Shenzhen are not distinguished here. Entering
  Shanghai or Shenzhen will return the stocks in the Shanghai and Shenzhen
  markets.
  
  
  
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
  <td>If ret == RET_OK, IPO data is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - IPO data format as follows:
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
    <td style="text-align: left;">list_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Listing date, expected listing date for US
    stocks.
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">list_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Listing date timestamp, expected listing
    date timestamp for US stocks.</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_code</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subscription code (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">issue_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Total number of issuance (applicable to
    A-shares); Total quantity of issuance (applicable to US stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">online_issue_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Online issuance (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_upper_limit</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Subscription limit (applicable for
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_limit_market_value</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">The market value required for maximium
    subscription (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_estimate_ipo_price</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Weather to estimate the issuance price
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Issuance price.
    
      
    
    
     
    
    Estimated value, for reference only, will change due to changes in data
    such as raised funds, issuance quantity, issuance costs, etc. The actual
    data will be updated as soon as it is released.
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">industry_pe_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Industry P/E ratio (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_estimate_winning_ratio</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether to estimate the winning rate
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_ratio</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Winning rate.
    
      
    
    
     
    
    <ul>
    <li>This field is in percentage form, so 20 is equivalent to 20%.</li>
    <li>The estimated value, for reference only, will change due to changes
    in data such as funds raised, issuance quantity, issuance costs, etc.
    The actual data will be updated as soon as it is released.</li>
    </ul>
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">issue_pe_rate</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Issue P/E ratio (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subscription date string
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Subscription date timestamp (applicable to
    A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Time string of announcement date
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    
    (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Timestamp of announcement date (applicable
    to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_has_won</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Whether the winning number has been
    announced (applicable to A-shares).</td>
    </tr>
    <tr>
    <td style="text-align: left;">winning_num_data</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">The winning number (applicable to
    A-shares).
    
      
    
    
     
    
    The format is similar:<br />
    The last "five" digits: 12345, 12346.<br />
    The last "six" digits: 123456.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_price_min</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Lowest offer price (applicable to HK
    stocks); lowest issue price (applicable to US stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">ipo_price_max</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Highest offer price (applicable to HK
    stocks); highest issue price (applicable to US stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">list_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">List price (applicable to HK stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">lot_size</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Number of shares per lot.</td>
    </tr>
    <tr>
    <td style="text-align: left;">entrance_price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Entrance fee (applicable to HK
    stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">is_subscribe_status</td>
    <td style="text-align: left;">bool</td>
    <td style="text-align: left;">Is it a subscription status.
    
      
    
    
     
    
    True: is subscribing, False: pending listing.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_end_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Subscription deadline string
    
      
    
    
     
    
    Format：yyyy-MM-dd
    
    
    
    
    (applicable to HK stocks).</td>
    </tr>
    <tr>
    <td style="text-align: left;">apply_end_timestamp</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Subscription deadline timestamp.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

ret, data = quote_ctx.get_ipo_list(Market.HK)
if ret == RET_OK:
    print(data)
    print(data['code'][0]) # Take the first stock code
    print(data['code'].values.tolist()) # Convert to list
else:
    print('error:', data)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```





- **Output**



``` python
    code      name   list_time  list_timestamp apply_code issue_size online_issue_size apply_upper_limit apply_limit_market_value is_estimate_ipo_price ipo_price industry_pe_rate is_estimate_winning_ratio winning_ratio issue_pe_rate apply_time apply_timestamp winning_time winning_timestamp is_has_won winning_num_data  ipo_price_min  ipo_price_max  list_price  lot_size  entrance_price  is_subscribe_status apply_end_time  apply_end_timestamp
0  HK.06666  Evergrande Property Services Group Limited  2020-12-02    1.606838e+09        N/A        N/A               N/A               N/A                      N/A                   N/A       N/A              N/A                       N/A           N/A           N/A        N/A             N/A          N/A               N/A        N/A              N/A          8.500           9.75         0.0       500         4924.12                 True     2020-11-26         1.606352e+09
1  HK.02110                    Yue Kan Holdings Limited  2020-12-07    1.607270e+09        N/A        N/A               N/A               N/A                      N/A                   N/A       N/A              N/A                       N/A           N/A           N/A        N/A             N/A          N/A               N/A        N/A              N/A          0.225           0.27         0.0     10000         2727.21                 True     2020-11-27         1.606439e+09
HK.06666
['HK.06666', 'HK.02110']
```









## <a href="#4600-2" class="header-anchor">#</a> Qot_GetIpoList.proto

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, moomoo subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  3217





`uint GetIpoList(QotGetIpoList.Request req);`  
`virtual void OnReply_GetIpoList(MMAPI_Conn client, uint nSerialNo, QotGetIpoList.Response rsp);`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, moomoo subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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

        QotGetIpoList.C2S c2s = QotGetIpoList.C2S.CreateBuilder()
                .SetMarket((int)QotCommon.QotMarket.QotMarket_CNSH_Security)
                .Build();
        QotGetIpoList.Request req = QotGetIpoList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = qot.GetIpoList(req);
        Console.Write("Send QotGetIpoList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Qot onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetIpoList(MMAPI_Conn client, uint nSerialNo, QotGetIpoList.Response rsp)
    {
        Console.Write("Reply: QotGetIpoList: {0}\n", nSerialNo);
        if(rsp.S2C.IpoListCount > 0)
        {
            Console.Write("name: {0} \n", rsp.S2C.IpoListList[0].Basic.Name);
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
Qot onInitConnect: ret=0 desc= connID=6826061149989914129
Send QotGetIpoList: 3
Reply: QotGetIpoList: 3
name: Joy Kie Corporation
```









`int getIpoList(QotGetIpoList.Request req);`  
`void onReply_GetIpoList(MMAPI_Conn client, int nSerialNo, QotGetIpoList.Response rsp);`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, moomoo subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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

        QotGetIpoList.C2S c2s = QotGetIpoList.C2S.newBuilder()
                .setMarket(QotCommon.QotMarket.QotMarket_HK_Security_VALUE)
                .build();
        QotGetIpoList.Request req = QotGetIpoList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = qot.getIpoList(req);
        System.out.printf("Send QotGetIpoList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Qot onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetIpoList(MMAPI_Conn client, int nSerialNo, QotGetIpoList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("QotGetIpoList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive QotGetIpoList: %s\n", json);
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
Send QotGetIpoList: 2
Receive QotGetIpoList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "ipoList": [{
      "basic": {
        "security": {
          "market": 1,
          "code": "02155"
        },
        "name": "Morimatsu International Holdings",
        "listTime": "2021-06-28",
        "listTimestamp": 1.6248096E9
      },
      "hkExData": {
        "ipoPriceMin": 2.2,
        "ipoPriceMax": 2.48,
        "listPrice": 2.48,
        "lotSize": 1000,
        "entrancePrice": 2504.98,
        "isSubscribeStatus": false,
        "applyEndTime": "2021-06-18",
        "applyEndTimestamp": 1.623978E9
      }
    }, ... {
      "basic": {
        "security": {
          "market": 1,
          "code": "02162"
        },
        "name": "Keymed Biosciences Inc.",
        "listTime": "2021-07-08",
        "listTimestamp": 1.6256736E9
      },
      "hkExData": {
        "ipoPriceMin": 50.5,
        "ipoPriceMax": 53.3,
        "listPrice": 0.0,
        "lotSize": 500,
        "entrancePrice": 26918.55,
        "isSubscribeStatus": true,
        "applyEndTime": "2021-06-30",
        "applyEndTimestamp": 1.6250148E9
      }
    }]
  }
}
```









`moomoo::u32_t GetIpoList(const Qot_GetIpoList::Request &stReq);`  
`virtual void OnReply_GetIpoList(moomoo::u32_t nSerialNo, const Qot_GetIpoList::Response &stRsp) = 0;`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, moomoo subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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
        Qot_GetIpoList::Request req;
        Qot_GetIpoList::C2S *c2s = req.mutable_c2s();
        c2s->set_market(1);

        m_GetIpoListSerialNo = m_pQotApi->GetIpoList(req);
        cout << "Request GetIpoList SerialNo: " << m_GetIpoListSerialNo << endl;
    }

    virtual void OnReply_GetIpoList(moomoo::u32_t nSerialNo, const Qot_GetIpoList::Response &stRsp){
        if(nSerialNo == m_GetIpoListSerialNo)
        {
            cout << "OnReply_GetIpoList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Qot *m_pQotApi;

    moomoo::u32_t m_GetIpoListSerialNo;
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
Request GetIpoList SerialNo: 4
OnReply_GetIpoList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "ipoList": [
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "06699"
     },
     "name": "Angelalign Technology Inc.",
     "listTime": "2021-06-16",
     "listTimestamp": 1623772800
    },
    "hkExData": {
     "ipoPriceMin": 147,
     "ipoPriceMax": 173,
     "listPrice": 0,
     "lotSize": 200,
     "entrancePrice": 34948.66,
     "isSubscribeStatus": false,
     "applyEndTime": "2021-06-08",
     "applyEndTimestamp": 1623119400
    }
   },
...
   {
    "basic": {
     "security": {
      "market": 1,
      "code": "04246"
     },
     "name": "HKGB c 2406",
     "listTime": "2021-06-24",
     "listTimestamp": 1624464000
    },
    "hkExData": {
     "ipoPriceMin": 100,
     "ipoPriceMax": 100,
     "listPrice": 0,
     "lotSize": 100,
     "entrancePrice": 10000,
     "isSubscribeStatus": true,
     "applyEndTime": "2021-06-11",
     "applyEndTimestamp": 1623378600
    }
   }
  ]
 }
}
```









`GetIpoList(req);`

- **Description**

  Get IPO information of a specific market

- **Parameters**



``` protobuf
message C2S
{
    required int32 market = 1; //Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks. Shanghai stocks and Shenzhen stocks do not distinguish between each other, either of each represent the A-share market.
}

message Request
{
    required C2S c2s = 1;
}
```





> - For market type, refer to
>   [QotMarket](/moomoo-api-doc/en/quote/quote.html#456)

- **Return**



``` protobuf
// Ipo basic data
message BasicIpoData
{
    required Qot_Common.Security security = 1; // Qot_Common::QotMarket. stock market, supports Shanghai stocks and Shenzhen stocks, and Shanghai stocks and Shenzhen stocks represent the A-share market without distinction.
    required string name = 2; // Stock name
    optional string listTime = 3; // List date string (Format: yyyy-MM-dd)
    optional double listTimestamp = 4; // List date timestamp
}

// A-share Ipo list additional data
message CNIpoExData
{
    required string applyCode = 1; //Subscription code
    required int64 issueSize = 2; //Total number of issues
    required int64 onlineIssueSize = 3; //Online issuance 
    required int64 applyUpperLimit = 4; //Subscription limit
    required int64 applyLimitMarketValue = 5; //The market value required for maximium subscription
    required bool isEstimateIpoPrice = 6; //Weather to estimate the issuance price
    required double ipoPrice = 7; //Estimated value, for reference only, will change due to changes in data such as raised funds, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double industryPeRate = 8; //Industry P/E ratio
    required bool isEstimateWinningRatio = 9; //Whether to estimate the winning rate
    required double winningRatio = 10; //Winning rate is in percentage form, so 20 is equivalent to 20%. The estimated value, for reference only, will change due to changes in data such as funds raised, issuance quantity, issuance costs, etc. The actual data will be updated as soon as it is released. Applicable to A-shares
    required double issuePeRate = 11; //Issuance P/E ratio
    optional string applyTime = 12; //Subscription date string (Format: yyyy-MM-dd)
    optional double applyTimestamp = 13; //Subscription date timestamp
    optional string winningTime = 14; //Time string of announcement date (Format: yyyy-MM-dd)
    optional double winningTimestamp = 15; //Timestamp of announcement date
    required bool isHasWon = 16; //Whether the winning number has been announced
    repeated WinningNumData winningNumData = 17; // Qot_GetIpoList::WinningNumData. The winning number
}

// Winning number data
message WinningNumData
{
    required string winningName = 1; //Winning group name
    required string winningInfo = 2; //Winning number information
}

// Additional data for HK stock Ipo list
message HKIpoExData
{
    required double ipoPriceMin = 1; //Lowest offer price
    required double ipoPriceMax = 2; //Highest offer price
    required double listPrice = 3; //List price
    required int32 lotSize = 4; //Number of shares per lot
    required double entrancePrice = 5; //Entrance fee
    required bool isSubscribeStatus = 6; //Is it a subscription status, True-is subscribing, False-to be listed
    optional string applyEndTime = 7; //Subscription deadline string (Format: yyyy-MM-dd)
    optional double applyEndTimestamp = 8; //Time stamp of the subscription deadline. Due to the process of subscription procedures, moomoo subscription deadline will be earlier than the date announced by the exchange.
}

// Additional data on the US stock Ipo list
message USIpoExData
{
    required double ipoPriceMin = 1; //Lowest issue price
    required double ipoPriceMax = 2; //Highest issue price
    required int64 issueSize = 3; //Issuance size
}

// IPO data
message IpoData
{
    required BasicIpoData basic = 1; //IPO basic data
    optional CNIpoExData cnExData = 2; //Additional data for A-share IPO
    optional HKIpoExData hkExData = 3; //Additional data for HK stocks IPO
    optional USIpoExData usExData = 4; //Additional data for US stocks IPO
}

message S2C
{
    repeated IpoData ipoList = 1; //IPO data of new shares
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
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function QotGetIpoList(){
    const { RetType } = Common
    const { QotMarket } = Qot_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new mmWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { 

            const req = {
                c2s: {
                    market: QotMarket.QotMarket_US_Security,
                },
            };

            websocket.GetIpoList(req)
            .then((res) => {
                let { errCode, retMsg, retType,s2c } = res
                console.log("IpoList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
IpoList: errCode 0, retMsg , retType 0
{
  "ipoList": [{
    "basic": {
      "security": {
        "market": 11,
        "code": "FHLTU"
      },
      "name": "Future Health ESG Corp.",
      "listTime": "2021-09-10",
      "listTimestamp": 1631246400
    },
    "usExData": {
      "ipoPriceMin": 10,
      "ipoPriceMax": 10,
      "issueSize": "20000000"
    }
  }, {
    "basic": {
      "security": {
        "market": 11,
        "code": "FLAG.U"
      },
      "name": "FIRST LIGHT ACQUISITION GROUP, INC.",
      "listTime": "2021-09-10",
      "listTimestamp": 1631246400
    },
    "usExData": {
      "ipoPriceMin": 10,
      "ipoPriceMax": 10,
      "issueSize": "20000000"
    }
  }, ..., {
    "basic": {
      "security": {
        "market": 11,
        "code": "ROXA"
      },
      "name": "ROX FINANCIAL LP",
      "listTime": "2021-09-30",
      "listTimestamp": 1632974400
    },
    "usExData": {
      "ipoPriceMin": 10,
      "ipoPriceMax": 10,
      "issueSize": "8300000"
    }
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds













