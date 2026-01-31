



# <a href="#6088" class="header-anchor">#</a> OpenAPI Introduction

## <a href="#6105" class="header-anchor">#</a> Overview





OpenAPI provides wide varieties of market data and trading services for
your programmed trading to meet the needs of every developer's
programmed trading and help your Quant dreams.

Futubull users can
<a href="https://www.futunn.com/OpenAPI?lang=en-US" target="_blank"
rel="noopener noreferrer">click here</a> to learn more.

*OpenAPI* consists of *OpenD* and *Futu API*:

- *OpenD* is the gateway program of *Futu API*, running on your local
  computer or cloud server. It is responsible for transferring the
  protocol requests to Futu servers, and returning the processed data.
- Futu API is an API SDK encapsulated by Futu, including mainstream
  programming languages (Python, Java, C#, C++, JavaScript), to reduce
  the difficulty of your trading strategy development. If the language
  you want to use is not listed above, you can still interface with the
  protocol yourself to complete the trading strategy development.

Diagrams below illustrate the architecture of OpenAPI.

![openapi-frame](/moomoo-api-doc/assets/img/futu-openapi-frame.59b6b342.png)

![openapi-interactive](/moomoo-api-doc/assets/img/nnopenapi-interactive.c434e2f8.png)

The first time using OpenAPI, you need to finish the following two
steps:

The first step is to install and start a gateway program
[OpenD](/moomoo-api-doc/en/quick/opend-base.html) locally or in the
cloud.

OpenD exposes the interfaces in the way of TCP, which is responsible for
transferring the protocol requests to Futu Server and returning the
processed data. The protocol interface has nothing to do with the type
of programming language.

The second step is to download Futu API and complete [Environment
Setup](/moomoo-api-doc/en/quick/env.html).

For your convenience, Futu encapsulates API SDK for mainstream
programming languages (hereinafter referred to as Futu API).





OpenAPI provides wide varieties of market data and trading services for
your programmed trading to meet the needs of every developer's
programmed trading and help your Quant dreams.

Moomoo users can
<a href="https://www.moomoo.com/OpenAPI" target="_blank"
rel="noopener noreferrer">click here</a> to learn more.

*OpenAPI* consists of *OpenD* and *moomoo API*:

- *OpenD* is the gateway program of *moomoo API*, running on your local
  computer or cloud server. It is responsible for transferring the
  protocol requests to moomoo servers, and returning the processed data.
- moomoo API is an API SDK encapsulated by moomoo, including mainstream
  programming languages (Python, Java, C#, C++, JavaScript), to reduce
  the difficulty of your trading strategy development. If the language
  you want to use is not listed above, you can still interface with the
  protocol yourself to complete the trading strategy development.

Diagrams below illustrate the architecture of OpenAPI.

![openapi-frame](/moomoo-api-doc/assets/img/openapi-frame.b45819e0.png)

![openapi-interactive](/moomoo-api-doc/assets/img/openapi-interactive.1cf547e7.png)

The first time using OpenAPI, you need to finish the following two
steps:

The first step is to install and start a gateway program
[OpenD](/moomoo-api-doc/en/quick/opend-base.html) locally or in the
cloud.

OpenD exposes the interfaces in the way of TCP, which is responsible for
transferring the protocol requests to moomoo servers and returning the
processed data. The protocol interface has nothing to do with the type
of programming language.

The second step is to download moomoo API and complete [Environment
Setup](/moomoo-api-doc/en/quick/env.html).

For your convenience, moomoo encapsulates API SDK for mainstream
programming languages (hereinafter referred to as moomoo API).





## <a href="#3030" class="header-anchor">#</a> Account





OpenAPI involves two types of accounts, *Futu ID* and *universal
account*.

### <a href="#9863" class="header-anchor">#</a> Futu ID

Futu ID is your user account (Futubull ID ), which can be used in
Futubull APP and OpenAPI.  
You can use your *Futu ID* and *login password* to log in to OpenD and
obtain market data.

### <a href="#4042" class="header-anchor">#</a> Universal Account

Universal account allows trading across multiple markets (including Hong
Kong stocks, US stocks, A-shares, and funds) in various currencies.
There's no need for multiple accounts.  
Universal Accounts come in two forms:

- Securities Universal Account: Trade stocks, ETFs, options, and other
  securities across different markets.
- Futures Universal Account: Trade futures, including Hong Kong, US CME
  Group, Singapore, and Japanese futures.





OpenAPI involves two types of accounts, *moomoo ID* and *universal
account*.

### <a href="#4705" class="header-anchor">#</a> moomoo ID

moomoo ID is your user account (moomoo ID), which can be used in moomoo
APP and OpenAPI.  
You can use your *moomoo ID* and *login password* to log in to OpenD and
obtain market data.

### <a href="#4042-2" class="header-anchor">#</a> Universal Account

Universal account allows trading across multiple markets (including Hong
Kong stocks, US stocks, A-shares, and funds) in various currencies.
There's no need for multiple accounts.  
Universal Accounts come in two forms:

- Securities Universal Account: Trade stocks, ETFs, options, and other
  securities across different markets.
- Futures Universal Account: Trade futures, including Hong Kong, US CME
  Group, Singapore, and Japanese futures.





## <a href="#8029" class="header-anchor">#</a> Functionality

There are 2 functions of OpenAPI: quotation and trading.

### <a href="#8088" class="header-anchor">#</a> Quotation Functions

#### <a href="#5366" class="header-anchor">#</a> Quotation Data Categories





Including stocks, indices, options and futures from HK, US and A-share
market. Find the specific types of support in the table below. You need
authorities for each kinds of market data. For more details on how to
obtain authorities, please [click
here](/moomoo-api-doc/en/intro/authority.html#7371).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Market</th>
<th>Contract</th>
<th style="text-align: center;">Futu Users</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">HK Market</td>
<td>Stocks, ETFs, Warrants, CBBCs, Inline Warrants</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Options</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Plates</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td rowspan="6">US Market</td>
<td>Stocks, ETFs

  


 

Covers NYSE, NYSE-American and Nasdaq listed equities.



</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>OTC Securities</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Options

  


 

Covers US stock options, US index options.



</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Plates</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td rowspan="3">A-share Market</td>
<td>Stocks, ETFs</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Plates</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td rowspan="2">Singapore Market</td>
<td>Stocks, ETFs, Warrants, REITs, DLCs</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="2">Japanese Market</td>
<td>Stocks, ETFs, REITs</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Australian Market</td>
<td>Stocks, ETFs</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Global Markets</td>
<td>Forex</td>
<td style="text-align: center;">X</td>
</tr>
</tbody>
</table>





Including stocks, indices, options and futures from HK, US and A-share
market. Find the specific types of support in the table below. You need
authorities for each kinds of market data. For more details on how to
obtain authorities, please [click
here](/moomoo-api-doc/en/intro/authority.html#7371).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Market</th>
<th>Contract</th>
<th style="text-align: center;">Moomoo Users</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="5">HK Market</td>
<td>Stocks, ETFs, Warrants, CBBCs, Inline Warrants</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Options</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Plates</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td rowspan="6">US Market</td>
<td>Stocks, ETFs

  


 

Covers NYSE, NYSE-American and Nasdaq listed equities.



</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>OTC Securities</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Options

  


 

Covers US stock options, US index options.



</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Plates</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td rowspan="3">A-share Market</td>
<td>Stocks, ETFs</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Indices</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td>Plates</td>
<td style="text-align: center;">✓</td>
</tr>
<tr>
<td rowspan="2">Singapore Market</td>
<td>Stocks, ETFs, Warrants, REITs, DLCs</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="2">Japanese Market</td>
<td>Stocks, ETFs, REITs</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Australian Market</td>
<td>Stocks, ETFs</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Global Markets</td>
<td>Forex</td>
<td style="text-align: center;">X</td>
</tr>
</tbody>
</table>





#### <a href="#9027" class="header-anchor">#</a> Method to Obtain Market Data

- Subscribe and receive pushed real-time quote, candlestick,
  tick-by-tick and order book.
- Request for the latest market snapshot, historical candlesticks etc.

### <a href="#1667" class="header-anchor">#</a> Trading Functions

#### <a href="#6650" class="header-anchor">#</a> Trading Capacity

Including stocks, options and futures from HK, US, A-share, Singapore
and Japanese markets. Find the specific types of support in the table
below:

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th>Market</th>
<th>Contracts</th>
<th>Paper Trading</th>
<th colspan="7">Live Trading</th>
</tr>
</thead>
<tbody>
<tr>
<th>FUTU HK</th>
<th>Moomoo US</th>
<th>Moomoo SG</th>
<th>Moomoo AU</th>
<th>Moomoo MY</th>
<th>Moomoo CA</th>
<th>Moomoo JP</th>
<th></th>
<th></th>
<th></th>
</tr>
&#10;<tr>
<td rowspan="3">HK Market</td>
<td>Stocks, ETFs, Warrants, CBBCs, Inline Warrants</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Options

  


 

including index options, tradable through futures account



</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="3">US Market</td>
<td>Stocks, ETFs</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Options</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="2">A-share Market</td>
<td>China Connect Securities stocks</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Non-China Connect Securities stocks</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="2">Singapore Market</td>
<td>Stocks, ETFs, Warrants, REITs, DLCs</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td rowspan="2">Japanese Market</td>
<td>Stocks, ETFs, REITs</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Futures</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">✓</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
<tr>
<td>Australian Market</td>
<td>Stocks, ETFs</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
</tr>
</tbody>
</table>

#### <a href="#3992" class="header-anchor">#</a> Method of Trading

The trading interfaces are used for both live trading and paper trading.

## <a href="#2883" class="header-anchor">#</a> Features





1.  Full platform and multi-language

- OpenD supports Windows, MacOS, CentOS, Ubuntu
- Futu API supports Python, Java, C#, C++, JavaScript, etc.

2.  Stable speed and free

- Stable technical architecture, directly connected to the exchanges
- The fastest order is 0.0014s
- There is no additional charge for trading via OpenAPI

3.  Abundant investment varieties

- Supporting real-time market data, live trading, and simulated trading
  in multiple markets including United States, Hong Kong, etc.

4.  Professional institutional services

- Customized market data and trading solutions





1.  Full platform and multi-language

- OpenD supports Windows, MacOS, CentOS, Ubuntu
- moomoo API supports Python, Java, C#, C++, JavaScript, etc.

2.  Stable speed and free

- Stable technical architecture, directly connected to the exchanges
- The fastest order is 0.0014s
- There is no additional charge for trading via OpenAPI

3.  Abundant investment varieties

- Supporting real-time market data, live trading, and simulated trading
  in multiple markets including United States, Hong Kong, etc.

4.  Professional institutional services

- Customized market data and trading solutions











