



# <a href="#6986" class="header-anchor">#</a> Operation Command





You can do operate OpenD by sending Operation Command from the command
line or Telent.





You can do operate OpenD by sending Operation Command from the command
line or Telent.





Command format:
`cmd -param_key1=param_value1 -param_key2=param_value2`  
Using the following example to describe how to use Telnet:
`help -cmd=exit`

1.  Configure Telnet address and Telnet port in the OpenD set up
    parameter.
    ![telnet_GUI](/moomoo-api-doc/assets/img/telnet_GUI.0ac368ba.png)
    ![telnet_CMD](/moomoo-api-doc/assets/img/telnet_CMD.b0d3e174.jpg)
2.  Start OpenD (it will also start Telnet).
3.  Via Telnet，send the command `help -cmd=exit` to OpenD。



``` python
from telnetlib import Telnet
with Telnet('127.0.0.1', 22222) as tn:  # Telnet address is: 127.0.0.1, Telnet port is: 22222
    tn.write(b'help -cmd=exit\r\n')
    reply = b''
    while True:
        msg = tn.read_until(b'\r\n', timeout=0.5)
        reply += msg
        if msg == b'':
            break
    print(reply.decode('gb2312'))
```





### <a href="#5467" class="header-anchor">#</a> Command Help

`help -cmd=exit`

View the detailed information of the specified command, output the
command list if no parameter is specified

- Parameters:
  - cmd: command

### <a href="#629" class="header-anchor">#</a> Exit the Program

`Exit`





Exit OpenD





Exit OpenD





### <a href="#8890" class="header-anchor">#</a> Request Mobile Phone Verification Code

`req_phone_verify_code`

Requested mobile phone verification code. Security verification is
required when the device lock is enabled and the device is logged in at
the first time.

- Frequency limitations:
  - Maximal 1 request every 60 seconds

### <a href="#9904" class="header-anchor">#</a> Enter the Phone Verification Code

`Input_phone_verify_code -code=123456`

Enter the phone verification code and continue the login process.

- Parameters:

  - code: mobile phone verification code

- Frequency limitations:

  - Maximal 10 requests every 60 seconds

### <a href="#1508" class="header-anchor">#</a> Request Graphic Verification Code

`req_pic_verify_code`

Request a graphic verification code. When you enter the wrong login
password multiple times, you need to enter the graphic verification
code.

- Frequency limitations:
  - Maximal 10 requests every 60 seconds

### <a href="#7353" class="header-anchor">#</a> Enter Graphic Verification Code

`Input_pic_verify_code -code=1234`

Enter the graphic verification code and continue the login process.

- Parameters:

  - code: Graphic verification code

- Frequency limitations:

  - Maximal 10 requests every 60 seconds

### <a href="#1718" class="header-anchor">#</a> Relogin

`relogin -login_pwd=123456`

This command can be used when the user is required to log in again when
the login password is changed or the device lock is opened midway. You
can only relogin to the current account, and changing accounts is not
supported. The password parameter is mainly used to the situation that
the login password had been modified. If login_pwd is not set, the login
password at startup will be used.

- Parameters:

  - login_pwd: login password in plaintext

  - login_pwd_md5: login password in ciphertext (32-bit MD5 encrypted
    hexadecimal)

- Frequency limitations:

  - Maximal 10 requests every hour

### <a href="#4483" class="header-anchor">#</a> Time Delay Between Detection and Connection Point

`ping`

Delay before detection and connection point

- Frequency limitations:
  - Maximal 10 requests every 60 seconds





### <a href="#8217" class="header-anchor">#</a> Display Delay Statistics Report

`show_delay_report -detail_report_path=D:/detail.txt -push_count_type=sr2cs`

Display delay statistics report, including push delay, request delay and
order delay. Data is cleaned up at 6:00 Beijing time every day.

- Parameters:
  - detail_report_path: file output path (MAC system only supports
    absolute path, not relative path), optional parameter, if not
    specified, output to the console

  - push_count_type: the type of push delay (sr2ss, ss2cr, cr2cs, ss2cs,
    sr2cs), sr2cs by default.

    - sr refers to the server receiving time (currently only HK stocks
      support this time)
    - ss refers to the server sending time
    - cr refers to OpenD receiving time
    - cs refers to OpenD sending time





### <a href="#8217-2" class="header-anchor">#</a> Display Delay Statistics Report

`show_delay_report -detail_report_path=D:/detail.txt -push_count_type=sr2cs`

Display delay statistics report, including push delay, request delay and
order delay. Data is cleaned up at 6:00 Beijing time every day.

- Parameters:
  - detail_report_path: file output path (MAC system only supports
    absolute path, not relative path), optional parameter, if not
    specified, output to the console

  - push_count_type: the type of push delay (sr2ss, ss2cr, cr2cs, ss2cs,
    sr2cs), sr2cs by default.

    - sr refers to the server receiving time (currently only HK stocks
      support this time)
    - ss refers to the server sending time
    - cr refers to OpenD receiving time
    - cs refers to OpenD sending time





### <a href="#4483-2" class="header-anchor">#</a> Close API Connection

`close_api_conn -conn_id=123456`

Close an API connection, if not specified, close all connections

- Parameters:
  - conn_id: API connection ID

### <a href="#6886" class="header-anchor">#</a> Show Subscription Status

`show_sub_info -conn_id=123456 -sub_info_path=D:/detail.txt`

Display the subscription status of a connection, if not specified,
display all connections

- Parameters:
  - conn_id: API connection ID

  - sub_info_path: file output path (MAC system only supports absolute
    path, not relative path), optional parameter, if not specified,
    output to the console

### <a href="#1862" class="header-anchor">#</a> Request the Highest Quotation Permission

`request_highest_quote_right`

When the advanced quotation authority is occupied by other devices (such
as desktop/mobile terminal), you can use this command to request the
highest quotation authority again (And then, other devices that are
logged in will not be able to use advanced quote).

- Frequency limitations:
  - Maximal 10 requests every 60 seconds

### <a href="#63" class="header-anchor">#</a> Update

`update`

Update







