



# <a href="#6922" class="header-anchor">#</a> Others

## <a href="#5537" class="header-anchor">#</a> Q1：How to build C++ API?





A: futu-api c++ SDK is supported on Windows/MacOS/Linux. Pre-built libs
are provided for the common build environment on each platform:

| OS           | Building Environment |
|:-------------|:---------------------|
| Windows      | Visual Studio 2013   |
| Centos 7     | g++ 4.8.5            |
| Ubuntu 16.04 | g++ 5.4.0            |
| MacOS        | XCode 11             |

If different compiler version is used, or different protobuf version is
used, FTAPI and protobuf may be re-built. FTAPI source directory layout
is:



``` text
FTAPI directory structure：
+---Bin                               Libs for common build environment
+---Include                           Public headers, source files generated from proto files
+---Sample                            Sample project
\---Src
    +---FTAPI                         FTAPI source
    +---protobuf-all-3.5.1.tar.gz     protobuf source
```





#### <a href="#3830" class="header-anchor">#</a> Build steps：

1.  Build protobuf to generate libprotobuf static lib and protoc
    executable.
2.  Generated C++ source files from proto files.
3.  Build FTAPI to generate libFTAPI static lib

#### <a href="#964" class="header-anchor">#</a> Step1: Build protobuf：

- Windows：
  - Install CMake
  - Open Visual Studio command prompt, change directory to
    protobuf/cmake
  - Run：cmake -G "Visual Studio 12 2013" -DCMAKE_INSTALL_PREFIX=install -Dprotobuf_BUILD_TESTS=OFF  This
    will generate Visual Studio 2013 solution file. Change -G parameter
    for other Visual Studio versions.
  - Open Visual Studio solution file, set platform toolset to v120_xp,
    then build.
- Linux (Refer to protobuf/src/README)
  - Run ./autogen.sh
  - Run CXXFLAGS="-std=gnu++11" ./configure --disable-shared
  - Run make
  - Put generated libprotobuf.a in Bin/Linux
- MacOS (Refer to protobuf/src/README)
  - Install dependencies with brew：autoconf automake libtool
  - Run
    ./configure CC=clang CXX="clang++ -std=gnu++11 -stdlib=libc++" --disable-shared

#### <a href="#14" class="header-anchor">#</a> Step2: Generate C++ sources from proto files

- Use protoc to convert protofiles under Include/Proto to C++ source
  files. For example, the following command converts Common.proto to
  Common.pb.h and Common.pb.cc:
  - protoc -I="path-to-FTAPI/Include/Proto" --cpp_out="."
    path-to-FTAPI/Include/Proto/Common.proto
- Put the generated .h and .cc files in Include/Proto

#### <a href="#637" class="header-anchor">#</a> Step3: Build FTAPI

- Windows：Create Visual Studio C++ static lib project，add source files
  under Src/FTAPI and Include，and set platform toolset to v120_xp.
- Mac：Create XCode C++ static lib project，add source files under
  Src/FTAPI and Include
- Linux：Use cmake to build FTAPI static lib, run following command
  under path-to-FTAPI/Src:
  - cmake -DTARGET_OS=Linux





A: moomoo-api c++ SDK is supported on Windows/MacOS/Linux. Pre-built
libs are provided for the common build environment on each platform:

| OS           | Building Environment |
|:-------------|:---------------------|
| Windows      | Visual Studio 2013   |
| Centos 7     | g++ 4.8.5            |
| Ubuntu 16.04 | g++ 5.4.0            |
| MacOS        | XCode 11             |

If different compiler version is used, or different protobuf version is
used, MMAPI and protobuf may be re-built. MMAPI source directory layout
is:



``` text
MMAPI directory structure：
+---Bin                               Libs for common build environment
+---Include                           Public headers, source files generated from proto files
+---Sample                            Sample project
\---Src
    +---MMAPI                         MMAPI source
    +---protobuf-all-3.5.1.tar.gz     protobuf source
```





#### <a href="#3830-2" class="header-anchor">#</a> Build steps：

1.  Build protobuf to generate libprotobuf static lib and protoc
    executable.
2.  Generated C++ source files from proto files.
3.  Build MMAPI to generate libMMAPI static lib

#### <a href="#964-2" class="header-anchor">#</a> Step1: Build protobuf：

- Windows：
  - Install CMake
  - Open Visual Studio command prompt, change directory to
    protobuf/cmake
  - Run：cmake -G "Visual Studio 12 2013" -DCMAKE_INSTALL_PREFIX=install -Dprotobuf_BUILD_TESTS=OFF  This
    will generate Visual Studio 2013 solution file. Change -G parameter
    for other Visual Studio versions.
  - Open Visual Studio solution file, set platform toolset to v120_xp,
    then build.
- Linux (Refer to protobuf/src/README)
  - Run ./autogen.sh
  - Run CXXFLAGS="-std=gnu++11" ./configure --disable-shared
  - Run make
  - Put generated libprotobuf.a in Bin/Linux
- MacOS (Refer to protobuf/src/README)
  - Install dependencies with brew：autoconf automake libtool
  - Run
    ./configure CC=clang CXX="clang++ -std=gnu++11 -stdlib=libc++" --disable-shared

#### <a href="#14-2" class="header-anchor">#</a> Step2: Generate C++ sources from proto files

- Use protoc to convert protofiles under Include/Proto to C++ source
  files. For example, the following command converts Common.proto to
  Common.pb.h and Common.pb.cc:
  - protoc -I="path-to-MMAPI/Include/Proto" --cpp_out="."
    path-to-MMAPI/Include/Proto/Common.proto
- Put the generated .h and .cc files in Include/Proto

#### <a href="#3879" class="header-anchor">#</a> Step3: Build MMAPI

- Windows：Create Visual Studio C++ static lib project，add source files
  under Src/MMAPI and Include，and set platform toolset to v120_xp.
- Mac：Create XCode C++ static lib project，add source files under
  Src/MMAPI and Include
- Linux：Use cmake to build MMAPI static lib, run following command
  under path-to-MMAPI/Src:
  - cmake -DTARGET_OS=Linux





## <a href="#4658" class="header-anchor">#</a> Q2: Is there more complete strategy examples for reference?





A:

- Python strategy examples are in the /futu/examples/ folder. You can
  find the path of Python API by executing the following command:
  

  ``` text
  import futu
  print(futu.__file__)
  ```

  

  
- The C# strategy examples are in the /FTAPI4NET/Sample/ folder
- The Java strategy examples are in the /FTAPI4J/sample/ folder
- The C++ strategy examples are under the /FTAPI4CPP/Sample/ folder
- The JavaScript strategy examples are in the /FTAPI4JS/sample/ folder





A:

- Python strategy examples are in the /moomoo/examples/ folder. You can
  find the path of Python API by executing the following command:
  

  ``` text
  import moomoo
  print(moomoo.__file__)
  ```

  

  
- The C# strategy examples are in the /MMAPI4NET/Sample/ folder
- The Java strategy examples are in the /MMAPI4J/sample/ folder
- The C++ strategy examples are under the /MMAPI4CPP/Sample/ folder
- The JavaScript strategy examples are in the /MMAPI4JS/sample/ folder





## <a href="#548" class="header-anchor">#</a> Q3: Import error when using python API





A:

**First Scene:**  
I have already installed futu-api, but still get error: No module named
'futu'?  
It is possible that the interpreter your IDE currently uses is not the
interpreter of the futu-api module you installed. In other words, your
may have more than two Python environments installed on your computer.
You can do the following 2 steps:

1.  Run the codes below to get the path of the current interpreter:



``` text
import sys
print(sys.executable)
```





Example diagram:  
![No module named
'futu'](data:image/png;base64,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)

2.  Run `$ D:\software\anaconda3\python.exe -m pip install futu-api` in
    command line (The first half of the command comes from the result of
    step 1). This will install a futu-api module in the current
    interpreter.





**First Scene:**  
I have already installed moomoo-api, but still get error: No module
named 'moomoo'?  
It is possible that the interpreter your IDE currently uses is not the
interpreter of the moomoo-api module you installed. In other words, your
may have more than two Python environments installed on your computer.
You can do the following 2 steps:

1.  Run the codes below to get the path of the current interpreter:



``` text
import sys
print(sys.executable)
```





Example diagram:  
![No module named
'moomoo'](data:image/png;base64,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)

2.  Run `$ D:\software\anaconda3\python.exe -m pip install moomoo-api`
    in command line (The first half of the command comes from the result
    of step 1). This will install a moomoo-api module in the current
    interpreter.





## <a href="#5582" class="header-anchor">#</a> Q4: Import successful, but you still cannot call the relevant interface.





A: Usually in this case, you need to check if the ‘futu’ that was
successfully imported is a correct Futu API.

**First Scene:** There may be a file with the same name as 'futu'.

1.  The current file name is futu.py
2.  There is another file named futu.py under the path of the current
    file.
3.  There is a folder named `/futu` under the path of the current file.

Therefore, we strongly recommend that you do not name files / folders /
projects as *futu*.

**Second Scene:** A third-party library called 'futu' was installed by
mistake.

The correct name of the Futu API library is `futu-api`, not 'futu'.

If you have installed a third-party library named 'futu', please
uninstall it and [install
futu-api](/moomoo-api-doc/en/quick/demo.html#6763).

Take PyCharm as an example: Check the installation of libraries.

![settings](/moomoo-api-doc/assets/img/settings.a4197355.png)  
![futuku](/moomoo-api-doc/assets/img/futuku.5d8124c1.png)





A: Usually in this case, you need to check if the ‘moomoo’ that was
successfully imported is a correct moomoo API.

**First Scene:** There may be a file with the same name as 'moomoo'.

1.  The current file name is moomoo.py
2.  There is another file named moomoo.py under the path of the current
    file.
3.  There is a folder named `/moomoo` under the path of the current
    file.

Therefore, we strongly recommend that you do not name files / folders /
projects as *moomoo*.

**Second Scene:** A third-party library called 'moomoo' was installed by
mistake.

The correct name of the moomoo API library is `moomoo-api`, not
'moomoo'.

If you have installed a third-party library named 'moomoo', please
uninstall it and [install
moomoo-api](/moomoo-api-doc/en/quick/demo.html#6763).

Take PyCharm as an example: Check the installation of libraries.

![settings](/moomoo-api-doc/assets/img/settings.a4197355.png)  
![futuku](/moomoo-api-doc/assets/img/mmku.b7d92af2.png)





## <a href="#1479" class="header-anchor">#</a> Q5: Protocol Encryption-Related





A:

### <a href="#6105" class="header-anchor">#</a> Overview

To ensure privacy and confidentiality, you can use the asymmetric
encryption algorithm RSA to encrypt the request and return between
Strategy Scripts (Futu API) and OpenD.  
If Strategy Scripts (Futu API) is on the same computer as OpenD, it is
usually not necessary to encrypt.

### <a href="#3869" class="header-anchor">#</a> Protocol Encryption Process

You can try to solve this problem with the following steps:

1.  Generate the key file automatically through a third-party web
    platform.
    - To be specific: Search 'Online RSA Key Generator' on Baidu or
      Google. Set Key Format as PKCS#1. Set Key Length as 1024 bit. No
      password required. Then click the bottom 'Generate key pair'
      ![ui-config](/moomoo-api-doc/assets/img/en_create_rsa.60b193e5.png)
2.  Copy and paste the private key into a text file. Save it to a
    specified path of the computer which OpenD is located in.
3.  Specify the path of the RSA private key file on the computer which
    OpenD is located in. The path is the specified path mentioned in
    Step 2.
    - Method 1: Specify the path mentioned in Step 2 through 'Encryption
      Private Key' in [Visualization
      OpenD](/moomoo-api-doc/en/quick/opend-base.html#6196). As shown
      below:
      ![ui-config](/moomoo-api-doc/assets/img/en_rsa_ui-config.6fb5a349.png)
    - Method 2: Specify the path mentioned in Step 2 through the code
      `rsa_private_key` in [Command Line
      OpenD](/moomoo-api-doc/en/opend/opend-cmd.html#7893). As shown
      below:
      ![ui-config](/moomoo-api-doc/assets/img/rsa_xml.6ed36914.png)
4.  Save the text file in step 2 to a specified path of the computer
    which Strategy Scripts (Futu API) are located in, and [set the path
    of private key](/moomoo-api-doc/en/ftapi/init.html#6187) in Strategy
    Scripts.
5.  Enable protocol encryption. There are two ways to enable protocol
    encryption.
    - Method 1: Encrypt the context independently (general). You can set
      encryption through the parameter `is_encrypt` when creating and
      initializing the connection in [Quote
      Object](/moomoo-api-doc/en/quote/base.html#2335) or [Transaction
      Objects](/moomoo-api-doc/en/trade/base.html#8155).
    - Method 2: Encrypt the context globally (only Python). You can set
      encryption through the interface
      [enable_proto_encrypt](/moomoo-api-doc/en/ftapi/init.html#7910).



Tips

- When specifying the path of RSA private key in OpenD or in Strategy
  Scripts (Futu API), the path needs to be complete and include the file
  name.
- It is not necessary to save RSA public key which can be calculated by
  private key.







A:

### <a href="#6105-2" class="header-anchor">#</a> Overview

To ensure privacy and confidentiality, you can use the asymmetric
encryption algorithm RSA to encrypt the request and return between
Strategy Scripts (moomoo API) and OpenD.  
If Strategy Scripts (moomoo API) is on the same computer as OpenD, it is
usually not necessary to encrypt.

### <a href="#3869-2" class="header-anchor">#</a> Protocol Encryption Process

You can try to solve this problem with the following steps:

1.  Generate the key file automatically through a third-party web
    platform.
    - To be specific: Search 'Online RSA Key Generator' on Baidu or
      Google. Set Key Format as PKCS#1. Set Key Length as 1024 bit. No
      password required. Then click the bottom 'Generate key pair'
      ![ui-config](/moomoo-api-doc/assets/img/en_create_rsa.60b193e5.png)
2.  Copy and paste the private key into a text file. Save it to a
    specified path of the computer which OpenD is located in.
3.  Specify the path of the RSA private key file on the computer which
    OpenD is located in. The path is the specified path mentioned in
    Step 2.
    - Method 1: Specify the path mentioned in Step 2 through 'Encryption
      Private Key' in [Visualization
      OpenD](/moomoo-api-doc/en/quick/opend-base.html#6196). As shown
      below:
      ![ui-config](/moomoo-api-doc/assets/img/mmen_rsa_ui-config.fc08cb56.png)
    - Method 2: Specify the path mentioned in Step 2 through the code
      `rsa_private_key` in [Command Line
      OpenD](/moomoo-api-doc/en/opend/opend-cmd.html#7893). As shown
      below:
      ![ui-config](/moomoo-api-doc/assets/img/mm_xml.5faae8a3.png)
4.  Save the text file in step 2 to a specified path of the computer
    which Strategy Scripts (moomoo API) are located in, and [set the
    path of private key](/moomoo-api-doc/en/ftapi/init.html#6187) in
    Strategy Scripts.
5.  Enable protocol encryption. There are two ways to enable protocol
    encryption.
    - Method 1: Encrypt the context independently (general). You can set
      encryption through the parameter `is_encrypt` when creating and
      initializing the connection in [Quote
      Object](/moomoo-api-doc/en/quote/base.html#2335) or [Transaction
      Objects](/moomoo-api-doc/en/trade/base.html#8155).
    - Method 2: Encrypt the context globally (only Python). You can set
      encryption through the interface
      [enable_proto_encrypt](/moomoo-api-doc/en/ftapi/init.html#7910).



Tips

- When specifying the path of RSA private key in OpenD or in Strategy
  Scripts (moomoo API), the path needs to be complete and include the
  file name.
- It is not necessary to save RSA public key which can be calculated by
  private key.







## <a href="#9716" class="header-anchor">#</a> Q6: Why is the DataFrame data I got incomplete?

A: When printing pandas.DataFrame data, if there are too many columns
and rows, pandas will collapse the data by default, resulting in an
incomplete display.  
Therefore, it is not OpenD's fault. You can add the following code in
front of your Python script to solve the problem.



``` text
import pandas as pd
pd.options.display.max_rows=5000
pd.options.display.max_columns=5000
pd.options.display.width=1000
```





## <a href="#444" class="header-anchor">#</a> Q7: How to solve the problem that "Cannot open libFTAPIChannel.dylib" through C++ API on Mac?





A: Execute the following command in the directory where the file
"libFTAPIChannel.dylib" is stored:
`$ xattr -r -d com.apple.quarantine libFTAPIChannel.dylib`.





A: Execute the following command in the directory where the file
"libFTAPIChannel.dylib" is stored:
`$ xattr -r -d com.apple.quarantine libAPIChannel.dylib`.





## <a href="#6076" class="header-anchor">#</a> Q8: For Python users, why do large log files continue to be generated under the log folder, after the log level is set to no in the OpenD configuration file?

A：The *log_level* parameter in OpenD parameter configuration is only
used to control the logs generated by OpenD. Python API also generates
logs by default.  
If you do not like it, you can add the following codes to your Python
script:



``` text
logger.file_level = logging.FATAL  # Used to stop Python API log files generating
logger.console_level = logging.FATAL  # Used to stop printing Python log in running console
```





## <a href="#5994" class="header-anchor">#</a> Q9: For versions 5.4 and above, the library name and configuration method of Java API have been changed.





A:

- If you are a user of Java API 5.3 and below, please note the following
  changes when updating the version.  
  **Changes to the configuration process:**

  1.  Download Futu API from
      <a href="https://www.futunn.com/en/download/OpenAPI?client=OpenAPI"
      target="_blank" rel="noopener noreferrer">Futubull official website</a>.
  2.  Decompress the downloaded file. `/FTAPI4J` is the directory of
      Java API. Add `/lib/futu-api-.x.y.z.jar` file to your project
      settings. To establish a futu-api project, please refer to
      [here](/moomoo-api-doc/en/quick/demo.html#1983).

  **Changes to the directory:**

  1.  For the Java version of Futu API, the library name is changed from
      ftapi4j.jar to `futu-api-x.y.z.jar`, where "x.y.z" represents the
      version number.
  2.  For the third-party library, the dependencies of /lib/jna.jar and
      /lib/jna-platform.jar are removed, and the dependencies of
      `/lib/bcprov-jdk15on-1.68.jar` and `/lib/bcpkix-jdk15on-1.68.jar`
      are added.

  

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

  

  

- If you are a new user to the Futu API, we provide a more convenient
  way to configure Java API via maven repository for you. About the
  configuration process, please refer to
  [here](/moomoo-api-doc/en/quick/demo.html#5062).





A:

- If you are a user of Java API 5.3 and below, please note the following
  changes when updating the version.  
  **Changes to the configuration process:**

  1.  Download moomoo API from
      <a href="https://www.moomoo.com/download" target="_blank"
      rel="noopener noreferrer">moomoo official website</a>.
  2.  Decompress the downloaded file. `/MMAPI4J` is the directory of
      Java API. Add `/lib/moomoo-api-.x.y.z.jar` file to your project
      settings. To establish a moomoo-api project, please refer to
      [here](/moomoo-api-doc/en/quick/demo.html#1983).

  **Changes to the directory:**

  1.  For the Java version of moomoo API, the library name is changed
      from ftapi4j.jar to `moomoo-api-x.y.z.jar`, where "x.y.z"
      represents the version number.
  2.  For the third-party library, the dependencies of /lib/jna.jar and
      /lib/jna-platform.jar are removed, and the dependencies of
      `/lib/bcprov-jdk15on-1.68.jar` and `/lib/bcpkix-jdk15on-1.68.jar`
      are added.

  

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

  

  

- If you are a new user to the moomoo API, we provide a more convenient
  way to configure Java API via maven repository for you. About the
  configuration process, please refer to
  [here](/moomoo-api-doc/en/quick/demo.html#5062).





## <a href="#4128" class="header-anchor">#</a> Q10: For Python users, when using pyinstaller to package scripts that need to run api, an error is reported: Common_pb2 module cannot be found.





A: You can try to solve this problem with the following steps.  
Step 1. Suppose you need to package main.py. Using a command-line
statement and run the statement: pyinstaller path\main.py, without the
"- F" parameter.



``` text
pyinstaller path\main.py
```





After main.py is packaged, the /main folder will be created in the /dist
directory where it is located. main.exe is in this folder.  
![dist](data:image/png;base64,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)

Step 2. Run the following code to find the installation path of
futu-api: /path/futu.



``` text
import futu
print(futu.__file__)
```





Results:



``` text
C:\Users\ceciliali\Anaconda3\lib\site-packages\futu\__init__.py
```





![pathfutu](/moomoo-api-doc/assets/img/pathfutu.a048f949.png)

Step 3. Copy all the files in the /common/pb to /main.

Step 4. Create a folder in the /main and name it futu. Copy the
`/path/futu/VERSION.txt` file to /main/futu.  
![main_futu](/moomoo-api-doc/assets/img/main_futu.ef121317.png)  
Step 5. Try running the statement **pyinstaller main.py** again.





A: You can try to solve this problem with the following steps.  
Step 1. Suppose you need to package main.py. Using a command-line
statement and run the statement: pyinstaller path\main.py, without the
"- F" parameter.



``` text
pyinstaller path\main.py
```





After main.py is packaged, the /main folder will be created in the /dist
directory where it is located. main.exe is in this folder.  
![dist](/moomoo-api-doc/assets/img/mmdist.fde7a91b.png)

Step 2. Run the following code to find the installation path of
moomoo-api: /path/moomoo.



``` text
import moomoo
print(moomoo.__file__)
```





Results:



``` text
C:\Users\ceciliali\Anaconda3\lib\site-packages\moomoo\__init__.py
```





![pathfutu](/moomoo-api-doc/assets/img/pathmoomoo.a3726fe7.png)

Step 3. Copy all the files in the /common/pb to /main.

Step 4. Create a folder in the /main and name it moomoo. Copy the
`/path/moomoo/VERSION.txt` file to /main/moomoo.  
![main_moomoo](/moomoo-api-doc/assets/img/main_moomoo.45ec72a8.png)  
Step 5. Try running the statement **pyinstaller main.py** again.





## <a href="#3153" class="header-anchor">#</a> Q11: Why the interface result is success, but the return did not behave as expected？

A:

- A successful interface result means that server has successfully
  received and responded to your request, but the return may not behave
  as your expected.

  Example: If you call the
  [subscribe](/moomoo-api-doc/en/quote/sub.html) during non-trading
  hours, your request can be responded successfully, but the exchange
  will not update the ticker data during this period. So you will
  temporarily not receive real-time data until trading hours.

- The interface result (definition: [Interface
  Result](/moomoo-api-doc/en/ftapi/common.html#8800)) can be viewed from
  the field returned. A field of 0 means the interface result success, a
  non-zero means the interface result failed.

  For python user, the following two code statements are equivalent:

  

  ``` text
  if ret_code == RET_OK:
  ```

  

  

  

  ``` text
  if ret_code == 0:
  ```

  

  

## <a href="#5728" class="header-anchor">#</a> Q12: WebSocket Related





### <a href="#6105-3" class="header-anchor">#</a> Overview

In OpenAPI, WebSocket is mainly used in the following two aspects:

- In Visualization OpenD, WebSocket is used to communicate between the
  UI interface and the underlying Command Line OpenD.
- The communication between JavaScript API and OpenD uses WebSocket.

![WebSocket-struct](/moomoo-api-doc/assets/img/WebSocket-struct.422f6d9f.png)

- When WebSocket starts, Command Line OpenD establishes a Socket
  connection (TCP) with the **FTWebSocket transit service**. This
  connection uses the default **listening address** and **API protocol
  listening port**.
- At the same time, JavaScript API will establish a WebSocket connection
  (HTTP) with the **FTWebSocket transit service**. This connection will
  use the **WebSocket listening address** and **WebSocket port**.

### <a href="#6771" class="header-anchor">#</a> Usage

To ensure the security of your account, when WebSocket listens non-local
requests, we strongly recommend that you enable SSL and configure the
**WebSocket authentication key**

SSL is enabled by configuring the **WebSocket certificate** and the
**WebSocket private key**. Command Line OpenD can set the file path by
configuring OpenD.xml or configuring command line parameters.
Visualization OpenD clicks the "more" drop-down menu to see the
confifuration item.

![ui-more-config](/moomoo-api-doc/assets/img/ui-more-config.a516c891.png)



Tips

If the certificate is self-signed, you need to install the certificate
on the machine where the JavaScript API is called, or set not to verify
the certificate.



#### <a href="#6461" class="header-anchor">#</a> Generate Self-signed Certificate

It is not convenient to expand the details of self-signed certificate
generation in this document, please check it yourself. Simple and
available build steps are provided here:

1.  Install openssl.
2.  Modify openssl.cnf and add the IP address or domain name under the
    alt_names node on the machine where OpenD locates.  
    For example: IP.2 = xxx.xxx.xxx.xxx, DNS.2 = www.xxx.com
3.  Generate private key and certificate (PEM)。

**The certificate generation parameters are as follows**：  
`openssl req -x509 -newkey rsa:2048 -out futu.cer -outform PEM -keyout futu.key -days 10000 -verbose -config openssl.cnf -nodes -sha256 -subj "/CN=Futu CA" -reqexts v3_req -extensions v3_req`



Tips

- openssl.cnf needs to be placed under the system path, or an absolute
  path needs to be specified in the build parameters.
- Note that while generating a private key, you need to specify that the
  password is not set (-notes).



Attach the local self-signed certificate and the configuration file that
generates the certificate for testing:

- [openssl.cnf](../file/openssl.cnf)
- [futu.cer](../file/cer)
- [futu.key](../file/key)





### <a href="#6105-4" class="header-anchor">#</a> Overview

In OpenAPI, WebSocket is mainly used in the following two aspects:

- In Visualization OpenD, WebSocket is used to communicate between the
  UI interface and the underlying Command Line OpenD.
- The communication between JavaScript API and OpenD uses WebSocket.

![WebSocket-struct](/moomoo-api-doc/assets/img/WebSocket-struct.422f6d9f.png)

- When WebSocket starts, Command Line OpenD establishes a Socket
  connection (TCP) with the **MMWebSocket transit service**. This
  connection uses the default **listening address** and **API protocol
  listening port**.
- At the same time, JavaScript API will establish a WebSocket connection
  (HTTP) with the **MMWebSocket transit service**. This connection will
  use the **WebSocket listening address** and **WebSocket port**.

### <a href="#6771-2" class="header-anchor">#</a> Usage

To ensure the security of your account, when WebSocket listens non-local
requests, we strongly recommend that you enable SSL and configure the
**WebSocket authentication key**

SSL is enabled by configuring the **WebSocket certificate** and the
**WebSocket private key**. Command Line OpenD can set the file path by
configuring OpenD.xml or configuring command line parameters.
Visualization OpenD clicks the "more" drop-down menu to see the
confifuration item.

![ui-more-config](/moomoo-api-doc/assets/img/mmui-more-config.d50cf485.png)



Tips

If the certificate is self-signed, you need to install the certificate
on the machine where the JavaScript API is called, or set not to verify
the certificate.



#### <a href="#6461-2" class="header-anchor">#</a> Generate Self-signed Certificate

It is not convenient to expand the details of self-signed certificate
generation in this document, please check it yourself. Simple and
available build steps are provided here:

1.  Install openssl.
2.  Modify openssl.cnf and add the IP address or domain name under the
    alt_names node on the machine where OpenD locates.  
    For example: IP.2 = xxx.xxx.xxx.xxx, DNS.2 = www.xxx.com
3.  Generate private key and certificate (PEM)。

**The certificate generation parameters are as follows**：  
`openssl req -x509 -newkey rsa:2048 -out moomoo.cer -outform PEM -keyout moomoo.key -days 10000 -verbose -config openssl.cnf -nodes -sha256 -subj "/CN=moomoo CA" -reqexts v3_req -extensions v3_req`



Tips

- openssl.cnf needs to be placed under the system path, or an absolute
  path needs to be specified in the build parameters.
- Note that while generating a private key, you need to specify that the
  password is not set (-notes).



Attach the local self-signed certificate and the configuration file that
generates the certificate for testing:

- [openssl.cnf](../file/openssl.cnf)
- [moomoo.cer](../file/cer)
- [moomoo.key](../file/key)





## <a href="#2427" class="header-anchor">#</a> Q13: Where are the quote servers and the trade servers of OpenAPI?

A：

- Quote:

| Futu ID     | Quote Server Location                     |
|:------------|:------------------------------------------|
| Futubull ID | Tencent Cloud Guangzhou and Hong Kong     |
| moomoo ID   | Tencent Cloud Virginia, USA and Singapore |

- Trade:

| Securities Firm | Trade Server Location       |
|:----------------|:----------------------------|
| FUTU HK         | Tencent Cloud Hong Kong     |
| Moomoo US       | Tencent Cloud Virginia, USA |
| Moomoo SG       | Tencent Cloud Singapore     |
| Moomoo AU       | AWS Cloud Sydney            |





## <a href="#2212" class="header-anchor">#</a> Q14: The Guide for Universal Account Upgrade

### <a href="#2723" class="header-anchor">#</a> 1. <a href="https://www.futuhk.com/en/support/topic2_1734" target="_blank"
rel="noopener noreferrer"><strong>Universal Account Upgrade</strong></a>

The universal account allows trading securities, futures, and forex
across various markets using multiple currencies within one account.
Upgrading one or multiple single-market accounts to a universal account
involves migrating under your old account. This includes:

- Creating a universal account
- Transferring assets from your existing single-market account to the
  universal account
- Closing the single-market account

### <a href="#6205" class="header-anchor">#</a> 2. **OpenD Version Upgrade**

We are scheduled to upgrade your accounts to universal accounts on
September 14th and 15th, 2024. Please check your OpenD and API versions
in advance.

- **Version 7.01 and below**  
  Due to the outdated versions, OpenD will discontinue service on
  September 14th, 2024, during which you will be logged out of OpenD
  automatically. We recommend upgrading your
  [OpenD](/moomoo-api-doc/en/quick/opend-base.html#6196) and
  [API](/moomoo-api-doc/en/quick/demo.html#6763) to the latest version
  before September 14th, and stopping any live trading strategies over
  the weekend of September 14th to 15th.

- **Version 7.02 to 8.2**  
  Due to the older versions, OpenD no longer supports universal
  accounts. We recommend upgrading your
  [OpenD](/moomoo-api-doc/en/quick/opend-base.html#6196) and
  [API](/moomoo-api-doc/en/quick/demo.html#6763) to the latest version
  before September 14th, and stopping any live trading strategies over
  the weekend of September 14th to 15th.

- **Version 8.3 and above**  
  You can use these versions normally. However, we also recommend not
  running any live trading strategies over the weekend of September 14th
  to 15th.

After upgrading, your assets will be transferred to the new universal
account, causing strategies targeting the old account to malfunction. We
recommend conducting necessary checks and tests before live trading, to
ensure everything is set up properly.

### <a href="#4417" class="header-anchor">#</a> 3. **Changes in OpenAPI after the OpenD upgrade**

- Python API will no longer support creating transaction objects with
  OpenHKTradeContext, OpenUSTradeContext, OpenHKCCTradeContext, and
  OpenCNTradeContext. Please refer to the [Create the
  connection](/moomoo-api-doc/en/trade/base.html#3490), and use
  OpenSecTradeContext instead.

- For non-Python API users, when using the Trd_GetAccList, please set
  the needGeneralSecAccount to true in order to get Universal account
  information.

- Add [Account Status](/moomoo-api-doc/en/trade/trade.html#8311)  
  When using the [Get the List of Trading
  Accounts](/moomoo-api-doc/en/trade/get-acc-list.html#9665), the
  results will now include an *acc_status* field.

  - The universal accounts are marked as `ACTIVE`.
  - The old single-market accounts are marked as `DISABLED`.

- Changes in Trading API: [Place
  Orders](/moomoo-api-doc/en/trade/place-order.html#3634), [Modify or
  Cancel Orders](/moomoo-api-doc/en/trade/modify-order.html#8129),
  [Query the Maximum Quantity that Can be Bought or
  Sold](/moomoo-api-doc/en/trade/get-max-trd-qtys.html#334)

  - Executing transactions and querying purchasing power can only be
    allowed via the *acc_id* or *acc_index* of `ACTIVE` accounts.
  - Using the *acc_id* or *acc_index* of `DISABLED` accounts will cause
    errors.
  - Python API：please specify the **acc_id** as the upgraded universal
    account.
  - Non-Python API：in the TrdHeader, please specify the **accID** as
    the upgraded universal account.

### <a href="#6180" class="header-anchor">#</a> 4. **Need help?**

- **Team Support**  
  If you encounter any issues during the upgrade process or while using
  the universal account, you can contact our technical/product teams
  through [official channels](/moomoo-api-doc/en/qa/opend.html#605).

- **Stay Focused**  
  We will continue to publish the latest notifications and assistance
  information through Futu API Doc, emails, APP messages, QQ, etc.
  Please pay attention to official updates.















