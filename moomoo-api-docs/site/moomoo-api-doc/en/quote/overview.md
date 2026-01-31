



# <a href="#6105" class="header-anchor">#</a> Overview





- Python
- C#
- Java
- C++
- JavaScript
- 裸协议





<table>
<thead>
<tr>
<th colspan="2">Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="17">Real-time Data</td>
<td rowspan="4">Subscription</td>
<td><a href="./sub.html#5009">subscribe</a></td>
<td>Subscribe real-time market data</td>
</tr>
<tr>
<td><a href="./sub.html#1052">unsubscribe</a></td>
<td>Unsubscribe subscriptions</td>
</tr>
<tr>
<td><a href="./sub.html#771">unsubscribe_all</a></td>
<td>Unsubscribe all subscriptions</td>
</tr>
<tr>
<td><a href="./query-subscription.html">query_subscription</a></td>
<td>Get subscription information</td>
</tr>
<tr>
<td rowspan="6">Push and Callback</td>
<td><a href="./update-stock-quote.html">StockQuoteHandlerBase</a></td>
<td>Real-time quote callback</td>
</tr>
<tr>
<td><a href="./update-order-book.html">OrderBookHandlerBase</a></td>
<td>Real-time order book callback</td>
</tr>
<tr>
<td><a href="./update-kl.html">CurKlineHandlerBase</a></td>
<td>Real-time candlestick callback</td>
</tr>
<tr>
<td><a href="./update-ticker.html">TickerHandlerBase</a></td>
<td>Real-time tick-by-tick callback</td>
</tr>
<tr>
<td><a href="./update-rt.html">RTDataHandlerBase</a></td>
<td>Real-time time frame callback</td>
</tr>
<tr>
<td><a href="./update-broker.html">BrokerHandlerBase</a></td>
<td>Real-time broker queue callback</td>
</tr>
<tr>
<td rowspan="7">Get</td>
<td><a href="./get-market-snapshot.html">get_market_snapshot</a></td>
<td>Get market snapshot</td>
</tr>
<tr>
<td><a href="./get-stock-quote.html">get_stock_quote</a></td>
<td>Get real-time quote</td>
</tr>
<tr>
<td><a href="./get-order-book.html">get_order_book</a></td>
<td>Get real-time order book</td>
</tr>
<tr>
<td><a href="./get-kl.html">get_cur_kline</a></td>
<td>Get real-time candlestick</td>
</tr>
<tr>
<td><a href="./get-rt.html">get_rt_data</a></td>
<td>Get real-time time frame data</td>
</tr>
<tr>
<td><a href="./get-ticker.html">get_rt_ticker</a></td>
<td>Get real-time tick-by-tick</td>
</tr>
<tr>
<td><a href="./get-broker.html">get_broker_queue</a></td>
<td>Get real-time broker queue</td>
</tr>
<tr>
<td colspan="2" rowspan="6">Basic Data</td>
<td><a href="./get-market-state.html">get_market_state</a></td>
<td>Get market status of securities</td>
</tr>
<tr>
<td><a href="./get-capital-flow.html">get_capital_flow</a></td>
<td>Get capital flow</td>
</tr>
<tr>
<td><a
href="./get-capital-distribution.html">get_capital_distribution</a></td>
<td>Get capital distribution</td>
</tr>
<tr>
<td><a href="./get-owner-plate.html">get_owner_plate</a></td>
<td>Get the stock ownership plate</td>
</tr>
<tr>
<td><a
href="./request-history-kline.html">request_history_kline</a></td>
<td>Get historical candlesticks</td>
</tr>
<tr>
<td><a href="./get-rehab.html">get_rehab</a></td>
<td>Get the stock adjustment factor</td>
</tr>
<tr>
<td colspan="2" rowspan="5">Related Derivatives</td>
<td><a
href="../quote/get-option-expiration-date.html">get_option_expiration_date</a></td>
<td>Query all expiration dates of option chains through the underlying
stock.</td>
</tr>
<tr>
<td><a href="./get-option-chain.html">get_option_chain</a></td>
<td>Get the option chain from an underlying stock</td>
</tr>
<tr>
<td><a href="./get-warrant.html">get_warrant</a></td>
<td>Get filtered warrant (for HK market only)</td>
</tr>
<tr>
<td><a
href="./get-referencestock-list.html">get_referencestock_list</a></td>
<td>Get related data of securities</td>
</tr>
<tr>
<td><a href="./get-future-info.html">get_future_info</a></td>
<td>Get futures contract information</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Market Filter</td>
<td><a href="./get-stock-filter.html">get_stock_filter</a></td>
<td>Filter stocks by condition</td>
</tr>
<tr>
<td><a href="./get-plate-stock.html">get_plate_stock</a></td>
<td>Get the list of stocks in the plate</td>
</tr>
<tr>
<td><a href="./get-plate-list.html">get_plate_list</a></td>
<td>Get plate list</td>
</tr>
<tr>
<td><a href="./get-static-info.html">get_stock_basicinfo</a></td>
<td>Get stock basic information</td>
</tr>
<tr>
<td><a href="./get-ipo-list.html">get_ipo_list</a></td>
<td>Get IPO information of a specific market</td>
</tr>
<tr>
<td><a href="./get-global-state.html">get_global_state</a></td>
<td>Get global status</td>
</tr>
<tr>
<td><a href="./request-trading-days.html">request_trading_days</a></td>
<td>Get trading calendar</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Customization</td>
<td><a href="./get-history-kl-quota.html">get_history_kl_quota</a></td>
<td>Get usage details of historical candlestick quota</td>
</tr>
<tr>
<td><a href="./set-price-reminder.html">set_price_reminder</a></td>
<td>Add, delete, modify, enable, and disable price reminders for
specified stocks</td>
</tr>
<tr>
<td><a href="./get-price-reminder.html">get_price_reminder</a></td>
<td>Get a list of price reminders set for the specified stock or
market</td>
</tr>
<tr>
<td><a
href="./get-user-security-group.html">get_user_security_group</a></td>
<td>Get a list of groups from the user watchlist</td>
</tr>
<tr>
<td><a href="./get-user-security.html">get_user_security</a></td>
<td>Get a list of a specified group from watchlist</td>
</tr>
<tr>
<td><a href="./modify-user-security.html">modify_user_security</a></td>
<td>Modify the specific group from the watchlist</td>
</tr>
<tr>
<td><a
href="./update-price-reminder.html">PriceReminderHandlerBase</a></td>
<td>The price reminder notification callback</td>
</tr>
</tbody>
</table>





<table>
<thead>
<tr>
<th colspan="2">Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="15">Real-time Data</td>
<td rowspan="2">Subscription</td>
<td><a href="./sub.html">Sub</a></td>
<td>Subscribe or unsubscribe real-time market data</td>
</tr>
<tr>
<td><a href="./query-subscription.html">GetSubInfo</a></td>
<td>Get subscription information</td>
</tr>
<tr>
<td rowspan="6">Push and Callback</td>
<td><a href="./update-stock-quote.html">UpdateBasicQot</a></td>
<td>Real-time quote callback</td>
</tr>
<tr>
<td><a href="./update-order-book.html">UpdateOrderBook</a></td>
<td>Real-time order book callback</td>
</tr>
<tr>
<td><a href="./update-kl.html">UpdateKL</a></td>
<td>Real-time candlestick callback</td>
</tr>
<tr>
<td><a href="./update-ticker.html">UpdateTicker</a></td>
<td>Real-time tick-by-tick callback</td>
</tr>
<tr>
<td><a href="./update-rt.html">UpdateRT</a></td>
<td>Real-time time frame callback</td>
</tr>
<tr>
<td><a href="./update-broker.html">UpdateBroker</a></td>
<td>Real-time broker queue callback</td>
</tr>
<tr>
<td rowspan="7">Get</td>
<td><a href="./get-market-snapshot.html">GetSecuritySnapshot</a></td>
<td>Get market snapshot</td>
</tr>
<tr>
<td><a href="./get-stock-quote.html">GetBasicQot</a></td>
<td>Get real-time quote</td>
</tr>
<tr>
<td><a href="./get-order-book.html">GetOrderBook</a></td>
<td>Get real-time order book</td>
</tr>
<tr>
<td><a href="./get-kl.html">GetKL</a></td>
<td>Get real-time candlestick</td>
</tr>
<tr>
<td><a href="./get-rt.html">GetRT</a></td>
<td>Get real-time time frame data</td>
</tr>
<tr>
<td><a href="./get-ticker.html">GetTicker</a></td>
<td>Get real-time tick-by-tick</td>
</tr>
<tr>
<td><a href="./get-broker.html">GetBroker</a></td>
<td>Get real-time broker queue</td>
</tr>
<tr>
<td colspan="2" rowspan="6">Basic Data</td>
<td><a href="./get-market-state.html">GetMarketState</a></td>
<td>Get market status of securities</td>
</tr>
<tr>
<td><a href="./get-capital-flow.html">GetCapitalFlow</a></td>
<td>Get capital flow</td>
</tr>
<tr>
<td><a
href="./get-capital-distribution.html">GetCapitalDistribution</a></td>
<td>Get capital distribution</td>
</tr>
<tr>
<td><a href="./get-owner-plate.html">GetOwnerPlate</a></td>
<td>Get the stock ownership plate</td>
</tr>
<tr>
<td><a href="./request-history-kline.html">RequestHistoryKL</a></td>
<td>Get historical candlesticks</td>
</tr>
<tr>
<td><a href="./get-rehab.html">RequestRehab</a></td>
<td>Get the stock adjustment factor</td>
</tr>
<tr>
<td colspan="2" rowspan="5">Related Derivatives</td>
<td><a
href="./get-option-expiration-date.html">GetOptionExpirationDate</a></td>
<td>Query all expiration dates of option chains through the underlying
stock.</td>
</tr>
<tr>
<td><a href="./get-option-chain.html">GetOptionChain</a></td>
<td>Get the option chain from an underlying stock</td>
</tr>
<tr>
<td><a href="./get-warrant.html">GetWarrant</a></td>
<td>Get filtered warrant (for HK market only)</td>
</tr>
<tr>
<td><a href="./get-referencestock-list.html">GetReference</a></td>
<td>Get related data of securities</td>
</tr>
<tr>
<td><a href="./get-future-info.html">GetFutureInfo</a></td>
<td>Get futures contract information</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Market Filter</td>
<td><a href="./get-stock-filter.html">StockFilter</a></td>
<td>Filter stocks by condition</td>
</tr>
<tr>
<td><a href="./get-plate-stock.html">GetPlateSecurity</a></td>
<td>Get the list of stocks in the plate</td>
</tr>
<tr>
<td><a href="./get-plate-list.html">GetPlateSet</a></td>
<td>Get plate list</td>
</tr>
<tr>
<td><a href="./get-static-info.html">GetStaticInfo</a></td>
<td>Get stock basic information</td>
</tr>
<tr>
<td><a href="./get-ipo-list.html">GetIpoList</a></td>
<td>Get IPO information of a specific market</td>
</tr>
<tr>
<td><a href="./get-global-state.html">GetGlobalState</a></td>
<td>Get global status</td>
</tr>
<tr>
<td><a href="./request-trading-days.html">RequestTradeDate</a></td>
<td>Get trading calendar</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Customization</td>
<td><a href="./get-history-kl-quota.html">RequestHistoryKLQuota</a></td>
<td>Get usage details of historical candlestick quota</td>
</tr>
<tr>
<td><a href="./set-price-reminder.html">SetPriceReminder</a></td>
<td>Add, delete, modify, enable, and disable price reminders for
specified stocks</td>
</tr>
<tr>
<td><a href="./get-price-reminder.html">GetPriceReminder</a></td>
<td>Get a list of price reminders set for the specified stock or
market</td>
</tr>
<tr>
<td><a
href="./get-user-security-group.html">GetUserSecurityGroup</a></td>
<td>Get a list of groups from the user watchlist</td>
</tr>
<tr>
<td><a href="./get-user-security.html">GetUserSecurity</a></td>
<td>Get a list of a specified group from watchlist</td>
</tr>
<tr>
<td><a href="./modify-user-security.html">ModifyUserSecurity</a></td>
<td>Modify the specific group from the watchlist</td>
</tr>
<tr>
<td><a href="./update-price-reminder.html">UpdatePriceReminder</a></td>
<td>The price reminder notification callback</td>
</tr>
</tbody>
</table>





<table>
<thead>
<tr>
<th colspan="2">Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="15">Real-time Data</td>
<td rowspan="2">Subscription</td>
<td><a href="./sub.html">sub</a></td>
<td>Subscribe or unsubscribe real-time market data</td>
</tr>
<tr>
<td><a href="./query-subscription.html">getSubInfo</a></td>
<td>Get subscription information</td>
</tr>
<tr>
<td rowspan="6">Push and Callback</td>
<td><a href="./update-stock-quote.html">updateBasicQot</a></td>
<td>Real-time quote callback</td>
</tr>
<tr>
<td><a href="./update-order-book.html">updateOrderBook</a></td>
<td>Real-time order book callback</td>
</tr>
<tr>
<td><a href="./update-kl.html">updateKL</a></td>
<td>Real-time candlestick callback</td>
</tr>
<tr>
<td><a href="./update-ticker.html">updateTicker</a></td>
<td>Real-time tick-by-tick callback</td>
</tr>
<tr>
<td><a href="./update-rt.html">updateRT</a></td>
<td>Real-time time frame callback</td>
</tr>
<tr>
<td><a href="./update-broker.html">updateBroker</a></td>
<td>Real-time broker queue callback</td>
</tr>
<tr>
<td rowspan="7">Get</td>
<td><a href="./get-market-snapshot.html">getSecuritySnapshot</a></td>
<td>Get market snapshot</td>
</tr>
<tr>
<td><a href="./get-stock-quote.html">getBasicQot</a></td>
<td>Get real-time quote</td>
</tr>
<tr>
<td><a href="./get-order-book.html">getOrderBook</a></td>
<td>Get real-time order book</td>
</tr>
<tr>
<td><a href="./get-kl.html">getKL</a></td>
<td>Get real-time candlestick</td>
</tr>
<tr>
<td><a href="./get-rt.html">getRT</a></td>
<td>Get real-time time frame data</td>
</tr>
<tr>
<td><a href="./get-ticker.html">getTicker</a></td>
<td>Get real-time tick-by-tick</td>
</tr>
<tr>
<td><a href="./get-broker.html">getBroker</a></td>
<td>Get real-time broker queue</td>
</tr>
<tr>
<td colspan="2" rowspan="6">Basic Data</td>
<td><a href="./get-market-state.html">getMarketState</a></td>
<td>Get market status of securities</td>
</tr>
<tr>
<td><a href="./get-capital-flow.html">getCapitalFlow</a></td>
<td>Get capital flow</td>
</tr>
<tr>
<td><a
href="./get-capital-distribution.html">getCapitalDistribution</a></td>
<td>Get capital distribution</td>
</tr>
<tr>
<td><a href="./get-owner-plate.html">getOwnerPlate</a></td>
<td>Get the stock ownership plate</td>
</tr>
<tr>
<td><a href="./request-history-kline.html">requestHistoryKL</a></td>
<td>Get historical candlesticks</td>
</tr>
<tr>
<td><a href="./get-rehab.html">requestRehab</a></td>
<td>Get the stock adjustment factor</td>
</tr>
<tr>
<td colspan="2" rowspan="5">Related Derivatives</td>
<td><a
href="./get-option-expiration-date.html">getOptionExpirationDate</a></td>
<td>Query all expiration dates of option chains through the underlying
stock.</td>
</tr>
<tr>
<td><a href="./get-option-chain.html">getOptionChain</a></td>
<td>Get the option chain from an underlying stock</td>
</tr>
<tr>
<td><a href="./get-warrant.html">getWarrant</a></td>
<td>Get filtered warrant (for HK market only)</td>
</tr>
<tr>
<td><a href="./get-referencestock-list.html">getReference</a></td>
<td>Get related data of securities</td>
</tr>
<tr>
<td><a href="./get-future-info.html">getFutureInfo</a></td>
<td>Get futures contract information</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Market Filter</td>
<td><a href="./get-stock-filter.html">stockFilter</a></td>
<td>Filter stocks by condition</td>
</tr>
<tr>
<td><a href="./get-plate-stock.html">getPlateSecurity</a></td>
<td>Get the list of stocks in the plate</td>
</tr>
<tr>
<td><a href="./get-plate-list.html">getPlateSet</a></td>
<td>Get plate list</td>
</tr>
<tr>
<td><a href="./get-static-info.html">getStaticInfo</a></td>
<td>Get stock basic information</td>
</tr>
<tr>
<td><a href="./get-ipo-list.html">getIpoList</a></td>
<td>Get IPO information of a specific market</td>
</tr>
<tr>
<td><a href="./get-global-state.html">getGlobalState</a></td>
<td>Get global status</td>
</tr>
<tr>
<td><a href="./request-trading-days.html">requestTradeDate</a></td>
<td>Get trading calendar</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Customization</td>
<td><a href="./get-history-kl-quota.html">requestHistoryKLQuota</a></td>
<td>Get usage details of historical candlestick quota</td>
</tr>
<tr>
<td><a href="./set-price-reminder.html">setPriceReminder</a></td>
<td>Add, delete, modify, enable, and disable price reminders for
specified stocks</td>
</tr>
<tr>
<td><a href="./get-price-reminder.html">getPriceReminder</a></td>
<td>Get a list of price reminders set for the specified stock or
market</td>
</tr>
<tr>
<td><a
href="./get-user-security-group.html">getUserSecurityGroup</a></td>
<td>Get a list of groups from the user watchlist</td>
</tr>
<tr>
<td><a href="./get-user-security.html">getUserSecurity</a></td>
<td>Get a list of a specified group from watchlist</td>
</tr>
<tr>
<td><a href="./modify-user-security.html">modifyUserSecurity</a></td>
<td>Modify the specific group from the watchlist</td>
</tr>
<tr>
<td><a href="./update-price-reminder.html">updatePriceReminder</a></td>
<td>The price reminder notification callback</td>
</tr>
</tbody>
</table>





<table>
<thead>
<tr>
<th colspan="2">Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="15">Real-time Data</td>
<td rowspan="2">Subscription</td>
<td><a href="./sub.html">Sub</a></td>
<td>Subscribe or unsubscribe real-time market data</td>
</tr>
<tr>
<td><a href="./query-subscription.html">GetSubInfo</a></td>
<td>Get subscription information</td>
</tr>
<tr>
<td rowspan="6">Push and Callback</td>
<td><a href="./update-stock-quote.html">UpdateBasicQot</a></td>
<td>Real-time quote callback</td>
</tr>
<tr>
<td><a href="./update-order-book.html">UpdateOrderBook</a></td>
<td>Real-time order book callback</td>
</tr>
<tr>
<td><a href="./update-kl.html">UpdateKL</a></td>
<td>Real-time candlestick callback</td>
</tr>
<tr>
<td><a href="./update-ticker.html">UpdateTicker</a></td>
<td>Real-time tick-by-tick callback</td>
</tr>
<tr>
<td><a href="./update-rt.html">UpdateRT</a></td>
<td>Real-time time frame callback</td>
</tr>
<tr>
<td><a href="./update-broker.html">UpdateBroker</a></td>
<td>Real-time broker queue callback</td>
</tr>
<tr>
<td rowspan="7">Get</td>
<td><a href="./get-market-snapshot.html">GetSecuritySnapshot</a></td>
<td>Get market snapshot</td>
</tr>
<tr>
<td><a href="./get-stock-quote.html">GetBasicQot</a></td>
<td>Get real-time quote</td>
</tr>
<tr>
<td><a href="./get-order-book.html">GetOrderBook</a></td>
<td>Get real-time order book</td>
</tr>
<tr>
<td><a href="./get-kl.html">GetKL</a></td>
<td>Get real-time candlestick</td>
</tr>
<tr>
<td><a href="./get-rt.html">GetRT</a></td>
<td>Get real-time time frame data</td>
</tr>
<tr>
<td><a href="./get-ticker.html">GetTicker</a></td>
<td>Get real-time tick-by-tick</td>
</tr>
<tr>
<td><a href="./get-broker.html">GetBroker</a></td>
<td>Get real-time broker queue</td>
</tr>
<tr>
<td colspan="2" rowspan="6">Basic Data</td>
<td><a href="./get-market-state.html">GetMarketState</a></td>
<td>Get market status of securities</td>
</tr>
<tr>
<td><a href="./get-capital-flow.html">GetCapitalFlow</a></td>
<td>Get capital flow</td>
</tr>
<tr>
<td><a
href="./get-capital-distribution.html">GetCapitalDistribution</a></td>
<td>Get capital distribution</td>
</tr>
<tr>
<td><a href="./get-owner-plate.html">GetOwnerPlate</a></td>
<td>Get the stock ownership plate</td>
</tr>
<tr>
<td><a href="./request-history-kline.html">RequestHistoryKL</a></td>
<td>Get historical candlesticks</td>
</tr>
<tr>
<td><a href="./get-rehab.html">RequestRehab</a></td>
<td>Get the stock adjustment factor</td>
</tr>
<tr>
<td colspan="2" rowspan="5">Related Derivatives</td>
<td><a
href="./get-option-expiration-date.html">GetOptionExpirationDate</a></td>
<td>Query all expiration dates of option chains through the underlying
stock.</td>
</tr>
<tr>
<td><a href="./get-option-chain.html">GetOptionChain</a></td>
<td>Get the option chain from an underlying stock</td>
</tr>
<tr>
<td><a href="./get-warrant.html">GetWarrant</a></td>
<td>Get filtered warrant (for HK market only)</td>
</tr>
<tr>
<td><a href="./get-referencestock-list.html">GetReference</a></td>
<td>Get related data of securities</td>
</tr>
<tr>
<td><a href="./get-future-info.html">GetFutureInfo</a></td>
<td>Get futures contract information</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Market Filter</td>
<td><a href="./get-stock-filter.html">StockFilter</a></td>
<td>Filter stocks by condition</td>
</tr>
<tr>
<td><a href="./get-plate-stock.html">GetPlateSecurity</a></td>
<td>Get the list of stocks in the plate</td>
</tr>
<tr>
<td><a href="./get-plate-list.html">GetPlateSet</a></td>
<td>Get plate list</td>
</tr>
<tr>
<td><a href="./get-static-info.html">GetStaticInfo</a></td>
<td>Get stock basic information</td>
</tr>
<tr>
<td><a href="./get-ipo-list.html">GetIpoList</a></td>
<td>Get IPO information of a specific market</td>
</tr>
<tr>
<td><a href="./get-global-state.html">GetGlobalState</a></td>
<td>Get global status</td>
</tr>
<tr>
<td><a href="./request-trading-days.html">RequestTradeDate</a></td>
<td>Get trading calendar</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Customization</td>
<td><a href="./get-history-kl-quota.html">RequestHistoryKLQuota</a></td>
<td>Get usage details of historical candlestick quota</td>
</tr>
<tr>
<td><a href="./set-price-reminder.html">SetPriceReminder</a></td>
<td>Add, delete, modify, enable, and disable price reminders for
specified stocks</td>
</tr>
<tr>
<td><a href="./get-price-reminder.html">GetPriceReminder</a></td>
<td>Get a list of price reminders set for the specified stock or
market</td>
</tr>
<tr>
<td><a
href="./get-user-security-group.html">GetUserSecurityGroup</a></td>
<td>Get a list of groups from the user watchlist</td>
</tr>
<tr>
<td><a href="./get-user-security.html">GetUserSecurity</a></td>
<td>Get a list of a specified group from watchlist</td>
</tr>
<tr>
<td><a href="./modify-user-security.html">ModifyUserSecurity</a></td>
<td>Modify the specific group from the watchlist</td>
</tr>
<tr>
<td><a href="./update-price-reminder.html">UpdatePriceReminder</a></td>
<td>The price reminder notification callback</td>
</tr>
</tbody>
</table>





<table>
<thead>
<tr>
<th colspan="2">Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="15">Real-time Data</td>
<td rowspan="2">Subscription</td>
<td><a href="./sub.html">Sub</a></td>
<td>Subscribe or unsubscribe real-time market data</td>
</tr>
<tr>
<td><a href="./query-subscription.html">GetSubInfo</a></td>
<td>Get subscription information</td>
</tr>
<tr>
<td rowspan="6">Push and Callback</td>
<td><a href="./update-stock-quote.html">UpdateBasicQot</a></td>
<td>Real-time quote callback</td>
</tr>
<tr>
<td><a href="./update-order-book.html">UpdateOrderBook</a></td>
<td>Real-time order book callback</td>
</tr>
<tr>
<td><a href="./update-kl.html">UpdateKL</a></td>
<td>Real-time candlestick callback</td>
</tr>
<tr>
<td><a href="./update-ticker.html">UpdateTicker</a></td>
<td>Real-time tick-by-tick callback</td>
</tr>
<tr>
<td><a href="./update-rt.html">UpdateRT</a></td>
<td>Real-time time frame callback</td>
</tr>
<tr>
<td><a href="./update-broker.html">UpdateBroker</a></td>
<td>Real-time broker queue callback</td>
</tr>
<tr>
<td rowspan="7">Get</td>
<td><a href="./get-market-snapshot.html">GetSecuritySnapshot</a></td>
<td>Get market snapshot</td>
</tr>
<tr>
<td><a href="./get-stock-quote.html">GetBasicQot</a></td>
<td>Get real-time quote</td>
</tr>
<tr>
<td><a href="./get-order-book.html">GetOrderBook</a></td>
<td>Get real-time order book</td>
</tr>
<tr>
<td><a href="./get-kl.html">GetKL</a></td>
<td>Get real-time candlestick</td>
</tr>
<tr>
<td><a href="./get-rt.html">GetRT</a></td>
<td>Get real-time time frame data</td>
</tr>
<tr>
<td><a href="./get-ticker.html">GetTicker</a></td>
<td>Get real-time tick-by-tick</td>
</tr>
<tr>
<td><a href="./get-broker.html">GetBroker</a></td>
<td>Get real-time broker queue</td>
</tr>
<tr>
<td colspan="2" rowspan="6">Basic Data</td>
<td><a href="./get-market-state.html">GetMarketState</a></td>
<td>Get market status of securities</td>
</tr>
<tr>
<td><a href="./get-capital-flow.html">GetCapitalFlow</a></td>
<td>Get capital flow</td>
</tr>
<tr>
<td><a
href="./get-capital-distribution.html">GetCapitalDistribution</a></td>
<td>Get capital distribution</td>
</tr>
<tr>
<td><a href="./get-owner-plate.html">GetOwnerPlate</a></td>
<td>Get the stock ownership plate</td>
</tr>
<tr>
<td><a href="./request-history-kline.html">RequestHistoryKL</a></td>
<td>Get historical candlesticks</td>
</tr>
<tr>
<td><a href="./get-rehab.html">RequestRehab</a></td>
<td>Get the stock adjustment factor</td>
</tr>
<tr>
<td colspan="2" rowspan="5">Related Derivatives</td>
<td><a
href="./get-option-expiration-date.html">GetOptionExpirationDate</a></td>
<td>Query all expiration dates of option chains through the underlying
stock.</td>
</tr>
<tr>
<td><a href="./get-option-chain.html">GetOptionChain</a></td>
<td>Get the option chain from an underlying stock</td>
</tr>
<tr>
<td><a href="./get-warrant.html">GetWarrant</a></td>
<td>Get filtered warrant (for HK market only)</td>
</tr>
<tr>
<td><a href="./get-referencestock-list.html">GetReference</a></td>
<td>Get related data of securities</td>
</tr>
<tr>
<td><a href="./get-future-info.html">GetFutureInfo</a></td>
<td>Get futures contract information</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Market Filter</td>
<td><a href="./get-stock-filter.html">StockFilter</a></td>
<td>Filter stocks by condition</td>
</tr>
<tr>
<td><a href="./get-plate-stock.html">GetPlateSecurity</a></td>
<td>Get the list of stocks in the plate</td>
</tr>
<tr>
<td><a href="./get-plate-list.html">GetPlateSet</a></td>
<td>Get plate list</td>
</tr>
<tr>
<td><a href="./get-static-info.html">GetStaticInfo</a></td>
<td>Get stock basic information</td>
</tr>
<tr>
<td><a href="./get-ipo-list.html">GetIpoList</a></td>
<td>Get IPO information of a specific market</td>
</tr>
<tr>
<td><a href="./get-global-state.html">GetGlobalState</a></td>
<td>Get global status</td>
</tr>
<tr>
<td><a href="./request-trading-days.html">RequestTradeDate</a></td>
<td>Get trading calendar</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Customization</td>
<td><a href="./get-history-kl-quota.html">RequestHistoryKLQuota</a></td>
<td>Get usage details of historical candlestick quota</td>
</tr>
<tr>
<td><a href="./set-price-reminder.html">SetPriceReminder</a></td>
<td>Add, delete, modify, enable, and disable price reminders for
specified stocks</td>
</tr>
<tr>
<td><a href="./get-price-reminder.html">GetPriceReminder</a></td>
<td>Get a list of price reminders set for the specified stock or
market</td>
</tr>
<tr>
<td><a
href="./get-user-security-group.html">GetUserSecurityGroup</a></td>
<td>Get a list of groups from the user watchlist</td>
</tr>
<tr>
<td><a href="./get-user-security.html">GetUserSecurity</a></td>
<td>Get a list of a specified group from watchlist</td>
</tr>
<tr>
<td><a href="./modify-user-security.html">ModifyUserSecurity</a></td>
<td>Modify the specific group from the watchlist</td>
</tr>
<tr>
<td><a href="./update-price-reminder.html">UpdatePriceReminder</a></td>
<td>The price reminder notification callback</td>
</tr>
</tbody>
</table>





<table>
<thead>
<tr>
<th colspan="2">Module</th>
<th>Protocol ID</th>
<th>Protobuf File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="15">Real-Time Data</td>
<td rowspan="2">Subscription</td>
<td>3001</td>
<td><a href="../quote/sub.html">Qot_Sub</a></td>
<td>Subscribe or unsubscribe real-time market data</td>
</tr>
<tr>
<td>3003</td>
<td><a href="../quote/query-subscription.html">Qot_GetSubInfo</a></td>
<td>Get subscription information</td>
</tr>
<tr>
<td rowspan="6">Push and Callback</td>
<td>3005</td>
<td><a
href="../quote/update-stock-quote.html">Qot_UpdateBasicQot</a></td>
<td>Real-time quote callback</td>
</tr>
<tr>
<td>3013</td>
<td><a
href="../quote/update-order-book.html">Qot_UpdateOrderBook</a></td>
<td>Real-time order book callback</td>
</tr>
<tr>
<td>3007</td>
<td><a href="../quote/update-kl.html">Qot_UpdateKL</a></td>
<td>Real-time candlestick callback</td>
</tr>
<tr>
<td>3009</td>
<td><a href="../quote/update-rt.html">Qot_UpdateRT</a></td>
<td>Real-time time frame callback</td>
</tr>
<tr>
<td>3011</td>
<td><a href="../quote/update-ticker.html">Qot_UpdateTicker</a></td>
<td>Real-time tick-by-tick callback</td>
</tr>
<tr>
<td>3015</td>
<td><a href="../quote/update-broker.html">Qot_UpdateBroker</a></td>
<td>Real-time broker queue callback</td>
</tr>
<tr>
<td rowspan="7">Get</td>
<td>3203</td>
<td><a
href="../quote/get-market-snapshot.html">Qot_GetSecuritySnapshot</a></td>
<td>Get market snapshot</td>
</tr>
<tr>
<td>3004</td>
<td><a href="../quote/get-stock-quote.html">Qot_GetBasicQot</a></td>
<td>Get basic stock quote</td>
</tr>
<tr>
<td>3012</td>
<td><a href="../quote/get-order-book.html">Qot_GetOrderBook</a></td>
<td>Get real-time order book</td>
</tr>
<tr>
<td>3006</td>
<td><a href="../quote/get-kl.html">Qot_GetKL</a></td>
<td>Get real-time candlestick</td>
</tr>
<tr>
<td>3008</td>
<td><a href="../quote/get-rt.html">Qot_GetRT</a></td>
<td>Get real-time time frame data</td>
</tr>
<tr>
<td>3010</td>
<td><a href="../quote/get-ticker.html">Qot_GetTicker</a></td>
<td>Get real-time tick-by-tick</td>
</tr>
<tr>
<td>3014</td>
<td><a href="../quote/get-broker.html">Qot_GetBroker</a></td>
<td>Get real-time broker queue</td>
</tr>
<tr>
<td colspan="2" rowspan="6">Basic Data</td>
<td>3223</td>
<td><a href="../quote/get-market-state.html">Qot_GetMarketState</a></td>
<td>Get market status of securities</td>
</tr>
<tr>
<td>3211</td>
<td><a href="../quote/get-capital-flow.html">Qot_GetCapitalFlow</a></td>
<td>Get capital flow</td>
</tr>
<tr>
<td>3212</td>
<td><a
href="../quote/get-capital-distribution.html">Qot_GetCapitalDistribution</a></td>
<td>Get capital distribution</td>
</tr>
<tr>
<td>3207</td>
<td><a href="../quote/get-owner-plate.html">Qot_GetOwnerPlate</a></td>
<td>Get the stock ownership plate</td>
</tr>
<tr>
<td>3103</td>
<td><a
href="../quote/request-history-kline.html">Qot_RequestHistoryKL</a></td>
<td>Get historical candlesticks</td>
</tr>
<tr>
<td>3105</td>
<td><a href="../quote/get-rehab.html">Qot_RequestRehab</a></td>
<td>Get the stock adjustment factor</td>
</tr>
<tr>
<td colspan="2" rowspan="5">Related Derivatives</td>
<td>3224</td>
<td><a
href="../quote/get-option-expiration-date.html">Qot_GetOptionExpirationDate</a></td>
<td>Query all expiration dates of option chains through the underlying
stock</td>
</tr>
<tr>
<td>3209</td>
<td><a href="../quote/get-option-chain.html">Qot_GetOptionChain</a></td>
<td>Get option chain</td>
</tr>
<tr>
<td>3210</td>
<td><a href="../quote/get-warrant.html">Qot_GetWarrant</a></td>
<td>Get warrant</td>
</tr>
<tr>
<td>3206</td>
<td><a
href="../quote/get-referencestock-list.html">Qot_GetReference</a></td>
<td>Get the reference of stock</td>
</tr>
<tr>
<td>3218</td>
<td><a href="../quote/get-future-info.html">Qot_GetFutureInfo</a></td>
<td>Get futures contract information</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Market Filter</td>
<td>3215</td>
<td><a href="../quote/get-stock-filter.html">Qot_StockFilter</a></td>
<td>Get conditional stock selection</td>
</tr>
<tr>
<td>3205</td>
<td><a
href="../quote/get-plate-stock.html">Qot_GetPlateSecurity</a></td>
<td>Get stocks under the plate</td>
</tr>
<tr>
<td>3204</td>
<td><a href="../quote/get-plate-list.html">Qot_GetPlateSet</a></td>
<td>Get plate list</td>
</tr>
<tr>
<td>3202</td>
<td><a href="../quote/get-static-info.html">Qot_GetStaticInfo</a></td>
<td>Get stock basic information</td>
</tr>
<tr>
<td>3217</td>
<td><a href="../quote/get-ipo-list.html">Qot_GetIpoList</a></td>
<td>Get IPO information of a specific market</td>
</tr>
<tr>
<td>1002</td>
<td><a href="../quote/get-global-state.html">GetGlobalState</a></td>
<td>Get global market status</td>
</tr>
<tr>
<td>3219</td>
<td><a
href="../quote/request-trading-days.html">Qot_RequestTradeDate</a></td>
<td>Get trading calendar</td>
</tr>
<tr>
<td colspan="2" rowspan="7">Customization</td>
<td>3104</td>
<td><a
href="../quote/get-history-kl-quota.html">Qot_RequestHistoryKLQuota</a></td>
<td>Get historical candlestick quota</td>
</tr>
<tr>
<td>3220</td>
<td><a
href="../quote/set-price-reminder.html">Qot_SetPriceReminder</a></td>
<td>Set price reminder</td>
</tr>
<tr>
<td>3221</td>
<td><a
href="../quote/get-price-reminder.html">Qot_GetPriceReminder</a></td>
<td>Get price reminder</td>
</tr>
<tr>
<td>3213</td>
<td><a
href="../quote/get-user-security.html">Qot_GetUserSecurity</a></td>
<td>Get the stock under the watchlists</td>
</tr>
<tr>
<td>3222</td>
<td><a
href="../quote/get-user-security-group.html">Qot_GetUserSecurityGroup</a></td>
<td>Get a list of watchlists</td>
</tr>
<tr>
<td>3214</td>
<td><a
href="../quote/modify-user-security.html">Qot_ModifyUserSecurity</a></td>
<td>Modify the stock under the watchlists</td>
</tr>
<tr>
<td>3019</td>
<td><a
href="../quote/update-price-reminder.html">Qot_UpdatePriceReminder</a></td>
<td>Price reminder callback</td>
</tr>
</tbody>
</table>











