



# <a href="#6240" class="header-anchor">#</a> Trading Definitions

## <a href="#428" class="header-anchor">#</a> Account Risk Control Level





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **CltRiskLevel**

- `NONE`

  Unknown

- `SAFE`

  Safe

- `WARNING`

  Warning

- `DANGER`

  Danger

- `ABSOLUTE_SAFE`

  Absolutely safe

- `OPT_DANGER`

  Danger

  

  
  

  

  
  
  

  Option related.

  

  

  

  



Tips

- It is recommanded to use risk_status field to get risk status of
  futures account, see
  [CltRiskStatus](/moomoo-api-doc/en/trade/trade.html#7469)







**CltRiskLevel**



``` protobuf
enum CltRiskLevel
{
    CltRiskLevel_Unknown = -1; //Unknown
    CltRiskLevel_Safe = 0; //Safe
    CltRiskLevel_Warning = 1; //Warning
    CltRiskLevel_Danger = 2; //Danger
    CltRiskLevel_AbsoluteSafe = 3; //Absolutely safe
    CltRiskLevel_OptDanger = 4; //Danger (option related)
}
```









**CltRiskLevel**



``` protobuf
enum CltRiskLevel
{
    CltRiskLevel_Unknown = -1; //Unknown
    CltRiskLevel_Safe = 0; //Safe
    CltRiskLevel_Warning = 1; //Warning
    CltRiskLevel_Danger = 2; //Danger
    CltRiskLevel_AbsoluteSafe = 3; //Absolutely safe
    CltRiskLevel_OptDanger = 4; //Danger (option related)
}
```









**CltRiskLevel**



``` protobuf
enum CltRiskLevel
{
    CltRiskLevel_Unknown = -1; //Unknown
    CltRiskLevel_Safe = 0; //Safe
    CltRiskLevel_Warning = 1; //Warning
    CltRiskLevel_Danger = 2; //Danger
    CltRiskLevel_AbsoluteSafe = 3; //Absolutely safe
    CltRiskLevel_OptDanger = 4; //Danger (option related)
}
```









**CltRiskLevel**



``` protobuf
enum CltRiskLevel
{
    CltRiskLevel_Unknown = -1; //Unknown
    CltRiskLevel_Safe = 0; //Safe
    CltRiskLevel_Warning = 1; //Warning
    CltRiskLevel_Danger = 2; //Danger
    CltRiskLevel_AbsoluteSafe = 3; //Absolutely safe
    CltRiskLevel_OptDanger = 4; //Danger (option related)
}
```









**CltRiskLevel**



``` protobuf
enum CltRiskLevel
{
    CltRiskLevel_Unknown = -1; //Unknown
    CltRiskLevel_Safe = 0; //Safe
    CltRiskLevel_Warning = 1; //Warning
    CltRiskLevel_Danger = 2; //Danger
    CltRiskLevel_AbsoluteSafe = 3; //Absolutely safe
    CltRiskLevel_OptDanger = 4; //Danger (option related)
}
```









## <a href="#1655" class="header-anchor">#</a> Currency Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **Currency**

- `NONE`

  Unknown currency

- `HKD`

  HK dollar

- `USD`

  US dollar

- `CNH`

  Offshore RMB

- `JPY`

  Japanese Yen

- `SGD`

  SG dollar

- `AUD`

  Australian dollar

- `CAD`

  Canadian dollar

- `MYR`

  Malaysian Ringgit





**Currency**



``` protobuf
enum Currency
{
    Currency_Unknown = 0; //Unknown currency
    Currency_HKD = 1; //Hong Kong dollar
    Currency_USD = 2; //USD
    Currency_CNH = 3; //Offshore RMB
    Currency_JPY = 4; //Japanese Yen
    Currency_SGD = 5; //SG dollar
    Currency_AUD = 6; //Australian dollar
    Currency_CAD = 7; // Canadian dollar
    Currency_MYR = 8; // Malaysian Ringgit

}
```









**Currency**



``` protobuf
enum Currency
{
    Currency_Unknown = 0; //Unknown currency
    Currency_HKD = 1; //Hong Kong dollar
    Currency_USD = 2; //USD
    Currency_CNH = 3; //Offshore RMB
    Currency_JPY = 4; //Japanese Yen
    Currency_SGD = 5; //SG dollar
    Currency_AUD = 6; //Australian dollar
    Currency_CAD = 7; // Canadian dollar
    Currency_MYR = 8; // Malaysian Ringgit
}
```









**Currency**



``` protobuf
enum Currency
{
    Currency_Unknown = 0; //Unknown currency
    Currency_HKD = 1; //Hong Kong dollar
    Currency_USD = 2; //USD
    Currency_CNH = 3; //Offshore RMB
    Currency_JPY = 4; //Japanese Yen
    Currency_SGD = 5; //SG dollar
    Currency_AUD = 6; //Australian dollar
    Currency_CAD = 7; // Canadian dollar
    Currency_MYR = 8; // Malaysian Ringgit
}
```









**Currency**



``` protobuf
enum Currency
{
    Currency_Unknown = 0; //Unknown currency
    Currency_HKD = 1; //Hong Kong dollar
    Currency_USD = 2; //USD
    Currency_CNH = 3; //Offshore RMB
    Currency_JPY = 4; //Japanese Yen
    Currency_SGD = 5; //SG dollar
    Currency_AUD = 6; //Australian dollar
    Currency_CAD = 7; // Canadian dollar
    Currency_MYR = 8; // Malaysian Ringgit
}
```









**Currency**



``` protobuf
enum Currency
{
    Currency_Unknown = 0; //Unknown currency
    Currency_HKD = 1; //Hong Kong dollar
    Currency_USD = 2; //USD
    Currency_CNH = 3; //Offshore RMB
    Currency_JPY = 4; //Japanese Yen
    Currency_SGD = 5; //SG dollar
    Currency_AUD = 6; //Australian dollar
    Currency_CAD = 7; // Canadian dollar
    Currency_MYR = 8; // Malaysian Ringgit
}
```









## <a href="#12" class="header-anchor">#</a> TrailType





- Python
- Proto
- C#
- Java
- C++
- JavaScript





**TrailType**

- `NONE`

  Unknown

- `RATIO`

  Trailing ratio

- `AMOUNT`

  Trailing amount







``` protobuf
enum TrailType
{
    TrailType_Unknown = 0; //Unknown
    TrailType_Ratio = 1; //Trailing ratio
    TrailType_Amount = 2; //Trailing amount
}
```











``` protobuf
enum TrailType
{
    TrailType_Unknown = 0; //Unknown
    TrailType_Ratio = 1; //Trailing ratio
    TrailType_Amount = 2; //Trailing amount
}
```











``` protobuf
enum TrailType
{
    TrailType_Unknown = 0; //Unknown
    TrailType_Ratio = 1; //Trailing ratio
    TrailType_Amount = 2; //Trailing amount
}
```











``` protobuf
enum TrailType
{
    TrailType_Unknown = 0; //Unknown
    TrailType_Ratio = 1; //Trailing ratio
    TrailType_Amount = 2; //Trailing amount
}
```











``` protobuf
enum TrailType
{
    TrailType_Unknown = 0; //Unknown
    TrailType_Ratio = 1; //Trailing ratio
    TrailType_Amount = 2; //Trailing amount
}
```









## <a href="#3811" class="header-anchor">#</a> Modify Order Operation





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **ModifyOrderOp**

- `NONE`

  Unknown operation

- `NORMAL`

  Modify order

- `CANCEL`

  Cancel

  

  
  

  

  
  
  

  The uncompleted order will be directly cancelled from the exchange
  matching queue.

  

  

  

  

- `DISABLE`

  Disable

  

  
  

  

  
  
  

  - To the exchange, DISABLE is the same as CANCEL.
  - After the order is invalid, the unfilled order will be directly
    withdrawn from the exchange matching queue, but the order
    information (such as price and quantity) will continue to be
    retained in Futu server, and you still can ENABLE it.

  

  

  

  

- `ENABLE`

  Enable

  

  
  

  

  
  
  

  - Validate the invalid order. To the exchange, ENABLE is the same as
    placing a new order.
  - After the order is validated, the order will be re-submitted to the
    exchange according to the original price and quantity, and the
    re-validated orders need to be re-queued in the order of price
    priority and time priority.

  

  

  

  

- `DELETE`

  Delete

  

  
  

  

  
  
  

  Hide the order that is canceled or failed.

  

  

  

  





**ModifyOrderOp**



``` protobuf
enum ModifyOrderOp
{
    //Hong Kong market supports all operations; US market currently only supports ModifyOrderOp_Normal and ModifyOrderOp_Cancel
    ModifyOrderOp_Unknown = 0; //Unknown operation
    ModifyOrderOp_Normal = 1; //Modify price/quantity of order
    ModifyOrderOp_Cancel = 2; //Cancel. The uncompleted order will be directly cancelled from the exchange matching queue.
    ModifyOrderOp_Disable = 3; //Disable. To the exchange, disable is the same as cancel. After the order is invalid, the unfilled order will be directly withdrawn from the exchange matching queue, but the order information (such as price and quantity) will continue to be retained in Futu server, and you still can enable it.
    ModifyOrderOp_Enable = 4; //Enable. Validate the invalid order. To the exchange, enable is the same as placing a new order. After the order is validated, the order will be re-submitted to the exchange according to the original price and quantity, and the re-validated orders need to be re-queued in the order of price priority and time priority.
    ModifyOrderOp_Delete = 5; //Delete. Hide the order that is canceled or failed.
}
```









**ModifyOrderOp**



``` protobuf
enum ModifyOrderOp
{
    //Hong Kong market supports all operations; US market currently only supports ModifyOrderOp_Normal and ModifyOrderOp_Cancel
    ModifyOrderOp_Unknown = 0; //Unknown operation
    ModifyOrderOp_Normal = 1; //Modify price/quantity of order
    ModifyOrderOp_Cancel = 2; //Cancel. The uncompleted order will be directly cancelled from the exchange matching queue.
    ModifyOrderOp_Disable = 3; //Disable. To the exchange, disable is the same as cancel. After the order is invalid, the unfilled order will be directly withdrawn from the exchange matching queue, but the order information (such as price and quantity) will continue to be retained in Futu server, and you still can enable it.
    ModifyOrderOp_Enable = 4; //Enable. Validate the invalid order. To the exchange, enable is the same as placing a new order. After the order is validated, the order will be re-submitted to the exchange according to the original price and quantity, and the re-validated orders need to be re-queued in the order of price priority and time priority.
    ModifyOrderOp_Delete = 5; //Delete. Hide the order that is canceled or failed.
}
```









**ModifyOrderOp**



``` protobuf
enum ModifyOrderOp
{
    //Hong Kong market supports all operations; US market currently only supports ModifyOrderOp_Normal and ModifyOrderOp_Cancel
    ModifyOrderOp_Unknown = 0; //Unknown operation
    ModifyOrderOp_Normal = 1; //Modify price/quantity of order
    ModifyOrderOp_Cancel = 2; //Cancel. The uncompleted order will be directly cancelled from the exchange matching queue.
    ModifyOrderOp_Disable = 3; //Disable. To the exchange, disable is the same as cancel. After the order is invalid, the unfilled order will be directly withdrawn from the exchange matching queue, but the order information (such as price and quantity) will continue to be retained in Futu server, and you still can enable it.
    ModifyOrderOp_Enable = 4; //Enable. Validate the invalid order. To the exchange, enable is the same as placing a new order. After the order is validated, the order will be re-submitted to the exchange according to the original price and quantity, and the re-validated orders need to be re-queued in the order of price priority and time priority.
    ModifyOrderOp_Delete = 5; //Delete. Hide the order that is canceled or failed.
}
```









**ModifyOrderOp**



``` protobuf
enum ModifyOrderOp
{
    //Hong Kong market supports all operations; US market currently only supports ModifyOrderOp_Normal and ModifyOrderOp_Cancel
    ModifyOrderOp_Unknown = 0; //Unknown operation
    ModifyOrderOp_Normal = 1; //Modify price/quantity of order
    ModifyOrderOp_Cancel = 2; //Cancel. The uncompleted order will be directly cancelled from the exchange matching queue.
    ModifyOrderOp_Disable = 3; //Disable. To the exchange, disable is the same as cancel. After the order is invalid, the unfilled order will be directly withdrawn from the exchange matching queue, but the order information (such as price and quantity) will continue to be retained in Futu server, and you still can enable it.
    ModifyOrderOp_Enable = 4; //Enable. Validate the invalid order. To the exchange, enable is the same as placing a new order. After the order is validated, the order will be re-submitted to the exchange according to the original price and quantity, and the re-validated orders need to be re-queued in the order of price priority and time priority.
    ModifyOrderOp_Delete = 5; //Delete. Hide the order that is canceled or failed.
}
```









**ModifyOrderOp**



``` protobuf
enum ModifyOrderOp
{
    //Hong Kong market supports all operations; US market currently only supports ModifyOrderOp_Normal and ModifyOrderOp_Cancel
    ModifyOrderOp_Unknown = 0; //Unknown operation
    ModifyOrderOp_Normal = 1; //Modify price/quantity of order
    ModifyOrderOp_Cancel = 2; //Cancel. The uncompleted order will be directly cancelled from the exchange matching queue.
    ModifyOrderOp_Disable = 3; //Disable. To the exchange, disable is the same as cancel. After the order is invalid, the unfilled order will be directly withdrawn from the exchange matching queue, but the order information (such as price and quantity) will continue to be retained in Futu server, and you still can enable it.
    ModifyOrderOp_Enable = 4; //Enable. Validate the invalid order. To the exchange, enable is the same as placing a new order. After the order is validated, the order will be re-submitted to the exchange according to the original price and quantity, and the re-validated orders need to be re-queued in the order of price priority and time priority.
    ModifyOrderOp_Delete = 5; //Delete. Hide the order that is canceled or failed.
}
```









## <a href="#4379" class="header-anchor">#</a> Transaction Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **DealStatus**

- `OK`

  Transaction success

- `CANCELLED`

  Transaction cancelled

- `CHANGED`

  Transaction changed





**OrderFillStatus**



``` protobuf
enum OrderFillStatus
{
    OrderFillStatus_OK = 0; //Transaction success
    OrderFillStatus_Cancelled = 1; //Transaction cancelled
    OrderFillStatus_Changed = 2; //Transaction changed
}
```









**OrderFillStatus**



``` protobuf
enum OrderFillStatus
{
    OrderFillStatus_OK = 0; //Transaction success
    OrderFillStatus_Cancelled = 1; //Transaction cancelled
    OrderFillStatus_Changed = 2; //Transaction changed
}
```









**OrderFillStatus**



``` protobuf
enum OrderFillStatus
{
    OrderFillStatus_OK = 0; //Transaction success
    OrderFillStatus_Cancelled = 1; //Transaction cancelled
    OrderFillStatus_Changed = 2; //Transaction changed
}
```









**OrderFillStatus**



``` protobuf
enum OrderFillStatus
{
    OrderFillStatus_OK = 0; //Transaction success
    OrderFillStatus_Cancelled = 1; //Transaction cancelled
    OrderFillStatus_Changed = 2; //Transaction changed
}
```









**OrderFillStatus**



``` protobuf
enum OrderFillStatus
{
    OrderFillStatus_OK = 0; //Transaction success
    OrderFillStatus_Cancelled = 1; //Transaction cancelled
    OrderFillStatus_Changed = 2; //Transaction changed
}
```









## <a href="#8074" class="header-anchor">#</a> Order Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OrderStatus**

- `NONE`

  Unknown status

- `WAITING_SUBMIT`

  Queued

  

  
  

  

  
  
  

  Futu server has received your order and is preparing to submit it to
  the exchange.

  

  

  

  

- `SUBMITTING`

  Submitting

  

  
  

  

  
  
  

  Futu server has sent your order to the exchange, and the exchange is
  processing the order.

  

  

  

  

- `SUBMITTED`

  Working

  

  
  

  

  
  
  

  Order has been successfully submitted to the exchange.

  

  

  

  

- `FILLED_PART`

  Partially filled

  

  
  

  

  
  
  

  You can choose to cancel, or wait for fullly filled.

  

  

  

  

- `FILLED_ALL`

  Fully filled

- `CANCELLED_PART`

  Partially cancelled

- `CANCELLED_ALL`

  Fully cancelled

- `FAILED`

  Failed. Rejected by server.

- `DISABLED`

  Deactivated

  

  
  

  

  
  
  

  Actively operate a disabled order, this will not be submitted to the
  exchange.

  

  

  

  

- `DELETED`

  Deleted, only unfilled orders can be deleted

  

  
  

  

  
  
  

  The status after you actively delete the order.

  

  

  

  





**OrderStatus**



``` protobuf
enum OrderStatus
{
    OrderStatus_Unsubmitted = 0; //Unsubmitted (This enum value is deprecated)
    OrderStatus_Unknown = -1; //Unknown status
    OrderStatus_WaitingSubmit = 1; //Waiting to submit (Futu server has received your order and is preparing to submit it to the exchange)
    OrderStatus_Submitting = 2; //Queued  (Futu server has sent your order to the exchange, and the exchange is processing the order)
    OrderStatus_SubmitFailed = 3; //Submission failed (This enum value is deprecated)
    OrderStatus_TimeOut = 4; //Processing timed out, result unknown (This enum value is deprecated)
    OrderStatus_Submitted = 5; //Working, waiting to be filled (Your order has been successfully submitted to the exchange)
    OrderStatus_Filled_Part = 10; //Partially filled (The unfilled part of the order has not been cancelled. You can choose to cancel, or wait for fullly filled)
    OrderStatus_Filled_All = 11; //All filled
    OrderStatus_Cancelling_Part = 12; //Cancelling part of the order (One part of the order has been filled, and the rest is being cancelled) (This enum value is deprecated)
    OrderStatus_Cancelling_All = 13; //Cancelling the whole order (This enum value is deprecated)
    OrderStatus_Cancelled_Part = 14; //Part of the order is filled, and the remaining has been withdrawn (This enum value is deprecated)
    OrderStatus_Cancelled_All = 15; //All orders have been cancelled, no transactions (This enum value is deprecated)
    OrderStatus_Failed = 21; //Order failed, refused by serser
    OrderStatus_Disabled = 22; //Order disabled (Actively operate a disabled order, this will not be submitted to the exchange)
    OrderStatus_Deleted = 23; //Deleted, only unfilled orders can be deleted (The status after you actively delete the order)
    OrderStatus_FillCancelled = 24; //The transaction is canceled (This enum value is deprecated)
}
```









**OrderStatus**



``` protobuf
enum OrderStatus
{
    OrderStatus_Unsubmitted = 0; //Unsubmitted (This enum value is deprecated)
    OrderStatus_Unknown = -1; //Unknown status
    OrderStatus_WaitingSubmit = 1; //Waiting to submit (Futu server has received your order and is preparing to submit it to the exchange)
    OrderStatus_Submitting = 2; //Queued  (Futu server has sent your order to the exchange, and the exchange is processing the order)
    OrderStatus_SubmitFailed = 3; //Submission failed (This enum value is deprecated)
    OrderStatus_TimeOut = 4; //Processing timed out, result unknown (This enum value is deprecated)
    OrderStatus_Submitted = 5; //Working, waiting to be filled (Your order has been successfully submitted to the exchange)
    OrderStatus_Filled_Part = 10; //Partially filled (The unfilled part of the order has not been cancelled. You can choose to cancel, or wait for fullly filled)
    OrderStatus_Filled_All = 11; //All filled
    OrderStatus_Cancelling_Part = 12; //Cancelling part of the order (One part of the order has been filled, and the rest is being cancelled) (This enum value is deprecated)
    OrderStatus_Cancelling_All = 13; //Cancelling the whole order (This enum value is deprecated)
    OrderStatus_Cancelled_Part = 14; //Part of the order is filled, and the remaining has been withdrawn (This enum value is deprecated)
    OrderStatus_Cancelled_All = 15; //All orders have been cancelled, no transactions (This enum value is deprecated)
    OrderStatus_Failed = 21; //Order failed, refused by serser
    OrderStatus_Disabled = 22; //Order disabled (Actively operate a disabled order, this will not be submitted to the exchange)
    OrderStatus_Deleted = 23; //Deleted, only unfilled orders can be deleted (The status after you actively delete the order)
    OrderStatus_FillCancelled = 24; //The transaction is canceled (This enum value is deprecated)
}
```









**OrderStatus**



``` protobuf
enum OrderStatus
{
    OrderStatus_Unsubmitted = 0; //Unsubmitted (This enum value is deprecated)
    OrderStatus_Unknown = -1; //Unknown status
    OrderStatus_WaitingSubmit = 1; //Waiting to submit (Futu server has received your order and is preparing to submit it to the exchange)
    OrderStatus_Submitting = 2; //Queued  (Futu server has sent your order to the exchange, and the exchange is processing the order)
    OrderStatus_SubmitFailed = 3; //Submission failed (This enum value is deprecated)
    OrderStatus_TimeOut = 4; //Processing timed out, result unknown (This enum value is deprecated)
    OrderStatus_Submitted = 5; //Working, waiting to be filled (Your order has been successfully submitted to the exchange)
    OrderStatus_Filled_Part = 10; //Partially filled (The unfilled part of the order has not been cancelled. You can choose to cancel, or wait for fullly filled)
    OrderStatus_Filled_All = 11; //All filled
    OrderStatus_Cancelling_Part = 12; //Cancelling part of the order (One part of the order has been filled, and the rest is being cancelled) (This enum value is deprecated)
    OrderStatus_Cancelling_All = 13; //Cancelling the whole order (This enum value is deprecated)
    OrderStatus_Cancelled_Part = 14; //Part of the order is filled, and the remaining has been withdrawn (This enum value is deprecated)
    OrderStatus_Cancelled_All = 15; //All orders have been cancelled, no transactions (This enum value is deprecated)
    OrderStatus_Failed = 21; //Order failed, refused by serser
    OrderStatus_Disabled = 22; //Order disabled (Actively operate a disabled order, this will not be submitted to the exchange)
    OrderStatus_Deleted = 23; //Deleted, only unfilled orders can be deleted (The status after you actively delete the order)
    OrderStatus_FillCancelled = 24; //The transaction is canceled (This enum value is deprecated)
}
```









**OrderStatus**



``` protobuf
enum OrderStatus
{
    OrderStatus_Unsubmitted = 0; //Unsubmitted (This enum value is deprecated)
    OrderStatus_Unknown = -1; //Unknown status
    OrderStatus_WaitingSubmit = 1; //Waiting to submit (Futu server has received your order and is preparing to submit it to the exchange)
    OrderStatus_Submitting = 2; //Queued  (Futu server has sent your order to the exchange, and the exchange is processing the order)
    OrderStatus_SubmitFailed = 3; //Submission failed (This enum value is deprecated)
    OrderStatus_TimeOut = 4; //Processing timed out, result unknown (This enum value is deprecated)
    OrderStatus_Submitted = 5; //Working, waiting to be filled (Your order has been successfully submitted to the exchange)
    OrderStatus_Filled_Part = 10; //Partially filled (The unfilled part of the order has not been cancelled. You can choose to cancel, or wait for fullly filled)
    OrderStatus_Filled_All = 11; //All filled
    OrderStatus_Cancelling_Part = 12; //Cancelling part of the order (One part of the order has been filled, and the rest is being cancelled) (This enum value is deprecated)
    OrderStatus_Cancelling_All = 13; //Cancelling the whole order (This enum value is deprecated)
    OrderStatus_Cancelled_Part = 14; //Part of the order is filled, and the remaining has been withdrawn (This enum value is deprecated)
    OrderStatus_Cancelled_All = 15; //All orders have been cancelled, no transactions (This enum value is deprecated)
    OrderStatus_Failed = 21; //Order failed, refused by serser
    OrderStatus_Disabled = 22; //Order disabled (Actively operate a disabled order, this will not be submitted to the exchange)
    OrderStatus_Deleted = 23; //Deleted, only unfilled orders can be deleted (The status after you actively delete the order)
    OrderStatus_FillCancelled = 24; //The transaction is canceled (This enum value is deprecated)
}
```









**OrderStatus**



``` protobuf
enum OrderStatus
{
    OrderStatus_Unsubmitted = 0; //Unsubmitted (This enum value is deprecated)
    OrderStatus_Unknown = -1; //Unknown status
    OrderStatus_WaitingSubmit = 1; //Waiting to submit (Futu server has received your order and is preparing to submit it to the exchange)
    OrderStatus_Submitting = 2; //Queued  (Futu server has sent your order to the exchange, and the exchange is processing the order)
    OrderStatus_SubmitFailed = 3; //Submission failed (This enum value is deprecated)
    OrderStatus_TimeOut = 4; //Processing timed out, result unknown (This enum value is deprecated)
    OrderStatus_Submitted = 5; //Working, waiting to be filled (Your order has been successfully submitted to the exchange)
    OrderStatus_Filled_Part = 10; //Partially filled (The unfilled part of the order has not been cancelled. You can choose to cancel, or wait for fullly filled)
    OrderStatus_Filled_All = 11; //All filled
    OrderStatus_Cancelling_Part = 12; //Cancelling part of the order (One part of the order has been filled, and the rest is being cancelled) (This enum value is deprecated)
    OrderStatus_Cancelling_All = 13; //Cancelling the whole order (This enum value is deprecated)
    OrderStatus_Cancelled_Part = 14; //Part of the order is filled, and the remaining has been withdrawn (This enum value is deprecated)
    OrderStatus_Cancelled_All = 15; //All orders have been cancelled, no transactions (This enum value is deprecated)
    OrderStatus_Failed = 21; //Order failed, refused by serser
    OrderStatus_Disabled = 22; //Order disabled (Actively operate a disabled order, this will not be submitted to the exchange)
    OrderStatus_Deleted = 23; //Deleted, only unfilled orders can be deleted (The status after you actively delete the order)
    OrderStatus_FillCancelled = 24; //The transaction is canceled (This enum value is deprecated)
}
```









## <a href="#245" class="header-anchor">#</a> Order Type



Tips

- [Order types supported in live
  trading](/moomoo-api-doc/en/qa/trade.html#7467).
- Paper trade only supports limit orders (NORMAL) and market orders
  (MARKET).







- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **OrderType**

- `NONE`

  Unknown type.

- `NORMAL`

  Limit orders.

- `MARKET`

  Market orders.

- `ABSOLUTE_LIMIT`

  Absolute limit orders.

  

  
  

  

  
  
  

  Only the price exactly matches before the transaction, otherwise the
  order will fail.
  - Example: For the next absolute limit buy order with a price of 5
    dollers, the seller's price must also be 5 dollers to complete the
    transaction. The seller cannot complete the transaction even if it
    is less than 5 yuan, and the order fails. The same goes for selling.

  

  

  

  

- `AUCTION`

  At-auction market orders.

  

  
  

  

  
  
  

  Valid for HK stocks early and closing auctions only

  

  

  

  

- `AUCTION_LIMIT`

  At-auction limit orders.

  

  
  

  

  
  
  

  Valid for HK stocks early and closing auctions only. Participate in
  the auction, and the specified price is required to be traded.

  

  

  

  

- `SPECIAL_LIMIT`

  Special limit orders.

  

  
  

  

  
  
  

  The transaction rules are the same as enhanced limit orders, and the
  exchange will automatically cancel the order after partial
  transaction.

  

  

  

  

- `SPECIAL_LIMIT_ALL`

  AON special limit orders.

  

  
  

  

  
  
  

  The order must be fully filled, otherwise cancelled automatically.

  

  

  

  

- `STOP`

  Stop orders.

- `STOP_LIMIT`

  Stop Limit orders.

- `MARKET_IF_TOUCHED`

  Market if Touched orders.

- `LIMIT_IF_TOUCHED`

  Limit if Touched orders.

- `TRAILING_STOP`

  Trailing Stop orders.

- `TRAILING_STOP_LIMIT`

  Trailing Stop Limit orders.

- `TWAP_LIMIT`

  Time Weighted Average Price Limit orders (HK and US securities only).

  

  
  

  

  
  
  

  Algo orders only support order queries and do not support trading.

  

  

  

  

- `TWAP`

  Time Weighted Average Price Market orders (US securities only).

  

  
  

  

  
  
  

  Algo orders only support order queries and do not support trading.

  

  

  

  

- `VWAP_LIMIT`

  Volume Weighted Average Price Limit orders (HK and US securities
  only).

  

  
  

  

  
  
  

  Algo orders only support order queries and do not support trading.

  

  

  

  

- `VWAP`

  Volume Weighted Average Price Market orders (US securities only).

  

  
  

  

  
  
  

  Algo orders only support order queries and do not support trading.

  

  

  

  





**OrderType**



``` protobuf
enum OrderType
{
    OrderType_Unknown = 0; //Unknown type
    OrderType_Normal = 1; //Normal orders
    OrderType_Market = 2; //Market order
    OrderType_AbsoluteLimit = 5; //Absolute limit order (Hong Kong stocks only), only the price exactly matches before the transaction, otherwise the order will fail. Example: For the next absolute limit buy order with a price of 5 dollers, the seller's price must also be 5 dollers to complete the transaction. The seller cannot complete the transaction even if it is less than 5 yuan, and the order fails. The same goes for selling.
    OrderType_Auction = 6; //Auction order (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only
    OrderType_AuctionLimit = 7; //Auction limit orders (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only. Participate in the auction, and the specified price is required to be traded
    OrderType_SpecialLimit = 8; //Special limit orders (Hong Kong stocks only), the transaction rules are the same as enhanced limit orders, and the exchange will automatically cancel the order after partial transaction
    OrderType_SpecialLimit_All = 9; //Special limit orders and all transaction orders are required (Hong Kong stocks only). All transaction orders are filled, otherwise cancelled automatically.
    OrderType_Stop = 10; // Stop orders
    OrderType_StopLimit = 11; // Stop Limit orders
    OrderType_MarketifTouched = 12; // Market if Touched orders
    OrderType_LimitifTouched = 13; // Limit if Touched orders
    OrderType_TrailingStop = 14; // Trailing Stop orders
    OrderType_TrailingStopLimit = 15; // Trailing Stop Limit orders
    OrderType_TWAP  = 16; // Time Weighted Average Price Market orders (US securities only)
    OrderType_TWAP_LIMIT = 17; // Time Weighted Average Price Limit orders (HK and US securities only)
    OrderType_VWAP  = 18; // Volume Weighted Average Price Market orders (US securities only)
    OrderType_VWAP_LIMIT  = 19; // Volume Weighted Average Price Limit orders (HK and US securities only)
}
```









**OrderType**



``` protobuf
enum OrderType
{
    OrderType_Unknown = 0; //Unknown type
    OrderType_Normal = 1; //Normal orders
    OrderType_Market = 2; //Market order
    OrderType_AbsoluteLimit = 5; //Absolute limit order (Hong Kong stocks only), only the price exactly matches before the transaction, otherwise the order will fail. Example: For the next absolute limit buy order with a price of 5 dollers, the seller's price must also be 5 dollers to complete the transaction. The seller cannot complete the transaction even if it is less than 5 yuan, and the order fails. The same goes for selling.
    OrderType_Auction = 6; //Auction order (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only
    OrderType_AuctionLimit = 7; //Auction limit orders (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only. Participate in the auction, and the specified price is required to be traded
    OrderType_SpecialLimit = 8; //Special limit orders (Hong Kong stocks only), the transaction rules are the same as enhanced limit orders, and the exchange will automatically cancel the order after partial transaction
    OrderType_SpecialLimit_All = 9; //Special limit orders and all transaction orders are required (Hong Kong stocks only). All transaction orders are filled, otherwise cancelled automatically.
    OrderType_Stop = 10; // Stop orders
    OrderType_StopLimit = 11; // Stop Limit orders
    OrderType_MarketifTouched = 12; // Market if Touched orders
    OrderType_LimitifTouched = 13; // Limit if Touched orders
    OrderType_TrailingStop = 14; // Trailing Stop orders
    OrderType_TrailingStopLimit = 15; // Trailing Stop Limit orders
    OrderType_TWAP  = 16; // Time Weighted Average Price Market orders (US securities only)
    OrderType_TWAP_LIMIT = 17; // Time Weighted Average Price Limit orders (HK and US securities only)
    OrderType_VWAP  = 18; // Volume Weighted Average Price Market orders (US securities only)
    OrderType_VWAP_LIMIT  = 19; // Volume Weighted Average Price Limit orders (HK and US securities only)
}
```









**OrderType**



``` protobuf
enum OrderType
{
    OrderType_Unknown = 0; //Unknown type
    OrderType_Normal = 1; //Normal orders
    OrderType_Market = 2; //Market order
    OrderType_AbsoluteLimit = 5; //Absolute limit order (Hong Kong stocks only), only the price exactly matches before the transaction, otherwise the order will fail. Example: For the next absolute limit buy order with a price of 5 dollers, the seller's price must also be 5 dollers to complete the transaction. The seller cannot complete the transaction even if it is less than 5 yuan, and the order fails. The same goes for selling.
    OrderType_Auction = 6; //Auction order (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only
    OrderType_AuctionLimit = 7; //Auction limit orders (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only. Participate in the auction, and the specified price is required to be traded
    OrderType_SpecialLimit = 8; //Special limit orders (Hong Kong stocks only), the transaction rules are the same as enhanced limit orders, and the exchange will automatically cancel the order after partial transaction
    OrderType_SpecialLimit_All = 9; //Special limit orders and all transaction orders are required (Hong Kong stocks only). All transaction orders are filled, otherwise cancelled automatically.
    OrderType_Stop = 10; // Stop orders
    OrderType_StopLimit = 11; // Stop Limit orders
    OrderType_MarketifTouched = 12; // Market if Touched orders
    OrderType_LimitifTouched = 13; // Limit if Touched orders
    OrderType_TrailingStop = 14; // Trailing Stop orders
    OrderType_TrailingStopLimit = 15; // Trailing Stop Limit orders
    OrderType_TWAP  = 16; // Time Weighted Average Price Market orders (US securities only)
    OrderType_TWAP_LIMIT = 17; // Time Weighted Average Price Limit orders (HK and US securities only)
    OrderType_VWAP  = 18; // Volume Weighted Average Price Market orders (US securities only)
    OrderType_VWAP_LIMIT  = 19; // Volume Weighted Average Price Limit orders (HK and US securities only)
}
```









**OrderType**



``` protobuf
enum OrderType
{
    OrderType_Unknown = 0; //Unknown type
    OrderType_Normal = 1; //Normal orders
    OrderType_Market = 2; //Market order
    OrderType_AbsoluteLimit = 5; //Absolute limit order (Hong Kong stocks only), only the price exactly matches before the transaction, otherwise the order will fail. Example: For the next absolute limit buy order with a price of 5 dollers, the seller's price must also be 5 dollers to complete the transaction. The seller cannot complete the transaction even if it is less than 5 yuan, and the order fails. The same goes for selling.
    OrderType_Auction = 6; //Auction order (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only
    OrderType_AuctionLimit = 7; //Auction limit orders (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only. Participate in the auction, and the specified price is required to be traded
    OrderType_SpecialLimit = 8; //Special limit orders (Hong Kong stocks only), the transaction rules are the same as enhanced limit orders, and the exchange will automatically cancel the order after partial transaction
    OrderType_SpecialLimit_All = 9; //Special limit orders and all transaction orders are required (Hong Kong stocks only). All transaction orders are filled, otherwise cancelled automatically.
    OrderType_Stop = 10; // Stop orders
    OrderType_StopLimit = 11; // Stop Limit orders
    OrderType_MarketifTouched = 12; // Market if Touched orders
    OrderType_LimitifTouched = 13; // Limit if Touched orders
    OrderType_TrailingStop = 14; // Trailing Stop orders
    OrderType_TrailingStopLimit = 15; // Trailing Stop Limit orders
    OrderType_TWAP  = 16; // Time Weighted Average Price Market orders (US securities only)
    OrderType_TWAP_LIMIT = 17; // Time Weighted Average Price Limit orders (HK and US securities only)
    OrderType_VWAP  = 18; // Volume Weighted Average Price Market orders (US securities only)
    OrderType_VWAP_LIMIT  = 19; // Volume Weighted Average Price Limit orders (HK and US securities only)
}
```







Tips

- Paper trade only supports limit orders (NORMAL) and market orders
  (MARKET).







**OrderType**



``` protobuf
enum OrderType
{
    OrderType_Unknown = 0; //Unknown type
    OrderType_Normal = 1; //Normal orders
    OrderType_Market = 2; //Market order
    OrderType_AbsoluteLimit = 5; //Absolute limit order (Hong Kong stocks only), only the price exactly matches before the transaction, otherwise the order will fail. Example: For the next absolute limit buy order with a price of 5 dollers, the seller's price must also be 5 dollers to complete the transaction. The seller cannot complete the transaction even if it is less than 5 yuan, and the order fails. The same goes for selling.
    OrderType_Auction = 6; //Auction order (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only
    OrderType_AuctionLimit = 7; //Auction limit orders (Hong Kong stocks only), valid for Hong Kong stocks early and closing auctions only. Participate in the auction, and the specified price is required to be traded
    OrderType_SpecialLimit = 8; //Special limit orders (Hong Kong stocks only), the transaction rules are the same as enhanced limit orders, and the exchange will automatically cancel the order after partial transaction
    OrderType_SpecialLimit_All = 9; //Special limit orders and all transaction orders are required (Hong Kong stocks only). All transaction orders are filled, otherwise cancelled automatically.
    OrderType_Stop = 10; // Stop orders
    OrderType_StopLimit = 11; // Stop Limit orders
    OrderType_MarketifTouched = 12; // Market if Touched orders
    OrderType_LimitifTouched = 13; // Limit if Touched orders
    OrderType_TrailingStop = 14; // Trailing Stop orders
    OrderType_TrailingStopLimit = 15; // Trailing Stop Limit orders
    OrderType_TWAP  = 16; // Time Weighted Average Price Market orders (US securities only)
    OrderType_TWAP_LIMIT = 17; // Time Weighted Average Price Limit orders (HK and US securities only)
    OrderType_VWAP  = 18; // Volume Weighted Average Price Market orders (US securities only)
    OrderType_VWAP_LIMIT  = 19; // Volume Weighted Average Price Limit orders (HK and US securities only)
}
```









## <a href="#7930" class="header-anchor">#</a> Position Direction





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **PositionSide**

- `NONE`

  Unknown position

- `LONG`

  Long position, by default

- `SHORT`

  Short position





**PositionSide**



``` protobuf
enum PositionSide
{
    PositionSide_Long = 0; //Long position, by default
    PositionSide_Unknown = -1; //Unknown position
    PositionSide_Short = 1; //Short position
}
```









**PositionSide**



``` protobuf
enum PositionSide
{
    PositionSide_Long = 0; //Long position, by default
    PositionSide_Unknown = -1; //Unknown position
    PositionSide_Short = 1; //Short position
}
```









**PositionSide**



``` protobuf
enum PositionSide
{
    PositionSide_Long = 0; //Long position, by default
    PositionSide_Unknown = -1; //Unknown position
    PositionSide_Short = 1; //Short position
}
```









**PositionSide**



``` protobuf
enum PositionSide
{
    PositionSide_Long = 0; //Long position, by default
    PositionSide_Unknown = -1; //Unknown position
    PositionSide_Short = 1; //Short position
}
```









**PositionSide**



``` protobuf
enum PositionSide
{
    PositionSide_Long = 0; //Long position, by default
    PositionSide_Unknown = -1; //Unknown position
    PositionSide_Short = 1; //Short position
}
```









## <a href="#7166" class="header-anchor">#</a> Account Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TrdAccType**

- `NONE`

  Unknown type

- `CASH`

  Cash account

- `MARGIN`

  Margin Account





**TrdAccType**



``` protobuf
enum TrdAccType
{
    TrdAccType_Unknown = 0; //Unknown type
    TrdAccType_Cash = 1; //Cash account
    TrdAccType_Margin = 2; //Margin account
};
```









**TrdAccType**



``` protobuf
enum TrdAccType
{
    TrdAccType_Unknown = 0; //Unknown type
    TrdAccType_Cash = 1; //Cash account
    TrdAccType_Margin = 2; //Margin account
};
```









**TrdAccType**



``` protobuf
enum TrdAccType
{
    TrdAccType_Unknown = 0; //Unknown type
    TrdAccType_Cash = 1; //Cash account
    TrdAccType_Margin = 2; //Margin account
};
```









**TrdAccType**



``` protobuf
enum TrdAccType
{
    TrdAccType_Unknown = 0; //Unknown type
    TrdAccType_Cash = 1; //Cash account
    TrdAccType_Margin = 2; //Margin account
};
```









**TrdAccType**



``` protobuf
enum TrdAccType
{
    TrdAccType_Unknown = 0; //Unknown type
    TrdAccType_Cash = 1; //Cash account
    TrdAccType_Margin = 2; //Margin account
};
```









## <a href="#48" class="header-anchor">#</a> Trading Environment





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TrdEnv**

- `SIMULATE`

  Simulated environment

- `REAL`

  Real environment





**TrdEnv**



``` protobuf
enum TrdEnv
{
    TrdEnv_Simulate = 0; //Simulated environment
    TrdEnv_Real = 1; //Real environment
}
```









**TrdEnv**



``` protobuf
enum TrdEnv
{
    TrdEnv_Simulate = 0; //Simulated environment
    TrdEnv_Real = 1; //Real environment
}
```









**TrdEnv**



``` protobuf
enum TrdEnv
{
    TrdEnv_Simulate = 0; //Simulated environment
    TrdEnv_Real = 1; //Real environment
}
```









**TrdEnv**



``` protobuf
enum TrdEnv
{
    TrdEnv_Simulate = 0; //Simulated environment
    TrdEnv_Real = 1; //Real environment
}
```









**TrdEnv**



``` protobuf
enum TrdEnv
{
    TrdEnv_Simulate = 0; //Simulated environment
    TrdEnv_Real = 1; //Real environment
}
```









## <a href="#6257" class="header-anchor">#</a> Transaction Market





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TrdMarket**

- `NONE`

  Unknown market

- `HK`

  Hong Kong market

- `US`

  US market

- `CN`

  A-share market

  

  
  

  

  
  
  

  The A-share market only supports paper trading, not live trading.

  

  

  

  

- `HKCC`

  HKCC market

  

  
  

  

  
  
  

  - The HKCC market only supports live trading, not paper trading.
  - The HKCC market can only trade Shanghai Stock Connect and Shenzhen
    Stock Connect stocks. For details, please refer to HKEX <a
    href="https://www.hkex.com.hk/mutual-market/stock-connect/eligible-stocks/%20view-all-eligible-securities?sc_lang=zh-HK"
    target="_blank" rel="noopener noreferrer">HKCC List</a>.

  

  

  

  

- `FUTURES`

  Futures market

- `FUTURES_SIMULATE_US`

  US futures simulated market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 7.7.3908

  

  

  

  

- `FUTURES_SIMULATE_HK`

  Hong Kong futures simulated market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 7.7.3908

  

  

  

  

- `FUTURES_SIMULATE_SG`

  Singapore futures simulated market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 7.7.3908

  

  

  

  

- `FUTURES_SIMULATE_JP`

  Japan futures simulated market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 7.7.3908

  

  

  

  

- `HKFUND`

  HK fund market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 8.2.4218

  

  

  

  

- `USFUND`

  US fund market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 8.2.4218

  

  

  

  

- `SG`

  SG market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 9.0.5008

  

  

  

  

- `JP`

  JP market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 9.0.5008

  

  

  

  

- `AU`

  AU market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 9.0.5008

  

  

  

  

- `MY`

  MY market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 9.0.5008

  

  

  

  

- `CA`

  CA market

  

  
  

  

  
  
  

  Minimum OpenD version requirements: 9.0.5008

  

  

  

  





**TrdMarket**



``` protobuf
enum TrdMarket
{
    TrdMarket_Unknown = 0; //Unknown market
    TrdMarket_HK = 1; //HK market (securities, options)
    TrdMarket_US = 2; //US market (securities, options)
    TrdMarket_CN = 3; //A-share market (only used in paper trading)
    TrdMarket_HKCC = 4; //HKCC market (stocks)
    TrdMarket_Futures = 5; //Futures market (global futures)
    TrdMarket_SG = 6; //SG market
    TrdMarket_AU = 8; //AU market
    TrdMarket_Futures_Simulate_HK = 10; //Hong Kong futures simulated market
    TrdMarket_Futures_Simulate_US = 11; //US futures simulated market
    TrdMarket_Futures_Simulate_SG = 12; //Singapore futures simulated market
    TrdMarket_Futures_Simulate_JP = 13; //Japan futures simulated market
    TrdMarket_JP = 15; //JP market
    TrdMarket_MY = 111; //MY market
    TrdMarket_CA = 112; //CA market
    TrdMarket_HK_Fund = 113; //Hong Kong fund market
    TrdMarket_US_Fund = 123; //US fund market
}
```









**TrdMarket**



``` protobuf
enum TrdMarket
{
    TrdMarket_Unknown = 0; //Unknown market
    TrdMarket_HK = 1; //HK market (securities, options)
    TrdMarket_US = 2; //US market (securities, options)
    TrdMarket_CN = 3; //A-share market (only used in paper trading)
    TrdMarket_HKCC = 4; //HKCC market (stocks)
    TrdMarket_Futures = 5; //Futures market (global futures)
    TrdMarket_SG = 6; //SG market
    TrdMarket_AU = 8; //AU market
    TrdMarket_Futures_Simulate_HK = 10; //Hong Kong futures simulated market
    TrdMarket_Futures_Simulate_US = 11; //US futures simulated market
    TrdMarket_Futures_Simulate_SG = 12; //Singapore futures simulated market
    TrdMarket_Futures_Simulate_JP = 13; //Japan futures simulated market
    TrdMarket_JP = 15; //JP market
    TrdMarket_MY = 111; //MY market
    TrdMarket_CA = 112; //CA market
    TrdMarket_HK_Fund = 113; //Hong Kong fund market
    TrdMarket_US_Fund = 123; //US fund market  
}
```









**TrdMarket**



``` protobuf
enum TrdMarket
{
    TrdMarket_Unknown = 0; //Unknown market
    TrdMarket_HK = 1; //HK market (securities, options)
    TrdMarket_US = 2; //US market (securities, options)
    TrdMarket_CN = 3; //A-share market (only used in paper trading)
    TrdMarket_HKCC = 4; //HKCC market (stocks)
    TrdMarket_Futures = 5; //Futures market (global futures)
    TrdMarket_SG = 6; //SG market
    TrdMarket_AU = 8; //AU market
    TrdMarket_Futures_Simulate_HK = 10; //Hong Kong futures simulated market
    TrdMarket_Futures_Simulate_US = 11; //US futures simulated market
    TrdMarket_Futures_Simulate_SG = 12; //Singapore futures simulated market
    TrdMarket_Futures_Simulate_JP = 13; //Japan futures simulated market
    TrdMarket_JP = 15; //JP market
    TrdMarket_MY = 111; //MY market
    TrdMarket_CA = 112; //CA market
    TrdMarket_HK_Fund = 113; //Hong Kong fund market
    TrdMarket_US_Fund = 123; //US fund market  
}
```









**TrdMarket**



``` protobuf
enum TrdMarket
{
    TrdMarket_Unknown = 0; //Unknown market
    TrdMarket_HK = 1; //HK market (securities, options)
    TrdMarket_US = 2; //US market (securities, options)
    TrdMarket_CN = 3; //A-share market (only used in paper trading)
    TrdMarket_HKCC = 4; //HKCC market (stocks)
    TrdMarket_Futures = 5; //Futures market (global futures)
    TrdMarket_SG = 6; //SG market
    TrdMarket_AU = 8; //AU market
    TrdMarket_Futures_Simulate_HK = 10; //Hong Kong futures simulated market
    TrdMarket_Futures_Simulate_US = 11; //US futures simulated market
    TrdMarket_Futures_Simulate_SG = 12; //Singapore futures simulated market
    TrdMarket_Futures_Simulate_JP = 13; //Japan futures simulated market
    TrdMarket_JP = 15; //JP market
    TrdMarket_MY = 111; //MY market
    TrdMarket_CA = 112; //CA market
    TrdMarket_HK_Fund = 113; //Hong Kong fund market
    TrdMarket_US_Fund = 123; //US fund market  
}
```









**TrdMarket**



``` protobuf
enum TrdMarket
{
    TrdMarket_Unknown = 0; //Unknown market
    TrdMarket_HK = 1; //HK market (securities, options)
    TrdMarket_US = 2; //US market (securities, options)
    TrdMarket_CN = 3; //A-share market (only used in paper trading)
    TrdMarket_HKCC = 4; //HKCC market (stocks)
    TrdMarket_Futures = 5; //Futures market (global futures)
    TrdMarket_SG = 6; //SG market
    TrdMarket_AU = 8; //AU market
    TrdMarket_Futures_Simulate_HK = 10; //Hong Kong futures simulated market
    TrdMarket_Futures_Simulate_US = 11; //US futures simulated market
    TrdMarket_Futures_Simulate_SG = 12; //Singapore futures simulated market
    TrdMarket_Futures_Simulate_JP = 13; //Japan futures simulated market
    TrdMarket_JP = 15; //JP market
    TrdMarket_MY = 111; //MY market
    TrdMarket_CA = 112; //CA market
    TrdMarket_HK_Fund = 113; //Hong Kong fund market
    TrdMarket_US_Fund = 123; //US fund market  
}
```









## <a href="#8311" class="header-anchor">#</a> Account Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TrdAccStatus**

- `ACTIVE`

  Active account

- `DISABLED`

  Disabled account





**TrdAccStatus**



``` protobuf
enum TrdAccStatus
{
    TrdAccStatus_Active = 0; //生效账户
    TrdAccStatus_Disabled = 1; //失效账户
}
```









**TrdAccStatus**



``` protobuf
enum TrdAccStatus
{
    TrdAccStatus_Active = 0; //生效账户
    TrdAccStatus_Disabled = 1; //失效账户
}
```









**TrdAccStatus**



``` protobuf
enum TrdAccStatus
{
    TrdAccStatus_Active = 0; //生效账户
    TrdAccStatus_Disabled = 1; //失效账户
}
```









**TrdAccStatus**



``` protobuf
enum TrdAccStatus
{
    TrdAccStatus_Active = 0; //生效账户
    TrdAccStatus_Disabled = 1; //失效账户
}
```









**TrdAccStatus**



``` protobuf
enum TrdAccStatus
{
    TrdAccStatus_Active = 0; //生效账户
    TrdAccStatus_Disabled = 1; //失效账户
}
```









## <a href="#8663" class="header-anchor">#</a> Account Structure





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TrdAccRole**

- `NONE`

  Unknown

- `MASTER`

  Master account

- `NORMAL`

  Normal account





**TrdAccRole**



``` protobuf
enum TrdAccRole
{
    TrdAccRole_Unknown = 0; //Unknown
    TrdAccRole_Normal = 1; //Normal account
    TrdAccRole_Master = 2; //Master account
}
```









**TrdAccRole**



``` protobuf
enum TrdAccRole
{
    TrdAccRole_Unknown = 0; //Unknown
    TrdAccRole_Normal = 1; //Normal account
    TrdAccRole_Master = 2; //Master account
}
```









**TrdAccRole**



``` protobuf
enum TrdAccRole
{
    TrdAccRole_Unknown = 0; //Unknown
    TrdAccRole_Normal = 1; //Normal account
    TrdAccRole_Master = 2; //Master account
}
```









**TrdAccRole**



``` protobuf
enum TrdAccRole
{
    TrdAccRole_Unknown = 0; //Unknown
    TrdAccRole_Normal = 1; //Normal account
    TrdAccRole_Master = 2; //Master account
}
```









**TrdAccRole**



``` protobuf
enum TrdAccRole
{
    TrdAccRole_Unknown = 0; //Unknown
    TrdAccRole_Normal = 1; //Normal account
    TrdAccRole_Master = 2; //Master account
}
```









## <a href="#4905" class="header-anchor">#</a> Transaction Securities Market





- Python
- Proto
- C#
- Java
- C++
- JavaScript









**TrdSecMarket**



``` protobuf
enum TrdSecMarket
{
    TrdSecMarket_Unknown = 0; //Unknown market
    TrdSecMarket_HK = 1; //Hong Kong (underlying stocks, warrants, etc.)
    TrdSecMarket_US = 2; //US (underlying stocks, options, futures etc.)
    TrdSecMarket_CN_SH = 31; //Shanghai (underlying stocks)
    TrdSecMarket_CN_SZ = 32; //Shenzhen (underlying stocks)
    TrdSecMarket_SG = 41; //Singapore (futures)
    TrdSecMarket_JP = 51; //Japanese (futures)
    TrdSecMarket_AU = 61; // Australia
    TrdSecMarket_MY = 71; // Malaysia
    TrdSecMarket_CA = 81; // Canada
    TrdSecMarket_FX = 91; // Forex
}
```









**TrdSecMarket**



``` protobuf
enum TrdSecMarket
{
    TrdSecMarket_Unknown = 0; //Unknown market
    TrdSecMarket_HK = 1; //Hong Kong (underlying stocks, warrants, etc.)
    TrdSecMarket_US = 2; //US (underlying stocks, options, futures etc.)
    TrdSecMarket_CN_SH = 31; //Shanghai (underlying stocks)
    TrdSecMarket_CN_SZ = 32; //Shenzhen (underlying stocks)
    TrdSecMarket_SG = 41; //Singapore (futures)
    TrdSecMarket_JP = 51; //Japanese (futures)
    TrdSecMarket_AU = 61; // Australia
    TrdSecMarket_MY = 71; // Malaysia
    TrdSecMarket_CA = 81; // Canada
    TrdSecMarket_FX = 91; // Forex
}
```









**TrdSecMarket**



``` protobuf
enum TrdSecMarket
{
    TrdSecMarket_Unknown = 0; //Unknown market
    TrdSecMarket_HK = 1; //Hong Kong (underlying stocks, warrants, etc.)
    TrdSecMarket_US = 2; //US (underlying stocks, options, futures etc.)
    TrdSecMarket_CN_SH = 31; //Shanghai (underlying stocks)
    TrdSecMarket_CN_SZ = 32; //Shenzhen (underlying stocks)
    TrdSecMarket_SG = 41; //Singapore (futures)
    TrdSecMarket_JP = 51; //Japanese (futures)
    TrdSecMarket_AU = 61; // Australia
    TrdSecMarket_MY = 71; // Malaysia
    TrdSecMarket_CA = 81; // Canada
    TrdSecMarket_FX = 91; // Forex
}
```









**TrdSecMarket**



``` protobuf
enum TrdSecMarket
{
    TrdSecMarket_Unknown = 0; //Unknown market
    TrdSecMarket_HK = 1; //Hong Kong (underlying stocks, warrants, etc.)
    TrdSecMarket_US = 2; //US (underlying stocks, options, futures etc.)
    TrdSecMarket_CN_SH = 31; //Shanghai (underlying stocks)
    TrdSecMarket_CN_SZ = 32; //Shenzhen (underlying stocks)
    TrdSecMarket_SG = 41; //Singapore (futures)
    TrdSecMarket_JP = 51; //Japanese (futures)
    TrdSecMarket_AU = 61; // Australia
    TrdSecMarket_MY = 71; // Malaysia
    TrdSecMarket_CA = 81; // Canada
    TrdSecMarket_FX = 91; // Forex
}
```









**TrdSecMarket**



``` protobuf
enum TrdSecMarket
{
    TrdSecMarket_Unknown = 0; //Unknown market
    TrdSecMarket_HK = 1; //Hong Kong (underlying stocks, warrants, etc.)
    TrdSecMarket_US = 2; //US (underlying stocks, options, futures etc.)
    TrdSecMarket_CN_SH = 31; //Shanghai (underlying stocks)
    TrdSecMarket_CN_SZ = 32; //Shenzhen (underlying stocks)
    TrdSecMarket_SG = 41; //Singapore (futures)
    TrdSecMarket_JP = 51; //Japanese (futures)
    TrdSecMarket_AU = 61; // Australia
    TrdSecMarket_MY = 71; // Malaysia
    TrdSecMarket_CA = 81; // Canada
    TrdSecMarket_FX = 91; // Forex
}
```









## <a href="#832" class="header-anchor">#</a> Transaction Direction





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TrdSide**

- `NONE`

  Unknown direction

- `BUY`

  Buy

- `SELL`

  Sell

- `SELL_SHORT`

  Sell short

- `BUY_BACK`

  Buy back





**TrdSide**



``` protobuf
enum TrdSide
{
    //The client places only Buy or Sell. SellShort is a direction returned by the US server. BuyBack does not currently exist, but it might be returned by the server.
    TrdSide_Unknown = 0; //Unknown direction
    TrdSide_Buy = 1; //Buy
    TrdSide_Sell = 2; //Sell
    TrdSide_SellShort = 3; //Sell short
    TrdSide_BuyBack = 4; //Buy Back
}
```









**TrdSide**



``` protobuf
enum TrdSide
{
    //The client places only Buy or Sell. SellShort is a direction returned by the US server. BuyBack does not currently exist, but it might be returned by the server.
    TrdSide_Unknown = 0; //Unknown direction
    TrdSide_Buy = 1; //Buy
    TrdSide_Sell = 2; //Sell
    TrdSide_SellShort = 3; //Sell short
    TrdSide_BuyBack = 4; //Buy Back
}
```









**TrdSide**



``` protobuf
enum TrdSide
{
    //The client places only Buy or Sell. SellShort is a direction returned by the US server. BuyBack does not currently exist, but it might be returned by the server.
    TrdSide_Unknown = 0; //Unknown direction
    TrdSide_Buy = 1; //Buy
    TrdSide_Sell = 2; //Sell
    TrdSide_SellShort = 3; //Sell short
    TrdSide_BuyBack = 4; //Buy Back
}
```









**TrdSide**



``` protobuf
enum TrdSide
{
    //The client places only Buy or Sell. SellShort is a direction returned by the US server. BuyBack does not currently exist, but it might be returned by the server.
    TrdSide_Unknown = 0; //Unknown direction
    TrdSide_Buy = 1; //Buy
    TrdSide_Sell = 2; //Sell
    TrdSide_SellShort = 3; //Sell short
    TrdSide_BuyBack = 4; //Buy Back
}
```









**TrdSide**



``` protobuf
enum TrdSide
{
    //The client places only Buy or Sell. SellShort is a direction returned by the US server. BuyBack does not currently exist, but it might be returned by the server.
    TrdSide_Unknown = 0; //Unknown direction
    TrdSide_Buy = 1; //Buy
    TrdSide_Sell = 2; //Sell
    TrdSide_SellShort = 3; //Sell short
    TrdSide_BuyBack = 4; //Buy Back
}
```











Tips

It is recommanded that only use `Buy` or `Sell` as the input parameter
of direction of **place_order** interface.  
`BuyBack` and `SellShort` is only used as the display field for **Get
Order List** , **Get History Order List**, **Orders Push Callback**,
**Get Today's Deals**, **Get Historical Deals** and **Deals Push
Callback** interface.



## <a href="#7678" class="header-anchor">#</a> Order Validity Period





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **TimeInForce**

- `DAY`

  Good for the day

- `GTC`

  Good until cancel





**TimeInForce**



``` protobuf
enum TimeInForce
{
    TimeInForce_DAY = 0; //Good for the day
    TimeInForce_GTC = 1; //Good until cancel, no more than 90 natural days
}
```









**TimeInForce**



``` protobuf
enum TimeInForce
{
    TimeInForce_DAY = 0; //Good for the day
    TimeInForce_GTC = 1; //Good until cancel, no more than 90 natural days
}
```









**TimeInForce**



``` protobuf
enum TimeInForce
{
    TimeInForce_DAY = 0; //Good for the day
    TimeInForce_GTC = 1; //Good until cancel, no more than 90 natural days
}
```









**TimeInForce**



``` protobuf
enum TimeInForce
{
    TimeInForce_DAY = 0; //Good for the day
    TimeInForce_GTC = 1; //Good until cancel, no more than 90 natural days
}
```









**TimeInForce**



``` protobuf
enum TimeInForce
{
    TimeInForce_DAY = 0; //Good for the day
    TimeInForce_GTC = 1; //Good until cancel, no more than 90 natural days
}
```









## <a href="#9434" class="header-anchor">#</a> Securities Firm to Which the Account Belongs





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SecurityFirm**

- `NONE`

  Unknown

- `FUTUSECURITIES`

  FUTU HK

- `FUTUINC`

  Moomoo US

- `FUTUSG`

  Moomoo SG

- `FUTUAU`

  Moomoo AU





**SecurityFirm**



``` protobuf
enum SecurityFirm
{
    SecurityFirm_Unknown = 0;        //Unknown
    SecurityFirm_FutuSecurities = 1; //FUTU HK
    SecurityFirm_FutuInc = 2;        //Moomoo US
    SecurityFirm_FutuSG = 3;         //Moomoo SG
    SecurityFirm_FutuAU = 4;         //Moomoo AU
}
```









**SecurityFirm**



``` protobuf
enum SecurityFirm
{
    SecurityFirm_Unknown = 0;        //Unknown
    SecurityFirm_FutuSecurities = 1; //FUTU HK
    SecurityFirm_FutuInc = 2;        //Moomoo US
    SecurityFirm_FutuSG = 3;         //Moomoo SG
    SecurityFirm_FutuAU = 4;         //Moomoo AU
}
```









**SecurityFirm**



``` protobuf
enum SecurityFirm
{
    SecurityFirm_Unknown = 0;        //Unknown
    SecurityFirm_FutuSecurities = 1; //FUTU HK
    SecurityFirm_FutuInc = 2;        //Moomoo US
    SecurityFirm_FutuSG = 3;         //Moomoo SG
    SecurityFirm_FutuAU = 4;         //Moomoo AU
}
```









**SecurityFirm**



``` protobuf
enum SecurityFirm
{
    SecurityFirm_Unknown = 0;        //Unknown
    SecurityFirm_FutuSecurities = 1; //FUTU HK
    SecurityFirm_FutuInc = 2;        //Moomoo US
    SecurityFirm_FutuSG = 3;         //Moomoo SG
    SecurityFirm_FutuAU = 4;         //Moomoo AU
}
```









**SecurityFirm**



``` protobuf
enum SecurityFirm
{
    SecurityFirm_Unknown = 0;        //Unknown
    SecurityFirm_FutuSecurities = 1; //FUTU HK
    SecurityFirm_FutuInc = 2;        //Moomoo US
    SecurityFirm_FutuSG = 3;         //Moomoo SG
    SecurityFirm_FutuAU = 4;         //Moomoo AU
}
```









## <a href="#7358" class="header-anchor">#</a> Simulate Account Type





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **SimAccType**

- `NONE`

  Unknown

- `STOCK`

  Stock simulation account

- `OPTION`

  Option simulation account

- `FUTURES`

  Futures simulation account





**SimAccType**



``` protobuf
enum SimAccType
{
    SimAccType_Unknown = 0;    //Unknown
      SimAccType_Stock = 1;        //Stock simulation account (used for trading securities only, does not support trading options)
      SimAccType_Option = 2;  //Option simulation account (used for trading options only, does not support trading of securities)
    SimAccType_Futures = 3;  //Futures simulation account
}
```









**SimAccType**



``` protobuf
enum SimAccType
{
    SimAccType_Unknown = 0;    //Unknown
      SimAccType_Stock = 1;        //Stock simulation account (used for trading securities only, does not support trading options)
      SimAccType_Option = 2;  //Option simulation account (used for trading options only, does not support trading of securities)
    SimAccType_Futures = 3;  //Futures simulation account
}
```









**SimAccType**



``` protobuf
enum SimAccType
{
    SimAccType_Unknown = 0;    //Unknown
      SimAccType_Stock = 1;        //Stock simulation account (used for trading securities only, does not support trading options)
      SimAccType_Option = 2;  //Option simulation account (used for trading options only, does not support trading of securities)
    SimAccType_Futures = 3;  //Futures simulation account
}
```









**SimAccType**



``` protobuf
enum SimAccType
{
    SimAccType_Unknown = 0;    //Unknown
      SimAccType_Stock = 1;        //Stock simulation account (used for trading securities only, does not support trading options)
      SimAccType_Option = 2;  //Option simulation account (used for trading options only, does not support trading of securities)
    SimAccType_Futures = 3;  //Futures simulation account
}
```









**SimAccType**



``` protobuf
enum SimAccType
{
    SimAccType_Unknown = 0;    //Unknown
      SimAccType_Stock = 1;        //Stock simulation account (used for trading securities only, does not support trading options)
      SimAccType_Option = 2;  //Option simulation account (used for trading options only, does not support trading of securities)
    SimAccType_Futures = 3;  //Futures simulation account
}
```









## <a href="#7469" class="header-anchor">#</a> Account Risk Control Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **CltRiskStatus**

- `NONE`

  Unknown

- `LEVEL1`

  Very Safe

- `LEVEL2`

  Safe

- `LEVEL3`

  Safe

- `LEVEL4`

  Low Risk

- `LEVEL5`

  Medium Risk

- `LEVEL6`

  High Risk

- `LEVEL7`

  Warning

- `LEVEL8`

  Margin Call

- `LEVEL9`

  Margin Call





**CltRiskStatus**



``` protobuf
enum CltRiskStatus
{
    CltRiskStatus_Level1 = 0;  //Very Safe
    CltRiskStatus_Level2 = 1;  //Safe
    CltRiskStatus_Level3 = 2;  //Safe
    CltRiskStatus_Level4 = 3;  //Low Risk
    CltRiskStatus_Level5 = 4;  //Medium Risk
    CltRiskStatus_Level6 = 5;  //High Risk
    CltRiskStatus_Level7 = 6;  //Warning
    CltRiskStatus_Level8 = 7;  //Margin Call
    CltRiskStatus_Level9 = 8;  //Margin Call
}
```









**CltRiskStatus**



``` protobuf
enum CltRiskStatus
{
    CltRiskStatus_Level1 = 0;  //Very Safe
    CltRiskStatus_Level2 = 1;  //Safe
    CltRiskStatus_Level3 = 2;  //Safe
    CltRiskStatus_Level4 = 3;  //Low Risk
    CltRiskStatus_Level5 = 4;  //Medium Risk
    CltRiskStatus_Level6 = 5;  //High Risk
    CltRiskStatus_Level7 = 6;  //Warning
    CltRiskStatus_Level8 = 7;  //Margin Call
    CltRiskStatus_Level9 = 8;  //Margin Call
}
```









**CltRiskStatus**



``` protobuf
enum CltRiskStatus
{
    CltRiskStatus_Level1 = 0;  //Very Safe
    CltRiskStatus_Level2 = 1;  //Safe
    CltRiskStatus_Level3 = 2;  //Safe
    CltRiskStatus_Level4 = 3;  //Low Risk
    CltRiskStatus_Level5 = 4;  //Medium Risk
    CltRiskStatus_Level6 = 5;  //High Risk
    CltRiskStatus_Level7 = 6;  //Warning
    CltRiskStatus_Level8 = 7;  //Margin Call
    CltRiskStatus_Level9 = 8;  //Margin Call
}
```









**CltRiskStatus**



``` protobuf
enum CltRiskStatus
{
    CltRiskStatus_Level1 = 0;  //Very Safe
    CltRiskStatus_Level2 = 1;  //Safe
    CltRiskStatus_Level3 = 2;  //Safe
    CltRiskStatus_Level4 = 3;  //Low Risk
    CltRiskStatus_Level5 = 4;  //Medium Risk
    CltRiskStatus_Level6 = 5;  //High Risk
    CltRiskStatus_Level7 = 6;  //Warning
    CltRiskStatus_Level8 = 7;  //Margin Call
    CltRiskStatus_Level9 = 8;  //Margin Call
}
```









**CltRiskStatus**



``` protobuf
enum CltRiskStatus
{
    CltRiskStatus_Level1 = 0;  //Very Safe
    CltRiskStatus_Level2 = 1;  //Safe
    CltRiskStatus_Level3 = 2;  //Safe
    CltRiskStatus_Level4 = 3;  //Low Risk
    CltRiskStatus_Level5 = 4;  //Medium Risk
    CltRiskStatus_Level6 = 5;  //High Risk
    CltRiskStatus_Level7 = 6;  //Warning
    CltRiskStatus_Level8 = 7;  //Margin Call
    CltRiskStatus_Level9 = 8;  //Margin Call
}
```









## <a href="#1018" class="header-anchor">#</a> Day-trading Status





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **DtStatus**

- `NONE`

  Unknown

- `Unlimited`

  Unlimited

  

  
  

  

  
  
  

  You can day trade for unlimited times. But you pay attention to your
  remaining day-trading buying power.

  

  

  

  

- `EM_Call`

  EM-Call

  

  
  

  

  
  
  

  You cannot initiate any new positions now. You should make your equity
  over \$25000, or you cannot initiate any new positions for 90 days.

  

  

  

  

- `DT_Call`

  DT-Call

  

  
  

  

  
  
  

  You have an unmet day-trading margin call. And you have five business
  days to deposit funds to meet the DT Call to get more DTBP. If your DT
  Call past due, you will not be allowed to initiate any new positions
  for 90 days until the DT call is met.

  

  

  

  





**DTStatus**



``` protobuf
enum DTStatus
{
    DTStatus_Unknown = 0;      //Unknown
    DTStatus_Unlimited = 1;        //Unlimited. You can day trade for unlimited times. But you pay attention to your remaining day-trading buying power.
    DTStatus_EMCall = 2;       //EM-Call. You cannot initiate any new positions now. You should make your equity over $25000, or you cannot initiate any new positions for 90 days.
    DTStatus_DTCall = 3;       //DT-Call. You have an unmet day-trading margin call. And you have five business days to deposit funds to meet the DT Call to get more DTBP. If your DT Call past due, you will not be allowed to initiate any new positions for 90 days until the DT call is met.
}
```









**DTStatus**



``` protobuf
enum DTStatus
{
    DTStatus_Unknown = 0;      //Unknown
    DTStatus_Unlimited = 1;        //Unlimited. You can day trade for unlimited times. But you pay attention to your remaining day-trading buying power.
    DTStatus_EMCall = 2;       //EM-Call.You cannot initiate any new positions now. You should make your equity over $25000, or you cannot initiate any new positions for 90 days.
    DTStatus_DTCall = 3;       //DT-Call. You have an unmet day-trading margin call. And you have five business days to deposit funds to meet the DT Call to get more DTBP. If your DT Call past due, you will not be allowed to initiate any new positions for 90 days until the DT call is met.
}
```









**DTStatus**



``` protobuf
enum DTStatus
{
    DTStatus_Unknown = 0;      //Unknown
    DTStatus_Unlimited = 1;        //Unlimited. You can day trade for unlimited times. But you pay attention to your remaining day-trading buying power.
    DTStatus_EMCall = 2;       //EM-Call.You cannot initiate any new positions now. You should make your equity over $25000, or you cannot initiate any new positions for 90 days.
    DTStatus_DTCall = 3;       //DT-Call. You have an unmet day-trading margin call. And you have five business days to deposit funds to meet the DT Call to get more DTBP. If your DT Call past due, you will not be allowed to initiate any new positions for 90 days until the DT call is met.
}
```









**DTStatus**



``` protobuf
enum DTStatus
{
    DTStatus_Unknown = 0;      //Unknown
    DTStatus_Unlimited = 1;        //Unlimited. You can day trade for unlimited times. But you pay attention to your remaining day-trading buying power.
    DTStatus_EMCall = 2;       //EM-Call.You cannot initiate any new positions now. You should make your equity over $25000, or you cannot initiate any new positions for 90 days.
    DTStatus_DTCall = 3;       //DT-Call. You have an unmet day-trading margin call. And you have five business days to deposit funds to meet the DT Call to get more DTBP. If your DT Call past due, you will not be allowed to initiate any new positions for 90 days until the DT call is met.
}
```









**DTStatus**



``` protobuf
enum DTStatus
{
    DTStatus_Unknown = 0;      //Unknown
    DTStatus_Unlimited = 1;        //Unlimited. You can day trade for unlimited times. But you pay attention to your remaining day-trading buying power.
    DTStatus_EMCall = 2;       //EM-Call.You cannot initiate any new positions now. You should make your equity over $25000, or you cannot initiate any new positions for 90 days.
    DTStatus_DTCall = 3;       //DT-Call. You have an unmet day-trading margin call. And you have five business days to deposit funds to meet the DT Call to get more DTBP. If your DT Call past due, you will not be allowed to initiate any new positions for 90 days until the DT call is met.
}
```









## <a href="#1384" class="header-anchor">#</a> Cash Flow Direction





- Python
- Proto
- C#
- Java
- C++
- JavaScript





> **CashFlowDirection**

- `NONE`

  Unknown

- `IN`

  Cash Inflow

- `OUT`

  Cash Outflow





**TrdCashFlowDirection**



``` protobuf
enum TrdCashFlowDirection
{
    TrdCashFlowDirection_Unknown = 0; //Unknown
    TrdCashFlowDirection_In = 1; //Cash Inflow
    TrdCashFlowDirection_Out = 2; //Cash Outflow
}
```









**TrdCashFlowDirection**



``` protobuf
enum TrdCashFlowDirection
{
    TrdCashFlowDirection_Unknown = 0; //Unknown
    TrdCashFlowDirection_In = 1; //Cash Inflow
    TrdCashFlowDirection_Out = 2; //Cash Outflow
}
```









**TrdCashFlowDirection**



``` protobuf
enum TrdCashFlowDirection
{
    TrdCashFlowDirection_Unknown = 0; //Unknown
    TrdCashFlowDirection_In = 1; //Cash Inflow
    TrdCashFlowDirection_Out = 2; //Cash Outflow
}
```









**TrdCashFlowDirection**



``` protobuf
enum TrdCashFlowDirection
{
    TrdCashFlowDirection_Unknown = 0; //Unknown
    TrdCashFlowDirection_In = 1; //Cash Inflow
    TrdCashFlowDirection_Out = 2; //Cash Outflow
}
```









**TrdCashFlowDirection**



``` protobuf
enum TrdCashFlowDirection
{
    TrdCashFlowDirection_Unknown = 0; //Unknown
    TrdCashFlowDirection_In = 1; //Cash Inflow
    TrdCashFlowDirection_Out = 2; //Cash Outflow
}
```









## <a href="#9120" class="header-anchor">#</a> Transaction Category

**TrdCategory**



``` protobuf
enum TrdCategory
{
    TrdCategory_Unknown = 0; //Unknown
    TrdCategory_Security = 1; //Securities
    TrdCategory_Future = 2; //Futures
}
```





## <a href="#4540" class="header-anchor">#</a> Account Cash Information

**AccCashInfo**



``` protobuf
message AccCashInfo
{
    optional int32 currency = 1; //Currency type, refer to Currency
    optional double cash = 2; //Cash balance
    optional double availableBalance = 3; //Available cash withdrawal amount
    optional double netCashPower = 4;        // Net cash power
}
```





## <a href="#7343" class="header-anchor">#</a> Account Assets Information by Market

**AccMarketInfo**



``` protobuf
message AccCashInfo
{
    optional int32 trdMarket = 1;        // Trading market, refer to TrdMarket
    optional double assets = 2;          // Account assets information by market
}
```





## <a href="#8729" class="header-anchor">#</a> Transaction Protocol Public Header

**TrdHeader**



``` protobuf
message TrdHeader
{
  required int32 trdEnv = 1; //Trading environment, refer to the enumeration definition of TrdEnv
  required uint64 accID = 2; //Trading account, trading account should match to trading environment and market permissions, otherwise an error will be returned
  required int32 trdMarket = 3; //Trading market, refer to the enumeration definition of TrdMarket
}
```





## <a href="#2879" class="header-anchor">#</a> Trading Account

**TrdAcc**



``` protobuf
message TrdAcc
{
  required int32 trdEnv = 1; //Trading environment, refer to the enumeration definition of TrdEnv
  required uint64 accID = 2; //Trading account
  repeated int32 trdMarketAuthList = 3; //The trading market permissions supported by the trading account, can have multiple trading market permissions, currently only a single, refer to the enumeration definition of TrdMarket
  optional int32 accType = 4; //Account type, refer to TrdAccType
  optional string cardNum = 5; //card number
  optional int32 securityFirm = 6; //security firm，refer to SecurityFirm
  optional int32 simAccType = 7; //simulate account type, see SimAccType
  optional string uniCardNum = 8; //Universal account number
  optional int32 accStatus = 9; //Account status，refer to TrdAccStatus
}
```





## <a href="#1356" class="header-anchor">#</a> Account Funds

**Funds**



``` protobuf
message Funds
{
  required double power = 1; //Maximum Buying Power (Minimum OpenD version requirements: 5.0.1310. This field is the approximate value calculated according to the marginable initial margin of 50%. But in fact, this ratio of each financial contract is not the same. We recommend using Buy on Margin, returned by Query the Maximum Quantity that Can be Bought or Sold, to get the maximum quantity can buy.) 
  required double totalAssets = 2; //Net Assets
  required double cash = 3; //Cash (Only Single market accounts use this field. If your account is an universial account, please use cashInfoList to get cash for each currency.)
  required double marketVal = 4; //Securities Market Value (only applicable to securities accounts)
  required double frozenCash = 5; //Funds on Hold 
  required double debtCash = 6; //Interest Charged Amount (Minimum OpenD version requirements: 5.0.1310) 
  required double avlWithdrawalCash = 7; //Withdrawable Cash (Only Single market accounts use this field. If your account is an universial account, please use cashInfoList to get withdrawalbe cash for each currency.)

  optional int32 currency = 8;            //The currency used for this query (only applicable to universal securities accounts and futures accounts). See Currency
  optional double availableFunds = 9;     //Available funds (only applicable to futures accounts)
  optional double unrealizedPL = 10;      //Unrealized gain or loss (only applicable to futures accounts)
  optional double realizedPL = 11;        //Realized gain or loss (only applicable to futures accounts)
  optional int32 riskLevel = 12;           //Risk control level (only applicable to futures accounts), See CltRiskLevel. It is recommanded to use riskStatus field to get the risk status of securities accounts or futures accounts.
  optional double initialMargin = 13;      //Initial Margin (only applicable to futures accounts, minimum OpenD version requirements: 5.0.1310)
  optional double maintenanceMargin = 14;  //Maintenance Margin (Minimum OpenD version requirements: 5.0.1310) 
  repeated AccCashInfo cashInfoList = 15;  //Cash information by currency (only applicable to futures accounts)
  optional double maxPowerShort = 16; //Short Buying Power (Minimum OpenD version requirements: 5.0.1310. This field is the approximate value calculated according to the shortable initial margin of 60%. But in fact, this ratio of each financial contract is not the same. We recommend using the Short sell field, returned by the API of Query the Maximum Quantity that Can be Bought or Sold, to get the maximum quantity can be shorted.) 
  optional double netCashPower = 17;  //Cash Buying Power （Only Single market accounts use this field. If your account is an universial account, please use cashInfoList to get cash buying power for each currency.）
  optional double longMv = 18;        //Long Market Value (Minimum OpenD version requirements: 5.0.1310) 
  optional double shortMv = 19;       //Short Market Value (Minimum OpenD version requirements: 5.0.1310) 
  optional double pendingAsset = 20;  //Asset in Transit (Minimum OpenD version requirements: 5.0.1310) 
  optional double maxWithdrawal = 21;          //Maximum Withdrawal (only applicable to securities accounts, minimum OpenD version requirements: 5.0.1310) 
  optional int32 riskStatus = 22;              //Risk status (only applicable to securities accounts, minimum OpenD version requirements: 5.0.1310), divided into 9 grades, LEVEL1 is the safest and LEVEL9 is the most dangerous. See CltRiskStatus
  optional double marginCallMargin = 23;       //Margin-call Margin (Minimum OpenD version requirements: 5.0.1310) 
  
  optional bool isPdt = 24;              //Is it marked as a PDT. True: It is a PDT.  False: Not a PDT. Only applicable to securities accounts of moomoo US. Minimum OpenD version requirements: 5.8.2008.
  optional string pdtSeq = 25;           //Day Trades Left. Only applicable to securities accounts of moomoo US. Minimum OpenD version requirements: 5.8.2008. 
  optional double beginningDTBP = 26;        //Beginning DTBP. Only applicable to securities accounts of moomoo US marked as a PDT. Minimum OpenD version requirements: 5.8.2008.
  optional double remainingDTBP = 27;        //Remaining DTBP. Only applicable to securities accounts of moomoo US marked as a PDT. Minimum OpenD version requirements: 5.8.2008.
  optional double dtCallAmount = 28;     //Day-trading Call Amount. Only applicable to securities accounts of moomoo US marked as a PDT. Minimum OpenD version requirements: 5.8.2008.
  optional int32 dtStatus = 29;              //Day-trading Status. Only applicable to securities accounts of moomoo US marked as a PDT. Minimum OpenD version requirements: 5.8.2008.
  
  optional double securitiesAssets = 30; // Net asset value of securities
  optional double fundAssets = 31; // Net asset value of fund
  optional double bondAssets = 32; // Net asset value of bond

repeated AccMarketInfo marketInfoList = 33; //Account assets information by market
}
```





## <a href="#5027" class="header-anchor">#</a> Account Holding

**Position**



``` protobuf
message Position
{
    required uint64 positionID = 1; //Position ID, a unique identifier of a position
    required int32 positionSide = 2; //Position direction, refer to the enumeration definition of PositionSide
    required string code = 3; //Code
    required string name = 4; //Name
    required double qty = 5; //Holding quantity, 2 decimal places, the same below
    required double canSellQty = 6; //Available quantity. Available quantity = Holding quantity - Frozen quantity. The unit of options and futures is "contract".
    required double price = 7; //Market price, 3 decimal places, 2 decimal places for futures
    optional double costPrice = 8; //Diluted Cost (for securities account). Average opening price (for futures account). No precision limit for securities. 2 decimal places for futures. If not passed, it means this value is invalid at this time.
    required double val = 9; //Market value, 3 decimal places, value of this field for futures is 0
    required double plVal = 10; //Amount of profit or loss, 3 decimal places,  2 decimal places for futures
    optional double plRatio = 11; //Percentage of profit or loss(under diluted cost price mode), no precision limit, if not passed, it means this value is invalid at this time
    optional int32 secMarket = 12; //The market to which the securities belong, refer to enumeration definition of TrdSecMarket
    
    //The following is the statistics of this position today
    optional double td_plVal = 21; //Today's profit or loss, 3 decimal places, the same below,  2 decimal places for futures
    optional double td_trdVal = 22; //Today's trading volume, not applicable for futures
    optional double td_buyVal = 23; //Total value bought today, not applicable for futures
    optional double td_buyQty = 24; //Total amount bought today, not applicable for futures
    optional double td_sellVal = 25; //Total value sold today, not applicable for futures
    optional double td_sellQty = 26; //Total amount sold today, not applicable for futures

    optional double unrealizedPL = 28; //Unrealized profit or loss (only applicable to futures accounts)
    optional double realizedPL = 29; //Realized profit or loss (only applicable to futures accounts)
    optional int32 currency = 30;        // Currency type, refer to Currency
    optional int32 trdMarket = 31;  //Trading market, refer to the enumeration definition of TrdMarket

    optional double dilutedCostPrice = 32;  //diluted cost price，applicable for securities accounts only
    optional double averageCostPrice = 33;  //average cost price，not applicable for securities papper trading accounts
    optional double averagePlRatio = 34;  //Percentage of profit or loss(under average cost price mode), no precision limit, if not passed, it means this value is invalid at this time
}
```





## <a href="#6192" class="header-anchor">#</a> Order

**Order**



``` protobuf
message Order
{
    required int32 trdSide = 1; //Trading direction, refer to TrdSide enumeration definition
    required int32 orderType = 2; //Order type, refer to enumeration definition of OrderType
    required int32 orderStatus = 3; //Order status, refer to enumeration definition of OrderStatus
    required uint64 orderID = 4; //Order number
    required string orderIDEx = 5; //Extended order number (only for checking the problem)
    required string code = 6; //code
    required string name = 7; //Name
    required double qty = 8; //Order quantity,  3 decimal places, option unit is "Zhang"
    optional double price = 9; //Order price, 3 decimal places
    required string createTime = 10; //Create time, strictly in accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS format
    required string updateTime = 11; //The last update time, strictly according to YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS format
    optional double fillQty = 12; //Filled quantity, 2 decimal place accuracy, the option unit is "contract"
    optional double fillAvgPrice = 13; //Average price of the fill, no precision limit
    optional string lastErrMsg = 14; //The last error description, if there is an error, there will be this description of the reason for the last error, no error is empty
    optional int32 secMarket = 15; //The market to which the securities belong, refer to enumeration definition of TrdSecMarket
    optional double createTimestamp = 16; //Timestamp for creation
    optional double updateTimestamp = 17; //Timestamp for last update
    optional string remark = 18; //User remark string, the maximum length is 64 bytes
    optional double auxPrice = 21; //Trigger price
    optional int32 trailType = 22; //Trailing type, see Trd_Common.TrailType enumeration definition
    optional double trailValue = 23; //Trailing amount / ratio
    optional double trailSpread = 24; //Specify spread
    optional int32 currency = 25;        // Currency type, refer to Currency
    optional int32 trdMarket = 26;  //Trading market, refer to the enumeration definition of TrdMarket
    optional int32 session = 27; //Trading session, refer to the enumeration definition of Session
}
```





## <a href="#88" class="header-anchor">#</a> Order Fee Item

**OrderFeeItem**



``` protobuf
message OrderFeeItem
{
    optional string title = 1; //Fee title
    optional double value = 2; //Fee Value
}
```





## <a href="#7615" class="header-anchor">#</a> Order Fee

**OrderFee**



``` protobuf
message OrderFee
{
    required string orderIDEx = 1; //Server order id
    optional double feeAmount = 2; //Fee amount
    repeated OrderFeeItem feeList = 3; //Fee details
}
```





## <a href="#9504" class="header-anchor">#</a> Order Fill

**OrderFill**



``` protobuf
message OrderFill
{
    required int32 trdSide = 1; //Trading direction, refer to enumeration definition of TrdSide
    required uint64 fillID = 2; //OrderFill ID
    required string fillIDEx = 3; //Extended OrderFill ID (only for checking the problem)
    optional uint64 orderID = 4; //Order ID
    optional string orderIDEx = 5; //Extended order ID (only when checking the problem)
    required string code = 6; //code
    required string name = 7; //Name
    required double qty = 8; //Filled quantity, 2 decimal place accuracy, the option unit is "contract"
    required double price = 9; //Price of the fill, 3 decimal places
    required string createTime = 10; //Create time (transaction time), in strict accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS format
    optional int32 counterBrokerID = 11; //Counter Broker ID, valid for Hong Kong stocks
    optional string counterBrokerName = 12; //Counter Broker Name, valid for Hong Kong stocks
    optional int32 secMarket = 13; //Securities belong to the market, refer to enumeration definition of TrdSecMarket
    optional double createTimestamp = 14; //Create a timestamp
    optional double updateTimestamp = 15; //last update timestamp
    optional int32 status = 16; //Deal status, refer to enumeration definition of OrderFillStatus
    optional int32 trdMarket = 17;  //Trading market, refer to enumeration definition of TrdMarket
}
```





## <a href="#8387" class="header-anchor">#</a> Maximum Trading Quantity

**MaxTrdQtys**



``` protobuf
message MaxTrdQtys
{
    //Due to the current server's implementation, it is required to sell the holding positions before a short selling, and to buy back short positions before a long buying (two steps). Nevertheless a bulish buying can be bought in one step with cash and financing. Please note this difference
    required double maxCashBuy = 1; //Buy on cash. (Maximum quantity that can be bought in cash. The unit of options is "contract".Futures accounts are not applicable.)
    optional double maxCashAndMarginBuy = 2; //Buy on margin. (Maximum quantity that can be bought on margin. The unit of options is "contract". Futures accounts are not applicable.)
    required double maxPositionSell = 3; //Sell on position. (Maximum quantity can be sold. The unit of options is "contract".)
    optional double maxSellShort = 4; //Short sell. (Maximum quantity can be shorted. The unit of options is "contract". Futures accounts are not applicable.)
    optional double maxBuyBack = 5; //Short positions. (Buyback required quantity to close a position. When holding short positions, you must first buy back the short positions before you can continue to buy long. The unit of options and futures is "contract".)
    optional double longRequiredIM = 6;         //Initial margin change when buying one contract of an asset. Only futures and options apply. No position: Returns the initial margin needed to buy one contract (a positive value).   Long position: Returns the initial margin required to buy one contract (a positive value). Short position: Returns the initial margin released for buying back one contract (a negative value). 
    optional double shortRequiredIM = 7;        //Initial margin change when selling one contract of an asset. Currently only futures and options apply. No position: Returns the initial margin needed to short one contract (a positive value). Long position: Returns the initial margin released for selling one contract (a negative value).  Short position: Returns the initial margin needed to short one contract (a positive value).
}
```





## <a href="#9686" class="header-anchor">#</a> Cash Flow Summary Info

**FlowSummaryInfo**



``` protobuf
message FlowSummaryInfo
{
    optional string clearingDate = 1; //clearing date
    optional string settlementDate = 2; //settlement date
    optional int32 currency = 3; //currency
    optional string cashFlowType = 4; //cash flow type
    optional int32 cashFlowDirection = 5; //cash flow direction, refer to TrdCashFlowDirection
    optional double cashFlowAmount = 6; //amount
    optional string cashFlowRemark = 7; //remark
    optional uint64 cashFlowID = 8; //cash flow ID
}
```





## <a href="#9070" class="header-anchor">#</a> Filter Conditions

**TrdFilterConditions**



``` protobuf
message TrdFilterConditions
{
  repeated string codeList = 1; //Code filtering, only returns the products for these codes, and this condition is ignored if it is not set
  repeated uint64 idList = 2; //ID primary key filter, only returns the products with these IDs, no filtering is not passed, orderID for order, fillID for deal, positionID for position
  optional string beginTime = 3; //Start time, strictly in accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS format. It is invalid for holding positions, and historical data must be filled in
  optional string endTime = 4; //The end time, strictly in accordance with YYYY-MM-DD HH:MM:SS or YYYY-MM-DD HH:MM:SS.MS format. It is invalid for holding positions, and historical data must be filled in
  repeated string orderIDExList = 5; // The server order id list, which can be used instead of orderID list, or choose one from orderID list
  optional int32 filterMarket = 6; //Trading market filter, refer to enumeration definition of TrdMarket
}
```











