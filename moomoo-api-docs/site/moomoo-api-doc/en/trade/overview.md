



# <a href="#6105" class="header-anchor">#</a> Overview





- Python
- C#
- Java
- C++
- JavaScript
- 裸协议





<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Account</td>
<td><a href="./get-acc-list.html">get_acc_list</a></td>
<td>Get account list</td>
</tr>
<tr>
<td><a href="./unlock.html">unlock_trade</a></td>
<td>Unlock trading</td>
</tr>
<tr>
<td rowspan="5">Asset and Position</td>
<td><a href="./get-funds.html">accinfo_query</a></td>
<td>Get account financial information</td>
</tr>
<tr>
<td><a href="./get-max-trd-qtys.html">acctradinginfo_query</a></td>
<td>Get maximum tradable quantity</td>
</tr>
<tr>
<td><a href="./get-position-list.html">position_list_query</a></td>
<td>Get positions list</td>
</tr>
<tr>
<td><a href="../trade/get-margin-ratio.html">Trd_GetMarginRatio</a></td>
<td>Get margin data</td>
</tr>
<tr>
<td><a href="../trade/get-acc-cash-flow.html">Get Cash Flow
Summary</a></td>
<td>Get Account Cash Flow Data

  


 

Minimum version requirement：9.1.5108



</td>
</tr>
<tr>
<td rowspan="7">Order</td>
<td><a href="./place-order.html">place_order</a></td>
<td>Place order</td>
</tr>
<tr>
<td><a href="./modify-order.html">modify_order</a></td>
<td>Modify or cancel order</td>
</tr>
<tr>
<td><a href="./get-order-list.html">order_list_query</a></td>
<td>Get order list</td>
</tr>
<tr>
<td><a href="./order-fee-query.html">order_fee_query</a></td>
<td>Get order fees

  


 

Minimum version requirement: 8.2.4218



</td>
</tr>
<tr>
<td><a
href="./get-history-order-list.html">history_order_list_query</a></td>
<td>Get historical order list</td>
</tr>
<tr>
<td><a href="./update-order.html">TradeOrderHandlerBase</a></td>
<td>Order callback</td>
</tr>
<tr>
<td><a href="./sub-acc-push.html">SubAccPush</a></td>
<td>Trade data callback</td>
</tr>
<tr>
<td rowspan="3">Deal</td>
<td><a href="./get-order-fill-list.html">deal_list_query</a></td>
<td>Get today's executed trades</td>
</tr>
<tr>
<td><a
href="./get-history-order-fill-list.html">history_deal_list_query</a></td>
<td>Get historical executed trades</td>
</tr>
<tr>
<td><a href="./update-order-fill.html">TradeDealHandlerBase</a></td>
<td>Trade execution callback</td>
</tr>
</tbody>
</table>





<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Account</td>
<td><a href="./get-acc-list.html">GetAccList</a></td>
<td>Get account list</td>
</tr>
<tr>
<td><a href="./unlock.html">UnlockTrade</a></td>
<td>Lock or unlock the trade</td>
</tr>
<tr>
<td rowspan="5">Asset and Position</td>
<td><a href="./get-funds.html">GetFunds</a></td>
<td>Get account funds</td>
</tr>
<tr>
<td><a href="./get-max-trd-qtys.html">GetMaxTrdQtys</a></td>
<td>Get the maximum number of trade</td>
</tr>
<tr>
<td><a href="./get-position-list.html">GetPositionList</a></td>
<td>Get account positions</td>
</tr>
<tr>
<td><a href="../trade/get-margin-ratio.html">Trd_GetMarginRatio</a></td>
<td>Get margin data</td>
</tr>
<tr>
<td><a href="../trade/get-acc-cash-flow.html">Get Cash Flow
Summary</a></td>
<td>Get Account Cash Flow Data

  


 

Minimum version requirement：9.1.5108



</td>
</tr>
<tr>
<td rowspan="7">Order</td>
<td><a href="./place-order.html">PlaceOrder</a></td>
<td>Place order</td>
</tr>
<tr>
<td><a href="./modify-order.html">ModifyOrder</a></td>
<td>Modify order</td>
</tr>
<tr>
<td><a href="./get-order-list.html">GetOrderList</a></td>
<td>Get order list</td>
</tr>
<tr>
<td><a href="./order-fee-query.html">GetOrderFee</a></td>
<td>Get order fee

  


 

Minimum version requirement: 8.2.4218



</td>
</tr>
<tr>
<td><a href="./get-history-order-list.html">GetHistoryOrderList</a></td>
<td>Get historical order list</td>
</tr>
<tr>
<td><a href="./update-order.html">UpdateOrder</a></td>
<td>Push notification of order status changes</td>
</tr>
<tr>
<td><a href="./sub-acc-push.html">SubAccPush</a></td>
<td>Subscribe to the trade push data of the account</td>
</tr>
<tr>
<td rowspan="3">Deal</td>
<td><a href="./get-order-fill-list.html">GetOrderFillList</a></td>
<td>Get a list of deal</td>
</tr>
<tr>
<td><a
href="./get-history-order-fill-list.html">GetHistoryOrderFillList</a></td>
<td>Get historical deal list</td>
</tr>
<tr>
<td><a href="./update-order-fill.html">OnPush_UpdateOrderFill</a></td>
<td>Push deal notification</td>
</tr>
</tbody>
</table>





<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Account</td>
<td><a href="./get-acc-list.html">getAccList</a></td>
<td>Get account list</td>
</tr>
<tr>
<td><a href="./unlock.html">unlockTrade</a></td>
<td>Lock or unlock the trade</td>
</tr>
<tr>
<td rowspan="5">Asset and Position</td>
<td><a href="./get-funds.html">getFunds</a></td>
<td>Get account funds</td>
</tr>
<tr>
<td><a href="./get-max-trd-qtys.html">getMaxTrdQtys</a></td>
<td>Get the maximum number of trade</td>
</tr>
<tr>
<td><a href="./get-position-list.html">getPositionList</a></td>
<td>Get account positions</td>
</tr>
<tr>
<td><a href="../trade/get-margin-ratio.html">Trd_GetMarginRatio</a></td>
<td>Get margin data</td>
</tr>
<tr>
<td><a href="../trade/get-acc-cash-flow.html">Get Cash Flow
Summary</a></td>
<td>Get Account Cash Flow Data

  


 

Minimum version requirement：9.1.5108



</td>
</tr>
<tr>
<td rowspan="7">Order</td>
<td><a href="./place-order.html">placeOrder</a></td>
<td>Place order</td>
</tr>
<tr>
<td><a href="./modify-order.html">modifyOrder</a></td>
<td>Modify order</td>
</tr>
<tr>
<td><a href="./get-order-list.html">getOrderList</a></td>
<td>Get order list</td>
</tr>
<tr>
<td><a href="./order-fee-query.html">getOrderFee</a></td>
<td>Get order fee

  


 

Minimum version requirement: 8.2.4218



</td>
</tr>
<tr>
<td><a href="./get-history-order-list.html">getHistoryOrderList</a></td>
<td>Get historical order list</td>
</tr>
<tr>
<td><a href="./update-order.html">updateOrder</a></td>
<td>Push notification of order status changes</td>
</tr>
<tr>
<td><a href="./sub-acc-push.html">subAccPush</a></td>
<td>Subscribe to the trade push data of the account</td>
</tr>
<tr>
<td rowspan="3">Deal</td>
<td><a href="./get-order-fill-list.html">getOrderFillList</a></td>
<td>Get a list of deal</td>
</tr>
<tr>
<td><a
href="./get-history-order-fill-list.html">getHistoryOrderFillList</a></td>
<td>Get historical deal list</td>
</tr>
<tr>
<td><a href="./update-order-fill.html">onPush_UpdateOrderFill</a></td>
<td>Push deal notification</td>
</tr>
</tbody>
</table>





<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Account</td>
<td><a href="./get-acc-list.html">GetAccList</a></td>
<td>Get account list</td>
</tr>
<tr>
<td><a href="./unlock.html">UnlockTrade</a></td>
<td>Lock or unlock the trade</td>
</tr>
<tr>
<td rowspan="5">Asset and Position</td>
<td><a href="./get-funds.html">GetFunds</a></td>
<td>Get account funds</td>
</tr>
<tr>
<td><a href="./get-max-trd-qtys.html">GetMaxTrdQtys</a></td>
<td>Get the maximum number of trade</td>
</tr>
<tr>
<td><a href="./get-position-list.html">GetPositionList</a></td>
<td>Get account positions</td>
</tr>
<tr>
<td><a href="../trade/get-margin-ratio.html">Trd_GetMarginRatio</a></td>
<td>Get margin data</td>
</tr>
<tr>
<td><a href="../trade/get-acc-cash-flow.html">Get Cash Flow
Summary</a></td>
<td>Get Account Cash Flow Data

  


 

Minimum version requirement：9.1.5108



</td>
</tr>
<tr>
<td rowspan="7">Order</td>
<td><a href="./place-order.html">PlaceOrder</a></td>
<td>Place order</td>
</tr>
<tr>
<td><a href="./modify-order.html">ModifyOrder</a></td>
<td>Modify order</td>
</tr>
<tr>
<td><a href="./get-order-list.html">GetOrderList</a></td>
<td>Get order list</td>
</tr>
<tr>
<td><a href="./order-fee-query.html">GetOrderFee</a></td>
<td>Get order fee

  


 

Minimum version requirement: 8.2.4218



</td>
</tr>
<tr>
<td><a href="./get-history-order-list.html">GetHistoryOrderList</a></td>
<td>Get historical order list</td>
</tr>
<tr>
<td><a href="./update-order.html">UpdateOrder</a></td>
<td>Push notification of order status changes</td>
</tr>
<tr>
<td><a href="./sub-acc-push.html">SubAccPush</a></td>
<td>Subscribe to the trade push data of the account</td>
</tr>
<tr>
<td rowspan="3">Deal</td>
<td><a href="./get-order-fill-list.html">GetOrderFillList</a></td>
<td>Get a list of deal</td>
</tr>
<tr>
<td><a
href="./get-history-order-fill-list.html">GetHistoryOrderFillList</a></td>
<td>Get historical deal list</td>
</tr>
<tr>
<td><a href="./update-order-fill.html">OnPush_UpdateOrderFill</a></td>
<td>Push deal notification</td>
</tr>
</tbody>
</table>





<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th>Module</th>
<th>Interface Name</th>
<th>Function Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Account</td>
<td><a href="./get-acc-list.html">GetAccList</a></td>
<td>Get account list</td>
</tr>
<tr>
<td><a href="./unlock.html">UnlockTrade</a></td>
<td>Lock or unlock the trade</td>
</tr>
<tr>
<td rowspan="5">Asset and Position</td>
<td><a href="./get-funds.html">GetFunds</a></td>
<td>Get account funds</td>
</tr>
<tr>
<td><a href="./get-max-trd-qtys.html">GetMaxTrdQtys</a></td>
<td>Get the maximum number of trade</td>
</tr>
<tr>
<td><a href="./get-position-list.html">GetPositionList</a></td>
<td>Get account positions</td>
</tr>
<tr>
<td><a href="../trade/get-margin-ratio.html">Trd_GetMarginRatio</a></td>
<td>Get margin data</td>
</tr>
<tr>
<td><a href="../trade/get-acc-cash-flow.html">Get Cash Flow
Summary</a></td>
<td>Get Account Cash Flow Data

  


 

Minimum version requirement：9.1.5108



</td>
</tr>
<tr>
<td rowspan="7">Order</td>
<td><a href="./place-order.html">PlaceOrder</a></td>
<td>Place order</td>
</tr>
<tr>
<td><a href="./modify-order.html">ModifyOrder</a></td>
<td>Modify order</td>
</tr>
<tr>
<td><a href="./get-order-list.html">GetOrderList</a></td>
<td>Get order list</td>
</tr>
<tr>
<td><a href="./order-fee-query.html">GetOrderFee</a></td>
<td>Get order fee

  


 

Minimum version requirement: 8.2.4218



</td>
</tr>
<tr>
<td><a href="./get-history-order-list.html">GetHistoryOrderList</a></td>
<td>Get historical order list</td>
</tr>
<tr>
<td><a href="./update-order.html">UpdateOrder</a></td>
<td>Push notification of order status changes</td>
</tr>
<tr>
<td><a href="./sub-acc-push.html">SubAccPush</a></td>
<td>Subscribe to the trade push data of the account</td>
</tr>
<tr>
<td rowspan="3">Deal</td>
<td><a href="./get-order-fill-list.html">GetOrderFillList</a></td>
<td>Get a list of deal</td>
</tr>
<tr>
<td><a
href="./get-history-order-fill-list.html">GetHistoryOrderFillList</a></td>
<td>Get historical deal list</td>
</tr>
<tr>
<td><a href="./update-order-fill.html">OnPush_UpdateOrderFill</a></td>
<td>Push deal notification</td>
</tr>
</tbody>
</table>





<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th>Module</th>
<th>Protocol ID</th>
<th>Protobuf File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Account</td>
<td>2001</td>
<td><a href="../trade/get-acc-list.html">Trd_GetAccList</a></td>
<td>Get a list of accounts</td>
</tr>
<tr>
<td>2005</td>
<td><a href="../trade/unlock.html">Trd_UnlockTrade</a></td>
<td>Lock or unlock the trade</td>
</tr>
<tr>
<td rowspan="5">Asset and Position</td>
<td>2101</td>
<td><a href="../trade/get-funds.html">Trd_GetFunds</a></td>
<td>Get account funds</td>
</tr>
<tr>
<td>2111</td>
<td><a href="../trade/get-max-trd-qtys.html">Trd_GetMaxTrdQtys</a></td>
<td>Get the maximum number of trade</td>
</tr>
<tr>
<td>2102</td>
<td><a
href="../trade/get-position-list.html">Trd_GetPositionList</a></td>
<td>Get account positions</td>
</tr>
<tr>
<td>2223</td>
<td><a href="../trade/get-margin-ratio.html">Trd_GetMarginRatio</a></td>
<td>Get margin data</td>
</tr>
<tr>
<td>2226</td>
<td><a href="../trade/get-acc-cash-flow.html">Get Cash Flow
Summary</a></td>
<td>Get Account Cash Flow Data

  


 

Minimum version requirement：9.1.5108



</td>
</tr>
<tr>
<td rowspan="7">Order</td>
<td>2202</td>
<td><a href="../trade/place-order.html">Trd_PlaceOrder</a></td>
<td>Place order</td>
</tr>
<tr>
<td>2205</td>
<td><a href="../trade/modify-order.html">Trd_ModifyOrder</a></td>
<td>Modify order</td>
</tr>
<tr>
<td>2201</td>
<td><a href="../trade/get-order-list.html">Trd_GetOrderList</a></td>
<td>Get order list</td>
</tr>
<tr>
<td>2225</td>
<td><a href="../trade/order-fee-query.html">Trd_GetOrderFee</a></td>
<td>Get order fee

  


 

Minimum version requirement: 8.2.4218



</td>
</tr>
<tr>
<td>2221</td>
<td><a
href="../trade/get-history-order-list.html">Trd_GetHistoryOrderList</a></td>
<td>Get historical order list</td>
</tr>
<tr>
<td>2208</td>
<td><a href="../trade/update-order.html">Trd_UpdateOrder</a></td>
<td>Push notification of order status changes</td>
</tr>
<tr>
<td>2008</td>
<td><a href="../trade/sub-acc-push.html">Trd_SubAccPush</a></td>
<td>Subscribe to the trade push data of the account</td>
</tr>
<tr>
<td rowspan="3">Deal</td>
<td>2211</td>
<td><a href="../trade/get-order-list.html">Trd_GetOrderFillList</a></td>
<td>Get a list of deal</td>
</tr>
<tr>
<td>2222</td>
<td><a
href="../trade/get-history-order-fill-list.html">Trd_GetHistoryOrderFillList</a></td>
<td>Get historical deal list</td>
</tr>
<tr>
<td>2218</td>
<td><a
href="../trade/update-order-fill.html">Trd_UpdateOrderFill</a></td>
<td>Push deal notification</td>
</tr>
</tbody>
</table>











