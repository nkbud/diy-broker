# Orders

## Place New Orders
Orders can be placed with a POST request to our /v2/orders endpoint.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing market order
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )
```

## Submit Shorts
Short orders can also be placed for securities which you do not hold an open long position in.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )
```

## Using Client Order IDs
client_order_id can be used to organize and track specific orders in your client program. Unique client_order_ids for different strategies is a good way of running parallel algos across the same account.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=0.023,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    client_order_id='my_first_order',
                    )

# Market order
market_order = trading_client.submit_order(
                order_data=market_order_data
               )

# Get our order using its Client Order ID.
my_order = trading_client.get_order_by_client_id('my_first_order')
print('Got order #{}'.format(my_order.id))
```

## Submitting Bracket Orders
Bracket orders allow you to create a chain of orders that react to execution and stock price.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, TakeProfitRequest, StopLossRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# preparing bracket order with both stop loss and take profit
bracket__order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=5,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY,
                    order_class=OrderClass.BRACKET,
                    take_profit=TakeProfitRequest(400),
                    stop_loss=StopLossRequest(300)
                    )

bracket_order = trading_client.submit_order(
                order_data=bracket__order_data
               )
```

## Submitting Trailing Stop Orders
Trailing stop orders allow you to create a stop order that automatically changes the stop price allowing you to maximize your profits while still protecting your position with a stop price.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import TrailingStopOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

trading_client = TradingClient('api-key', 'secret-key', paper=True)

trailing_percent_data = TrailingStopOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.GTC,
                    trail_percent=1.00 # hwm * 0.99
                    )

trailing_percent_order = trading_client.submit_order(
                order_data=trailing_percent_data
               )
```

## Retrieve All Orders
If you’d like to see a list of your existing orders, you can send a GET request to our /v2/orders endpoint.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import QueryOrderStatus

trading_client = TradingClient('api-key', 'secret-key', paper=True)

# Get the last 100 closed orders
get_orders_data = GetOrdersRequest(
    status=QueryOrderStatus.CLOSED,
    limit=100,
    nested=True  # show nested multi-leg orders
)

trading_client.get_orders(filter=get_orders_data)
```

## Listen for Updates to Orders
You can use Websockets to receive real-time updates about the status of your orders as they change. 

```python
from alpaca.trading.stream import TradingStream

stream = TradingStream('api-key', 'secret-key', paper=True)

@conn.on(client_order_id)
async def on_msg(data):
    # Print the update to the console.
    print("Update for {}. Event: {}.".format(data.event))

stream.subscribe_trade_updates(on_msg)
# Start listening for updates.
stream.run()
```

