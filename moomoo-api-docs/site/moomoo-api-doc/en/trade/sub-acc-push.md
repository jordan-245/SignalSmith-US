



# <a href="#826" class="header-anchor">#</a> Subscribe to Transaction Push









- Python
- Proto
- C#
- Java
- C++
- JavaScript





Python does not need to subscribe to transaction push





## <a href="#7366" class="header-anchor">#</a> Trd_Trade Data Callback.proto

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **协议 ID**

  2008





`uint SubAccPush(TrdSubAccPush.Request req);`  
`virtual void OnReply_SubAccPush(FTAPI_Conn client, uint nSerialNo, TrdSubAccPush.Response rsp);`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : FTSPI_Trd, FTSPI_Conn {
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
        Console.Write("Reply: TrdSubAccPush: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827944734875485972
Send TrdSubAccPush: 3
Reply: TrdSubAccPush: 3
retMsg:
```









`int subAccPush(TrdSubAccPush.Request req);`  
`void onReply_SubAccPush(FTAPI_Conn client, int nSerialNo, TrdSubAccPush.Response rsp);`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
    public void onReply_SubAccPush(FTAPI_Conn client, int nSerialNo, TrdSubAccPush.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdSubAccPush failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdSubAccPush: %s\n", json);
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
OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 5,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:06",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225606,
   "remark": "",
   "timeInForce": 0
  }
 }
}

OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 15,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:22",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225622,
   "remark": "",
   "timeInForce": 0
  }
 }
}
```









`Futu::u32_t SubAccPush(const Trd_SubAccPush::Request &stReq);`  
`virtual void OnReply_SubAccPush(Futu::u32_t nSerialNo, const Trd_SubAccPush::Response &stRsp) = 0;`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





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

    virtual void OnPush_UpdateOrder(const Trd_UpdateOrder::Response &stRsp)
    {
        cout << "OnPush_UpdateOrder:" << endl;
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
OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 5,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:06",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225606,
   "remark": "",
   "timeInForce": 0
  }
 }
}

OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 15,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:22",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225622,
   "remark": "",
   "timeInForce": 0
  }
 }
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)





`SubAccPush(req);`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import ftWebsocket from "futu-api";
import { ftCmdID } from "futu-api";
import { Common, Qot_Common, Trd_Common } from "futu-api/proto";
import beautify from "js-beautify";

function TrdSubAccPush(){
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
        } else if(ftCmdID.TrdUpdateOrder.cmd == cmd){  
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                let data = beautify(JSON.stringify(s2c), {
                    indent_size: 2,
                    space_in_empty_paren: true,
                });
                console.log("TrdUpdateOrder:");
                console.log(data);
            } else {
                console.log("TrdUpdateOrderTest: error")
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
TrdUpdateOrder:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "order": {
    "trdSide": 1,
    "orderType": 1,
    "orderStatus": 2,
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00",
    "updateTime": "2021-09-13 16:45:00",
    "fillQty": 0,
    "fillAvgPrice": 0,
    "secMarket": 1,
    "createTimestamp": 1631522700,
    "updateTimestamp": 1631522700,
    "remark": "",
    "timeInForce": 0
  }
}
TrdUpdateOrder:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "order": {
    "trdSide": 1,
    "orderType": 1,
    "orderStatus": 5,
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.313",
    "updateTime": "2021-09-13 16:45:00.568",
    "fillQty": 0,
    "fillAvgPrice": 0,
    "secMarket": 1,
    "createTimestamp": 1631522700.312849,
    "updateTimestamp": 1631522700.567732,
    "remark": "",
    "timeInForce": 0
  }
}
TrdUpdateOrder:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "order": {
    "trdSide": 1,
    "orderType": 1,
    "orderStatus": 11,
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.313",
    "updateTime": "2021-09-13 16:45:00.604",
    "fillQty": 100,
    "fillAvgPrice": 480,
    "secMarket": 1,
    "createTimestamp": 1631522700.312849,
    "updateTimestamp": 1631522700.604215,
    "remark": "",
    "timeInForce": 0
  }
}
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





Python does not need to subscribe to transaction push





## <a href="#6589" class="header-anchor">#</a> Trd_SubAccPush.proto

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **协议 ID**

  2008





`uint SubAccPush(TrdSubAccPush.Request req);`  
`virtual void OnReply_SubAccPush(MMAPI_Conn client, uint nSerialNo, TrdSubAccPush.Response rsp);`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` cs
public class Program : MMSPI_Trd, MMSPI_Conn {
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
        Console.Write("Reply: TrdSubAccPush: {0}\n", nSerialNo);
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
Trd onInitConnect: ret=0 desc= connID=6827944734875485972
Send TrdSubAccPush: 3
Reply: TrdSubAccPush: 3
retMsg:
```









`int subAccPush(TrdSubAccPush.Request req);`  
`void onReply_SubAccPush(MMAPI_Conn client, int nSerialNo, TrdSubAccPush.Response rsp);`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





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
    public void onReply_SubAccPush(MMAPI_Conn client, int nSerialNo, TrdSubAccPush.Response rsp) {
        if (rsp.getRetType() != 0) {
            System.out.printf("TrdSubAccPush failed: %s\n", rsp.getRetMsg());
        }
        else {
            try {
                String json = JsonFormat.printer().print(rsp);
                System.out.printf("Receive TrdSubAccPush: %s\n", json);
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
OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 5,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:06",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225606,
   "remark": "",
   "timeInForce": 0
  }
 }
}

OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 15,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:22",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225622,
   "remark": "",
   "timeInForce": 0
  }
 }
}
```









`moomoo::u32_t SubAccPush(const Trd_SubAccPush::Request &stReq);`  
`virtual void OnReply_SubAccPush(moomoo::u32_t nSerialNo, const Trd_SubAccPush::Response &stRsp) = 0;`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





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

    virtual void OnPush_UpdateOrder(const Trd_UpdateOrder::Response &stRsp)
    {
        cout << "OnPush_UpdateOrder:" << endl;
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
OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 5,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:06",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225606,
   "remark": "",
   "timeInForce": 0
  }
 }
}

OnPush_UpdateOrder:
{
 "retType": 0,
 "s2c": {
  "header": {
   "trdEnv": 0,
   "accID": "3637840",
   "trdMarket": 1
  },
  "order": {
   "trdSide": 1,
   "orderType": 5,
   "orderStatus": 15,
   "orderID": "3964487190993133422",
   "orderIDEx": "1741803",
   "code": "00700",
   "name": "Tencent",
   "qty": 100,
   "price": 607.5,
   "createTime": "2021-06-09 16:00:06",
   "updateTime": "2021-06-09 16:00:22",
   "fillQty": 0,
   "fillAvgPrice": 0,
   "secMarket": 1,
   "createTimestamp": 1623225606,
   "updateTimestamp": 1623225622,
   "remark": "",
   "timeInForce": 0
  }
 }
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)





`SubAccPush(req);`

- **Description**

  Subscribe to receive pushed data from trading accounts Specify the
  connection that sends the protocol to receive transaction data push
  (order status, transaction status, etc.)

- **Parameters**



``` protobuf
message C2S
{
    repeated uint64 accIDList = 1; //The list of trading accounts that want to receive pushed data. Always pass the full account list, that is, users should pass all trading accounts that need to receive pushed data every time
}

message Request
{
    required C2S c2s = 1;
}
```





- **Return**



``` protobuf
message S2C
{
    
}

message Response
{
    //以下3个字段每条协议都有，注释说明在 InitConnect.proto 中
    required int32 retType = 1 [default = -400];
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```





> - For interface result, refer to
>   [RetType](/moomoo-api-doc/en/ftapi/common.html#8800)

- **Example**



``` javascript
import mmWebsocket from "moomoo-api";
import { mmCmdID } from "moomoo-api";
import { Common, Qot_Common, Trd_Common } from "moomoo-api/proto";
import beautify from "js-beautify";

function TrdSubAccPush(){
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
        } else if(ftCmdID.TrdUpdateOrder.cmd == cmd){  
            let { retType, s2c } = res
            if(retType == RetType.RetType_Succeed){
                let data = beautify(JSON.stringify(s2c), {
                    indent_size: 2,
                    space_in_empty_paren: true,
                });
                console.log("TrdUpdateOrder:");
                console.log(data);
            } else {
                console.log("TrdUpdateOrderTest: error")
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
TrdUpdateOrder:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "order": {
    "trdSide": 1,
    "orderType": 1,
    "orderStatus": 2,
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00",
    "updateTime": "2021-09-13 16:45:00",
    "fillQty": 0,
    "fillAvgPrice": 0,
    "secMarket": 1,
    "createTimestamp": 1631522700,
    "updateTimestamp": 1631522700,
    "remark": "",
    "timeInForce": 0
  }
}
TrdUpdateOrder:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "order": {
    "trdSide": 1,
    "orderType": 1,
    "orderStatus": 5,
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.313",
    "updateTime": "2021-09-13 16:45:00.568",
    "fillQty": 0,
    "fillAvgPrice": 0,
    "secMarket": 1,
    "createTimestamp": 1631522700.312849,
    "updateTimestamp": 1631522700.567732,
    "remark": "",
    "timeInForce": 0
  }
}
TrdUpdateOrder:
{
  "header": {
    "trdEnv": 1,
    "accID": "281756455988249902",
    "trdMarket": 1
  },
  "order": {
    "trdSide": 1,
    "orderType": 1,
    "orderStatus": 11,
    "orderID": "4883217202603317248",
    "orderIDEx": "20210913_5915950_OD|pM+9NqXZAaxnZYpScrsjT4zHWtlk1",
    "code": "00700",
    "name": "Tencent",
    "qty": 100,
    "price": 480,
    "createTime": "2021-09-13 16:45:00.313",
    "updateTime": "2021-09-13 16:45:00.604",
    "fillQty": 100,
    "fillAvgPrice": 480,
    "secMarket": 1,
    "createTimestamp": 1631522700.312849,
    "updateTimestamp": 1631522700.604215,
    "remark": "",
    "timeInForce": 0
  }
}
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



















