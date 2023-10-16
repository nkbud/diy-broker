# Positions

You can view the positions in your portfolio by making a GET request to the /v2/positions endpoint. If you specify a symbol, you’ll see only your position for the associated stock.

```python
from alpaca.trading.client import TradingClient

trading_client = TradingClient('api-key', 'secret-key')

# Get our position in AAPL.
aapl_position = trading_client.get_open_position('AAPL')

# Get a list of all of our positions.
portfolio = trading_client.get_all_positions()

# Print the quantity of shares for each position.
for position in portfolio:
    print("{} shares of {}".format(position.qty, position.symbol))
```

The current price reflected will be based on the following:

- 4:00 am ET - 9:30 am ET - Last trade based on the premarket
- 9:30 am ET - 4pm ET - Last trade
- 4:00 pm ET - 10:00 pm ET - Last trade based on after-hours trading
- 10 pm ET - 4:00 am ET next trading day - Official closing price from the primary exchange at 4 pm ET.
