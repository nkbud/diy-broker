
# Account

## View Account Information
By sending a GET request to our /v2/account endpoint, you can see various information about your account, such as the amount of buying power available or whether or not it has a PDT flag.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))
```

## View Gain/Loss of Portfolio
You can use the information from the account endpoint to do things like calculating the daily profit or loss of your account.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# Get our account information.
account = trading_client.get_account()

# Check our current balance vs. our balance at the last market close
balance_change = float(account.equity) - float(account.last_equity)
print(f'Today\'s portfolio balance change: ${balance_change}')
```

## The Account object:
``` 
{
  "account_blocked": false,
  "account_number": "010203ABCD",
  "buying_power": "262113.632",
  "cash": "-23140.2",
  "created_at": "2019-06-12T22:47:07.99658Z",
  "currency": "USD",
  "crypto_status": "ACTIVE",
  "non_marginable_buying_power": "7386.56",
  "accrued_fees": "0",
  "pending_transfer_in": "0",
  "pending_transfer_out": "0",
  "daytrade_count": "0",
  "daytrading_buying_power": "262113.632",
  "equity": "103820.56",
  "id": "e6fe16f3-64a4-4921-8928-cadf02f92f98",
  "initial_margin": "63480.38",
  "last_equity": "103529.24",
  "last_maintenance_margin": "38000.832",
  "long_market_value": "126960.76",
  "maintenance_margin": "38088.228",
  "multiplier": "4",
  "pattern_day_trader": false,
  "portfolio_value": "103820.56",
  "regt_buying_power": "80680.36",
  "short_market_value": "0",
  "shorting_enabled": true,
  "sma": "0",
  "status": "ACTIVE",
  "trade_suspended_by_user": false,
  "trading_blocked": false,
  "transfers_blocked": false
}
```


| Attribute                          | Type                         | Description                                                                                                                                                                                                                                               |
|------------------------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                               | string                       | Account ID.                                                                                                                                                                                                                                               |
| `account_number`                   | string                       | Account number.                                                                                                                                                                                                                                           |
| `status`                           | string<account_status>       | See detailed account statuses below                                                                                                                                                                                                                      |
| `crypto_status`                    | string<account_status>       | The current status of the crypto enablement. See detailed crypto statuses below.                                                                                                                                                                          |
| `currency`                         | string                       | "USD"                                                                                                                                                                                                                                                    |
| `cash`                             | string                       | Cash balance                                                                                                                                                                                                                                             |
| `portfolio_value`                  | string                       | **[Deprecated]** Total value of cash + holding positions (Equivalent to the equity field)                                                                                                                                                                 |
| `non_marginable_buying_power`      | string                       | Current available non-margin dollar buying power                                                                                                                                                                                                         |
| `accrued_fees`                     | string                       | The fees collected.                                                                                                                                                                                                                                      |
| `pending_transfer_in`              | string                       | Cash pending transfer in.                                                                                                                                                                                                                                |
| `pending_transfer_out`             | string                       | Cash pending transfer out                                                                                                                                                                                                                                |
| `pattern_day_trader`               | boolean                      | Whether or not the account has been flagged as a pattern day trader                                                                                                                                                                                      |
| `trade_suspended_by_user`          | boolean                      | User setting. If `true`, the account is not allowed to place orders.                                                                                                                                                                                     |
| `trading_blocked`                  | boolean                      | If `true`, the account is not allowed to place orders.                                                                                                                                                                                                   |
| `transfers_blocked`                | boolean                      | If `true`, the account is not allowed to request money transfers.                                                                                                                                                                                        |
| `account_blocked`                  | boolean                      | If `true`, the account activity by user is prohibited.                                                                                                                                                                                                   |
| `created_at`                       | string                       | Timestamp this account was created at                                                                                                                                                                                                                    |
| `shorting_enabled`                | boolean                      | Flag to denote whether or not the account is permitted to short                                                                                                                                                                                          |
| `long_market_value`                | string                       | Real-time MtM value of all long positions held in the account                                                                                                                                                                                           |
| `short_market_value`               | string                       | Real-time MtM value of all short positions held in the account                                                                                                                                                                                          |
| `equity`                           | string                       | `cash` + `long_market_value` + `short_market_value`                                                                                                                                                                                                      |
| `last_equity`                      | string                       | Equity as of previous trading day at 16:00:00 ET                                                                                                                                                                                                         |
| `multiplier`                       | string                       | Buying power (BP) multiplier that represents account margin classification  Valid values:  - **1** (standard limited margin account with 1x BP),  - **2** (reg T margin account with 2x intraday and overnight BP; this is the default for all non-PDT accounts with $2,000 or more equity),  - **4** (PDT account with 4x intraday BP and 2x reg T overnight BP)  |
| `buying_power`                     | string                       | Current available $ buying power; If multiplier = 4, this is your daytrade buying power which is calculated as (last*equity - (last) maintenance_margin) * 4; If multiplier = 2, buying*power = max(equity – initial_margin,0) * 2; If multiplier = 1, buying_power = cash |
