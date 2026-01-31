



# <a href="#2412" class="header-anchor">#</a> General Definitions

## <a href="#8800" class="header-anchor">#</a> Interface Result





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **RET_CODE**

- `RET_OK`

  Success

- `RET_ERROR`

  Failed





**RetType**



``` protobuf
enum RetType
{
  RetType_Succeed = 0; //Success
  RetType_Failed = -1; //Failed
  RetType_TimeOut = -100; //Timeout
  RetType_Unknown = -400; //Unknown result
}
```









**RetType**



``` protobuf
enum RetType
{
  RetType_Succeed = 0; //Success
  RetType_Failed = -1; //Failed
  RetType_TimeOut = -100; //Timeout
  RetType_Unknown = -400; //Unknown result
}
```









**RetType**



``` protobuf
enum RetType
{
  RetType_Succeed = 0; //Success
  RetType_Failed = -1; //Failed
  RetType_TimeOut = -100; //Timeout
  RetType_Unknown = -400; //Unknown result
}
```









**RetType**



``` protobuf
enum RetType
{
  RetType_Succeed = 0; //Success
  RetType_Failed = -1; //Failed
  RetType_TimeOut = -100; //Timeout
  RetType_Unknown = -400; //Unknown result
}
```









**RetType**



``` protobuf
enum RetType
{
  RetType_Succeed = 0; //Success
  RetType_Failed = -1; //Failed
  RetType_TimeOut = -100; //Timeout
  RetType_Unknown = -400; //Unknown result
}
```









## <a href="#4358" class="header-anchor">#</a> Protocol Format





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **ProtoFMT**

- `Protobuf`

  Google Protobuf

- `Json`

  Json





**ProtoFmt**



``` protobuf
enum ProtoFmt
{
  ProtoFmt_Protobuf = 0; //Google Protobuf
  ProtoFmt_Json = 1; //Json
}
```









**ProtoFmt**



``` protobuf
enum ProtoFmt
{
  ProtoFmt_Protobuf = 0; //Google Protobuf
  ProtoFmt_Json = 1; //Json
}
```









**ProtoFmt**



``` protobuf
enum ProtoFmt
{
  ProtoFmt_Protobuf = 0; //Google Protobuf
  ProtoFmt_Json = 1; //Json
}
```









**ProtoFmt**



``` protobuf
enum ProtoFmt
{
  ProtoFmt_Protobuf = 0; //Google Protobuf
  ProtoFmt_Json = 1; //Json
}
```









**ProtoFmt**



``` protobuf
enum ProtoFmt
{
  ProtoFmt_Protobuf = 0; //Google Protobuf
  ProtoFmt_Json = 1; //Json
}
```









## <a href="#3338" class="header-anchor">#</a> Packet Encryption Algorithm





- Python
- Proto
- C#
- Java
- C++
- JavaScript









**PacketEncAlgo**







``` protobuf
enum PacketEncAlgo
{
  PacketEncAlgo_FTAES_ECB = 0; //AES ECB mode encryption modified by Futu
  PacketEncAlgo_None = -1; //No encryption
  PacketEncAlgo_AES_ECB = 1; //Standard AES ECB mode encryption
  PacketEncAlgo_AES_CBC = 2; //Standard AES CBC mode encryption
}
```











``` protobuf
enum PacketEncAlgo
{
  PacketEncAlgo_FTAES_ECB = 0; //AES ECB mode encryption modified by moomoo
  PacketEncAlgo_None = -1; //No encryption
  PacketEncAlgo_AES_ECB = 1; //Standard AES ECB mode encryption
  PacketEncAlgo_AES_CBC = 2; //Standard AES CBC mode encryption
}
```













**PacketEncAlgo**







``` protobuf
enum PacketEncAlgo
{
  PacketEncAlgo_FTAES_ECB = 0; //AES ECB mode encryption modified by Futu
  PacketEncAlgo_None = -1; //No encryption
  PacketEncAlgo_AES_ECB = 1; //Standard AES ECB mode encryption
  PacketEncAlgo_AES_CBC = 2; //Standard AES CBC mode encryption
}
```











``` protobuf
enum PacketEncAlgo
{
  PacketEncAlgo_FTAES_ECB = 0; //AES ECB mode encryption modified by moomoo
  PacketEncAlgo_None = -1; //No encryption
  PacketEncAlgo_AES_ECB = 1; //Standard AES ECB mode encryption
  PacketEncAlgo_AES_CBC = 2; //Standard AES CBC mode encryption
}
```

























## <a href="#9803" class="header-anchor">#</a> Program Status Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **ProgramStatusType**

- `NONE`

  Unknown

- `LOADED`

  The necessary modules have been loaded

- `LOGING`

  Logging in

- `NEED_PIC_VERIFY_CODE`

  Need graphic verification code

- `NEED_PHONE_VERIFY_CODE`

  Need mobile phone verification code

- `LOGIN_FAILED`

  Login failed

- `FORCE_UPDATE`

  The client version is too low

- `NESSARY_DATA_PREPARING`

  Pulling necessary information

- `NESSARY_DATA_MISSING`

  Missing necessary information

- `UN_AGREE_DISCLAIMER`

  Disclaimer is not agreed

- `READY`

  Ready to use

- `FORCE_LOGOUT`

  OpenD was forced to log out





**ProgramStatusType**



``` protobuf
enum ProgramStatusType
{
  ProgramStatusType_None = 0;
  ProgramStatusType_Loaded = 1; //Operations such as loading configuration and starting the server have been completed, and the status  before the server is started does not need to be returned

  ProgramStatusType_Loging = 2; //Logging in
  ProgramStatusType_NeedPicVerifyCode = 3; //Need a graphic verification code
  ProgramStatusType_NeedPhoneVerifyCode = 4; //Need phone verification code
  ProgramStatusType_LoginFailed = 5; //Login failed, and the reason is returned in the description
  ProgramStatusType_ForceUpdate = 6; //The client version is too low

  ProgramStatusType_NessaryDataPreparing = 7; //Some necessary information like disclaimer is being pulled
  ProgramStatusType_NessaryDataMissing = 8; //Missing necessary information
  ProgramStatusType_UnAgreeDisclaimer = 9; //Disclaimer is not agreed
  ProgramStatusType_Ready = 10; //Can receive and send the business protocol, normal available status

  //OpenD is forced to log out after logging in, which will cause all the connections to be disconnected. You need to reconnect to get  the following status (and need to be in ui mode)
  ProgramStatusType_ForceLogout = 11; //Is forced to log out, because of changing the login password, opening the device lock, etc. The reason is returned in the description

  ProgramStatusType_DisclaimerPullFailed = 12; //Failed to get disclaimers
}
```









**ProgramStatusType**



``` protobuf
enum ProgramStatusType
{
  ProgramStatusType_None = 0;
  ProgramStatusType_Loaded = 1; //Operations such as loading configuration and starting the server have been completed, and the status  before the server is started does not need to be returned

  ProgramStatusType_Loging = 2; //Logging in
  ProgramStatusType_NeedPicVerifyCode = 3; //Need a graphic verification code
  ProgramStatusType_NeedPhoneVerifyCode = 4; //Need phone verification code
  ProgramStatusType_LoginFailed = 5; //Login failed, and the reason is returned in the description
  ProgramStatusType_ForceUpdate = 6; //The client version is too low

  ProgramStatusType_NessaryDataPreparing = 7; //Some necessary information like disclaimer is being pulled
  ProgramStatusType_NessaryDataMissing = 8; //Missing necessary information
  ProgramStatusType_UnAgreeDisclaimer = 9; //Disclaimer is not agreed
  ProgramStatusType_Ready = 10; //Can receive and send the business protocol, normal available status

  //OpenD is forced to log out after logging in, which will cause all the connections to be disconnected. You need to reconnect to get  the following status (and need to be in ui mode)
  ProgramStatusType_ForceLogout = 11; //is forced to log out, because of changing the login password, opening the device lock, etc. The reason is returned in the description

  ProgramStatusType_DisclaimerPullFailed = 12; //Failed to get disclaimers
}
```









**ProgramStatusType**



``` protobuf
enum ProgramStatusType
{
  ProgramStatusType_None = 0;
  ProgramStatusType_Loaded = 1; //Operations such as loading configuration and starting the server have been completed, and the status  before the server is started does not need to be returned

  ProgramStatusType_Loging = 2; //Logging in
  ProgramStatusType_NeedPicVerifyCode = 3; //Need a graphic verification code
  ProgramStatusType_NeedPhoneVerifyCode = 4; //Need phone verification code
  ProgramStatusType_LoginFailed = 5; //Login failed, and the reason is returned in the description
  ProgramStatusType_ForceUpdate = 6; //The client version is too low

  ProgramStatusType_NessaryDataPreparing = 7; //Some necessary information like disclaimer is being pulled
  ProgramStatusType_NessaryDataMissing = 8; //Missing necessary information
  ProgramStatusType_UnAgreeDisclaimer = 9; //Disclaimer is not agreed
  ProgramStatusType_Ready = 10; //Can receive and send the business protocol, normal available status

  //OpenD is forced to log out after logging in, which will cause all the connections to be disconnected. You need to reconnect to get  the following status (and need to be in ui mode)
  ProgramStatusType_ForceLogout = 11; //is forced to log out, because of changing the login password, opening the device lock, etc. The reason is returned in the description

  ProgramStatusType_DisclaimerPullFailed = 12; //Failed to get disclaimers
}
```









**ProgramStatusType**



``` protobuf
enum ProgramStatusType
{
  ProgramStatusType_None = 0;
  ProgramStatusType_Loaded = 1; //Operations such as loading configuration and starting the server have been completed, and the status  before the server is started does not need to be returned

  ProgramStatusType_Loging = 2; //Logging in
  ProgramStatusType_NeedPicVerifyCode = 3; //Need a graphic verification code
  ProgramStatusType_NeedPhoneVerifyCode = 4; //Need phone verification code
  ProgramStatusType_LoginFailed = 5; //Login failed, and the reason is returned in the description
  ProgramStatusType_ForceUpdate = 6; //The client version is too low

  ProgramStatusType_NessaryDataPreparing = 7; //Some necessary information like disclaimer is being pulled
  ProgramStatusType_NessaryDataMissing = 8; //Missing necessary information
  ProgramStatusType_UnAgreeDisclaimer = 9; //Disclaimer is not agreed
  ProgramStatusType_Ready = 10; //Can receive and send the business protocol, normal available status

  //OpenD is forced to log out after logging in, which will cause all the connections to be disconnected. You need to reconnect to get  the following status (and need to be in ui mode)
  ProgramStatusType_ForceLogout = 11; //is forced to log out, because of changing the login password, opening the device lock, etc. The reason is returned in the description

  ProgramStatusType_DisclaimerPullFailed = 12; //Failed to get disclaimers
}
```









**ProgramStatusType**



``` protobuf
enum ProgramStatusType
{
  ProgramStatusType_None = 0;
  ProgramStatusType_Loaded = 1; //Operations such as loading configuration and starting the server have been completed, and the status  before the server is started does not need to be returned

  ProgramStatusType_Loging = 2; //Logging in
  ProgramStatusType_NeedPicVerifyCode = 3; //Need a graphic verification code
  ProgramStatusType_NeedPhoneVerifyCode = 4; //Need phone verification code
  ProgramStatusType_LoginFailed = 5; //Login failed, and the reason is returned in the description
  ProgramStatusType_ForceUpdate = 6; //The client version is too low

  ProgramStatusType_NessaryDataPreparing = 7; //Some necessary information like disclaimer is being pulled
  ProgramStatusType_NessaryDataMissing = 8; //Missing necessary information
  ProgramStatusType_UnAgreeDisclaimer = 9; //Disclaimer is not agreed
  ProgramStatusType_Ready = 10; //Can receive and send the business protocol, normal available status

  //OpenD is forced to log out after logging in, which will cause all the connections to be disconnected. You need to reconnect to get  the following status (and need to be in ui mode)
  ProgramStatusType_ForceLogout = 11; //is forced to log out, because of changing the login password, opening the device lock, etc. The reason is returned in the description

  ProgramStatusType_DisclaimerPullFailed = 12; //Failed to get disclaimers
}
```









## <a href="#1581" class="header-anchor">#</a> OpenD Event Notification Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **GtwEventType**

- `LocalCfgLoadFailed`

  Failed to load the local configuration file

- `APISvrRunFailed`

  Failed to run the OpenD monitoring service

- `ForceUpdate`

  Force upgrade of the OpenD





- `LoginFailed`

  Failed to log in to Futu servers





- `LoginFailed`

  Failed to log in to moomoo servers





- `UnAgreeDisclaimer`

  Did not agree to the disclaimer, unable to run

- `LOGIN_FAILED`

  Login failed

- `NetCfgMissing`

  Missing network connection configuration

- `KickedOut`

  Login kicked offline

- `LoginPwdChanged`

  Login password has been changed





- `BanLogin`

  This account is not allowed to log in by Futu servers





- `BanLogin`

  This account is not allowed to log in by moomoo servers





- `NeedPicVerifyCode`

  Need graphic verification code

- `NeedPhoneVerifyCode`

  Need mobile verification code

- `AppDataNotExist`

  Program package data loss

- `NessaryDataMissing`

  The necessary data is not synchronized successfully

- `TradePwdChanged`

  Transaction password change notice

- `EnableDeviceLock`

  Need to enable device lock





**GtwEventType**



``` protobuf
enum GtwEventType
{
  GtwEventType_None = 0; //No error
  GtwEventType_LocalCfgLoadFailed = 1; //Load local configuration failed
  GtwEventType_APISvrRunFailed = 2; //Server start failed
  GtwEventType_ForceUpdate = 3; //The client version is too low
  GtwEventType_LoginFailed = 4; //Login failed
  GtwEventType_UnAgreeDisclaimer = 5; //Disclaimer is not agreed
  GtwEventType_NetCfgMissing = 6; //Missing necessary network configuration information. For example, to control the subscription quota //It has been optimized and this situation will not occur again
  GtwEventType_KickedOut = 7; //Account is logged in elsewhere
  GtwEventType_LoginPwdChanged = 8; //Login password has been changed
  GtwEventType_BanLogin = 9; //User is forbidden to log in
  GtwEventType_NeedPicVerifyCode = 10; //Need graphic verification code
  GtwEventType_NeedPhoneVerifyCode = 11; //Need phone verification code
  GtwEventType_AppDataNotExist = 12; //The program's own data does not exist
  GtwEventType_NessaryDataMissing = 13; //Missing necessary data
  GtwEventType_TradePwdChanged = 14; //Trading password has been changed
  GtwEventType_EnableDeviceLock = 15; //Enable device lock
}
```









**GtwEventType**



``` protobuf
enum GtwEventType
{
  GtwEventType_None = 0; //No error
  GtwEventType_LocalCfgLoadFailed = 1; //Load local configuration failed
  GtwEventType_APISvrRunFailed = 2; //Server start failed
  GtwEventType_ForceUpdate = 3; //The client version is too low
  GtwEventType_LoginFailed = 4; //Login failed
  GtwEventType_UnAgreeDisclaimer = 5; //Disclaimer is not agreed
  GtwEventType_NetCfgMissing = 6; //Missing necessary network configuration information. For example, to control the subscription quota //It has been optimized and this situation will not occur again
  GtwEventType_KickedOut = 7; //Account is logged in elsewhere
  GtwEventType_LoginPwdChanged = 8; //Login password has been changed
  GtwEventType_BanLogin = 9; //User is forbidden to log in
  GtwEventType_NeedPicVerifyCode = 10; //Need graphic verification code
  GtwEventType_NeedPhoneVerifyCode = 11; //Need phone verification code
  GtwEventType_AppDataNotExist = 12; //The program's own data does not exist
  GtwEventType_NessaryDataMissing = 13; //Missing necessary data
  GtwEventType_TradePwdChanged = 14; //Trading password has been changed
  GtwEventType_EnableDeviceLock = 15; //Enable device lock
}
```









**GtwEventType**



``` protobuf
enum GtwEventType
{
  GtwEventType_None = 0; //No error
  GtwEventType_LocalCfgLoadFailed = 1; //Load local configuration failed
  GtwEventType_APISvrRunFailed = 2; //Server start failed
  GtwEventType_ForceUpdate = 3; //The client version is too low
  GtwEventType_LoginFailed = 4; //Login failed
  GtwEventType_UnAgreeDisclaimer = 5; //Disclaimer is not agreed
  GtwEventType_NetCfgMissing = 6; //Missing necessary network configuration information. For example, to control the subscription quota //It has been optimized and this situation will not occur again
  GtwEventType_KickedOut = 7; //Account is logged in elsewhere
  GtwEventType_LoginPwdChanged = 8; //Login password has been changed
  GtwEventType_BanLogin = 9; //User is forbidden to log in
  GtwEventType_NeedPicVerifyCode = 10; //Need graphic verification code
  GtwEventType_NeedPhoneVerifyCode = 11; //Need phone verification code
  GtwEventType_AppDataNotExist = 12; //The program's own data does not exist
  GtwEventType_NessaryDataMissing = 13; //Missing necessary data
  GtwEventType_TradePwdChanged = 14; //Trading password has been changed
  GtwEventType_EnableDeviceLock = 15; //Enable device lock
}
```









**GtwEventType**



``` protobuf
enum GtwEventType
{
  GtwEventType_None = 0; //No error
  GtwEventType_LocalCfgLoadFailed = 1; //Load local configuration failed
  GtwEventType_APISvrRunFailed = 2; //Server start failed
  GtwEventType_ForceUpdate = 3; //The client version is too low
  GtwEventType_LoginFailed = 4; //Login failed
  GtwEventType_UnAgreeDisclaimer = 5; //Disclaimer is not agreed
  GtwEventType_NetCfgMissing = 6; //Missing necessary network configuration information. For example, to control the subscription quota //It has been optimized and this situation will not occur again
  GtwEventType_KickedOut = 7; //Account is logged in elsewhere
  GtwEventType_LoginPwdChanged = 8; //Login password has been changed
  GtwEventType_BanLogin = 9; //User is forbidden to log in
  GtwEventType_NeedPicVerifyCode = 10; //Need graphic verification code
  GtwEventType_NeedPhoneVerifyCode = 11; //Need phone verification code
  GtwEventType_AppDataNotExist = 12; //The program's own data does not exist
  GtwEventType_NessaryDataMissing = 13; //Missing necessary data
  GtwEventType_TradePwdChanged = 14; //Trading password has been changed
  GtwEventType_EnableDeviceLock = 15; //Enable device lock
}
```









**GtwEventType**



``` protobuf
enum GtwEventType
{
  GtwEventType_None = 0; //No error
  GtwEventType_LocalCfgLoadFailed = 1; //Load local configuration failed
  GtwEventType_APISvrRunFailed = 2; //Server start failed
  GtwEventType_ForceUpdate = 3; //The client version is too low
  GtwEventType_LoginFailed = 4; //Login failed
  GtwEventType_UnAgreeDisclaimer = 5; //Disclaimer is not agreed
  GtwEventType_NetCfgMissing = 6; //Missing necessary network configuration information. For example, to control the subscription quota //It has been optimized and this situation will not occur again
  GtwEventType_KickedOut = 7; //Account is logged in elsewhere
  GtwEventType_LoginPwdChanged = 8; //Login password has been changed
  GtwEventType_BanLogin = 9; //User is forbidden to log in
  GtwEventType_NeedPicVerifyCode = 10; //Need graphic verification code
  GtwEventType_NeedPhoneVerifyCode = 11; //Need phone verification code
  GtwEventType_AppDataNotExist = 12; //The program's own data does not exist
  GtwEventType_NessaryDataMissing = 13; //Missing necessary data
  GtwEventType_TradePwdChanged = 14; //Trading password has been changed
  GtwEventType_EnableDeviceLock = 15; //Enable device lock
}
```









## <a href="#5979" class="header-anchor">#</a> System Notification Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SysNotifyType**

- `GTW_EVENT`

  Gateway event

- `PROGRAM_STATUS`

  Program status changes





- `CONN_STATUS`

  Status of Connection to Futu servers has been changed





- `CONN_STATUS`

  Status of Connection to moomoo servers has been changed





- `QOT_RIGHT`

  Quotes authority changed





**NotifyType**



``` protobuf
enum NotifyType
{
  NotifyType_None = 0; //None
  NotifyType_GtwEvent = 1; //OpenD running event notification
  NotifyType_ProgramStatus = 2; //Program status
  NotifyType_ConnStatus = 3; //Connection status
  NotifyType_QotRight = 4; //Quotes authority
  NotifyType_APILevel = 5; //User level, has been deprecated after version 2.10
  NotifyType_APIQuota = 6; //API Quota
}
```









**NotifyType**



``` protobuf
enum NotifyType
{
  NotifyType_None = 0; //None
  NotifyType_GtwEvent = 1; //OpenD running event notification
  NotifyType_ProgramStatus = 2; //Program status
  NotifyType_ConnStatus = 3; //Connection status
  NotifyType_QotRight = 4; //Quotes authority
  NotifyType_APILevel = 5; //User level, has been deprecated after version 2.10
  NotifyType_APIQuota = 6; //API Quota
}
```









**NotifyType**



``` protobuf
enum NotifyType
{
  NotifyType_None = 0; //None
  NotifyType_GtwEvent = 1; //OpenD running event notification
  NotifyType_ProgramStatus = 2; //Program status
  NotifyType_ConnStatus = 3; //Connection status
  NotifyType_QotRight = 4; //Quotes authority
  NotifyType_APILevel = 5; //User level, has been deprecated after version 2.10
  NotifyType_APIQuota = 6; //API Quota
}
```









**NotifyType**



``` protobuf
enum NotifyType
{
  NotifyType_None = 0; //None
  NotifyType_GtwEvent = 1; //OpenD running event notification
  NotifyType_ProgramStatus = 2; //Program status
  NotifyType_ConnStatus = 3; //Connection status
  NotifyType_QotRight = 4; //Quotes authority
  NotifyType_APILevel = 5; //User level, has been deprecated after version 2.10
  NotifyType_APIQuota = 6; //API Quota
}
```









**NotifyType**



``` protobuf
enum NotifyType
{
  NotifyType_None = 0; //None
  NotifyType_GtwEvent = 1; //OpenD running event notification
  NotifyType_ProgramStatus = 2; //Program status
  NotifyType_ConnStatus = 3; //Connection status
  NotifyType_QotRight = 4; //Quotes authority
  NotifyType_APILevel = 5; //User level, has been deprecated after version 2.10
  NotifyType_APIQuota = 6; //API Quota
}
```









## <a href="#1903" class="header-anchor">#</a> Package Unique Identifier

**PacketID**



``` protobuf
message PacketID
{
  required uint64 connID = 1; //The current TCP connection ID, the unique identifier of a connection, returned by the InitConnect protocol
  required uint32 serialNo = 2; //Increment serial number
}
```





## <a href="#9898" class="header-anchor">#</a> Program Status

**ProgramStatus**



``` protobuf
message ProgramStatus
{
  required ProgramStatusType type = 1; //Current status
  optional string strExtDesc = 2; //Additional description
}
```











