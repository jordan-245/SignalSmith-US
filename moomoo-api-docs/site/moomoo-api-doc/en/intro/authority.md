



# <a href="#3512" class="header-anchor">#</a> Authorities and Limitations

## <a href="#7200" class="header-anchor">#</a> Login Limitations

### <a href="#5755" class="header-anchor">#</a> Opening Accounts





You need to finish opening your trading accounts on Futubull APP, before
logging in to OpenAPI.





You need to finish opening your trading accounts on moomoo APP, before
logging in to OpenAPI.





### <a href="#7459" class="header-anchor">#</a> Compliance Confirmation





After the first login, you need to complete *API Questionnaire and
Agreements* before you can continue to use OpenAPI.
<a href="https://www.futunn.com/about/api-disclaimer?lang=en-US"
target="_blank" rel="noopener noreferrer">Click here</a> for Futubull users.





After the first login, you need to complete *API Questionnaire and
Agreements* before you can continue to use OpenAPI.
<a href="https://www.moomoo.com/about/api-disclaimer?lang=en-us"
target="_blank" rel="noopener noreferrer">Click here</a> for moomoo users.





## <a href="#7371" class="header-anchor">#</a> Quotation Data

There are several limitations for market quotation data as follow:

- **Quote Right** -- The authority to obtain the relevant market data.
- **Interface Frequency Limitations** -- Frequency limits of calling
  interfaces.
- **Subscription Quota** -- Number of real-time quotes subscribed at the
  same time.
- **Historical Candlestick Quota** -- The total number of subjects
  pulling the historical candlestick per 30 days.





### <a href="#5331" class="header-anchor">#</a> Quote Right

You need the corresponding permission to obtain data of each market
through OpenAPI. The permission of OpenAPI is not exactly the same as
that of APP. Different levels correspond to different time delay, order
book levels, and the permission to use the interface.

You need to buy a quotation card before you can obtain the quotation of
some varieties, the specific way to obtain is shown in the table below.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Market</th>
<th>Security Type</th>
<th style="text-align: left;">Quote Right Acquisition Method</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">HK Market</td>
<td>Securities (including stocks, ETFs, warrants, CBBCs, Inline
Warrants)</td>
<td rowspan="3" style="text-align: left;">* Chinese mainland customers:
LV2 market quotes for free. Purchase <a
href="https://qtcard.futunn.com/intro/sf?type=10&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">HK Stocks Advanced Full Market Quotes</a> for SF market
quotes<br />
* Non-Chinese mainland customers: LV1 market quotes for free. Purchase
<a
href="https://qtcard.futunn.com/intro/hklv2?type=1&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">HK stocks LV2 advanced market</a> for LV2 market quotes.
Purchase <a
href="https://qtcard.futunn.com/intro/sf?type=10&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">HK Stocks Advanced Full Market Quotes</a> for SF market
quotes</td>
</tr>
<tr>
<td>Indices</td>
</tr>
<tr>
<td>Plates</td>
</tr>
<tr>
<td>Options</td>
<td rowspan="2" style="text-align: left;">* Chinese mainland customers:
LV2 market quotes for free during promotion period.<br />
* Non-Chinese mainland customers: LV1 market quotes for free. Purchase
<a
href="https://qtcard.futunn.com/intro/hk-derivativeslv2?type=8&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">HK stock options futures LV2 advanced market</a> for LV2
market data</td>
</tr>
<tr>
<td>Futures</td>
</tr>
<tr>
<td rowspan="6">US Market</td>
<td>Securities (Covers NYSE, NYSE-American and Nasdaq listed equities,
ETFs)</td>
<td rowspan="2" style="text-align: left;">* Not shared with App market
data permissions. Purchase <a
href="https://qtcardfthk.futufin.com/intro/nasdaq-basic?type=12&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">Nasdaq Basic</a> for LV1 market quotes (basic quotes,
24H).<br />
* Not shared with App market data permissions. Purchase <a
href="https://qtcardfthk.futufin.com/intro/nasdaq-basic?type=18&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">Nasdaq Basic+TotalView</a> for LV2 market quotes (Full
Order Book for 24H trading).</td>
</tr>
<tr>
<td>Plates</td>
</tr>
<tr>
<td>OTC Securities</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
<tr>
<td>Options (Covers US stock options, US index options)</td>
<td style="text-align: left;">* Customers who meet the threshold

  


 

Threshold：Total assets greater than $3000.




: get LV1 market data for free<br />
* Customers who do not meet the threshold

  


 

Threshold：Total assets greater than $3000.




: Purchase <a
href="https://qtcardfthk.futufin.com/intro/api-usoption-realtime?type=16&amp;is_support_buy=1&amp;lang=en-us"
target="_blank">OPRA Options Real-time Quote</a> for LV1 market
data</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: left;">* For clients who have a futures account.

  


 

<ul>
<li>Supported by FUTU HK/Moomoo Financial Singapore Pte. Ltd.</li>
<li>Futures accounts do not supported by Moomoo Financial Inc.</li>
</ul>




<br />
For CME Group quotes

  


 

Covers quotes from CME, CBOT, NYMEX, COMEX




, please access the <a
href="https://qtcardfthk.futufin.com/intro/cme?type=30&amp;is_support_buy=1"
target="_blank">CME Group Futures LV2</a><br />
For CME quotes, please access the <a
href="%20https://qtcardfthk.futufin.com/intro/cme?type=31&amp;is_support_buy=1"
target="_blank">CME Futures LV2</a><br />
For CBOT quotes, please access the <a
href="https://qtcardfthk.futufin.com/intro/cme?type=32&amp;is_support_buy=1"
target="_blank">CBOT Futures LV2</a><br />
For NYMEX quotes, please access the <a
href="%20%20%20%20https://qtcardfthk.futufin.com/intro/cme?type=33&amp;is_support_buy=1"
target="_blank">NYMEX Futures LV2</a><br />
For NYMEX quotes, please access the <a
href="%20%20https://qtcardfthk.futufin.com/intro/cme?type=34&amp;is_support_buy=1"
target="_blank">COMEX Futures LV2</a><br />
<br />
* For clients who do not have a futures account: Unsupported.</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
<tr>
<td rowspan="3">A-share Market</td>
<td>Securities (including stocks, ETFs)</td>
<td rowspan="3" style="text-align: left;">* Chinese mainland customers:
LV1 market data for free.<br />
* Non-Chinese mainland customers/institutional customers:
Unsupported.</td>
</tr>
<tr>
<td>Indices</td>
</tr>
<tr>
<td>Plates</td>
</tr>
<tr>
<td>Singapore Market</td>
<td>Futures</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
<tr>
<td>Japanese Market</td>
<td>Futures</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
</tbody>
</table>





### <a href="#5331-2" class="header-anchor">#</a> Quote Right

You need the corresponding permission to obtain data of each market
through OpenAPI. The permission of OpenAPI is not exactly the same as
that of APP. Different levels correspond to different time delay, order
book levels, and the permission to use the interface.

You need to buy a quotation card before you can obtain the quotation of
some varieties, the specific way to obtain is shown in the table below.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Market</th>
<th>Security Type</th>
<th style="text-align: left;">Quote Right Acquisition Method</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">HK Market</td>
<td>Securities (including stocks, ETFs, warrants, CBBCs, Inline
Warrants)</td>
<td rowspan="3" style="text-align: left;">* Chinese mainland customers:
LV2 market quotes for free. Purchase <a
href="https://qtcard.moomoo.com/intro/sf?type=10&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">HK Stocks Advanced Full Market Quotes</a> for SF market
quotes<br />
* Non-Chinese mainland customers: LV1 market quotes for free. Purchase
<a
href="https://qtcard.moomoo.com/intro/hklv2?type=1&amp;clientlang=2&amp;is_support_buy=1"
target="_blank">HK stocks LV2 advanced market</a> for LV2 market quotes.
Purchase <a
href="https://qtcard.moomoo.com/intro/sf?type=10&amp;is_support_buy=1&amp;clientlang=2"
target="_blank">HK Stocks Advanced Full Market Quotes</a> for SF market
quotes</td>
</tr>
<tr>
<td>Indices</td>
</tr>
<tr>
<td>Plates</td>
</tr>
<tr>
<td>Options</td>
<td rowspan="2" style="text-align: left;">* Chinese mainland customers:
LV2 market quotes for free during promotion period.<br />
* Non-Chinese mainland customers: LV1 market quotes for free. Purchase
<a
href="https://qtcard.moomoo.com/intro/hklv2-derivativeslv2?type=9&amp;is_support_buy=1&amp;clientlang=2"
target="_blank">HK stock options futures LV2 advanced market</a> for LV2
market data</td>
</tr>
<tr>
<td>Futures</td>
</tr>
<tr>
<td rowspan="6">US Market</td>
<td>Securities (Covers NYSE, NYSE-American and Nasdaq listed equities,
ETFs)</td>
<td rowspan="2" style="text-align: left;">* Not shared with App market
data permissions. Purchase <a
href="https://qtcard.moomoo.com/intro/nasdaq-basic?type=12&amp;is_support_buy=1"
target="_blank">Nasdaq Basic</a> for LV1 market quotes (basic quotes,
24H).<br />
* Not shared with App market data permissions. Purchase <a
href="https://qtcard.moomoo.com/intro/nasdaq-basic?type=18&amp;is_support_buy=1"
target="_blank">Nasdaq Basic+TotalView</a> for LV2 market quotes (Full
Order Book for 24H trading).</td>
</tr>
<tr>
<td>Plates</td>
</tr>
<tr>
<td>OTC Securities</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
<tr>
<td>Options (Covers US stock options, US index options)</td>
<td style="text-align: left;">* Customers who meet the threshold

  


 

Threshold：
<ul>
<li>Total assets of HK and US stocks greater than $3000.</li>
<li>Have traded in HK and US stocks.</li>
</ul>




: get LV1 market data for free<br />
* Customers who do not meet the threshold

  


 

Threshold：
<ul>
<li>Total assets of HK and US stocks greater than $3000.</li>
<li>Have traded in HK and US stocks.</li>
</ul>




: Purchase <a
href="https://qtcard.moomoo.com/intro/api-usoption-realtime?type=16&amp;is_support_buy=1&amp;lang=en-us"
target="_blank">OPRA Options Real-time Quote</a> for LV1 market
data</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: left;">* For clients who have a futures account.

  


 

<ul>
<li>Supported by FUTU HK/Moomoo Financial Singapore Pte. Ltd.</li>
<li>Futures accounts do not supported by Moomoo Financial Inc.</li>
</ul>




<br />
For CME Group quotes

  


 

Covers quotes from CME, CBOT, NYMEX, COMEX




, please access the <a
href="https://qtcard.moomoo.com/intro/cme?type=30&amp;is_support_buy=1"
target="_blank">CME Group Futures LV2</a><br />
For CME quotes, please access the <a
href="%20%20%20https://qtcard.moomoo.com/intro/cme?type=31&amp;is_support_buy=1"
target="_blank">CME Futures LV2</a><br />
For CBOT quotes, please access the <a
href="https://qtcard.moomoo.com/intro/cme?type=32&amp;is_support_buy=1"
target="_blank">CBOT Futures LV2</a><br />
For NYMEX quotes, please access the <a
href="%20%20https://qtcard.moomoo.com/intro/cme?type=33&amp;is_support_buy=1"
target="_blank">NYMEX Futures LV2</a><br />
For NYMEX quotes, please access the <a
href="%20%20%20https://qtcard.moomoo.com/intro/cme?type=34&amp;is_support_buy=1"
target="_blank">COMEX Futures LV2</a><br />
<br />
* For clients who do not have a futures account: Unsupported.</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
<tr>
<td rowspan="3">A-share Market</td>
<td>Securities (including stocks, ETFs)</td>
<td rowspan="3" style="text-align: left;">* Chinese mainland customers:
LV1 market data for free.<br />
* Non-Chinese mainland customers/institutional customers:
Unsupported.</td>
</tr>
<tr>
<td>Indices</td>
</tr>
<tr>
<td>Plates</td>
</tr>
<tr>
<td>Singapore Market</td>
<td>Futures</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
<tr>
<td>Japanese Market</td>
<td>Futures</td>
<td style="text-align: left;">Unsupported.</td>
</tr>
</tbody>
</table>











Tips

In the above table, the Chinese mainland customers and the Non-Chinese
mainland customers are distinguished by the login IP address of OpenD.









Tips

In the above table, the Chinese mainland customers and the Non-Chinese
mainland customers are distinguished by the login IP address of OpenD.







### <a href="#8815" class="header-anchor">#</a> Interface Frequency Limitations





In order to protect the server from malicious attacks, there are
frequency limitations for all interfaces that need to send requests to
Futu servers. The frequency limitation rules for each API are different.
For more information, please see **Interface Limitations** at the bottom
of each API page.

Example:  
The limitation rule of [Get Market
Snapshot](/moomoo-api-doc/en/quote/get-market-snapshot.html) is: A
maximum of 60 requests every 30 seconds. You can request a uniform
request every 0.5 seconds. You can also quickly request 60 times, rest
for 30 seconds, and then request the next round. If the frequency
limitation is exceeded, an error will be returned by the interface.





In order to protect the server from malicious attacks, there are
frequency limitations for all interfaces that need to send requests to
moomoo servers. The frequency limitation rules for each API are
different. For more information, please see **Interface Limitations** at
the bottom of each API page.

Example:  
The limitation rule of [Get Market
Snapshot](/moomoo-api-doc/en/quote/get-market-snapshot.html) is: A
maximum of 60 requests every 30 seconds. You can request a uniform
request every 0.5 seconds. You can also quickly request 60 times, rest
for 30 seconds, and then request the next round. If the frequency
limitation is exceeded, an error will be returned by the interface.





### <a href="#9123" class="header-anchor">#</a> Subscription Quota & Historical Candlestick Quota

The limitation rules of subscription quota and historical candlestick
quota as follows:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr data-align="center">
<th style="text-align: left;">User Type</th>
<th style="text-align: center;">Subscription Quota</th>
<th style="text-align: center;">Historical Candlestick Quota</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">Finished Opening trading accounts.</td>
<td style="text-align: center;">100</td>
<td style="text-align: center;">100</td>
</tr>
<tr>
<td style="text-align: left;">Total asset &gt; 10,000 HKD.</td>
<td style="text-align: center;">300</td>
<td style="text-align: center;">300</td>
</tr>
<tr>
<td style="text-align: left;">Satisfy 1 of the items following:<br />
1. Total asset &gt; 500,000 HKD;<br />
2. The number of monthly filled orders &gt; 200;<br />
3. Monthly trading volume &gt; 2 million HKD.</td>
<td style="text-align: center;">1000</td>
<td style="text-align: center;">1000</td>
</tr>
<tr>
<td style="text-align: left;">Satisfy 1 of the items following:<br />
1. Total asset &gt; 5 million HKD;<br />
2. The number of monthly filled orders &gt; 2000;<br />
3. Monthly trading volume &gt; 20 million HKD.</td>
<td style="text-align: center;">2000</td>
<td style="text-align: center;">2000</td>
</tr>
</tbody>
</table>





**1. Total asset**  
Total asset，refers to all your assets in Futu, including securities,
futures, funds and bonds assets, converted into HKD according to the
spot exchange rate.

**2. The monthly number of filled orders**  
It is calculated by taking the larger value of the number of filled
orders the last natural month and that of the current natural month,
that is:  
**max (the number of filled orders of the last natural month, the number
of filled orders of the current natural month)**

**3. Monthly Trading volume**  
It is calculated by taking the larger value of the total trading volume
of your last natural month and that of the current natural month, which
is converted into HKD according to the spot exchange rate, that is:  
**max (the total trading volume of the last natural month, the total
trading volume of the current natural month)**  
The calculation of futures trading value needs to be multiplied by the
adjustment factor (0.1 by default). The formula for calculating futures
trading volume is as follows:  
**Futures trading value = ∑ (volume of a single transaction \* trading
price \* contract multiplier \* exchange rate \* adjustment factor)**

**4. Subscription Quota**  
It is applicable to the real-time data interface that can only be
obtained after a subscription. One type of subscription for each stock
takes up 1 subscription quota, and canceling the subscription will
release the occupied quota.  
Example:  
Suppose your Subscription Quota is 100. When you subscribe to real-time
order book for HK.00700, real-time ticker for US.AAPL, and real-time
quotation for SH.600519 at the same time, the Subscription Quota will
occupy 3, and the remaining Subscription Quota will be 97. At this time,
if you cancel the real-time order book subscription of HK.00700, your
Subscription Quota will become 2, and the remaining Subscription Quota
will become 98.

**5. Historical Candlestick Quota**  
Suitable for [Get Historical
Candlesticks](/moomoo-api-doc/en/quote/request-history-kline.html)
interface. In the last 30 days, requests for historical candlesticks of
each stock will occupy one Historical Candlestick Quota. Repeated
requests for historical candlestick of the same stock within the last 30
days will not be counted repeatedly.  
Example:  
Suppose your Historical Candlestick Quota is 100, and today is July 5,
2020. You have requested historical candlesticks for a total of 60
stocks between June 5, 2020 and July 5, 2020. The remaining Historical
Candlestick Quota is 40.





**1. Total asset**  
Total asset, refers to all your assets in moomoo, including securities,
futures, funds and bonds assets, converted into HKD according to the
spot exchange rate.

**2. The monthly number of filled orders**  
It is calculated by taking the larger value of the number of filled
orders the last natural month and that of the current natural month,
that is:  
**max (the number of filled orders of the last natural month, the number
of filled orders of the current natural month)**

**3. Monthly Trading volume**  
It is calculated by taking the larger value of the total trading volume
of your last natural month and that of the current natural month, which
is converted into HKD according to the spot exchange rate, that is:  
**max (the total trading volume of the last natural month, the total
trading volume of the current natural month)**  
The calculation of futures trading value needs to be multiplied by the
adjustment factor (0.1 by default). The formula for calculating futures
trading volume is as follows:  
**Futures trading value = ∑ (volume of a single transaction \* trading
price \* contract multiplier \* exchange rate \* adjustment factor)**

**4. Subscription Quota**  
It is applicable to the real-time data interface that can only be
obtained after a subscription. One type of subscription for each stock
takes up 1 subscription quota, and canceling the subscription will
release the occupied quota.  
Example:  
Suppose your Subscription Quota is 100. When you subscribe to real-time
order book for HK.00700, real-time ticker for US.AAPL, and real-time
quotation for SH.600519 at the same time, the Subscription Quota will
occupy 3, and the remaining Subscription Quota will be 97. At this time,
if you cancel the real-time order book subscription of HK.00700, your
Subscription Quota will become 2, and the remaining Subscription Quota
will become 98.

**5. Historical Candlestick Quota**  
Suitable for [Get Historical
Candlesticks](/moomoo-api-doc/en/quote/request-history-kline.html)
interface. In the last 30 days, requests for historical candlesticks of
each stock will occupy one Historical Candlestick Quota. Repeated
requests for historical candlestick of the same stock within the last 30
days will not be counted repeatedly. Meanwhile, subscribing to
candlestick of different periods for the same stockonly occupies one
quota and will not be accumulated repeatedly. Example:  
Suppose your Historical Candlestick Quota is 100, and today is July 5,
2020. You have requested historical candlesticks for a total of 60
stocks between June 5, 2020 and July 5, 2020. The remaining Historical
Candlestick Quota is 40.







Tips

- Subscription Quota and Historical Candlestick Quota are automatically
  assigned and do not need to be applied manually.
- For newly deposited accounts, the quota will automatically take effect
  within 2 hours.
- *Asset in Transit*
  

  
  

  

  
  
  

  HK IPO Subscription and application for rights issue may generate
  Asset in Transit.

  

  

  

  

  will not be calculated in quota assign.



## <a href="#1667" class="header-anchor">#</a> Trading Functions

- When you trade in a specific market, you need to first confirm whether
  a trading account has been opened in that market.  
  For example: you can only trade US stocks under the US trading
  account, but not under the HK trading account.







