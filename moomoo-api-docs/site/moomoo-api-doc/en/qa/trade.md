



# <a href="#2552" class="header-anchor">#</a> Transaction related

## <a href="#5987" class="header-anchor">#</a> Q1: How to use paper trading?





A:

### <a href="#6105" class="header-anchor">#</a> Overview

Paper trading is a simulation that allows you to practice trading
without the risk of using real money.

#### <a href="#7194" class="header-anchor">#</a> Trading time

Paper trading only supports trading during regular trading hours, and
does not support trading outside regular trading hours, US market
pre-market and after-hours, HK market and China A-shares market Opening
and Closing Auction. For details, please click
<a href="https://support.futunn.com/topic692?lang=en-US" target="_blank"
rel="noopener noreferrer">Rules of paper trading</a>.

#### <a href="#1909" class="header-anchor">#</a> Categories supported

For categories that OpenAPI supports by paper trading, please click
[here](/moomoo-api-doc/en/intro/intro.html#8029).

#### <a href="#5713" class="header-anchor">#</a> Unlock Trade

Different from live trading, you do not need to unlock the account to
place orders or modify or cancel orders when using paper trading.

#### <a href="#9947" class="header-anchor">#</a> Orders

1.  Order Types: limit order and market order.
2.  Modify Order Operation: Paper trading does not support enabling,
    disabling, and deleting the order, but supports modifying and
    canceling the order.
3.  Deals: Paper trading does not support deals related operations,
    including [Get today's
    deals](/moomoo-api-doc/en/trade/get-order-fill-list.html#9411), [Get
    historical
    deals](/moomoo-api-doc/en/trade/get-history-order-fill-list.html#6628),
    and [Respond to the transaction
    push](/moomoo-api-doc/en/trade/update-order-fill.html#4428).
4.  Valid Period: Paper trading only supports good for day order when
    setting valid period.
5.  Short Selling: Options and futures support short selling. Only US
    stocks support short selling.

#### <a href="#4499" class="header-anchor">#</a> Platform

1.  Mobile clients: Me — Paper Trading.

![sim-page](/moomoo-api-doc/assets/img/en-sim-page.8eac62e8.png)

2.  Desktop clients: Left side tab *Paper* .

![sim-page](/moomoo-api-doc/assets/img/en-create-sim-account.3ea1117c.png)

3.  Web clients:
    <a href="https://support.futunn.com/topic692?lang=en-US" target="_blank"
    rel="noopener noreferrer">Paper Trading Website</a>.

4.  OpenAPI: When calling the interface, set the parameter trading
    environment to the simulated environment. Click [How to use paper
    trading through OpenAPI](/moomoo-api-doc/en/qa/trade.html#4514) for
    detail.



Tips

- The four platforms shown above use the same paper trading accounts.



### <a href="#4514" class="header-anchor">#</a> How to use paper trading through OpenAPI?

#### <a href="#1897" class="header-anchor">#</a> Create Connection

Firstly, [create the corresponding
connection](/moomoo-api-doc/en/trade/base.html#8155). When the
underlyings are stocks or options, please use `OpenSecTradeContext`.
When the underlyings are futures, please use `OpenFutureTradeContext`.

#### <a href="#9665" class="header-anchor">#</a> Get the List of Trading Accounts

Use the interface [Get the List of Trading
Accounts](/moomoo-api-doc/en/trade/get-acc-list.html#9665) to view
trading accounts (including paper trading accounts and live trading
accounts). Take Python as an example: When the returned parameter
`trd_env` is `SIMULATE`, it means the corresponding account is a paper
trading account.





A:

### <a href="#6105-2" class="header-anchor">#</a> Overview

Paper trading is a simulation that allows you to practice trading
without the risk of using real money.

#### <a href="#7194-2" class="header-anchor">#</a> Trading time

Paper trading only supports trading during regular trading hours, and
does not support trading outside regular trading hours, US market
pre-market and after-hours, HK market and China A-shares market Opening
and Closing Auction. For details, please click <a
href="https://www.moomoo.com/us/support/topic3_15?from_platform=4&amp;lang=en-us"
target="_blank" rel="noopener noreferrer">Rules of paper trading</a>.

#### <a href="#1909-2" class="header-anchor">#</a> Categories supported

For categories that OpenAPI supports by paper trading, please click
[here](/moomoo-api-doc/en/intro/intro.html#8029).

#### <a href="#5713-2" class="header-anchor">#</a> Unlock Trade

Different from live trading, you do not need to unlock the account to
place orders or modify or cancel orders when using paper trading.

#### <a href="#9947-2" class="header-anchor">#</a> Orders

1.  Order Types: limit order and market order.
2.  Modify Order Operation: Paper trading does not support enabling,
    disabling, and deleting the order, but supports modifying and
    canceling the order.
3.  Deals: Paper trading does not support deals related operations,
    including [Get today's
    deals](/moomoo-api-doc/en/trade/get-order-fill-list.html#9411), [Get
    historical
    deals](/moomoo-api-doc/en/trade/get-history-order-fill-list.html#6628),
    and [Respond to the transaction
    push](/moomoo-api-doc/en/trade/update-order-fill.html#4428).
4.  Valid Period: Paper trading only supports good for day order when
    setting valid period.
5.  Short Selling: Options and futures support short selling. Only US
    stocks support short selling.

#### <a href="#4499-2" class="header-anchor">#</a> Platform

1.  Mobile clients: Me — Paper Trading.

![sim-page](/moomoo-api-doc/assets/img/en-sim-page.8eac62e8.png)

2.  Desktop clients: Left side tab *Paper* .

![sim-page](/moomoo-api-doc/assets/img/en-create-sim-account.3ea1117c.png)

3.  Web clients: <a
    href="https://www.moomoo.com/us/support/topic3_15?from_platform=4&amp;lang=en-us"
    target="_blank" rel="noopener noreferrer">Paper Trading Website</a>.

4.  OpenAPI: When calling the interface, set the parameter trading
    environment to the simulated environment. Click [How to use paper
    trading through OpenAPI](/moomoo-api-doc/en/qa/trade.html#4514-2)
    for detail.



Tips

- The four platforms shown above use the same paper trading accounts.



### <a href="#4514-2" class="header-anchor">#</a> How to use paper trading through OpenAPI?

#### <a href="#1897-2" class="header-anchor">#</a> Create Connection

Firstly, [create the corresponding
connection](/moomoo-api-doc/en/trade/base.html#8155). When the
underlyings are stocks or options, please use `OpenSecTradeContext`.
When the underlyings are futures, please use `OpenFutureTradeContext`.

#### <a href="#9665-2" class="header-anchor">#</a> Get the List of Trading Accounts

Use the interface [Get the List of Trading
Accounts](/moomoo-api-doc/en/trade/get-acc-list.html#9665) to view
trading accounts (including paper trading accounts and live trading
accounts). Take Python as an example: When the returned parameter
`trd_env` is `SIMULATE`, it means the corresponding account is a paper
trading account.









- **Example：Stocks and Options**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
#trd_ctx = OpenFutureTradeContext(host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_list()
if ret == RET_OK:
    print(data)
    print(data['acc_id'][0])  # get the first account id
    print(data['acc_id'].values.tolist())  # convert to list format
else:
    print('get_acc_list error: ', data)
trd_ctx.close()
```





- **Output**



``` python
               acc_id   trd_env acc_type          card_num   security_firm  \
0  281756480572583411      REAL   MARGIN  1001318721909873  FUTUSECURITIES   
1             9053218  SIMULATE     CASH               N/A             N/A   
2             9048221  SIMULATE   MARGIN               N/A             N/A   

  sim_acc_type  trdmarket_auth  
0          N/A  [HK, US, HKCC]  
1        STOCK            [HK]  
2       OPTION            [HK] 
```







Tips

- In paper trading, stock accounts and options accounts are
  distinguished. Stock accounts can only trade stocks, and options
  accounts can only trade options; take Python as an example:
  `sim_acc_type` in the returned field is `STOCK`, which means stock
  account; `OPTION` means option account.



- **Example: Futures**



``` python
from futu import *
#trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
trd_ctx = OpenFutureTradeContext(host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_list()
if ret == RET_OK:
    print(data)
    print(data['acc_id'][0])  # get the first account id
    print(data['acc_id'].values.tolist())  # convert to list format
else:
    print('get_acc_list error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    acc_id   trd_env acc_type card_num security_firm sim_acc_type  \
0  9497808  SIMULATE   MARGIN      N/A           N/A      FUTURES   
1  9497809  SIMULATE   MARGIN      N/A           N/A      FUTURES   
2  9497810  SIMULATE   MARGIN      N/A           N/A      FUTURES   
3  9497811  SIMULATE   MARGIN      N/A           N/A      FUTURES   

          trdmarket_auth  
0  [FUTURES_SIMULATE_HK]  
1  [FUTURES_SIMULATE_US]  
2  [FUTURES_SIMULATE_SG]  
3  [FUTURES_SIMULATE_JP]  
```





#### <a href="#3634" class="header-anchor">#</a> Place Orders

When using the Interface [Place
Orders](/moomoo-api-doc/en/trade/place-order.html), set the trading
environment to the simulated environment. Take Python as an example:
`trd_env = TrdEnv.SIMULATE`.

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.place_order(price=510.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE)
if ret == RET_OK:
    print(data)
else:
    print('place_order error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    code    stock_name  trd_side    order_type  order_status    order_id    qty price   create_time updated_time    dealt_qty   dealt_avg_price last_err_msg    remark  time_in_force   fill_outside_rth
0 HK.00700   Tencent BUY NORMAL  SUBMITTING  4642000476506964749   100.0 510.0 2021-10-09 11:34:54   2021-10-09 11:34:54   0.0   0.0           DAY N/A
```





#### <a href="#8129" class="header-anchor">#</a> Modify or Cancel Orders

When using the Interface [Modify or Cancel
Orders](/moomoo-api-doc/en/trade/modify-order.html), set the trading
environment to the simulated environment. Take Python as an example:
`trd_env = TrdEnv.SIMULATE`.

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
order_id = "4642000476506964749"
ret, data = trd_ctx.modify_order(ModifyOrderOp.CANCEL, order_id, 0, 0, trd_env=TrdEnv.SIMULATE)
if ret == RET_OK:
    print(data)
else:
    print('modify_order error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    trd_env             order_id
0  SIMULATE  4642000476506964749
```





#### <a href="#5974" class="header-anchor">#</a> Get Historical Orders

When using the Interface [Get Historical
Orders](/moomoo-api-doc/en/trade/get-history-order-list.html), set the
trading environment to the simulated environment. Take Python as an
example: `trd_env = TrdEnv.SIMULATE`.

- **Example**



``` python
from futu import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.history_order_list_query(trd_env=TrdEnv.SIMULATE)
if ret == RET_OK:
    print(data)
else:
    print('history_order_list_query error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    code    stock_name  trd_side    order_type  order_status    order_id    qty price   create_time updated_time    dealt_qty   dealt_avg_price last_err_msg    remark  time_in_force   fill_outside_rth
0 HK.00700   Tencent BUY ABSOLUTE_LIMIT  CANCELLED_ALL   4642000476506964749   100.0 510.0 2021-10-09 11:34:54   2021-10-09 11:37:08   0.0   0.0           DAY N/A
```





### <a href="#5939" class="header-anchor">#</a> How to reset the paper trading account?

Currently, OpenAPI does not support resetting the paper trading account.
You can use the reset card on the mobile clients. After the reset, net
assets would be restored to the initial value and the historical orders
would be emptied.

#### <a href="#3893" class="header-anchor">#</a> Specific process

Modify clients: Me — Paper Trading — My Icon — My Card — Reset Card
![sim-page](/moomoo-api-doc/assets/img/en-sim-reset.73ab8cdb.png)





- **Example: Stocks and Options**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
#trd_ctx = OpenFutureTradeContext(host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_list()
if ret == RET_OK:
    print(data)
    print(data['acc_id'][0])  # get the first account id
    print(data['acc_id'].values.tolist())  # convert to list format
else:
    print('get_acc_list error: ', data)
trd_ctx.close()
```





- **Output**



``` python
               acc_id   trd_env acc_type          card_num   security_firm  \
0  281756480572583411      REAL   MARGIN  1001318721909873  FUTUSECURITIES   
1             9053218  SIMULATE     CASH               N/A             N/A   
2             9048221  SIMULATE   MARGIN               N/A             N/A   

  sim_acc_type  trdmarket_auth  
0          N/A  [HK, US, HKCC]  
1        STOCK            [HK]  
2       OPTION            [HK] 
```







Tips

- In paper trading, stock accounts and options accounts are
  distinguished. Stock accounts can only trade stocks, and options
  accounts can only trade options; take Python as an example:
  `sim_acc_type` in the returned field is `STOCK`, which means stock
  account; `OPTION` means option account.



- **Example: Futures**



``` python
from moomoo import *
#trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
trd_ctx = OpenFutureTradeContext(host='127.0.0.1', port=11111, is_encrypt=None, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_list()
if ret == RET_OK:
    print(data)
    print(data['acc_id'][0])  # get the first account id
    print(data['acc_id'].values.tolist())  # convert to list format
else:
    print('get_acc_list error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    acc_id   trd_env acc_type card_num security_firm sim_acc_type  \
0  9497808  SIMULATE   MARGIN      N/A           N/A      FUTURES   
1  9497809  SIMULATE   MARGIN      N/A           N/A      FUTURES   
2  9497810  SIMULATE   MARGIN      N/A           N/A      FUTURES   
3  9497811  SIMULATE   MARGIN      N/A           N/A      FUTURES   

          trdmarket_auth  
0  [FUTURES_SIMULATE_HK]  
1  [FUTURES_SIMULATE_US]  
2  [FUTURES_SIMULATE_SG]  
3  [FUTURES_SIMULATE_JP]  
```





#### <a href="#3634-2" class="header-anchor">#</a> Place Orders

When using the interface [Place
Orders](/moomoo-api-doc/en/trade/place-order.html), set the trading
environment to the simulated environment. Take Python as an example:
`trd_env = TrdEnv.SIMULATE`.

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.place_order(price=510.0, qty=100, code="HK.00700", trd_side=TrdSide.BUY, trd_env=TrdEnv.SIMULATE)
if ret == RET_OK:
    print(data)
else:
    print('place_order error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    code    stock_name  trd_side    order_type  order_status    order_id    qty price   create_time updated_time    dealt_qty   dealt_avg_price last_err_msg    remark  time_in_force   fill_outside_rth
0 HK.00700   Tencent BUY NORMAL  SUBMITTING  4642000476506964749   100.0 510.0 2021-10-09 11:34:54   2021-10-09 11:34:54   0.0   0.0           DAY N/A
```





#### <a href="#8129-2" class="header-anchor">#</a> Modify or Cancel Orders

When using the Interface [Modify or Cancel
Orders](/moomoo-api-doc/en/trade/modify-order.html), set the trading
environment to the simulated environment. Take Python as an example:
`trd_env = TrdEnv.SIMULATE`.

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
order_id = "4642000476506964749"
ret, data = trd_ctx.modify_order(ModifyOrderOp.CANCEL, order_id, 0, 0, trd_env=TrdEnv.SIMULATE)
if ret == RET_OK:
    print(data)
else:
    print('modify_order error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    trd_env             order_id
0  SIMULATE  4642000476506964749
```





#### <a href="#5974-2" class="header-anchor">#</a> Get Historical Orders

When using the Interface [Get Historical
Orders](/moomoo-api-doc/en/trade/get-history-order-list.html), set the
trading environment to the simulated environment. Take Python as an
example: `trd_env = TrdEnv.SIMULATE`.

- **Example**



``` python
from moomoo import *
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.history_order_list_query(trd_env=TrdEnv.SIMULATE)
if ret == RET_OK:
    print(data)
else:
    print('history_order_list_query error: ', data)
trd_ctx.close()
```





- **Output**



``` python
    code    stock_name  trd_side    order_type  order_status    order_id    qty price   create_time updated_time    dealt_qty   dealt_avg_price last_err_msg    remark  time_in_force   fill_outside_rth
0 HK.00700   Tencent BUY ABSOLUTE_LIMIT  CANCELLED_ALL   4642000476506964749   100.0 510.0 2021-10-09 11:34:54   2021-10-09 11:37:08   0.0   0.0           DAY N/A
```





### <a href="#5939-2" class="header-anchor">#</a> How to reset the paper trading account?

Currently, OpenAPI does not support resetting the paper trading account.
You can use the reset card on the mobile clients. After the reset, net
assets would be restored to the initial value and the historical orders
would be emptied.

#### <a href="#3893-2" class="header-anchor">#</a> Specific process

Modify clients: Me — Paper Trading — My Icon — My Card — Reset Card
![sim-page](/moomoo-api-doc/assets/img/en-sim-reset.73ab8cdb.png)





### <a href="#5939-3" class="header-anchor">#</a> How to reset the paper trading account?

Currently, OpenAPI does not support resetting the paper trading account.
You can use the reset card on the mobile clients. After the reset, net
assets would be restored to the initial value and the historical orders
would be emptied.

#### <a href="#3893-3" class="header-anchor">#</a> Specific process

Modify clients: Me — Paper Trading — My Icon — My Card — Reset Card
![sim-page](/moomoo-api-doc/assets/img/en-sim-reset.73ab8cdb.png)

## <a href="#7290" class="header-anchor">#</a> Q2: If support A-share trading or not?

A: Paper trading supports A-share trading. However, real trade can only
be used to trade some A-shares through A-shares connect. For details,
please refer to <a
href="https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities?sc_lang=en"
target="_blank" rel="noopener noreferrer">List of HKCC</a>.

## <a href="#2916" class="header-anchor">#</a> Q3: Trading directions supported by each market

A: Except for futures, other stocks only support the two trading
directions of BUY and SELL. In the case of a short position, SELL is
passed in, and the direction of the resulting order is short selling.

## <a href="#7467" class="header-anchor">#</a> Q4: Order types supported in each market in real environment

A:

<table style="font-size:14px;">
<thead>
<tr>
<th>Market</th>
<th>Variety</th>
<th>Limit Orders</th>
<th>Market Orders</th>
<th>At-auction Limit Orders</th>
<th>At-auction Market Orders</th>
<th>Absolute Limit Orders</th>
<th>Special Limit Orders</th>
<th>AON Special Limit Orders</th>
<th>Stop Orders</th>
<th>Stop Limit Orders</th>
<th>Market if Touched Orders</th>
<th>Limit if Touched Orders</th>
<th>Trailing Stop Orders</th>
<th>Trailing Stop Limit Orders</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">HK</td>
<td>Securities (including stocks, ETFs, warrants, CBBCs, Inline
Warrants)</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td>Options</td>
<td>✓</td>
<td>X</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>X</td>
<td>✓</td>
<td>X</td>
<td>✓</td>
<td>X</td>
<td>✓</td>
</tr>
<tr>
<td>Futures</td>
<td>✓</td>
<td>✓</td>
<td>-</td>
<td>✓</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td rowspan="3">US</td>
<td>Securities (including stocks, ETFs)</td>
<td>✓</td>
<td>✓</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td>Options</td>
<td>✓</td>
<td>✓</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td>Futures</td>
<td>✓</td>
<td>✓</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td>HKCC</td>
<td>Securities (including stocks, ETFs)</td>
<td>✓</td>
<td>X</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>X</td>
<td>✓</td>
<td>X</td>
<td>✓</td>
<td>X</td>
<td>✓</td>
</tr>
<tr>
<td>Singapore</td>
<td>Futures</td>
<td>✓</td>
<td>✓</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
<tr>
<td>Japanese</td>
<td>Futures</td>
<td>✓</td>
<td>✓</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
</tr>
</tbody>
</table>

## <a href="#179" class="header-anchor">#</a> Q5: Order operations supported by each market

A:

- HK stocks support order modification, cancellation, entry into force,
  invalidation, and deletion
- US stocks only support order modification and cancellation
- HKCC only supports cancellation of orders
- Futures supports order modification, cancellation, and deletion

## <a href="#2794" class="header-anchor">#</a> Q6: How to use OpenD startup parameter future_trade_api_time_zone?

A: Since the types of futures supported for trading account are
distributed in multiple exchanges around the world, and the time zones
of the exchanges are different, the time display of the futures trading
API has become a problem. The future_trade_api_time_zone parameter has
been added to the OpenD startup parameters, allowing futures traders in
different regions of the world to flexibly specify the time zone. The
default time zone is UTC+8. If you are more accustomed to Eastern Time,
you only need to configure this parameter to UTC-5.



Tips

- This parameter is only valid for futures trading interface objects.
  The time zone of HK stock trading, US stock trading, and HKCC trading
  interface objects is still displayed in accordance with the time zone
  of the exchange.
- The interfaces affected by this parameter include: responding to order
  push callbacks, responding to transaction push callbacks, querying
  today's orders, querying historical orders, querying current
  transactions, querying historical transactions, and placing orders.



## <a href="#7900" class="header-anchor">#</a> Q7: Can I see the order placed through OpenAPI, in APP?

A：Yes, you can.  
After the order is successfully placed through OpenAPI, you can view
today's orders, order status change in the trade page of APP, and you
can also receive **Order Notice** in the APP.





![download-page](/moomoo-api-doc/assets/img/download-page.01238e55.png)





![download-page](/moomoo-api-doc/assets/img/download-mmpage.1bd01e90.png)





## <a href="#6327" class="header-anchor">#</a> Q8: Which trading targets support Off-Market order?

A：All orders can only be filled during the market opening period.  
Orders made outside market hours and extended hours trading are queued
and fulfilled either at or near the beginning of extended hours trading
or at or near the market open, according to your instructions. These
orders may be named as off market orders or overnight order. OpenAPI
supports Off-Market order for a part of trading targets (APP supports
much more trading targets' Off-Market order), as follows:

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th>Market</th>
<th>Contracts</th>
<th>Paper Trading</th>
<th colspan="4">Live Trading</th>
</tr>
</thead>
<tbody>
<tr>
<th>FUTU HK</th>
<th>Moomoo Financial Inc.</th>
<th>Moomoo Financial Singapore Pte. Ltd.</th>
<th>FUTU AU</th>
<th></th>
<th></th>
<th></th>
</tr>
&#10;<tr>
<td rowspan="3">HK Market</td>
<td>Securities<br />
(including stocks, ETFs, warrants, CBBCs, Inline Warrants)</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Options</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="3">US Market</td>
<td>Securities (including stocks, ETFs)</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Options</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="2">A-share Market</td>
<td>HKCC stocks</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Non-HKCC stocks</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Singapore Market</td>
<td>Futures</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Japanese Market</td>
<td>Futures</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
</tbody>
</table>



Tip

- ✓：support Off-Market order
- X：do not support Off-Market order（or non-tradable）



## <a href="#8229" class="header-anchor">#</a> Q9: For each order type，mandatory parameters of PlaceOrder and broker limits for the single order.

A1: Mandatory parameters of PlaceOrder.

| Parameters | Limit Orders | Market Orders | At-auction Limit Orders | At-auction Market Orders | Absolute Limit Orders | Special Limit Orders | AON Special Limit Orders | Stop Orders | Stop Limit Orders | Market if Touched Orders | Limit if Touched Orders | Trailing Stop Orders | Trailing Stop Limit Orders |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| price | ✓ |  | ✓ |  | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |  |  |
| qty | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| code | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| trd_side | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| order_type | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| trd_env | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| aux_price |  |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |
| trail_type |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |
| trail_value |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |
| trail_spread |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |

`Python users` should note that,
[place_order](/moomoo-api-doc/en/trade/place-order.html) does not set a
default value for price. For the five types of orders mentioned above,
you still need to pass in price, which can be any value.

A2: The broker sets limits on shares or amounts for single orders of
various trading products. Exceeding these limits may result in order
failures. See the table below for details.

<table style="font-size:14px;">
<thead>
<tr>
<th>Broker</th>
<th>Product</th>
<th>Quantity Limit Per Order</th>
<th>Amount Limit Per Order</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="3">FUTU HK</td>
<td>China A-Shares</td>
<td>1,000,000 Shares</td>
<td>￥5,000,000</td>
</tr>
<tr>
<td>US Stocks</td>
<td>500,000 Shares</td>
<td>$5,000,000</td>
</tr>
<tr>
<td>Hong Kong Stock Futures or Options</td>
<td>3,000 Contracts</td>
<td>Unlimited</td>
</tr>
<tr>
<td>moomoo US</td>
<td>US Stocks</td>
<td>500,000 Shares</td>
<td>$10,000,000</td>
</tr>
<tr>
<td>moomoo SG</td>
<td>US Stocks</td>
<td>500,000 Shares</td>
<td>$5,000,000</td>
</tr>
<tr>
<td>moomoo AU</td>
<td>US Stocks</td>
<td>Unlimited</td>
<td>Unlimited</td>
</tr>
</tbody>
</table>

## <a href="#2440" class="header-anchor">#</a> Q10: For each order type, when modifying the order, mandatory parameters of ModifyOrder as follows.

| Parameters | Limit Orders | Market Orders | At-auction Limit Orders | At-auction Market Orders | Absolute Limit Orders | Special Limit Orders | AON Special Limit Orders | Stop Orders | Stop Limit Orders | Market if Touched Orders | Limit if Touched Orders | Trailing Stop Orders | Trailing Stop Limit Orders |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| modify_order_op | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| order_id | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| price | ✓ |  | ✓ |  | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |  |  |
| qty | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| trd_env | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| aux_price |  |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |
| trail_type |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |
| trail_value |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |
| trail_spread |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |

`Python users` should note that,
[modify_order](/moomoo-api-doc/en/trade/modify-order.html) does not set
a default value for price. For the five types of orders mentioned above,
you still need to pass in price, which can be any value.

## <a href="#5049" class="header-anchor">#</a> Q11: The Trade API returns "The current securities account has not yet agreed to the disclaimer."?

A:  
Click the link below to confirm the agreement, and restart OpenD to use
trading functions normally.

| Securities Firm | Aggrement Link |
|:---|:---|
| FUTU HK | <a href="https://risk-disclosure.futuhk.com/index?agreementNo=HKOT0015"
target="_blank" rel="noopener noreferrer">Click here</a> |
| Moomoo US | <a
href="https://risk-disclosure.us.moomoo.com/index?agreementNo=USOT0027"
target="_blank" rel="noopener noreferrer">Click here</a> |
| Moomoo SG | <a
href="https://risk-disclosure.sg.moomoo.com/index?agreementNo=SGOT0015"
target="_blank" rel="noopener noreferrer">Click here</a> |
| Moomoo AU | <a
href="https://risk-disclosure.au.moomoo.com/index?agreementNo=AUOT0025"
target="_blank" rel="noopener noreferrer">Click here</a> |

## <a href="#3037" class="header-anchor">#</a> Q12: Pattern Day Trader (PDT)

### <a href="#6105-3" class="header-anchor">#</a> Overview





When clients use Moomoo US accounts for intraday trading, they are
subject to regulations by the US Financial Industry Regulatory Authority
(FINRA). This is a regulatory requirement for US brokers and has nothing
to do with the market to which a stock being traded belongs. The trading
accounts of brokers in other countries or regions, such as Futu HK and
Moomoo SG accounts, are not subject to this restriction. If a client
conducts over 3 day trades in any 5 consecutive trading days, the client
will be labelled as a pattern day trader (PDT).  
For more details, refer to
<a href="https://fastsupport.fututrade.com/hans/category11014/scid11017"
target="_blank" rel="noopener noreferrer">Help Center - Day Trade
Rules</a>.

### <a href="#3600" class="header-anchor">#</a> Day Trading Flowchart

![PDT_process](/moomoo-api-doc/assets/img/PDT_process.50477bd9.png)

### <a href="#7522" class="header-anchor">#</a> How to turn off "Pattern Day Trade Protection", if I'm willing to be labelled as a PDT and do not want the quant trading program to be interrupted?

A:  
To prevent you from being unintentionally labelled as a PDT, the server
will automatically intercept your 4th day trade in any 5 consecutive
trading days. If you are willing to be labelled as a PDT and do not want
the server to intercept your trade, you can take the following step:  
Via [Command Line OpenD](/moomoo-api-doc/en/opend/opend-cmd.html),
modify the value of the startup parameter "pdt_protection" to "0".

![US_para](/moomoo-api-doc/assets/img/US_para.cb012764.png) NOTE: You
will not be able to establish new positions when you are labelled as a
PDT and your account equity is below \$25000.





When clients use moomoo US accounts for intraday trading, they are
subject to regulations by the US Financial Industry Regulatory Authority
(FINRA). This is a regulatory requirement for US brokers and has nothing
to do with the market to which a stock being traded belongs. The trading
accounts of brokers in other countries or regions, such as moomoo HK and
moomoo SG accounts, are not subject to this restriction. If a client
conducts over 3 day trades in any 5 consecutive trading days, the client
will be labelled as a pattern day trader (PDT).  
For more details, refer to <a
href="https://www.moomoo.com/us/support/topic4_5?from_platform=4&amp;lang=en-us"
target="_blank" rel="noopener noreferrer">Help Center - Day Trade
Rules</a>.

### <a href="#3600-2" class="header-anchor">#</a> Day Trading Flowchart

![PDT_process](/moomoo-api-doc/assets/img/PDT_process.50477bd9.png)

### <a href="#7522-2" class="header-anchor">#</a> How to turn off "Pattern Day Trade Protection", if I'm willing to be labelled as a PDT and do not want the quant trading program to be interrupted?

A:  
To prevent you from being unintentionally labelled as a PDT, the server
will automatically intercept your 4th day trade in any 5 consecutive
trading days. If you are willing to be labelled as a PDT and do not want
the server to intercept your trade, you can take the following step:  
Via [Command Line OpenD](/moomoo-api-doc/en/opend/opend-cmd.html),
modify the value of the startup parameter "pdt_protection" to "0".

![US_para](/moomoo-api-doc/assets/img/us_mmpara.def79740.png) NOTE: You
will not be able to establish new positions when you are labelled as a
PDT and your account equity is below \$25000.





### <a href="#6811" class="header-anchor">#</a> How to turn off the Day-Trading Call Warning?

A:  
Once you are labelled as a PDT, you need to pay attention to the day
trading buying power (DTBP) of your account. When the DTBP is
insufficient, you will receive a DTCall. The server will intercept your
order that exceeds the DTBP. If you still want to place the order and do
not want the server to intercept it, you can take the following step:  
Via [Command Line OpenD](/moomoo-api-doc/en/opend/opend-cmd.html),
modify the value of the startup parameter "dtcall_confirmation" to "0".

![US_para2](/moomoo-api-doc/assets/img/US_para2.01f6f10b.png) NOTE: If
the market value of a newly established position exceeds your remaining
DTBP and you close the position in the same day, you will receive a
DTCall, which can only be met by depositing funds.

### <a href="#7143" class="header-anchor">#</a> How to check my DTBP?

A:  
Via [Get Account Funds
Interface](/moomoo-api-doc/en/trade/get-funds.html), you can request
values related to day trading, such as Day Trades Left, Beginning DTBP,
Remaining DTBP, etc.

## <a href="#1647" class="header-anchor">#</a> Q13: How to track the status of orders?

A:  
The two interfaces can be uesed to track the status of orders, after
which have been placed.

| Trading Enviroment | Interfaces |
|----|----|
| Real | [Orders Push Callback](/moomoo-api-doc/en/trade/update-order.html), [Deals Push Callback](/moomoo-api-doc/en/trade/update-order-fill.html) |
| Simulate | [Orders Push Callback](/moomoo-api-doc/en/trade/update-order.html) |

Note: Non-python users need to [Subscribe to Transaction
Push](/moomoo-api-doc/en/trade/sub-acc-push.html) before using the above
two interfaces.

#### <a href="#3884" class="header-anchor">#</a> Orders Push Callback:

Feedback changes of the entire order. The order push will be triggered
when the following 8 fields change:  
`Order status`, `Order price`, `Order quantity`, `Deal quantity`,
`Traget price`, `Trailing type`, `Trailing amount/ratio`,
`Specify spread`

Therefore, when you place, modify, cancel, enable, or disable the order,
or when an advanced order is triggered or an order has transaction
changes, it will cause orders push. You just need to call the [Orders
Push Callback](/moomoo-api-doc/en/trade/update-order.html) to listen for
these messages.

#### <a href="#7454" class="header-anchor">#</a> Deals Push Callback:

Feedback changes of a transaction. The order push will be triggered when
the following field change:  
`Deal status`

Fot example: Suppose a limit order of 900 shares is divided into 3
transactions before it is completely filled, with each transaction being
200, 300 and 400 shares.
![example](/moomoo-api-doc/assets/img/example.d9e2bccb.png)

## <a href="#8970" class="header-anchor">#</a> Q14: Why does the order interface return “The minimum tick size for this product is xxx. Please enter an integer multiple of the minimum tick size before submitting”?

A:  
Different exchanges have different rules on order price spreads. If the
price of a submitted order does not follow relevant rules, the order
will be rejected.

### <a href="#2248" class="header-anchor">#</a> Rules on Price Spread

#### <a href="#3030" class="header-anchor">#</a> Hong Kong Market





Refer to the official
<a href="https://www.futufin.com/en/support/topic605?lang=en-us"
target="_blank" rel="noopener noreferrer">HKEX Spread Table</a>





Refer to the official
<a href="https://www.moomoo.com/us/support/topic4_304?from_platform=4"
target="_blank" rel="noopener noreferrer">HKEX Spread Table</a>





#### <a href="#4862" class="header-anchor">#</a> China A-Shares

Stock price spread: 0.01

#### <a href="#4151" class="header-anchor">#</a> US Market

Stock Price Spreads:

| Price        | Spread   |
|--------------|----------|
| Below \$1    | \$0.0001 |
| \$1 or above | \$0.01   |

Option Price Spreads:

| Price           | Spread           |
|-----------------|------------------|
| \$0.10 - \$3.00 | \$0.01 or \$0.05 |
| \$3.00+         | \$0.05 or \$0.10 |

Futures Price Spreads:  
Different contracts have different price spreads, which can be obtained
via the `Price change step` of [Get Futures Contract
Information](/moomoo-api-doc/en/quote/get-future-info.html) interface.

### <a href="#5533" class="header-anchor">#</a> How to ensure an order price meets spread rules?

- Method 1: Valid order prices can be obtained via the [Get Real-time
  Order Book](/moomoo-api-doc/en/quote/get-order-book.html) interface,
  since the prices of orders on the order book must be valid.

- Method 2: Auto-adjust an order price to a valid value via the
  `Price adjustment range` parameter in the [Place
  Orders](/moomoo-api-doc/en/trade/place-order.html) interface.

  How it works:

  Suppose the Adjust Limit is set to 0.0015. A positive value means that
  OpenD will auto-adjust upward the price of a submitted order to a
  valid value within +0.15% of the original price.

  Suppose the current market price of Tencent Holdings is 359.600, so
  the spread is 0.200 according to the HKEX Spread Table. Let’s say an
  order priced at 359.678 is submitted. In this case, the nearest upward
  valid price is 359.800, which means the order price only needs to be
  adjusted by 0.034%. The adjustment satisfies the Adjust Limit, so the
  final price of the submitted order is 359.800.

  If the actual adjustment exceeds the Adjust Limit, OpenD will fail to
  auto-adjust the price, and the order submission will still return the
  error prompt "The minimum tick size for this product is xxx. Please
  enter an integer multiple of the minimum tick size before submitting".

## <a href="#1784" class="header-anchor">#</a> Q15: Why did it say "Insufficient Buying Power" when I place a market order with enough buying power in my account?

A:

### <a href="#370" class="header-anchor">#</a> Why it indicates insufficient buying power when you place a market order

- For the sake of risk management, the system poses a higher buying
  power coefficient on market orders. With the same order parameters, a
  market order takes up more buying power than a limit order.
- Depending on different product types and market conditions, the risk
  management system dynamically adjusts the buying power coefficient of
  market orders. Therefore, when placing a market order, if you
  calculate the maximum buyable quantity using your maximum buying
  power, you are likely to get an inaccurate result.

### <a href="#7871" class="header-anchor">#</a> How to get the correct buyable quantity

Instead of calculating it, you can obtain the correct buyable quantity
through the \[Query the Maximum Quantity that Can be Bought or Sold\]
(../trade/get-max-trd-qtys.html) API.

### <a href="#179-2" class="header-anchor">#</a> How to buy as much as possible

You can place a limit order at the BBO, instead of a market order. In
particular, the BBO means the best bid (or Bid 1) in the case of a sell
order, or the best ask (or Ask 1) for a buy order.

## <a href="#732" class="header-anchor">#</a> Q16: Why can't I see the API papper trading orders on the mobile app?

A:  
On all the mobile, desktop and website, the US stock paper trading
account has been upgraded from the **US Paper Trading Accounts** to the
**US Paper Trading Margin Accounts**.  
The OpenAPI has not yet been upgraded (planning phase). At present, only
the old US Paper Trading Account is available for use. Please note that
this old account cannot be displayed on other clients, so use it with
caution.

## <a href="#3463" class="header-anchor">#</a> Q17: Instructions for Using Trade API Parameters

### <a href="#687" class="header-anchor">#</a> 1. What is the Transaction Object?

Under your user ID, there is generally a margin universal account with
several sub-accounts (usually two, a univeral securities account and a
universal futures accoun; also a universal forex account if needed).
Some users or instituational clients may open multiple universal
accounts with multiple brokers.  
Creating a transaction object is the process of initially screening
sub-accounts.

- When calling get_acc_list using OpenSecTradeContext, only trading
  securities accounts will be returned.
- When calling get_acc_list using OpenFutureTradeContext, only trading
  futures accounts will be returned.

The `security_firm` is used to filter accounts belonging to the
corresponding securities firm, and the `filter_trdmarket` is used to
filter accounts with the corresponding trading market permissions.

#### <a href="#335" class="header-anchor">#</a> 1.1 security_firm

The brokers currently supported by OpenAPI are [as
follows](/moomoo-api-doc/en/trade/trade.html#9434).  
When calling get_acc_list, it will return the real account of the
securities firm corresponding to security_firm and all paper trading
accounts (paper trading has no concept of brokers, so no matter what
security_firm is passed, all paper trading accounts will be returned).  
The default value of security_firm is FUTUSECURITIES. You can leave this
parameter blank for FUTU HK accounts, but you need to modify this
parameter when you want to obtain accounts from other brokers.

- **Example 1**



``` python
trd_ctx = OpenSecTradeContext(security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.get_acc_list()
print(data)
```





- **Output**



``` python
               acc_id   trd_env acc_type      uni_card_num          card_num   security_firm sim_acc_type                  trdmarket_auth acc_status
0  281756478396547854      REAL   MARGIN  1001200163530138  1001369091153722  FUTUSECURITIES          N/A  [HK, US, HKCC, HKFUND, USFUND]     ACTIVE
1             3450309  SIMULATE     CASH               N/A               N/A             N/A        STOCK                            [HK]     ACTIVE
2             3548731  SIMULATE   MARGIN               N/A               N/A             N/A       OPTION                            [HK]     ACTIVE
3  281756455998014447      REAL   MARGIN               N/A  1001100320482767  FUTUSECURITIES          N/A                            [HK]   DISABLED
```





- **Example 2**



``` python
trd_ctx = OpenSecTradeContext(security_firm=SecurityFirm.FUTUSG)
ret, data = trd_ctx.get_acc_list()
print(data)
```





- **Output**



``` python
    acc_id   trd_env acc_type uni_card_num card_num security_firm sim_acc_type trdmarket_auth acc_status
0  3450309  SIMULATE     CASH          N/A      N/A           N/A        STOCK           [HK]     ACTIVE
1  3548731  SIMULATE   MARGIN          N/A      N/A           N/A       OPTION           [HK]     ACTIVE
```





#### <a href="#5971" class="header-anchor">#</a> 1.2 filter_trdmarket

The trading markets supported by OpenAPI are [as
follows](/moomoo-api-doc/en/trade/trade.html#6257).  
When calling get_acc_list, it will return all accounts with trading
permissions in the filter_trdmarket market; when the filter_trdmarket is
passed as NONE, the market will not be filtered and all accounts will be
returned.  
The default trdmarket is HK. Under the universal account system, this
parameter is used to filter paper trading accounts in different markets.

- **Example 1**



``` python
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US)
ret, data = trd_ctx.get_acc_list()
print(data)
```





- **Output**



``` python
               acc_id   trd_env acc_type      uni_card_num          card_num   security_firm sim_acc_type                  trdmarket_auth acc_status
0  281756478396547854      REAL   MARGIN  1001200163530138  1001369091153722  FUTUSECURITIES          N/A  [HK, US, HKCC, HKFUND, USFUND]     ACTIVE
1             3450310  SIMULATE   MARGIN               N/A               N/A             N/A        STOCK                            [US]     ACTIVE
2             3548732  SIMULATE   MARGIN               N/A               N/A             N/A       OPTION                            [US]     ACTIVE
3  281756460292981743      REAL   MARGIN               N/A  1001100520714263  FUTUSECURITIES          N/A                            [US]   DISABLED
```





- **Example 2**



``` python
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.NONE)
ret, data = trd_ctx.get_acc_list()
print(data)
```





- **Output**



``` python
                acc_id   trd_env acc_type      uni_card_num          card_num   security_firm sim_acc_type                  trdmarket_auth acc_status
0   281756478396547854      REAL   MARGIN  1001200163530138  1001369091153722  FUTUSECURITIES          N/A  [HK, US, HKCC, HKFUND, USFUND]     ACTIVE
1              3450309  SIMULATE     CASH               N/A               N/A             N/A        STOCK                            [HK]     ACTIVE
2              3450310  SIMULATE   MARGIN               N/A               N/A             N/A        STOCK                            [US]     ACTIVE
3              3450311  SIMULATE     CASH               N/A               N/A             N/A        STOCK                            [CN]     ACTIVE
4              3548732  SIMULATE   MARGIN               N/A               N/A             N/A       OPTION                            [US]     ACTIVE
5              3548731  SIMULATE   MARGIN               N/A               N/A             N/A       OPTION                            [HK]     ACTIVE
6   281756455998014447      REAL   MARGIN               N/A  1001100320482767  FUTUSECURITIES          N/A                            [HK]   DISABLED
7   281756460292981743      REAL   MARGIN               N/A  1001100520714263  FUTUSECURITIES          N/A                            [US]   DISABLED
8   281756468882916335      REAL   MARGIN               N/A  1001100610464507  FUTUSECURITIES          N/A                          [HKCC]   DISABLED
9   281756507537621999      REAL     CASH               N/A  1001100910390035  FUTUSECURITIES          N/A                        [HKFUND]   DISABLED
10  281756550487294959      REAL     CASH               N/A  1001101010406844  FUTUSECURITIES          N/A                        [USFUND]   DISABLED
```







Tips

When the filter_trdmarket is passed NONE, all trading accounts will be
returned. Row 0 is the active real universal account, rows 1-5 are paper
trading accounts, and rows 6-10 are disabled real accounts which are all
single-market accounts, that have been replaced by the universal account
(row 0). However, historical orders and deals are still in these
disabled accounts, and you can query them via these accounts.  
There is no filter_trdmarket in the OpenFutureTradeContext, but
security_firm, which has the same function as that in
OpenSecTradeContext.



### <a href="#2511" class="header-anchor">#</a> 2. Trade API Parameters

When using specific trading API (such as place orders, get open orders),
the `trd_env`, `acc_index`and `acc_id` parameters will first filter and
confirm a unique account, and then implement the corresponding interface
function for this account.

![acc-select-en](/moomoo-api-doc/assets/img/acc-select-en.bb497618.png)



Summary

1.  Filter out real or paper trading accounts according to trd_env.
2.  Among the results, the account specified by acc_id is prioritized.
3.  If acc_id is 0, select the corresponding account through acc_index.
4.  Error: The specified acc_id does not exist, or the acc_index is out
    of range.



### <a href="#5004" class="header-anchor">#</a> 3. Examples

#### <a href="#2023" class="header-anchor">#</a> 3.1 Place Orders through Universal securities accounts



``` python
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.NONE, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.unlock_trade("123123")
if ret == RET_OK:
    print("unlock success!")
    ret, data = trd_ctx.place_order(45, 200, 'HK.00700', TrdSide.BUY,
                                    order_type=OrderType.NORMAL,
                                    trd_env=TrdEnv.REAL,
                                    acc_id=0)
    print(data)
```





#### <a href="#3265" class="header-anchor">#</a> 3.2 Get Open Orders through Universal futures accounts



``` python
trd_ctx = OpenFutureTradeContext(security_firm=SecurityFirm.FUTUSECURITIES)

ret, data = trd_ctx.order_list_query(trd_env=TrdEnv.REAL,
                                     acc_id=0)
print(data)
```





#### <a href="#2014" class="header-anchor">#</a> 3.3 Get Account Funds through HK Cash Account (Paper Trading)



``` python
# filter_trdmarket: TrdMarket.HK
# trd_env: TrdEnv.SIMULATE
# acc_index: 0
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.HK)
ret, data = trd_ctx.accinfo_query(trd_env=TrdEnv.SIMULATE, acc_index=0)
print(data)
```





#### <a href="#7105" class="header-anchor">#</a> 3.4 Trade Options through US Margin Account (Paper Trading)



``` python
# Only two accounts returned after filtering by filter_trdmarket and trd_env
# acc_index = 0: US Cash Account (Trading stocks)
# acc_index = 1: US Margin Account (Trading options)
# acc_index: 1
trd_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US)
ret, data = trd_ctx.place_order(10, 1, code="US.AAPL250618P550000",trd_side=TrdSide.BUY,
                                trd_env=TrdEnv.SIMULATE,
                                acc_index=1)
print(data)
```





#### <a href="#6874" class="header-anchor">#</a> 3.5 Query the Max Quantity that can be Bought or Sold through JP Futures Paper Trading



``` python
# Print the outcome of get_acc_list, the acc_id of JP Futures Paper Trading is 6271199
# Pass this acc_id when querying the max quantity that can be bought/sold
trd_ctx = OpenFutureTradeContext()
ret, data = trd_ctx.acctradinginfo_query(order_type=OrderType.NORMAL,
                                         price=5000,
                                         trd_env=TrdEnv.SIMULATE,
                                         acc_id=6271199,
                                         code="JP.NK225main")
print(data)
```





### <a href="#8659" class="header-anchor">#</a> 4. How to map the accounts in OpenAPI to those in the APP?

![card-app-en](/moomoo-api-doc/assets/img/card-app-en.24712374.png)  
The accounts on the APP only show the last 4-digits of the card
number.  
According to the result of
[get_acc_list](/moomoo-api-doc/en/trade/get-acc-list.html), the columns
uni_card_num and card_num, are corresponding to the card number of
Universal account and Single-market account (disabled), respectively.  
The account obtained in the API can be matched with that on the APP
through the last 4 digits of the card number.







