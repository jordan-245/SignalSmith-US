



# <a href="#6196" class="header-anchor">#</a> Visualization OpenD





OpenD provides two operation modes: visualization and command line. Here
is a description of Visualization OpenD which is relatively simple to
operate.

Please refer to [Command Line
FutuOpenD](/moomoo-api-doc/en/opend/opend-cmd.html) for more
informations for your interest.

## <a href="#6196-2" class="header-anchor">#</a> Visualization OpenD

### <a href="#1318" class="header-anchor">#</a> Step 1: Download

Visualization OpenD can be runned under 4 operating systems:
Windows、MacOS、CentOS、Ubuntu (Click to download).

- OpenD - <a
  href="https://www.futunn.com/download/fetch-lasted-link?name=opend-windows"
  target="_blank" rel="noopener noreferrer">Windows</a>、<a
  href="https://www.futunn.com/download/fetch-lasted-link?name=opend-macos"
  target="_blank" rel="noopener noreferrer">MacOS</a> 、<a
  href="https://www.futunn.com/download/fetch-lasted-link?name=opend-centos"
  target="_blank" rel="noopener noreferrer">CenOS</a> 、<a
  href="https://www.futunn.com/download/fetch-lasted-link?name=opend-ubuntu"
  target="_blank" rel="noopener noreferrer">Ubuntu</a>

### <a href="#9710" class="header-anchor">#</a> Step 2: Installation

- Extract the file and find the corresponding installation file to
  install OpenD.
- OpenD is installed in the `% appdata%` directory by default under
  Windows System.

### <a href="#8367" class="header-anchor">#</a> Step 3: Configuration

- The Visualization OpenD launch configuration is on the right side of
  the graphical interface, as shown in the following figure:

![ui-config](/moomoo-api-doc/assets/img/ui-config.034b704d.png)

**Configuration item list**：

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Configuration Item</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">IP</td>
<td style="text-align: left;">API listening IP address.

  


 

Option:<br />
&#10;127.0.0.1 (for local connections)
0.0.0.0 (for connections from all network cards)
or you can fill in the address of one of your network card



</td>
</tr>
<tr>
<td style="text-align: left;">Port</td>
<td style="text-align: left;">API listening port.</td>
</tr>
<tr>
<td style="text-align: left;">Log Level</td>
<td style="text-align: left;">Log level of OpenD.

  


 

Option:<br />
&#10;no (no log)
debug (the most detailed)
info (less detailed)



</td>
</tr>
<tr>
<td style="text-align: left;">Language</td>
<td style="text-align: left;">Language.

  


 

Option:<br />
&#10;Simplified Chinese
English



</td>
</tr>
<tr>
<td style="text-align: left;">Time Zone of Future Trade API</td>
<td style="text-align: left;">Specify the futures trading API time zone.

  


 

When trading API is called with futures accounts, the time involved is
in accordance with this parameter.



</td>
</tr>
<tr>
<td style="text-align: left;">Data Push Frequency</td>
<td style="text-align: left;">API subscription data push frequency
control.

  


 

In milliseconds.
Candlestick and Time Frame are not included.



</td>
</tr>
<tr>
<td style="text-align: left;">Telnet IP</td>
<td style="text-align: left;">Listening address of remote operation
command.</td>
</tr>
<tr>
<td style="text-align: left;">Telnet Port</td>
<td style="text-align: left;">Listening port of remote operation
command.</td>
</tr>
<tr>
<td style="text-align: left;">Encrypted Private Key</td>
<td style="text-align: left;">Absolute path of <a
href="/moomoo-api-doc/en/qa/other.html#1479">RSA</a> Encrypted Private
Key.</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket IP</td>
<td style="text-align: left;">WebSocket listening address.

  


 

Option:<br />
&#10;127.0.0.1 (for local connections)
0.0.0.0 (for connections from all network cards)



</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Port</td>
<td style="text-align: left;">WebSocket listening port.</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Certificate</td>
<td style="text-align: left;">WebSocket certificate file path.

  


 

If not configured, WebSocket is not enabled.
It needs to be configured with the private key at the same time.



</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Private Key</td>
<td style="text-align: left;">WebSocket certificate private key file
path.

  


 

The private key cannot be configured with a password.
If not configured, WebSocket is not enabled.
It needs to be configured at the same time with the certificate.



</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Authentication Key</td>
<td style="text-align: left;">Cipher text of key (32-bit MD5 encrypted
hexadecimal).

  


 

Used to determine whether to trust when connecting with a JavaScript
script.



</td>
</tr>
</tbody>
</table>



Tips

- Visual OpenD provides services by launching command line OpenD,
  interacted through WebSocket, so the WebSocket function must be
  started.

- To ensure safety of your trading accounts, if the listening address is
  not local, you must configure a private key to use the trading
  interface. The quote interface is not subject to this restriction.

- When the WebSocket listening address is not local, you need to
  configure SSL to start it, and a password should not be set during the
  certificate private key generation.

- Ciphertext is represented in hexadecimal after plaintext is encrypted
  by 32-bit MD5, which can be calculated by searching online MD5
  encryption (note that there may be a risk of records colliding with
  libraries calculated through third-party websites) or by downloading
  MD5 computing tools. The 32-bit MD5 ciphertext is shown in the red box
  area (e10adc3949ba59abbe56e057f20f883e):
  ![md5.png](data:image/png;base64,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)

- OpenD reads OpenD.xml in the same directory by default. On MacOS, due
  to the system protection mechanism, FutuOpenD.app will be assigned a
  random path at run time, so that the original path can not be found.
  At this point, there are the following methods:

  - Execute fixrun.sh under tar package
  - Specify the configuration file path with the command line parameter
    `-cfg_file`, as described below

- The log level defaults to the info level. During the system
  development phase, it is not recommended to close the log or modify
  the log to the warning, error, fatal level to prevent failure to
  locate problems.



### <a href="#4592" class="header-anchor">#</a> Step 4: Login

- Enter your account number and password to login.  
  You need to complete the questionnaire evaluation and agreement
  confirmation when you log in for the first time.  
  You can see your account information and [quote
  right](/moomoo-api-doc/en/intro/authority.html#5331), After logging in
  successfully.





OpenD provides two operation modes: visualization and command line. Here
is a description of Visualization OpenD which is relatively simple to
operate.

Please refer to [Command Line
OpenD](/moomoo-api-doc/en/opend/opend-cmd.html) for more informations
for your interest.

## <a href="#6196-3" class="header-anchor">#</a> Visualization OpenD

### <a href="#1318-2" class="header-anchor">#</a> Step 1: Download

Visualization OpenD can be runned under 4 operating systems:
Windows、MacOS、CentOS、Ubuntu.

- You can download through
  <a href="https://www.moomoo.com/download/OpenAPI" target="_blank"
  rel="noopener noreferrer">moomoo official website</a>
  ![download-page](/moomoo-api-doc/assets/img/download-mmpage.1bd01e90.png)

### <a href="#9710-2" class="header-anchor">#</a> Step 2: Installation

- Extract the file and find the corresponding installation file to
  install OpenD.
- OpenD is installed in the `% appdata%` directory by default under
  Windows System.

### <a href="#8367-2" class="header-anchor">#</a> Step 3: Configuration

- The Visualization OpenD launch configuration is on the right side of
  the graphical interface, as shown in the following figure:

![ui-config](/moomoo-api-doc/assets/img/mmui-config.0832084b.png)

**Configuration item list**：

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Configuration Item</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">IP</td>
<td style="text-align: left;">API listening IP address.

  


 

Option:<br />
&#10;127.0.0.1 (for local connections)
0.0.0.0 (for connections from all network cards)
or you can fill in the address of one of your network card



</td>
</tr>
<tr>
<td style="text-align: left;">Port</td>
<td style="text-align: left;">API listening port.</td>
</tr>
<tr>
<td style="text-align: left;">Log Level</td>
<td style="text-align: left;">Log level of OpenD.

  


 

Option:<br />
&#10;no (no log)
debug (the most detailed)
info (less detailed)



</td>
</tr>
<tr>
<td style="text-align: left;">Language</td>
<td style="text-align: left;">Language.

  


 

Option:<br />
&#10;Simplified Chinese
English



</td>
</tr>
<tr>
<td style="text-align: left;">Time Zone of Future Trade API</td>
<td style="text-align: left;">Specify the futures trading API time zone.

  


 

When trading API is called with futures accounts, the time involved is
in accordance with this parameter.



</td>
</tr>
<tr>
<td style="text-align: left;">Data Push Frequency</td>
<td style="text-align: left;">API subscription data push frequency
control.

  


 

In milliseconds.
Candlestick and Time Frame are not included.



</td>
</tr>
<tr>
<td style="text-align: left;">Telnet IP</td>
<td style="text-align: left;">Listening address of remote operation
command.</td>
</tr>
<tr>
<td style="text-align: left;">Telnet Port</td>
<td style="text-align: left;">Listening port of remote operation
command.</td>
</tr>
<tr>
<td style="text-align: left;">Encrypted Private Key</td>
<td style="text-align: left;">Absolute path of <a
href="/moomoo-api-doc/en/qa/other.html#1479">RSA</a> Encrypted Private
Key.</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket IP</td>
<td style="text-align: left;">WebSocket listening address.

  


 

Option:<br />
&#10;127.0.0.1 (for local connections)
0.0.0.0 (for connections from all network cards)



</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Port</td>
<td style="text-align: left;">WebSocket listening port.</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Certificate</td>
<td style="text-align: left;">WebSocket certificate file path.

  


 

If not configured, WebSocket is not enabled.
It needs to be configured with the private key at the same time.



</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Private Key</td>
<td style="text-align: left;">WebSocket certificate private key file
path.

  


 

The private key cannot be configured with a password.
If not configured, WebSocket is not enabled.
It needs to be configured at the same time with the certificate.



</td>
</tr>
<tr>
<td style="text-align: left;">WebSocket Authentication Key</td>
<td style="text-align: left;">Cipher text of key (32-bit MD5 encrypted
hexadecimal).

  


 

Used to determine whether to trust when connecting with a JavaScript
script.



</td>
</tr>
</tbody>
</table>



Tips

- Visual OpenD provides services by launching command line OpenD,
  interacted through WebSocket, so the WebSocket function must be
  started.

- To ensure safety of your trading accounts, if the listening address is
  not local, you must configure a private key to use the trading
  interface. The quote interface is not subject to this restriction.

- When the WebSocket listening address is not local, you need to
  configure SSL to start it, and a password should not be set during the
  certificate private key generation.

- Ciphertext is represented in hexadecimal after plaintext is encrypted
  by 32-bit MD5, which can be calculated by searching online MD5
  encryption (note that there may be a risk of records colliding with
  libraries calculated through third-party websites) or by downloading
  MD5 computing tools. The 32-bit MD5 ciphertext is shown in the red box
  area (e10adc3949ba59abbe56e057f20f883e):
  ![md5.png](data:image/png;base64,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)

- OpenD reads OpenD.xml in the same directory by default. On MacOS, due
  to the system protection mechanism, OpenD.app will be assigned a
  random path at run time, so that the original path can not be found.
  At this point, there are the following methods:

  - Execute fixrun.sh under tar package
  - Specify the configuration file path with the command line parameter
    `-cfg_file`, as described below

- The log level defaults to the info level. During the system
  development phase, it is not recommended to close the log or modify
  the log to the warning, error, fatal level to prevent failure to
  locate problems.



### <a href="#4592-2" class="header-anchor">#</a> Step 4: Login

- Enter your account number and password to login.  
  You need to complete the questionnaire evaluation and agreement
  confirmation when you log in for the first time.  
  You can see your account information and [quote
  right](/moomoo-api-doc/en/intro/authority.html#5331), After logging in
  successfully.











