



# <a href="#6680" class="header-anchor">#</a> Program Samples









- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#2039" class="header-anchor">#</a> Python Example

### <a href="#2577" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#6763" class="header-anchor">#</a> Step 2: Download Python API

- Method 1: Use pip install in cmd.

  - Initial installation: Windows: `$ pip install futu-api`, Linux/Mac
    `$ pip3 install futu-api`.
  - Secondary upgrade: Windows:
    `$ pip install futu-api --upgrade`，Linux/Mac
    `$ pip3 install futu-api --upgrade`.

- Method 2: Click to download latest version of <a
  href="https://www.futunn.com/download/fetch-lasted-link?name=openapi-python"
  target="_blank" rel="noopener noreferrer">Python API</a>.

### <a href="#9364" class="header-anchor">#</a> Step 3: Create New Project

Open PyCharm and click 'New Project' from 'Welcome to PyCharm' window.
If you have already created a project, you can open the project
directly.

![demo-newproject](/moomoo-api-doc/assets/img/demo-newproject.2fb2c25b.png)

### <a href="#14" class="header-anchor">#</a> Step 4: Create new file

Create new Python file under the project, and copy the sample code below
to that file. The sample code includes viewing the market snapshot and
placing an order through paper trading account.



``` python
from futu import *

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # Create quote object
print(quote_ctx.get_market_snapshot('HK.00700'))  # Get market snapshot for HK.00700
quote_ctx.close() # Close object to prevent the number of connextions from running out


trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)  # Create trade object
print(trd_ctx.place_order(price=500.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE))  # Placing an order through paper trading account (It is nessary to unlock trade by trading password for placing orders in the real environment.)

trd_ctx.close()  # Close object to prevent the number of connextions from running out
```





### <a href="#592" class="header-anchor">#</a> Step 5: Running file

Run the project, and you can see the returned message of a successful
run as follows:



``` text
2020-11-05 17:09:29,705 [open_context_base.py] _socket_reconnect_and_wait_ready:255: Start connecting: host=127.0.0.1; port=11111;
2020-11-05 17:09:29,705 [open_context_base.py] on_connected:344: Connected : conn_id=1; 
2020-11-05 17:09:29,706 [open_context_base.py] _handle_init_connect:445: InitConnect ok: conn_id=1; info={'server_version': 218, 'login_user_id': 7157878, 'conn_id': 6730043337026687703, 'conn_key': '3F17CF3EEF912C92', 'conn_iv': 'C119DDDD6314F18A', 'keep_alive_interval': 10, 'is_encrypt': False};
(0,        code          update_time  last_price  open_price  high_price  ...  after_high_price  after_low_price  after_change_val  after_change_rate  after_amplitude
0  HK.00700  2020-11-05 16:08:06       625.0       610.0       625.0  ...               N/A              N/A               N/A                N/A              N/A

[1 rows x 132 columns])
2020-11-05 17:09:29,739 [open_context_base.py] _socket_reconnect_and_wait_ready:255: Start connecting: host=127.0.0.1; port=11111;
2020-11-05 17:09:29,739 [network_manager.py] work:366: Close: conn_id=1
2020-11-05 17:09:29,739 [open_context_base.py] on_connected:344: Connected : conn_id=2; 
2020-11-05 17:09:29,740 [open_context_base.py] _handle_init_connect:445: InitConnect ok: conn_id=2; info={'server_version': 218, 'login_user_id': 7157878, 'conn_id': 6730043337169705045, 'conn_key': 'A624CF3EEF91703C', 'conn_iv': 'BF1FF3806414617B', 'keep_alive_interval': 10, 'is_encrypt': False};
(0,        code stock_name trd_side order_type order_status  ... dealt_avg_price  last_err_msg  remark time_in_force fill_outside_rth
0  HK.00700       腾讯控股      BUY     NORMAL   SUBMITTING  ...             0.0                                 DAY              N/A

[1 rows x 16 columns])
2020-11-05 17:09:32,843 [network_manager.py] work:366: Close: conn_id=2
(0,        code stock_name trd_side      order_type order_status  ... dealt_avg_price  last_err_msg  remark time_in_force fill_outside_rth
0  HK.00700       腾讯控股      BUY  ABSOLUTE_LIMIT    SUBMITTED  ...             0.0                                 DAY              N/A

[1 rows x 16 columns])
```









Click to download latest version of <a
href="https://www.futunn.com/download/fetch-lasted-link?name=openapi-protobuf"
target="_blank" rel="noopener noreferrer">Protobuf API</a>.





## <a href="#8982" class="header-anchor">#</a> C# Example

### <a href="#2577-2" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#7193" class="header-anchor">#</a> Step 2: Download C# API

We provide two methods to download C# API, you can choose one of them.

- Method 1: Use nuget install in cmd `$ dotnet add package futu-api`
  (nuget only supports downloading C# API source code. For more samples,
  please refer to Method 2).

- Method 2: Click to download latest version of <a
  href="https://www.futunn.com/download/fetch-lasted-link?name=openapi-csharp"
  target="_blank" rel="noopener noreferrer">C# API</a>. The source code and samples for C# API
  are in the `/FTAPI4NET` folder. For directory structure, please refer
  to [FTAPI4NET Directory](/moomoo-api-doc/en/quick/demo.html#3557).

#### <a href="#3557" class="header-anchor">#</a> FTAPI4NET Directory



``` text
+---FTAPI4Net                                          Source code for FTAPI4NET. If the .NET version you are using is not compatible, you can recompile FTAPI4Net.dll with source code
+---lib
    +---net4.5                                         Dependent livraries under .NET 4.5
    |       FTAPI4Net.dll                              C# version for OpenAPI
    |       Google.ProtocolBuffers.dll                 Third-party library used for parsing protobuf data
    |       Google.ProtocolBuffers.Serialization.dll   Third-party library used for parsing protobuf data
    |
    +---netcore2.1                                     Dependent livraries under .NET 4.5
    |       FTAPI4Net.dll                              C# version for OpenAPI
    |       Google.ProtocolBuffers.dll                 Third-party library used for parsing protobuf data
    |       Google.ProtocolBuffers.Serialization.dll   Third-party library used for parsing protobuf data
    |
    FTAPIChannel                                       C dynamic licrary depended by FTAPI4NET, used for API to communicate with OpenD and is stored in directories named by each operating system. Before running the .NET program, you need to copy the dynamic libraries under the corresponding platform to the current directory where the program is running.
+---Sample                                             Sample project
+---tools                                              A third-party tool for converting the protobuf into C# code, as described in the readme.md in this directory
```





### <a href="#181" class="header-anchor">#</a> Step 3: Import the sample project

Open Vusual Studio development evnironment, import the project file
*FTAPI4NetCore.sln* in the directory.

### <a href="#8775" class="header-anchor">#</a> Step 4: Run

1.  Check whether the interface configuration used in the sample program
    is consistent with the configuration of OpenD.

2.  Check the functions that need to be run in the Main function in the
    Program.cs file under the Sample project. After running, you can see
    the following message printed:



``` text
InitConnected
Send QotGetUserSecurity: 3
{"staticInfoList":[{"basic":{"security":{"market":1,"code":"08311"},"id":69179038244983,"lotSize":10000,"secType":3,"name":"\u5706\u7f8e\u5149\u7535","listTime":"2014-02-07","delisting":false,"listTimestamp":1391702400}},{"basic":{"security":{"market":1,"code":"02127"},"id":79925046413391,"lotSize":2000,"secType":3,"name":"\u6c47\u68ee\u5bb6\u5c45","listTime":"2020-12-
29","delisting":false,"listTimestamp":1609171200}},{"basic":{"security":{"market":1,"code":"EVG2101"},"id":71002729,"lotSize":2000,"secType":10,"name":"\u4e2d\u56fd\u6052\u5927\u96c6\u56e22101","listTime":"","delisting":false},"futureExData":{"lastTradeTime":"2021-01-28","lastTradeTimestamp":1611820800,"isMainContract":false}},{"basic":{"security":{"market":1,"code":"0
2333"},"id":53257594472733,"lotSize":500,"secType":3,"name":"\u957f\u57ce\u6c7d\u8f66","listTime":"2003-12-15","delisting":false,"listTimestamp":1071417600}},{"basic":{"security":{"market":1,"code":"06993"},"id":79882096745297,"lotSize":500,"secType":3,"name":"\u84dd\u6708\u4eae\u96c6\u56e2","listTime":"2020-12-16","delisting":false,"listTimestamp":1608048000}},{"basic
":{"security":{"market":1,"code":"01810"},"id":76033806042898,"lotSize":200,"secType":3,"name":"\u5c0f\u7c73\u96c6\u56e2-W","listTime":"2018-07-09","delisting":false,"listTimestamp":1531065600}},{"basic":{"security":{"market":1,"code":"09992"},"id":79869211846408,"lotSize":200,"secType":3,"name":"\u6ce1\u6ce1\u739b\u7279","listTime":"2020-12-11","delisting":false,"list
Timestamp":1607616000}},{"basic":{"security":{"market":1,"code":"03948"},"id":66709432045420,"lotSize":100,"secType":3,"name":"\u4f0a\u6cf0\u7164\u70ad","listTime":"2012-07-12","delisting":false,"listTimestamp":1342022400}},{"basic":{"security":{"market":1,"code":"01398"},"id":57754425230710,"lotSize":1000,"secType":3,"name":"\u5de5\u5546\u94f6\u884c","listTime":"2006-
10-27","delisting":false,"listTimestamp":1161878400}},{"basic":{"security":{"market":1,"code":"06618"},"id":79843442039258,"lotSize":50,"secType":3,"name":"\u4eac\u4e1c\u5065\u5eb7","listTime":"2020-12-08","delisting":false,"listTimestamp":1607356800}},{"basic":{"security":{"market":1,"code":"09698"},"id":79693118186978,"lotSize":100,"secType":3,"name":"\u4e07\u56fd\u6
570\u636e-SW","listTime":"2020-11-02","delisting":false,"listTimestamp":1604246400}},{"basic":{"security":{"market":1,"code":"03690"},"id":76364518526570,"lotSize":100,"secType":3,"name":"\u7f8e\u56e2-W","listTime":"2018-09-20","delisting":false,"listTimestamp":1537372800}},{"basic":{"security":{"market":1,"code":"09988"},"id":78224239372036,"lotSize":100,"secType":3,"
name":"\u963f\u91cc\u5df4\u5df4-SW","listTime":"2019-11-26","delisting":false,"listTimestamp":1574697600}},{"basic":{"security":{"market":1,"code":"800000"},"id":800000,"lotSize":0,"secType":6,"name":"\u6052\u751f\u6307\u6570","listTime":"1970-01-01","delisting":false,"listTimestamp":0}},{"basic":{"security":{"market":1,"code":"00005"},"id":5,"lotSize":400,"secType":3,
"name":"\u6c47\u4e30\u63a7\u80a1","listTime":"1970-01-01","delisting":false,"listTimestamp":0}},{"basic":{"security":{"market":1,"code":"00175"},"id":4930622455983,"lotSize":1000,"secType":3,"name":"\u5409\u5229\u6c7d\u8f66","listTime":"1973-02-23","delisting":false,"listTimestamp":99244800}},{"basic":{"security":{"market":1,"code":"09677"},"id":79598628906445,"lotSize
":1000,"secType":3,"name":"\u5a01\u6d77\u94f6\u884c","listTime":"2020-10-12","delisting":false,"listTimestamp":1602432000}},{"basic":{"security":{"market":1,"code":"06055"},"id":77494094927783,"lotSize":1000,"secType":3,"name":"\u4e2d\u70df\u9999\u6e2f","listTime":"2019-06-12","delisting":false,"listTimestamp":1560268800}},{"basic":{"security":{"market":1,"code":"00788
"},"id":76175539962644,"lotSize":2000,"secType":3,"name":"\u4e2d\u56fd\u94c1\u5854","listTime":"2018-08-08","delisting":false,"listTimestamp":1533657600}},{"basic":{"security":{"market":1,"code":"02318"},"id":54082228193550,"lotSize":500,"secType":3,"name":"\u4e2d\u56fd\u5e73\u5b89","listTime":"2004-06-24","delisting":false,"listTimestamp":1088006400}},{"basic":{"secur
ity":{"market":1,"code":"BK1011"},"id":10001011,"lotSize":0,"secType":7,"name":"\u5316\u80a5\u53ca\u519c\u7528\u5316\u5408\u7269","listTime":"1970-01-01","delisting":false,"listTimestamp":0}},{"basic":{"security":{"market":1,"code":"BK1095"},"id":10001095,"lotSize":0,"secType":7,"name":"\u697c\u5b87\u5efa\u9020","listTime":"1970-01-01","delisting":false,"listTimestamp"
:0}},{"basic":{"security":{"market":1,"code":"01328"},"id":59274843653424,"lotSize":10000,"secType":3,"name":"\u91d1\u6d8c\u6295\u8d44","listTime":"2007-10-16","delisting":false,"listTimestamp":1192464000}},{"basic":{"security":{"market":1,"code":"00900"},"id":40312563041156,"lotSize":2000,"secType":3,"name":"AEON\u4fe1\u8d37","listTime":"1995-09-14","delisting":false,
"listTimestamp":811008000}},{"basic":{"security":{"market":1,"code":"00030"},"id":34144990003230,"lotSize":2000,"secType":3,"name":"\u4e07\u9686\u63a7\u80a1\u96c6\u56e2","listTime":"1991-10-09","delisting":false,"listTimestamp":686937600}},{"basic":{"security":{"market":1,"code":"00028"},"id":26989574488092,"lotSize":1000,"secType":3,"name":"\u5929\u5b89","listTime":"1
987-03-18","delisting":false,"listTimestamp":542995200}},{"basic":{"security":{"market":1,"code":"00519"},"id":25447681229319,"lotSize":5000,"secType":3,"name":"\u5b9e\u529b\u5efa\u4e1a","listTime":"1986-03-24","delisting":false,"listTimestamp":511977600}},{"basic":{"security":{"market":1,"code":"00276"},"id":4140348473620,"lotSize":3000,"secType":3,"name":"\u8499\u53e
4\u80fd\u6e90","listTime":"1972-08-23","delisting":false,"listTimestamp":83347200}},{"basic":{"security":{"market":1,"code":"06862"},"id":76385993366222,"lotSize":1000,"secType":3,"name":"\u6d77\u5e95\u635e","listTime":"2018-09-26","delisting":false,"listTimestamp":1537891200}},{"basic":{"security":{"market":1,"code":"00451"},"id":34866544509379,"lotSize":2000,"secType
":3,"name":"\u534f\u946b\u65b0\u80fd\u6e90","listTime":"1992-03-25","delisting":false,"listTimestamp":701452800}},{"basic":{"security":{"market":1,"code":"02899"},"id":53291954211667,"lotSize":2000,"secType":3,"name":"\u7d2b\u91d1\u77ff\u4e1a","listTime":"2003-12-23","delisting":false,"listTimestamp":1072108800}},{"basic":{"security":{"market":1,"code":"08133"},"id":71
098888626117,"lotSize":20000,"secType":3,"name":"\u94f8\u80fd\u63a7\u80a1","listTime":"2015-04-30","delisting":false,"listTimestamp":1430323200}},{"basic":{"security":{"market":1,"code":"01432"},"id":69857643070872,"lotSize":1000,"secType":3,"name":"\u4e2d\u56fd\u5723\u7267","listTime":"2014-07-15","delisting":false,"listTimestamp":1405353600}},{"basic":{"security":{"m
arket":1,"code":"09933"},"id":78426102834893,"lotSize":4000,"secType":3,"name":"GHW INTL","listTime":"2020-01-21","delisting":false,"listTimestamp":1579536000}},{"basic":{"security":{"market":1,"code":"07500"},"id":77494094929228,"lotSize":100,"secType":4,"name":"\u5357\u65b9\u4e24\u500d\u770b\u7a7a\u6052\u6307","listTime":"2019-05-28","delisting":false,"listTimestamp"
:1558972800}},{"basic":{"security":{"market":1,"code":"00981"},"id":53661321397205,"lotSize":500,"secType":3,"name":"\u4e2d\u82af\u56fd\u9645","listTime":"2004-03-18","delisting":false,"listTimestamp":1079539200}}]}
```







Tips

- If the FTAPIChannel dynamic library file cannot be found, you need to
  copy the *FTAPIChannel* file of the corresponding platform in the
  `/lib` folder, to the directory in which the program is running.







## <a href="#6540" class="header-anchor">#</a> Java Example

### <a href="#2577-3" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#3647" class="header-anchor">#</a> Step 2: Download Java API

We provide two methods to download Java API, you can choose one of them.

#### <a href="#5062" class="header-anchor">#</a> Method 1: Configure Java API via maven repository.

1.  Select the latest version of futu-api in
    <a href="https://search.maven.org/artifact/com.futunn.openapi/futu-api"
    target="_blank" rel="noopener noreferrer">maven</a> and click to enter.
2.  Copy the relevant dependency on the right side of the webpage, and
    add it to your project settings.  
    Example: Users who use Apache Maven to manage their projects can
    copy the code in the red box below into your project settings.  
    ![maven](/moomoo-api-doc/assets/img/maven.75366f6c.png)

#### <a href="#114" class="header-anchor">#</a> Method 2: Download Java API.

1.  Click to download latest version of <a
    href="https://www.futunn.com/download/fetch-lasted-link?name=openapi-java"
    target="_blank" rel="noopener noreferrer">Java API</a>.
2.  Decompress the downloaded file. `/FTAPI4J` is the directory of Java
    API. For directory structure, please refer to [FTAPI4J
    Directory](/moomoo-api-doc/en/quick/demo.html#3216). Add
    `/lib/futu-api-.x.y.z.jar` file to your project settings.

##### <a href="#3216" class="header-anchor">#</a> FTAPI4J Directory



``` text
+---ftapi4j                      FTAPI4J source code. If the JDK version used is not compatible, you can use the project to recompile the ftapi.jar.
+---lib                          The folder with common libraries
|    futu-api-x.y.z.jar          Java version of Futu API
|    bcprov-jdk15on-1.68.jar     Third-party library, for encryption and decryption
|    bcpkix-jdk15on-1.68.jar     Third-party library, for encryption and decryption
|    protobuf-java-3.5.1.jar     Third-party library, for parsing protobuf data
+---sample                       Sample project
+---resources                    The default generated directory of the maven project
```





### <a href="#1983" class="header-anchor">#</a> Step 3: Establish a futu-api java project

Take the IntelliJ IDEA as an example.

1.  Create a new project.  
    ![new_java](/moomoo-api-doc/assets/img/new_java.8a9550c5.png)

2.  Choose Maven.  
    ![maven_proj](/moomoo-api-doc/assets/img/maven_proj.68228f60.png)

3.  Designate a loction for the project.  
    ![loc_java](/moomoo-api-doc/assets/img/loc_java.c1a313eb.png)

4.  Biuld tools for maven. This example used IDEA's own tools
    directory.  
    ![tool_java](/moomoo-api-doc/assets/img/tool_java.641bfef3.png)

5.  Finish it and wait for the project initialization. If nothing gose
    wrong, you will see the words 'BUILD SUCCESS' below.  
    ![suc_java](/moomoo-api-doc/assets/img/suc_java.04e106fd.png)

6.  Configure the futu-api.

- If you configure Java API via the mave repository, please follow the
  instructions:  
  Edit the pom.xml file directly and insert the futu-api dependency in
  dependencies (x.y.z should be replaced with the version number).  
  ![maven_futu](/moomoo-api-doc/assets/img/maven_futu.12353f70.png)

- If you download Java API via official website, please follow the
  instructions:  
  Create a '/lib/' directory under the project. Copy the
  '/FTAPI4J/lib/futu-api-x.y.x.jar' file under '/lib/' (e.g. The
  futu-api-5.4.1607.jar file shown below).  
  Edit the pom.xml file, and insert the futu-api dependency in
  dependencies.  
  ![maven_api](/moomoo-api-doc/assets/img/maven_api.e3682d1f.png)

### <a href="#7582" class="header-anchor">#</a> Step 4: Import the sample project

The example provides a maven compilation script. The project under
directory `/sample` can be imported by IDE that supports maven.

### <a href="#1129" class="header-anchor">#</a> Step 5: Run

1.  Check whether the interface configuration of main.java is consistent
    with the configuration of OpenD.

2.  Run the *main.java* file in the `/sample` directory, and you can see
    that the returned message for successful running as follows:



``` text
Qot onInitConnect: ret=true desc=Succeed! connID=6750011030360491012
onReply_GetMarketState: retType: 0
retMsg: ""
errCode: 0
s2c {
  marketInfoList {
    security {
      market: 1
      code: "00700"
    }
    name: "\350\205\276\350\256\257\346\216\247\350\202\241"
    marketState: 6
  }
}
```







Tips

- If the FTAPIChannel dynamic library file cannot be found, you need to
  copy the *FTAPIChannel* file of the corresponding platform in the
  `/lib` folder, to the directory in which the program is running.







## <a href="#4196" class="header-anchor">#</a> C++ Example

### <a href="#2577-4" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#7643" class="header-anchor">#</a> Step 2: Download C++ API

Click to download latest version of <a
href="https://www.futunn.com/download/fetch-lasted-link?name=openapi-cpp"
target="_blank" rel="noopener noreferrer">C++ API</a>.

Decompress the downloaded file, the source code and samples for C++ API
are in the `/FTAPI4CPP` folder. For directory structure, please refer to
[FTAPI4CPP Directory](/moomoo-api-doc/en/quick/demo.html#3420).

#### <a href="#3420" class="header-anchor">#</a> FTAPI4CPP Directory



``` text
+---Bin                  Store the common library files compiled by the default compilation environment of various systems
+---Include              Directory store public header files, and .h/.cc files created by protobuf
+---Sample               Sample project
+---Src                  Source code
    +---FTAPI            FTAPI source code
    +---protobuf         Protobuf source code
```





### <a href="#181-2" class="header-anchor">#</a> Step 3: Import the sample project

The example provides project file for *Visual Studio* and *XCode*. You
can import sample projects using the *Visual Studio* or *XCode*
development environment.

### <a href="#8775-2" class="header-anchor">#</a> Step 4: Run

1.  Check whether the interface configuration of file simpleSample.cpp
    is consistent with the configuration of OpenD.

2.  You can see that the returned message for successful running as
    follows:



``` text
Run GetSecuritySnapshotDemo
InitQot, suc = 1
GetHKEqtySecList, count = 2698
GetSecuritySnapshot, i = 0
GetSecuritySnapshot, i = 1
GetSecuritySnapshot, i = 2
GetSecuritySnapshot, i = 3
GetSecuritySnapshot, i = 4
GetSecuritySnapshot, i = 5
GetSecuritySnapshot, i = 6
GetSecuritySnapshot, i = 7
GetSecuritySnapshot, i = 8
GetSecuritySnapshot, i = 9
GetSecuritySnapshot, i = 10
GetSecuritySnapshot, i = 11
GetSecuritySnapshot, i = 12
GetSecuritySnapshot, i = 13
ParseHKEqtySecQot, first = (HK.00001, 56.65)
GetSecuritySnapshotDemo End
```





















- Python
- Proto
- C#
- Java
- C++
- JavaScript





## <a href="#2039-2" class="header-anchor">#</a> Python Example

### <a href="#2577-5" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#6763-2" class="header-anchor">#</a> Step 2: Download Python API

- Method 1: Use pip install in cmd.

  - Initial installation: Windows: `$ pip install moomoo-api`, Linux/Mac
    `$ pip3 install moomoo-api`.
  - Secondary upgrade: Windows:
    `$ pip install moomoo-api --upgrade`，Linux/Mac
    `$ pip3 install moomoo-api --upgrade`.

- Method 2: Download latest version of Python API from
  <a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
  rel="noopener noreferrer">moomoo official website</a>.

### <a href="#9364-2" class="header-anchor">#</a> Step 3: Create New Project

Open PyCharm and click 'New Project' from 'Welcome to PyCharm' window.
If you have already created a project, you can open the project
directly.

![demo-newproject](/moomoo-api-doc/assets/img/demo-newproject.2fb2c25b.png)

### <a href="#14-2" class="header-anchor">#</a> Step 4: Create new file

Create new Python file under the project, and copy the sample code below
to that file. The sample code includes viewing the market snapshot and
placing an order through paper trading account.



``` python
from moomoo import *

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)  # Create quote object
print(quote_ctx.get_market_snapshot('HK.00700'))  # Get market snapshot for HK.00700
quote_ctx.close() # Close object to prevent the number of connextions from running out


trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)  # Create trade object
print(trd_ctx.place_order(price=500.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE))  # Placing an order through paper trading account (It is nessary to unlock trade by trading password for placing orders in the real environment.)

trd_ctx.close()  # Close object to prevent the number of connextions from running out
```





### <a href="#592-2" class="header-anchor">#</a> Step 5: Running file

Run the project, and you can see the returned message of a successful
run as follows:



``` text
2020-11-05 17:09:29,705 [open_context_base.py] _socket_reconnect_and_wait_ready:255: Start connecting: host=127.0.0.1; port=11111;
2020-11-05 17:09:29,705 [open_context_base.py] on_connected:344: Connected : conn_id=1; 
2020-11-05 17:09:29,706 [open_context_base.py] _handle_init_connect:445: InitConnect ok: conn_id=1; info={'server_version': 218, 'login_user_id': 7157878, 'conn_id': 6730043337026687703, 'conn_key': '3F17CF3EEF912C92', 'conn_iv': 'C119DDDD6314F18A', 'keep_alive_interval': 10, 'is_encrypt': False};
(0,        code          update_time  last_price  open_price  high_price  ...  after_high_price  after_low_price  after_change_val  after_change_rate  after_amplitude
0  HK.00700  2020-11-05 16:08:06       625.0       610.0       625.0  ...               N/A              N/A               N/A                N/A              N/A

[1 rows x 132 columns])
2020-11-05 17:09:29,739 [open_context_base.py] _socket_reconnect_and_wait_ready:255: Start connecting: host=127.0.0.1; port=11111;
2020-11-05 17:09:29,739 [network_manager.py] work:366: Close: conn_id=1
2020-11-05 17:09:29,739 [open_context_base.py] on_connected:344: Connected : conn_id=2; 
2020-11-05 17:09:29,740 [open_context_base.py] _handle_init_connect:445: InitConnect ok: conn_id=2; info={'server_version': 218, 'login_user_id': 7157878, 'conn_id': 6730043337169705045, 'conn_key': 'A624CF3EEF91703C', 'conn_iv': 'BF1FF3806414617B', 'keep_alive_interval': 10, 'is_encrypt': False};
(0,        code stock_name trd_side order_type order_status  ... dealt_avg_price  last_err_msg  remark time_in_force fill_outside_rth
0  HK.00700       腾讯控股      BUY     NORMAL   SUBMITTING  ...             0.0                                 DAY              N/A

[1 rows x 16 columns])
2020-11-05 17:09:32,843 [network_manager.py] work:366: Close: conn_id=2
(0,        code stock_name trd_side      order_type order_status  ... dealt_avg_price  last_err_msg  remark time_in_force fill_outside_rth
0  HK.00700       腾讯控股      BUY  ABSOLUTE_LIMIT    SUBMITTED  ...             0.0                                 DAY              N/A

[1 rows x 16 columns])
```









Download and decompress latest version of Protobuf API from
<a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
rel="noopener noreferrer">moomoo official website</a>.





### <a href="#2577-6" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#7193-2" class="header-anchor">#</a> Step 2: Download C# API

We provide two methods to download C# API, you can choose one of them.

- Method 1: Use nuget install in cmd `$ dotnet add package moomoo-api`
  (nuget only supports downloading C# API source code. For more samples,
  please refer to Method 2).

- Method 2: Download and decompress latest version of C# API from
  <a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
  rel="noopener noreferrer">moomoo official website</a>. The source code and samples for C# API
  are in the `/MMAPI4NET` folder. For directory structure, please refer
  to [MMAPI4NET Directory](/moomoo-api-doc/en/quick/demo.html#3557).

#### <a href="#9501" class="header-anchor">#</a> MMAPI4NET Directory



``` text
+---MMAPI4Net                                          Source code for MMAPI4NET. If the .NET version you are using is not compatible, you can recompile MMAPI4Net.dll with source code
+---lib
    +---net4.5                                         Dependent livraries under .NET 4.5
    |       MMAPI4Net.dll                              C# version for OpenAPI
    |       Google.ProtocolBuffers.dll                 Third-party library used for parsing protobuf data
    |       Google.ProtocolBuffers.Serialization.dll   Third-party library used for parsing protobuf data
    |
    +---netcore2.1                                     Dependent livraries under .NET 4.5
    |       MMAPI4Net.dll                              C# version for OpenAPI
    |       Google.ProtocolBuffers.dll                 Third-party library used for parsing protobuf data
    |       Google.ProtocolBuffers.Serialization.dll   Third-party library used for parsing protobuf data
    |
    MMAPIChannel                                       C dynamic licrary depended by MMAPI4NET, used for API to communicate with OpenD and is stored in directories named by each operating system. Before running the .NET program, you need to copy the dynamic libraries under the corresponding platform to the current directory where the program is running.
+---Sample                                             Sample project
+---tools                                              A third-party tool for converting the protobuf into C# code, as described in the readme.md in this directory
```





### <a href="#181-3" class="header-anchor">#</a> Step 3: Import the sample project

Open Vusual Studio development evnironment, import the project file
*MMAPI4NetCore.sln* in the directory.

### <a href="#8775-3" class="header-anchor">#</a> Step 4: Run

1.  Check whether the interface configuration used in the sample program
    is consistent with the configuration of OpenD.

2.  Check the functions that need to be run in the Main function in the
    Program.cs file under the Sample project. After running, you can see
    the following message printed:



``` text
InitConnected
Send QotGetUserSecurity: 3
{"staticInfoList":[{"basic":{"security":{"market":1,"code":"08311"},"id":69179038244983,"lotSize":10000,"secType":3,"name":"\u5706\u7f8e\u5149\u7535","listTime":"2014-02-07","delisting":false,"listTimestamp":1391702400}},{"basic":{"security":{"market":1,"code":"02127"},"id":79925046413391,"lotSize":2000,"secType":3,"name":"\u6c47\u68ee\u5bb6\u5c45","listTime":"2020-12-
29","delisting":false,"listTimestamp":1609171200}},{"basic":{"security":{"market":1,"code":"EVG2101"},"id":71002729,"lotSize":2000,"secType":10,"name":"\u4e2d\u56fd\u6052\u5927\u96c6\u56e22101","listTime":"","delisting":false},"futureExData":{"lastTradeTime":"2021-01-28","lastTradeTimestamp":1611820800,"isMainContract":false}},{"basic":{"security":{"market":1,"code":"0
2333"},"id":53257594472733,"lotSize":500,"secType":3,"name":"\u957f\u57ce\u6c7d\u8f66","listTime":"2003-12-15","delisting":false,"listTimestamp":1071417600}},{"basic":{"security":{"market":1,"code":"06993"},"id":79882096745297,"lotSize":500,"secType":3,"name":"\u84dd\u6708\u4eae\u96c6\u56e2","listTime":"2020-12-16","delisting":false,"listTimestamp":1608048000}},{"basic
":{"security":{"market":1,"code":"01810"},"id":76033806042898,"lotSize":200,"secType":3,"name":"\u5c0f\u7c73\u96c6\u56e2-W","listTime":"2018-07-09","delisting":false,"listTimestamp":1531065600}},{"basic":{"security":{"market":1,"code":"09992"},"id":79869211846408,"lotSize":200,"secType":3,"name":"\u6ce1\u6ce1\u739b\u7279","listTime":"2020-12-11","delisting":false,"list
Timestamp":1607616000}},{"basic":{"security":{"market":1,"code":"03948"},"id":66709432045420,"lotSize":100,"secType":3,"name":"\u4f0a\u6cf0\u7164\u70ad","listTime":"2012-07-12","delisting":false,"listTimestamp":1342022400}},{"basic":{"security":{"market":1,"code":"01398"},"id":57754425230710,"lotSize":1000,"secType":3,"name":"\u5de5\u5546\u94f6\u884c","listTime":"2006-
10-27","delisting":false,"listTimestamp":1161878400}},{"basic":{"security":{"market":1,"code":"06618"},"id":79843442039258,"lotSize":50,"secType":3,"name":"\u4eac\u4e1c\u5065\u5eb7","listTime":"2020-12-08","delisting":false,"listTimestamp":1607356800}},{"basic":{"security":{"market":1,"code":"09698"},"id":79693118186978,"lotSize":100,"secType":3,"name":"\u4e07\u56fd\u6
570\u636e-SW","listTime":"2020-11-02","delisting":false,"listTimestamp":1604246400}},{"basic":{"security":{"market":1,"code":"03690"},"id":76364518526570,"lotSize":100,"secType":3,"name":"\u7f8e\u56e2-W","listTime":"2018-09-20","delisting":false,"listTimestamp":1537372800}},{"basic":{"security":{"market":1,"code":"09988"},"id":78224239372036,"lotSize":100,"secType":3,"
name":"\u963f\u91cc\u5df4\u5df4-SW","listTime":"2019-11-26","delisting":false,"listTimestamp":1574697600}},{"basic":{"security":{"market":1,"code":"800000"},"id":800000,"lotSize":0,"secType":6,"name":"\u6052\u751f\u6307\u6570","listTime":"1970-01-01","delisting":false,"listTimestamp":0}},{"basic":{"security":{"market":1,"code":"00005"},"id":5,"lotSize":400,"secType":3,
"name":"\u6c47\u4e30\u63a7\u80a1","listTime":"1970-01-01","delisting":false,"listTimestamp":0}},{"basic":{"security":{"market":1,"code":"00175"},"id":4930622455983,"lotSize":1000,"secType":3,"name":"\u5409\u5229\u6c7d\u8f66","listTime":"1973-02-23","delisting":false,"listTimestamp":99244800}},{"basic":{"security":{"market":1,"code":"09677"},"id":79598628906445,"lotSize
":1000,"secType":3,"name":"\u5a01\u6d77\u94f6\u884c","listTime":"2020-10-12","delisting":false,"listTimestamp":1602432000}},{"basic":{"security":{"market":1,"code":"06055"},"id":77494094927783,"lotSize":1000,"secType":3,"name":"\u4e2d\u70df\u9999\u6e2f","listTime":"2019-06-12","delisting":false,"listTimestamp":1560268800}},{"basic":{"security":{"market":1,"code":"00788
"},"id":76175539962644,"lotSize":2000,"secType":3,"name":"\u4e2d\u56fd\u94c1\u5854","listTime":"2018-08-08","delisting":false,"listTimestamp":1533657600}},{"basic":{"security":{"market":1,"code":"02318"},"id":54082228193550,"lotSize":500,"secType":3,"name":"\u4e2d\u56fd\u5e73\u5b89","listTime":"2004-06-24","delisting":false,"listTimestamp":1088006400}},{"basic":{"secur
ity":{"market":1,"code":"BK1011"},"id":10001011,"lotSize":0,"secType":7,"name":"\u5316\u80a5\u53ca\u519c\u7528\u5316\u5408\u7269","listTime":"1970-01-01","delisting":false,"listTimestamp":0}},{"basic":{"security":{"market":1,"code":"BK1095"},"id":10001095,"lotSize":0,"secType":7,"name":"\u697c\u5b87\u5efa\u9020","listTime":"1970-01-01","delisting":false,"listTimestamp"
:0}},{"basic":{"security":{"market":1,"code":"01328"},"id":59274843653424,"lotSize":10000,"secType":3,"name":"\u91d1\u6d8c\u6295\u8d44","listTime":"2007-10-16","delisting":false,"listTimestamp":1192464000}},{"basic":{"security":{"market":1,"code":"00900"},"id":40312563041156,"lotSize":2000,"secType":3,"name":"AEON\u4fe1\u8d37","listTime":"1995-09-14","delisting":false,
"listTimestamp":811008000}},{"basic":{"security":{"market":1,"code":"00030"},"id":34144990003230,"lotSize":2000,"secType":3,"name":"\u4e07\u9686\u63a7\u80a1\u96c6\u56e2","listTime":"1991-10-09","delisting":false,"listTimestamp":686937600}},{"basic":{"security":{"market":1,"code":"00028"},"id":26989574488092,"lotSize":1000,"secType":3,"name":"\u5929\u5b89","listTime":"1
987-03-18","delisting":false,"listTimestamp":542995200}},{"basic":{"security":{"market":1,"code":"00519"},"id":25447681229319,"lotSize":5000,"secType":3,"name":"\u5b9e\u529b\u5efa\u4e1a","listTime":"1986-03-24","delisting":false,"listTimestamp":511977600}},{"basic":{"security":{"market":1,"code":"00276"},"id":4140348473620,"lotSize":3000,"secType":3,"name":"\u8499\u53e
4\u80fd\u6e90","listTime":"1972-08-23","delisting":false,"listTimestamp":83347200}},{"basic":{"security":{"market":1,"code":"06862"},"id":76385993366222,"lotSize":1000,"secType":3,"name":"\u6d77\u5e95\u635e","listTime":"2018-09-26","delisting":false,"listTimestamp":1537891200}},{"basic":{"security":{"market":1,"code":"00451"},"id":34866544509379,"lotSize":2000,"secType
":3,"name":"\u534f\u946b\u65b0\u80fd\u6e90","listTime":"1992-03-25","delisting":false,"listTimestamp":701452800}},{"basic":{"security":{"market":1,"code":"02899"},"id":53291954211667,"lotSize":2000,"secType":3,"name":"\u7d2b\u91d1\u77ff\u4e1a","listTime":"2003-12-23","delisting":false,"listTimestamp":1072108800}},{"basic":{"security":{"market":1,"code":"08133"},"id":71
098888626117,"lotSize":20000,"secType":3,"name":"\u94f8\u80fd\u63a7\u80a1","listTime":"2015-04-30","delisting":false,"listTimestamp":1430323200}},{"basic":{"security":{"market":1,"code":"01432"},"id":69857643070872,"lotSize":1000,"secType":3,"name":"\u4e2d\u56fd\u5723\u7267","listTime":"2014-07-15","delisting":false,"listTimestamp":1405353600}},{"basic":{"security":{"m
arket":1,"code":"09933"},"id":78426102834893,"lotSize":4000,"secType":3,"name":"GHW INTL","listTime":"2020-01-21","delisting":false,"listTimestamp":1579536000}},{"basic":{"security":{"market":1,"code":"07500"},"id":77494094929228,"lotSize":100,"secType":4,"name":"\u5357\u65b9\u4e24\u500d\u770b\u7a7a\u6052\u6307","listTime":"2019-05-28","delisting":false,"listTimestamp"
:1558972800}},{"basic":{"security":{"market":1,"code":"00981"},"id":53661321397205,"lotSize":500,"secType":3,"name":"\u4e2d\u82af\u56fd\u9645","listTime":"2004-03-18","delisting":false,"listTimestamp":1079539200}}]}
```







Tips

- If the MMAPIChannel dynamic library file cannot be found, you need to
  copy the *MMAPIChannel* file of the corresponding platform in the
  `/lib` folder, to the directory in which the program is running.







## <a href="#6540-2" class="header-anchor">#</a> Java Example

### <a href="#2577-7" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#3647-2" class="header-anchor">#</a> Step 2: Download Java API

We provide two methods to download Java API, you can choose one of them.

#### <a href="#5062-2" class="header-anchor">#</a> Method 1: Configure Java API via maven repository.

1.  Select the latest version of moomoo-api in
    <a href="https://search.maven.org/artifact/com.futunn.openapi/futu-api"
    target="_blank" rel="noopener noreferrer">maven</a> and click to enter.
2.  Copy the relevant dependency on the right side of the webpage, and
    add it to your project settings.  
    Example: Users who use Apache Maven to manage their projects can
    copy the code in the red box below into your project settings.  
    ![maven](/moomoo-api-doc/assets/img/mm-maven.95db9106.png)

#### <a href="#8127" class="header-anchor">#</a> Method 2: Download Java API via official website.

1.  Download latest version of Java API from
    <a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
    rel="noopener noreferrer">moomoo official website</a>.
2.  Decompress the downloaded file. `/MMAPI4J` is the directory of Java
    API. For directory structure, please refer to [MMAPI4J
    Directory](/moomoo-api-doc/en/quick/demo.html#3216). Add
    `/lib/moomoo-api-.x.y.z.jar` file to your project settings.

##### <a href="#5116" class="header-anchor">#</a> MMAPI4J Directory



``` text
+---mmapi4j                      MMAPI4J source code. If the JDK version used is not compatible, you can use the project to recompile the mmapi.jar.
+---lib                          The folder with common libraries
|    moomoo-api-x.y.z.jar          Java version of moomoo API
|    bcprov-jdk15on-1.68.jar     Third-party library, for encryption and decryption
|    bcpkix-jdk15on-1.68.jar     Third-party library, for encryption and decryption
|    protobuf-java-3.5.1.jar     Third-party library, for parsing protobuf data
+---sample                       Sample project
+---resources                    The default generated directory of the maven project
```





### <a href="#3556" class="header-anchor">#</a> Step 3: Establish a moomoo-api java project

Take the IntelliJ IDEA as an example.

1.  Create a new project.  
    ![new_java](/moomoo-api-doc/assets/img/mm-new_java.8a9550c5.png)

2.  Choose Maven.  
    ![maven_proj](/moomoo-api-doc/assets/img/maven_proj.68228f60.png)

3.  Designate a loction for the project.  
    ![loc_java](/moomoo-api-doc/assets/img/mm-loc_java.62455662.png)

4.  Biuld tools for maven. This example used IDEA's own tools
    directory.  
    ![tool_java](/moomoo-api-doc/assets/img/mm-tool_java.625eaea3.png)

5.  Finish it and wait for the project initialization. If nothing gose
    wrong, you will see the words 'BUILD SUCCESS' below.  
    ![suc_java](/moomoo-api-doc/assets/img/mm-suc_java.f851386d.png)

6.  Configure the moomoo-api.

- If you configure Java API via the mave repository, please follow the
  instructions:  
  Edit the pom.xml file directly and insert the moomoo-api dependency in
  dependencies (x.y.z should be replaced with the version number).  
  ![maven_futu](/moomoo-api-doc/assets/img/mm-maven_futu.f25e47e7.png)

- If you download Java API via official website, please follow the
  instructions:  
  Create a '/lib/' directory under the project. Copy the
  '/MMAPI4J/lib/moomoo-api-x.y.x.jar' file under '/lib/' (e.g. The
  moomoo-api-5.4.1607.jar file shown below).  
  Edit the pom.xml file, and insert the moomoo-api dependency in
  dependencies.  
  ![maven_api](/moomoo-api-doc/assets/img/mm-maven_api.2cffc3d9.png)

### <a href="#7582-2" class="header-anchor">#</a> Step 4: Import the sample project

The example provides a maven compilation script. The project under
directory `/sample` can be imported by IDE that supports maven.

### <a href="#1129-2" class="header-anchor">#</a> Step 5: Run

1.  Check whether the interface configuration of main.java is consistent
    with the configuration of OpenD.

2.  Run the *main.java* file in the `/sample` directory, and you can see
    that the returned message for successful running as follows:



``` text
Qot onInitConnect: ret=true desc=Succeed! connID=6750011030360491012
onReply_GetMarketState: retType: 0
retMsg: ""
errCode: 0
s2c {
  marketInfoList {
    security {
      market: 1
      code: "00700"
    }
    name: "\350\205\276\350\256\257\346\216\247\350\202\241"
    marketState: 6
  }
}
```







Tips

- If the MMAPIChannel dynamic library file cannot be found, you need to
  copy the *MMAPIChannel* file of the corresponding platform in the
  `/lib` folder, to the directory in which the program is running.







## <a href="#4196-2" class="header-anchor">#</a> C++ Example

### <a href="#2577-8" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#7643-2" class="header-anchor">#</a> Step 2: Download C++ API

Download latest version of C++ API from
<a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
rel="noopener noreferrer">moomoo official website</a>.

Decompress the downloaded file, the source code and samples for C++ API
are in the `/MMAPI4CPP` folder. For directory structure, please refer to
[MMAPI4CPP Directory](/moomoo-api-doc/en/quick/demo.html#3420).

#### <a href="#3786" class="header-anchor">#</a> MMAPI4CPP Directory



``` text
+---Bin                  Store the common library files compiled by the default compilation environment of various systems
+---Include              Directory store public header files, and .h/.cc files created by protobuf
+---Sample               Sample project
+---Src                  Source code
    +---MMAPI            MMAPI source code
    +---protobuf         Protobuf source code
```





### <a href="#181-4" class="header-anchor">#</a> Step 3: Import the sample project

The example provides project file for *Visual Studio* and *XCode*. You
can import sample projects using the *Visual Studio* or *XCode*
development environment.

### <a href="#8775-4" class="header-anchor">#</a> Step 4: Run

1.  Check whether the interface configuration of file simpleSample.cpp
    is consistent with the configuration of OpenD.

2.  You can see that the returned message for successful running as
    follows:



``` text
Run GetSecuritySnapshotDemo
InitQot, suc = 1
GetHKEqtySecList, count = 2698
GetSecuritySnapshot, i = 0
GetSecuritySnapshot, i = 1
GetSecuritySnapshot, i = 2
GetSecuritySnapshot, i = 3
GetSecuritySnapshot, i = 4
GetSecuritySnapshot, i = 5
GetSecuritySnapshot, i = 6
GetSecuritySnapshot, i = 7
GetSecuritySnapshot, i = 8
GetSecuritySnapshot, i = 9
GetSecuritySnapshot, i = 10
GetSecuritySnapshot, i = 11
GetSecuritySnapshot, i = 12
GetSecuritySnapshot, i = 13
ParseHKEqtySecQot, first = (HK.00001, 56.65)
GetSecuritySnapshotDemo End
```









## <a href="#7588" class="header-anchor">#</a> JavaScript example

### <a href="#2577-9" class="header-anchor">#</a> Step 1: Download and install OpenD

Please refer to [here](/moomoo-api-doc/en/quick/opend-base.html) to
finish downloading, installing and logging in OpenD.

### <a href="#6220" class="header-anchor">#</a> Step 2: Download JavaScript API

We provide two methods to download JavaScript API, you can choose one of
them.

- Method 1: Use npm install in cmd (npm only supports downloading
  JavaScript API source code. For more samples, please refer to Method
  2).

  - Initial installation: `$ npm install --save moomoo-api`.
  - Secondary upgrade: `$ npm update moomoo-api`.

- Method 2: Download latest version of JavaScript API from
  <a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
  rel="noopener noreferrer">moomoo official website</a>. Decompress the downloaded file, the
  source code and samples for JavaScript API are in the
  `/MMAPI4JS folder`. For directory structure, please refer to [MMAPI4JS
  Directory](/moomoo-api-doc/en/quick/demo.html#3557).

#### <a href="#2771" class="header-anchor">#</a> MMAPI4JS Directory



``` text
+---Sample               Sample project  
+---src                  Source code  
```





### <a href="#5927" class="header-anchor">#</a> Step 3: Run the example

1.  Open the example code folder `MMAPI4JS/sample` with Visual Studio
    Code.

2.  Find every WebSocket related code in the Demo folder, shown as
    below. Modify the configuration settlement (Note: WebSocket function
    will start in the Visualization OpenD by default, and need
    [Configuration
    Parameter](/moomoo-api-doc/en/opend/opend-cmd.html#149) to start in
    the Command Line OpenD.)
    ![websocket-demo-config](/moomoo-api-doc/assets/img/mm-websocket-demo-config.e4b9ca5c.png)

3.  Input `npm install` in the terminal of Visual Studio Code to install
    project dependency.
    ![websocket-demo-depend](/moomoo-api-doc/assets/img/mm-websocket-demo-depend.d1365ef4.png)

4.  Input `npm run serve` in the terminal of Visual Studio Code to run
    the project.
    ![websocket-demo-run](/moomoo-api-doc/assets/img/mm-websocket-demo-run.677381c2.png)

5.  After the project successful running, open the corresponding service
    address.
    ![websocket-demo-suc](/moomoo-api-doc/assets/img/mm-websocket-demo-suc.b677bded.png)

6.  Experience the relevant functions on the page.  
    ![websocket-demo-page](/moomoo-api-doc/assets/img/mm-websocket-demo-page.8967fce9.png)















