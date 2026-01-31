



# <a href="#5119" class="header-anchor">#</a> Get Order Fee









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`order_fee_query(order_id_list=[], acc_id=0, acc_index=0, trd_env=TrdEnv.REAL)`

- **介绍**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **参数**

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
  <td style="text-align: left;">order_id_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Order id list.
  
    
  
  
   
  
  <ul>
  <li>At most 400 orders for each request.</li>
  <li>The data type of elements in the list is str.</li>
  </ul>
  
  
  
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

- **返回**

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
  <td>If ret == RET_OK, order fee list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Order list format as follows：
    <table>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">字段</th>
    <th style="text-align: left;">类型</th>
    <th style="text-align: left;">说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Order ID</td>
    </tr>
    <tr>
    <td style="text-align: left;">fee_amount</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total fee of the order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">fee_details</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Fee details of the order.
    
      
    
    
     
    
    Format：[('item1', fee amount of item1), ('item2', fee amount of item2),
    ('item3', fee amount of item3)]
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret1, data1 = trd_ctx.history_order_list_query(status_filter_list=[OrderStatus.FILLED_ALL])
if ret1 == RET_OK:
    if data1.shape[0] > 0:  # If the order list is not empty
        ret2, data2 = trd_ctx.order_fee_query(data1['order_id'].values.tolist())  # Convert order ids to list data type, and request for order fees.
        if ret2 == RET_OK:
            print(data2)
            print(data2['fee_details'][0])  # Get fee details of the first order
        else:
            print('order_fee_query error: ', data2)
else:
    print('order_list_query error: ', data1)
trd_ctx.close()
```





- **Output**



``` python
                                            order_id  fee_amount                                        fee_details
0  v3_20240314_12345678_MTc4NzA5NzY5OTA3ODAzMzMwN       10.46  [(Commission, 5.85), (Platform Fee, 2.7), (ORF...
1  v3_20240318_12345678_MTM5Nzc5MDYxNDY1NDM1MDI1M        2.25  [(Commission, 0.99), (Platform Fee, 1.0), (Set...
[('Commission', 5.85), ('Platform Fee', 2.7), ('ORF', 0.11), ('OCC Fee', 0.18), ('Option Settlement Fees', 1.62)]
```









## <a href="#7662" class="header-anchor">#</a> Trd_GetOrderFee.proto

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2225





`uint GetOrderFee(TrdGetOrderFee.Request req);`  
`virtual void OnReply_GetOrderFee(FTAPI_Conn client, uint nSerialNo, TrdGetOrderFee.Response rsp);`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn
{
    FTAPI_Trd trd = new FTAPI_Trd();
    private TrdCommon.TrdEnv trdEnv = TrdCommon.TrdEnv.TrdEnv_Real;
    private TrdCommon.TrdMarket trdMkt = TrdCommon.TrdMarket.TrdMarket_US;
    public Program()
    {
        trd.SetClientInfo("csharp", 1);
        trd.SetConnCallback(this);
        trd.SetTrdCallback(this);
    }
    public void Start()
    {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }
    public void OnInitConnect(FTAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;
        TrdGetAccList.C2S c2s = TrdGetAccList.C2S.CreateBuilder().SetUserID(0)
                .Build();
        TrdGetAccList.Request req = TrdGetAccList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetAccList(req);
        Console.Write("Send TrdGetAccList: {0}\n", seqNo);
    }
    public void OnDisconnect(FTAPI_Conn client, long errCode)
    {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }
    public void OnReply_GetAccList(FTAPI_Conn client, uint nSerialNo, TrdGetAccList.Response rsp)
    {
        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
        {
            Console.WriteLine("ERROR: GetAccList, retMsg = {0}", rsp.RetMsg);
            return;
        }
        Console.Write("Recv GetAccList succeed. accCount: {0}\n", rsp.S2C.AccListCount);
        ulong accID = 0;
        foreach (TrdCommon.TrdAcc acc in rsp.S2C.AccListList)
        {
            if (acc.TrdEnv == (int)trdEnv && acc.TrdMarketAuthListList[0] == (int)trdMkt)
            {
                accID = acc.AccID;
                Console.Write("accInfo: accId: {0}, trdEnv: {1}, trdMarketAuthList: {2}, simAccType: {3}\n",
                    acc.AccID, (TrdCommon.TrdEnv)acc.TrdEnv, (TrdCommon.TrdMarket)acc.TrdMarketAuthListList[0],
                    (TrdCommon.TrdAccType)acc.SimAccType);
                break;
            }
        }
        if (accID == 0)
        {
            return;
        }
        string svrOrderId = "20240403_900053_Fy0gPKjKE1ZW1hUuf0z0DABgxvzfmQYq";
        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.CreateBuilder().SetTrdEnv((int)trdEnv)
            .SetTrdMarket((int)trdMkt)
            .SetAccID(accID)
            .Build();
        TrdGetOrderFee.C2S c2s = TrdGetOrderFee.C2S.CreateBuilder().SetHeader(header)
            .AddOrderIdExList(svrOrderId).Build();
        TrdGetOrderFee.Request req = TrdGetOrderFee.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetOrderFee(req);
        Console.Write("Send GetOrderFee: {0}\n", seqNo);
    }
    public void OnReply_GetOrderFee(FTAPI_Conn client, uint nSerialNo, TrdGetOrderFee.Response rsp)
    {
        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
        {
            Console.WriteLine("ERROR: GetOrderFee, retMsg = {0}", rsp.RetMsg);
            return;
        }
        foreach (TrdCommon.OrderFee ordFee in rsp.S2C.OrderFeeListList)
        {
            if (ordFee.HasFeeAmount)
            {
                Console.WriteLine("orderId: {0}, amount: {1}", ordFee.OrderIDEx, ordFee.FeeAmount);
            }
            else
            {
                Console.WriteLine("orderId: {0}", ordFee.OrderIDEx);
            }
            foreach (TrdCommon.OrderFeeItem feeItem in ordFee.FeeListList)
            {
                Console.WriteLine("title: {0}, fee: {1}", feeItem.Title, feeItem.Value);
            }
        }
    }
    public static void Main(String[] args)
    {
        FTAPI.Init();
        Program Trd = new Program();
        Trd.Start();
        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
orderId: 20240403_900053_Fy0gPKjKE1ZW1hUuf0z0DABgxvzfmQYq, amount: 2.01
title: ..., fee: 0.99
title: ..., fee: 1
title: ..., fee: 0
title: ..., fee: 0.01
title: ..., fee: 0.01
```









`int getOrderFee(TrdGetOrderFee.Request req);`  
`void onReply_GetOrderFee(FTAPI_Conn client, int nSerialNo, TrdGetOrderFee.Response rsp);`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
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
                .setAccID(281756457888247915L)  //Use your own trade account
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        String orderId = "20210625_123456_OD|IqKozO18ODL1pwZNcLzgvEe9sW8gm"; //Use your own order id 
        TrdGetOrderFee.C2S c2s = TrdGetOrderFee.C2S.newBuilder()
                .setHeader(header)
                .addOrderIdExList(orderId)
                .build();
        TrdGetOrderFee.Request req =TrdGetOrderFee.Request.newBuilder().setC2S(c2s).build();
        int sn = trd.getOrderFee(req);
        System.out.printf("getOrderFee: sn=%d\n", sn);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOrderFee(FTAPI_Conn client, int nSerialNo, TrdGetOrderList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetOrderFee failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("onReply_GetOrderFee: %s\n", json);
            } catch (InvalidProtocolBufferException err) {
                err.printStackTrace();
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
getOrderFee: sn=2
onReply_GetOrderFee: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756455988306264",
      "trdMarket": 1
    },
    "orderFeeList": [{
      "orderIDEx": "20210625_5972312_OD|IqKozO18ODL1pwZNcLzgvEe9sW8gm",
      "feeAmount": 7.569999999999999,
      "feeList": [{
        "title": "Commission",
        "value": 1.0
      }, {
        "title": "Platform Fee",
        "value": 0.0
      }, {
        "title": "Trading Tariff",
        "value": 0.0
      }, {
        "title": "Settlement Fee",
        "value": 5.5
      }, {
        "title": "Stamp Duty",
        "value": 1.0
      }, {
        "title": "Trading Fee",
        "value": 0.05
      }, {
        "title": "Transaction Levy",
        "value": 0.02
      }]
    }]
  }
}
```









`Futu::u32_t GetOrderFee(const Trd_GetOrderFee::Request &stReq);`  
`virtual void OnReply_GetOrderFee(Futu::u32_t nSerialNo, const Trd_GetOrderFee::Response &stRsp) = 0;`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
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

        Trd_GetOrderFee::Request req;
        Trd_GetOrderFee::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(281756455983234005);
        header->set_trdenv(1);
        header->set_trdmarket(1);
        c2s->add_orderidexlist("20240410_900053_OD|kSoBjXk8SRhW4aJfWHwAmrhzYFyJS");

        m_GetOrderFeeSerialNo = m_pTrdApi->GetOrderFee(req);
        cout << "Request GetOrderFee SerialNo: " << m_GetOrderFeeSerialNo << endl;
    }

    virtual void OnReply_GetOrderFee(Futu::u32_t nSerialNo, const Trd_GetOrderFee::Response &stRsp){
        if(nSerialNo == m_GetOrderFeeSerialNo)
        {
            cout << "OnReply_GetOrderFee SerialNo: " << nSerialNo << endl;
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_GetOrderFeeSerialNo;
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
Request_GetOrderFee SerialNo: 4
OnReply_GetOrderFee SerialNo: 4
{
    "retType": 0,
    "retMsg": "",
    "errCode": 0,
    "s2c": {
        "header": {
            "trdEnv": 1,
            "accID": "281756455983234005",
            "trdMarket": 1
        },
        "orderFeeList": [
            {
                "orderIDEx": "20240410_900053_OD|kSoBjXk8SRhW4aJfWHwAmrhzYFyJS",
                "feeAmount": 24.27,
                "feeList": [
                    {
                        "title": "...",
                        "value": 3
                    },
                    {
                        "title": "...",
                        "value": 15
                    },
                    {
                        "title": "...",
                        "value": 0
                    },
                    {
                        "title": "...",
                        "value": 2
                    },
                    {
                        "title": "...",
                        "value": 4
                    },
                    {
                        "title": "...",
                        "value": 0.18
                    },
                    {
                        "title": "...",
                        "value": 0.09
                    },
                    {
                        "title": "...",
                        "value": 0
                    }
                ]
            }
        ]
    }
}
```









`GetOrderFee(req);`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdGetOrderList(){
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

                    websocket.GetOrderFee(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetOrderFee: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetOrderFee: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFeeList": [{
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "feeAmount": 522700.6,
    "feeList": [
        {
            "title":"...",
            "value":"...",
        }, ...,{
            "title":"...",
            "value":"...",
        },
    ]
  }, ..., {
    "orderIDEx": "20210913_5915950_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld",
    "feeAmount": 67356.8,
    "feeList": [
        {
            "title":"...",
            "value":"...",
        }, ...,{
            "title":"...",
            "value":"...",
        },
    ]
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- Only orders after 2018-01-01 are supported.
- Can not query order fee through paper trading accounts.











- Python
- Proto
- C#
- Java
- C++
- JavaScript





`order_fee_query(order_id_list=[], acc_id=0, acc_index=0, trd_env=TrdEnv.REAL)`

- **介绍**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **参数**

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
  <td style="text-align: left;">order_id_list</td>
  <td style="text-align: left;">list</td>
  <td style="text-align: left;">Order id list.
  
    
  
  
   
  
  <ul>
  <li>At most 400 orders for each request.</li>
  <li>The data type of elements in the list is str.</li>
  </ul>
  
  
  
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

- **返回**

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
  <td>If ret == RET_OK, order fee list is returned.</td>
  </tr>
  <tr>
  <td>str</td>
  <td>If ret != RET_OK, error description is returned.</td>
  </tr>
  </tbody>
  </table>

  - Order list format as follows：
    <table>
    <colgroup>
    <col style="width: 33%" />
    <col style="width: 33%" />
    <col style="width: 33%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">字段</th>
    <th style="text-align: left;">类型</th>
    <th style="text-align: left;">说明</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;">order_id</td>
    <td style="text-align: left;">str</td>
    <td style="text-align: left;">Order ID</td>
    </tr>
    <tr>
    <td style="text-align: left;">fee_amount</td>
    <td style="text-align: left;">float</td>
    <td style="text-align: left;">Total fee of the order.</td>
    </tr>
    <tr>
    <td style="text-align: left;">fee_details</td>
    <td style="text-align: left;">list</td>
    <td style="text-align: left;">Fee details of the order.
    
      
    
    
     
    
    <ul>
    <li>Format：[('item1', fee amount of item1), ('item2', fee amount of
    item2), ('item3', fee amount of item3)]</li>
    <li>Common fee items: Commission, Platform Fee, ORF, OCC Fee,Option
    Settlement Fees, Settlement Fee, SEC Fee, TAF.</li>
    </ul>
    
    
    
    </td>
    </tr>
    </tbody>
    </table>

    

    
    

    

    
    
    

    Format：\[('item1', fee amount of item1), ('item2', fee amount of
    item2), ('item3', fee amount of item3)\]

    

    

    

    

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
ret1, data1 = trd_ctx.history_order_list_query(status_filter_list=[OrderStatus.FILLED_ALL])
if ret1 == RET_OK:
    if data1.shape[0] > 0:  # If the order list is not empty
        ret2, data2 = trd_ctx.order_fee_query(data1['order_id'].values.tolist())  # Convert order ids to list data type, and request for order fees.
        if ret2 == RET_OK:
            print(data2)
            print(data2['fee_details'][0])  # Get fee details of the first order
        else:
            print('order_fee_query error: ', data2)
else:
    print('order_list_query error: ', data1)
trd_ctx.close()
```





- **Output**



``` python
                                            order_id  fee_amount                                        fee_details
0  v3_20240314_12345678_MTc4NzA5NzY5OTA3ODAzMzMwN       10.46  [(Commission, 5.85), (Platform Fee, 2.7), (ORF...
1  v3_20240318_12345678_MTM5Nzc5MDYxNDY1NDM1MDI1M        2.25  [(Commission, 0.99), (Platform Fee, 1.0), (Set...
[('Commission', 5.85), ('Platform Fee', 2.7), ('ORF', 0.11), ('OCC Fee', 0.18), ('Option Settlement Fees', 1.62)]
```









## <a href="#7662-2" class="header-anchor">#</a> Trd_GetOrderFee.proto

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Protocol ID**

  2225





`uint GetOrderFee(TrdGetOrderFee.Request req);`  
`virtual void OnReply_GetOrderFee(MMAPI_Conn client, uint nSerialNo, TrdGetOrderFee.Response rsp);`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Trd, MMSPI_Conn
{
    MMAPI_Trd trd = new MMAPI_Trd();
    private TrdCommon.TrdEnv trdEnv = TrdCommon.TrdEnv.TrdEnv_Real;
    private TrdCommon.TrdMarket trdMkt = TrdCommon.TrdMarket.TrdMarket_HK;
    public Program()
    {
        trd.SetClientInfo("csharp", 1);
        trd.SetConnCallback(this);
        trd.SetTrdCallback(this);
    }
    public void Start()
    {
        trd.InitConnect("127.0.0.1", (ushort)11111, false);
    }
    public void OnInitConnect(MMAPI_Conn client, long errCode, String desc)
    {
        Console.Write("Trd onInitConnect: ret={0} desc={1} connID={2}\n", errCode, desc, client.GetConnectID());
        if (errCode != 0)
            return;
        TrdGetAccList.C2S c2s = TrdGetAccList.C2S.CreateBuilder().SetUserID(0)
                .Build();
        TrdGetAccList.Request req = TrdGetAccList.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetAccList(req);
        Console.Write("Send TrdGetAccList: {0}\n", seqNo);
    }
    public void OnDisconnect(MMAPI_Conn client, long errCode)
    {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }
    public void OnReply_GetAccList(MMAPI_Conn client, uint nSerialNo, TrdGetAccList.Response rsp)
    {
        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
        {
            Console.WriteLine("ERROR: GetAccList, retMsg = {0}", rsp.RetMsg);
            return;
        }
        Console.Write("Recv GetAccList succeed. accCount: {0}\n", rsp.S2C.AccListCount);
        ulong accID = 0;
        foreach (TrdCommon.TrdAcc acc in rsp.S2C.AccListList)
        {
            if (acc.TrdEnv == (int)trdEnv && acc.TrdMarketAuthListList[0] == (int)trdMkt)
            {
                accID = acc.AccID;
                Console.Write("accInfo: accId: {0}, trdEnv: {1}, trdMarketAuthList: {2}, simAccType: {3}\n",
                    acc.AccID, (TrdCommon.TrdEnv)acc.TrdEnv, (TrdCommon.TrdMarket)acc.TrdMarketAuthListList[0],
                    (TrdCommon.TrdAccType)acc.SimAccType);
                break;
            }
        }
        if (accID == 0)
        {
            return;
        }
        string svrOrderId = "20240409_900062_ODc3ODI3NDQwNTA3NjU1NTkzNTRmNDJk";
        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.CreateBuilder().SetTrdEnv((int)trdEnv)
            .SetTrdMarket((int)trdMkt)
            .SetAccID(accID)
            .Build();
        TrdGetOrderFee.C2S c2s = TrdGetOrderFee.C2S.CreateBuilder().SetHeader(header)
            .AddOrderIdExList(svrOrderId).Build();
        TrdGetOrderFee.Request req = TrdGetOrderFee.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.GetOrderFee(req);
        Console.Write("Send GetOrderFee: {0}\n", seqNo);
    }
    public void OnReply_GetOrderFee(MMAPI_Conn client, uint nSerialNo, TrdGetOrderFee.Response rsp)
    {
        if (rsp.RetType != (int)Common.RetType.RetType_Succeed)
        {
            Console.WriteLine("ERROR: GetOrderFee, retMsg = {0}", rsp.RetMsg);
            return;
        }
        foreach (TrdCommon.OrderFee ordFee in rsp.S2C.OrderFeeListList)
        {
            if (ordFee.HasFeeAmount)
            {
                Console.WriteLine("orderId: {0}, amount: {1}", ordFee.OrderIDEx, ordFee.FeeAmount);
            }
            else
            {
                Console.WriteLine("orderId: {0}", ordFee.OrderIDEx);
            }
            foreach (TrdCommon.OrderFeeItem feeItem in ordFee.FeeListList)
            {
                Console.WriteLine("title: {0}, fee: {1}", feeItem.Title, feeItem.Value);
            }
        }
    }
    public static void Main(String[] args)
    {
        MMAPI.Init();
        Program Trd = new Program();
        Trd.Start();
        while (true)
            Thread.Sleep(1000 * 600);
    }
}
```





- **Output**



``` cs
orderId: 20240409_900062_ODc3ODI3NDQwNTA3NjU1NTkzNTRmNDJk, amount: 28.6
title: ..., fee: 3
title: ..., fee: 15
title: ..., fee: 0
title: ..., fee: 2
title: ..., fee: 8
title: ..., fee: 0.4
title: ..., fee: 0.19
title: ..., fee: 0.01
```









`int getOrderFee(TrdGetOrderFee.Request req);`  
`void onReply_GetOrderFee(MMAPI_Conn client, int nSerialNo, TrdGetOrderFee.Response rsp);`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` java
public class TrdDemo implements MMSPI_Trd, MMSPI_Conn {
    MMAPI_Conn_Trd trd = new MMAPI_Conn_Trd();

    public TrdDemo() {
        trd.setClientInfo("javaclient", 1);  //Set client information
        trd.setConnSpi(this);  //Set connection callback
        trd.setTrdSpi(this);   //Set transaction callback
    }

    public void start() {
        trd.initConnect("127.0.0.1", (short)11111, false);
    }

    @Override
    public void onInitConnect(MMSPI_Conn client, long errCode, String desc)
    {
        System.out.printf("Trd onInitConnect: ret=%b desc=%s connID=%d\n", errCode, desc, client.getConnectID());
        if (errCode != 0)
            return;

        TrdCommon.TrdHeader header = TrdCommon.TrdHeader.newBuilder()
                .setAccID(281756457888247915L)  //Use your own trade account
                .setTrdEnv(TrdCommon.TrdEnv.TrdEnv_Real_VALUE)
                .setTrdMarket(TrdCommon.TrdMarket.TrdMarket_HK_VALUE)
                .build();
        String orderId = "20210625_123456_OD|IqKozO18ODL1pwZNcLzgvEe9sW8gm"; //Use your own order id 
        TrdGetOrderFee.C2S c2s = TrdGetOrderFee.C2S.newBuilder()
                .setHeader(header)
                .addOrderIdExList(orderId)
                .build();
        TrdGetOrderFee.Request req =TrdGetOrderFee.Request.newBuilder().setC2S(c2s).build();
        int sn = trd.getOrderFee(req);
        System.out.printf("getOrderFee: sn=%d\n", sn);
    }

    @Override
    public void onDisconnect(MMSPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onReply_GetOrderFee(MMSPI_Conn client, int nSerialNo, TrdGetOrderList.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdGetOrderFee failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("onReply_GetOrderFee: %s\n", json);
            } catch (InvalidProtocolBufferException err) {
                err.printStackTrace();
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
getOrderFee: sn=2
onReply_GetOrderFee: {
  "retType": 0,
  "retMsg": "",
  "errCode": 0,
  "s2c": {
    "header": {
      "trdEnv": 1,
      "accID": "281756455988306264",
      "trdMarket": 1
    },
    "orderFeeList": [{
      "orderIDEx": "20210625_5972312_OD|IqKozO18ODL1pwZNcLzgvEe9sW8gm",
      "feeAmount": 7.569999999999999,
      "feeList": [{
        "title": "Commission",
        "value": 1.0
      }, {
        "title": "Platform Fee",
        "value": 0.0
      }, {
        "title": "Trading Tariff",
        "value": 0.0
      }, {
        "title": "Settlement Fee",
        "value": 5.5
      }, {
        "title": "Stamp Duty",
        "value": 1.0
      }, {
        "title": "Trading Fee",
        "value": 0.05
      }, {
        "title": "Transaction Levy",
        "value": 0.02
      }]
    }]
  }
}
```









`moomoo::u32_t GetOrderFee(const Trd_GetOrderFee::Request &stReq);`  
`virtual void OnReply_GetOrderFee(moomoo::u32_t nSerialNo, const Trd_GetOrderFee::Response &stRsp) = 0;`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
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
        Trd_GetOrderFee::Request req;
        Trd_GetOrderFee::C2S *c2s = req.mutable_c2s();
        Trd_Common::TrdHeader *header = c2s->mutable_header();
        header->set_accid(281756455983234005);
        header->set_trdenv(1);
        header->set_trdmarket(1);
        c2s->add_orderidexlist("20240410_900053_OD|kSoBjXk8SRhW4aJfWHwAmrhzYFyJS");

        m_GetOrderFeeSerialNo = m_pTrdApi->GetOrderFee(req);
        cout << "Request GetOrderFee SerialNo: " << m_GetOrderFeeSerialNo << endl;
    }

    virtual void OnReply_GetOrderFee(moomoo::u32_t nSerialNo, const Trd_GetOrderList::Response &stRsp){
        if(nSerialNo == m_GetOrderListSerialNo)
        {
            cout << "OnReply_GetOrderFee SerialNo: " << nSerialNo << endl; 
            // print response
            // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
            string resp_str;
            ProtoBufToBodyData(stRsp, resp_str);
            cout << UTF8ToLocal(resp_str) << endl;
        }
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_GetOrderListSerialNo;
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
Request_GetOrderFee SerialNo: 4
OnReply_GetOrderFee SerialNo: 4
{
    "retType": 0,
    "retMsg": "",
    "errCode": 0,
    "s2c": {
        "header": {
            "trdEnv": 1,
            "accID": "281756455983234005",
            "trdMarket": 1
        },
        "orderFeeList": [{
            "orderIDEx": "20240410_900053_OD|kSoBjXk8SRhW4aJfWHwAmrhzYFyJS",
            "feeAmount": 24.27,
            "feeList": [{
                "title": "Commission",
                "value": 3
            },
            {
                "title": "Platform Fee",
                "value": 15
            },
            {
                "title": "Trading Tariff",
                "value": 0
            },
            {
                "title": "Settlement Fee",
                "value": 2
            },
            {
                "title": "Stamp Duty",
                "value": 4
            },
            {
                "title": "Trading Fee",
                "value": 0.18
            },
            {
                "title": "SFC Levy",
                "value": 0.09
            },
            {
                "title": "FRC Levy",
                "value": 0
            }]
        }]
    }
}
```









`GetOrderFee(req);`

- **Description**

  Get specified orders' fee details. (Minimum version requirement:
  8.2.4218)

- **Parameters**



``` protobuf
message C2S
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated string orderIdExList = 2; // Server order id
}

message Request
{
    required C2S c2s = 1;
}
```





> - For protocol header, refer to
>   [TrdHeader](/moomoo-api-doc/en/trade/trade.html#8729)

- **Return**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    repeated Trd_Common.OrderFee orderFeeList = 2; //Order fee list
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
> - For order fee structure, refer to
>   [OrderFee](/moomoo-api-doc/en/trade/trade.html#7615)
> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdGetOrderList(){
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

                    websocket.GetOrderFee(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("GetOrderFee: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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
GetOrderFee: errCode 0, retMsg , retType 0
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFeeList": [{
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "feeAmount": 522700.6,
    "feeList": [
        {
            "title":"...",
            "value":"...",
        }, ...,{
            "title":"...",
            "value":"...",
        },
    ]
  }, ..., {
    "orderIDEx": "20210913_5915950_OD|rILqM3WaKl2rXYpRYuigcJmBKtRld",
    "feeAmount": 67356.8,
    "feeList": [
        {
            "title":"...",
            "value":"...",
        }, ...,{
            "title":"...",
            "value":"...",
        },
    ]
  }]
}
stop
```











Interface Limitations

- A maximum of 10 requests per 30 seconds under a single account ID
  (acc_id).
- Only orders after 2018-01-01 are supported.
- Can not query order fee through paper trading accounts.













