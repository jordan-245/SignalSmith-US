



# <a href="#4873" class="header-anchor">#</a> OpenD Related

## <a href="#3127" class="header-anchor">#</a> Q1: OpenD automatically exited due to failure to complete "Questionnaire Evaluation and Agreement Confirmation"





A: You need to carryout relevant questionnaire evaluation and agreement
confirmation before you can use OpenD. Please
<a href="https://www.futunn.com/about/api-disclaimer?lang=en-US"
target="_blank" rel="noopener noreferrer">go to complete</a>.





A: You need to carryout relevant questionnaire evaluation and agreement
confirmation before you can use OpenD. Please
<a href="https://www.moomoo.com/en-us/about/api-disclaimer"
target="_blank" rel="noopener noreferrer">go to complete</a>.





## <a href="#8726" class="header-anchor">#</a> Q2: OpenD exited due to "the program's own data does not exist"





A: Generally, the copy of the own data fails due to permission problems.
You can try to copy the file extracted from ***Appdata.dat*** in the
program directory to the program data directory.

- Windows program data directory:`%appdata%/com.futunn.FutuOpenD/F3CNN`
- Non-windows program data directory: `~/.com.futunn.FutuOpenD/F3CNN`





A: Generally, the copy of the own data fails due to permission problems.
You can try to copy the file extracted from ***Appdata.dat*** in the
program directory to the program data directory.

- Windows program data directory:`%appdata%/com.moomoo.OpenD/F3CNN`
- Non-windows program data directory:`~/.com.moomoo.OpenD/F3CNN`





## <a href="#2083" class="header-anchor">#</a> Q3: OpenD service failed to start

A: Please check:

1.  Whether there are other programs occupying the configured port;
2.  Is there a OpenD configured with the same port already running?

## <a href="#583" class="header-anchor">#</a> Q4: How to verify the mobile phone verification code?

A: On the OpenD interface or remotely to the Telnet port, enter the
command ʻinput_phone_verify_code -code=123456\`.



Tips

- 123456 is the mobile phone verification code received
- there is a space before '-code=123456'



## <a href="#9516" class="header-anchor">#</a> Q5: Are other programming languages supported?





A: OpenD provides a socket-based protocol. Currently we provide and
maintain Python, C++, Java, C# and JavaScript interfaces,
<a href="https://www.futunn.com/download/OpenAPI?lang=en-US"
target="_blank" rel="noopener noreferrer">download entry</a>.

If the above languages still cannot meet your needs, you can connect to
the Protobuf protocol by yourself.





A: OpenD provides a socket-based protocol. Currently we provide and
maintain Python, C++, Java, C# and JavaScript interfaces,
<a href="https://www.futunn.com/download/OpenAPI?lang=en-US"
target="_blank" rel="noopener noreferrer">download entry</a>.

If the above languages still cannot meet your needs, you can connect to
the Protobuf protocol by yourself.





## <a href="#2453" class="header-anchor">#</a> Q6: Verify the device lock multiple times on the same device





A: The device ID is randomly generated and stored in the
\com.futunn.OpenD\F3CNN\Device.dat file.



Tips

1.  If the file is deleted or damaged, OpenD will regenerate a new
    device ID and then verify the device lock.
2.  In addition, users of mirror copy deployment need to be aware that
    if the Device.dat content of multiple machines is the same, it will
    also cause these machines to verify the device lock multiple times.
    Delete the Device.dat file to solve it.







A: The device ID is randomly generated and stored in the
\com.moomoo.OpenD\F3CNN\Device.dat file.



Tips

1.  If the file is deleted or damaged, OpenD will regenerate a new
    device ID and then verify the device lock.
2.  In addition, users of mirror copy deployment need to be aware that
    if the Device.dat content of multiple machines is the same, it will
    also cause these machines to verify the device lock multiple times.
    Delete the Device.dat file to solve it.







## <a href="#3889" class="header-anchor">#</a> Q7: Does OpenD provide a Docker image?

A: Not currently available.

## <a href="#8879" class="header-anchor">#</a> Q8: Can one account log in to multiple OpenD?

A: One account can log in to OpenD or other client terminals on multiple
machines, and up to 10 OpenD terminals are allowed to log in at the same
time. At the same time, there is a restriction of "market kicking", and
only one OpenD can obtain the highest authority market. For example, if
two terminals log into the same account, there can only be one HK stock
LV2 quotation and the other HK stock BMP quotation.

## <a href="#5285" class="header-anchor">#</a> Q9: How to control the market permissions of OpenD and other clients (desktop and mobile)?

A: In accordance with the regulations of the exchange, there will be a
restriction on “market kicking” when multiple terminals are online at
the same time, and only one terminal can obtain the highest authority
market. The
[auto_hold_quote_right](/moomoo-api-doc/en/opend/opend-cmd.html#149)
parameter is built-in in the startup parameters of the command line
version of OpenD, which is used to flexibly configure market
permissions. When this parameter option is enabled, OpenD will
automatically retrieve it after the market permission is robbed. If it
is robbed again within 10 seconds, other terminals will obtain the
highest market quotation authority (OpenD will not rob again).

## <a href="#801" class="header-anchor">#</a> Q10: How to give priority to the OpenD market authority?





A:

1.  Configure the OpenD startup parameter
    [auto_hold_quote_right](/moomoo-api-doc/en/opend/opend-cmd.html#149)
    to 1;
2.  Make sure not to grab the highest authority twice in a row within 10
    seconds on the mobile or desktop Futubull (login counts once, and
    click "Restart Quotes" to count the second time).





A:

1.  Configure the OpenD startup parameter
    [auto_hold_quote_right](/moomoo-api-doc/en/opend/opend-cmd.html#149)
    to 1;
2.  Make sure not to grab the highest authority twice in a row within 10
    seconds on the mobile or desktop moomoo (login counts once, and
    click "Restart Quotes" to count the second time).





![quote-right-kick](data:image/png;base64,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)

## <a href="#2244" class="header-anchor">#</a> Q11: How to give priority to the market authority of the mobile terminal (or desktop terminal)?





A: Set OpenD startup parameter
[auto_hold_quote_right](/moomoo-api-doc/en/opend/opend-cmd.html#149) to
0, and login with mobile or PC Futubull after OpenD.





A: Set OpenD startup parameter
[auto_hold_quote_right](/moomoo-api-doc/en/opend/opend-cmd.html#149) to
0, and login with mobile or PC moomoo after OpenD.





## <a href="#9285" class="header-anchor">#</a> Q12: Use the Visualization OpenD to remember the password to log in. After a long time hang up, it prompts that the connection is disconnected. Do I need to log in again?

A: Using the Visualization OpenD, if you choose to remember the password
to log in, you will use the token recorded locally. Due to the time
limit of the token, when the token expires, if there is network
fluctuation or moomoo background release, it may cause the situation
that it cannot be automatically connected after disconnecting from the
background. Therefore, if you want visiulization OpenD for a long time
to hang up, it is recommended to manually enter the password to log in,
and OpenD will automatically handle this situation.

## <a href="#605" class="header-anchor">#</a> Q13: How to request official engineers to investigate logs when encountering product defects?





A: Communicate the issue with customer service, providing details such
as: the time when the error occurred, OpenD version number, API version
number, script language name, interface name or protocol number, and
short code or screenshots containing detailed input parameters and
returns.

After customer service confirms it's a product defect, if further log
investigation is needed, development engineers will proactively contact
you.

Some issues may require OpenD logs to help locate and confirm the
problem. For trading-related issues, info log level is needed; for
market-data-related issues, debug log level is required. The log level
(log_level) can be configured in OpenD.xml . After configuration, OpenD
needs to be restarted for the changes to take effect. Once the issue is
reproduced, package that section of the log and send it to Futu's
development engineers.



Tips

The log path is as follows:

windows: `%appdata%/com.futunn.FutuOpenD/Log`

Non-windows: `~/.com.futunn.FutuOpenD/Log`







A:

1.  Contact OpenAPI developers via QQ/WeChat to facilitate instant
    communication and file transferation.

2.  Detailed description: the time when the error occurred, OpenD
    version number, moomoo API version number, script language name,
    interface name or protocol number, short code or screenshot with
    detailed input and return.

3.  If necessary, OpenD log must be provided to facilitate location and
    confirmation of problems. Transaction issues require info log level,
    and market issues require debug log level. The log level log_level
    can be configured in ***OpenD.xml***
    [Configure](/moomoo-api-doc/en/opend/opend-cmd.html#149). After
    configuration, OpenD needs to be restarted to take effect. After the
    problem recurs, package the log and send it to moomoo R&D personnel.



Tips

The log path is as follows:

windows: `%appdata%/com.moomoo.OpenD/Log`

Non-windows: `~/.com.moomoo.OpenD/Log`







## <a href="#1308" class="header-anchor">#</a> Q14: Script cannot connect to OpenD

A: Please try to check first:

1.  Whether the port connected by the script is consistent with the port
    configured by OpenD.
2.  Since the upper limit of OpenD connection is 128, is there any
    useless connection that is not closed?
3.  Check whether the listening address is correct. If the script and
    OpenD are not on the same machine, the OpenD listening address needs
    to be set to 0.0.0.0.

## <a href="#3043" class="header-anchor">#</a> Q15: Disconnected after being connected for a while

A: If it is a self-docking protocol, check whether there is a regular
heartbeat to maintain the connection.

## <a href="#2215" class="header-anchor">#</a> Q16: I can't connect to OpenD when I run Python scripts in multiprocessing mode through the multiprocessing module under Linux?





A: After the process is created by default in the Linux/Mac environment,
the thread created inside py-futu-api in the parent process will
disappear in the child process, resulting in an internal program error.
You can use spawn to start the process:



``` python
import multiprocessing as mp
mp.set_start_method('spawn')
p = mp.Process(target=func)
```









A: After the process is created by default in the Linux/Mac environment,
the thread created inside py-moomoo-api in the parent process will
disappear in the child process, resulting in an internal program error.
You can use spawn to start the process:



``` python
import multiprocessing as mp
mp.set_start_method('spawn')
p = mp.Process(target=func)
```









## <a href="#7685" class="header-anchor">#</a> Q17: How to log in to two OpenD at the same time on one computer?





A: Visualization OpenD does not support, but Command Line OpenD
supports.

1.  Unzip the file downloaded from the official website, and copy the
    entire Command Line OpenD folder (e.g.
    ***OpenD_5.2.1408_Windows***). Take Windows as an example, other
    systems can do the same operation.

![en-copied](/moomoo-api-doc/assets/img/en-copied.6341117e.png)

2.  Configure two ***OpenD.xml*** files that are placed in two Command
    Line OpenD folders. Configure items as follow:

Configuration file 1: api_port = 11111, login_account = Login Account 1,
login_pwd = Login Password 1

Configuration file 2: api_port = 11112, login_account = Login Account 2,
login_pwd = Login Password 2

![order-page](/moomoo-api-doc/assets/img/nnorder-page.9716528d.png)

3.  Run the two OpenD.exe.

![en-folder](/moomoo-api-doc/assets/img/en-folder.086dc7c1.png)

4.  When calling the interface, note that the parameter `port` (OpenD
    listening address) should corresponds to the parameter `api_port` in
    the ***OpenD.xml file***.  
    For example:



``` python
from futu import *

# Send requests to OpenD logged in account 1
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111, is_encrypt=False)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out

# Send requests to OpenD logged in account 2
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11112, is_encrypt=False)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```









A: Visualization OpenD does not support, but Command Line OpenD
supports.

1.  Unzip the file downloaded from the official website, and copy the
    entire Command Line OpenD folder (e.g.
    ***moomoo_OpenD_5.2.1408_Windows***). Take Windows as an example,
    other systems can do the same operation.

![en-copied](/moomoo-api-doc/assets/img/en-mmcopied.72750354.png)

2.  Configure two ***OpenD.xml*** files that are placed in two Command
    Line OpenD folders. Configure items as follow:

Configuration file 1: api_port = 11111, login_account = Login Account 1,
login_pwd = Login Password 1

Configuration file 2: api_port = 11112, login_account = Login Account 2,
login_pwd = Login Password 2

![order-page](/moomoo-api-doc/assets/img/order-page.5d13af50.png)

3.  Run the two OpenD.exe.

![en-folder](/moomoo-api-doc/assets/img/mmen-folder.101b4c82.png)

4.  When calling the interface, note that the parameter `port` (OpenD
    listening address) should corresponds to the parameter `api_port` in
    the ***OpenD.xml file***.  
    For example:



``` python
from moomoo import *

# Send requests to OpenD logged in account 1
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111, is_encrypt=False)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out

# Send requests to OpenD logged in account 2
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11112, is_encrypt=False)
quote_ctx.close() # After using the connection, remember to close it to prevent the number of connections from running out
```









## <a href="#4390" class="header-anchor">#</a> Q18: How do I execute the operation and maintenance commands for grabbing permissions through scripts when the market permission is kicked off by other clients?

A:

1.  Configure Telnet address and Telnet port.
    ![telnet_GUI](/moomoo-api-doc/assets/img/telnet_GUI.0ac368ba.png)
    ![telnet_CMD](/moomoo-api-doc/assets/img/telnet_CMD.b0d3e174.jpg)
2.  Start OpenD (it will also start Telnet).
3.  After finding that the market quotation authority has been robbed,
    you can refer to the following code example and send the
    `request_highest_quote_right` command to OpenD via Telnet.



``` python
from telnetlib import Telnet
with Telnet('127.0.0.1', 22222) as tn: # Telnet address is: 127.0.0.1, Telnet port is: 22222
     tn.write(b'request_highest_quote_right\r\n')
     reply = b''
     while True:
         msg = tn.read_until(b'\r\n', timeout=0.5)
         reply += msg
         if msg == b'':
             break
     print(reply.decode('gb2312'))
```







## <a href="#9361" class="header-anchor">#</a> Q19: OpenD automatic upgrade failed

A: The automatic update of OpenD failed to be executed by the `update`
command. Possible reasons:

- The file is occupied by other processes: you can try to close other
  OpenD processes, or restart the system and execute `update` again If
  the above still cannot be solved, you can download the update by
  yourself through
  <a href="https://www.moomoo.com/download/OpenAPI/" target="_blank"
  rel="noopener noreferrer">Official Website</a>.

## <a href="#7762" class="header-anchor">#</a> Q20: Fail to launch the visualization OpenD on ubuntu22？

A: When running the visualization OpenD on certain Linux distributions
(such as Ubuntu 22.04), you may encounter the error:
`dlopen(): error loading libfuse.so.2`. This occurs because libfuse is
not installed by default on these systems. Typically you can resolve
this issue by installing libfuse manually. For example, you can install
it via the commane line on Ubuntu22.04 with:



``` text
sudo apt update
sudo apt install -y libfuse2
```





Once successfully installed, you will be able to run the visualization
OpenD normally. Please refer to
<a href="https://docs.appimage.org/user-guide/troubleshooting/fuse.html"
target="_blank"
rel="noopener noreferrer">https://docs.appimage.org/user-guide/troubleshooting/fuse.html</a> for more details.

## <a href="#758" class="header-anchor">#</a> Q21: How to run the command line OpenD in the background on Linux?





A: First, switch to the directory where FutuOpenD is located, configure
FutuOpenD.xml, and then execute the following command.



``` text
nohup ./FutuOpenD &
```









A: First, switch to the directory where OpenD is located, configure
OpenD.xml, and then execute the following command.



``` text
nohup ./OpenD &
```















