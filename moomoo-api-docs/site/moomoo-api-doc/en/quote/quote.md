



# <a href="#1099" class="header-anchor">#</a> Quotation Definitions

## <a href="#8316" class="header-anchor">#</a> Cumulative Filter Properties





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **StockField**

- `NONE`

  unknown

- `CHANGE_RATE`

  Yield

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-10.2, 20.4\]

  

  

  

  

- `AMPLITUDE`

  Amplitude

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[0.5, 20.6\]

  

  

  

  

- `VOLUME`

  Average daily trading volume

  

  
  

  

  
  
  

  - 0 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[2000, 70000\]

  

  

  

  

- `TURNOVER`

  Average daily turnover

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1400, 890000\]

  

  

  

  

- `TURNOVER_RATE`

  Turnover rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[2, 30\]

  

  

  

  





**AccumulateField**



``` protobuf
enum AccumulateField
{
    AccumulateField_Unknown = 0; // unknown
    AccumulateField_ChangeRate = 1; // Yield(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10.2, 20.4] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Amplitude = 2; // Amplitude(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20.6] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Volume = 3; // Average daily trading volume(0 decimal place accuracy, the excess part is discarded), for example, a range of [2000, 70000]
    AccumulateField_Turnover = 4; // Average daily turnover(3 decimal place accuracy, the excess part is discarded), for example, a range of [1400, 890000]
    AccumulateField_TurnoverRate = 5; // Turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [2, 30] (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**AccumulateField**



``` protobuf
enum AccumulateField
{
    AccumulateField_Unknown = 0; // unknown
    AccumulateField_ChangeRate = 1; // Yield(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10.2, 20.4] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Amplitude = 2; // Amplitude(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20.6] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Volume = 3; // Average daily trading volume(0 decimal place accuracy, the excess part is discarded), for example, a range of [2000, 70000]
    AccumulateField_Turnover = 4; // Average daily turnover(3 decimal place accuracy, the excess part is discarded), for example, a range of [1400, 890000]
    AccumulateField_TurnoverRate = 5; // Turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [2, 30] (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**AccumulateField**



``` protobuf
enum AccumulateField
{
    AccumulateField_Unknown = 0; // unknown
    AccumulateField_ChangeRate = 1; // Yield(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10.2, 20.4] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Amplitude = 2; // Amplitude(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20.6] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Volume = 3; // Average daily trading volume(0 decimal place accuracy, the excess part is discarded), for example, a range of [2000, 70000]
    AccumulateField_Turnover = 4; // Average daily turnover(3 decimal place accuracy, the excess part is discarded), for example, a range of [1400, 890000]
    AccumulateField_TurnoverRate = 5; // Turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [2, 30] (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**AccumulateField**



``` protobuf
enum AccumulateField
{
    AccumulateField_Unknown = 0; // unknown
    AccumulateField_ChangeRate = 1; // Yield(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10.2, 20.4] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Amplitude = 2; // Amplitude(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20.6] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Volume = 3; // Average daily trading volume(0 decimal place accuracy, the excess part is discarded), for example, a range of [2000, 70000]
    AccumulateField_Turnover = 4; // Average daily turnover(3 decimal place accuracy, the excess part is discarded), for example, a range of [1400, 890000]
    AccumulateField_TurnoverRate = 5; // Turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [2, 30] (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**AccumulateField**



``` protobuf
enum AccumulateField
{
    AccumulateField_Unknown = 0; // unknown
    AccumulateField_ChangeRate = 1; // Yield(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10.2, 20.4] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Amplitude = 2; // Amplitude(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20.6] (This field is in percentage form, so 20 is equivalent to 20%.)
    AccumulateField_Volume = 3; // Average daily trading volume(0 decimal place accuracy, the excess part is discarded), for example, a range of [2000, 70000]
    AccumulateField_Turnover = 4; // Average daily turnover(3 decimal place accuracy, the excess part is discarded), for example, a range of [1400, 890000]
    AccumulateField_TurnoverRate = 5; // Turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [2, 30] (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









## <a href="#4696" class="header-anchor">#</a> Asset Types





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **AssetClass**

- `UNKNOW`

  Unknown

- `STOCK`

  Stocks

- `BOND`

  Bonds

- `COMMODITY`

  Commodities

- `CURRENCY_MARKET`

  Currency markets

- `FUTURE`

  Futures

- `SWAP`

  Swaps





**AssetClass**



``` protobuf
enum AssetClass
{
    AssetClass_Unknow = 0; //Unknown
    AssetClass_Stock = 1; //Stock
    AssetClass_Bond = 2; //Bond
    AssetClass_Commodity = 3; //Commodity
    AssetClass_CurrencyMarket = 4; //Currency Market
    AssetClass_Future = 5; //Futures
    AssetClass_Swap = 6; //Swap
}
```









**AssetClass**



``` protobuf
enum AssetClass
{
    AssetClass_Unknow = 0; //Unknown
    AssetClass_Stock = 1; //Stock
    AssetClass_Bond = 2; //Bond
    AssetClass_Commodity = 3; //Commodity
    AssetClass_CurrencyMarket = 4; //Currency Market
    AssetClass_Future = 5; //Futures
    AssetClass_Swap = 6; //Swap
}
```









**AssetClass**



``` protobuf
enum AssetClass
{
    AssetClass_Unknow = 0; //Unknown
    AssetClass_Stock = 1; //Stock
    AssetClass_Bond = 2; //Bond
    AssetClass_Commodity = 3; //Commodity
    AssetClass_CurrencyMarket = 4; //Currency Market
    AssetClass_Future = 5; //Futures
    AssetClass_Swap = 6; //Swap
}
```









**AssetClass**



``` protobuf
enum AssetClass
{
    AssetClass_Unknow = 0; //Unknown
    AssetClass_Stock = 1; //Stock
    AssetClass_Bond = 2; //Bond
    AssetClass_Commodity = 3; //Commodity
    AssetClass_CurrencyMarket = 4; //Currency Market
    AssetClass_Future = 5; //Futures
    AssetClass_Swap = 6; //Swap
}
```









**AssetClass**



``` protobuf
enum AssetClass
{
    AssetClass_Unknow = 0; //Unknown
    AssetClass_Stock = 1; //Stock
    AssetClass_Bond = 2; //Bond
    AssetClass_Commodity = 3; //Commodity
    AssetClass_CurrencyMarket = 4; //Currency Market
    AssetClass_Future = 5; //Futures
    AssetClass_Swap = 6; //Swap
}
```









## <a href="#4631" class="header-anchor">#</a> Corporate Action





- Python
- Proto
- C#
- Java
- C++
- JavaScript









**CompanyAct**



``` protobuf
enum CompanyAct
{
    CompanyAct_None = 0; //None
    CompanyAct_Split = 1; //Share split
    CompanyAct_Join = 2; //Reverse stock split
    CompanyAct_Bonus = 4; //Bonus shares
    CompanyAct_Transfer = 8; //Transfer shares
    CompanyAct_Allot = 16; //Allotment
    CompanyAct_Add = 32; //Secondary Offering
    CompanyAct_Dividend = 64; //Cash dividend
    CompanyAct_SPDividend = 128; //Special dividend
}
```









**CompanyAct**



``` protobuf
enum CompanyAct
{
    CompanyAct_None = 0; //None
    CompanyAct_Split = 1; //Share split
    CompanyAct_Join = 2; //Reverse stock split
    CompanyAct_Bonus = 4; //Bonus shares
    CompanyAct_Transfer = 8; //Transfer shares
    CompanyAct_Allot = 16; //Allotment
    CompanyAct_Add = 32; //Secondary Offering
    CompanyAct_Dividend = 64; //Cash dividend
    CompanyAct_SPDividend = 128; //Special dividend
}
```









**CompanyAct**



``` protobuf
enum CompanyAct
{
    CompanyAct_None = 0; //None
    CompanyAct_Split = 1; //Share split
    CompanyAct_Join = 2; //Reverse stock split
    CompanyAct_Bonus = 4; //Bonus shares
    CompanyAct_Transfer = 8; //Transfer shares
    CompanyAct_Allot = 16; //Allotment
    CompanyAct_Add = 32; //Secondary Offering
    CompanyAct_Dividend = 64; //Cash dividend
    CompanyAct_SPDividend = 128; //Special dividend
}
```









**CompanyAct**



``` protobuf
enum CompanyAct
{
    CompanyAct_None = 0; //None
    CompanyAct_Split = 1; //Share split
    CompanyAct_Join = 2; //Reverse stock split
    CompanyAct_Bonus = 4; //Bonus shares
    CompanyAct_Transfer = 8; //Transfer shares
    CompanyAct_Allot = 16; //Allotment
    CompanyAct_Add = 32; //Secondary Offering
    CompanyAct_Dividend = 64; //Cash dividend
    CompanyAct_SPDividend = 128; //Special dividend
}
```









**CompanyAct**



``` protobuf
enum CompanyAct
{
    CompanyAct_None = 0; //None
    CompanyAct_Split = 1; //Share split
    CompanyAct_Join = 2; //Reverse stock split
    CompanyAct_Bonus = 4; //Bonus shares
    CompanyAct_Transfer = 8; //Transfer shares
    CompanyAct_Allot = 16; //Allotment
    CompanyAct_Add = 32; //Secondary Offering
    CompanyAct_Dividend = 64; //Cash dividend
    CompanyAct_SPDividend = 128; //Special dividend
}
```









## <a href="#6341" class="header-anchor">#</a> Dark Disk Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **DarkStatus**

- `NONE`

  No grey market trading

- `TRADING`

  Ongoing grey market trading

- `END`

  Grey market trading finished





**DarkStatus**



``` protobuf
enum DarkStatus
{
    DarkStatus_None = 0; //No grey market trading
    DarkStatus_Trading = 1; //Ongoing grey market trading
    DarkStatus_End = 2; //Grey market trading finished
}
```









**DarkStatus**



``` protobuf
enum DarkStatus
{
    DarkStatus_None = 0; //No grey market trading
    DarkStatus_Trading = 1; //Ongoing grey market trading
    DarkStatus_End = 2; //Grey market trading finished
}
```









**DarkStatus**



``` protobuf
enum DarkStatus
{
    DarkStatus_None = 0; //No grey market trading
    DarkStatus_Trading = 1; //Ongoing grey market trading
    DarkStatus_End = 2; //Grey market trading finished
}
```









**DarkStatus**



``` protobuf
enum DarkStatus
{
    DarkStatus_None = 0; //No grey market trading
    DarkStatus_Trading = 1; //Ongoing grey market trading
    DarkStatus_End = 2; //Grey market trading finished
}
```









**DarkStatus**



``` protobuf
enum DarkStatus
{
    DarkStatus_None = 0; //No grey market trading
    DarkStatus_Trading = 1; //Ongoing grey market trading
    DarkStatus_End = 2; //Grey market trading finished
}
```









## <a href="#2317" class="header-anchor">#</a> Financial Filter Properties





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **StockField**

- `NONE`

  unknown

- `NET_PROFIT`

  Net profit

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[100000000, 2500000000\]

  

  

  

  

- `NET_PROFIX_GROWTH`

  Net profit growth rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-10, 300\]

  

  

  

  

- `SUM_OF_BUSINESS`

  Operating income

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[100000000, 6400000000\]

  

  

  

  

- `SUM_OF_BUSINESS_GROWTH`

  Year-on-year growth rate of operating income

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-5, 200\]

  

  

  

  

- `NET_PROFIT_RATE`

  Net profit rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[10, 113\]

  

  

  

  

- `GROSS_PROFIT_RATE`

  Gross profit margin

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[4, 65\]

  

  

  

  

- `DEBT_ASSET_RATE`

  Asset-liability ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[5, 470\]

  

  

  

  

- `RETURN_ON_EQUITY_RATE`

  Return on equity

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[20, 230\]

  

  

  

  

- `ROIC`

  Return on invested capital

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `ROA_TTM`

  Return on assets TTM

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `EBIT_TTM`

  Earnings before interest and tax TTM

  

  
  

  

  
  
  

  - unit: yuan.
  - Only applicable to annual reports.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `EBITDA`

  Earnings before interest, tax, depreciation and amortization

  

  
  

  

  
  
  

  - unit: yuan.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `OPERATING_MARGIN_TTM`

  Operating profit margin TTM

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `EBIT_MARGIN`

  EBIT margin

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `EBITDA_MARGIN`

  EBITDA margin

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `FINANCIAL_COST_RATE`

  Financial cost rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `OPERATING_PROFIT_TTM`

  Operating profit TTM

  

  
  

  

  
  
  

  - unit: yuan.
  - Only applicable to annual reports.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `SHAREHOLDER_NET_PROFIT_TTM`

  Net profit attributable to the parent company

  

  
  

  

  
  
  

  - unit: yuan.
  - Only applicable to annual reports.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `NET_PROFIT_CASH_COVER_TTM`

  The proportion of cash income in profit

  

  
  

  

  
  
  

  - This field is in percentage form, so 20 is equivalent to 20%.
  - Only applicable to annual reports.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1.0, 60.0\]

  

  

  

  

- `CURRENT_RATIO`

  Current ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[100, 250\]

  

  

  

  

- `QUICK_RATIO`

  Quick ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[100, 250\]

  

  

  

  

- `CURRENT_ASSET_RATIO`

  Liquidity rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[10, 100\]

  

  

  

  

- `CURRENT_DEBT_RATIO`

  Current debt ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[10, 100\]

  

  

  

  

- `EQUITY_MULTIPLIER`

  Equity multiplier

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[100, 180\]

  

  

  

  

- `PROPERTY_RATIO`

  Equity ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[50, 100\]

  

  

  

  

- `CASH_AND_CASH_EQUIVALENTS`

  Cash and cash equivalent

  

  
  

  

  
  
  

  - unit: yuan.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `TOTAL_ASSET_TURNOVER`

  Total asset turnover rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[50, 100\]

  

  

  

  

- `FIXED_ASSET_TURNOVER`

  Fixed asset turnover rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[50, 100\]

  

  

  

  

- `INVENTORY_TURNOVER`

  Inventory turnover rate

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[50, 100\]

  

  

  

  

- `OPERATING_CASH_FLOW_TTM`

  Operating cash flow TTM

  

  
  

  

  
  
  

  - unit: yuan.
  - Only applicable to annual reports.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `ACCOUNTS_RECEIVABLE`

  Net accounts receivable

  

  
  

  

  
  
  

  - unit: yuan.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `EBIT_GROWTH_RATE`

  Year-on-year growth rate of EBIT

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `OPERATING_PROFIT_GROWTH_RATE`

  Year-on-year growth rate of operating profit

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `TOTAL_ASSETS_GROWTH_RATE`

  Year-on-year growth rate of total assets

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `PROFIT_TO_SHAREHOLDERS_GROWTH_RATE`

  Year-on-year growth rate of net profit attributed to parent company
  owner

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `PROFIT_BEFORE_TAX_GROWTH_RATE`

  Year-on-year growth rate of total profit

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `EPS_GROWTH_RATE`

  Year-on-year growth rate of EPS

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `ROE_GROWTH_RATE`

  Year-on-year growth rate of ROE

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `ROIC_GROWTH_RATE`

  Year-on-year growth rate of ROIC

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `NOCF_GROWTH_RATE`

  Year-on-year growth rate of operating cash flow

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `NOCF_PER_SHARE_GROWTH_RATE`

  Year-on-year growth rate of operating cash flow per share

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[1.0, 10.0\]

  

  

  

  

- `OPERATING_REVENUE_CASH_COVER`

  Operating cash cover ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[10, 100\]

  

  

  

  

- `OPERATING_PROFIT_TO_TOTAL_PROFIT`

  Operating profit ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[10, 100\]

  

  

  

  

- `BASIC_EPS`

  Basic earnings per share

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - unit: yuan.
  - For example, a range of \[0.1, 10\]

  

  

  

  

- `DILUTED_EPS`

  Diluted earnings per share

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - unit: yuan.
  - For example, a range of \[0.1, 10\]

  

  

  

  

- `NOCF_PER_SHARE`

  Net operating cash flow per share

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - unit: yuan.
  - For example, a range of \[0.1, 10\]

  

  

  

  





**FinancialField**



``` protobuf
enum FinancialField
{
    // Basic financial attributes
    FinancialField_Unknown = 0; // unknown
    FinancialField_NetProfit = 1; // Net profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 2500000000]
    FinancialField_NetProfitGrowth = 2; // Net profit growth rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 300] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_SumOfBusiness = 3; // Operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 6400000000]
    FinancialField_SumOfBusinessGrowth = 4; // The year-on-year growth rate of operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 200] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NetProfitRate = 5; // Net profit rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 113] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_GrossProfitRate = 6; // Gross profit margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [4, 65] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_DebtAssetsRate = 7; // Asset-liability ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [5, 470] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ReturnOnEquityRate = 8; // Return on equity(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 230] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Profitability attributes
    FinancialField_ROIC = 9; // Return on invested capital(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROATTM = 10; // Return on assets TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)actually corresponds to 20%. Only applicable to annual reports.)
    FinancialField_EBITTTM = 11; // Earnings before interest and tax TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_EBITDA = 12; // Earnings before interest, tax, depreciation and amortization(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
    FinancialField_OperatingMarginTTM = 13; // Operating profit margin TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITMargin = 14; // EBIT margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITDAMargin = 15; // EBITDA margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FinancialCostRate = 16; // Financial cost rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitTTM = 17; // Operating profit TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_ShareholderNetProfitTTM = 18; // Net profit attributable to the parent company(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_NetProfitCashCoverTTM = 19; // The proportion of cash income in profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 60.0] (This field is in percentage form, so 20 is equivalent to 20%.. Only applicable to annual reports.)

    // solvency attribute
    FinancialField_CurrentRatio = 20; // Current ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_QuickRatio = 21; // Quick ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Debt clearing ability attribute
    FinancialField_CurrentAssetRatio = 22; // Liquidity rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CurrentDebtRatio = 23; // Current debt ratio(3 decimal place accuracy, the excess part is discarded), for example, fill in the [10, 100] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EquityMultiplier = 24; // Equity multiplier(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 180]
    FinancialField_PropertyRatio = 25; // Equity ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CashAndCashEquivalents = 26; // Cash and cash equivalent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)

    // Operational capability attributes
    FinancialField_TotalAssetTurnover = 27; //Total asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FixedAssetTurnover = 28; // Fixed asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_InventoryTurnover = 29; // Inventory turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingCashFlowTTM = 30; // Operating cash flow TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_AccountsReceivable = 31; // Net accounts receivable(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] For example, a range of [1000000000,1000000000] (unit: yuan)

    // Growth ability attributes
    FinancialField_EBITGrowthRate = 32; // Year-on-year growth rate of EBIT(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitGrowthRate = 33; // Year-on-year growth rate of operating profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_TotalAssetsGrowthRate = 34; // Year-on-year growth rate of total assets(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitToShareholdersGrowthRate = 35; // Year-on-year growth rate of net profit attributable to the parent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0,10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitBeforeTaxGrowthRate = 36; // Year-on-year growth rate of total profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EPSGrowthRate = 37; // Year-on-year growth rate of EPS(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROEGrowthRate = 38; // Year-on-year growth rate of ROE(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROICGrowthRate = 39; // Year-on-year growth rate of ROIC(3 decimal place accuracy, the excess part is discarded), for example, fill in the [1.0, 10.0] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFGrowthRate = 40; // Year-on-year growth rate of operating cash flow(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFPerShareGrowthRate = 41; // Year-on-year growth rate of operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Cash flow attributes
    FinancialField_OperatingRevenueCashCover = 42; // Operating cash cover ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitToTotalProfit = 43; // Operating profit ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Market performance attributes
    FinancialField_BasicEPS = 44; // Basic earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_DilutedEPS = 45; // Diluted earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_NOCFPerShare = 46; // Net operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
}
```









**FinancialField**



``` protobuf
enum FinancialField
{
    // Basic financial attributes
    FinancialField_Unknown = 0; // unknown
    FinancialField_NetProfit = 1; // Net profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 2500000000]
    FinancialField_NetProfitGrowth = 2; // Net profit growth rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 300] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_SumOfBusiness = 3; // Operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 6400000000]
    FinancialField_SumOfBusinessGrowth = 4; // The year-on-year growth rate of operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 200] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NetProfitRate = 5; // Net profit rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 113] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_GrossProfitRate = 6; // Gross profit margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [4, 65] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_DebtAssetsRate = 7; // Asset-liability ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [5, 470] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ReturnOnEquityRate = 8; // Return on equity(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 230] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Profitability attributes
    FinancialField_ROIC = 9; // Return on invested capital(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROATTM = 10; // Return on assets TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)actually corresponds to 20%. Only applicable to annual reports.)
    FinancialField_EBITTTM = 11; // Earnings before interest and tax TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_EBITDA = 12; // Earnings before interest, tax, depreciation and amortization(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
    FinancialField_OperatingMarginTTM = 13; // Operating profit margin TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITMargin = 14; // EBIT margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITDAMargin = 15; // EBITDA margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FinancialCostRate = 16; // Financial cost rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitTTM = 17; // Operating profit TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_ShareholderNetProfitTTM = 18; // Net profit attributable to the parent company(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_NetProfitCashCoverTTM = 19; // The proportion of cash income in profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 60.0] (This field is in percentage form, so 20 is equivalent to 20%.. Only applicable to annual reports.)

    // solvency attribute
    FinancialField_CurrentRatio = 20; // Current ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_QuickRatio = 21; // Quick ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Debt clearing ability attribute
    FinancialField_CurrentAssetRatio = 22; // Liquidity rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CurrentDebtRatio = 23; // Current debt ratio(3 decimal place accuracy, the excess part is discarded), for example, fill in the [10, 100] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EquityMultiplier = 24; // Equity multiplier(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 180]
    FinancialField_PropertyRatio = 25; // Equity ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CashAndCashEquivalents = 26; // Cash and cash equivalent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)

    // Operational capability attributes
    FinancialField_TotalAssetTurnover = 27; //Total asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FixedAssetTurnover = 28; // Fixed asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_InventoryTurnover = 29; // Inventory turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingCashFlowTTM = 30; // Operating cash flow TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_AccountsReceivable = 31; // Net accounts receivable(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] For example, a range of [1000000000,1000000000] (unit: yuan)

    // Growth ability attributes
    FinancialField_EBITGrowthRate = 32; // Year-on-year growth rate of EBIT(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitGrowthRate = 33; // Year-on-year growth rate of operating profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_TotalAssetsGrowthRate = 34; // Year-on-year growth rate of total assets(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitToShareholdersGrowthRate = 35; // Year-on-year growth rate of net profit attributable to the parent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0,10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitBeforeTaxGrowthRate = 36; // Year-on-year growth rate of total profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EPSGrowthRate = 37; // Year-on-year growth rate of EPS(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROEGrowthRate = 38; // Year-on-year growth rate of ROE(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROICGrowthRate = 39; // Year-on-year growth rate of ROIC(3 decimal place accuracy, the excess part is discarded), for example, fill in the [1.0, 10.0] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFGrowthRate = 40; // Year-on-year growth rate of operating cash flow(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFPerShareGrowthRate = 41; // Year-on-year growth rate of operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Cash flow attributes
    FinancialField_OperatingRevenueCashCover = 42; // Operating cash cover ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitToTotalProfit = 43; // Operating profit ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Market performance attributes
    FinancialField_BasicEPS = 44; // Basic earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_DilutedEPS = 45; // Diluted earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_NOCFPerShare = 46; // Net operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
}
```









**FinancialField**



``` protobuf
enum FinancialField
{
    // Basic financial attributes
    FinancialField_Unknown = 0; // unknown
    FinancialField_NetProfit = 1; // Net profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 2500000000]
    FinancialField_NetProfitGrowth = 2; // Net profit growth rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 300] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_SumOfBusiness = 3; // Operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 6400000000]
    FinancialField_SumOfBusinessGrowth = 4; // The year-on-year growth rate of operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 200] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NetProfitRate = 5; // Net profit rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 113] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_GrossProfitRate = 6; // Gross profit margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [4, 65] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_DebtAssetsRate = 7; // Asset-liability ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [5, 470] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ReturnOnEquityRate = 8; // Return on equity(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 230] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Profitability attributes
    FinancialField_ROIC = 9; // Return on invested capital(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROATTM = 10; // Return on assets TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)actually corresponds to 20%. Only applicable to annual reports.)
    FinancialField_EBITTTM = 11; // Earnings before interest and tax TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_EBITDA = 12; // Earnings before interest, tax, depreciation and amortization(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
    FinancialField_OperatingMarginTTM = 13; // Operating profit margin TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITMargin = 14; // EBIT margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITDAMargin = 15; // EBITDA margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FinancialCostRate = 16; // Financial cost rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitTTM = 17; // Operating profit TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_ShareholderNetProfitTTM = 18; // Net profit attributable to the parent company(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_NetProfitCashCoverTTM = 19; // The proportion of cash income in profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 60.0] (This field is in percentage form, so 20 is equivalent to 20%.. Only applicable to annual reports.)

    // solvency attribute
    FinancialField_CurrentRatio = 20; // Current ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_QuickRatio = 21; // Quick ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Debt clearing ability attribute
    FinancialField_CurrentAssetRatio = 22; // Liquidity rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CurrentDebtRatio = 23; // Current debt ratio(3 decimal place accuracy, the excess part is discarded), for example, fill in the [10, 100] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EquityMultiplier = 24; // Equity multiplier(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 180]
    FinancialField_PropertyRatio = 25; // Equity ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CashAndCashEquivalents = 26; // Cash and cash equivalent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)

    // Operational capability attributes
    FinancialField_TotalAssetTurnover = 27; //Total asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FixedAssetTurnover = 28; // Fixed asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_InventoryTurnover = 29; // Inventory turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingCashFlowTTM = 30; // Operating cash flow TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_AccountsReceivable = 31; // Net accounts receivable(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] For example, a range of [1000000000,1000000000] (unit: yuan)

    // Growth ability attributes
    FinancialField_EBITGrowthRate = 32; // Year-on-year growth rate of EBIT(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitGrowthRate = 33; // Year-on-year growth rate of operating profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_TotalAssetsGrowthRate = 34; // Year-on-year growth rate of total assets(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitToShareholdersGrowthRate = 35; // Year-on-year growth rate of net profit attributable to the parent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0,10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitBeforeTaxGrowthRate = 36; // Year-on-year growth rate of total profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EPSGrowthRate = 37; // Year-on-year growth rate of EPS(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROEGrowthRate = 38; // Year-on-year growth rate of ROE(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROICGrowthRate = 39; // Year-on-year growth rate of ROIC(3 decimal place accuracy, the excess part is discarded), for example, fill in the [1.0, 10.0] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFGrowthRate = 40; // Year-on-year growth rate of operating cash flow(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFPerShareGrowthRate = 41; // Year-on-year growth rate of operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Cash flow attributes
    FinancialField_OperatingRevenueCashCover = 42; // Operating cash cover ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitToTotalProfit = 43; // Operating profit ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Market performance attributes
    FinancialField_BasicEPS = 44; // Basic earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_DilutedEPS = 45; // Diluted earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_NOCFPerShare = 46; // Net operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
}
```









**FinancialField**



``` protobuf
enum FinancialField
{
    // Basic financial attributes
    FinancialField_Unknown = 0; // unknown
    FinancialField_NetProfit = 1; // Net profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 2500000000]
    FinancialField_NetProfitGrowth = 2; // Net profit growth rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 300] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_SumOfBusiness = 3; // Operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 6400000000]
    FinancialField_SumOfBusinessGrowth = 4; // The year-on-year growth rate of operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 200] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NetProfitRate = 5; // Net profit rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 113] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_GrossProfitRate = 6; // Gross profit margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [4, 65] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_DebtAssetsRate = 7; // Asset-liability ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [5, 470] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ReturnOnEquityRate = 8; // Return on equity(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 230] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Profitability attributes
    FinancialField_ROIC = 9; // Return on invested capital(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROATTM = 10; // Return on assets TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)actually corresponds to 20%. Only applicable to annual reports.)
    FinancialField_EBITTTM = 11; // Earnings before interest and tax TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_EBITDA = 12; // Earnings before interest, tax, depreciation and amortization(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
    FinancialField_OperatingMarginTTM = 13; // Operating profit margin TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITMargin = 14; // EBIT margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITDAMargin = 15; // EBITDA margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FinancialCostRate = 16; // Financial cost rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitTTM = 17; // Operating profit TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_ShareholderNetProfitTTM = 18; // Net profit attributable to the parent company(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_NetProfitCashCoverTTM = 19; // The proportion of cash income in profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 60.0] (This field is in percentage form, so 20 is equivalent to 20%.. Only applicable to annual reports.)

    // solvency attribute
    FinancialField_CurrentRatio = 20; // Current ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_QuickRatio = 21; // Quick ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Debt clearing ability attribute
    FinancialField_CurrentAssetRatio = 22; // Liquidity rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CurrentDebtRatio = 23; // Current debt ratio(3 decimal place accuracy, the excess part is discarded), for example, fill in the [10, 100] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EquityMultiplier = 24; // Equity multiplier(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 180]
    FinancialField_PropertyRatio = 25; // Equity ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CashAndCashEquivalents = 26; // Cash and cash equivalent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)

    // Operational capability attributes
    FinancialField_TotalAssetTurnover = 27; //Total asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FixedAssetTurnover = 28; // Fixed asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_InventoryTurnover = 29; // Inventory turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingCashFlowTTM = 30; // Operating cash flow TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_AccountsReceivable = 31; // Net accounts receivable(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] For example, a range of [1000000000,1000000000] (unit: yuan)

    // Growth ability attributes
    FinancialField_EBITGrowthRate = 32; // Year-on-year growth rate of EBIT(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitGrowthRate = 33; // Year-on-year growth rate of operating profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_TotalAssetsGrowthRate = 34; // Year-on-year growth rate of total assets(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitToShareholdersGrowthRate = 35; // Year-on-year growth rate of net profit attributable to the parent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0,10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitBeforeTaxGrowthRate = 36; // Year-on-year growth rate of total profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EPSGrowthRate = 37; // Year-on-year growth rate of EPS(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROEGrowthRate = 38; // Year-on-year growth rate of ROE(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROICGrowthRate = 39; // Year-on-year growth rate of ROIC(3 decimal place accuracy, the excess part is discarded), for example, fill in the [1.0, 10.0] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFGrowthRate = 40; // Year-on-year growth rate of operating cash flow(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFPerShareGrowthRate = 41; // Year-on-year growth rate of operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Cash flow attributes
    FinancialField_OperatingRevenueCashCover = 42; // Operating cash cover ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitToTotalProfit = 43; // Operating profit ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Market performance attributes
    FinancialField_BasicEPS = 44; // Basic earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_DilutedEPS = 45; // Diluted earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_NOCFPerShare = 46; // Net operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
}
```









**FinancialField**



``` protobuf
enum FinancialField
{
    // Basic financial attributes
    FinancialField_Unknown = 0; // unknown
    FinancialField_NetProfit = 1; // Net profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 2500000000]
    FinancialField_NetProfitGrowth = 2; // Net profit growth rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 300] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_SumOfBusiness = 3; // Operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [100000000, 6400000000]
    FinancialField_SumOfBusinessGrowth = 4; // The year-on-year growth rate of operating income(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 200] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NetProfitRate = 5; // Net profit rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 113] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_GrossProfitRate = 6; // Gross profit margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [4, 65] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_DebtAssetsRate = 7; // Asset-liability ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [5, 470] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ReturnOnEquityRate = 8; // Return on equity(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 230] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Profitability attributes
    FinancialField_ROIC = 9; // Return on invested capital(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROATTM = 10; // Return on assets TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)actually corresponds to 20%. Only applicable to annual reports.)
    FinancialField_EBITTTM = 11; // Earnings before interest and tax TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_EBITDA = 12; // Earnings before interest, tax, depreciation and amortization(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
    FinancialField_OperatingMarginTTM = 13; // Operating profit margin TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITMargin = 14; // EBIT margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EBITDAMargin = 15; // EBITDA margin(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FinancialCostRate = 16; // Financial cost rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitTTM = 17; // Operating profit TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_ShareholderNetProfitTTM = 18; // Net profit attributable to the parent company(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (Unit: Yuan. Only applicable to annual reports.)
    FinancialField_NetProfitCashCoverTTM = 19; // The proportion of cash income in profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 60.0] (This field is in percentage form, so 20 is equivalent to 20%.. Only applicable to annual reports.)

    // solvency attribute
    FinancialField_CurrentRatio = 20; // Current ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_QuickRatio = 21; // Quick ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 250] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Debt clearing ability attribute
    FinancialField_CurrentAssetRatio = 22; // Liquidity rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CurrentDebtRatio = 23; // Current debt ratio(3 decimal place accuracy, the excess part is discarded), for example, fill in the [10, 100] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EquityMultiplier = 24; // Equity multiplier(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 180]
    FinancialField_PropertyRatio = 25; // Equity ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_CashAndCashEquivalents = 26; // Cash and cash equivalent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)

    // Operational capability attributes
    FinancialField_TotalAssetTurnover = 27; //Total asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_FixedAssetTurnover = 28; // Fixed asset turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_InventoryTurnover = 29; // Inventory turnover rate(3 decimal place accuracy, the excess part is discarded), for example, a range of [50, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingCashFlowTTM = 30; // Operating cash flow TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan. Only applicable to annual reports.)
    FinancialField_AccountsReceivable = 31; // Net accounts receivable(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] For example, a range of [1000000000,1000000000] (unit: yuan)

    // Growth ability attributes
    FinancialField_EBITGrowthRate = 32; // Year-on-year growth rate of EBIT(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitGrowthRate = 33; // Year-on-year growth rate of operating profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_TotalAssetsGrowthRate = 34; // Year-on-year growth rate of total assets(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitToShareholdersGrowthRate = 35; // Year-on-year growth rate of net profit attributable to the parent(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0,10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ProfitBeforeTaxGrowthRate = 36; // Year-on-year growth rate of total profit(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_EPSGrowthRate = 37; // Year-on-year growth rate of EPS(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROEGrowthRate = 38; // Year-on-year growth rate of ROE(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_ROICGrowthRate = 39; // Year-on-year growth rate of ROIC(3 decimal place accuracy, the excess part is discarded), for example, fill in the [1.0, 10.0] value range (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFGrowthRate = 40; // Year-on-year growth rate of operating cash flow(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_NOCFPerShareGrowthRate = 41; // Year-on-year growth rate of operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [1.0, 10.0] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Cash flow attributes
    FinancialField_OperatingRevenueCashCover = 42; // Operating cash cover ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)
    FinancialField_OperatingProfitToTotalProfit = 43; // Operating profit ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 100] (This field is in percentage form, so 20 is equivalent to 20%.)

    // Market performance attributes
    FinancialField_BasicEPS = 44; // Basic earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_DilutedEPS = 45; // Diluted earnings per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
    FinancialField_NOCFPerShare = 46; // Net operating cash flow per share(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.1, 10] (unit: yuan)
}
```









## <a href="#8409" class="header-anchor">#</a> Financial Filter Properties Period





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **FinancialQuarter**

- `NONE`

  unknown

- `ANNUAL`

  annual report

- `FIRST_QUARTER`

  First quarter report

- `INTERIM`

  Interim report

- `THIRD_QUARTER`

  Third quarter report

- `MOST_RECENT_QUARTER`

  Latest quarter report





**FinancialQuarter**



``` protobuf
enum FinancialQuarter
{
    FinancialQuarter_Unknown = 0; // unknown
    FinancialQuarter_Annual = 1; // Annual report
    FinancialQuarter_FirstQuarter = 2; // First quarter report
    FinancialQuarter_Interim = 3; // Interim report
    FinancialQuarter_ThirdQuarter = 4; // Third quarter report
    FinancialQuarter_MostRecentQuarter = 5; // Last quarter report
}
```









**FinancialQuarter**



``` protobuf
enum FinancialQuarter
{
    FinancialQuarter_Unknown = 0; // unknown
    FinancialQuarter_Annual = 1; // Annual report
    FinancialQuarter_FirstQuarter = 2; // First quarter report
    FinancialQuarter_Interim = 3; // Interim report
    FinancialQuarter_ThirdQuarter = 4; // Third quarter report
    FinancialQuarter_MostRecentQuarter = 5; // Last quarter report
}
```









**FinancialQuarter**



``` protobuf
enum FinancialQuarter
{
    FinancialQuarter_Unknown = 0; // unknown
    FinancialQuarter_Annual = 1; // Annual report
    FinancialQuarter_FirstQuarter = 2; // First quarter report
    FinancialQuarter_Interim = 3; // Interim report
    FinancialQuarter_ThirdQuarter = 4; // Third quarter report
    FinancialQuarter_MostRecentQuarter = 5; // Last quarter report
}
```









**FinancialQuarter**



``` protobuf
enum FinancialQuarter
{
    FinancialQuarter_Unknown = 0; // unknown
    FinancialQuarter_Annual = 1; // Annual report
    FinancialQuarter_FirstQuarter = 2; // First quarter report
    FinancialQuarter_Interim = 3; // Interim report
    FinancialQuarter_ThirdQuarter = 4; // Third quarter report
    FinancialQuarter_MostRecentQuarter = 5; // Last quarter report
}
```









**FinancialQuarter**



``` protobuf
enum FinancialQuarter
{
    FinancialQuarter_Unknown = 0; // unknown
    FinancialQuarter_Annual = 1; // Annual report
    FinancialQuarter_FirstQuarter = 2; // First quarter report
    FinancialQuarter_Interim = 3; // Interim report
    FinancialQuarter_ThirdQuarter = 4; // Third quarter report
    FinancialQuarter_MostRecentQuarter = 5; // Last quarter report
}
```









## <a href="#3936" class="header-anchor">#</a> Custom indicator attributes





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **StockField**

- `NONE`

  Unknown

- `PRICE`

  latest price

- `MA5`

  Simple moving average

- `MA5`

  5-day simple moving average (Not recommended)

- `MA10`

  10-day simple moving average (Not recommended)

- `MA20`

  20-day simple moving average (Not recommended)

- `MA30`

  30-day simple moving average (Not recommended)

- `MA60`

  60-day simple moving average (Not recommended)

- `MA120`

  120-day simple moving average (Not recommended)

- `MA250`

  250-day simple moving average (Not recommended)

- `RSI`

  RSI

  

  
  

  

  
  
  

  The default value of the indicator parameter is \[12\].

  

  

  

  

- `EMA`

  Exponential moving average

- `EMA5`

  5-day exponential moving average (Not recommended)

- `EMA10`

  10-day exponential moving average (Not recommended)

- `EMA20`

  20-day exponential moving average (Not recommended)

- `EMA30`

  30-day exponential moving average (Not recommended)

- `EMA60`

  60-day exponential moving average (Not recommended)

- `EMA120`

  120-day exponential moving average (Not recommended)

- `EMA250`

  250-day exponential moving average (Not recommended)

- `KDJ_K`

  K value of KDJ indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to KDJ. If not
  passed, the default value is \[9,3,3\].

  

  

  

  

- `KDJ_D`

  D value of KDJ indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to KDJ. If not
  passed, the default value is \[9,3,3\].

  

  

  

  

- `KDJ_J`

  J value of KDJ indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to KDJ. If not
  passed, the default value is \[9,3,3\].

  

  

  

  

- `MACD_DIFF`

  DIFF value of MACD indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to MACD. If not
  passed, the default value is \[12,26,9\].

  

  

  

  

- `MACD_DEA`

  DEA value of MACD indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to MACD. If not
  passed, the default value is \[12,26,9\].

  

  

  

  

- `MACD`

  MACD value of MACD indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to MACD. If not
  passed, the default value is \[12,26,9\].

  

  

  

  

- `BOLL_UPPER`

  UPPER value of BOLL indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to BOLL. If not
  passed, the default value is \[20,2\].

  

  

  

  

- `BOLL_MIDDLER`

  MIDDLER value of BOLL indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to BOLL. If not
  passed, the default value is \[20,2\].

  

  

  

  

- `BOLL_LOWER`

  LOWER value of BOLL indicator

  

  
  

  

  
  
  

  Indicator parameters need to be passed according to BOLL. If not
  passed, the default value is \[20,2\].

  

  

  

  

- `VALUE`

  Custom value (stock_field1 does not support this field)





**CustomIndicatorField**



``` protobuf
enum CustomIndicatorField
{
    CustomIndicatorField_Unknown = 0; // Unknown
    CustomIndicatorField_Price = 1; // latest price 
    CustomIndicatorField_MA5 = 2; // 5-day simple moving average (Not recommended)
    CustomIndicatorField_MA10 = 3; // 10-day simple moving average (Not recommended) 
    CustomIndicatorField_MA20 = 4; // 20-day simple moving average (Not recommended)
    CustomIndicatorField_MA30 = 5; // 30-day simple moving average (Not recommended)
    CustomIndicatorField_MA60 = 6; // 60-day simple moving average (Not recommended)
    CustomIndicatorField_MA120 = 7; // 120-day simple moving average (Not recommended)
    CustomIndicatorField_MA250 = 8; // 250-day simple moving average (Not recommended)
    CustomIndicatorField_RSI = 9; // RSI. The default value of the indicator parameter is [12].
    CustomIndicatorField_EMA5 = 10; // 5-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA10 = 11; // 10-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA20 = 12; // 20-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA30 = 13; // 30-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA60 = 14; // 60-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA120 = 15; // 120-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA250 = 16; // 250-day exponential moving average (Not recommended)
    CustomIndicatorField_Value = 17; // Custom value (stock_field1 does not support this field)
    CustomIndicatorField_MA = 30; // Simple moving average
    CustomIndicatorField_EMA = 40; // Exponential moving average
    CustomIndicatorField_KDJ_K = 50; // K value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_D = 51; // D value of KDJ indicator.Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_J = 52; // J value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].    
    CustomIndicatorField_MACD_DIFF = 60; // DIFF value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD_DEA = 61; // DEA value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD = 62; // MACD value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_BOLL_UPPER = 70; // UPPER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_MIDDLER = 71; // MIDDLER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_LOWER = 72; // LOWER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
}
```









**CustomIndicatorField**



``` protobuf
enum CustomIndicatorField
CustomIndicatorField
```









**CustomIndicatorField**



``` protobuf
enum CustomIndicatorField
{
    CustomIndicatorField_Unknown = 0; // Unknown
    CustomIndicatorField_Price = 1; // latest price 
    CustomIndicatorField_MA5 = 2; // 5-day simple moving average (Not recommended)
    CustomIndicatorField_MA10 = 3; // 10-day simple moving average (Not recommended) 
    CustomIndicatorField_MA20 = 4; // 20-day simple moving average (Not recommended)
    CustomIndicatorField_MA30 = 5; // 30-day simple moving average (Not recommended)
    CustomIndicatorField_MA60 = 6; // 60-day simple moving average (Not recommended)
    CustomIndicatorField_MA120 = 7; // 120-day simple moving average (Not recommended)
    CustomIndicatorField_MA250 = 8; // 250-day simple moving average (Not recommended)
    CustomIndicatorField_RSI = 9; // RSI. The default value of the indicator parameter is [12].
    CustomIndicatorField_EMA5 = 10; // 5-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA10 = 11; // 10-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA20 = 12; // 20-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA30 = 13; // 30-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA60 = 14; // 60-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA120 = 15; // 120-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA250 = 16; // 250-day exponential moving average (Not recommended)
    CustomIndicatorField_Value = 17; // Custom value (stock_field1 does not support this field)
    CustomIndicatorField_MA = 30; // Simple moving average
    CustomIndicatorField_EMA = 40; // Exponential moving average
    CustomIndicatorField_KDJ_K = 50; // K value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_D = 51; // D value of KDJ indicator.Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_J = 52; // J value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].    
    CustomIndicatorField_MACD_DIFF = 60; // DIFF value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD_DEA = 61; // DEA value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD = 62; // MACD value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_BOLL_UPPER = 70; // UPPER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_MIDDLER = 71; // MIDDLER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_LOWER = 72; // LOWER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
}
```









**CustomIndicatorField**



``` protobuf
enum CustomIndicatorField
{
    CustomIndicatorField_Unknown = 0; // Unknown
    CustomIndicatorField_Price = 1; // latest price 
    CustomIndicatorField_MA5 = 2; // 5-day simple moving average (Not recommended)
    CustomIndicatorField_MA10 = 3; // 10-day simple moving average (Not recommended) 
    CustomIndicatorField_MA20 = 4; // 20-day simple moving average (Not recommended)
    CustomIndicatorField_MA30 = 5; // 30-day simple moving average (Not recommended)
    CustomIndicatorField_MA60 = 6; // 60-day simple moving average (Not recommended)
    CustomIndicatorField_MA120 = 7; // 120-day simple moving average (Not recommended)
    CustomIndicatorField_MA250 = 8; // 250-day simple moving average (Not recommended)
    CustomIndicatorField_RSI = 9; // RSI. The default value of the indicator parameter is [12].
    CustomIndicatorField_EMA5 = 10; // 5-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA10 = 11; // 10-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA20 = 12; // 20-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA30 = 13; // 30-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA60 = 14; // 60-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA120 = 15; // 120-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA250 = 16; // 250-day exponential moving average (Not recommended)
    CustomIndicatorField_Value = 17; // Custom value (stock_field1 does not support this field)
    CustomIndicatorField_MA = 30; // Simple moving average
    CustomIndicatorField_EMA = 40; // Exponential moving average
    CustomIndicatorField_KDJ_K = 50; // K value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_D = 51; // D value of KDJ indicator.Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_J = 52; // J value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].    
    CustomIndicatorField_MACD_DIFF = 60; // DIFF value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD_DEA = 61; // DEA value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD = 62; // MACD value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_BOLL_UPPER = 70; // UPPER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_MIDDLER = 71; // MIDDLER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_LOWER = 72; // LOWER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
}
```









**CustomIndicatorField**



``` protobuf
enum CustomIndicatorField
{
    CustomIndicatorField_Unknown = 0; // Unknown
    CustomIndicatorField_Price = 1; // latest price 
    CustomIndicatorField_MA5 = 2; // 5-day simple moving average (Not recommended)
    CustomIndicatorField_MA10 = 3; // 10-day simple moving average (Not recommended) 
    CustomIndicatorField_MA20 = 4; // 20-day simple moving average (Not recommended)
    CustomIndicatorField_MA30 = 5; // 30-day simple moving average (Not recommended)
    CustomIndicatorField_MA60 = 6; // 60-day simple moving average (Not recommended)
    CustomIndicatorField_MA120 = 7; // 120-day simple moving average (Not recommended)
    CustomIndicatorField_MA250 = 8; // 250-day simple moving average (Not recommended)
    CustomIndicatorField_RSI = 9; // RSI. The default value of the indicator parameter is [12].
    CustomIndicatorField_EMA5 = 10; // 5-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA10 = 11; // 10-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA20 = 12; // 20-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA30 = 13; // 30-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA60 = 14; // 60-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA120 = 15; // 120-day exponential moving average (Not recommended)
    CustomIndicatorField_EMA250 = 16; // 250-day exponential moving average (Not recommended)
    CustomIndicatorField_Value = 17; // Custom value (stock_field1 does not support this field)
    CustomIndicatorField_MA = 30; // Simple moving average
    CustomIndicatorField_EMA = 40; // Exponential moving average
    CustomIndicatorField_KDJ_K = 50; // K value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_D = 51; // D value of KDJ indicator.Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].
    CustomIndicatorField_KDJ_J = 52; // J value of KDJ indicator. Indicator parameters need to be passed according to KDJ. If not passed, the default value is [9,3,3].    
    CustomIndicatorField_MACD_DIFF = 60; // DIFF value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD_DEA = 61; // DEA value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_MACD = 62; // MACD value of MACD indicator. Indicator parameters need to be passed according to MACD. If not passed, the default value is [12,26,9].
    CustomIndicatorField_BOLL_UPPER = 70; // UPPER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_MIDDLER = 71; // MIDDLER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
    CustomIndicatorField_BOLL_LOWER = 72; // LOWER value of BOLL indicator. Indicator parameters need to be passed according to BOLL. If not passed, the default value is [20,2].
}
```









## <a href="#9084" class="header-anchor">#</a> Relative position





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **RelativePosition**

- `NONE`

  Unknown

- `MORE`

  Stock_field1 is greater than stock_field2

- `LESS`

  Stock_field1 is less than stock_field2

- `CROSS_UP`

  Stock_field1 cross over stock_field2

- `CROSS_DOWN`

  Stock_field1 cross below stock_field2





**RelativePosition**



``` protobuf
enum RelativePosition
{
    RelativePosition_Unknown = 0; // Unknown
    RelativePosition_More = 1; // Stock_field1 is greater than stock_field2
    RelativePosition_Less = 2; // Stock_field1 is less than stock_field2
    RelativePosition_CrossUp = 3; // Stock_field1 cross over stock_field2
    RelativePosition_CrossDown = 4; // Stock_field1 cross below stock_field2
}
```









**RelativePosition**



``` protobuf
enum RelativePosition
{
    RelativePosition_Unknown = 0; // Unknown
    RelativePosition_More = 1; // Stock_field1 is greater than stock_field2
    RelativePosition_Less = 2; // Stock_field1 is less than stock_field2
    RelativePosition_CrossUp = 3; // Stock_field1 cross over stock_field2
    RelativePosition_CrossDown = 4; // Stock_field1 cross below stock_field2
}
```









**RelativePosition**



``` protobuf
enum RelativePosition
{
    RelativePosition_Unknown = 0; // Unknown
    RelativePosition_More = 1; // Stock_field1 is greater than stock_field2
    RelativePosition_Less = 2; // Stock_field1 is less than stock_field2
    RelativePosition_CrossUp = 3; // Stock_field1 cross over stock_field2
    RelativePosition_CrossDown = 4; // Stock_field1 cross below stock_field2
}
```









**RelativePosition**



``` protobuf
enum RelativePosition
{
    RelativePosition_Unknown = 0; // Unknown
    RelativePosition_More = 1; // Stock_field1 is greater than stock_field2
    RelativePosition_Less = 2; // Stock_field1 is less than stock_field2
    RelativePosition_CrossUp = 3; // Stock_field1 cross over stock_field2
    RelativePosition_CrossDown = 4; // Stock_field1 cross below stock_field2
}
```









**RelativePosition**



``` protobuf
enum RelativePosition
{
    RelativePosition_Unknown = 0; // Unknown
    RelativePosition_More = 1; // Stock_field1 is greater than stock_field2
    RelativePosition_Less = 2; // Stock_field1 is less than stock_field2
    RelativePosition_CrossUp = 3; // Stock_field1 cross over stock_field2
    RelativePosition_CrossDown = 4; // Stock_field1 cross below stock_field2
}
```









## <a href="#6605" class="header-anchor">#</a> Pattern attributes





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PatternField**

- `NONE`

  未知

- `MA_ALIGNMENT_LONG`

  MA bullish alignment (MA5 \> MA10 \> MA20 \> MA30 \> MA60 for two
  consecutive days, and the closing price of the day is greater than the
  closing price of the previous day)

- `MA_ALIGNMENT_SHORT`

  MA bearish alignment (MA5 \< MA10 \< MA20 \< MA30 \< MA60 for two
  consecutive days, and the closing price of the day is less than the
  closing price of the previous day)

- `EMA_ALIGNMENT_LONG`

  EMA bullish alignment (EMA5 \> EMA10 \> EMA20 \> EMA30 \> EMA60 for
  two consecutive days, and the closing price of the day is greater than
  the closing price of the previous day)

- `EMA_ALIGNMENT_SHORT`

  EMA bearish alignment (EMA5 \< EMA10 \< EMA20 \< EMA30 \< MA60 for two
  consecutive days, and the closing price of the day is less than the
  closing price of the previous day)

- `RSI_GOLD_CROSS_LOW`

  RSI low golden cross (short-term RSI crosses over long-term RSI below
  50 (short-term RSI of the previous day is less than long-term RSI,
  short-term RSI of the current day is greater than long-term RSI))

- `RSI_DEATH_CROSS_HIGH`

  RSI high dead cross (short-term RSI crosses below long-term RSI above
  50 (short-term RSI of the previous day is greater than long-term RSI,
  short-term RSI of the current day is less than long-term RSI))

- `RSI_TOP_DIVERGENCE`

  RSI top divergence (two adjacent candlestick peaks, the CLOSE of the
  later peak \> the CLOSE of the earlier peak, the RSI12 value of the
  later peak \< the RSI12 value of the earlier peak)

- `RSI_BOTTOM_DIVERGENCE`

  RSI bottom divergence (two adjacent candlestick troughs, the CLOSE of
  the later trough \< the CLOSE of the earlier trough, the RSI12 value
  of the later trough \> the RSI12 value of the earlier trough)

- `KDJ_GOLD_CROSS_LOW`

  KDJ low golden cross (D value is less than or equal to 30, and the K
  value of the previous day is less than the D value, and the K value of
  the day is greater than the D value)

- `KDJ_DEATH_CROSS_HIGH`

  KDJ high death cross (D value is greater than or equal to 70, and the
  K value of the previous day is greater than the D value, and the K
  value of the day is less than the D value)

- `KDJ_TOP_DIVERGENCE`

  KDJ top divergence (two adjacent candlestick peaks, the CLOSE of the
  later peak \> the CLOSE of the earlier peak, the J value of the later
  peak \< the J value of the earlier peak)

- `KDJ_BOTTOM_DIVERGENCE`

  KDJ bottom divergence (two adjacent candlestick troughs, the CLOSE of
  the later trough \< the CLOSE of the earlier trough, the J value of
  the later trough \> the J value of the earlier trough)

- `MACD_GOLD_CROSS_LOW`

  MACD golden cross (DIFF crosses over DEA ​​(DIFF is less than DEA of the
  previous day, and DIFF is greater than DEA of the current day))

- `MACD_DEATH_CROSS_HIGH`

  MACD dead cross (DIFF crosses below DEA (DIFF is greater than DEA of
  the previous day, and DIFF is less than DEA of the current day))

- `MACD_TOP_DIVERGENCE`

  MACD top divergence (two adjacent candlestick peaks, the CLOSE of the
  later peak \> the CLOSE of the earlier peak, the MACD value of the
  later peak \< the MACD value of the earlier peak)

- `MACD_BOTTOM_DIVERGENCE`

  MACD bottom deviation (two adjacent candlestick troughs, the CLOSE of
  the later trough \< the CLOSE of the earlier trough, the MACD value of
  the later trough \> the MACD value of the earlier trough)

- `BOLL_BREAK_UPPER`

  Break up bollinger upper bound (the stock price of the previous day
  was lower than the upper bound, and the stock price of the current day
  is greater than the upper bound)

- `BOLL_BREAK_LOWER`

  Break up bollinger lower bound (the stock price of the previous day
  was greater than the lower bound, and the stock price of the current
  day is less than the lower bound)

- `BOLL_CROSS_MIDDLE_UP`

  Cross over bollinger mid line (the stock price of the previous day was
  lower than the mid line, and the stock price of the current day is
  greater than the mid line)

- `BOLL_CROSS_MIDDLE_DOWN`

  Cross below bollinger mid line (the stock price of the previous day
  was greater than the mid line, and the stock price of the current day
  is less than the mid line)





**PatternField**



``` protobuf
enum PatternField
{
    PatternField_Unknown = 0 ; // Unknown
    PatternField_MAAlignmentLong = 1; // MA bullish alignment (MA5 > MA10 > MA20 > MA30 > MA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_MAAlignmentShort = 2; // MA bearish alignment (MA5 < MA10 < MA20 < MA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_EMAAlignmentLong = 3; // EMA bullish alignment (EMA5 > EMA10 > EMA20 > EMA30 > EMA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_EMAAlignmentShort = 4; // EMA bearish alignment (EMA5 < EMA10 < EMA20 < EMA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_RSIGoldCrossLow = 5; // RSI low golden cross (short-term RSI crosses over long-term RSI below 50 (short-term RSI of the previous day is less than long-term RSI, short-term RSI of the current day is greater than long-term RSI))
    PatternField_RSIDeathCrossHigh = 6; // RSI high dead cross (short-term RSI crosses below long-term RSI above 50 (short-term RSI of the previous day is greater than long-term RSI, short-term RSI of the current day is less than long-term RSI))
    PatternField_RSITopDivergence = 7; // RSI top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the RSI12 value of the later peak < the RSI12 value of the earlier peak)
    PatternField_RSIBottomDivergence = 8; // RSI bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the RSI12 value of the later trough > the RSI12 value of the earlier trough)
    PatternField_KDJGoldCrossLow = 9; // KDJ low golden cross (D value is less than or equal to 30, and the K value of the previous day is less than the D value, and the K value of the day is greater than the D value)
    PatternField_KDJDeathCrossHigh = 10; // KDJ high death cross (D value is greater than or equal to 70, and the K value of the previous day is greater than the D value, and the K value of the day is less than the D value)
    PatternField_KDJTopDivergence = 11; // KDJ top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the J value of the later peak < the J value of the earlier peak)
    PatternField_KDJBottomDivergence = 12; // KDJ bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the J value of the later trough > the J value of the earlier trough)
    PatternField_MACDGoldCrossLow = 13; // MACD golden cross (DIFF crosses over DEA ​​(DIFF is less than DEA of the previous day, and DIFF is greater than DEA of the current day))
    PatternField_MACDDeathCrossHigh = 14; // MACD dead cross (DIFF crosses below DEA (DIFF is greater than DEA of the previous day, and DIFF is less than DEA of the current day))
    PatternField_MACDTopDivergence = 15; // MACD top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the MACD value of the later peak < the MACD value of the earlier peak)
    PatternField_MACDBottomDivergence = 16; // MACD bottom deviation (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the MACD value of the later trough > the MACD value of the earlier trough)
    PatternField_BOLLBreakUpper = 17; // Break up bollinger upper bound (the stock price of the previous day was lower than the upper bound, and the stock price of the current day is greater than the upper bound)
    PatternField_BOLLLower = 18; // Break up bollinger lower bound (the stock price of the previous day was greater than the lower bound, and the stock price of the current day is less than the lower bound)
    PatternField_BOLLCrossMiddleUp = 19; // Cross over bollinger mid line (the stock price of the previous day was lower than the mid line, and the stock price of the current day is greater than the mid line)
    PatternField_BOLLCrossMiddleDown = 20; // Cross below bollinger mid line (the stock price of the previous day was greater than the mid line, and the stock price of the current day is less than the mid line)
}
```









**PatternField**



``` protobuf
enum PatternField
{
    PatternField_Unknown = 0 ; // Unknown
    PatternField_MAAlignmentLong = 1; // MA bullish alignment (MA5 > MA10 > MA20 > MA30 > MA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_MAAlignmentShort = 2; // MA bearish alignment (MA5 < MA10 < MA20 < MA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_EMAAlignmentLong = 3; // EMA bullish alignment (EMA5 > EMA10 > EMA20 > EMA30 > EMA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_EMAAlignmentShort = 4; // EMA bearish alignment (EMA5 < EMA10 < EMA20 < EMA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_RSIGoldCrossLow = 5; // RSI low golden cross (short-term RSI crosses over long-term RSI below 50 (short-term RSI of the previous day is less than long-term RSI, short-term RSI of the current day is greater than long-term RSI))
    PatternField_RSIDeathCrossHigh = 6; // RSI high dead cross (short-term RSI crosses below long-term RSI above 50 (short-term RSI of the previous day is greater than long-term RSI, short-term RSI of the current day is less than long-term RSI))
    PatternField_RSITopDivergence = 7; // RSI top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the RSI12 value of the later peak < the RSI12 value of the earlier peak)
    PatternField_RSIBottomDivergence = 8; // RSI bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the RSI12 value of the later trough > the RSI12 value of the earlier trough)
    PatternField_KDJGoldCrossLow = 9; // KDJ low golden cross (D value is less than or equal to 30, and the K value of the previous day is less than the D value, and the K value of the day is greater than the D value)
    PatternField_KDJDeathCrossHigh = 10; // KDJ high death cross (D value is greater than or equal to 70, and the K value of the previous day is greater than the D value, and the K value of the day is less than the D value)
    PatternField_KDJTopDivergence = 11; // KDJ top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the J value of the later peak < the J value of the earlier peak)
    PatternField_KDJBottomDivergence = 12; // KDJ bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the J value of the later trough > the J value of the earlier trough)
    PatternField_MACDGoldCrossLow = 13; // MACD golden cross (DIFF crosses over DEA ​​(DIFF is less than DEA of the previous day, and DIFF is greater than DEA of the current day))
    PatternField_MACDDeathCrossHigh = 14; // MACD dead cross (DIFF crosses below DEA (DIFF is greater than DEA of the previous day, and DIFF is less than DEA of the current day))
    PatternField_MACDTopDivergence = 15; // MACD top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the MACD value of the later peak < the MACD value of the earlier peak)
    PatternField_MACDBottomDivergence = 16; // MACD bottom deviation (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the MACD value of the later trough > the MACD value of the earlier trough)
    PatternField_BOLLBreakUpper = 17; // Break up bollinger upper bound (the stock price of the previous day was lower than the upper bound, and the stock price of the current day is greater than the upper bound)
    PatternField_BOLLLower = 18; // Break up bollinger lower bound (the stock price of the previous day was greater than the lower bound, and the stock price of the current day is less than the lower bound)
    PatternField_BOLLCrossMiddleUp = 19; // Cross over bollinger mid line (the stock price of the previous day was lower than the mid line, and the stock price of the current day is greater than the mid line)
    PatternField_BOLLCrossMiddleDown = 20; // Cross below bollinger mid line (the stock price of the previous day was greater than the mid line, and the stock price of the current day is less than the mid line)
}
```









**PatternField**



``` protobuf
enum PatternField
{
    PatternField_Unknown = 0 ; // Unknown
    PatternField_MAAlignmentLong = 1; // MA bullish alignment (MA5 > MA10 > MA20 > MA30 > MA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_MAAlignmentShort = 2; // MA bearish alignment (MA5 < MA10 < MA20 < MA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_EMAAlignmentLong = 3; // EMA bullish alignment (EMA5 > EMA10 > EMA20 > EMA30 > EMA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_EMAAlignmentShort = 4; // EMA bearish alignment (EMA5 < EMA10 < EMA20 < EMA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_RSIGoldCrossLow = 5; // RSI low golden cross (short-term RSI crosses over long-term RSI below 50 (short-term RSI of the previous day is less than long-term RSI, short-term RSI of the current day is greater than long-term RSI))
    PatternField_RSIDeathCrossHigh = 6; // RSI high dead cross (short-term RSI crosses below long-term RSI above 50 (short-term RSI of the previous day is greater than long-term RSI, short-term RSI of the current day is less than long-term RSI))
    PatternField_RSITopDivergence = 7; // RSI top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the RSI12 value of the later peak < the RSI12 value of the earlier peak)
    PatternField_RSIBottomDivergence = 8; // RSI bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the RSI12 value of the later trough > the RSI12 value of the earlier trough)
    PatternField_KDJGoldCrossLow = 9; // KDJ low golden cross (D value is less than or equal to 30, and the K value of the previous day is less than the D value, and the K value of the day is greater than the D value)
    PatternField_KDJDeathCrossHigh = 10; // KDJ high death cross (D value is greater than or equal to 70, and the K value of the previous day is greater than the D value, and the K value of the day is less than the D value)
    PatternField_KDJTopDivergence = 11; // KDJ top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the J value of the later peak < the J value of the earlier peak)
    PatternField_KDJBottomDivergence = 12; // KDJ bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the J value of the later trough > the J value of the earlier trough)
    PatternField_MACDGoldCrossLow = 13; // MACD golden cross (DIFF crosses over DEA ​​(DIFF is less than DEA of the previous day, and DIFF is greater than DEA of the current day))
    PatternField_MACDDeathCrossHigh = 14; // MACD dead cross (DIFF crosses below DEA (DIFF is greater than DEA of the previous day, and DIFF is less than DEA of the current day))
    PatternField_MACDTopDivergence = 15; // MACD top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the MACD value of the later peak < the MACD value of the earlier peak)
    PatternField_MACDBottomDivergence = 16; // MACD bottom deviation (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the MACD value of the later trough > the MACD value of the earlier trough)
    PatternField_BOLLBreakUpper = 17; // Break up bollinger upper bound (the stock price of the previous day was lower than the upper bound, and the stock price of the current day is greater than the upper bound)
    PatternField_BOLLLower = 18; // Break up bollinger lower bound (the stock price of the previous day was greater than the lower bound, and the stock price of the current day is less than the lower bound)
    PatternField_BOLLCrossMiddleUp = 19; // Cross over bollinger mid line (the stock price of the previous day was lower than the mid line, and the stock price of the current day is greater than the mid line)
    PatternField_BOLLCrossMiddleDown = 20; // Cross below bollinger mid line (the stock price of the previous day was greater than the mid line, and the stock price of the current day is less than the mid line)
}
```









**PatternField**



``` protobuf
enum PatternField
{
    PatternField_Unknown = 0 ; // Unknown
    PatternField_MAAlignmentLong = 1; // MA bullish alignment (MA5 > MA10 > MA20 > MA30 > MA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_MAAlignmentShort = 2; // MA bearish alignment (MA5 < MA10 < MA20 < MA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_EMAAlignmentLong = 3; // EMA bullish alignment (EMA5 > EMA10 > EMA20 > EMA30 > EMA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_EMAAlignmentShort = 4; // EMA bearish alignment (EMA5 < EMA10 < EMA20 < EMA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_RSIGoldCrossLow = 5; // RSI low golden cross (short-term RSI crosses over long-term RSI below 50 (short-term RSI of the previous day is less than long-term RSI, short-term RSI of the current day is greater than long-term RSI))
    PatternField_RSIDeathCrossHigh = 6; // RSI high dead cross (short-term RSI crosses below long-term RSI above 50 (short-term RSI of the previous day is greater than long-term RSI, short-term RSI of the current day is less than long-term RSI))
    PatternField_RSITopDivergence = 7; // RSI top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the RSI12 value of the later peak < the RSI12 value of the earlier peak)
    PatternField_RSIBottomDivergence = 8; // RSI bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the RSI12 value of the later trough > the RSI12 value of the earlier trough)
    PatternField_KDJGoldCrossLow = 9; // KDJ low golden cross (D value is less than or equal to 30, and the K value of the previous day is less than the D value, and the K value of the day is greater than the D value)
    PatternField_KDJDeathCrossHigh = 10; // KDJ high death cross (D value is greater than or equal to 70, and the K value of the previous day is greater than the D value, and the K value of the day is less than the D value)
    PatternField_KDJTopDivergence = 11; // KDJ top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the J value of the later peak < the J value of the earlier peak)
    PatternField_KDJBottomDivergence = 12; // KDJ bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the J value of the later trough > the J value of the earlier trough)
    PatternField_MACDGoldCrossLow = 13; // MACD golden cross (DIFF crosses over DEA ​​(DIFF is less than DEA of the previous day, and DIFF is greater than DEA of the current day))
    PatternField_MACDDeathCrossHigh = 14; // MACD dead cross (DIFF crosses below DEA (DIFF is greater than DEA of the previous day, and DIFF is less than DEA of the current day))
    PatternField_MACDTopDivergence = 15; // MACD top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the MACD value of the later peak < the MACD value of the earlier peak)
    PatternField_MACDBottomDivergence = 16; // MACD bottom deviation (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the MACD value of the later trough > the MACD value of the earlier trough)
    PatternField_BOLLBreakUpper = 17; // Break up bollinger upper bound (the stock price of the previous day was lower than the upper bound, and the stock price of the current day is greater than the upper bound)
    PatternField_BOLLLower = 18; // Break up bollinger lower bound (the stock price of the previous day was greater than the lower bound, and the stock price of the current day is less than the lower bound)
    PatternField_BOLLCrossMiddleUp = 19; // Cross over bollinger mid line (the stock price of the previous day was lower than the mid line, and the stock price of the current day is greater than the mid line)
    PatternField_BOLLCrossMiddleDown = 20; // Cross below bollinger mid line (the stock price of the previous day was greater than the mid line, and the stock price of the current day is less than the mid line)
}
```









**PatternField**



``` protobuf
enum PatternField
{
    PatternField_Unknown = 0 ; // Unknown
    PatternField_MAAlignmentLong = 1; // MA bullish alignment (MA5 > MA10 > MA20 > MA30 > MA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_MAAlignmentShort = 2; // MA bearish alignment (MA5 < MA10 < MA20 < MA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_EMAAlignmentLong = 3; // EMA bullish alignment (EMA5 > EMA10 > EMA20 > EMA30 > EMA60 for two consecutive days, and the closing price of the day is greater than the closing price of the previous day)
    PatternField_EMAAlignmentShort = 4; // EMA bearish alignment (EMA5 < EMA10 < EMA20 < EMA30 < MA60 for two consecutive days, and the closing price of the day is less than the closing price of the previous day)
    PatternField_RSIGoldCrossLow = 5; // RSI low golden cross (short-term RSI crosses over long-term RSI below 50 (short-term RSI of the previous day is less than long-term RSI, short-term RSI of the current day is greater than long-term RSI))
    PatternField_RSIDeathCrossHigh = 6; // RSI high dead cross (short-term RSI crosses below long-term RSI above 50 (short-term RSI of the previous day is greater than long-term RSI, short-term RSI of the current day is less than long-term RSI))
    PatternField_RSITopDivergence = 7; // RSI top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the RSI12 value of the later peak < the RSI12 value of the earlier peak)
    PatternField_RSIBottomDivergence = 8; // RSI bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the RSI12 value of the later trough > the RSI12 value of the earlier trough)
    PatternField_KDJGoldCrossLow = 9; // KDJ low golden cross (D value is less than or equal to 30, and the K value of the previous day is less than the D value, and the K value of the day is greater than the D value)
    PatternField_KDJDeathCrossHigh = 10; // KDJ high death cross (D value is greater than or equal to 70, and the K value of the previous day is greater than the D value, and the K value of the day is less than the D value)
    PatternField_KDJTopDivergence = 11; // KDJ top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the J value of the later peak < the J value of the earlier peak)
    PatternField_KDJBottomDivergence = 12; // KDJ bottom divergence (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the J value of the later trough > the J value of the earlier trough)
    PatternField_MACDGoldCrossLow = 13; // MACD golden cross (DIFF crosses over DEA ​​(DIFF is less than DEA of the previous day, and DIFF is greater than DEA of the current day))
    PatternField_MACDDeathCrossHigh = 14; // MACD dead cross (DIFF crosses below DEA (DIFF is greater than DEA of the previous day, and DIFF is less than DEA of the current day))
    PatternField_MACDTopDivergence = 15; // MACD top divergence (two adjacent candlestick peaks, the CLOSE of the later peak > the CLOSE of the earlier peak, the MACD value of the later peak < the MACD value of the earlier peak)
    PatternField_MACDBottomDivergence = 16; // MACD bottom deviation (two adjacent candlestick troughs, the CLOSE of the later trough < the CLOSE of the earlier trough, the MACD value of the later trough > the MACD value of the earlier trough)
    PatternField_BOLLBreakUpper = 17; // Break up bollinger upper bound (the stock price of the previous day was lower than the upper bound, and the stock price of the current day is greater than the upper bound)
    PatternField_BOLLLower = 18; // Break up bollinger lower bound (the stock price of the previous day was greater than the lower bound, and the stock price of the current day is less than the lower bound)
    PatternField_BOLLCrossMiddleUp = 19; // Cross over bollinger mid line (the stock price of the previous day was lower than the mid line, and the stock price of the current day is greater than the mid line)
    PatternField_BOLLCrossMiddleDown = 20; // Cross below bollinger mid line (the stock price of the previous day was greater than the mid line, and the stock price of the current day is less than the mid line)
}
```









## <a href="#8561" class="header-anchor">#</a> Watchlist Group Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **UserSecurityGroupType**

- `NONE`

  unknown

- `CUSTOM`

  Custom groups

- `SYSTEM`

  System groups

- `ALL`

  All groups





**GroupType**



``` protobuf
enum GroupType
{
    GroupType_Unknown = 0; // unknown
    GroupType_Custom = 1; // Custom groups
    GroupType_System = 2; // System groups
    GroupType_All = 3; // All groupss
}
```









**GroupType**



``` protobuf
enum GroupType
{
    GroupType_Unknown = 0; // unknown
    GroupType_Custom = 1; // Custom groups
    GroupType_System = 2; // System groups
    GroupType_All = 3; // All groupss
}
```









**GroupType**



``` protobuf
enum GroupType
{
    GroupType_Unknown = 0; // unknown
    GroupType_Custom = 1; // Custom groups
    GroupType_System = 2; // System groups
    GroupType_All = 3; // All groupss
}
```









**GroupType**



``` protobuf
enum GroupType
{
    GroupType_Unknown = 0; // unknown
    GroupType_Custom = 1; // Custom groups
    GroupType_System = 2; // System groups
    GroupType_All = 3; // All groupss
}
```









**GroupType**



``` protobuf
enum GroupType
{
    GroupType_Unknown = 0; // unknown
    GroupType_Custom = 1; // Custom groups
    GroupType_System = 2; // System groups
    GroupType_All = 3; // All groupss
}
```









## <a href="#2866" class="header-anchor">#</a> Index Option Category





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **IndexOptionType**

- `NONE`

  unknown

- `NORMAL`

  Ordinary index option

- `SMALL`

  Small Index Options





**IndexOptionType**



``` protobuf
enum IndexOptionType
{
    IndexOptionType_Unknown = 0; //Unknown
    IndexOptionType_Normal = 1; //Normal index option
    IndexOptionType_Small = 2; //Small index options
}
```









**IndexOptionType**



``` protobuf
enum IndexOptionType
{
    IndexOptionType_Unknown = 0; //Unknown
    IndexOptionType_Normal = 1; //Normal index option
    IndexOptionType_Small = 2; //Small index options
}
```









**IndexOptionType**



``` protobuf
enum IndexOptionType
{
    IndexOptionType_Unknown = 0; //Unknown
    IndexOptionType_Normal = 1; //Normal index option
    IndexOptionType_Small = 2; //Small index options
}
```









**IndexOptionType**



``` protobuf
enum IndexOptionType
{
    IndexOptionType_Unknown = 0; //Unknown
    IndexOptionType_Normal = 1; //Normal index option
    IndexOptionType_Small = 2; //Small index options
}
```









**IndexOptionType**



``` protobuf
enum IndexOptionType
{
    IndexOptionType_Unknown = 0; //Unknown
    IndexOptionType_Normal = 1; //Normal index option
    IndexOptionType_Small = 2; //Small index options
}
```









## <a href="#2961" class="header-anchor">#</a> Listing Time





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **IpoPeriod**

- `NONE`

  unknown

- `TODAY`

  Listed today

- `TOMORROW`

  To be listed tomorrow

- `NEXTWEEK`

  To be listed next week

- `LASTWEEK`

  Has been listed last week

- `LASTMONTH`

  Has been listed last month





**IpoPeriod**



``` protobuf
enum IpoPeriod
{
    IpoPeriod_Unknow = 0; //Unknown
    IpoPeriod_Today = 1; //Listed today
    IpoPeriod_Tomorrow = 2; //To be listed tomorrow
    IpoPeriod_Nextweek = 3; //To be listed next week
    IpoPeriod_Lastweek = 4; //Has been listed last week
    IpoPeriod_Lastmonth = 5; //Has been listed last month
}
```









**IpoPeriod**



``` protobuf
enum IpoPeriod
{
    IpoPeriod_Unknow = 0; //Unknown
    IpoPeriod_Today = 1; //Listed today
    IpoPeriod_Tomorrow = 2; //To be listed tomorrow
    IpoPeriod_Nextweek = 3; //To be listed next week
    IpoPeriod_Lastweek = 4; //Has been listed last week
    IpoPeriod_Lastmonth = 5; //Has been listed last month
}
```









**IpoPeriod**



``` protobuf
enum IpoPeriod
{
    IpoPeriod_Unknow = 0; //Unknown
    IpoPeriod_Today = 1; //Listed today
    IpoPeriod_Tomorrow = 2; //To be listed tomorrow
    IpoPeriod_Nextweek = 3; //To be listed next week
    IpoPeriod_Lastweek = 4; //Has been listed last week
    IpoPeriod_Lastmonth = 5; //Has been listed last month
}
```









**IpoPeriod**



``` protobuf
enum IpoPeriod
{
    IpoPeriod_Unknow = 0; //Unknown
    IpoPeriod_Today = 1; //Listed today
    IpoPeriod_Tomorrow = 2; //To be listed tomorrow
    IpoPeriod_Nextweek = 3; //To be listed next week
    IpoPeriod_Lastweek = 4; //Has been listed last week
    IpoPeriod_Lastmonth = 5; //Has been listed last month
}
```









**IpoPeriod**



``` protobuf
enum IpoPeriod
{
    IpoPeriod_Unknow = 0; //Unknown
    IpoPeriod_Today = 1; //Listed today
    IpoPeriod_Tomorrow = 2; //To be listed tomorrow
    IpoPeriod_Nextweek = 3; //To be listed next week
    IpoPeriod_Lastweek = 4; //Has been listed last week
    IpoPeriod_Lastmonth = 5; //Has been listed last month
}
```









## <a href="#5122" class="header-anchor">#</a> Warrant Issuer





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **Issuer**

- `UNKNOW`

  unknown

- `SG`

  Societe Generale

- `BP`

  BNP Paribas

- `CS`

  Credit Suisse

- `CT`

  Citi Bank

- `EA`

  The Bank of East Aisa

- `GS`

  Goldman Sachs

- `HS`

  HSBC

- `JP`

  JPMorgan Chase

- `MB`

  Macquarie Bank

- `SC`

  Standard Chartered Bank

- `UB`

  Union Bank of Switzerland

- `BI`

  Bank of China

- `DB`

  Deutsche Bank

- `DC`

  Daiwa Bank

- `ML`

  Merrill Lynch

- `NM`

  Nomura Bank

- `RB`

  Rabobank

- `RS`

  The Royal Bank of Scotland

- `BC`

  Barclays

- `HT`

  Haitong Bank

- `VT`

  Bank Vontobel

- `KC`

  KBC Bank

- `MS`

  Morgan Stanley

- `GJ`

  Guotai Junan

- `XZ`

  DBS Bank

- `HU`

  Huatai

- `KS`

  Korea Investment

- `CI`

  CITIC Securities





**Issuer**



``` protobuf
enum Issuer
{
    Issuer_Unknow = 0; //Unknown
    Issuer_SG = 1; //Societe Generale
    Issuer_BP = 2; //BNP Paribas
    Issuer_CS = 3; //Credit Suisse
    Issuer_CT = 4; //Citi Bank
    Issuer_EA = 5; //The Bank of East Aisa
    Issuer_GS = 6; //Goldman Sachs
    Issuer_HS = 7; //HSBC
    Issuer_JP = 8; //JPMorgan Chase
    Issuer_MB = 9; //Macquarie Bank
    Issuer_SC = 10; //Standard Chartered Bank
    Issuer_UB = 11; //Union Bank of Switzerland
    Issuer_BI = 12; //Bank of China
    Issuer_DB = 13; //Deutsche Bank
    Issuer_DC = 14; //Daiwa Bank
    Issuer_ML = 15; //Merrill Lynch
    Issuer_NM = 16; //Nomura Bank
    Issuer_RB = 17; //Rabobank
    Issuer_RS = 18; //The Royal Bank of Scotland
    Issuer_BC = 19; //Barclays
    Issuer_HT = 20; //Haitong Bank
    Issuer_VT = 21; //Bank Vontobel
    Issuer_KC = 22; //KBC Bank
    Issuer_MS = 23; //Morgan Stanley
    Issuer_GJ = 24; //Guotai Junan
    Issuer_XZ = 25; //DBS Bank
    Issuer_HU = 26; //Huatai
    Issuer_KS = 27; //Korea Investment
    Issuer_CI = 28; //CITIC Securities
}
```









**Issuer**



``` protobuf
enum Issuer
{
    Issuer_Unknow = 0; //Unknown
    Issuer_SG = 1; //Societe Generale
    Issuer_BP = 2; //BNP Paribas
    Issuer_CS = 3; //Credit Suisse
    Issuer_CT = 4; //Citi Bank
    Issuer_EA = 5; //The Bank of East Aisa
    Issuer_GS = 6; //Goldman Sachs
    Issuer_HS = 7; //HSBC
    Issuer_JP = 8; //JPMorgan Chase
    Issuer_MB = 9; //Macquarie Bank
    Issuer_SC = 10; //Standard Chartered Bank
    Issuer_UB = 11; //Union Bank of Switzerland
    Issuer_BI = 12; //Bank of China
    Issuer_DB = 13; //Deutsche Bank
    Issuer_DC = 14; //Daiwa Bank
    Issuer_ML = 15; //Merrill Lynch
    Issuer_NM = 16; //Nomura Bank
    Issuer_RB = 17; //Rabobank
    Issuer_RS = 18; //The Royal Bank of Scotland
    Issuer_BC = 19; //Barclays
    Issuer_HT = 20; //Haitong Bank
    Issuer_VT = 21; //Bank Vontobel
    Issuer_KC = 22; //KBC Bank
    Issuer_MS = 23; //Morgan Stanley
    Issuer_GJ = 24; //Guotai Junan
    Issuer_XZ = 25; //DBS Bank
    Issuer_HU = 26; //Huatai
    Issuer_KS = 27; //Korea Investment
    Issuer_CI = 28; //CITIC Securities
}
```









**Issuer**



``` protobuf
enum Issuer
{
    Issuer_Unknow = 0; //Unknown
    Issuer_SG = 1; //Societe Generale
    Issuer_BP = 2; //BNP Paribas
    Issuer_CS = 3; //Credit Suisse
    Issuer_CT = 4; //Citi Bank
    Issuer_EA = 5; //The Bank of East Aisa
    Issuer_GS = 6; //Goldman Sachs
    Issuer_HS = 7; //HSBC
    Issuer_JP = 8; //JPMorgan Chase
    Issuer_MB = 9; //Macquarie Bank
    Issuer_SC = 10; //Standard Chartered Bank
    Issuer_UB = 11; //Union Bank of Switzerland
    Issuer_BI = 12; //Bank of China
    Issuer_DB = 13; //Deutsche Bank
    Issuer_DC = 14; //Daiwa Bank
    Issuer_ML = 15; //Merrill Lynch
    Issuer_NM = 16; //Nomura Bank
    Issuer_RB = 17; //Rabobank
    Issuer_RS = 18; //The Royal Bank of Scotland
    Issuer_BC = 19; //Barclays
    Issuer_HT = 20; //Haitong Bank
    Issuer_VT = 21; //Bank Vontobel
    Issuer_KC = 22; //KBC Bank
    Issuer_MS = 23; //Morgan Stanley
    Issuer_GJ = 24; //Guotai Junan
    Issuer_XZ = 25; //DBS Bank
    Issuer_HU = 26; //Huatai
    Issuer_KS = 27; //Korea Investment
    Issuer_CI = 28; //CITIC Securities
}
```









**Issuer**



``` protobuf
enum Issuer
{
    Issuer_Unknow = 0; //Unknown
    Issuer_SG = 1; //Societe Generale
    Issuer_BP = 2; //BNP Paribas
    Issuer_CS = 3; //Credit Suisse
    Issuer_CT = 4; //Citi Bank
    Issuer_EA = 5; //The Bank of East Aisa
    Issuer_GS = 6; //Goldman Sachs
    Issuer_HS = 7; //HSBC
    Issuer_JP = 8; //JPMorgan Chase
    Issuer_MB = 9; //Macquarie Bank
    Issuer_SC = 10; //Standard Chartered Bank
    Issuer_UB = 11; //Union Bank of Switzerland
    Issuer_BI = 12; //Bank of China
    Issuer_DB = 13; //Deutsche Bank
    Issuer_DC = 14; //Daiwa Bank
    Issuer_ML = 15; //Merrill Lynch
    Issuer_NM = 16; //Nomura Bank
    Issuer_RB = 17; //Rabobank
    Issuer_RS = 18; //The Royal Bank of Scotland
    Issuer_BC = 19; //Barclays
    Issuer_HT = 20; //Haitong Bank
    Issuer_VT = 21; //Bank Vontobel
    Issuer_KC = 22; //KBC Bank
    Issuer_MS = 23; //Morgan Stanley
    Issuer_GJ = 24; //Guotai Junan
    Issuer_XZ = 25; //DBS Bank
    Issuer_HU = 26; //Huatai
    Issuer_KS = 27; //Korea Investment
    Issuer_CI = 28; //CITIC Securities
}
```









**Issuer**



``` protobuf
enum Issuer
{
    Issuer_Unknow = 0; //Unknown
    Issuer_SG = 1; //Societe Generale
    Issuer_BP = 2; //BNP Paribas
    Issuer_CS = 3; //Credit Suisse
    Issuer_CT = 4; //Citi Bank
    Issuer_EA = 5; //The Bank of East Aisa
    Issuer_GS = 6; //Goldman Sachs
    Issuer_HS = 7; //HSBC
    Issuer_JP = 8; //JPMorgan Chase
    Issuer_MB = 9; //Macquarie Bank
    Issuer_SC = 10; //Standard Chartered Bank
    Issuer_UB = 11; //Union Bank of Switzerland
    Issuer_BI = 12; //Bank of China
    Issuer_DB = 13; //Deutsche Bank
    Issuer_DC = 14; //Daiwa Bank
    Issuer_ML = 15; //Merrill Lynch
    Issuer_NM = 16; //Nomura Bank
    Issuer_RB = 17; //Rabobank
    Issuer_RS = 18; //The Royal Bank of Scotland
    Issuer_BC = 19; //Barclays
    Issuer_HT = 20; //Haitong Bank
    Issuer_VT = 21; //Bank Vontobel
    Issuer_KC = 22; //KBC Bank
    Issuer_MS = 23; //Morgan Stanley
    Issuer_GJ = 24; //Guotai Junan
    Issuer_XZ = 25; //DBS Bank
    Issuer_HU = 26; //Huatai
    Issuer_KS = 27; //Korea Investment
    Issuer_CI = 28; //CITIC Securities
}
```









## <a href="#5803" class="header-anchor">#</a> Candlestick Field





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **KL_FIELD**

- `ALL`

  All

- `DATE_TIME`

  Time

- `HIGH`

  High

- `OPEN`

  Open

- `LOW`

  Low

- `CLOSE`

  Close

- `LAST_CLOSE`

  Close yesterday

- `TRADE_VOL`

  Volume

- `TRADE_VAL`

  Turnover

- `TURNOVER_RATE`

  Turnover rate

- `PE_RATIO`

  P/E ratio

- `CHANGE_RATE`

  Yield





**KLFields**



``` protobuf
enum KLFields
{
    KLFields_None = 0; //
    KLFields_High = 1; //High
    KLFields_Open = 2; //Open
    KLFields_Low = 4; //Low
    KLFields_Close = 8; //Close
    KLFields_LastClose = 16; //Close yesterday
    KLFields_Volume = 32; //Volume
    KLFields_Turnover = 64; //Turnover
    KLFields_TurnoverRate = 128; //Turnover rate
    KLFields_PE = 256; //P/E ratio
    KLFields_ChangeRate = 512; //Yield
}
```









**KLFields**



``` protobuf
enum KLFields
{
    KLFields_None = 0; //
    KLFields_High = 1; //High
    KLFields_Open = 2; //Open
    KLFields_Low = 4; //Low
    KLFields_Close = 8; //Close
    KLFields_LastClose = 16; //Close yesterday
    KLFields_Volume = 32; //Volume
    KLFields_Turnover = 64; //Turnover
    KLFields_TurnoverRate = 128; //Turnover rate
    KLFields_PE = 256; //P/E ratio
    KLFields_ChangeRate = 512; //Yield
}
```









**KLFields**



``` protobuf
enum KLFields
{
    KLFields_None = 0; //
    KLFields_High = 1; //High
    KLFields_Open = 2; //Open
    KLFields_Low = 4; //Low
    KLFields_Close = 8; //Close
    KLFields_LastClose = 16; //Close yesterday
    KLFields_Volume = 32; //Volume
    KLFields_Turnover = 64; //Turnover
    KLFields_TurnoverRate = 128; //Turnover rate
    KLFields_PE = 256; //P/E ratio
    KLFields_ChangeRate = 512; //Yield
}
```









**KLFields**



``` protobuf
enum KLFields
{
    KLFields_None = 0; //
    KLFields_High = 1; //High
    KLFields_Open = 2; //Open
    KLFields_Low = 4; //Low
    KLFields_Close = 8; //Close
    KLFields_LastClose = 16; //Close yesterday
    KLFields_Volume = 32; //Volume
    KLFields_Turnover = 64; //Turnover
    KLFields_TurnoverRate = 128; //Turnover rate
    KLFields_PE = 256; //P/E ratio
    KLFields_ChangeRate = 512; //Yield
}
```









**KLFields**



``` protobuf
enum KLFields
{
    KLFields_None = 0; //
    KLFields_High = 1; //High
    KLFields_Open = 2; //Open
    KLFields_Low = 4; //Low
    KLFields_Close = 8; //Close
    KLFields_LastClose = 16; //Close yesterday
    KLFields_Volume = 32; //Volume
    KLFields_Turnover = 64; //Turnover
    KLFields_TurnoverRate = 128; //Turnover rate
    KLFields_PE = 256; //P/E ratio
    KLFields_ChangeRate = 512; //Yield
}
```









## <a href="#66" class="header-anchor">#</a> Candlestick Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **KLType**

- `NONE`

  unknown

- `K_1M`

  1 minute candlestick

- `K_DAY`

  1 day candlestick

- `K_WEEK`

  1 week candlestick

  

  
  

  

  
  
  

  Option is not supported

  

  

  

  

- `K_MON`

  1 month candlestick

  

  
  

  

  
  
  

  Option is not supported

  

  

  

  

- `K_YEAR`

  1 year candlestick

  

  
  

  

  
  
  

  Option is not supported

  

  

  

  

- `K_5M`

  5 minutes candlestick

- `K_15M`

  15 minutes candlestick

- `K_30M`

  30 minutes candlestick

  

  
  

  

  
  
  

  Option is not supported

  

  

  

  

- `K_60M`

  60 minutes candlestick

- `K_3M`

  3 minutes candlestick

  

  
  

  

  
  
  

  Option is not supported

  

  

  

  

- `K_QUARTER`

  1 quarter candlestick

  

  
  

  

  
  
  

  Option is not supported

  

  

  

  





**KLType**



``` protobuf
enum KLType
{
    KLType_Unknown = 0; //Unknown
    KLType_1Min = 1; //1 minute candlestick
    KLType_Day = 2; //1 day candlestick
    KLType_Week = 3; //1 week candlestick (Option is not supported)
    KLType_Month = 4; //1 month candlestick (Option is not supported)
    KLType_Year = 5; //1 year candlestick (Option is not supported)
    KLType_5Min = 6; //5 minutes candlestick
    KLType_15Min = 7; //15 minutes candlestick
    KLType_30Min = 8; //30 minutes candlestick (Option is not supported)
    KLType_60Min = 9; //60 minutes candlestick
    KLType_3Min = 10; //3 minutes candlestick (Option is not supported)
    KLType_Quarter = 11; //1 quarter candlestick (Option is not supported)
}
```









**KLType**



``` protobuf
enum KLType
{
    KLType_Unknown = 0; //Unknown
    KLType_1Min = 1; //1 minute candlestick
    KLType_Day = 2; //1 day candlestick
    KLType_Week = 3; //1 week candlestick (Option is not supported)
    KLType_Month = 4; //1 month candlestick (Option is not supported)
    KLType_Year = 5; //1 year candlestick (Option is not supported)
    KLType_5Min = 6; //5 minutes candlestick
    KLType_15Min = 7; //15 minutes candlestick
    KLType_30Min = 8; //30 minutes candlestick (Option is not supported)
    KLType_60Min = 9; //60 minutes candlestick
    KLType_3Min = 10; //3 minutes candlestick (Option is not supported)
    KLType_Quarter = 11; //1 quarter candlestick (Option is not supported)
}
```









**KLType**



``` protobuf
enum KLType
{
    KLType_Unknown = 0; //Unknown
    KLType_1Min = 1; //1 minute candlestick
    KLType_Day = 2; //1 day candlestick
    KLType_Week = 3; //1 week candlestick (Option is not supported)
    KLType_Month = 4; //1 month candlestick (Option is not supported)
    KLType_Year = 5; //1 year candlestick (Option is not supported)
    KLType_5Min = 6; //5 minutes candlestick
    KLType_15Min = 7; //15 minutes candlestick
    KLType_30Min = 8; //30 minutes candlestick (Option is not supported)
    KLType_60Min = 9; //60 minutes candlestick
    KLType_3Min = 10; //3 minutes candlestick (Option is not supported)
    KLType_Quarter = 11; //1 quarter candlestick (Option is not supported)
}
```









**KLType**



``` protobuf
enum KLType
{
    KLType_Unknown = 0; //Unknown
    KLType_1Min = 1; //1 minute candlestick
    KLType_Day = 2; //1 day candlestick
    KLType_Week = 3; //1 week candlestick (Option is not supported)
    KLType_Month = 4; //1 month candlestick (Option is not supported)
    KLType_Year = 5; //1 year candlestick (Option is not supported)
    KLType_5Min = 6; //5 minutes candlestick
    KLType_15Min = 7; //15 minutes candlestick
    KLType_30Min = 8; //30 minutes candlestick (Option is not supported)
    KLType_60Min = 9; //60 minutes candlestick
    KLType_3Min = 10; //3 minutes candlestick (Option is not supported)
    KLType_Quarter = 11; //1 quarter candlestick (Option is not supported)
}
```









**KLType**



``` protobuf
enum KLType
{
    KLType_Unknown = 0; //Unknown
    KLType_1Min = 1; //1 minute candlestick
    KLType_Day = 2; //1 day candlestick
    KLType_Week = 3; //1 week candlestick (Option is not supported)
    KLType_Month = 4; //1 month candlestick (Option is not supported)
    KLType_Year = 5; //1 year candlestick (Option is not supported)
    KLType_5Min = 6; //5 minutes candlestick
    KLType_15Min = 7; //15 minutes candlestick
    KLType_30Min = 8; //30 minutes candlestick (Option is not supported)
    KLType_60Min = 9; //60 minutes candlestick
    KLType_3Min = 10; //3 minutes candlestick (Option is not supported)
    KLType_Quarter = 11; //1 quarter candlestick (Option is not supported)
}
```









## <a href="#2884" class="header-anchor">#</a> Period Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PeriodType**

- `INTRADAY`

  Intraday

- `DAY`

  Day

- `WEEK`

  Week

- `MONTH`

  Month





**PeriodType**



``` protobuf
enum PeriodType
{
    PeriodType_INTRADAY = 0; //Intraday
    PeriodType_DAY = 1; //DAY
    PeriodType_WEEK = 2; //Week
    PeriodType_MONTH = 3; //Month
}
```









**PeriodType**



``` protobuf
enum PeriodType
{
    PeriodType_INTRADAY = 0; //Intraday
    PeriodType_DAY = 1; //DAY
    PeriodType_WEEK = 2; //Week
    PeriodType_MONTH = 3; //Month
}
```









**PeriodType**



``` protobuf
enum PeriodType
{
    PeriodType_INTRADAY = 0; //Intraday
    PeriodType_DAY = 1; //DAY
    PeriodType_WEEK = 2; //Week
    PeriodType_MONTH = 3; //Month
}
```









**PeriodType**



``` protobuf
enum PeriodType
{
    PeriodType_INTRADAY = 0; //Intraday
    PeriodType_DAY = 1; //DAY
    PeriodType_WEEK = 2; //Week
    PeriodType_MONTH = 3; //Month
}
```









**PeriodType**



``` protobuf
enum PeriodType
{
    PeriodType_INTRADAY = 0; //Intraday
    PeriodType_DAY = 1; //DAY
    PeriodType_WEEK = 2; //Week
    PeriodType_MONTH = 3; //Month
}
```









## <a href="#6578" class="header-anchor">#</a> Price Reminder Market Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PriceReminderMarketStatus**

- `UNKNOW`

  unknown

- `OPEN`

  Market opens

- `US_PRE`

  Pre-market of US stocks

- `US_AFTER`

  After-hours of US stocks

- `US_OVERNIGHT`

  Overnight trading session of US stocks





**MarketStatus**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Market opens
    MarketStatus_USPre = 2; //Pre-market
    MarketStatus_USAfter = 3; //After-hours
}
```









**MarketStatus**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Market opens
    MarketStatus_USPre = 2; //Pre-market
    MarketStatus_USAfter = 3; //After-hours
}
```









**MarketStatus**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Market opens
    MarketStatus_USPre = 2; //Pre-market
    MarketStatus_USAfter = 3; //After-hours
}
```









**MarketStatus**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Market opens
    MarketStatus_USPre = 2; //Pre-market
    MarketStatus_USAfter = 3; //After-hours
}
```









**MarketStatus**



``` protobuf
enum MarketStatus
{
    MarketStatus_Unknow = 0;
    MarketStatus_Open = 1; //Market opens
    MarketStatus_USPre = 2; //Pre-market
    MarketStatus_USAfter = 3; //After-hours
}
```









## <a href="#5843" class="header-anchor">#</a> Watchlist Operation





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **ModifyUserSecurityOp**

- `NONE`

  Unknown

- `ADD`

  Add

- `DEL`

  Delete

- `MOVE_OUT`

  Remove from group





**ModifyUserSecurityOp**



``` protobuf
enum ModifyUserSecurityOp
{
    ModifyUserSecurityOp_Unknown = 0; //Unknown
    ModifyUserSecurityOp_Add = 1; //Add
    ModifyUserSecurityOp_Del = 2; //Delete
    ModifyUserSecurityOp_MoveOut = 3; //Remove from group
}
```









**ModifyUserSecurityOp**



``` protobuf
enum ModifyUserSecurityOp
{
    ModifyUserSecurityOp_Unknown = 0; //Unknown
    ModifyUserSecurityOp_Add = 1; //Add
    ModifyUserSecurityOp_Del = 2; //Delete
    ModifyUserSecurityOp_MoveOut = 3; //Remove from group
}
```









**ModifyUserSecurityOp**



``` protobuf
enum ModifyUserSecurityOp
{
    ModifyUserSecurityOp_Unknown = 0; //Unknown
    ModifyUserSecurityOp_Add = 1; //Add
    ModifyUserSecurityOp_Del = 2; //Delete
    ModifyUserSecurityOp_MoveOut = 3; //Remove from group
}
```









**ModifyUserSecurityOp**



``` protobuf
enum ModifyUserSecurityOp
{
    ModifyUserSecurityOp_Unknown = 0; //Unknown
    ModifyUserSecurityOp_Add = 1; //Add
    ModifyUserSecurityOp_Del = 2; //Delete
    ModifyUserSecurityOp_MoveOut = 3; //Remove from group
}
```









**ModifyUserSecurityOp**



``` protobuf
enum ModifyUserSecurityOp
{
    ModifyUserSecurityOp_Unknown = 0; //Unknown
    ModifyUserSecurityOp_Add = 1; //Add
    ModifyUserSecurityOp_Del = 2; //Delete
    ModifyUserSecurityOp_MoveOut = 3; //Remove from group
}
```









## <a href="#3628" class="header-anchor">#</a> Option Type (by Exercise Time)





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OptionAreaType**

- `NONE`

  unknown

- `AMERICAN`

  American Option

- `EUROPEAN`

  European Option

- `BERMUDA`

  Bermuda Option





**OptionAreaType**



``` protobuf
enum OptionAreaType
{
    OptionAreaType_Unknown = 0; //Unknown
    OptionAreaType_American = 1; //American Option
    OptionAreaType_European = 2; //European Option
    OptionAreaType_Bermuda = 3; //Bermuda Option
}
```









**OptionAreaType**



``` protobuf
enum OptionAreaType
{
    OptionAreaType_Unknown = 0; //Unknown
    OptionAreaType_American = 1; //American Option
    OptionAreaType_European = 2; //European Option
    OptionAreaType_Bermuda = 3; //Bermuda Option
}
```









**OptionAreaType**



``` protobuf
enum OptionAreaType
{
    OptionAreaType_Unknown = 0; //Unknown
    OptionAreaType_American = 1; //American Option
    OptionAreaType_European = 2; //European Option
    OptionAreaType_Bermuda = 3; //Bermuda Option
}
```









**OptionAreaType**



``` protobuf
enum OptionAreaType
{
    OptionAreaType_Unknown = 0; //Unknown
    OptionAreaType_American = 1; //American Option
    OptionAreaType_European = 2; //European Option
    OptionAreaType_Bermuda = 3; //Bermuda Option
}
```









**OptionAreaType**



``` protobuf
enum OptionAreaType
{
    OptionAreaType_Unknown = 0; //Unknown
    OptionAreaType_American = 1; //American Option
    OptionAreaType_European = 2; //European Option
    OptionAreaType_Bermuda = 3; //Bermuda Option
}
```









## <a href="#9027" class="header-anchor">#</a> Option in/out of The Money





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OptionCondType**

- `ALL`

  All

- `WITHIN`

  In the money

- `OUTSIDE`

  Out of the money





**OptionCondType**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0; //All
    OptionCondType_WithIn = 1; //In the money
    OptionCondType_Outside = 2; //Out of the money
}
```









**OptionCondType**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0; //All
    OptionCondType_WithIn = 1; //In the money
    OptionCondType_Outside = 2; //Out of the money
}
```









**OptionCondType**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0; //All
    OptionCondType_WithIn = 1; //In the money
    OptionCondType_Outside = 2; //Out of the money
}
```









**OptionCondType**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0; //All
    OptionCondType_WithIn = 1; //In the money
    OptionCondType_Outside = 2; //Out of the money
}
```









**OptionCondType**



``` protobuf
enum OptionCondType
{
    OptionCondType_Unknow = 0; //All
    OptionCondType_WithIn = 1; //In the money
    OptionCondType_Outside = 2; //Out of the money
}
```









## <a href="#9598" class="header-anchor">#</a> Option Type (by Direction)





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OptionType**

- `ALL`

  all

- `CALL`

  Call option

- `PUT`

  Put option





**OptionType**



``` protobuf
enum OptionType
{
    OptionType_Unknown = 0; //Unknown
    OptionType_Call = 1; //Call option
    OptionType_Put = 2; //Put option
};
```









**OptionType**



``` protobuf
enum OptionType
{
    OptionType_Unknown = 0; //Unknown
    OptionType_Call = 1; //Call option
    OptionType_Put = 2; //Put option
};
```









**OptionType**



``` protobuf
enum OptionType
{
    OptionType_Unknown = 0; //Unknown
    OptionType_Call = 1; //Call option
    OptionType_Put = 2; //Put option
};
```









**OptionType**



``` protobuf
enum OptionType
{
    OptionType_Unknown = 0; //Unknown
    OptionType_Call = 1; //Call option
    OptionType_Put = 2; //Put option
};
```









**OptionType**



``` protobuf
enum OptionType
{
    OptionType_Unknown = 0; //Unknown
    OptionType_Call = 1; //Call option
    OptionType_Put = 2; //Put option
};
```









## <a href="#978" class="header-anchor">#</a> Plate Set Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **Plate**

- `ALL`

  All plates

- `INDUSTRY`

  Industry plate

- `REGION`

  Regional plate

  

  
  

  

  
  
  

  The regional plate of the Hong Kong and US stock markets are
  temporarily empty.

  

  

  

  

- `CONCEPT`

  Concept plate

- `OTHER`

  Other plates

  

  
  

  

  
  
  

  Only used for the return of the [Get plates of
  stocks](/moomoo-api-doc/en/quote/get-owner-plate.html) interface and
  cannot be used as a request parameter of other interfaces.

  

  

  

  





**PlateSetType**



``` protobuf
enum PlateSetType
{
    PlateSetType_All = 0; //All plate
    PlateSetType_Industry = 1; //Industry plate
    PlateSetType_Region = 2; //Regional plate (the regional plate of the Hong Kong and US stock markets are temporarily empty)
    PlateSetType_Concept = 3; //Concept plate
    PlateSetType_Other = 4; //Other plates, only used for 3207 (acquiring the plate to which the stock belongs) protocol return, and cannot be used as a request parameter of other protocols
}
```









**PlateSetType**



``` protobuf
enum PlateSetType
{
    PlateSetType_All = 0; //All plate
    PlateSetType_Industry = 1; //Industry plate
    PlateSetType_Region = 2; //Regional plate (the regional plate of the Hong Kong and US stock markets are temporarily empty)
    PlateSetType_Concept = 3; //Concept plate
    PlateSetType_Other = 4; //Other plates, only used for 3207 (acquiring the plate to which the stock belongs) protocol return, and cannot be used as a request parameter of other protocols
}
```









**PlateSetType**



``` protobuf
enum PlateSetType
{
    PlateSetType_All = 0; //All plate
    PlateSetType_Industry = 1; //Industry plate
    PlateSetType_Region = 2; //Regional plate (the regional plate of the Hong Kong and US stock markets are temporarily empty)
    PlateSetType_Concept = 3; //Concept plate
    PlateSetType_Other = 4; //Other plates, only used for 3207 (acquiring the plate to which the stock belongs) protocol return, and cannot be used as a request parameter of other protocols
}
```









**PlateSetType**



``` protobuf
enum PlateSetType
{
    PlateSetType_All = 0; //All plate
    PlateSetType_Industry = 1; //Industry plate
    PlateSetType_Region = 2; //Regional plate (the regional plate of the Hong Kong and US stock markets are temporarily empty)
    PlateSetType_Concept = 3; //Concept plate
    PlateSetType_Other = 4; //Other plates, only used for 3207 (acquiring the plate to which the stock belongs) protocol return, and cannot be used as a request parameter of other protocols
}
```









**PlateSetType**



``` protobuf
enum PlateSetType
{
    PlateSetType_All = 0; //All plate
    PlateSetType_Industry = 1; //Industry plate
    PlateSetType_Region = 2; //Regional plate (the regional plate of the Hong Kong and US stock markets are temporarily empty)
    PlateSetType_Concept = 3; //Concept plate
    PlateSetType_Other = 4; //Other plates, only used for 3207 (acquiring the plate to which the stock belongs) protocol return, and cannot be used as a request parameter of other protocols
}
```









## <a href="#9918" class="header-anchor">#</a> Price Reminder Frequency





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PriceReminderFreq**

- `NONE`

  Unknown

- `ALWAYS`

  Keep reminding

- `ONCE_A_DAY`

  Once a day

- `ONCE`

  Only remind once





**PriceReminderFreq**



``` protobuf
enum PriceReminderFreq
{
    PriceReminderFreq_Unknown = 0; //Unknown
    PriceReminderFreq_Always = 1; //Keep reminding
    PriceReminderFreq_OnceADay = 2; //Once a day
    PriceReminderFreq_OnlyOnce = 3; //Only remind once
}
```









**PriceReminderFreq**



``` protobuf
enum PriceReminderFreq
{
    PriceReminderFreq_Unknown = 0; //Unknown
    PriceReminderFreq_Always = 1; //Keep reminding
    PriceReminderFreq_OnceADay = 2; //Once a day
    PriceReminderFreq_OnlyOnce = 3; //Only remind once
}
```









**PriceReminderFreq**



``` protobuf
enum PriceReminderFreq
{
    PriceReminderFreq_Unknown = 0; //Unknown
    PriceReminderFreq_Always = 1; //Keep reminding
    PriceReminderFreq_OnceADay = 2; //Once a day
    PriceReminderFreq_OnlyOnce = 3; //Only remind once
}
```









**PriceReminderFreq**



``` protobuf
enum PriceReminderFreq
{
    PriceReminderFreq_Unknown = 0; //Unknown
    PriceReminderFreq_Always = 1; //Keep reminding
    PriceReminderFreq_OnceADay = 2; //Once a day
    PriceReminderFreq_OnlyOnce = 3; //Only remind once
}
```









**PriceReminderFreq**



``` protobuf
enum PriceReminderFreq
{
    PriceReminderFreq_Unknown = 0; //Unknown
    PriceReminderFreq_Always = 1; //Keep reminding
    PriceReminderFreq_OnceADay = 2; //Once a day
    PriceReminderFreq_OnlyOnce = 3; //Only remind once
}
```









## <a href="#3793" class="header-anchor">#</a> Price Reminder Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PriceReminderType**

- `NONE`

  Unknown

- `PRICE_UP`

  Price rise to

- `PRICE_DOWN`

  Price fall to

- `CHANGE_RATE_UP`

  Daily increase rate exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  

- `CHANGE_RATE_DOWN`

  Daily decline rate exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  

- `FIVE_MIN_CHANGE_RATE_UP`

  Increate rate in 5 minutes exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  

- `FIVE_MIN_CHANGE_RATE_DOWN`

  Decline rate in 5 minutes exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  

- `VOLUME_UP`

  Volume exceeds

- `TURNOVER_UP`

  Turnover exceeds

- `TURNOVER_RATE_UP`

  Turnover rate exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  

- `BID_PRICE_UP`

  Bid price higher than

- `ASK_PRICE_DOWN`

  Ask price lower than

- `BID_VOL_UP`

  Bid volume higher than

- `ASK_VOL_UP`

  Ask volume higher than

- `THREE_MIN_CHANGE_RATE_UP`

  Increate rate in 3 minutes exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  

- `THREE_MIN_CHANGE_RATE_DOWN`

  Decline rate in 3 minutes exceeds

  

  
  

  

  
  
  

  This field is in percentage form, so 20 is equivalent to 20%.

  

  

  

  





**PriceReminderType**



``` protobuf
enum PriceReminderType
{
    PriceReminderType_Unknown = 0; //Unknown
    PriceReminderType_PriceUp = 1; //Price rise to
    PriceReminderType_PriceDown = 2; //Price fall to
    PriceReminderType_ChangeRateUp = 3; //Daily increase rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_ChangeRateDown = 4; //Daily decline rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateUp = 5; //Increate rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateDown = 6; //Decline rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_VolumeUp = 7; //Volume exceeds
    PriceReminderType_TurnoverUp = 8; //Turnover exceeds
    PriceReminderType_TurnoverRateUp = 9; //Turnover rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_BidPriceUp = 10; //Bid price higher than
    PriceReminderType_AskPriceDown = 11; //Ask price lower than
    PriceReminderType_BidVolUp = 12; //Bid volume higher than
    PriceReminderType_AskVolUp = 13; //Ask volume higher than
    PriceReminderType_3MinChangeRateUp = 14; //Increate rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_3MinChangeRateDown = 15; //Decline rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**PriceReminderType**



``` protobuf
enum PriceReminderType
{
    PriceReminderType_Unknown = 0; //Unknown
    PriceReminderType_PriceUp = 1; //Price rise to
    PriceReminderType_PriceDown = 2; //Price fall to
    PriceReminderType_ChangeRateUp = 3; //Daily increase rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_ChangeRateDown = 4; //Daily decline rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateUp = 5; //Increate rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateDown = 6; //Decline rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_VolumeUp = 7; //Volume exceeds
    PriceReminderType_TurnoverUp = 8; //Turnover exceeds
    PriceReminderType_TurnoverRateUp = 9; //Turnover rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_BidPriceUp = 10; //Bid price higher than
    PriceReminderType_AskPriceDown = 11; //Ask price lower than
    PriceReminderType_BidVolUp = 12; //Bid volume higher than
    PriceReminderType_AskVolUp = 13; //Ask volume higher than
    PriceReminderType_3MinChangeRateUp = 14; //Increate rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_3MinChangeRateDown = 15; //Decline rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**PriceReminderType**



``` protobuf
enum PriceReminderType
{
    PriceReminderType_Unknown = 0; //Unknown
    PriceReminderType_PriceUp = 1; //Price rise to
    PriceReminderType_PriceDown = 2; //Price fall to
    PriceReminderType_ChangeRateUp = 3; //Daily increase rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_ChangeRateDown = 4; //Daily decline rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateUp = 5; //Increate rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateDown = 6; //Decline rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_VolumeUp = 7; //Volume exceeds
    PriceReminderType_TurnoverUp = 8; //Turnover exceeds
    PriceReminderType_TurnoverRateUp = 9; //Turnover rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_BidPriceUp = 10; //Bid price higher than
    PriceReminderType_AskPriceDown = 11; //Ask price lower than
    PriceReminderType_BidVolUp = 12; //Bid volume higher than
    PriceReminderType_AskVolUp = 13; //Ask volume higher than
    PriceReminderType_3MinChangeRateUp = 14; //Increate rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_3MinChangeRateDown = 15; //Decline rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**PriceReminderType**



``` protobuf
enum PriceReminderType
{
    PriceReminderType_Unknown = 0; //Unknown
    PriceReminderType_PriceUp = 1; //Price rise to
    PriceReminderType_PriceDown = 2; //Price fall to
    PriceReminderType_ChangeRateUp = 3; //Daily increase rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_ChangeRateDown = 4; //Daily decline rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateUp = 5; //Increate rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateDown = 6; //Decline rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_VolumeUp = 7; //Volume exceeds
    PriceReminderType_TurnoverUp = 8; //Turnover exceeds
    PriceReminderType_TurnoverRateUp = 9; //Turnover rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_BidPriceUp = 10; //Bid price higher than
    PriceReminderType_AskPriceDown = 11; //Ask price lower than
    PriceReminderType_BidVolUp = 12; //Bid volume higher than
    PriceReminderType_AskVolUp = 13; //Ask volume higher than
    PriceReminderType_3MinChangeRateUp = 14; //Increate rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_3MinChangeRateDown = 15; //Decline rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









**PriceReminderType**



``` protobuf
enum PriceReminderType
{
    PriceReminderType_Unknown = 0; //Unknown
    PriceReminderType_PriceUp = 1; //Price rise to
    PriceReminderType_PriceDown = 2; //Price fall to
    PriceReminderType_ChangeRateUp = 3; //Daily increase rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_ChangeRateDown = 4; //Daily decline rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateUp = 5; //Increate rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_5MinChangeRateDown = 6; //Decline rate in 5 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_VolumeUp = 7; //Volume exceeds
    PriceReminderType_TurnoverUp = 8; //Turnover exceeds
    PriceReminderType_TurnoverRateUp = 9; //Turnover rate exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_BidPriceUp = 10; //Bid price higher than
    PriceReminderType_AskPriceDown = 11; //Ask price lower than
    PriceReminderType_BidVolUp = 12; //Bid volume higher than
    PriceReminderType_AskVolUp = 13; //Ask volume higher than
    PriceReminderType_3MinChangeRateUp = 14; //Increate rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
    PriceReminderType_3MinChangeRateDown = 15; //Decline rate in 3 minutes exceeds (This field is in percentage form, so 20 is equivalent to 20%.)
}
```









## <a href="#9794" class="header-anchor">#</a> Warrant in/out of the Money





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PriceType**

- `UNKNOW`

  Unknown

- `OUTSIDE`

  Out of the money

- `WITH_IN`

  In the money





**PriceType**



``` protobuf
enum PriceType
{
    PriceType_Unknow = 0; //Unknown
    PriceType_Outside = 1; //Out of the money
    PriceType_WithIn = 2; //In the money
}
```









**PriceType**



``` protobuf
enum PriceType
{
    PriceType_Unknow = 0; //Unknown
    PriceType_Outside = 1; //Out of the money
    PriceType_WithIn = 2; //In the money
}
```









**PriceType**



``` protobuf
enum PriceType
{
    PriceType_Unknow = 0; //Unknown
    PriceType_Outside = 1; //Out of the money
    PriceType_WithIn = 2; //In the money
}
```









**PriceType**



``` protobuf
enum PriceType
{
    PriceType_Unknow = 0; //Unknown
    PriceType_Outside = 1; //Out of the money
    PriceType_WithIn = 2; //In the money
}
```









**PriceType**



``` protobuf
enum PriceType
{
    PriceType_Unknow = 0; //Unknown
    PriceType_Outside = 1; //Out of the money
    PriceType_WithIn = 2; //In the money
}
```









## <a href="#2567" class="header-anchor">#</a> Quote Push Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PushDataType**

- `UNKNOW`

  Unknown

- `REALTIME`

  Real-time data

- `BYDISCONN`

  Pull supplementary data (up to 50) during disconnection from Futu
  server

- `CACHE`

  Non-real-time non-supplementary data





**PushDataType**



``` protobuf
enum PushDataType
{
    PushDataType_Unknow = 0; //Unknown
    PushDataType_Real-time = 1; //Real-time data
    PushDataType_ByDisConn = 2; //Pull supplementary data during the disconnection of the background market (up to 50)
    PushDataType_Cache = 3; //Non-real-time non-supplementary data
}
```









**PushDataType**



``` protobuf
enum PushDataType
{
    PushDataType_Unknow = 0; //Unknown
    PushDataType_Real-time = 1; //Real-time data
    PushDataType_ByDisConn = 2; //Pull supplementary data during the disconnection of the background market (up to 50)
    PushDataType_Cache = 3; //Non-real-time non-supplementary data
}
```









**PushDataType**



``` protobuf
enum PushDataType
{
    PushDataType_Unknow = 0; //Unknown
    PushDataType_Real-time = 1; //Real-time data
    PushDataType_ByDisConn = 2; //Pull supplementary data during the disconnection of the background market (up to 50)
    PushDataType_Cache = 3; //Non-real-time non-supplementary data
}
```









**PushDataType**



``` protobuf
enum PushDataType
{
    PushDataType_Unknow = 0; //Unknown
    PushDataType_Real-time = 1; //Real-time data
    PushDataType_ByDisConn = 2; //Pull supplementary data during the disconnection of the background market (up to 50)
    PushDataType_Cache = 3; //Non-real-time non-supplementary data
}
```









**PushDataType**



``` protobuf
enum PushDataType
{
    PushDataType_Unknow = 0; //Unknown
    PushDataType_Real-time = 1; //Real-time data
    PushDataType_ByDisConn = 2; //Pull supplementary data during the disconnection of the background market (up to 50)
    PushDataType_Cache = 3; //Non-real-time non-supplementary data
}
```









## <a href="#456" class="header-anchor">#</a> Quote Market





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **Market**

- `NONE`

  Unknown market

- `HK`

  HK market

- `US`

  US market

- `SH`

  Shanghai market

- `SZ`

  Shenzhen market

- `SG`

  Singapore market

- `JP`

  Japanese market

- `AU`

  Australian market

- `MY`

  Malaysian market

- `CA`

  Canadian market

- `FX`

  Forex market





**QotMarket**



``` protobuf
enum QotMarket
{
    QotMarket_Unknown = 0; //Unknown market
    QotMarket_HK_Security = 1; //HK market
    QotMarket_HK_Future = 2; //Hong Kong futures market (deprecated, just use QotMarket_HK_Security)
    QotMarket_US_Security = 11; //US market
    QotMarket_CNSH_Security = 21; //Shanghai market
    QotMarket_CNSZ_Security = 22; //Shenzhen market
    QotMarket_SG_Security = 31; //Singapore market
    QotMarket_JP_Security = 41; //Japanese market
    QotMarket_AU_Security = 51; //Australian market
    QotMarket_MY_Security = 61; //Malaysian market
    QotMarket_CA_Security = 71; //Canadian market
    QotMarket_FX_Security = 81; //Forex market

}
```









**QotMarket**



``` protobuf
enum QotMarket
{
    QotMarket_Unknown = 0; //Unknown market
    QotMarket_HK_Security = 1; //Hong Kong stock market
    QotMarket_HK_Future = 2; //Hong Kong futures market (deprecated, just use QotMarket_HK_Security)
    QotMarket_US_Security = 11; //US stock market
    QotMarket_CNSH_Security = 21; //Shanghai stock market
    QotMarket_CNSZ_Security = 22; //Shenzhen stock market
    QotMarket_SG_Security = 31; //Singapore market
    QotMarket_JP_Security = 41; //Japanese market
    QotMarket_AU_Security = 51; //Australian market
    QotMarket_MY_Security = 61; //Malaysian market
    QotMarket_CA_Security = 71; //Canadian market
    QotMarket_FX_Security = 81; //Forex market
}
```









**QotMarket**



``` protobuf
enum QotMarket
{
    QotMarket_Unknown = 0; //Unknown market
    QotMarket_HK_Security = 1; //Hong Kong stock market
    QotMarket_HK_Future = 2; //Hong Kong futures market (deprecated, just use QotMarket_HK_Security)
    QotMarket_US_Security = 11; //US stock market
    QotMarket_CNSH_Security = 21; //Shanghai stock market
    QotMarket_CNSZ_Security = 22; //Shenzhen stock market
    QotMarket_SG_Security = 31; //Singapore market
    QotMarket_JP_Security = 41; //Japanese market
    QotMarket_AU_Security = 51; //Australian market
    QotMarket_MY_Security = 61; //Malaysian market
    QotMarket_CA_Security = 71; //Canadian market
    QotMarket_FX_Security = 81; //Forex market
}
```









**QotMarket**



``` protobuf
enum QotMarket
{
    QotMarket_Unknown = 0; //Unknown market
    QotMarket_HK_Security = 1; //Hong Kong stock market
    QotMarket_HK_Future = 2; //Hong Kong futures market (deprecated, just use QotMarket_HK_Security)
    QotMarket_US_Security = 11; //US stock market
    QotMarket_CNSH_Security = 21; //Shanghai stock market
    QotMarket_CNSZ_Security = 22; //Shenzhen stock market
    QotMarket_SG_Security = 31; //Singapore market
    QotMarket_JP_Security = 41; //Japanese market
    QotMarket_AU_Security = 51; //Australian market
    QotMarket_MY_Security = 61; //Malaysian market
    QotMarket_CA_Security = 71; //Canadian market
    QotMarket_FX_Security = 81; //Forex market
}
```









**QotMarket**



``` protobuf
enum QotMarket
{
    QotMarket_Unknown = 0; //Unknown market
    QotMarket_HK_Security = 1; //Hong Kong stock market
    QotMarket_HK_Future = 2; //Hong Kong futures market (deprecated, just use QotMarket_HK_Security)
    QotMarket_US_Security = 11; //US stock market
    QotMarket_CNSH_Security = 21; //Shanghai stock market
    QotMarket_CNSZ_Security = 22; //Shenzhen stock market
    QotMarket_SG_Security = 31; //Singapore market
    QotMarket_JP_Security = 41; //Japanese market
    QotMarket_AU_Security = 51; //Australian market
    QotMarket_MY_Security = 61; //Malaysian market
    QotMarket_CA_Security = 71; //Canadian market
    QotMarket_FX_Security = 81; //Forex market
}
```









## <a href="#8663" class="header-anchor">#</a> Market State





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **MarketState**

Corresponding time period of each market state, [click
here](/moomoo-api-doc/en/qa/quote.html#2076) to learn more

- `NONE`

  No trading

- `AUCTION`

  Pre-market trading

- `WAITING_OPEN`

  Waiting for opening

- `MORNING`

  Morning session

- `REST`

  Lunch break

- `AFTERNOON`

  Afternoon session / Regular trading hours for U.S stock market

- `CLOSED`

  Market closed

- `PRE_MARKET_BEGIN`

  Pre-market trading of U.S stock market

- `PRE_MARKET_END`

  Pre-market ending of U.S stock market

- `AFTER_HOURS_BEGIN`

  After-hours trading of U.S stock market

- `AFTER_HOURS_END`

  Market closed of U.S. stock market

- `OVERNIGHT`

  Overnight trading of U.S. stock market

- `NIGHT_OPEN`

  Night market trading hours

- `NIGHT_END`

  Night market closed

- `NIGHT`

  Night market trading hours for U.S. index options

- `TRADE_AT_LAST`

  Late trading hours for U.S. index options

- `FUTURE_DAY_OPEN`

  Day market trading hours

- `FUTURE_DAY_BREAK`

  Day market break

- `FUTURE_DAY_CLOSE`

  Day market closed

- `FUTURE_DAY_WAIT_OPEN`

  Futures market wait for opening

- `HK_CAS`

  After-hours bidding for HK stocks

- `FUTURE_NIGHT_WAIT`

  Futures night market wait for opening (Obsolete)

- `FUTURE_AFTERNOON`

  Futures afternoon (Obsolete)

- `FUTURE_SWITCH_DATE`

  Waiting for U.S. futures opening

- `FUTURE_OPEN`

  Trading hours of U.S. futures

- `FUTURE_BREAK`

  Break of U.S. futures

- `FUTURE_BREAK_OVER`

  Trading hours of U.S. futures after break

- `FUTURE_CLOSE`

  Market closed of U.S. futures

- `STIB_AFTER_HOURS_WAIT`

  After-hours matching period on the Sci-tech innovation plate
  (Obsolete)

- `STIB_AFTER_HOURS_BEGIN`

  After-hours trading on the Sci-tech innovation plate begins (Obsolete)

- `STIB_AFTER_HOURS_END`

  After-hours trading on the Sci-tech innovation plate ends (Obsolete)





**QotMarketState**

Corresponding time period of each market state, [click
here](/moomoo-api-doc/en/qa/quote.html#2076) to learn more



``` protobuf
enum QotMarketState
{
    QotMarketState_None = 0; //No trading
    QotMarketState_Auction = 1; //Pre-market trading
    QotMarketState_WaitingOpen = 2; //Waiting for opening
    QotMarketState_Morning = 3; //Morning session
    QotMarketState_Rest = 4; //Lunch break
    QotMarketState_Afternoon = 5; //Afternoon session / Regular trading hours for U.S stock market
    QotMarketState_Closed = 6; //Market closed
    QotMarketState_PreMarketBegin = 8; //Pre-market trading of U.S stock market
    QotMarketState_PreMarketEnd = 9; //Pre-market ending of U.S stock market
    QotMarketState_AfterHoursBegin = 10; //After-hours trading of U.S stock market
    QotMarketState_AfterHoursEnd = 11; //Market closed of U.S. stock market
    QotMarketState_NightOpen = 13; //Night market trading hours
    QotMarketState_NightEnd = 14; //Night market closed
    QotMarketState_FutureDayOpen = 15; //Day market trading hours
    QotMarketState_FutureDayBreak = 16; //Day market break
    QotMarketState_FutureDayClose = 17; //Day market closed
    QotMarketState_FutureDayWaitForOpen = 18; //Futures market wait for opening
    QotMarketState_HkCas = 19; //After-hours bidding
    QotMarketState_FutureNightWait = 20; //Futures night market wait for opening (Obsolete)
    QotMarketState_FutureAfternoon = 21; //Futures afternoon (Obsolete)
    //New status of US futures
    QotMarketState_FutureSwitchDate = 22; //Waiting for U.S. futures opening
    QotMarketState_FutureOpen = 23; //Trading hours of U.S. futures
    QotMarketState_FutureBreak = 24; //Break of U.S. futures
    QotMarketState_FutureBreakOver = 25; //Trading hours of U.S. futures after break
    QotMarketState_FutureClose = 26; //Market closed of U.S. futures
    //New status of Sci-tech Innovation Board
    QotMarketState_StibAfterHoursWait = 27; //After-hours matching period on the Sci-tech innovation plate(Obsolete)
    QotMarketState_StibAfterHoursBegin = 28; //After-hours trading on the Sci-tech innovation plate begins(Obsolete)
    QotMarketState_StibAfterHoursEnd = 29; //After-hours trading on the Sci-tech innovation plate ends(Obsolete)
    //New status for US index options
    QotMarketState_NIGHT = 32; //Night trading hours of U.S. index options
    QotMarketState_TRADE_AT_LAST = 35; //Late trading hours of U.S. index options
    QotMarketState_OVERNIGHT = 37;  //Overnight trading hours for U.S stock market
}
```









**QotMarketState**

Corresponding time period of each market state, [click
here](/moomoo-api-doc/en/qa/quote.html#2076) to learn more



``` protobuf
enum QotMarketState
{
    QotMarketState_None = 0; //No trading
    QotMarketState_Auction = 1; //Pre-market trading
    QotMarketState_WaitingOpen = 2; //Waiting for opening
    QotMarketState_Morning = 3; //Morning session
    QotMarketState_Rest = 4; //Lunch break
    QotMarketState_Afternoon = 5; //Afternoon session / Regular trading hours for U.S stock market
    QotMarketState_Closed = 6; //Market closed
    QotMarketState_PreMarketBegin = 8; //Pre-market trading of U.S stock market
    QotMarketState_PreMarketEnd = 9; //Pre-market ending of U.S stock market
    QotMarketState_AfterHoursBegin = 10; //After-hours trading of U.S stock market
    QotMarketState_AfterHoursEnd = 11; //Market closed of U.S. stock market
    QotMarketState_NightOpen = 13; //Night market trading hours
    QotMarketState_NightEnd = 14; //Night market closed
    QotMarketState_FutureDayOpen = 15; //Day market trading hours
    QotMarketState_FutureDayBreak = 16; //Day market break
    QotMarketState_FutureDayClose = 17; //Day market closed
    QotMarketState_FutureDayWaitForOpen = 18; //Futures market wait for opening
    QotMarketState_HkCas = 19; //After-hours bidding
    QotMarketState_FutureNightWait = 20; //Futures night market wait for opening (Obsolete)
    QotMarketState_FutureAfternoon = 21; //Futures afternoon (Obsolete)
    //New status of US futures
    QotMarketState_FutureSwitchDate = 22; //Waiting for U.S. futures opening
    QotMarketState_FutureOpen = 23; //Trading hours of U.S. futures
    QotMarketState_FutureBreak = 24; //Break of U.S. futures
    QotMarketState_FutureBreakOver = 25; //Trading hours of U.S. futures after break
    QotMarketState_FutureClose = 26; //Market closed of U.S. futures
    //New status of Sci-tech Innovation Board
    QotMarketState_StibAfterHoursWait = 27; //After-hours matching period on the Sci-tech innovation plate(Obsolete)
    QotMarketState_StibAfterHoursBegin = 28; //After-hours trading on the Sci-tech innovation plate begins(Obsolete)
    QotMarketState_StibAfterHoursEnd = 29; //After-hours trading on the Sci-tech innovation plate ends(Obsolete)
    //New status for US index options
    QotMarketState_NIGHT = 32; //Night trading hours of U.S. index options
    QotMarketState_TRADE_AT_LAST = 35; //Late trading hours of U.S. index options
    QotMarketState_OVERNIGHT = 37;  //Overnight trading hours for U.S stock market
}
```









**QotMarketState**

Corresponding time period of each market state, [click
here](/moomoo-api-doc/en/qa/quote.html#2076) to learn more



``` protobuf
enum QotMarketState
{
    QotMarketState_None = 0; //No trading
    QotMarketState_Auction = 1; //Pre-market trading
    QotMarketState_WaitingOpen = 2; //Waiting for opening
    QotMarketState_Morning = 3; //Morning session
    QotMarketState_Rest = 4; //Lunch break
    QotMarketState_Afternoon = 5; //Afternoon session / Regular trading hours for U.S stock market
    QotMarketState_Closed = 6; //Market closed
    QotMarketState_PreMarketBegin = 8; //Pre-market trading of U.S stock market
    QotMarketState_PreMarketEnd = 9; //Pre-market ending of U.S stock market
    QotMarketState_AfterHoursBegin = 10; //After-hours trading of U.S stock market
    QotMarketState_AfterHoursEnd = 11; //Market closed of U.S. stock market
    QotMarketState_NightOpen = 13; //Night market trading hours
    QotMarketState_NightEnd = 14; //Night market closed
    QotMarketState_FutureDayOpen = 15; //Day market trading hours
    QotMarketState_FutureDayBreak = 16; //Day market break
    QotMarketState_FutureDayClose = 17; //Day market closed
    QotMarketState_FutureDayWaitForOpen = 18; //Futures market wait for opening
    QotMarketState_HkCas = 19; //After-hours bidding
    QotMarketState_FutureNightWait = 20; //Futures night market wait for opening (Obsolete)
    QotMarketState_FutureAfternoon = 21; //Futures afternoon (Obsolete)
    //New status of US futures
    QotMarketState_FutureSwitchDate = 22; //Waiting for U.S. futures opening
    QotMarketState_FutureOpen = 23; //Trading hours of U.S. futures
    QotMarketState_FutureBreak = 24; //Break of U.S. futures
    QotMarketState_FutureBreakOver = 25; //Trading hours of U.S. futures after break
    QotMarketState_FutureClose = 26; //Market closed of U.S. futures
    //New status of Sci-tech Innovation Board
    QotMarketState_StibAfterHoursWait = 27; //After-hours matching period on the Sci-tech innovation plate(Obsolete)
    QotMarketState_StibAfterHoursBegin = 28; //After-hours trading on the Sci-tech innovation plate begins(Obsolete)
    QotMarketState_StibAfterHoursEnd = 29; //After-hours trading on the Sci-tech innovation plate ends(Obsolete)
    //New status for US index options
    QotMarketState_NIGHT = 32; //Night trading hours of U.S. index options
    QotMarketState_TRADE_AT_LAST = 35; //Late trading hours of U.S. index options
    QotMarketState_OVERNIGHT = 37;  //Overnight trading hours for U.S stock market
}
```









**QotMarketState**

Corresponding time period of each market state, [click
here](/moomoo-api-doc/en/qa/quote.html#2076) to learn more



``` protobuf
enum QotMarketState
{
    QotMarketState_None = 0; //No trading
    QotMarketState_Auction = 1; //Pre-market trading
    QotMarketState_WaitingOpen = 2; //Waiting for opening
    QotMarketState_Morning = 3; //Morning session
    QotMarketState_Rest = 4; //Lunch break
    QotMarketState_Afternoon = 5; //Afternoon session / Regular trading hours for U.S stock market
    QotMarketState_Closed = 6; //Market closed
    QotMarketState_PreMarketBegin = 8; //Pre-market trading of U.S stock market
    QotMarketState_PreMarketEnd = 9; //Pre-market ending of U.S stock market
    QotMarketState_AfterHoursBegin = 10; //After-hours trading of U.S stock market
    QotMarketState_AfterHoursEnd = 11; //Market closed of U.S. stock market
    QotMarketState_NightOpen = 13; //Night market trading hours
    QotMarketState_NightEnd = 14; //Night market closed
    QotMarketState_FutureDayOpen = 15; //Day market trading hours
    QotMarketState_FutureDayBreak = 16; //Day market break
    QotMarketState_FutureDayClose = 17; //Day market closed
    QotMarketState_FutureDayWaitForOpen = 18; //Futures market wait for opening
    QotMarketState_HkCas = 19; //After-hours bidding
    QotMarketState_FutureNightWait = 20; //Futures night market wait for opening (Obsolete)
    QotMarketState_FutureAfternoon = 21; //Futures afternoon (Obsolete)
    //New status of US futures
    QotMarketState_FutureSwitchDate = 22; //Waiting for U.S. futures opening
    QotMarketState_FutureOpen = 23; //Trading hours of U.S. futures
    QotMarketState_FutureBreak = 24; //Break of U.S. futures
    QotMarketState_FutureBreakOver = 25; //Trading hours of U.S. futures after break
    QotMarketState_FutureClose = 26; //Market closed of U.S. futures
    //New status of Sci-tech Innovation Board
    QotMarketState_StibAfterHoursWait = 27; //After-hours matching period on the Sci-tech innovation plate(Obsolete)
    QotMarketState_StibAfterHoursBegin = 28; //After-hours trading on the Sci-tech innovation plate begins(Obsolete)
    QotMarketState_StibAfterHoursEnd = 29; //After-hours trading on the Sci-tech innovation plate ends(Obsolete)
    //New status for US index options
    QotMarketState_NIGHT = 32; //Night trading hours of U.S. index options
    QotMarketState_TRADE_AT_LAST = 35; //Late trading hours of U.S. index options
    QotMarketState_OVERNIGHT = 37;  //Overnight trading hours for U.S stock market
}
```









**QotMarketState**

Corresponding time period of each market state, [click
here](/moomoo-api-doc/en/qa/quote.html#2076) to learn more



``` protobuf
enum QotMarketState
{
    QotMarketState_None = 0; //No trading
    QotMarketState_Auction = 1; //Pre-market trading
    QotMarketState_WaitingOpen = 2; //Waiting for opening
    QotMarketState_Morning = 3; //Morning session
    QotMarketState_Rest = 4; //Lunch break
    QotMarketState_Afternoon = 5; //Afternoon session / Regular trading hours for U.S stock market
    QotMarketState_Closed = 6; //Market closed
    QotMarketState_PreMarketBegin = 8; //Pre-market trading of U.S stock market
    QotMarketState_PreMarketEnd = 9; //Pre-market ending of U.S stock market
    QotMarketState_AfterHoursBegin = 10; //After-hours trading of U.S stock market
    QotMarketState_AfterHoursEnd = 11; //Market closed of U.S. stock market
    QotMarketState_NightOpen = 13; //Night market trading hours
    QotMarketState_NightEnd = 14; //Night market closed
    QotMarketState_FutureDayOpen = 15; //Day market trading hours
    QotMarketState_FutureDayBreak = 16; //Day market break
    QotMarketState_FutureDayClose = 17; //Day market closed
    QotMarketState_FutureDayWaitForOpen = 18; //Futures market wait for opening
    QotMarketState_HkCas = 19; //After-hours bidding
    QotMarketState_FutureNightWait = 20; //Futures night market wait for opening (Obsolete)
    QotMarketState_FutureAfternoon = 21; //Futures afternoon (Obsolete)
    //New status of US futures
    QotMarketState_FutureSwitchDate = 22; //Waiting for U.S. futures opening
    QotMarketState_FutureOpen = 23; //Trading hours of U.S. futures
    QotMarketState_FutureBreak = 24; //Break of U.S. futures
    QotMarketState_FutureBreakOver = 25; //Trading hours of U.S. futures after break
    QotMarketState_FutureClose = 26; //Market closed of U.S. futures
    //New status of Sci-tech Innovation Board
    QotMarketState_StibAfterHoursWait = 27; //After-hours matching period on the Sci-tech innovation plate(Obsolete)
    QotMarketState_StibAfterHoursBegin = 28; //After-hours trading on the Sci-tech innovation plate begins(Obsolete)
    QotMarketState_StibAfterHoursEnd = 29; //After-hours trading on the Sci-tech innovation plate ends(Obsolete)
    //New status for US index options
    QotMarketState_NIGHT = 32; //Night trading hours of U.S. index options
    QotMarketState_TRADE_AT_LAST = 35; //Late trading hours of U.S. index options
    QotMarketState_OVERNIGHT = 37;  //Overnight trading hours for U.S stock market
}
```









## <a href="#8688" class="header-anchor">#</a> US Stock Session





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **Session**

- `NONE`

  Unknown

- `RTH`

  US Stocks Regular trading hours

- `ETH`

  US Stocks Pre/Post + regular trading hours

- `OVERNIGHT`

  US Stocks Overnight trading hours (only applied to Trade API)

- `ALL`

  US Stocks 24H trading hours (applied to Quote API & Trade API)





> **Session**



``` protobuf
enum Session
{
    Session_NONE = 0; // Unknown
    Session_RTH = 1; // Regular Trading Hours
    Session_ETH = 2; // RTH + Pre/Post-Mkt
    Session_ALL = 3; // 24 Hour Trading
    Session_OVERNIGHT = 4; // Overnight Trading
}
```









> **Session**



``` protobuf
enum Session
{
    Session_NONE = 0; // Unknown
    Session_RTH = 1; // Regular Trading Hours
    Session_ETH = 2; // RTH + Pre/Post-Mkt
    Session_ALL = 3; // 24 Hour Trading
    Session_OVERNIGHT = 4; // Overnight Trading
}
```









> **Session**



``` protobuf
enum Session
{
    Session_NONE = 0; // Unknown
    Session_RTH = 1; // Regular Trading Hours
    Session_ETH = 2; // RTH + Pre/Post-Mkt
    Session_ALL = 3; // 24 Hour Trading
    Session_OVERNIGHT = 4; // Overnight Trading
}
```









> **Session**



``` protobuf
enum Session
{
    Session_NONE = 0; // Unknown
    Session_RTH = 1; // Regular Trading Hours
    Session_ETH = 2; // RTH + Pre/Post-Mkt
    Session_ALL = 3; // 24 Hour Trading
    Session_OVERNIGHT = 4; // Overnight Trading
}
```









> **Session**



``` protobuf
enum Session
{
    Session_NONE = 0; // Unknown
    Session_RTH = 1; // Regular Trading Hours
    Session_ETH = 2; // RTH + Pre/Post-Mkt
    Session_ALL = 3; // 24 Hour Trading
    Session_OVERNIGHT = 4; // Overnight Trading
}
```









## <a href="#3959" class="header-anchor">#</a> Quote Authorities





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **QotRight**

- `UNKNOW`

  Unknown

- `BMP`

  BMP (subscription is not supported for this permission)

- `LEVEL1`

  Level1

- `LEVEL2`

  Level2

- `SF`

  HK Securities FullTick Quotes

- `NO`

  No permission





**QotRight**



``` protobuf
enum QotRight
{
    QotRight_Unknow = 0; //Unknown
    QotRight_Bmp = 1; //BMP (subscription is not supported for this permission)
    QotRight_Level1 = 2; //Level1
    QotRight_Level2 = 3; //Level2
    QotRight_SF = 4; //SF advanced market
    QotRight_No = 5; //No permission
}
```









**QotRight**



``` protobuf
enum QotRight
{
    QotRight_Unknow = 0; //Unknown
    QotRight_Bmp = 1; //BMP (subscription is not supported for this permission)
    QotRight_Level1 = 2; //Level1
    QotRight_Level2 = 3; //Level2
    QotRight_SF = 4; //SF advanced market
    QotRight_No = 5; //No permission
}
```









**QotRight**



``` protobuf
enum QotRight
{
    QotRight_Unknow = 0; //Unknown
    QotRight_Bmp = 1; //BMP (subscription is not supported for this permission)
    QotRight_Level1 = 2; //Level1
    QotRight_Level2 = 3; //Level2
    QotRight_SF = 4; //SF advanced market
    QotRight_No = 5; //No permission
}
```









**QotRight**



``` protobuf
enum QotRight
{
    QotRight_Unknow = 0; //Unknown
    QotRight_Bmp = 1; //BMP (subscription is not supported for this permission)
    QotRight_Level1 = 2; //Level1
    QotRight_Level2 = 3; //Level2
    QotRight_SF = 4; //SF advanced market
    QotRight_No = 5; //No permission
}
```









**QotRight**



``` protobuf
enum QotRight
{
    QotRight_Unknow = 0; //Unknown
    QotRight_Bmp = 1; //BMP (subscription is not supported for this permission)
    QotRight_Level1 = 2; //Level1
    QotRight_Level2 = 3; //Level2
    QotRight_SF = 4; //SF advanced market
    QotRight_No = 5; //No permission
}
```









## <a href="#687" class="header-anchor">#</a> Associated \* **Data Type**





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SecurityReferenceType**

- `UNKNOW`

  Unknown

- `WARRANT`

  Warrants for stocks

- `FUTURE`

  Contracts related to futures main





**ReferenceType**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}
```









**ReferenceType**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}
```









**ReferenceType**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}
```









**ReferenceType**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}
```









**ReferenceType**



``` protobuf
enum ReferenceType
{
    ReferenceType_Unknow = 0; //Unknown
    ReferenceType_Warrant = 1; //Warrants for stocks
    ReferenceType_Future = 2; //Contracts related to futures main
}
```









## <a href="#7071" class="header-anchor">#</a> Candlestick Adjustment Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **AuType**

- `NONE`

  Actual

- `QFQ`

  Adjust forward

- `HFQ`

  Adjust backward





**RehabType**



``` protobuf
enum RehabType
{
    RehabType_None = 0; //Actual
    RehabType_Forward = 1; //Adjust forward
    RehabType_Backward = 2; //Adjust backward
}
```









**RehabType**



``` protobuf
enum RehabType
{
    RehabType_None = 0; //Actual
    RehabType_Forward = 1; //Adjust forward
    RehabType_Backward = 2; //Adjust backward
}
```









**RehabType**



``` protobuf
enum RehabType
{
    RehabType_None = 0; //Actual
    RehabType_Forward = 1; //Adjust forward
    RehabType_Backward = 2; //Adjust backward
}
```









**RehabType**



``` protobuf
enum RehabType
{
    RehabType_None = 0; //Actual
    RehabType_Forward = 1; //Adjust forward
    RehabType_Backward = 2; //Adjust backward
}
```









**RehabType**



``` protobuf
enum RehabType
{
    RehabType_None = 0; //Actual
    RehabType_Forward = 1; //Adjust forward
    RehabType_Backward = 2; //Adjust backward
}
```









## <a href="#4415" class="header-anchor">#</a> Stock Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SecurityStatus**

- `NONE`

  Unknown

- `NORMAL`

  Normal status

- `LISTING`

  To be listed

- `PURCHASING`

  Purchasing

- `SUBSCRIBING`

  Subscribing

- `BEFORE_DRAK_TRADE_OPENING`

  Before the grey market trading opens

- `DRAK_TRADING`

  Ongoing grey market trading

- `DRAK_TRADE_END`

  Grey market trading closed

- `TO_BE_OPEN`

  To be open

- `SUSPENDED`

  Suspended

- `CALLED`

  Called

- `EXPIRED_LAST_TRADING_DATE`

  Expired latest trading date

- `EXPIRED`

  Expired

- `DELISTED`

  Delisted

- `CHANGE_TO_TEMPORARY_CODE`

  During the company action, the trading was closed and transferred to
  the temporary code trading

- `TEMPORARY_CODE_TRADE_END`

  Temporary trading ends

- `CHANGED_PLATE_TRADE_END`

  Plate changed, the old code is not available for trading

- `CHANGED_CODE_TRADE_END`

  The code has been changed, the old code is not available for trading

- `RECOVERABLE_CIRCUIT_BREAKER`

  Recoverable circuit breaker

- `UN_RECOVERABLE_CIRCUIT_BREAKER`

  Unrecoverable circuit breaker

- `AFTER_COMBINATION`

  After-hours matchmaking

- `AFTER_TRANSATION`

  After-hours trading





**SecurityStatus**



``` protobuf
enum SecurityStatus
{
    SecurityStatus_Unknown = 0; //Unknown
    SecurityStatus_Normal = 1; //Normal status
    SecurityStatus_Listing = 2; //To be listed
    SecurityStatus_Purchasing = 3; //Purchasing
    SecurityStatus_Subscribing = 4; //Subscribing
    SecurityStatus_BeforeDrakTradeOpening = 5; //Before the grey market trading opens
    SecurityStatus_DrakTrading = 6; //Ongoing grey market trading
    SecurityStatus_DrakTradeEnd = 7; //Grey market trading closed
    SecurityStatus_ToBeOpen = 8; //To be open
    SecurityStatus_Suspended = 9; //Suspended
    SecurityStatus_Called = 10; //Called
    SecurityStatus_ExpiredLastTradingDate = 11; //Expired latest trading date
    SecurityStatus_Expired = 12; //Expired
    SecurityStatus_Delisted = 13; //Delisted
    SecurityStatus_ChangeToTemporaryCode = 14; //During the company action, the trading was closed and transferred to the temporary code trading
    SecurityStatus_TemporaryCodeTradeEnd = 15; //Temporary trading ends
    SecurityStatus_ChangedPlateTradeEnd = 16; //Plate changed, the old trading code is not available
    SecurityStatus_ChangedCodeTradeEnd = 17; //The code has been changed, the old code is not available
    SecurityStatus_RecoverableCircuitBreaker = 18; //Recoverable circuit breaker
    SecurityStatus_UnRecoverableCircuitBreaker = 19; //Unrecoverable circuit breaker
    SecurityStatus_AfterCombination = 20; //After-hours matchmaking
    SecurityStatus_AfterTransation = 21; //After-hours trading
}
```









**SecurityStatus**



``` protobuf
enum SecurityStatus
{
    SecurityStatus_Unknown = 0; //Unknown
    SecurityStatus_Normal = 1; //Normal status
    SecurityStatus_Listing = 2; //To be listed
    SecurityStatus_Purchasing = 3; //Purchasing
    SecurityStatus_Subscribing = 4; //Subscribing
    SecurityStatus_BeforeDrakTradeOpening = 5; //Before the grey market trading opens
    SecurityStatus_DrakTrading = 6; //Ongoing grey market trading
    SecurityStatus_DrakTradeEnd = 7; //Grey market trading closed
    SecurityStatus_ToBeOpen = 8; //To be open
    SecurityStatus_Suspended = 9; //Suspended
    SecurityStatus_Called = 10; //Called
    SecurityStatus_ExpiredLastTradingDate = 11; //Expired latest trading date
    SecurityStatus_Expired = 12; //Expired
    SecurityStatus_Delisted = 13; //Delisted
    SecurityStatus_ChangeToTemporaryCode = 14; //During the company action, the trading was closed and transferred to the temporary code trading
    SecurityStatus_TemporaryCodeTradeEnd = 15; //Temporary trading ends
    SecurityStatus_ChangedPlateTradeEnd = 16; //Plate changed, the old trading code is not available
    SecurityStatus_ChangedCodeTradeEnd = 17; //The code has been changed, the old code is not available
    SecurityStatus_RecoverableCircuitBreaker = 18; //Recoverable circuit breaker
    SecurityStatus_UnRecoverableCircuitBreaker = 19; //Unrecoverable circuit breaker
    SecurityStatus_AfterCombination = 20; //After-hours matchmaking
    SecurityStatus_AfterTransation = 21; //After-hours trading
}
```









**SecurityStatus**



``` protobuf
enum SecurityStatus
{
    SecurityStatus_Unknown = 0; //Unknown
    SecurityStatus_Normal = 1; //Normal status
    SecurityStatus_Listing = 2; //To be listed
    SecurityStatus_Purchasing = 3; //Purchasing
    SecurityStatus_Subscribing = 4; //Subscribing
    SecurityStatus_BeforeDrakTradeOpening = 5; //Before the grey market trading opens
    SecurityStatus_DrakTrading = 6; //Ongoing grey market trading
    SecurityStatus_DrakTradeEnd = 7; //Grey market trading closed
    SecurityStatus_ToBeOpen = 8; //To be open
    SecurityStatus_Suspended = 9; //Suspended
    SecurityStatus_Called = 10; //Called
    SecurityStatus_ExpiredLastTradingDate = 11; //Expired latest trading date
    SecurityStatus_Expired = 12; //Expired
    SecurityStatus_Delisted = 13; //Delisted
    SecurityStatus_ChangeToTemporaryCode = 14; //During the company action, the trading was closed and transferred to the temporary code trading
    SecurityStatus_TemporaryCodeTradeEnd = 15; //Temporary trading ends
    SecurityStatus_ChangedPlateTradeEnd = 16; //Plate changed, the old trading code is not available
    SecurityStatus_ChangedCodeTradeEnd = 17; //The code has been changed, the old code is not available
    SecurityStatus_RecoverableCircuitBreaker = 18; //Recoverable circuit breaker
    SecurityStatus_UnRecoverableCircuitBreaker = 19; //Unrecoverable circuit breaker
    SecurityStatus_AfterCombination = 20; //After-hours matchmaking
    SecurityStatus_AfterTransation = 21; //After-hours trading
}
```









**SecurityStatus**



``` protobuf
enum SecurityStatus
{
    SecurityStatus_Unknown = 0; //Unknown
    SecurityStatus_Normal = 1; //Normal status
    SecurityStatus_Listing = 2; //To be listed
    SecurityStatus_Purchasing = 3; //Purchasing
    SecurityStatus_Subscribing = 4; //Subscribing
    SecurityStatus_BeforeDrakTradeOpening = 5; //Before the grey market trading opens
    SecurityStatus_DrakTrading = 6; //Ongoing grey market trading
    SecurityStatus_DrakTradeEnd = 7; //Grey market trading closed
    SecurityStatus_ToBeOpen = 8; //To be open
    SecurityStatus_Suspended = 9; //Suspended
    SecurityStatus_Called = 10; //Called
    SecurityStatus_ExpiredLastTradingDate = 11; //Expired latest trading date
    SecurityStatus_Expired = 12; //Expired
    SecurityStatus_Delisted = 13; //Delisted
    SecurityStatus_ChangeToTemporaryCode = 14; //During the company action, the trading was closed and transferred to the temporary code trading
    SecurityStatus_TemporaryCodeTradeEnd = 15; //Temporary trading ends
    SecurityStatus_ChangedPlateTradeEnd = 16; //Plate changed, the old trading code is not available
    SecurityStatus_ChangedCodeTradeEnd = 17; //The code has been changed, the old code is not available
    SecurityStatus_RecoverableCircuitBreaker = 18; //Recoverable circuit breaker
    SecurityStatus_UnRecoverableCircuitBreaker = 19; //Unrecoverable circuit breaker
    SecurityStatus_AfterCombination = 20; //After-hours matchmaking
    SecurityStatus_AfterTransation = 21; //After-hours trading
}
```









**SecurityStatus**



``` protobuf
enum SecurityStatus
{
    SecurityStatus_Unknown = 0; //Unknown
    SecurityStatus_Normal = 1; //Normal status
    SecurityStatus_Listing = 2; //To be listed
    SecurityStatus_Purchasing = 3; //Purchasing
    SecurityStatus_Subscribing = 4; //Subscribing
    SecurityStatus_BeforeDrakTradeOpening = 5; //Before the grey market trading opens
    SecurityStatus_DrakTrading = 6; //Ongoing grey market trading
    SecurityStatus_DrakTradeEnd = 7; //Grey market trading closed
    SecurityStatus_ToBeOpen = 8; //To be open
    SecurityStatus_Suspended = 9; //Suspended
    SecurityStatus_Called = 10; //Called
    SecurityStatus_ExpiredLastTradingDate = 11; //Expired latest trading date
    SecurityStatus_Expired = 12; //Expired
    SecurityStatus_Delisted = 13; //Delisted
    SecurityStatus_ChangeToTemporaryCode = 14; //During the company action, the trading was closed and transferred to the temporary code trading
    SecurityStatus_TemporaryCodeTradeEnd = 15; //Temporary trading ends
    SecurityStatus_ChangedPlateTradeEnd = 16; //Plate changed, the old trading code is not available
    SecurityStatus_ChangedCodeTradeEnd = 17; //The code has been changed, the old code is not available
    SecurityStatus_RecoverableCircuitBreaker = 18; //Recoverable circuit breaker
    SecurityStatus_UnRecoverableCircuitBreaker = 19; //Unrecoverable circuit breaker
    SecurityStatus_AfterCombination = 20; //After-hours matchmaking
    SecurityStatus_AfterTransation = 21; //After-hours trading
}
```









## <a href="#9767" class="header-anchor">#</a> Stock Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SecurityType**

- `NONE`

  Unknown

- `BOND`

  Bonds

- `BWRT`

  Blanket warrants

- `STOCK`

  Stocks

- `ETF`

  ETFs

- `WARRANT`

  Warrants

- `IDX`

  Indexs

- `PLATE`

  Plates

- `DRVT`

  Options

- `PLATESET`

  Plate sets

- `FUTURE`

  Futures





**SecurityType**



``` protobuf
enum SecurityType
{
    SecurityType_Unknown = 0; //Unknown
    SecurityType_Bond = 1; //Bonds
    SecurityType_Bwrt = 2; //Blanket warrants
    SecurityType_Eqty = 3; //Stocks
    SecurityType_Trust = 4; //ETFs
    SecurityType_Warrant = 5; //Warrants
    SecurityType_Index = 6; //Indexs
    SecurityType_Plate = 7; //Plates
    SecurityType_Drvt = 8; //Options
    SecurityType_PlateSet = 9; //Plate Sets
    SecurityType_Future = 10; //Futures
}
```









**SecurityType**



``` protobuf
enum SecurityType
{
    SecurityType_Unknown = 0; //Unknown
    SecurityType_Bond = 1; //Bonds
    SecurityType_Bwrt = 2; //Blanket warrants
    SecurityType_Eqty = 3; //Stocks
    SecurityType_Trust = 4; //ETFs
    SecurityType_Warrant = 5; //Warrants
    SecurityType_Index = 6; //Indexs
    SecurityType_Plate = 7; //Plates
    SecurityType_Drvt = 8; //Options
    SecurityType_PlateSet = 9; //Plate Sets
    SecurityType_Future = 10; //Futures
}
```









**SecurityType**



``` protobuf
enum SecurityType
{
    SecurityType_Unknown = 0; //Unknown
    SecurityType_Bond = 1; //Bonds
    SecurityType_Bwrt = 2; //Blanket warrants
    SecurityType_Eqty = 3; //Stocks
    SecurityType_Trust = 4; //ETFs
    SecurityType_Warrant = 5; //Warrants
    SecurityType_Index = 6; //Indexs
    SecurityType_Plate = 7; //Plates
    SecurityType_Drvt = 8; //Options
    SecurityType_PlateSet = 9; //Plate Sets
    SecurityType_Future = 10; //Futures
}
```









**SecurityType**



``` protobuf
enum SecurityType
{
    SecurityType_Unknown = 0; //Unknown
    SecurityType_Bond = 1; //Bonds
    SecurityType_Bwrt = 2; //Blanket warrants
    SecurityType_Eqty = 3; //Stocks
    SecurityType_Trust = 4; //ETFs
    SecurityType_Warrant = 5; //Warrants
    SecurityType_Index = 6; //Indexs
    SecurityType_Plate = 7; //Plates
    SecurityType_Drvt = 8; //Options
    SecurityType_PlateSet = 9; //Plate Sets
    SecurityType_Future = 10; //Futures
}
```









**SecurityType**



``` protobuf
enum SecurityType
{
    SecurityType_Unknown = 0; //Unknown
    SecurityType_Bond = 1; //Bonds
    SecurityType_Bwrt = 2; //Blanket warrants
    SecurityType_Eqty = 3; //Stocks
    SecurityType_Trust = 4; //ETFs
    SecurityType_Warrant = 5; //Warrants
    SecurityType_Index = 6; //Indexs
    SecurityType_Plate = 7; //Plates
    SecurityType_Drvt = 8; //Options
    SecurityType_PlateSet = 9; //Plate Sets
    SecurityType_Future = 10; //Futures
}
```









## <a href="#8810" class="header-anchor">#</a> Set Price Reminder Operation Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SetPriceReminderOp**

- `NONE`

  Unknown

- `ADD`

  Add

- `DEL`

  Delete

- `ENABLE`

  Enable

- `DISABLE`

  Disable

- `MODIFY`

  Modify

- `DEL_ALL`

  Delete all (delete all price alerts under the specified stock)





**SetPriceReminderOp**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all (delete all price reminders under the specified stock)
}
```









**SetPriceReminderOp**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all (delete all price reminders under the specified stock)
}
```









**SetPriceReminderOp**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all (delete all price reminders under the specified stock)
}
```









**SetPriceReminderOp**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all (delete all price reminders under the specified stock)
}
```









**SetPriceReminderOp**



``` protobuf
enum SetPriceReminderOp
{
    SetPriceReminderOp_Unknown = 0;
    SetPriceReminderOp_Add = 1; //Add
    SetPriceReminderOp_Del = 2; //Delete
    SetPriceReminderOp_Enable = 3; //Enable
    SetPriceReminderOp_Disable = 4; //Disable
    SetPriceReminderOp_Modify = 5; //Modify
    SetPriceReminderOp_DelAll = 6; //Delete all (delete all price reminders under the specified stock)
}
```









## <a href="#9029" class="header-anchor">#</a> Sort Direction





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SortDir**

- `NONE`

  Not sorted

- `ASCEND`

  Ascending

- `DESCEND`

  Descending





**SortDir**



``` protobuf
enum SortDir
{
    SortDir_No = 0; //Do not sort
    SortDir_Ascend = 1; //Ascending order
    SortDir_Descend = 2; //Descending order
}
```









**SortDir**



``` protobuf
enum SortDir
{
    SortDir_No = 0; //Do not sort
    SortDir_Ascend = 1; //Ascending order
    SortDir_Descend = 2; //Descending order
}
```









**SortDir**



``` protobuf
enum SortDir
{
    SortDir_No = 0; //Do not sort
    SortDir_Ascend = 1; //Ascending order
    SortDir_Descend = 2; //Descending order
}
```









**SortDir**



``` protobuf
enum SortDir
{
    SortDir_No = 0; //Do not sort
    SortDir_Ascend = 1; //Ascending order
    SortDir_Descend = 2; //Descending order
}
```









**SortDir**



``` protobuf
enum SortDir
{
    SortDir_No = 0; //Do not sort
    SortDir_Ascend = 1; //Ascending order
    SortDir_Descend = 2; //Descending order
}
```









## <a href="#5823" class="header-anchor">#</a> Sort Field





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SortField**

- `NONE`

  Unknown

- `CODE`

  Code

- `CUR_PRICE`

  Latest price

- `PRICE_CHANGE_VAL`

  Price changed

- `CHANGE_RATE`

  Yield

- `STATUS`

  Status

- `BID_PRICE`

  Bid price

- `ASK_PRICE`

  Ask price

- `BID_VOL`

  Bid volume

- `ASK_VOL`

  Ask volume

- `VOLUME`

  Volume

- `TURNOVER`

  Turnover

- `AMPLITUDE`

  Amplitude

- `SCORE`

  Comprehensive score

- `PREMIUM`

  Premium

- `EFFECTIVE_LEVERAGE`

  Effective leverage

- `DELTA`

  Hedging value

  

  
  

  

  
  
  

  For puts and calls only

  

  

  

  

- `IMPLIED_VOLATILITY`

  Implied volatility

  

  
  

  

  
  
  

  For puts and calls only

  

  

  

  

- `TYPE`

  Type

- `STRIKE_PRICE`

  Strike price

- `BREAK_EVEN_POINT`

  Break even point

- `MATURITY_TIME`

  Maturity date

- `LIST_TIME`

  Listing date

- `LAST_TRADE_TIME`

  Lastest trading day

- `LEVERAGE`

  Leverage ratio

- `IN_OUT_MONEY`

  In/out of the money %

- `RECOVERY_PRICE`

  Recovery price

  

  
  

  

  
  
  

  For CBBCs only

  

  

  

  

- `CHANGE_PRICE`

  Change price

- `CHANGE`

  Change ratio

- `STREET_RATE`

  Outstanding percentage (the propotioin of retail investors)

- `STREET_VOL`

  Outstanding quantity (the volume held by retail investors)

- `WARRANT_NAME`

  Warrant name

- `ISSUER`

  Issuer

- `LOT_SIZE`

  Lot size

- `ISSUE_SIZE`

  Issue size

- `UPPER_STRIKE_PRICE`

  Upper bound

  

  
  

  

  
  
  

  Only for Inline Warrants

  

  

  

  

- `LOWER_STRIKE_PRICE`

  Lower bound

  

  
  

  

  
  
  

  Only for Inline Warrants

  

  

  

  

- `INLINE_PRICE_STATUS`

  In/out of bounds

  

  
  

  

  
  
  

  Only for Inline Warrants

  

  

  

  

- `PRE_CUR_PRICE`

  Latest price of pre-market

- `AFTER_CUR_PRICE`

  Latest price of after-hours

- `PRE_PRICE_CHANGE_VAL`

  Pre-market changes

- `AFTER_PRICE_CHANGE_VAL`

  After-hours changes

- `PRE_CHANGE_RATE`

  Pre-market change rate %

- `AFTER_CHANGE_RATE`

  After-hours change rate %

- `PRE_AMPLITUDE`

  Pre-market amplitude %

- `AFTER_AMPLITUDE`

  After-hours amplitude %

- `PRE_TURNOVER`

  Pre-market turnover

- `AFTER_TURNOVER`

  After-hours turnover

- `LAST_SETTLE_PRICE`

  Last settle price

- `POSITION`

  Position

- `POSITION_CHANGE`

  Daily increase of position





**SortField**



``` protobuf
enum SortField
{
    SortField_Unknow = 0; //Unknown
    SortField_Code = 1; //Code
    SortField_CurPrice = 2; //Latest price
    SortField_PriceChangeVal = 3; //Price changed
    SortField_ChangeRate = 4; //Yield
    SortField_Status = 5; //Status
    SortField_BidPrice = 6; //Bid price
    SortField_AskPrice = 7; //Ask price
    SortField_BidVol = 8; //Bid volume
    SortField_AskVol = 9; //Ask volume
    SortField_Volume = 10; //Volume
    SortField_Turnover = 11; //Turnover
    SortField_Amplitude = 30; //Amplitude

    //The following sort fields are only supported for Qot_GetWarrant protocol
    SortField_Score = 12; //Comprehensive score
    SortField_Premium = 13; //Premium
    SortField_EffectiveLeverage = 14; //Effective leverage
    SortField_Delta = 15; //Hedging value, for puts and calls only
    SortField_ImpliedVolatility = 16; //Implied volatility, for puts and calls only
    SortField_Type = 17; //Type
    SortField_StrikePrice = 18; //Strike price
    SortField_BreakEvenPoint = 19; //Break even point
    SortField_MaturityTime = 20; //Maturity date
    SortField_ListTime = 21; //Listing date
    SortField_LastTradeTime = 22; //Lastest trading day
    SortField_Leverage = 23; //Leverage ratio
    SortField_InOutMoney = 24; //In/out of the money %
    SortField_RecoveryPrice = 25; //Recovery price, for CBBCs only
    SortField_ChangePrice = 26; //Change price
    SortField_Change = 27; //Change ratio
    SortField_StreetRate = 28; //Outstanding percentage (the propotioin of retail investors)
    SortField_StreetVol = 29; //Outstanding quantity (the volume held by retail investors)
    SortField_WarrantName = 31; //Warrant name
    SortField_Issuer = 32; //Issuer
    SortField_LotSize = 33; //Lot size
    SortField_IssueSize = 34; //Issue size
    SortField_UpperStrikePrice = 45; //Upper bound, only for Inline Warrants
    SortField_LowerStrikePrice = 46; //Lower bound, only for Inline Warrants
    SortField_InLinePriceStatus = 47; //In/out of bounds, only for Inline Warrants

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only support US stocks
    SortField_PreCurPrice = 35; //Latest price of pre-market
    SortField_AfterCurPrice = 36; //Latest price of after-hours
    SortField_PrePriceChangeVal = 37; //Pre-market changes
    SortField_AfterPriceChangeVal = 38; //After-hours changes
    SortField_PreChangeRate = 39; //Pre-market change rate %
    SortField_AfterChangeRate = 40; //After-hours change rate %
    SortField_PreAmplitude = 41; //Pre-market amplitude %
    SortField_AfterAmplitude = 42; //After-hours amplitude %
    SortField_PreTurnover = 43; //Pre-market turnover
    SortField_AfterTurnover = 44; //After-hours turnover

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only futures
    SortField_LastSettlePrice = 48; //Last settle price 
    SortField_Position = 49; //Position
    SortField_PositionChange = 50; //Daily increase of position
}
```









**SortField**



``` protobuf
enum SortField
{
    SortField_Unknow = 0; //Unknown
    SortField_Code = 1; //Code
    SortField_CurPrice = 2; //Latest price
    SortField_PriceChangeVal = 3; //Price changed
    SortField_ChangeRate = 4; //Yield
    SortField_Status = 5; //Status
    SortField_BidPrice = 6; //Bid price
    SortField_AskPrice = 7; //Ask price
    SortField_BidVol = 8; //Bid volume
    SortField_AskVol = 9; //Ask volume
    SortField_Volume = 10; //Volume
    SortField_Turnover = 11; //Turnover
    SortField_Amplitude = 30; //Amplitude

    //The following sort fields are only supported for Qot_GetWarrant protocol
    SortField_Score = 12; //Comprehensive score
    SortField_Premium = 13; //Premium
    SortField_EffectiveLeverage = 14; //Effective leverage
    SortField_Delta = 15; //Hedging value, for puts and calls only
    SortField_ImpliedVolatility = 16; //Implied volatility, for puts and calls only
    SortField_Type = 17; //Type
    SortField_StrikePrice = 18; //Strike price
    SortField_BreakEvenPoint = 19; //Break even point
    SortField_MaturityTime = 20; //Maturity date
    SortField_ListTime = 21; //Listing date
    SortField_LastTradeTime = 22; //Lastest trading day
    SortField_Leverage = 23; //Leverage ratio
    SortField_InOutMoney = 24; //In/out of the money %
    SortField_RecoveryPrice = 25; //Recovery price, for CBBCs only
    SortField_ChangePrice = 26; //Change price
    SortField_Change = 27; //Change ratio
    SortField_StreetRate = 28; //Outstanding percentage (the propotioin of retail investors)
    SortField_StreetVol = 29; //Outstanding quantity (the volume held by retail investors)
    SortField_WarrantName = 31; //Warrant name
    SortField_Issuer = 32; //Issuer
    SortField_LotSize = 33; //Lot size
    SortField_IssueSize = 34; //Issue size
    SortField_UpperStrikePrice = 45; //Upper bound, only for Inline Warrants
    SortField_LowerStrikePrice = 46; //Lower bound, only for Inline Warrants
    SortField_InLinePriceStatus = 47; //In/out of bounds, only for Inline Warrants

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only support US stocks
    SortField_PreCurPrice = 35; //Latest price of pre-market
    SortField_AfterCurPrice = 36; //Latest price of after-hours
    SortField_PrePriceChangeVal = 37; //Pre-market changes
    SortField_AfterPriceChangeVal = 38; //After-hours changes
    SortField_PreChangeRate = 39; //Pre-market change rate %
    SortField_AfterChangeRate = 40; //After-hours change rate %
    SortField_PreAmplitude = 41; //Pre-market amplitude %
    SortField_AfterAmplitude = 42; //After-hours amplitude %
    SortField_PreTurnover = 43; //Pre-market turnover
    SortField_AfterTurnover = 44; //After-hours turnover

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only futures
    SortField_LastSettlePrice = 48; //Last settle price 
    SortField_Position = 49; //Position
    SortField_PositionChange = 50; //Daily increase of position
}
```









**SortField**



``` protobuf
enum SortField
{
    SortField_Unknow = 0; //Unknown
    SortField_Code = 1; //Code
    SortField_CurPrice = 2; //Latest price
    SortField_PriceChangeVal = 3; //Price changed
    SortField_ChangeRate = 4; //Yield
    SortField_Status = 5; //Status
    SortField_BidPrice = 6; //Bid price
    SortField_AskPrice = 7; //Ask price
    SortField_BidVol = 8; //Bid volume
    SortField_AskVol = 9; //Ask volume
    SortField_Volume = 10; //Volume
    SortField_Turnover = 11; //Turnover
    SortField_Amplitude = 30; //Amplitude

    //The following sort fields are only supported for Qot_GetWarrant protocol
    SortField_Score = 12; //Comprehensive score
    SortField_Premium = 13; //Premium
    SortField_EffectiveLeverage = 14; //Effective leverage
    SortField_Delta = 15; //Hedging value, for puts and calls only
    SortField_ImpliedVolatility = 16; //Implied volatility, for puts and calls only
    SortField_Type = 17; //Type
    SortField_StrikePrice = 18; //Strike price
    SortField_BreakEvenPoint = 19; //Break even point
    SortField_MaturityTime = 20; //Maturity date
    SortField_ListTime = 21; //Listing date
    SortField_LastTradeTime = 22; //Lastest trading day
    SortField_Leverage = 23; //Leverage ratio
    SortField_InOutMoney = 24; //In/out of the money %
    SortField_RecoveryPrice = 25; //Recovery price, for CBBCs only
    SortField_ChangePrice = 26; //Change price
    SortField_Change = 27; //Change ratio
    SortField_StreetRate = 28; //Outstanding percentage (the propotioin of retail investors)
    SortField_StreetVol = 29; //Outstanding quantity (the volume held by retail investors)
    SortField_WarrantName = 31; //Warrant name
    SortField_Issuer = 32; //Issuer
    SortField_LotSize = 33; //Lot size
    SortField_IssueSize = 34; //Issue size
    SortField_UpperStrikePrice = 45; //Upper bound, only for Inline Warrants
    SortField_LowerStrikePrice = 46; //Lower bound, only for Inline Warrants
    SortField_InLinePriceStatus = 47; //In/out of bounds, only for Inline Warrants

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only support US stocks
    SortField_PreCurPrice = 35; //Latest price of pre-market
    SortField_AfterCurPrice = 36; //Latest price of after-hours
    SortField_PrePriceChangeVal = 37; //Pre-market changes
    SortField_AfterPriceChangeVal = 38; //After-hours changes
    SortField_PreChangeRate = 39; //Pre-market change rate %
    SortField_AfterChangeRate = 40; //After-hours change rate %
    SortField_PreAmplitude = 41; //Pre-market amplitude %
    SortField_AfterAmplitude = 42; //After-hours amplitude %
    SortField_PreTurnover = 43; //Pre-market turnover
    SortField_AfterTurnover = 44; //After-hours turnover

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only futures
    SortField_LastSettlePrice = 48; //Last settle price 
    SortField_Position = 49; //Position
    SortField_PositionChange = 50; //Daily increase of position
}
```









**SortField**



``` protobuf
enum SortField
{
    SortField_Unknow = 0; //Unknown
    SortField_Code = 1; //Code
    SortField_CurPrice = 2; //Latest price
    SortField_PriceChangeVal = 3; //Price changed
    SortField_ChangeRate = 4; //Yield
    SortField_Status = 5; //Status
    SortField_BidPrice = 6; //Bid price
    SortField_AskPrice = 7; //Ask price
    SortField_BidVol = 8; //Bid volume
    SortField_AskVol = 9; //Ask volume
    SortField_Volume = 10; //Volume
    SortField_Turnover = 11; //Turnover
    SortField_Amplitude = 30; //Amplitude

    //The following sort fields are only supported for Qot_GetWarrant protocol
    SortField_Score = 12; //Comprehensive score
    SortField_Premium = 13; //Premium
    SortField_EffectiveLeverage = 14; //Effective leverage
    SortField_Delta = 15; //Hedging value, for puts and calls only
    SortField_ImpliedVolatility = 16; //Implied volatility, for puts and calls only
    SortField_Type = 17; //Type
    SortField_StrikePrice = 18; //Strike price
    SortField_BreakEvenPoint = 19; //Break even point
    SortField_MaturityTime = 20; //Maturity date
    SortField_ListTime = 21; //Listing date
    SortField_LastTradeTime = 22; //Lastest trading day
    SortField_Leverage = 23; //Leverage ratio
    SortField_InOutMoney = 24; //In/out of the money %
    SortField_RecoveryPrice = 25; //Recovery price, for CBBCs only
    SortField_ChangePrice = 26; //Change price
    SortField_Change = 27; //Change ratio
    SortField_StreetRate = 28; //Outstanding percentage (the propotioin of retail investors)
    SortField_StreetVol = 29; //Outstanding quantity (the volume held by retail investors)
    SortField_WarrantName = 31; //Warrant name
    SortField_Issuer = 32; //Issuer
    SortField_LotSize = 33; //Lot size
    SortField_IssueSize = 34; //Issue size
    SortField_UpperStrikePrice = 45; //Upper bound, only for Inline Warrants
    SortField_LowerStrikePrice = 46; //Lower bound, only for Inline Warrants
    SortField_InLinePriceStatus = 47; //In/out of bounds, only for Inline Warrants

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only support US stocks
    SortField_PreCurPrice = 35; //Latest price of pre-market
    SortField_AfterCurPrice = 36; //Latest price of after-hours
    SortField_PrePriceChangeVal = 37; //Pre-market changes
    SortField_AfterPriceChangeVal = 38; //After-hours changes
    SortField_PreChangeRate = 39; //Pre-market change rate %
    SortField_AfterChangeRate = 40; //After-hours change rate %
    SortField_PreAmplitude = 41; //Pre-market amplitude %
    SortField_AfterAmplitude = 42; //After-hours amplitude %
    SortField_PreTurnover = 43; //Pre-market turnover
    SortField_AfterTurnover = 44; //After-hours turnover

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only futures
    SortField_LastSettlePrice = 48; //Last settle price 
    SortField_Position = 49; //Position
    SortField_PositionChange = 50; //Daily increase of position
}
```









**SortField**



``` protobuf
enum SortField
{
    SortField_Unknow = 0; //Unknown
    SortField_Code = 1; //Code
    SortField_CurPrice = 2; //Latest price
    SortField_PriceChangeVal = 3; //Price changed
    SortField_ChangeRate = 4; //Yield
    SortField_Status = 5; //Status
    SortField_BidPrice = 6; //Bid price
    SortField_AskPrice = 7; //Ask price
    SortField_BidVol = 8; //Bid volume
    SortField_AskVol = 9; //Ask volume
    SortField_Volume = 10; //Volume
    SortField_Turnover = 11; //Turnover
    SortField_Amplitude = 30; //Amplitude

    //The following sort fields are only supported for Qot_GetWarrant protocol
    SortField_Score = 12; //Comprehensive score
    SortField_Premium = 13; //Premium
    SortField_EffectiveLeverage = 14; //Effective leverage
    SortField_Delta = 15; //Hedging value, for puts and calls only
    SortField_ImpliedVolatility = 16; //Implied volatility, for puts and calls only
    SortField_Type = 17; //Type
    SortField_StrikePrice = 18; //Strike price
    SortField_BreakEvenPoint = 19; //Break even point
    SortField_MaturityTime = 20; //Maturity date
    SortField_ListTime = 21; //Listing date
    SortField_LastTradeTime = 22; //Lastest trading day
    SortField_Leverage = 23; //Leverage ratio
    SortField_InOutMoney = 24; //In/out of the money %
    SortField_RecoveryPrice = 25; //Recovery price, for CBBCs only
    SortField_ChangePrice = 26; //Change price
    SortField_Change = 27; //Change ratio
    SortField_StreetRate = 28; //Outstanding percentage (the propotioin of retail investors)
    SortField_StreetVol = 29; //Outstanding quantity (the volume held by retail investors)
    SortField_WarrantName = 31; //Warrant name
    SortField_Issuer = 32; //Issuer
    SortField_LotSize = 33; //Lot size
    SortField_IssueSize = 34; //Issue size
    SortField_UpperStrikePrice = 45; //Upper bound, only for Inline Warrants
    SortField_LowerStrikePrice = 46; //Lower bound, only for Inline Warrants
    SortField_InLinePriceStatus = 47; //In/out of bounds, only for Inline Warrants

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only support US stocks
    SortField_PreCurPrice = 35; //Latest price of pre-market
    SortField_AfterCurPrice = 36; //Latest price of after-hours
    SortField_PrePriceChangeVal = 37; //Pre-market changes
    SortField_AfterPriceChangeVal = 38; //After-hours changes
    SortField_PreChangeRate = 39; //Pre-market change rate %
    SortField_AfterChangeRate = 40; //After-hours change rate %
    SortField_PreAmplitude = 41; //Pre-market amplitude %
    SortField_AfterAmplitude = 42; //After-hours amplitude %
    SortField_PreTurnover = 43; //Pre-market turnover
    SortField_AfterTurnover = 44; //After-hours turnover

    //The following sort fields are only supported for the Qot_GetPlateSecurity protocol, and only futures
    SortField_LastSettlePrice = 48; //Last settle price 
    SortField_Position = 49; //Position
    SortField_PositionChange = 50; //Daily increase of position
}
```









## <a href="#9377" class="header-anchor">#</a> Simple Filter Properties





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **StockField**

- `NONE`

  unknown

- `STOCK_CODE`

  Stock code, does not accept list inputs as an interval

- `STOCK_NAME`

  Stock name, does not accept list inputs as an interval

- `CUR_PRICE`

  The latest price

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[10, 20\]

  

  

  

  

- `CUR_PRICE_TO_HIGHEST52_WEEKS_RATIO`

  **(CP - WH52) / WH52**  
  **CP**: Current price  
  **WH52**: 52-week high  
  Corresponding to the “percentage from 52-week high” on the PC terminal

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-30, -10\]

  

  

  

  

- `CUR_PRICE_TO_LOWEST52_WEEKS_RATIO`

  **(CP - WL52) / WL52**  
  **CP**: Current price  
  **WL52**: 52-week low  
  Corresponding to the “percentage from 52-week low” on the PC terminal

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[20, 40\]

  

  

  

  

- `HIGH_PRICE_TO_HIGHEST52_WEEKS_RATIO`

  **(TH - WH52) / WH52**  
  **TH**: Today's high  
  **WH52**: 52-week high  

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-3, -1\]

  

  

  

  

- `LOW_PRICE_TO_LOWEST52_WEEKS_RATIO`

  **(TL - WL52) / WL52**  
  **TL**: Today's low  
  **WL52**: 52-week low  

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[10, 70\]

  

  

  

  

- `VOLUME_RATIO`

  Volume ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[0.5, 30\]

  

  

  

  

- `BID_ASK_RATIO`

  Bid-ask ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-20, 80.5\]

  

  

  

  

- `LOT_PRICE`

  Price per lot

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[40, 100\]

  

  

  

  

- `MARKET_VAL`

  Market value

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[50000000, 3000000000\]

  

  

  

  

- `PE_ANNUAL`

  Trailing P/E

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[-8, 65.3\]

  

  

  

  

- `PE_TTM`

  P/E TTM

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[-10, 20.5\]

  

  

  

  

- `PB_RATE`

  P/B ratio

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[0.5, 20\]

  

  

  

  

- `CHANGE_RATE_5MIN`

  Change rate in 5 minutes

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-5, 6.3\]

  

  

  

  

- `CHANGE_RATE_BEGIN_YEAR`

  Price change rate from this year

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[-50.1, 400.7\]

  

  

  

  

- `PS_TTM`

  P/S TTM

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[100, 500\]

  

  

  

  

- `PCF_TTM`

  PCF TTM

  

  
  

  

  
  
  

  - 3 decimal place accuracy, the excess part is discarded.
  - This field is in percentage form, so 20 is equivalent to 20%.
  - For example, a range of \[100, 1000\]

  

  

  

  

- `TOTAL_SHARE`

  Total number of shares

  

  
  

  

  
  
  

  - unit: share.
  - 0 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `FLOAT_SHARE`

  Shares outstanding

  

  
  

  

  
  
  

  - unit: share.
  - 0 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  

- `FLOAT_MARKET_VAL`

  Market value outstanding

  

  
  

  

  
  
  

  - unit: yuan.
  - 3 decimal place accuracy, the excess part is discarded.
  - For example, a range of \[1000000000, 1000000000\]

  

  

  

  





**StockField**



``` protobuf
enum StockField
{
    StockField_Unknown = 0; //Unknown
    StockField_StockCode = 1; //Stock code, does not accept list inputs as an interval
    StockField_StockName = 2; //Stock name, does not accept list inputs as an interval
    StockField_CurPrice = 3; //The latest price(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 20]
    StockField_CurPriceToHighest52WeeksRatio = 4; //(Current price - 52-week high) / 52-week high, corresponding to the “percentage from 52-week high” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [-30, -10] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_CurPriceToLowest52WeeksRatio = 5; //(Current price - 52-week minimum) / 52-week minimum, corresponding to the “percentage from 52-week low” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 40] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_HighPriceToHighest52WeeksRatio = 6; //(Today's high - 52 weeks' highest) / 52 weeks' highest(3 decimal place accuracy, the excess part is discarded), for example, a range of [-3, -1] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LowPriceToLowest52WeeksRatio = 7; //(Today's low-52 weeks' lowest) / 52 weeks' lowest(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 70] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_VolumeRatio = 8; //Volume ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 30]
    StockField_BidAskRatio = 9; //Bid-ask ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [-20, 80.5] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LotPrice = 10; //Price per lot(3 decimal place accuracy, the excess part is discarded), for example, a range of [40, 100]
    StockField_MarketVal = 11; //Market value(3 decimal place accuracy, the excess part is discarded), for example, a range of [50000000, 3000000000]
    StockField_PeAnnual = 12; //Trailing P/E(3 decimal place accuracy, the excess part is discarded), for example, a range of [-8, 65.3]
    StockField_PeTTM = 13; //P/E TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 20.5]
    StockField_PbRate = 14; //P/B ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20]
    StockField_ChangeRate5min = 15; //Change rate in 5 minutes(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 6.3] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_ChangeRateBeginYear = 16; //Price change rate from this year(3 decimal place accuracy, the excess part is discarded), for example, a range of [-50.1, 400.7] (This field is in percentage form, so 20 is equivalent to 20%.)
        
    // Basic volume and price attributes
    StockField_PSTTM = 17; //P/S TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 500] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_PCFTTM = 18; //PCF TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 1000] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_TotalShare = 19; //Total number of shares(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatShare = 20; //Shares outstanding(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatMarketVal = 21; //Market value outstanding(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
}
```









**StockField**



``` protobuf
enum StockField
{
    StockField_Unknown = 0; //Unknown
    StockField_StockCode = 1; //Stock code, does not accept list inputs as an interval
    StockField_StockName = 2; //Stock name, does not accept list inputs as an interval
    StockField_CurPrice = 3; //The latest price(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 20]
    StockField_CurPriceToHighest52WeeksRatio = 4; //(Current price - 52-week high) / 52-week high, corresponding to the “percentage from 52-week high” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [-30, -10] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_CurPriceToLowest52WeeksRatio = 5; //(Current price - 52-week minimum) / 52-week minimum, corresponding to the “percentage from 52-week low” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 40] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_HighPriceToHighest52WeeksRatio = 6; //(Today's high - 52 weeks' highest) / 52 weeks' highest(3 decimal place accuracy, the excess part is discarded), for example, a range of [-3, -1] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LowPriceToLowest52WeeksRatio = 7; //(Today's low-52 weeks' lowest) / 52 weeks' lowest(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 70] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_VolumeRatio = 8; //Volume ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 30]
    StockField_BidAskRatio = 9; //Bid-ask ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [-20, 80.5] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LotPrice = 10; //Price per lot(3 decimal place accuracy, the excess part is discarded), for example, a range of [40, 100]
    StockField_MarketVal = 11; //Market value(3 decimal place accuracy, the excess part is discarded), for example, a range of [50000000, 3000000000]
    StockField_PeAnnual = 12; //Trailing P/E(3 decimal place accuracy, the excess part is discarded), for example, a range of [-8, 65.3]
    StockField_PeTTM = 13; //P/E TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 20.5]
    StockField_PbRate = 14; //P/B ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20]
    StockField_ChangeRate5min = 15; //Change rate in 5 minutes(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 6.3] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_ChangeRateBeginYear = 16; //Price change rate from this year(3 decimal place accuracy, the excess part is discarded), for example, a range of [-50.1, 400.7] (This field is in percentage form, so 20 is equivalent to 20%.)
        
    // Basic volume and price attributes
    StockField_PSTTM = 17; //P/S TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 500] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_PCFTTM = 18; //PCF TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 1000] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_TotalShare = 19; //Total number of shares(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatShare = 20; //Shares outstanding(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatMarketVal = 21; //Market value outstanding(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
}
```









**StockField**



``` protobuf
enum StockField
{
    StockField_Unknown = 0; //Unknown
    StockField_StockCode = 1; //Stock code, does not accept list inputs as an interval
    StockField_StockName = 2; //Stock name, does not accept list inputs as an interval
    StockField_CurPrice = 3; //The latest price(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 20]
    StockField_CurPriceToHighest52WeeksRatio = 4; //(Current price - 52-week high) / 52-week high, corresponding to the “percentage from 52-week high” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [-30, -10] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_CurPriceToLowest52WeeksRatio = 5; //(Current price - 52-week minimum) / 52-week minimum, corresponding to the “percentage from 52-week low” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 40] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_HighPriceToHighest52WeeksRatio = 6; //(Today's high - 52 weeks' highest) / 52 weeks' highest(3 decimal place accuracy, the excess part is discarded), for example, a range of [-3, -1] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LowPriceToLowest52WeeksRatio = 7; //(Today's low-52 weeks' lowest) / 52 weeks' lowest(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 70] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_VolumeRatio = 8; //Volume ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 30]
    StockField_BidAskRatio = 9; //Bid-ask ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [-20, 80.5] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LotPrice = 10; //Price per lot(3 decimal place accuracy, the excess part is discarded), for example, a range of [40, 100]
    StockField_MarketVal = 11; //Market value(3 decimal place accuracy, the excess part is discarded), for example, a range of [50000000, 3000000000]
    StockField_PeAnnual = 12; //Trailing P/E(3 decimal place accuracy, the excess part is discarded), for example, a range of [-8, 65.3]
    StockField_PeTTM = 13; //P/E TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 20.5]
    StockField_PbRate = 14; //P/B ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20]
    StockField_ChangeRate5min = 15; //Change rate in 5 minutes(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 6.3] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_ChangeRateBeginYear = 16; //Price change rate from this year(3 decimal place accuracy, the excess part is discarded), for example, a range of [-50.1, 400.7] (This field is in percentage form, so 20 is equivalent to 20%.)
        
    // Basic volume and price attributes
    StockField_PSTTM = 17; //P/S TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 500] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_PCFTTM = 18; //PCF TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 1000] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_TotalShare = 19; //Total number of shares(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatShare = 20; //Shares outstanding(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatMarketVal = 21; //Market value outstanding(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
}
```









**StockField**



``` protobuf
enum StockField
{
    StockField_Unknown = 0; //Unknown
    StockField_StockCode = 1; //Stock code, does not accept list inputs as an interval
    StockField_StockName = 2; //Stock name, does not accept list inputs as an interval
    StockField_CurPrice = 3; //The latest price(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 20]
    StockField_CurPriceToHighest52WeeksRatio = 4; //(Current price - 52-week high) / 52-week high, corresponding to the “percentage from 52-week high” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [-30, -10] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_CurPriceToLowest52WeeksRatio = 5; //(Current price - 52-week minimum) / 52-week minimum, corresponding to the “percentage from 52-week low” on the PC terminal (3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 40] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_HighPriceToHighest52WeeksRatio = 6; //(Today's high - 52 weeks' highest) / 52 weeks' highest(3 decimal place accuracy, the excess part is discarded), for example, a range of [-3, -1] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LowPriceToLowest52WeeksRatio = 7; //(Today's low-52 weeks' lowest) / 52 weeks' lowest(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 70] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_VolumeRatio = 8; //Volume ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 30]
    StockField_BidAskRatio = 9; //Bid-ask ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [-20, 80.5] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LotPrice = 10; //Price per lot(3 decimal place accuracy, the excess part is discarded), for example, a range of [40, 100]
    StockField_MarketVal = 11; //Market value(3 decimal place accuracy, the excess part is discarded), for example, a range of [50000000, 3000000000]
    StockField_PeAnnual = 12; //Trailing P/E(3 decimal place accuracy, the excess part is discarded), for example, a range of [-8, 65.3]
    StockField_PeTTM = 13; //P/E TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 20.5]
    StockField_PbRate = 14; //P/B ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20]
    StockField_ChangeRate5min = 15; //Change rate in 5 minutes(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 6.3] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_ChangeRateBeginYear = 16; //Price change rate from this year(3 decimal place accuracy, the excess part is discarded), for example, a range of [-50.1, 400.7] (This field is in percentage form, so 20 is equivalent to 20%.)
        
    // Basic volume and price attributes
    StockField_PSTTM = 17; //P/S TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 500] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_PCFTTM = 18; //PCF TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 1000] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_TotalShare = 19; //Total number of shares(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatShare = 20; //Shares outstanding(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatMarketVal = 21; //Market value outstanding(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
}
```









**StockField**



``` protobuf
enum StockField
{
    StockField_Unknown = 0; //Unknown
    StockField_StockCode = 1; //Stock code, does not accept list inputs as an interval
    StockField_StockName = 2; //Stock name, does not accept list inputs as an interval
    StockField_CurPrice = 3; //The latest price(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 20]
    StockField_CurPriceToHighest52WeeksRatio = 4; //(Current price - 52-week high) / 52-week high, corresponding to the “percentage from 52-week high” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [-30, -10] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_CurPriceToLowest52WeeksRatio = 5; //(Current price - 52-week minimum) / 52-week minimum, corresponding to the “percentage from 52-week low” on the PC terminal(3 decimal place accuracy, the excess part is discarded), for example, a range of [20, 40] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_HighPriceToHighest52WeeksRatio = 6; //(Today's high - 52 weeks' highest) / 52 weeks' highest(3 decimal place accuracy, the excess part is discarded), for example, a range of [-3, -1] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LowPriceToLowest52WeeksRatio = 7; //(Today's low-52 weeks' lowest) / 52 weeks' lowest(3 decimal place accuracy, the excess part is discarded), for example, a range of [10, 70] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_VolumeRatio = 8; //Volume ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 30]
    StockField_BidAskRatio = 9; //Bid-ask ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [-20, 80.5] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_LotPrice = 10; //Price per lot(3 decimal place accuracy, the excess part is discarded), for example, a range of [40, 100]
    StockField_MarketVal = 11; //Market value(3 decimal place accuracy, the excess part is discarded), for example, a range of [50000000, 3000000000]
    StockField_PeAnnual = 12; //Trailing P/E(3 decimal place accuracy, the excess part is discarded), for example, a range of [-8, 65.3]
    StockField_PeTTM = 13; //P/E TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [-10, 20.5]
    StockField_PbRate = 14; //P/B ratio(3 decimal place accuracy, the excess part is discarded), for example, a range of [0.5, 20]
    StockField_ChangeRate5min = 15; //Change rate in 5 minutes(3 decimal place accuracy, the excess part is discarded), for example, a range of [-5, 6.3] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_ChangeRateBeginYear = 16; //Price change rate from this year(3 decimal place accuracy, the excess part is discarded), for example, a range of [-50.1, 400.7] (This field is in percentage form, so 20 is equivalent to 20%.)
        
    // Basic volume and price attributes
    StockField_PSTTM = 17; //P/S TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 500] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_PCFTTM = 18; //PCF TTM(3 decimal place accuracy, the excess part is discarded), for example, a range of [100, 1000] (This field is in percentage form, so 20 is equivalent to 20%.)
    StockField_TotalShare = 19; //Total number of shares(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatShare = 20; //Shares outstanding(0 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: share)
    StockField_FloatMarketVal = 21; //Market value outstanding(3 decimal place accuracy, the excess part is discarded), for example, a range of [1000000000, 1000000000] (unit: yuan)
}
```









## <a href="#7721" class="header-anchor">#</a> Subscription Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SubType**

- `NONE`

  Unknown

- `QUOTE`

  Basic quote

- `ORDER_BOOK`

  Order book

- `TICKER`

  Tick-by-tick

- `RT_DATA`

  Time Frame

- `K_DAY`

  Daily candlesticks

- `K_5M`

  5 minutes candlesticks

- `K_15M`

  15 minutes candlesticks

- `K_30M`

  30 minutes candlesticks

- `K_60M`

  60 minutes candlesticks

- `K_1M`

  1 minute candlesticks

- `K_WEEK`

  Weekly candlesticks

- `K_MON`

  Monthly candlesticks

- `BROKER`

  Broker's queue

- `K_QURATER`

  Seasonal candlesticks

- `K_YEAR`

  Annual candlesticks

- `K_3M`

  3 minutes candlesticks





**SubType**



``` protobuf
enum SubType
{
    SubType_None = 0; //Unknown
    SubType_Basic = 1; //Basic quote
    SubType_OrderBook = 2; //Order book
    SubType_Ticker = 4; //Tick-by-tick
    SubType_RT = 5; //Time Frame
    SubType_KL_Day = 6; //Daily candlesticks
    SubType_KL_5Min = 7; //5 minutes candlesticks
    SubType_KL_15Min = 8; //15 minutes candlesticks
    SubType_KL_30Min = 9; //30 minutes candlesticks
    SubType_KL_60Min = 10; //60 minutes candlesticks
    SubType_KL_1Min = 11; //1 minute candlesticks
    SubType_KL_Week = 12; //Weekly candlesticks
    SubType_KL_Month = 13; //Monthly candlesticks
    SubType_Broker = 14; //Broker's queue
    SubType_KL_Qurater = 15; //Seasonal candlesticks
    SubType_KL_Year = 16; //Annual candlesticks
    SubType_KL_3Min = 17; //3 minutes candlesticks
}
```









**SubType**



``` protobuf
enum SubType
{
    SubType_None = 0; //Unknown
    SubType_Basic = 1; //Basic quote
    SubType_OrderBook = 2; //Order book
    SubType_Ticker = 4; //Tick-by-tick
    SubType_RT = 5; //Time Frame
    SubType_KL_Day = 6; //Daily candlesticks
    SubType_KL_5Min = 7; //5 minutes candlesticks
    SubType_KL_15Min = 8; //15 minutes candlesticks
    SubType_KL_30Min = 9; //30 minutes candlesticks
    SubType_KL_60Min = 10; //60 minutes candlesticks
    SubType_KL_1Min = 11; //1 minute candlesticks
    SubType_KL_Week = 12; //Weekly candlesticks
    SubType_KL_Month = 13; //Monthly candlesticks
    SubType_Broker = 14; //Broker's queue
    SubType_KL_Qurater = 15; //Seasonal candlesticks
    SubType_KL_Year = 16; //Annual candlesticks
    SubType_KL_3Min = 17; //3 minutes candlesticks
}
```









**SubType**



``` protobuf
enum SubType
{
    SubType_None = 0; //Unknown
    SubType_Basic = 1; //Basic quote
    SubType_OrderBook = 2; //Order book
    SubType_Ticker = 4; //Tick-by-tick
    SubType_RT = 5; //Time Frame
    SubType_KL_Day = 6; //Daily candlesticks
    SubType_KL_5Min = 7; //5 minutes candlesticks
    SubType_KL_15Min = 8; //15 minutes candlesticks
    SubType_KL_30Min = 9; //30 minutes candlesticks
    SubType_KL_60Min = 10; //60 minutes candlesticks
    SubType_KL_1Min = 11; //1 minute candlesticks
    SubType_KL_Week = 12; //Weekly candlesticks
    SubType_KL_Month = 13; //Monthly candlesticks
    SubType_Broker = 14; //Broker's queue
    SubType_KL_Qurater = 15; //Seasonal candlesticks
    SubType_KL_Year = 16; //Annual candlesticks
    SubType_KL_3Min = 17; //3 minutes candlesticks
}
```









**SubType**



``` protobuf
enum SubType
{
    SubType_None = 0; //Unknown
    SubType_Basic = 1; //Basic quote
    SubType_OrderBook = 2; //Order book
    SubType_Ticker = 4; //Tick-by-tick
    SubType_RT = 5; //Time Frame
    SubType_KL_Day = 6; //Daily candlesticks
    SubType_KL_5Min = 7; //5 minutes candlesticks
    SubType_KL_15Min = 8; //15 minutes candlesticks
    SubType_KL_30Min = 9; //30 minutes candlesticks
    SubType_KL_60Min = 10; //60 minutes candlesticks
    SubType_KL_1Min = 11; //1 minute candlesticks
    SubType_KL_Week = 12; //Weekly candlesticks
    SubType_KL_Month = 13; //Monthly candlesticks
    SubType_Broker = 14; //Broker's queue
    SubType_KL_Qurater = 15; //Seasonal candlesticks
    SubType_KL_Year = 16; //Annual candlesticks
    SubType_KL_3Min = 17; //3 minutes candlesticks
}
```









**SubType**



``` protobuf
enum SubType
{
    SubType_None = 0; //Unknown
    SubType_Basic = 1; //Basic quote
    SubType_OrderBook = 2; //Order book
    SubType_Ticker = 4; //Tick-by-tick
    SubType_RT = 5; //Time Frame
    SubType_KL_Day = 6; //Daily candlesticks
    SubType_KL_5Min = 7; //5 minutes candlesticks
    SubType_KL_15Min = 8; //15 minutes candlesticks
    SubType_KL_30Min = 9; //30 minutes candlesticks
    SubType_KL_60Min = 10; //60 minutes candlesticks
    SubType_KL_1Min = 11; //1 minute candlesticks
    SubType_KL_Week = 12; //Weekly candlesticks
    SubType_KL_Month = 13; //Monthly candlesticks
    SubType_Broker = 14; //Broker's queue
    SubType_KL_Qurater = 15; //Seasonal candlesticks
    SubType_KL_Year = 16; //Annual candlesticks
    SubType_KL_3Min = 17; //3 minutes candlesticks
}
```









## <a href="#832" class="header-anchor">#</a> Transaction Direction





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TickerDirect**

- `NONE`

  unknown

- `BUY`

  Active buy

  

  
  

  

  
  
  

  Active buy, a buyer actively buys stocks at the then sell price or
  higher price.

  

  

  

  

- `SELL`

  Active sell

  

  
  

  

  
  
  

  Active sell, a seller actively sells stocks at the then buy price or
  lower price.

  

  

  

  

- `NEUTRAL`

  Neutral transaction

  

  
  

  

  
  
  

  Neutral transaction, the stock price is between the bid price and ask
  price.

  

  

  

  





**TickerDirection**



``` protobuf
enum TickerDirection
{
    TickerDirection_Unknown = 0; //Unknown
    TickerDirection_Bid = 1; //Active buy, a buyer actively buys stocks at the then sell price or higher price.
    TickerDirection_Ask = 2; //Active sell, a seller actively sells stocks at the then buy price or lower price.
    TickerDirection_Neutral = 3; //Neutral transaction, the stock price is between the bid price and ask price.
}
```









**TickerDirection**



``` protobuf
enum TickerDirection
{
    TickerDirection_Unknown = 0; //Unknown
    TickerDirection_Bid = 1; //Active buy, a buyer actively buys stocks at the then sell price or higher price.
    TickerDirection_Ask = 2; //Active sell, a seller actively sells stocks at the then buy price or lower price.
    TickerDirection_Neutral = 3; //Neutral transaction, the stock price is between the bid price and ask price.
}
```









**TickerDirection**



``` protobuf
enum TickerDirection
{
    TickerDirection_Unknown = 0; //Unknown
    TickerDirection_Bid = 1; //Active buy, a buyer actively buys stocks at the then sell price or higher price.
    TickerDirection_Ask = 2; //Active sell, a seller actively sells stocks at the then buy price or lower price.
    TickerDirection_Neutral = 3; //Neutral transaction, the stock price is between the bid price and ask price.
}
```









**TickerDirection**



``` protobuf
enum TickerDirection
{
    TickerDirection_Unknown = 0; //Unknown
    TickerDirection_Bid = 1; //Active buy, a buyer actively buys stocks at the then sell price or higher price.
    TickerDirection_Ask = 2; //Active sell, a seller actively sells stocks at the then buy price or lower price.
    TickerDirection_Neutral = 3; //Neutral transaction, the stock price is between the bid price and ask price.
}
```









**TickerDirection**



``` protobuf
enum TickerDirection
{
    TickerDirection_Unknown = 0; //Unknown
    TickerDirection_Bid = 1; //Active buy, a buyer actively buys stocks at the then sell price or higher price.
    TickerDirection_Ask = 2; //Active sell, a seller actively sells stocks at the then buy price or lower price.
    TickerDirection_Neutral = 3; //Neutral transaction, the stock price is between the bid price and ask price.
}
```









## <a href="#9844" class="header-anchor">#</a> Tick-by-Tick Transaction Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TickerType**

- `UNKNOWN`

  Unknown

- `AUTO_MATCH`

  Regular sale

- `LATE`

  Pre-market trade

- `NON_AUTO_MATCH`

  Non-regular sale

- `INTER_AUTO_MATCH`

  Regular sale for same broker

- `INTER_NON_AUTO_MATCH`

  Non-regular sale for same broker

- `ODD_LOT`

  Odd lot trade

- `AUCTION`

  Auction trade

- `BULK`

  Bunched trade

- `CRASH`

  Cash trade

- `CROSS_MARKET`

  Intermarket sweep

- `BULK_SOLD`

  Bunched sold trade

- `FREE_ON_BOARD`

  Price variation trade

- `RULE127_OR155`

  Rule 127 (NYSE only) or Rule 155 (NYSE MKT only)

- `DELAY`

  Delay the transaction

- `MARKET_CENTER_CLOSE_PRICE`

  Market center close price

- `NEXT_DAY`

  Next day

- `MARKET_CENTER_OPENING`

  Market center opening trade

- `PRIOR_REFERENCE_PRICE`

  Prior reference price

- `MARKET_CENTER_OPEN_PRICE`

  Market center open price

- `SELLER`

  Seller

- `T`

  Form T(pre-open and post-close market trade)

- `EXTENDED_TRADING_HOURS`

  Extended trading hours/sold out of sequence

- `CONTINGENT`

  Contingent trade

- `AVERAGE_PRICE`

  Average price trade

- `OTC_SOLD`

  Sold(out of sequence)

- `ODD_LOT_CROSS_MARKET`

  Odd lot cross trade

- `DERIVATIVELY_PRICED`

  Derivatively priced

- `REOPENINGP_RICED`

  Re-Opening price

- `CLOSING_PRICED`

  Closing price

- `COMPREHENSIVE_DELAY_PRICE`

  Consolidated late price per listing packet

- `OVERSEAS`

  One party to the transaction is not a member of the Hong Kong Stock
  Exchange and is an over-the-counter transaction





**TickerType**



``` protobuf
enum TickerType
{
    TickerType_Unknown = 0; //Unknown
    TickerType_Automatch = 1; //Regular sale
    TickerType_Late = 2; //Pre-market trade
    TickerType_NoneAutomatch = 3; //Non-regular sale
    TickerType_InterAutomatch = 4; //Regular sale for same broker
    TickerType_InterNoneAutomatch = 5; //Non-regular sale for same broker
    TickerType_OddLot = 6; //Odd lot trade
    TickerType_Auction = 7; //Auction trade
    TickerType_Bulk = 8; //Bunched Trade
    TickerType_Crash = 9; //Cash Trade
    TickerType_CrossMarket = 10; //Intermarket sweep
    TickerType_BulkSold = 11; //Bunched sold trade
    TickerType_FreeOnBoard = 12; //Price variation trade
    TickerType_Rule127Or155 = 13; //Rule 127 (NYSE only) or Rule 155 (NYSE MKT only)
    TickerType_Delay = 14; //Sold last
    TickerType_MarketCenterClosePrice = 15; //Market center close price
    TickerType_NextDay = 16; //Next day
    TickerType_MarketCenterOpening = 17; //Market center opening trade
    TickerType_PriorReferencePrice = 18; //Prior reference price
    TickerType_MarketCenterOpenPrice = 19; //Market center open price
    TickerType_Seller = 20; //Seller
    TickerType_T = 21; //Form T(pre-open and post-close market trade)
    TickerType_ExtendedTradingHours = 22; //Extended trading hours/sold out of sequence
    TickerType_Contingent = 23; //Contingent trade
    TickerType_AvgPrice = 24; //Average price trade
    TickerType_OTCSold = 25; //Sold(out of sequence)
    TickerType_OddLotCrossMarket = 26; //Odd lot cross trade
    TickerType_DerivativelyPriced = 27; //Derivatively priced
    TickerType_ReOpeningPriced = 28; //Re-Opening price
    TickerType_ClosingPriced = 29; //Closing price
    TickerType_ComprehensiveDelayPrice = 30; //Consolidated late price per listing packet
    TickerType_Overseas = 31; //One party to the transaction is not a member of the Hong Kong Stock Exchange and is an over-the-counter transaction
}
```









**TickerType**



``` protobuf
enum TickerType
{
    TickerType_Unknown = 0; //Unknown
    TickerType_Automatch = 1; //Regular sale
    TickerType_Late = 2; //Pre-market trade
    TickerType_NoneAutomatch = 3; //Non-regular sale
    TickerType_InterAutomatch = 4; //Regular sale for same broker
    TickerType_InterNoneAutomatch = 5; //Non-regular sale for same broker
    TickerType_OddLot = 6; //Odd lot trade
    TickerType_Auction = 7; //Auction trade
    TickerType_Bulk = 8; //Bunched Trade
    TickerType_Crash = 9; //Cash Trade
    TickerType_CrossMarket = 10; //Intermarket sweep
    TickerType_BulkSold = 11; //Bunched sold trade
    TickerType_FreeOnBoard = 12; //Price variation trade
    TickerType_Rule127Or155 = 13; //Rule 127 (NYSE only) or Rule 155 (NYSE MKT only)
    TickerType_Delay = 14; //Sold last
    TickerType_MarketCenterClosePrice = 15; //Market center close price
    TickerType_NextDay = 16; //Next day
    TickerType_MarketCenterOpening = 17; //Market center opening trade
    TickerType_PriorReferencePrice = 18; //Prior reference price
    TickerType_MarketCenterOpenPrice = 19; //Market center open price
    TickerType_Seller = 20; //Seller
    TickerType_T = 21; //Form T(pre-open and post-close market trade)
    TickerType_ExtendedTradingHours = 22; //Extended trading hours/sold out of sequence
    TickerType_Contingent = 23; //Contingent trade
    TickerType_AvgPrice = 24; //Average price trade
    TickerType_OTCSold = 25; //Sold(out of sequence)
    TickerType_OddLotCrossMarket = 26; //Odd lot cross trade
    TickerType_DerivativelyPriced = 27; //Derivatively priced
    TickerType_ReOpeningPriced = 28; //Re-Opening price
    TickerType_ClosingPriced = 29; //Closing price
    TickerType_ComprehensiveDelayPrice = 30; //Consolidated late price per listing packet
    TickerType_Overseas = 31; //One party to the transaction is not a member of the Hong Kong Stock Exchange and is an over-the-counter transaction
}
```









**TickerType**



``` protobuf
enum TickerType
{
    TickerType_Unknown = 0; //Unknown
    TickerType_Automatch = 1; //Regular sale
    TickerType_Late = 2; //Pre-market trade
    TickerType_NoneAutomatch = 3; //Non-regular sale
    TickerType_InterAutomatch = 4; //Regular sale for same broker
    TickerType_InterNoneAutomatch = 5; //Non-regular sale for same broker
    TickerType_OddLot = 6; //Odd lot trade
    TickerType_Auction = 7; //Auction trade
    TickerType_Bulk = 8; //Bunched Trade
    TickerType_Crash = 9; //Cash Trade
    TickerType_CrossMarket = 10; //Intermarket sweep
    TickerType_BulkSold = 11; //Bunched sold trade
    TickerType_FreeOnBoard = 12; //Price variation trade
    TickerType_Rule127Or155 = 13; //Rule 127 (NYSE only) or Rule 155 (NYSE MKT only)
    TickerType_Delay = 14; //Sold last
    TickerType_MarketCenterClosePrice = 15; //Market center close price
    TickerType_NextDay = 16; //Next day
    TickerType_MarketCenterOpening = 17; //Market center opening trade
    TickerType_PriorReferencePrice = 18; //Prior reference price
    TickerType_MarketCenterOpenPrice = 19; //Market center open price
    TickerType_Seller = 20; //Seller
    TickerType_T = 21; //Form T(pre-open and post-close market trade)
    TickerType_ExtendedTradingHours = 22; //Extended trading hours/sold out of sequence
    TickerType_Contingent = 23; //Contingent trade
    TickerType_AvgPrice = 24; //Average price trade
    TickerType_OTCSold = 25; //Sold(out of sequence)
    TickerType_OddLotCrossMarket = 26; //Odd lot cross trade
    TickerType_DerivativelyPriced = 27; //Derivatively priced
    TickerType_ReOpeningPriced = 28; //Re-Opening price
    TickerType_ClosingPriced = 29; //Closing price
    TickerType_ComprehensiveDelayPrice = 30; //Consolidated late price per listing packet
    TickerType_Overseas = 31; //One party to the transaction is not a member of the Hong Kong Stock Exchange and is an over-the-counter transaction
}
```









**TickerType**



``` protobuf
enum TickerType
{
    TickerType_Unknown = 0; //Unknown
    TickerType_Automatch = 1; //Regular sale
    TickerType_Late = 2; //Pre-market trade
    TickerType_NoneAutomatch = 3; //Non-regular sale
    TickerType_InterAutomatch = 4; //Regular sale for same broker
    TickerType_InterNoneAutomatch = 5; //Non-regular sale for same broker
    TickerType_OddLot = 6; //Odd lot trade
    TickerType_Auction = 7; //Auction trade
    TickerType_Bulk = 8; //Bunched Trade
    TickerType_Crash = 9; //Cash Trade
    TickerType_CrossMarket = 10; //Intermarket sweep
    TickerType_BulkSold = 11; //Bunched sold trade
    TickerType_FreeOnBoard = 12; //Price variation trade
    TickerType_Rule127Or155 = 13; //Rule 127 (NYSE only) or Rule 155 (NYSE MKT only)
    TickerType_Delay = 14; //Sold last
    TickerType_MarketCenterClosePrice = 15; //Market center close price
    TickerType_NextDay = 16; //Next day
    TickerType_MarketCenterOpening = 17; //Market center opening trade
    TickerType_PriorReferencePrice = 18; //Prior reference price
    TickerType_MarketCenterOpenPrice = 19; //Market center open price
    TickerType_Seller = 20; //Seller
    TickerType_T = 21; //Form T(pre-open and post-close market trade)
    TickerType_ExtendedTradingHours = 22; //Extended trading hours/sold out of sequence
    TickerType_Contingent = 23; //Contingent trade
    TickerType_AvgPrice = 24; //Average price trade
    TickerType_OTCSold = 25; //Sold(out of sequence)
    TickerType_OddLotCrossMarket = 26; //Odd lot cross trade
    TickerType_DerivativelyPriced = 27; //Derivatively priced
    TickerType_ReOpeningPriced = 28; //Re-Opening price
    TickerType_ClosingPriced = 29; //Closing price
    TickerType_ComprehensiveDelayPrice = 30; //Consolidated late price per listing packet
    TickerType_Overseas = 31; //One party to the transaction is not a member of the Hong Kong Stock Exchange and is an over-the-counter transaction
}
```









**TickerType**



``` protobuf
enum TickerType
{
    TickerType_Unknown = 0; //Unknown
    TickerType_Automatch = 1; //Regular sale
    TickerType_Late = 2; //Pre-market trade
    TickerType_NoneAutomatch = 3; //Non-regular sale
    TickerType_InterAutomatch = 4; //Regular sale for same broker
    TickerType_InterNoneAutomatch = 5; //Non-regular sale for same broker
    TickerType_OddLot = 6; //Odd lot trade
    TickerType_Auction = 7; //Auction trade
    TickerType_Bulk = 8; //Bunched Trade
    TickerType_Crash = 9; //Cash Trade
    TickerType_CrossMarket = 10; //Intermarket sweep
    TickerType_BulkSold = 11; //Bunched sold trade
    TickerType_FreeOnBoard = 12; //Price variation trade
    TickerType_Rule127Or155 = 13; //Rule 127 (NYSE only) or Rule 155 (NYSE MKT only)
    TickerType_Delay = 14; //Sold last
    TickerType_MarketCenterClosePrice = 15; //Market center close price
    TickerType_NextDay = 16; //Next day
    TickerType_MarketCenterOpening = 17; //Market center opening trade
    TickerType_PriorReferencePrice = 18; //Prior reference price
    TickerType_MarketCenterOpenPrice = 19; //Market center open price
    TickerType_Seller = 20; //Seller
    TickerType_T = 21; //Form T(pre-open and post-close market trade)
    TickerType_ExtendedTradingHours = 22; //Extended trading hours/sold out of sequence
    TickerType_Contingent = 23; //Contingent trade
    TickerType_AvgPrice = 24; //Average price trade
    TickerType_OTCSold = 25; //Sold(out of sequence)
    TickerType_OddLotCrossMarket = 26; //Odd lot cross trade
    TickerType_DerivativelyPriced = 27; //Derivatively priced
    TickerType_ReOpeningPriced = 28; //Re-Opening price
    TickerType_ClosingPriced = 29; //Closing price
    TickerType_ComprehensiveDelayPrice = 30; //Consolidated late price per listing packet
    TickerType_Overseas = 31; //One party to the transaction is not a member of the Hong Kong Stock Exchange and is an over-the-counter transaction
}
```









## <a href="#6587" class="header-anchor">#</a> Check The Market on The Trading Day





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TradeDateMarket**

- `NONE`

  Unknown

- `HK`

  HK market

  

  
  

  

  
  
  

  - Including stocks, ETFs, warrants, CBBCs, options, non-holiday
    trading futures
  - Excluding holiday trading futures

  

  

  

  

- `US`

  US market

  

  
  

  

  
  
  

  - Including stocks, ETFs, options
  - Excluding futures

  

  

  

  

- `CN`

  A-share market

- `NT`

  Northbound Trading

- `ST`

  Southbound Trading

- `JP_FUTURE`

  Japanese future market

- `SG_FUTURE`

  Singapore future market





**TradeDateMarket**



``` protobuf
enum TradeDateMarket
{
    TradeDateMarket_Unknown = 0; //Unknown
    TradeDateMarket_HK = 1; //HK market (including stocks, ETFs, warrants, CBBCs, options, futures)
    TradeDateMarket_US = 2; //US market (including stocks, ETFs, options. Excluding futures)
    TradeDateMarket_CN = 3; //A-share stock market
    TradeDateMarket_NT = 4; //HK->SZ (SH) Connect
    TradeDateMarket_ST = 5; //Southbound (SZ, SH)
    TradeDateMarket_JP_Future = 6; //Japanese future market
    TradeDateMarket_SG_Future = 7; //Singapore future market
}
```









**TradeDateMarket**



``` protobuf
enum TradeDateMarket
{
    TradeDateMarket_Unknown = 0; //Unknown
    TradeDateMarket_HK = 1; //HK market (including stocks, ETFs, warrants, CBBCs, options, futures)
    TradeDateMarket_US = 2; //US market (including stocks, ETFs, options. Excluding futures)
    TradeDateMarket_CN = 3; //A-share stock market
    TradeDateMarket_NT = 4; //HK->SZ (SH) Connect
    TradeDateMarket_ST = 5; //Southbound (SZ, SH)
    TradeDateMarket_JP_Future = 6; //Japanese future market
    TradeDateMarket_SG_Future = 7; //Singapore future market
}
```









**TradeDateMarket**



``` protobuf
enum TradeDateMarket
{
    TradeDateMarket_Unknown = 0; //Unknown
    TradeDateMarket_HK = 1; //HK market (including stocks, ETFs, warrants, CBBCs, options, futures)
    TradeDateMarket_US = 2; //US market (including stocks, ETFs, options. Excluding futures)
    TradeDateMarket_CN = 3; //A-share stock market
    TradeDateMarket_NT = 4; //HK->SZ (SH) Connect
    TradeDateMarket_ST = 5; //Southbound (SZ, SH)
    TradeDateMarket_JP_Future = 6; //Japanese future market
    TradeDateMarket_SG_Future = 7; //Singapore future market
}
```









**TradeDateMarket**



``` protobuf
enum TradeDateMarket
{
    TradeDateMarket_Unknown = 0; //Unknown
    TradeDateMarket_HK = 1; //HK market (including stocks, ETFs, warrants, CBBCs, options, futures)
    TradeDateMarket_US = 2; //US market (including stocks, ETFs, options. Excluding futures)
    TradeDateMarket_CN = 3; //A-share stock market
    TradeDateMarket_NT = 4; //HK->SZ (SH) Connect
    TradeDateMarket_ST = 5; //Southbound (SZ, SH)
    TradeDateMarket_JP_Future = 6; //Japanese future market
    TradeDateMarket_SG_Future = 7; //Singapore future market
}
```









**TradeDateMarket**



``` protobuf
enum TradeDateMarket
{
    TradeDateMarket_Unknown = 0; //Unknown
    TradeDateMarket_HK = 1; //HK market (including stocks, ETFs, warrants, CBBCs, options, futures)
    TradeDateMarket_US = 2; //US market (including stocks, ETFs, options. Excluding futures)
    TradeDateMarket_CN = 3; //A-share stock market
    TradeDateMarket_NT = 4; //HK->SZ (SH) Connect
    TradeDateMarket_ST = 5; //Southbound (SZ, SH)
    TradeDateMarket_JP_Future = 6; //Japanese future market
    TradeDateMarket_SG_Future = 7; //Singapore future market
}
```









## <a href="#8930" class="header-anchor">#</a> Type of Trading Day





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TradeDateType**

- `WHOLE`

  Whole day trading

- `MORNING`

  Trading in the morning, closed in the afternoon

- `AFTERNOON`

  Trading in the afternoon, closed in the morning





**TradeDateType**



``` protobuf
enum TradeDateType
{
    TradeDateType_Whole = 0; //Whole day trading
    TradeDateType_Morning = 1; //Trading in the morning, closed in the afternoon
    TradeDateType_Afternoon = 2; //Trading in the afternoon, closed in the morning
}
```









**TradeDateType**



``` protobuf
enum TradeDateType
{
    TradeDateType_Whole = 0; //Whole day trading
    TradeDateType_Morning = 1; //Trading in the morning, closed in the afternoon
    TradeDateType_Afternoon = 2; //Trading in the afternoon, closed in the morning
}
```









**TradeDateType**



``` protobuf
enum TradeDateType
{
    TradeDateType_Whole = 0; //Whole day trading
    TradeDateType_Morning = 1; //Trading in the morning, closed in the afternoon
    TradeDateType_Afternoon = 2; //Trading in the afternoon, closed in the morning
}
```









**TradeDateType**



``` protobuf
enum TradeDateType
{
    TradeDateType_Whole = 0; //Whole day trading
    TradeDateType_Morning = 1; //Trading in the morning, closed in the afternoon
    TradeDateType_Afternoon = 2; //Trading in the afternoon, closed in the morning
}
```









**TradeDateType**



``` protobuf
enum TradeDateType
{
    TradeDateType_Whole = 0; //Whole day trading
    TradeDateType_Morning = 1; //Trading in the morning, closed in the afternoon
    TradeDateType_Afternoon = 2; //Trading in the afternoon, closed in the morning
}
```









## <a href="#5892" class="header-anchor">#</a> Warrant Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **WarrantStatus**

- `NONE`

  Unknown

- `NORMAL`

  Normal status

- `SUSPEND`

  Suspended

- `STOP_TRADE`

  Stop trading

- `PENDING_LISTING`

  Waiting to be listed





**WarrantStatus**



``` protobuf
enum WarrantStatus
{
    WarrantStatus_Unknow = 0; //Unknown
    WarrantStatus_Normal = 1; //Normal status
    WarrantStatus_Suspend = 2; //Suspended
    WarrantStatus_StopTrade = 3; //Stop trading
    WarrantStatus_PendingListing = 4; //Waiting to be listed
}
```









**WarrantStatus**



``` protobuf
enum WarrantStatus
{
    WarrantStatus_Unknow = 0; //Unknown
    WarrantStatus_Normal = 1; //Normal status
    WarrantStatus_Suspend = 2; //Suspended
    WarrantStatus_StopTrade = 3; //Stop trading
    WarrantStatus_PendingListing = 4; //Waiting to be listed
}
```









**WarrantStatus**



``` protobuf
enum WarrantStatus
{
    WarrantStatus_Unknow = 0; //Unknown
    WarrantStatus_Normal = 1; //Normal status
    WarrantStatus_Suspend = 2; //Suspended
    WarrantStatus_StopTrade = 3; //Stop trading
    WarrantStatus_PendingListing = 4; //Waiting to be listed
}
```









**WarrantStatus**



``` protobuf
enum WarrantStatus
{
    WarrantStatus_Unknow = 0; //Unknown
    WarrantStatus_Normal = 1; //Normal status
    WarrantStatus_Suspend = 2; //Suspended
    WarrantStatus_StopTrade = 3; //Stop trading
    WarrantStatus_PendingListing = 4; //Waiting to be listed
}
```









**WarrantStatus**



``` protobuf
enum WarrantStatus
{
    WarrantStatus_Unknow = 0; //Unknown
    WarrantStatus_Normal = 1; //Normal status
    WarrantStatus_Suspend = 2; //Suspended
    WarrantStatus_StopTrade = 3; //Stop trading
    WarrantStatus_PendingListing = 4; //Waiting to be listed
}
```









## <a href="#2421" class="header-anchor">#</a> Warrant Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **WrtType**

- `NONE`

  Unknown

- `CALL`

  Long warrants

- `PUT`

  Short warrants

- `BULL`

  Call warrants

- `BEAR`

  Put warrants

- `INLINE`

  Inline Warrants





**WarrantType**



``` protobuf
enum WarrantType
{
    WarrantType_Unknown = 0; //Unknown
    WarrantType_Buy = 1; //Long warrants
    WarrantType_Sell = 2; //Short warrants
    WarrantType_Bull = 3; //Call warrants
    WarrantType_Bear = 4; //Put warrants
    WarrantType_InLine = 5; //Inline Warrants
}
```









**WarrantType**



``` protobuf
enum WarrantType
{
    WarrantType_Unknown = 0; //Unknown
    WarrantType_Buy = 1; //Long warrants
    WarrantType_Sell = 2; //Short warrants
    WarrantType_Bull = 3; //Call warrants
    WarrantType_Bear = 4; //Put warrants
    WarrantType_InLine = 5; //Inline Warrants
}
```









**WarrantType**



``` protobuf
enum WarrantType
{
    WarrantType_Unknown = 0; //Unknown
    WarrantType_Buy = 1; //Long warrants
    WarrantType_Sell = 2; //Short warrants
    WarrantType_Bull = 3; //Call warrants
    WarrantType_Bear = 4; //Put warrants
    WarrantType_InLine = 5; //Inline Warrants
}
```









**WarrantType**



``` protobuf
enum WarrantType
{
    WarrantType_Unknown = 0; //Unknown
    WarrantType_Buy = 1; //Long warrants
    WarrantType_Sell = 2; //Short warrants
    WarrantType_Bull = 3; //Call warrants
    WarrantType_Bear = 4; //Put warrants
    WarrantType_InLine = 5; //Inline Warrants
}
```









**WarrantType**



``` protobuf
enum WarrantType
{
    WarrantType_Unknown = 0; //Unknown
    WarrantType_Buy = 1; //Long warrants
    WarrantType_Sell = 2; //Short warrants
    WarrantType_Bull = 3; //Call warrants
    WarrantType_Bear = 4; //Put warrants
    WarrantType_InLine = 5; //Inline Warrants
}
```









## <a href="#7268" class="header-anchor">#</a> Exchange Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **ExchType**

- `NONE`

  Unknown

- `HK_MAINBOARD`

  HKEx·Main Board

- `HK_GEMBOARD`

  HKEx·GEM

- `HK_HKEX`

  HKEx

- `US_NYSE`

  NYSE

- `US_NASDAQ`

  NASDAQ

- `US_PINK`

  OTC Mkt

- `US_AMEX`

  AMEX

- `US_OPTION`

  US

  

  
  

  

  
  
  

  Only applicable to US Options.

  

  

  

  

- `US_NYMEX`

  NYMEX

- `US_COMEX`

  COMEX

- `US_CBOT`

  CBOT

- `US_CME`

  CME

- `US_CBOE`

  CBOE

- `CN_SH`

  SH Stock Ex

- `CN_SZ`

  SZ Stock Ex

- `CN_STIB`

  STAR

- `SG_SGX`

  SGX

- `JP_OSE`

  OSE





**ExchType**



``` protobuf
enum ExchType
{
    ExchType_Unknown = 0; //Unknown
    ExchType_HK_MainBoard = 1; // HKEx·Main Board
    ExchType_HK_GEMBoard = 2; //HKEx·GEM
    ExchType_HK_HKEX = 3; //HKEx
    ExchType_US_NYSE = 4; //NYSE
    ExchType_US_Nasdaq = 5; //NASDAQ
    ExchType_US_Pink = 6; //OTC Mkt
    ExchType_US_AMEX = 7; //AMEX 
    ExchType_US_Option = 8; //US (Only applicable to US Options.)
    ExchType_US_NYMEX = 9; //NYMEX 
    ExchType_US_COMEX = 10; //COMEX
    ExchType_US_CBOT = 11; //CBOT
    ExchType_US_CME = 12; //CME
    ExchType_US_CBOE = 13; //CBOE
    ExchType_CN_SH = 14; //SH Stock Ex
    ExchType_CN_SZ = 15; //SZ Stock Ex
    ExchType_CN_STIB = 16; //STAR
    ExchType_SG_SGX = 17; //SGX
    ExchType_JP_OSE = 18; //OSE
};
```









**ExchType**



``` protobuf
enum ExchType
{
    ExchType_Unknown = 0; //Unknown
    ExchType_HK_MainBoard = 1; // HKEx·Main Board
    ExchType_HK_GEMBoard = 2; //HKEx·GEM
    ExchType_HK_HKEX = 3; //HKEx
    ExchType_US_NYSE = 4; //NYSE
    ExchType_US_Nasdaq = 5; //NASDAQ
    ExchType_US_Pink = 6; //OTC Mkt
    ExchType_US_AMEX = 7; //AMEX 
    ExchType_US_Option = 8; //US (Only applicable to US Options.)
    ExchType_US_NYMEX = 9; //NYMEX 
    ExchType_US_COMEX = 10; //COMEX
    ExchType_US_CBOT = 11; //CBOT
    ExchType_US_CME = 12; //CME
    ExchType_US_CBOE = 13; //CBOE
    ExchType_CN_SH = 14; //SH Stock Ex
    ExchType_CN_SZ = 15; //SZ Stock Ex
    ExchType_CN_STIB = 16; //STAR
    ExchType_SG_SGX = 17; //SGX
    ExchType_JP_OSE = 18; //OSE
};
```









**ExchType**



``` protobuf
enum ExchType
{
    ExchType_Unknown = 0; //Unknown
    ExchType_HK_MainBoard = 1; // HKEx·Main Board
    ExchType_HK_GEMBoard = 2; //HKEx·GEM
    ExchType_HK_HKEX = 3; //HKEx
    ExchType_US_NYSE = 4; //NYSE
    ExchType_US_Nasdaq = 5; //NASDAQ
    ExchType_US_Pink = 6; //OTC Mkt
    ExchType_US_AMEX = 7; //AMEX 
    ExchType_US_Option = 8; //US (Only applicable to US Options.)
    ExchType_US_NYMEX = 9; //NYMEX 
    ExchType_US_COMEX = 10; //COMEX
    ExchType_US_CBOT = 11; //CBOT
    ExchType_US_CME = 12; //CME
    ExchType_US_CBOE = 13; //CBOE
    ExchType_CN_SH = 14; //SH Stock Ex
    ExchType_CN_SZ = 15; //SZ Stock Ex
    ExchType_CN_STIB = 16; //STAR
    ExchType_SG_SGX = 17; //SGX
    ExchType_JP_OSE = 18; //OSE
};
```









**ExchType**



``` protobuf
enum ExchType
{
    ExchType_Unknown = 0; //Unknown
    ExchType_HK_MainBoard = 1; // HKEx·Main Board
    ExchType_HK_GEMBoard = 2; //HKEx·GEM
    ExchType_HK_HKEX = 3; //HKEx
    ExchType_US_NYSE = 4; //NYSE
    ExchType_US_Nasdaq = 5; //NASDAQ
    ExchType_US_Pink = 6; //OTC Mkt
    ExchType_US_AMEX = 7; //AMEX 
    ExchType_US_Option = 8; //US (Only applicable to US Options.)
    ExchType_US_NYMEX = 9; //NYMEX 
    ExchType_US_COMEX = 10; //COMEX
    ExchType_US_CBOT = 11; //CBOT
    ExchType_US_CME = 12; //CME
    ExchType_US_CBOE = 13; //CBOE
    ExchType_CN_SH = 14; //SH Stock Ex
    ExchType_CN_SZ = 15; //SZ Stock Ex
    ExchType_CN_STIB = 16; //STAR
    ExchType_SG_SGX = 17; //SGX
    ExchType_JP_OSE = 18; //OSE
};
```









**ExchType**



``` protobuf
enum ExchType
{
    ExchType_Unknown = 0; //Unknown
    ExchType_HK_MainBoard = 1; // HKEx·Main Board
    ExchType_HK_GEMBoard = 2; //HKEx·GEM
    ExchType_HK_HKEX = 3; //HKEx
    ExchType_US_NYSE = 4; //NYSE
    ExchType_US_Nasdaq = 5; //NASDAQ
    ExchType_US_Pink = 6; //OTC Mkt
    ExchType_US_AMEX = 7; //AMEX 
    ExchType_US_Option = 8; //US (Only applicable to US Options.)
    ExchType_US_NYMEX = 9; //NYMEX 
    ExchType_US_COMEX = 10; //COMEX
    ExchType_US_CBOT = 11; //CBOT
    ExchType_US_CME = 12; //CME
    ExchType_US_CBOE = 13; //CBOE
    ExchType_CN_SH = 14; //SH Stock Ex
    ExchType_CN_SZ = 15; //SZ Stock Ex
    ExchType_CN_STIB = 16; //STAR
    ExchType_SG_SGX = 17; //SGX
    ExchType_JP_OSE = 18; //OSE
};
```









## <a href="#5792" class="header-anchor">#</a> Security Identification

**Security**



``` protobuf
message Security
{
    required int32 market = 1; //QotMarket, quote market
    required string code = 2; //Code
}
```





## <a href="#500" class="header-anchor">#</a> Candlestick data

**KLine**



``` protobuf
message KLine
{
    required string time = 1; //String of timestamp (Format: yyyy-MM-dd HH:mm:ss)
    required bool isBlank = 2; //Whether it is a point with empty content, if it is true, only time information
    optional double highPrice = 3; //High
    optional double openPrice = 4; //Open
    optional double lowPrice = 5; //Low
    optional double closePrice = 6; //Close
    optional double lastClosePrice = 7; //Close yesterday
    optional int64 volume = 8; //Volume
    optional double turnover = 9; //Turnover
    optional double turnoverRate = 10; // Turnover rate (this field is in decimal form, so 0.2 is equivalent to 20%)
    optional double pe = 11; //P/E ratio
    optional double changeRate = 12; //Yield (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double timestamp = 13; //Timestamp
}
```





## <a href="#9569" class="header-anchor">#</a> Option Specific Fields of The Underlying Quote

**OptionBasicQotExData**



``` protobuf
message OptionBasicQotExData
{
    required double strikePrice = 1; //Strike price
    required int32 contractSize = 2; //Contract size (integer)
    optional double contractSizeFloat = 17; //Contract size (float)
    required int32 openInterest = 3; //Number of open positions
    required double impliedVolatility = 4; //Implied volatility (This field is in percentage form, so 20 is equivalent to 20%.)
    required double premium = 5; //Premium (This field is in percentage form, so 20 is equivalent to 20%.)
    required double delta = 6; //Greek value Delta
    required double gamma = 7; //Greek value Gamma
    required double vega = 8; //Greek value Vega
    required double theta = 9; //Greek value Theta
    required double rho = 10; //Greek value Rho
    optional int32 netOpenInterest = 11; //Net open contract number , only HK options support this field
    optional int32 expiryDateDistance = 12; //The number of days from the expiry date, a negative number means it has expired.
    optional double contractNominalValue = 13; //Contract nominal amount , only HK options support this field
    optional double ownerLotMultiplier = 14; //Equal number of underlying stocks, index options do not have this field , only HK options support this field  
    optional int32 optionAreaType = 15; //OptionAreaType, option type (by exercise time).
    optional double contractMultiplier = 16; //Contract multiplier
    optional int32 indexOptionType = 18; //Qot_Common.IndexOptionType, index option type
}    
```





## <a href="#8134" class="header-anchor">#</a> Futures Specific Fields of The Base Quote

**FutureBasicQotExData**



``` protobuf
message FutureBasicQotExData
{
    required double lastSettlePrice = 1; //Close yesterday
    required int32 position = 2; //Hold position
    required int32 positionChange = 3; //Daily change in position
    optional int32 expiryDateDistance = 4; //The number of days from the expiration date
}    
```





## <a href="#8930-2" class="header-anchor">#</a> Basic Quotation

**BasicQot**



``` protobuf
message BasicQot
{
    required Security security = 1; //Stock
    optional string name = 24; // stock name
    required bool isSuspended = 2; //whether trading is suspended
    required string listTime = 3; //listed date string (This field is deprecated. Format: yyyy-MM-dd)
    required double priceSpread = 4; //Spread
    required string updateTime = 5; //Update time string of the latest price (Format: yyyy-MM-dd HH:mm:ss), not applicable to other fields
    required double highPrice = 6; //High
    required double openPrice = 7; //Open
    required double lowPrice = 8; //low
    required double curPrice = 9; //The latest price
    required double lastClosePrice = 10; //Close yesterday
    required int64 volume = 11; //Volume
    required double turnover = 12; //Turnover
    required double turnoverRate = 13; //Turnover rate (This field is in percentage form, so 20 is equivalent to 20%.)
    required double amplitude = 14; //Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
    optional int32 darkStatus = 15; //Grey market trading status
    optional OptionBasicQotExData optionExData = 16; //Option specific field
    optional double listTimestamp = 17; //Time stamp of listing date (This field is deprecated.)
    optional double updateTimestamp = 18; //Update timestamp of the latest price, not applicable to other fields
    optional PreAfterMarketData preMarket = 19; //Pre-market data
    optional PreAfterMarketData afterMarket = 20; //After-hours data
    optional int32 secStatus = 21; //Security status
    optional FutureBasicQotExData futureExData = 22; //Futures specific field
}
```





## <a href="#9855" class="header-anchor">#</a> Before And After Data

**PreAfterMarketData**



``` protobuf
//US stocks support pre-market and after-hours data
//The Sci-tech Innovation Plate only supports after-hours data: trading volume, turnover
message PreAfterMarketData
{
    optional double price = 1; //Pre-market or after-hours## Price
    optional double highPrice = 2; //Pre-market or after-hours## High
    optional double lowPrice = 3; //Pre-market or after-hours## Low
    optional int64 volume = 4; //Pre-market or after-hours## Volume
    optional double turnover = 5; //Pre-market or after-hours## Turnover
    optional double changeVal = 6; //Pre-market or after-hours## Change in price
    optional double changeRate = 7; //Pre-market or after-hours## Yield (This field is in percentage form, so 20 is equivalent to 20%.)
    optional double amplitude = 8; //Pre-market or after-hours## Amplitude (This field is in percentage form, so 20 is equivalent to 20%.)
}
```





## <a href="#3690" class="header-anchor">#</a> Time Frame Data

**TimeShare**



``` protobuf
message TimeShare
{
    required string time = 1; //Time string (Format: yyyy-MM-dd HH:mm:ss)
    required int32 minute = 2; //Minutes after 0 o'clock
    required bool isBlank = 3; //Whether the content is empty, if true, it contents only time
    optional double price = 4; //Current price
    optional double lastClosePrice = 5; //Close yesterday
    optional double avgPrice = 6; //Average price
    optional int64 volume = 7; //Volume
    optional double turnover = 8; //Turnover
    optional double timestamp = 9; //Timestamp
}
```





## <a href="#1257" class="header-anchor">#</a> Basic Static Information of Securities

**SecurityStaticBasic**



``` protobuf

message SecurityStaticBasic
{
    required Qot_Common.Security security = 1; //Stock
    required int64 id = 2; //Stock ID
    required int32 lotSize = 3; //Lot size, the option type represents the number of shares in a contract
    required int32 secType = 4; //Qot_Common.SecurityType, stock type
    required string name = 5; //Stock name
    required string listTime = 6; //Listing time string (This field is deprecated. Format: yyyy-MM-dd)
    optional bool delisting = 7; //Delisted or not
    optional double listTimestamp = 8; //Listing timestamp (This field is deprecated.)
    optional int32 exchType = 9; //Qot_Common.ExchType, Exchange Type
}
```





## <a href="#4750" class="header-anchor">#</a> Warrant Additional Static Information

**WarrantStaticExData**



``` protobuf
message WarrantStaticExData
{
    required int32 type = 1; //Qot_Common.WarrantType, Warrant Type
    required Qot_Common.Security owner = 2; //The underlying stock
}   
```





## <a href="#1335" class="header-anchor">#</a> Option Additional Static Information

**OptionStaticExData**



``` protobuf
message OptionStaticExData
{
    required int32 type = 1; //Qot_Common.OptionType, option
    required Qot_Common.Security owner = 2; //Underlying stock
    required string strikeTime = 3; //Exercise date (Format: yyyy-MM-dd)
    required double strikePrice = 4; //Strike price
    required bool suspend = 5; //Suspended or not
    required string market = 6; //Issuance market name
    optional double strikeTimestamp = 7; //Exercise date timestamp
    optional int32 indexOptionType = 8; //Qot_Common.IndexOptionType, type of index option, only valid for index option
    optional int32 expirationCycle = 9; // Qot_Common.ExpirationCycle, type of option expiration cycle
    optional int32 optionStandardType = 10; // Qot_Common.OptionStandardType, type of option standard
    optional int32 optionSettlementMode = 11; // OptionSettlementMode, mode of option settlement
}   
```





## <a href="#9582" class="header-anchor">#</a> Additional Static Information About Futures

**FutureStaticExData**



``` protobuf
message FutureStaticExData
{
    required string lastTradeTime = 1; //The lastest trading day, only future non-main contracts have this field
    optional double lastTradeTimestamp = 2; //The lastest trading day timestamp, only future non-main contracts have this field
    required bool isMainContract = 3; //Futures main contract or not
}    
```





## <a href="#5588" class="header-anchor">#</a> Securities Static Information

**SecurityStaticInfo**



``` protobuf
message SecurityStaticInfo
{
    required SecurityStaticBasic basic = 1; //Basic security information
    optional WarrantStaticExData warrantExData = 2; //Additional information for warrants
    optional OptionStaticExData optionExData = 3; //Additional information for options
    optional FutureStaticExData futureExData = 4; //Additional information for futures
}
```





## <a href="#9607" class="header-anchor">#</a> Brokerage

**Broker**



``` protobuf
message Broker
{
    required int64 id = 1; //Broker ID
    required string name = 2; //Broker name
    required int32 pos = 3; //Broker position
  
    //The following fields are specific to SF quote
    optional int64 orderID = 4; //Exchange order ID, which is different from the order ID returned by the trading interface
    optional int64 volume = 5; //Number of shares in order
}
```





## <a href="#2975" class="header-anchor">#</a> Tick-by-Tick

**Ticker**



``` protobuf
message Ticker
{
    required string time = 1; //Time string (Format: yyyy-MM-dd HH:mm:ss)
    required int64 sequence = 2; //Unique identification
    required int32 dir = 3; //TickerDirection, buy or sell direction
    required double price = 4; //Price
    required int64 volume = 5; //Volume
    required double turnover = 6; // turnover
    optional double recvTime = 7; //Local timestamp of received push data, used to locate delay
    optional int32 type = 8; //TickerType, type by pen
    optional int32 typeSign = 9; //Pattern-by-stroke type sign
    optional int32 pushDataType = 10; //Used to distinguish push situations, this field is only available when pushing
    optional double timestamp = 11; //time stamp}
}
```





## <a href="#6220" class="header-anchor">#</a> Transaction File Details

**OrderBookDetail**



``` protobuf
message OrderBookDetail
{
    required int64 orderID = 1; //Exchange order ID, which is different from the order ID returned by the trading interface
    required int64 volume = 2; //Number of shares in order
}
```





## <a href="#3557" class="header-anchor">#</a> Order Book

**OrderBook**



``` protobuf
message OrderBook
{
    required double price = 1; //Order price
    required int64 volume = 2; //Order quantity
    required int32 orederCount = 3; //Number of commissioned orders
    repeated OrderBookDetail detailList = 4; //Order information, unique to HK SF, US LV2 market
}
```





## <a href="#7431" class="header-anchor">#</a> Changes in Holdings

**ShareHoldingChange**



``` protobuf
message ShareHoldingChange
{
    required string holderName = 1; //Holder name (institution name or fund name or executive name)
    required double holdingQty = 2; //Current number of holdings
    required double holdingRatio = 3; //Current shareholding percentage (This field is in percentage form, so 20 is equivalent to 20%.)
    required double changeQty = 4; //The number of changes from the previous time
    required double changeRatio = 5; //The percentage of change from the last time (This field is in percentage form, so 20 is equivalent to 20%.. It is the ratio relative to itself, not to total. For example, if the total share capital is 10,000 shares, holding 100 shares, the shareholding percentage is 1%, if 50 shares are sold, the change ratio is 50% instead of 0.5%)
    required string time = 6; //Release time (Format: yyyy-MM-dd HH:mm:ss)
    optional double timestamp = 7; //Timestamp
}
```





## <a href="#8622" class="header-anchor">#</a> Single Subscription Type Information

**SubInfo**



``` protobuf
message SubInfo
{
    required int32 subType = 1; //Qot_Common.SubType, subscription type
    repeated Qot_Common.Security securityList = 2; //Subscribe to securities of this type of market
}
```





## <a href="#3216" class="header-anchor">#</a> Single Connection Subscription Information

**ConnSubInfo**



``` protobuf
message ConnSubInfo
{
    repeated SubInfo subInfoList = 1; //The connection subscription information
    required int32 usedQuota = 2; //The subscription quota that the connection has used
    required bool isOwnConnData = 3; //Used to distinguish whether it is self-connected data
}
```





## <a href="#3203" class="header-anchor">#</a> Plate Information

**PlateInfo**



``` protobuf
message PlateInfo
{
    required Qot_Common.Security plate = 1; //Plate
    required string name = 2; //Plate name
    optional int32 plateType = 3; //Plate type, only 3207 (to get the plate to which the stock belongs) agreement returns this field
}
```





## <a href="#7728" class="header-anchor">#</a> Adjustment Information

**Rehab**



``` protobuf
message Rehab
{
    required string time = 1; //Time string (Format: yyyy-MM-dd)
    required int64 companyActFlag = 2; //CompanyAct combination flag bit, which specifies whether certain field values ​​are valid
    required double fwdFactorA = 3; //Adjustments factor A
    required double fwdFactorB = 4; //Adjustments factor B
    required double bwdFactorA = 5; //Adjustments factor A
    required double bwdFactorB = 6; //Adjustments factor B
    optional int32 splitBase = 7; //Stock split (for example, 1 split 5, Base is 1, Ert is 5)
    optional int32 splitErt = 8;
    optional int32 joinBase = 9; //Reverse stock split (for example, 50 in 1, Base is 50, Ert is 1)
    optional int32 joinErt = 10;
    optional int32 bonusBase = 11; //Bonus shares (for example, 10 free 3, Base is 10, Ert is 3)
    optional int32 bonusErt = 12;
    optional int32 transferBase = 13; //Transfer bonus shares (for example, 10 to 3, Base is 10, Ert is 3)
    optional int32 transferErt = 14;
    optional int32 allotBase = 15; //Allotment (for example, 10 get 2 free, allotment price is 6.3 yuan, Base is 10, Ert is 2, and Price is 6.3)
    optional int32 allotErt = 16;
    optional double allotPrice = 17;
    optional int32 addBase = 18; //Additional shares (for example, 10 get 2 free, additional issuance price is 6.3 yuan, Base is 10, Ert is 2, and Price is 6.3)
    optional int32 addErt = 19;
    optional double addPrice = 20;
    optional double dividend = 21; //Cash dividend (for example, if every 10 shares are paid out 0.5 yuan, the field value is 0.05)
    optional double spDividend = 22; //Special dividend (for example, if a special dividend is 0.5 yuan for every 10 shares, the value of this field is 0.05)
    optional double timestamp = 23; //Timestamp
}
```





> - For CompanyAct combination flag bit, refer to
>   [CompanyAct](/moomoo-api-doc/en/quote/quote.html#4631).

## <a href="#5181" class="header-anchor">#</a> Expiration Cycle





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **ExpirationCycle**

- `NONE`

  Unknown

- `WEEK`

  Weekly options

- `MONTH`

  Monthly options

- `END_OF_MONTH`

  End-Of-Monthly options

- `QUARTERLY`

  Quarterly options

- `WEEKMON`

  Monthly options-Monday

- `WEEKTUE`

  Monthly options-Tuesday

- `WEEKWED`

  Monthly options-Wednesday

- `WEEKTHU`

  Monthly options-Thursday

- `WEEKFRI`

  Monthly options-Friday





**ExpirationCycle**



``` protobuf
enum ExpirationCycle
{
    ExperationCycle_Unknow = 0; //Unknown
    ExperationCycle_Week = 1; //Weekly options
    ExperationCycle_Month = 2; //Monthly options
    ExpirationCycle_MonthEnd = 3;  // End-Of-Monthly options
    ExpirationCycle_Quarter = 4; //Quarterly options
    ExpirationCycle_WeekMon = 11; //Monthly options-Monday
    ExpirationCycle_WeekTue = 12; //Monthly options-Tuesday
    ExpirationCycle_WeekWed = 13; //Monthly options-Wednesday
    ExpirationCycle_WeekThu = 14; //Monthly options-Thursday
    ExpirationCycle_WeekFri = 15; //Monthly options-Friday
}
```









**ExpirationCycle**



``` protobuf
enum ExpirationCycle
{
    ExperationCycle_Unknow = 0; //Unknown
    ExperationCycle_Week = 1; //Weekly options
    ExperationCycle_Month = 2; //Monthly options
    ExpirationCycle_MonthEnd = 3;  // End-Of-Monthly options
    ExpirationCycle_Quarter = 4; //Quarterly options
    ExpirationCycle_WeekMon = 11; //Monthly options-Monday
    ExpirationCycle_WeekTue = 12; //Monthly options-Tuesday
    ExpirationCycle_WeekWed = 13; //Monthly options-Wednesday
    ExpirationCycle_WeekThu = 14; //Monthly options-Thursday
    ExpirationCycle_WeekFri = 15; //Monthly options-Friday
}
```









**ExpirationCycle**



``` protobuf
enum ExpirationCycle
{
    ExperationCycle_Unknow = 0; //Unknown
    ExperationCycle_Week = 1; //Weekly options
    ExperationCycle_Month = 2; //Monthly options
    ExpirationCycle_MonthEnd = 3;  // End-Of-Monthly options
    ExpirationCycle_Quarter = 4; //Quarterly options
    ExpirationCycle_WeekMon = 11; //Monthly options-Monday
    ExpirationCycle_WeekTue = 12; //Monthly options-Tuesday
    ExpirationCycle_WeekWed = 13; //Monthly options-Wednesday
    ExpirationCycle_WeekThu = 14; //Monthly options-Thursday
    ExpirationCycle_WeekFri = 15; //Monthly options-Friday
}
```









**ExpirationCycle**



``` protobuf
enum ExpirationCycle
{
    ExperationCycle_Unknow = 0; //Unknown
    ExperationCycle_Week = 1; //Weekly options
    ExperationCycle_Month = 2; //Monthly options
    ExpirationCycle_MonthEnd = 3;  // End-Of-Monthly options
    ExpirationCycle_Quarter = 4; //Quarterly options
    ExpirationCycle_WeekMon = 11; //Monthly options-Monday
    ExpirationCycle_WeekTue = 12; //Monthly options-Tuesday
    ExpirationCycle_WeekWed = 13; //Monthly options-Wednesday
    ExpirationCycle_WeekThu = 14; //Monthly options-Thursday
    ExpirationCycle_WeekFri = 15; //Monthly options-Friday
}
```









**ExpirationCycle**



``` protobuf
enum ExpirationCycle
{
    ExperationCycle_Unknow = 0; //Unknown
    ExperationCycle_Week = 1; //Weekly options
    ExperationCycle_Month = 2; //Monthly options
    ExpirationCycle_MonthEnd = 3;  // End-Of-Monthly options
    ExpirationCycle_Quarter = 4; //Quarterly options
    ExpirationCycle_WeekMon = 11; //Monthly options-Monday
    ExpirationCycle_WeekTue = 12; //Monthly options-Tuesday
    ExpirationCycle_WeekWed = 13; //Monthly options-Wednesday
    ExpirationCycle_WeekThu = 14; //Monthly options-Thursday
    ExpirationCycle_WeekFri = 15; //Monthly options-Friday
}
```









## <a href="#8553" class="header-anchor">#</a> Option Standard Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OptionStandardType**

- `NONE`

  Unknown

- `STANDARD`

  standard options

- `NON_STANDARD`

  non-standard options





**OptionStandardType**



``` protobuf
enum OptionStandardType
{
    OptionStandardType_Unknown = 0; //Unknown
    OptionStandardType_Standard = 1; // standard options
    OptionStandardType_NonStandard = 2; // non-standard options
}
```









**OptionStandardType**



``` protobuf
enum OptionStandardType
{
    OptionStandardType_Unknown = 0; //Unknown
    OptionStandardType_Standard = 1; // standard options
    OptionStandardType_NonStandard = 2; // non-standard options
}
```









**OptionStandardType**



``` protobuf
enum OptionStandardType
{
    OptionStandardType_Unknown = 0; //Unknown
    OptionStandardType_Standard = 1; // standard options
    OptionStandardType_NonStandard = 2; // non-standard options
}
```









**OptionStandardType**



``` protobuf
enum OptionStandardType
{
    OptionStandardType_Unknown = 0; //Unknown
    OptionStandardType_Standard = 1; // standard options
    OptionStandardType_NonStandard = 2; // non-standard options
}
```









**OptionStandardType**



``` protobuf
enum OptionStandardType
{
    OptionStandardType_Unknown = 0; //Unknown
    OptionStandardType_Standard = 1; // standard options
    OptionStandardType_NonStandard = 2; // non-standard options
}
```









## <a href="#6656" class="header-anchor">#</a> Option Settlement Mode





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OptionSettlementMode**

- `NONE`

  Unknown

- `AM`

  Asian Pricing

- `PM`

  Path-Dependent





**OptionSettlementMode**



``` protobuf
enum OptionSettlementMode
{
    OptionSettlementMode_Unknown = 0; //Unknown
    OptionSettlementMode_AM = 1; // AM
    OptionSettlementMode_PM = 2; // PM
}
```









**OptionSettlementMode**



``` protobuf
enum OptionSettlementMode
{
    OptionSettlementMode_Unknown = 0; //Unknown
    OptionSettlementMode_AM = 1; // AM
    OptionSettlementMode_PM = 2; // PM
}
```









**OptionSettlementMode**



``` protobuf
enum OptionSettlementMode
{
    OptionSettlementMode_Unknown = 0; //Unknown
    OptionSettlementMode_AM = 1; // AM
    OptionSettlementMode_PM = 2; // PM
}
```









**OptionSettlementMode**



``` protobuf
enum OptionSettlementMode
{
    OptionSettlementMode_Unknown = 0; //Unknown
    OptionSettlementMode_AM = 1; // AM
    OptionSettlementMode_PM = 2; // PM
}
```









**OptionSettlementMode**



``` protobuf
enum OptionSettlementMode
{
    OptionSettlementMode_Unknown = 0; //Unknown
    OptionSettlementMode_AM = 1; // AM
    OptionSettlementMode_PM = 2; // PM
}
```









\## Stockholder (Deprecated)

## <a href="#9472" class="header-anchor">#</a> Stock Holder





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **StockHolder**

- `NONE`

  Unknown

- `INSTITUTE`

  Institute

- `FUND`

  Fund

- `EXECUTIVE`

  Executives





**HolderCategory**



``` protobuf
enum HolderCategory
{
    HolderCategory_Unknow = 0; //Unknown
    HolderCategory_Agency = 1; //Institute
    HolderCategory_Fund = 2; //Fund
    HolderCategory_SeniorManager = 3; //Executives
}
```









**HolderCategory**



``` protobuf
enum HolderCategory
{
    HolderCategory_Unknow = 0; //Unknown
    HolderCategory_Agency = 1; //Institute
    HolderCategory_Fund = 2; //Fund
    HolderCategory_SeniorManager = 3; //Executives
}
```









**HolderCategory**



``` protobuf
enum HolderCategory
{
    HolderCategory_Unknow = 0; //Unknown
    HolderCategory_Agency = 1; //Institute
    HolderCategory_Fund = 2; //Fund
    HolderCategory_SeniorManager = 3; //Executives
}
```









**HolderCategory**



``` protobuf
enum HolderCategory
{
    HolderCategory_Unknow = 0; //Unknown
    HolderCategory_Agency = 1; //Institute
    HolderCategory_Fund = 2; //Fund
    HolderCategory_SeniorManager = 3; //Executives
}
```









**HolderCategory**



``` protobuf
enum HolderCategory
{
    HolderCategory_Unknow = 0; //Unknown
    HolderCategory_Agency = 1; //Institute
    HolderCategory_Fund = 2; //Fund
    HolderCategory_SeniorManager = 3; //Executives
}
```















