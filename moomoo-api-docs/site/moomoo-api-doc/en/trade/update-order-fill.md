



# <a href="#4428" class="header-anchor">#</a> Deals Push Callback









- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD. After receiving the
  order fill information pushed by OpenD, this function is called. You
  need to override on_recv_rsp in the derived class.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Trd_UpdateOrderFill_pb2.Response | This parameter does not need to be processed in the derived class. |

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
    <td style="text-align: left;">Fill price.</td>
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
from time import sleep
class TradeDealTest(TradeDealHandlerBase):
    """ order update push"""
    def on_recv_rsp(self, rsp_pb):
        ret, content = super(TradeDealTest, self).on_recv_rsp(rsp_pb)
        if ret == RET_OK:
            print("TradeDealTest content={}".format(content))
        return ret, content

trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
trd_ctx.set_handler(TradeDealTest())
print(trd_ctx.place_order(price=595.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY))

sleep(15)
trd_ctx.close()
```





- **Output**



``` python
TradeDealTest content=  trd_env      code stock_name              deal_id             order_id    qty  price trd_side              create_time  counter_broker_id counter_broker_name trd_market status
0    REAL  HK.00700       Tencent  2511067564122483295  8561504228375901919  100.0  518.0      BUY  2021-11-04 11:29:41.595                  5                   5         HK     OK
```









## <a href="#5508" class="header-anchor">#</a> Trd_UpdateOrderFill.proto

- **Description**

  Respond to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

  2218





`virtual void OnReply_UpdateOrderFill(FTAPI_Conn client, uint nSerialNo, TrdUpdateOrderFill.Response rsp);`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

        //Subscribe first to get push
        TrdSubAccPush.C2S c2s = TrdSubAccPush.C2S.CreateBuilder()
                .AddAccIDList(281753457989306260L)
                .Build();
        TrdSubAccPush.Request req = TrdSubAccPush.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.SubAccPush(req);
        Console.Write("Send TrdSubAccPush: {0}\n", seqNo);
    }

    
    public void OnDisconnect(FTAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_SubAccPush(FTAPI_Conn client, uint nSerialNo, TrdSubAccPush.Response rsp)
    {
        Console.Write("OnReply_SubAccPush: {0}\n", nSerialNo, rsp.ToString());
    }

    public void OnReply_UpdateOrderFill(FTAPI_Conn client, uint nSerialNo, TrdUpdateOrderFill.Response rsp)
    {
        Console.Write("Push: TrdUpdateOrderFill: {0}\n", nSerialNo);
        Console.Write("retMsg: {0}\n", rsp.RetMsg);
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
Trd onInitConnect: ret=0 desc= connID=6827940248993029021
Send TrdSubAccPush: 3
OnReply_SubAccPush: 3
Push: TrdUpdateOrderFill: 1
retMsg:
```









`void onPush_UpdateOrderFill(FTAPI_Conn client, int nSerialNo, TrdUpdateOrderFill.Response rsp);`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

        //Subscribe first to get push
        TrdSubAccPush.C2S c2s = TrdSubAccPush.C2S.newBuilder()
                .addAccIDList(281753457989306260L)
                .build();
        TrdSubAccPush.Request req = TrdSubAccPush.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.subAccPush(req);
        System.out.printf("Send TrdSubAccPush: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(FTAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onPush_UpdateOrderFill(FTAPI_Conn client, TrdUpdateOrderFill.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdUpdateOrderFill failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdUpdateOrderFill: %s\n", json);
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
Send TrdUpdateOrderFill: 2
Receive TrdUpdateOrderFill: {
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
      "name": "Futu Holdings Limited",
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









`virtual void OnPush_UpdateOrderFill(const Trd_UpdateOrderFill::Response &stRsp) = 0;`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

        Trd_SubAccPush::Request req;
        Trd_SubAccPush::C2S *c2s = req.mutable_c2s();
        c2s->add_accidlist(3637840);
        
        m_SubAccPushSerialNo = m_pTrdApi->SubAccPush(req);
        cout << "Request SubAccPush SerialNo: " << m_SubAccPushSerialNo << endl;
    }

    virtual void OnReply_SubAccPush(Futu::u32_t nSerialNo, const Trd_SubAccPush::Response &stRsp) {
        if(nSerialNo == m_SubAccPushSerialNo)
        {
            cout << "OnReply_SubAccPush SerialNo: " << nSerialNo << endl;
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "SubAccPush Failed" << endl;
                return;
            }
        }
    }

    virtual void OnPush_UpdateOrderFill(const Trd_UpdateOrderFill::Response &stRsp)
    {
        cout << "OnPush_UpdateOrderFill:" << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    FTAPI_Trd *m_pTrdApi;

    Futu::u32_t m_SubAccPushSerialNo;
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
Request SubAccPush SerialNo: 4
OnReply_SubAccPush SerialNo: 4
OnPush_UpdateOrderFill:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFill": {
    "trdSide": 1,
    "fillID": "932511865781776209",
    "fillIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1.2",
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.606",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522700.605828,
    "updateTimestamp": 1631522700.605828,
    "status": 0
  }
}
```









`OnPush(cmd,res)`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

function TrdUpdateOrderFill(){
    const { RetType } = Common
    const { TrdEnv, OrderType } = Trd_Common
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
                    let accIDList = accList.map((acc)=>{ return acc.accID }); // Subscribe to the transaction push of all accounts
                    
                    const req = {
                        c2s: {
                            accIDList: accIDList,
                        },
                    };

                    websocket.SubAccPush(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("SubAccPush: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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

    websocket.onPush = (cmd, res)=>{
        if(ftCmdID.TrdUpdateOrderFill.cmd == cmd){  
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                let data = beautify(JSON.stringify(s2c), {
                    indent_size: 2,
                    space_in_empty_paren: true,
                });
                console.log("TrdUpdateOrderFill:");
                console.log(data);
            } else {
                console.log("TrdUpdateOrderFillTest: error")
            }
        }
    };

    websocket.start(addr, port, enable_ssl, key);
    
    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 3600*1000); // Set the script to receive OpenD push duration to 3600 seconds
}
```





- **Output**



``` javascript
SubAccPush: errCode 0, retMsg , retType 0
null
TrdUpdateOrderFill:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFill": {
    "trdSide": 1,
    "fillID": "932511865781776209",
    "fillIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1.2",
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.606",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522700.605828,
    "updateTimestamp": 1631522700.605828,
    "status": 0
  }
}
stop
```

















- Python
- Proto
- C#
- Java
- C++
- JavaScript





`on_recv_rsp(self, rsp_pb)`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD. After receiving the
  order fill information pushed by OpenD, this function is called. You
  need to override on_recv_rsp in the derived class.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**

  | Parameter | Type | Description |
  |:---|:---|:---|
  | rsp_pb | Trd_UpdateOrderFill_pb2.Response | This parameter does not need to be processed in the derived class. |

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
    <td style="text-align: left;">Fill price.</td>
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
from time import sleep
class TradeDealTest(TradeDealHandlerBase):
    """ order update push"""
    def on_recv_rsp(self, rsp_pb):
        ret, content = super(TradeDealTest, self).on_recv_rsp(rsp_pb)
        if ret == RET_OK:
            print("TradeDealTest content={}".format(content))
        return ret, content

trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUINC)
trd_ctx.set_handler(TradeDealTest())
print(trd_ctx.place_order(price=595.0, qty=100, code="US.AAPL", trd_side=TrdSide.BUY))

sleep(15)
trd_ctx.close()
```





- **Output**



``` python
TradeDealTest content=  trd_env      code stock_name              deal_id             order_id    qty  price trd_side              create_time  counter_broker_id counter_broker_name trd_market status
0    REAL  US.AAPL      Apple Inc.  2511067564122483295  8561504228375901919  100.0  518.0      BUY  2021-11-04 11:29:41.595                  5                   5         US     OK
```









## <a href="#5508-2" class="header-anchor">#</a> Trd_UpdateOrderFill.proto

- **Description**

  Respond to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

  2218





`virtual void OnReply_UpdateOrderFill(MMAPI_Conn client, uint nSerialNo, TrdUpdateOrderFill.Response rsp);`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

        //Subscribe first to get push
        TrdSubAccPush.C2S c2s = TrdSubAccPush.C2S.CreateBuilder()
                .AddAccIDList(281753457989306260L)
                .Build();
        TrdSubAccPush.Request req = TrdSubAccPush.Request.CreateBuilder().SetC2S(c2s).Build();
        uint seqNo = trd.SubAccPush(req);
        Console.Write("Send TrdSubAccPush: {0}\n", seqNo);
    }

    
    public void OnDisconnect(MMAPI_Conn client, long errCode) {
        Console.Write("Trd onDisConnect: {0}\n", errCode);
    }

    public void OnReply_SubAccPush(MMAPI_Conn client, uint nSerialNo, TrdSubAccPush.Response rsp)
    {
        Console.Write("OnReply_SubAccPush: {0}\n", nSerialNo, rsp.ToString());
    }

    public void OnReply_UpdateOrderFill(MMAPI_Conn client, uint nSerialNo, TrdUpdateOrderFill.Response rsp)
    {
        Console.Write("Push: TrdUpdateOrderFill: {0}\n", nSerialNo);
        Console.Write("retMsg: {0}\n", rsp.RetMsg);
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
Trd onInitConnect: ret=0 desc= connID=6827940248993029021
Send TrdSubAccPush: 3
OnReply_SubAccPush: 3
Push: TrdUpdateOrderFill: 1
retMsg:
```









`void onPush_UpdateOrderFill(MMAPI_Conn client, int nSerialNo, TrdUpdateOrderFill.Response rsp);`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

        //Subscribe first to get push
        TrdSubAccPush.C2S c2s = TrdSubAccPush.C2S.newBuilder()
                .addAccIDList(281753457989306260L)
                .build();
        TrdSubAccPush.Request req = TrdSubAccPush.Request.newBuilder().setC2S(c2s).build();
        int seqNo = trd.subAccPush(req);
        System.out.printf("Send TrdSubAccPush: %d\n", seqNo);
    }

    @Override
    public void onDisconnect(MMAPI_Conn client, long errCode) {
        System.out.printf("Trd onDisConnect: %d\n", errCode);
    }

    @Override
    public void onPush_UpdateOrderFill(MMAPI_Conn client, TrdUpdateOrderFill.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdUpdateOrderFill failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdUpdateOrderFill: %s\n", json);
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
Send TrdUpdateOrderFill: 2
Receive TrdUpdateOrderFill: {
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
      "name": "Futu Holdings Limited",
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









`virtual void OnPush_UpdateOrderFill(const Trd_UpdateOrderFill::Response &stRsp) = 0;`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

        Trd_SubAccPush::Request req;
        Trd_SubAccPush::C2S *c2s = req.mutable_c2s();
        c2s->add_accidlist(3637840);
        
        m_SubAccPushSerialNo = m_pTrdApi->SubAccPush(req);
        cout << "Request SubAccPush SerialNo: " << m_SubAccPushSerialNo << endl;
    }

    virtual void OnReply_SubAccPush(moomoo::u32_t nSerialNo, const Trd_SubAccPush::Response &stRsp) {
        if(nSerialNo == m_SubAccPushSerialNo)
        {
            cout << "OnReply_SubAccPush SerialNo: " << nSerialNo << endl;
            if (stRsp.rettype() != Common::RetType::RetType_Succeed)
            {
                cout << "SubAccPush Failed" << endl;
                return;
            }
        }
    }

    virtual void OnPush_UpdateOrderFill(const Trd_UpdateOrderFill::Response &stRsp)
    {
        cout << "OnPush_UpdateOrderFill:" << endl;
        // print response
        // ProtoBufToBodyData and UTF8ToLocal refer to tool.h in Samples
        string resp_str;
        ProtoBufToBodyData(stRsp, resp_str);
        cout << UTF8ToLocal(resp_str) << endl;
    }

protected:
    MMAPI_Trd *m_pTrdApi;

    moomoo::u32_t m_SubAccPushSerialNo;
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
Request SubAccPush SerialNo: 4
OnReply_SubAccPush SerialNo: 4
OnPush_UpdateOrderFill:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFill": {
    "trdSide": 1,
    "fillID": "932511865781776209",
    "fillIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1.2",
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.606",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522700.605828,
    "updateTimestamp": 1631522700.605828,
    "status": 0
  }
}
```









`OnPush(cmd,res)`

- **Description**

  In response to the transaction push, asynchronously process the
  transaction status information pushed by OpenD.  
  This feature is only available for live trading and not for paper
  trading.

- **Parameters**



``` protobuf
message S2C
{
    required Trd_Common.TrdHeader header = 1; //Transaction common header
    required Trd_Common.OrderFill orderFill = 2; //Deal structure
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

function TrdUpdateOrderFill(){
    const { RetType } = Common
    const { TrdEnv, OrderType } = Trd_Common
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
                    let accIDList = accList.map((acc)=>{ return acc.accID }); // Subscribe to the transaction push of all accounts
                    
                    const req = {
                        c2s: {
                            accIDList: accIDList,
                        },
                    };

                    websocket.SubAccPush(req)
                    .then((res) => {
                        let { errCode, retMsg, retType,s2c } = res
                        console.log("SubAccPush: errCode %d, retMsg %s, retType %d", errCode, retMsg, retType); 
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

    websocket.onPush = (cmd, res)=>{
        if(mmCmdID.TrdUpdateOrderFill.cmd == cmd){  
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                let data = beautify(JSON.stringify(s2c), {
                    indent_size: 2,
                    space_in_empty_paren: true,
                });
                console.log("TrdUpdateOrderFill:");
                console.log(data);
            } else {
                console.log("TrdUpdateOrderFillTest: error")
            }
        }
    };

    websocket.start(addr, port, enable_ssl, key);
    
    // After using the connection, remember to close it to prevent the number of connections from running out
    setTimeout(()=>{ 
        websocket.stop();
        console.log("stop");
    }, 3600*1000); // Set the script to receive OpenD push duration to 3600 seconds
}
```





- **Output**



``` javascript
SubAccPush: errCode 0, retMsg , retType 0
null
TrdUpdateOrderFill:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "orderFill": {
    "trdSide": 1,
    "fillID": "932511865781776209",
    "fillIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1.2",
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.606",
    "counterBrokerID": 5,
    "counterBrokerName": "",
    "secMarket": 1,
    "createTimestamp": 1631522700.605828,
    "updateTimestamp": 1631522700.605828,
    "status": 0
  }
}
stop
```



















