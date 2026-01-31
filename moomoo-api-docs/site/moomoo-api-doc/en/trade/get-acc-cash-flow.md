



# <a href="#6104" class="header-anchor">#</a> Get Account Cash Flow









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_acc_cash_flow(clearing_date='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, cashflow_direction=CashFlowDirection.NONE)`

- **Description**

  Query the cash flow list of a specified trading account on a specified
  date. This includes all transactions that affect cash balances, such
  as deposits/withdrawals, fund transfers, currency exchanges,
  buying/selling financial assets, margin interest, and securities
  lending interest.

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
  <td style="text-align: left;">clearing_date</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Clearing date.
  
    
  
  
   
  
  Query each day separately with YYYY-MM-DD format (e.g.,'2017-06-20').
  
  
  
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
  <td style="text-align: left;">cashflow_direction</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#1384">CashFlowDirection</a></td>
  <td style="text-align: left;">Filter by the direction of cash flow
  (e.g., inflow/outflow).</td>
  </tr>
  </tbody>
  </table>

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
  <td>If ret == RET_OK, account cash flow list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Account cash flow list format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | cashflow_id | int | Cash flow ID |
    | clearing_date | str | Clearing date. |
    | settlement_date | str | Settlement date. |
    | currency | [Currency](/moomoo-api-doc/en/trade/trade.html#1655) | Transaction currency. |
    | cashflow_type | str | Cash flow type. |
    | cashflow_direction | [CashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384) | Cash flow direction. |
    | cashflow_amount | float | Cash flow amount (positive:inflow, negative:outflow). |
    | cashflow_remark | str | Remarks. |

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_cash_flow(clearing_date='2025-02-18', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, cashflow_direction=CashFlowDirection.NONE)
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If account cash flow list is not empty
        print(data['cashflow_type'][0])  # Get direction of the first cash flow record
        print(data['cashflow_amount'].values.tolist())  # Convert to list
else:
    print('get_acc_cash_flow error: ', data)
trd_ctx.close()
```





- **Output**



``` python
   cashflow_id     clearing_date     settlement_date     currency     cashflow_type     cashflow_direction     cashflow_amount     cashflow_remark
0  16308           2025-02-27        2025-02-28          HKD             Others                 N/A                   0.00      Opt ASS-P-JXC250227P13000-20250227
1  16357           2025-02-27        2025-03-03          HKD             Others                 OUT               -104000.00
2  16360           2025-02-27        2025-02-27          USD         Fund Redemption            IN                 23000.00     Fund Redemption#Taikang Kaitai US Dollar Money...      
3  16384           2025-02-27        2025-02-27          HKD         Fund Redemption            IN                104108.96     Fund Redemption#Taikang Kaitai Hong Kong Dolla...
Others
[0.00, -104000.00, 23000.00, 104108.96]
```









## <a href="#5786" class="header-anchor">#</a> Trd_FlowSummary.proto

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Proto ID**

  2226





`uint GetFlowSummary(TrdFlowSummary.Request req);`  
`virtual void OnReply_GetFlowSummary(FTAPI_Conn client, uint nSerialNo, TrdFlowSummary.Response rsp);`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1);  //Set client information
        trd.SetConnCallback(this);  //Set connection callback
        trd.SetTrdCallback(this);   //Set transaction callback
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
        TrdFlowSummary.C2S c2s = TrdFlowSummary.C2S.CreateBuilder()
                .SetHeader(header)
                .SetClearingDate("2025-02-18")
                .Build();
        TrdFlowSummary.Request req = TrdFlowSummary.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetFlowSummary(req);
        Console.Write("Send TrdFlowSummary: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetFlowSummary(FTAPI_Conn client, uint nSerialNo, TrdFlowSummary.Response rsp)
    {
        Console.Write("Reply: TrdFlowSummary: {0}\n", nSerialNo);
        Console.Write("CashFlowAmount: {0}\n", rsp.S2C.FlowSummaryInfoListList[0].CashFlowAmount);
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
Trd onInitConnect: ret=0 desc= connID=6826806647571888999
Send TrdFlowSummary: 3
Reply: TrdFlowSummary: 3
CashFlowAmount: 23000
```









`int getFlowSummary(TrdFlowSummary.Request req);`  
`void onReply_GetFlowSummary(MMAPI_Conn client, int nSerialNo, TrdFlowSummary.Response rsp);`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1);  //Set client information
        trd.setConnSpi(this);  //Set connection callback
        trd.setTrdSpi(this);   //Set transaction callback
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
        TrdFlowSummary.C2S c2s = TrdFlowSummary.C2S.newBuilder()
                .setHeader(header)
                .setClearingDate("2025-02-18")
            .build();
        TrdFlowSummary.Request req = TrdFlowSummary.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getFlowSummary(req);
        System.out.printf("Send TrdFlowSummary: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetFlowSummary(FTAPI_Conn client, int nSerialNo, TrdFlowSummary.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdFlowSummary failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdFlowSummary: %s\n", json);
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
Send TrdFlowSummary: 2
Receive TrdFlowSummary: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "flowSummaryInfoList": {
      "clearingDate": "2025-02-27",
      "settlementDate": "2025-02-28",
      "currency": 1,
      "cashFlowType": "Others",
      "cashFlowDirection": 1,
      "cashFlowAmount": 23000.00,
      "cashFlowRemark": "Fund Redemption#Taikang Kaitai US Dollar Money",
      "cashFlowID": 16328
    }
  }
}
```









`Futu::u32_t GetFlowSummary(const Trd_FlowSummary::Request& stReq);`  
`virtual OnReply_GetFlowSummary(Futu::u32_t nSerialNo, const Trd_FlowSummary::Response& stRsp) = 0;`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
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
        Trd_FlowSummary::Request req;
        Trd_FlowSummary::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(281756457888247915);
        header->set_trdenv(1);
        header->set_trdmarket(1);
        c2s->set_clearingdate("2025-02-18");

        m_GetFlowSummarySerialNo = m_pTrdApi->GetFlowSummary(req);
        cout << "Request GetFlowSummary SerialNo: " << m_GetFlowSummarySerialNo << endl;
    }

    virtual void OnReply_GetFlowSummary(Futu::u32_t nSerialNo, const Trd_FlowSummary::Response& stRsp) {
        if(nSerialNo == m_GetFlowSummarySerialNo)
        {
            cout << "OnReply_GetFlowSummary SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetFlowSummarySerialNo;
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
Request GetAccList SerialNo: 4
OnReply_GetAccList SerialNo: 4
{
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "flowSummaryInfoList": {
      "clearingDate": "2025-02-27",
      "settlementDate": "2025-02-28",
      "currency": 1,
      "cashFlowType": "Others",
      "cashFlowDirection": 1,
      "cashFlowAmount": 23000.00,
      "cashFlowRemark": "Fund Redemption#Taikang Kaitai US Dollar Money",
      "cashFlowID": 16328
    }
  }
}
```









`GetAccList(req);`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetFlowSummary(){
    const { RetType } = Common
    const { TrdEnv, OrderType, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { // 登录成功
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType, s2c: { accList }  } = res
                if(retType == RetType.RetType_Succeed){
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // 样例取第一个香港市场虚拟环境账户

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            clearingDate: "2025-02-18", 
                        },
                    };

                    websocket.GetFlowSummary(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetFlowSummary: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetFlowSummary: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 1,
    "accID": "281756457888247915",
    "trdMarket": 1
  },
  "flowSummaryInfoList": {
    "clearingDate": "2025-02-27",
    "settlementDate": "2025-02-28",
    "currency": 1,
    "cashFlowType": "Others",
    "cashFlowDirection": 1,
    "cashFlowAmount": 23000.00,
    "cashFlowRemark": "Fund Redemption#Taikang Kaitai US Dollar Money",
      "cashFlowID": 16328
  }
}
stop
```











Interface Limitations

- A maximum of 20 requests per 30 seconds under a single account ID
  (acc_id).
- Cash flows are arranged in chronological order.
- Can not query cash flow list through paper trading accounts.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`get_acc_cash_flow(clearing_date='', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, cashflow_direction=CashFlowDirection.NONE)`

- **Description**

  Query the cash flow list of a specified trading account on a specified
  date. This includes all transactions that affect cash balances, such
  as deposits/withdrawals, fund transfers, currency exchanges,
  buying/selling financial assets, margin interest, and securities
  lending interest.

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
  <td style="text-align: left;">clearing_date</td>
  <td style="text-align: left;">str</td>
  <td style="text-align: left;">Clearing date.
  
    
  
  
   
  
  Query each day separately with YYYY-MM-DD format (e.g.,'2017-06-20').
  
  
  
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
  <td style="text-align: left;">cashflow_direction</td>
  <td style="text-align: left;"><a
  href="/moomoo-api-doc/en/trade/trade.html#1384">CashFlowDirection</a></td>
  <td style="text-align: left;">Filter by the direction of cash flow
  (e.g., inflow/outflow).</td>
  </tr>
  </tbody>
  </table>

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
  <td>If ret == RET_OK, account cash flow list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Account cash flow list format as follows:
    | Field | Type | Description |
    |:---|:---|:---|
    | cashflow_id | int | Cash flow ID |
    | clearing_date | str | Clearing date. |
    | settlement_date | str | Settlement date. |
    | currency | [Currency](/moomoo-api-doc/en/trade/trade.html#1655) | Transaction currency. |
    | cashflow_type | str | Cash flow type. |
    | cashflow_direction | [CashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384) | Cash flow direction. |
    | cashflow_amount | float | Cash flow amount (positive:inflow, negative:outflow). |
    | cashflow_remark | str | Remarks. |

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret, data = trd_ctx.get_acc_cash_flow(clearing_date='2025-02-18', trd_env=TrdEnv.REAL, acc_id=0, acc_index=0, cashflow_direction=CashFlowDirection.NONE)
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # If account cash flow list is not empty
        print(data['cashflow_type'][0])  # Get direction of the first cash flow record
        print(data['cashflow_amount'].values.tolist())  # Convert to list
else:
    print('get_acc_cash_flow error: ', data)
trd_ctx.close()
```





- **Output**



``` python
   cashflow_id     clearing_date     settlement_date     currency     cashflow_type     cashflow_direction     cashflow_amount     cashflow_remark
0  16308           2025-02-27        2025-02-28          HKD             Others                 N/A                   0.00      Opt ASS-P-JXC250227P13000-20250227
1  16357           2025-02-27        2025-03-03          HKD             Others                 OUT               -104000.00
2  16360           2025-02-27        2025-02-27          USD         Fund Redemption            IN                 23000.00     Fund Redemption#Taikang Kaitai US Dollar Money...      
3  16384           2025-02-27        2025-02-27          HKD         Fund Redemption            IN                104108.96     Fund Redemption#Taikang Kaitai Hong Kong Dolla...
Others
[0.00, -104000.00, 23000.00, 104108.96]
```









## <a href="#5786-2" class="header-anchor">#</a> Trd_FlowSummary.proto

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Proto ID**

  2226





`uint GetFlowSummary(TrdFlowSummary.Request req);`  
`virtual void OnReply_GetFlowSummary(FTAPI_Conn client, uint nSerialNo, TrdFlowSummary.Response rsp);`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn {
    FTAPI_Trd trd = new FTAPI_Trd();

    public Program() {
        trd.SetClientInfo("csharp", 1);  //Set client information
        trd.SetConnCallback(this);  //Set connection callback
        trd.SetTrdCallback(this);   //Set transaction callback
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
        TrdFlowSummary.C2S c2s = TrdFlowSummary.C2S.CreateBuilder()
                .SetHeader(header)
                .SetClearingDate("2025-02-18")
                .Build();
        TrdFlowSummary.Request req = TrdFlowSummary.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetFlowSummary(req);
        Console.Write("Send TrdFlowSummary: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_GetFlowSummary(FTAPI_Conn client, uint nSerialNo, TrdFlowSummary.Response rsp)
    {
        Console.Write("Reply: TrdFlowSummary: {0}\n", nSerialNo);
        Console.Write("CashFlowAmount: {0}\n", rsp.S2C.FlowSummaryInfoListList[0].CashFlowAmount);
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
Trd onInitConnect: ret=0 desc= connID=6826806647571888999
Send TrdFlowSummary: 3
Reply: TrdFlowSummary: 3
CashFlowAmount: 23000
```









`int getFlowSummary(TrdFlowSummary.Request req);`  
`void onReply_GetFlowSummary(MMAPI_Conn client, int nSerialNo, TrdFlowSummary.Response rsp);`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements FTSPI_Trd, FTSPI_Conn {
    FTAPI_Conn_Trd trd = new FTAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1);  //Set client information
        trd.setConnSpi(this);  //Set connection callback
        trd.setTrdSpi(this);   //Set transaction callback
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
        TrdFlowSummary.C2S c2s = TrdFlowSummary.C2S.newBuilder()
                .setHeader(header)
                .setClearingDate("2025-02-18")
            .build();
        TrdFlowSummary.Request req = TrdFlowSummary.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.getFlowSummary(req);
        System.out.printf("Send TrdFlowSummary: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetFlowSummary(FTAPI_Conn client, int nSerialNo, TrdFlowSummary.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdFlowSummary failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdFlowSummary: %s\n", json);
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
Send TrdFlowSummary: 2
Receive TrdFlowSummary: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "flowSummaryInfoList": {
      "clearingDate": "2025-02-27",
      "settlementDate": "2025-02-28",
      "currency": 1,
      "cashFlowType": "Others",
      "cashFlowDirection": 1,
      "cashFlowAmount": 23000.00,
      "cashFlowRemark": "Fund Redemption#Taikang Kaitai US Dollar Money",
      "cashFlowID": 16328
    }
  }
}
```









`Futu::u32_t GetFlowSummary(const Trd_FlowSummary::Request& stReq);`  
`virtual OnReply_GetFlowSummary(Futu::u32_t nSerialNo, const Trd_FlowSummary::Response& stRsp) = 0;`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
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
        Trd_FlowSummary::Request req;
        Trd_FlowSummary::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(281756457888247915);
        header->set_trdenv(1);
        header->set_trdmarket(1);
        c2s->set_clearingdate("2025-02-18");

        m_GetFlowSummarySerialNo = m_pTrdApi->GetFlowSummary(req);
        cout << "Request GetFlowSummary SerialNo: " << m_GetFlowSummarySerialNo << endl;
    }

    virtual void OnReply_GetFlowSummary(Futu::u32_t nSerialNo, const Trd_FlowSummary::Response& stRsp) {
        if(nSerialNo == m_GetFlowSummarySerialNo)
        {
            cout << "OnReply_GetFlowSummary SerialNo: " << nSerialNo << endl;
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetFlowSummarySerialNo;
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
Request GetAccList SerialNo: 4
OnReply_GetAccList SerialNo: 4
{
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756457888247915",
      "trdMarket": 1
    },
    "flowSummaryInfoList": {
      "clearingDate": "2025-02-27",
      "settlementDate": "2025-02-28",
      "currency": 1,
      "cashFlowType": "Others",
      "cashFlowDirection": 1,
      "cashFlowAmount": 23000.00,
      "cashFlowRemark": "Fund Redemption#Taikang Kaitai US Dollar Money",
      "cashFlowID": 16328
    }
  }
}
```









`GetAccList(req);`

- **Description**

  Get Account Cash FlQuery the cash flow list of a specified trading
  account on a specified date. This includes all transactions that
  affect cash balances, such as deposits/withdrawals, fund transfers,
  currency exchanges, buying/selling financial assets, margin interest,
  and securities lending interest.ow Data

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required string clearingDate = 2; //clearing date，format in "2017-05-20"
    optional int32 cashFlowDirection = 3; //cash flow direction, refer to TrdCashFlowDirection
}

message Request
{
    required C2S c2s = 1;
}
```





> - For cash flow direction, refer to
>   [TrdCashFlowDirection](/moomoo-api-doc/en/trade/trade.html#1384)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated FlowSummaryInfo flowSummaryInfoList = 2; //Cash flow data
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





> - For cash flow data, refer to
>   [FlowSummaryInfo](/moomoo-api-doc/en/trade/trade.html#9686)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetFlowSummary(){
    const { RetType } = Common
    const { TrdEnv, OrderType, TrdMarket } = Trd_Common
    let [addr, port, enable_ssl, key] = ["127.0.0.1", 33333, false, '7522027ccf5a06b1'];
    let websocket = new ftWebsocket();

    websocket.onlogin = (ret, msg)=>{
        if (ret) { // 登录成功
            websocket.GetAccList({
                c2s: {
                    userID: 0,
                },
            }).then((res) => {
                let { retType, s2c: { accList }  } = res
                if(retType == RetType.RetType_Succeed){
                    let acc = accList.filter((item)=>{ 
                        return item.trdEnv == TrdEnv.TrdEnv_Simulate && item.trdMarketAuthList.some((auth)=>{ return auth == TrdMarket.TrdMarket_HK})
                    })[0]; // 样例取第一个香港市场虚拟环境账户

                    const req = {
                        c2s: {
                            header: {
                                trdEnv: acc.trdEnv,
                                accID: acc.accID,
                                trdMarket: TrdMarket.TrdMarket_HK,
                            },
                            clearingDate: "2025-02-18", 
                        },
                    };

                    websocket.GetFlowSummary(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetFlowSummary: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetFlowSummary: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 1,
    "accID": "281756457888247915",
    "trdMarket": 1
  },
  "flowSummaryInfoList": {
    "clearingDate": "2025-02-27",
    "settlementDate": "2025-02-28",
    "currency": 1,
    "cashFlowType": "Others",
    "cashFlowDirection": 1,
    "cashFlowAmount": 23000.00,
    "cashFlowRemark": "Fund Redemption#Taikang Kaitai US Dollar Money",
      "cashFlowID": 16328
  }
}
stop
```











Interface Limitations

- A maximum of 20 requests per 30 seconds under a single account ID
  (acc_id).
- Cash flows are arranged in chronological order.
- Can not query cash flow list through paper trading accounts and moomoo
  US accounts.













