



# <a href="#6628" class="header-anchor">#</a> Get Historical Deals









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`history_deal_list_query(code='', deal_market=TrdMarket.NONE, start='', end='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0)`

- **Description**

  Query historical deal list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

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
  
    
  
  
   
  
  Only return orders whose related security symbols correspond to these
  codes.<br />
  If this parameter is not passed, return all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">deal_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter deals by security market.
  
    
  
  
   
  
  <ul>
  <li>Return historical deals for the specified market.</li>
  <li>If this parameter is not passed or the default NONE is used, return
  historical deals for all markets.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
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
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 90 days before ***end***. |
    | str | None | ***end*** is 90 days after ***start***. |
    | None | None | ***start*** is 90 days before, ***end*** is the current date. |

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
  <td>If ret == RET_OK, transaction list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Transaction list format as follows:
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
    <td style="text-align: left;">trd_side</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#832">TrdSide</a></td>
    <td style="text-align: left;">Trading direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">deal_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Deal number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Order ID.</td>
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
    <td style="text-align: left;">deal_market</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
    <td style="text-align: left;">Deal market.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Quantity of shares bought/sold on this
    fill.
    
      
    
    
     
    
    Option futures unit is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Fill price.
    
      
    
    
     
    
    3 decimal place accuracy, excess part will be rounded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">create_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Create time.
    
      
    
    
     
    
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">counter_broker_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Counter broker ID.
    
      
    
    
     
    
    Only valid for HK stocks.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">counter_broker_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Counter broker name.
    
      
    
    
     
    
    Only valid for HK stocks.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#4379">DealStatus</a></td>
    <td style="text-align: left;">Deal status.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.history_deal_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the order fill list is not empty
        print(data['deal_id'][0])  # Get the first deal ID of the history order fill list
        print(data['deal_id'].values.tolist())  # Convert to list
else:
    print('history_deal_list_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
    code stock_name                       deal_market       deal_id             order_id    qty  price trd_side              create_time  counter_broker_id counter_broker_name status
0  HK.00388      Hong Kong Exchanges and Clearing  HK  5056208452274069375  4665291631090960915  100.0  370.0      BUY  2020-09-17 21:15:59.979                  5                         OK)    
5056208452274069375
['5056208452274069375']
```









## <a href="#7585" class="header-anchor">#</a> Trd_GetHistoryOrderFillList.proto

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2222





`uint GetHistoryOrderFillList(TrdGetHistoryOrderFillList.Request req);`  
`virtual void OnReply_GetHistoryOrderFillList(FTAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderFillList.Response rsp);`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
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
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.CreateBuilder().Build();
        TrdGetHistoryOrderFillList.C2S c2s = TrdGetHistoryOrderFillList.C2S.CreateBuilder()
                .SetHeader(header)
                .SetFilterConditions(filter)
                .Build();
        TrdGetHistoryOrderFillList.Request req = TrdGetHistoryOrderFillList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetHistoryOrderFillList(req);
        Console.Write("Send TrdGetHistoryOrderFillList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetHistoryOrderFillList(FTAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderFillListResponse rsp)
    {
        Console.Write("Reply: TrdGetHistoryOrderFillList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827861023441251037
Send TrdGetHistoryOrderFillList: 3
Reply: TrdGetHistoryOrderFillList: 3
accID: 281756457888247915
```









`int getHistoryOrderFillList(TrdGetHistoryOrderFillList.Request req);`  
`void onReply_GetHistoryOrderFillList(FTAPI_Conn client, int nSerialNo, TrdGetHistoryOrderFillList.Response rsp);`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
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
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_US_VALUE)
                .build();
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.newBuilder()
                .setBeginTime("2021-03-01 00:00:00")
                .setEndTime("2021-04-01 00:00:00")
                .build();
        TrdGetHistoryOrderFillList.C2S c2s = TrdGetHistoryOrderFillList.C2S.newBuilder()
                .setHeader(header)
                .setFilterConditions(filter)
                .build();
        TrdGetHistoryOrderFillList.Request req = TrdGetHistoryOrderFillList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getHistoryOrderFillList(req);
        System.out.printf("Send TrdGetHistoryOrderFillList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetHistoryOrderFillList(FTAPI_Conn client, int nSerialNo, TrdGetHistoryOrderFillList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetHistoryOrderFillList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetHistoryOrderFillList: %s\n", json);
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
Send TrdGetHistoryOrderFillList: 2
Receive TrdGetHistoryOrderFillList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 2
    },
    "orderFillList": [{
      "trdSide": 1,
      "fillID": "449150869556176742",
      "fillIDEx": "20210330_15680495_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1.4",
      "orderID": "6664320708369556828",
      "orderIDEx": "20210330_15680495_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1",
      "code": "FUTU",
      "name": "富途控股",
      "qty": 34.0,
      "price": 127.64,
      "createTime": "2021-03-30 09:34:24.019",
      "secMarket": 2,
      "createTimestamp": 1.617111264019109E9,
      "updateTimestamp": 1.617111264019109E9,
      "status": 0
    }]
  }
}
```









`Futu::u32_t GetHistoryOrderFillList(const Trd_GetHistoryOrderFillList::Request &stReq);`  
`virtual void OnReply_GetHistoryOrderFillList(Futu::u32_t nSerialNo, const Trd_GetHistoryOrderFillList::Response &stRsp) = 0;`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
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
        Trd_GetHistoryOrderFillList::Request req;
        Trd_GetHistoryOrderFillList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(281756456003951537L);
        header->set_trdenv(1);
        header->set_trdmarket(1);
        Trd_Common::TrdFilterConditions *filter = c2s->mutable_filterconditions();
        filter->set_begintime("2021-05-01 00:00:00");
        filter->set_endtime("2021-06-01 00:00:00");

        m_GetHistoryOrderFillListSerialNo = m_pTrdApi->GetHistoryOrderFillList(req);
        cout << "Request GetHistoryOrderFillList SerialNo: " << m_GetHistoryOrderFillListSerialNo << endl;
    }

    virtual void OnReply_GetHistoryOrderFillList(Futu::u32_t nSerialNo, const Trd_GetHistoryOrderFillList::Response &stRsp){
        if(nSerialNo == m_GetHistoryOrderFillListSerialNo)
        {
            cout << "OnReply_GetHistoryOrderFillList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetHistoryOrderFillListSerialNo;
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
Request GetHistoryOrderFillList SerialNo: 4
OnReply_GetHistoryOrderFillList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 1,
   "accID": "281756456003951537",
   "trdMarket": 1
  }
 }
}
```









`GetHistoryOrderFillList(req);`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetHistoryOrderFillList(){
    const { RetType } = Common
    const { TrdEnv, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ec16fde057a2e7a0'];
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
                        return item.trdEnv != TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK live trading environment account

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            filterConditions:{
                                beginTime:"2021-09-01 00:00:00",
                                endTime:"2021-09-30 00:00:00",
                            },
                        },
                    };

                    websocket.GetHistoryOrderFillList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetHistoryOrderFillList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetHistoryOrderFillList: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFillList": [{
    "trdSide": 1,
    "fillID": "932511865781776209",
    "fillIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1.2",
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.606",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522700.605828,
    "updateTimestamp": 1631522700.531,
    "status": 0
  }, {
    "trdSide": 1,
    "fillID": "2611798069690910040",
    "fillIDEx": "20210913_5915950_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld.2",
    "orderID": "9128832000130556480",
    "orderIDEx": "20210913_5915950_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld",
    "code": "00700",
    "name": "",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:40:19.183",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522419.18269,
    "updateTimestamp": 1631522419.005,
    "status": 0
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).





Tips

- Historical deals are arranged in reverse chronological order: later
  deals return first, followed by earlier deals.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`history_deal_list_query(code='', deal_market=TrdMarket.NONE, start='', end='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0)`

- **Description**

  Query historical deal list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

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
  
    
  
  
   
  
  Only return orders whose related security symbols correspond to these
  codes.<br />
  If this parameter is not passed, return all.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">deal_market</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
  <td style="text-align: left;">Filter deals by security market.
  
    
  
  
   
  
  <ul>
  <li>Return historical deals for the specified market.</li>
  <li>If this parameter is not passed or the default NONE is used, return
  historical deals for all markets.</li>
  </ul>
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">start</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Start time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
  </td>
  </tr>
  <tr>
  <td style="text-align: left;">end</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">End time.
  
    
  
  
   
  
  In strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS
  format.<br />
  For time zone of futures, please refer to <a
  href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
  Configuration</a>.
  
  
  
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
  </tbody>
  </table>

  - The combination of ***start*** and ***end*** is as follows
    | Start type | End type | Description |
    |:---|:---|:---|
    | str | str | ***start*** and ***end*** are the specified dates respectively. |
    | None | str | ***start*** is 90 days before ***end***. |
    | str | None | ***end*** is 90 days after ***start***. |
    | None | None | ***start*** is 90 days before, ***end*** is the current date. |

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
  <td>If ret == RET_OK, transaction list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Transaction list format as follows:
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
    <td style="text-align: left;">trd_side</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#832">TrdSide</a></td>
    <td style="text-align: left;">Trading direction.</td>
    </tr>
    <tr>
    <td style="text-align: left;">deal_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Deal number.</td>
    </tr>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Order ID.</td>
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
    <td style="text-align: left;">deal_market</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#6257">TrdMarket</a></td>
    <td style="text-align: left;">Deal market.</td>
    </tr>
    <tr>
    <td style="text-align: left;">qty</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Quantity of shares bought/sold on this
    fill.
    
      
    
    
     
    
    Option futures unit is "Contract".
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">price</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Fill price.
    
      
    
    
     
    
    3 decimal place accuracy, excess part will be rounded.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">create_time</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Create time.
    
      
    
    
     
    
    For time zone of futures, please refer to <a
    href="/moomoo-api-doc/en/opend/opend-cmd.html#149">OpenD
    Configuration</a>.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">counter_broker_id</td>
    <td style="text-align: left;">int</td>
    <td style="text-align: left;">Counter broker ID.
    
      
    
    
     
    
    Only valid for HK stocks.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">counter_broker_name</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Counter broker name.
    
      
    
    
     
    
    Only valid for HK stocks.
    
    
    
    </td>
    </tr>
    <tr>
    <td style="text-align: left;">status</td>
    <td style="text-align: left;"><a
    href="/moomoo-api-doc/en/trade/trade.html#4379">DealStatus</a></td>
    <td style="text-align: left;">Deal status.</td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.history_deal_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If the order fill list is not empty
        print(data['deal_id'][0])  # Get the first deal ID of the history order fill list
        print(data['deal_id'].values.tolist())  # Convert to list
else:
    print('history_deal_list_query error: ', data)
trd_ctx.close()  # Close the current connection
```





- **Output**



``` python
    code     stock_name      deal_market      deal_id             order_id      qty    price  trd_side     create_time          counter_broker_id counter_broker_name status
0  US.AAPL   Apple Inc.           US  5056208452274069375  4665291631090960915  100.0  370.0    BUY    2020-09-17 21:15:59.979          5                                 OK
5056208452274069375
['5056208452274069375']
```









## <a href="#7585-2" class="header-anchor">#</a> Trd_GetHistoryOrderFillList.proto

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2222





`uint GetHistoryOrderFillList(TrdGetHistoryOrderFillList.Request req);`  
`virtual void OnReply_GetHistoryOrderFillList(MMAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderFillList.Response rsp);`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program: MMSPI_Trd, MMSPI_Conn {
    MMAPI_Trd trd = new MMAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1); //Set client information
        trd.SetConnCallback(this); //Set connection callback
        trd.SetTrdCallback(this); //Set transaction callback
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
                .SetTrdEnv((int)TrdCommon.TrdEnv.TrdEnv_Real)
                .SetTrdMarket((int)TrdCommon.TrdMarket.TrdMarket_HK)
                .Build();
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.CreateBuilder().Build();
        TrdGetHistoryOrderFillList.C2S c2s = TrdGetHistoryOrderFillList.C2S.CreateBuilder()
                .SetHeader(header)
                .SetFilterConditions(filter)
                .Build();
        TrdGetHistoryOrderFillList.Request req = TrdGetHistoryOrderFillList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetHistoryOrderFillList(req);
        Console.Write("Send TrdGetHistoryOrderFillList: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetHistoryOrderFillList(MMAPI_Conn client, uint nSerialNo, TrdGetHistoryOrderFillListResponse rsp)
    {
        Console.Write("Reply: TrdGetHistoryOrderFillList: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827861023441251037
Send TrdGetHistoryOrderFillList: 3
Reply: TrdGetHistoryOrderFillList: 3
accID: 281756457888247915
```









`int getHistoryOrderFillList(TrdGetHistoryOrderFillList.Request req);`  
`void onReply_GetHistoryOrderFillList(MMAPI_Conn client, int nSerialNo, TrdGetHistoryOrderFillList.Response rsp);`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements MMSPI_Trd, MMSPI_Conn {
    MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1); //Set client information
        trd.setConnSpi(this); //Set connection callback
        trd.setTrdSpi(this); //Set transaction callback
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
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_US_VALUE)
                .build();
        TrdCommon.TrdFilterConditions filter = TrdCommon.TrdFilterConditions.newBuilder()
                .setBeginTime("2021-03-01 00:00:00")
                .setEndTime("2021-04-01 00:00:00")
                .build();
        TrdGetHistoryOrderFillList.C2S c2s = TrdGetHistoryOrderFillList.C2S.newBuilder()
                .setHeader(header)
                .setFilterConditions(filter)
                .build();
        TrdGetHistoryOrderFillList.Request req = TrdGetHistoryOrderFillList.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getHistoryOrderFillList(req);
        System.out.printf("Send TrdGetHistoryOrderFillList: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetHistoryOrderFillList(MMAPI_Conn client, int nSerialNo, TrdGetHistoryOrderFillList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetHistoryOrderFillList failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdGetHistoryOrderFillList: %s\n", json);
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
Send TrdGetHistoryOrderFillList: 2
Receive TrdGetHistoryOrderFillList: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 2
    },
    "orderFillList": [{
      "trdSide": 1,
      "fillID": "449150869556176742",
      "fillIDEx": "20210330_15680495_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1.4",
      "orderID": "6664320708369556828",
      "orderIDEx": "20210330_15680495_SQSWWgSYCStLVb7BDmx7kgAARgy31Nc1",
      "code": "FUTU",
      "name": "富途控股",
      "qty": 34.0,
      "price": 127.64,
      "createTime": "2021-03-30 09:34:24.019",
      "secMarket": 2,
      "createTimestamp": 1.617111264019109E9,
      "updateTimestamp": 1.617111264019109E9,
      "status": 0
    }]
  }
}
```









`moomoo::u32_t GetHistoryOrderFillList(const Trd_GetHistoryOrderFillList::Request &stReq);`  
`virtual void OnReply_GetHistoryOrderFillList(moomoo::u32_t nSerialNo, const Trd_GetHistoryOrderFillList::Response &stRsp) = 0;`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
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
        Trd_GetHistoryOrderFillList::Request req;
        Trd_GetHistoryOrderFillList::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(281756456003951537L);
        header->set_trdenv(1);
        header->set_trdmarket(1);
        Trd_Common::TrdFilterConditions *filter = c2s->mutable_filterconditions();
        filter->set_begintime("2021-05-01 00:00:00");
        filter->set_endtime("2021-06-01 00:00:00");

        m_GetHistoryOrderFillListSerialNo = m_pTrdApi->GetHistoryOrderFillList(req);
        cout << "Request GetHistoryOrderFillList SerialNo: " << m_GetHistoryOrderFillListSerialNo << endl;
    }

    virtual void OnReply_GetHistoryOrderFillList(moomoo::u32_t nSerialNo, const Trd_GetHistoryOrderFillList::Response &stRsp){
        if(nSerialNo == m_GetHistoryOrderFillListSerialNo)
        {
            cout << "OnReply_GetHistoryOrderFillList SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetHistoryOrderFillListSerialNo;
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
Request GetHistoryOrderFillList SerialNo: 4
OnReply_GetHistoryOrderFillList SerialNo: 4
{
 "retType": 0,
 "retMsg": "",
 "errCode": 0,
 "s2c": {
  "header": {
   "trdEnv": 1,
   "accID": "281756456003951537",
   "trdMarket": 1
  }
 }
}
```









`GetHistoryOrderFillList(req);`

- **Description**

  Query the historical transaction list of a specific trading account.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    required Trd_Common.TrdFilterConditions filterConditions = 2; //Filter condition
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
    required Trd_Common.TrdHeader header = 1; //Transaction public parameter header
    repeated Trd_Common.OrderFill orderFillList = 2; //Historical transaction list
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
> - For orderfill structure, refer to
>   [OrderFill](/moomoo-api-doc/en/trade/trade.html#9504)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdGetHistoryOrderFillList(){
    const { RetType } = Common
    const { TrdEnv, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, 'ec16fde057a2e7a0'];
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
                        return item.trdEnv != TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // The sample takes the first HK live trading environment account

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            filterConditions:{
                                beginTime:"2021-09-01 00:00:00",
                                endTime:"2021-09-30 00:00:00",
                            },
                        },
                    };

                    websocket.GetHistoryOrderFillList(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetHistoryOrderFillList: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetHistoryOrderFillList: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFillList": [{
    "trdSide": 1,
    "fillID": "932511865781776209",
    "fillIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1.2",
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.606",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522700.605828,
    "updateTimestamp": 1631522700.531,
    "status": 0
  }, {
    "trdSide": 1,
    "fillID": "2611798069690910040",
    "fillIDEx": "20210913_5915950_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld.2",
    "orderID": "9128832000130556480",
    "orderIDEx": "20210913_5915950_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld",
    "code": "00700",
    "name": "",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:40:19.183",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522419.18269,
    "updateTimestamp": 1631522419.005,
    "status": 0
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).





Tips

- Historical deals are arranged in reverse chronological order: later
  deals return first, followed by earlier deals.













