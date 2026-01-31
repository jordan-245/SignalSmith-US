



# <a href="#8508" class="header-anchor">#</a> Protocol Introduction





Futu API is an API SDK, encapsulated by Futu including mainstream
programming languages (Python, Java, C \#, C++, JavaScript) to make it
easy for you to call and reduce the difficulty of trading strategy
development.  
This part mainly introduces the underlying protocol of communication
between script and OpenD service, which is suitable for users who do not
use the above five programming languages.





moomoo API is an API SDK, encapsulated by moomoo including mainstream
programming languages (Python, Java, C \#, C++, JavaScript) to make it
easy for you to call and reduce the difficulty of trading strategy
development.  
This part mainly introduces the underlying protocol of communication
between script and OpenD service, which is suitable for users who do not
use the above five programming languages.







Tips

- If you are using a programming language that is one of the five
  mainstream programming languages mentioned above, you can skip this
  part.



## <a href="#3541" class="header-anchor">#</a> Protocol Request Process

- Create a connection
- Initialize the connection
- Request data or receive pushed data
- Send KeepAlive protocol periodically to keep connected





![proto-process](/moomoo-api-doc/assets/img/proto-process.8a7ac8f2.png)





![proto-process](/moomoo-api-doc/assets/img/proto_mmprocess.12101855.png)





## <a href="#7508" class="header-anchor">#</a> Protocol Design

The protocol data includes the protocol header and the protocol body.
The protocol header is fixed, and the protocol body is determined
according to the specific protocol.

### <a href="#218" class="header-anchor">#</a> Protocol Header



``` text
struct APIProtoHeader
{
    u8_t szHeaderFlag[2];
    u32_t nProtoID;
    u8_t nProtoFmtType;
    u8_t nProtoVer;
    u32_t nSerialNo;
    u32_t nBodyLen;
    u8_t arrBodySHA1[20];
    u8_t arrReserved[8];
};
```





| Field | Description |
|:---|:---|
| szHeaderFlag | Packet header start flag, fixed as "FT" |
| nProtoID | Protocol ID |
| nProtoFmtType | Protocol type, 0 for Protobuf, 1 for Json |
| nProtoVer | Protocol version, used for iterative compatibility, currently 0 |
| nSerialNo | Packet serial number, used to correspond to the request packet and return packet, and it is required to be incremented |
| nBodyLen | Body length |
| arrBodySHA1 | SHA1 hash value of the original data of the packet body (after decryption) |
| arrReserved | Reserved 8-byte extension |



Tips

- ***u8_t*** refer to 8-bit unsigned integer, ***u32_t*** refer to
  32-bit unsigned integer
- ***OpenD*** internal processing uses ***Protobuf***, so the protocol
  format recommends using ***Protobuf***, to reduce ***Json***
  conversion overhead.
- The ***nProtoFmtType*** field specifies the data type of the package
  body, and the corresponding protocol type will be returned when the
  package is returned. The data type of the push protocol is specified
  by the ***OpenD*** configuration file
- ***arrBodySHA1*** is used to verify the consistency of the requested
  data before and after network transmission, and must be filled in
  correctly
- The binary stream of the protocol header uses little-endian byte
  order, that is, generally there is no need to use ***ntohl*** and
  other related functions to convert the data



### <a href="#8928" class="header-anchor">#</a> Protocol Body

#### <a href="#2656" class="header-anchor">#</a> Packet Body Structure of Protobuf Request



``` text
message C2S
{
    required int64 req = 1;
}

message Request
{
    required C2S c2s = 1;
}
```





#### <a href="#4592" class="header-anchor">#</a> Packet Body Structure of Protobuf Response



``` text
message S2C
{
    required int64 data = 1;
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, result of return
    optional string retMsg = 2;
    optional int32 errCode = 3;
    optional S2C s2c = 4;
}
```





| Field | Description |
|:---|:---|
| c2s | Request parameter structure |
| req | Request parameters, actually defined according to the protocol |
| retType | Request result |
| retMsg | The reason for the failed request |
| errCode | The corresponding error code for failed request |
| s2c | Response data structure, some protocols do not return data if there is no such field |
| data | Response data, actually defined according to the protocol |



Tips

- The package body format type request package is specified by
  ***nProtoFmtType*** field from protocol header, and the ***OpenD***
  initiative push format is set in
  [InitConnect](/moomoo-api-doc/en/ftapi/init.html#6650).
- The original protocol file format is defined in ***Protobuf*** format.
  If you need ***json*** format transmission, it is recommended to use
  the ***protobuf3*** interface to directly convert to ***json***.
- The enumeration value field definition uses signed integer, and the
  comment indicates the corresponding enumeration. The enumeration is
  generally defined in ***Common.proto, Qot_Common.proto,
  Trd_Common.proto*** files.
- The price, percentage and other data in the protocol are transmitted
  in floating point type. Direct use will cause accuracy problems. It
  needs to be rounded according to the accuracy (if not specified in the
  protocol, the default is 3 decimal places) before use.



## <a href="#7390" class="header-anchor">#</a> Heartbeat Keep Alive







``` protobuf
syntax = "proto2";
package KeepAlive;
option java_package = "com.futu.openapi.pb";
option go_package = "github.com/futuopen/ftapi4go/pb/keepalive";

import "Common.proto";

message C2S
{
    required int64 time = 1; //Greenwich timestamp when the client sends the packet, in seconds
}

message S2C
{
    required int64 time = 1; //Greenwich timestamp when the server returned the packet, in seconds
}

message Request
{
    required C2S c2s = 1;
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```











``` protobuf
syntax = "proto2";
package KeepAlive;
option java_package = "com.moomoo.openapi.pb";
option go_package = "github.com/moomooopen/mmapi4go/pb/keepalive";

import "Common.proto";

message C2S
{
    required int64 time = 1; //Greenwich timestamp when the client sends the packet, in seconds
}

message S2C
{
    required int64 time = 1; //Greenwich timestamp when the server returned the packet, in seconds
}

message Request
{
    required C2S c2s = 1;
}

message Response
{
    required int32 retType = 1 [default = -400]; //RetType, return result
    optional string retMsg = 2;
    optional int32 errCode = 3;
    
    optional S2C s2c = 4;
}
```









- **Introduction**

  Heartbeat keep alive

- **Protocol ID**

  1004

- **Introduction**

  According to the heartbeat keeping alive interval returned by the
  [initialization protocol](/moomoo-api-doc/en/ftapi/init.html#7571),
  send the heartbeeat keep alive protocol to OpenD.

## <a href="#4573" class="header-anchor">#</a> Encrypted Communication Process

- If OpenD is configured with encryption,
  [InitConnect](/moomoo-api-doc/en/quote/base.html) must use
  [RSA](/moomoo-api-doc/en/qa/other.html#1479) public key encryption to
  initialize the connection protocol, and other subsequent protocols use
  the random key returned by InitConnect for AES encrypted
  communication.
- The encryption process of OpenD draws on the SSL protocol. Considering
  that services and applications are generally deployed locally, we
  simplifies the related processes. OpenD shares the same
  [RSA](/moomoo-api-doc/en/qa/other.html#1479) private key file with the
  access Client. Please save and distribute the private key file
  properly.
- Go to this
  <a href="http://web.chacuo.net/netrsakeypair" target="_blank"
  rel="noopener noreferrer">URL</a> to generate a random
  [RSA](/moomoo-api-doc/en/qa/other.html#1479) key pair online. The key
  format must be PCKS#1, the key length can be 512, 1024, and do not set
  password. Copy and save the generated private key to a file, and then
  configure the path of the private key file to the **rsa_private_key**
  configuration item agreed upon in [OpenD
  Configuration](/moomoo-api-doc/en/opend/opend-cmd.html#149).
- **It is recommended that users who have real trade configure
  encryption to avoid leakage of account and trade information.**





![encrypt](/moomoo-api-doc/assets/img/encrypt.9d680476.png)





![encrypt](/moomoo-api-doc/assets/img/mmencrypt.71115b21.png)





## <a href="#9579" class="header-anchor">#</a> RSA Encryption and Decryption

- [OpenD configuration](/moomoo-api-doc/en/opend/opend-cmd.html#149)
  Convention **rsa_private_key** is the path of the private key file
- OpenD shares the same private key file with the access client
- RSA encryption and decryption is only used for InitConnect requests,
  and is used to securely obtain symmetric encryption key of other
  request protocols
- The [RSA](/moomoo-api-doc/en/qa/other.html#1479) key of OpenD is
  1024-bit, the filling method is PKCS1, public key encryption, private
  key decryption, public key can be generated by private key

### <a href="#8526" class="header-anchor">#</a> Send Data Encryption

- RSA encryption rules: If the number of key bits is key_size, the
  maximum length of a single encryption string is (key_size)/8-11. The
  current number of bits is 1024, and the length of one encryption can
  be set to 100.
- Divide the plaintext data into one or several segments of up to 100
  bytes for encryption, and the final encrypted data is spliced by all
  segmented encrypted data.

### <a href="#3436" class="header-anchor">#</a> Receive Data Decryption

- RSA decryption also follows the segmentation rule. For a 1024-bit key,
  the length of each segment to be decrypted is 128-byte.
- Divide the ciphertext data into one or several segments of up to 128
  bytes for decryption, and the final decrypted data is spliced by all
  segmented decrypted data.

## <a href="#7863" class="header-anchor">#</a> AES Encryption and Decryption

- The encryption key is returned by the InitConnect protocol
- The ecb encryption mode of AES is used by default.

### <a href="#8526-2" class="header-anchor">#</a> Send Data Encryption

- AES encryption requires that the length of the source data must be an
  integer multiple of 16, so it needs to be aligned with ‘0’ before
  encryption. Record mod_len for source data length and 16 module.
- Because it is possible to modify the source data before encryption, it
  is necessary to add a 16-byte padding data block at the end of the
  encrypted data. The last byte is assigned mod_len, and the remaining
  bytes are assigned the value '0'. The encrypted data and additional
  populated data blocks are spliced as the body data to be sent in the
  end.

### <a href="#3436-2" class="header-anchor">#</a> Receive Data Decryption

- For protocol body data, first take out the last byte and record it as
  mod_len, then truncate the body to the 16-byte padding data block
  before decrypting it (corresponding to the encrypted padding extra
  data block logic).
- When mod_len is 0, the above decrypted data is the body data returned
  by the protocol, otherwise the tail (16-mod_len) length of the data
  used for filling and alignment needs to be truncated.

![aes](/moomoo-api-doc/assets/img/aes.729f06b1.png)







