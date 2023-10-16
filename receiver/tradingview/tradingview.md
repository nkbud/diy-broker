# Tradingview Webhooks

The first order maker we will receive is Tradingview. 
More info on that.

## Tradingview Variables

| variable                         | example       | default behavior                                   |
|----------------------------------|---------------|----------------------------------------------------|
| {{**ticker**}}                   | AAPL          | **required**                                       |
| {{**strategy.order.action**}}    | "buy", "sell" | "sell" if you have some or "buy" if none.          |
| {{**strategy.order.price**}}     | 123.4567      | "sell" to the highest bid or "buy" the lowest ask. |
| {{**strategy.order.contracts**}} | 0.123         | 100% of available equity, "buy" or "sell"          |


## Default Behaviors

| variable                     | default  |
|------------------------------|----------|
| {{**strategy.order.action**}}    |          |
| {{**strategy.order.price**}}     | 123.4567 |


- {{exchange}} + {{ticker}} = unique id of the stock
- {{strategy.order.action}} = action to take on the stock
- {{strategy.order.price}} = price to take action

## Tradingview Variables - Recommended



| variable                     | example              |
|------------------------------|----------------------|
| {{exchange}}                 | NASDAQ               | 
| {{strategy.order.price}}     | 123.4567             |
| {{strategy.market_position}} | "long", "short"      |
| {{timenow}}                  | 2020-09-06T01:44:17Z |





## Security

Your function is publicly accessible. 
We'll guard it using https encryption plus a password.

- passphrase: "abcdefgh"



Tradingview expected json format:
```
{
    "open": {{open}},
    "high": {{high}},
    "low": {{low}},
    "close": {{close}},
    "exchange": "{{exchange}}",
    "ticker": "{{ticker}}",
    "volume": {{volume}},
    "time": "{{time}}",
    "timenow": "{{timenow}}"
}
```


example webhook
```
{
    "passphrase": "abcdefgh",
    "time": "2020-09-06T01:44:17Z",
    "exchange": "BINANCE",
    "ticker": "DOGEUSDT",
    "bar": {
        "time": "2020-09-06T01:43:00Z",
        "open": 0.002748,
        "high": 0.0027486,
        "low": 0.002748,
        "close": 0.0027486,
        "volume": 150177
    },
    "strategy": {
        "position_size": 10000,
        "order_action": "buy",
        "order_contracts": 10000,
        "order_price": 0.0027451,
        "order_id": "doge door",
        "market_position": "long",
        "market_position_size": 10000,
        "prev_market_position": "flat",
        "prev_market_position_size": 0
    }
}
```

format
``` 
{
    "passphrase": "abcdefgh",
    "time": "{{timenow}}",
    "exchange": "{{exchange}}",
    "ticker": "{{ticker}}",
    "bar": {
        "time": "{{time}}",
        "open": {{open}},
        "high": {{high}},
        "low": {{low}},
        "close": {{close}},
        "volume": {{volume}}
    },
    "strategy": {
        "position_size": {{strategy.position_size}},
        "order_action": "{{strategy.order.action}}",
        "order_contracts": {{strategy.order.contracts}},
        "order_price": {{strategy.order.price}},
        "order_id": "{{strategy.order.id}}",
        "market_position": "{{strategy.market_position}}",
        "market_position_size": {{strategy.market_position_size}},
        "prev_market_position": "{{strategy.prev_market_position}}",
        "prev_market_position_size": {{strategy.prev_market_position_size}}
    }
}
```

Here is a list of available placeholders:


3. {{close}}, {{open}}, {{high}}, {{low}}, {{time}}, {{volume}} - corresponding values of the bar on which the alert has been triggered. Note that alerts on indicators, non-standard charts and drawings depends on a resolution, while simple price alerts (e.g., price crossing some value) are always calculated on 1-minute bars. {{time}} is in UTC, formatted as yyyy-MM-ddTHH:mm:ssZ. For example, 2019-08-27T09:56:00Z. Other values are fixed-point numbers with a decimal point separating the integral and fractional parts. For example, 1245.25.

4. {{timenow}} - current fire time of the alert, formatted in the same way as {{time}}. Return time to the nearest second, regardless of the resolution.

5. {{plot_0}}, {{plot_1}}, ... {{plot_19}} - corresponding output series of an indicator used in the alert. Note that the plots are numbered from zero. The highest plot ID is 19 (you can access only 20 first output series). Output series are the values of an indicator you can see on a chart. For example, the built-in volume indicator has two output series: Volume and Volume MA. You can create an alert on it and type in a message box something like this:

Volume: {{plot_0}}, Volume average: {{plot_1}}

6. {{interval}} - returns the interval (i.e. timeframe/resolution) of the chart that the alert is created on. Note that, for technical reasons, in some cases, this placeholder will return “1” instead of the timeframe on the chart. Regular price-based alerts (with conditions such as “AAPL Crossing 120” or “AMZN Greater Than 3600”) are all based on the symbol’s last value, so the timeframe of the chart is not relevant for the alert. Because of that, all price-based alerts are actually calculated on the 1m timeframe and the placeholder will always return “1” accordingly. Additionally, Range charts are also calculated based on 1m data so the {{interval}} placeholder will always return “1” on any alert created on a Range chart. With alerts created on drawings and indicators, this placeholder will function as expected.

Placeholders with the "strategy" prefix can only be used in strategy alerts:

{{strategy.position_size}} - returns the value of the same keyword in Pine, i.e., the size of the current position.
{{strategy.order.action}} - returns the string “buy” or “sell” for the executed order.
{{strategy.order.contracts}} - returns the number of contracts of the executed order.
{{strategy.order.price}} - returns the price at which the order was executed.
{{strategy.order.id}} - returns the ID of the executed order (the string used as the first parameter in one of the function calls generating orders: strategy.entry, strategy.exit or strategy.order).
{{strategy.order.comment}} - returns the comment of the executed order (the string used in the comment parameter in one of the function calls generating orders: strategy.entry, strategy.exit or strategy.order). If no comment is specified, then the value of strategy.order.id will be used.
{{strategy.order.alert_message}} - returns the value of the alert_message parameter which can be used in the strategy's Pine code when calling one of the functions used to place orders: strategy.entry, strategy.exit or strategy.order. This feature is only supported in Pine v4 and higher.
{{strategy.market_position}} - returns the current position of the strategy in string form: “long”, “flat”, or “short”.
{{strategy.market_position_size}} - returns the size of the current position as an absolute value, i.e. a non-negative number.
{{strategy.prev_market_position}} - returns the previous position of the strategy in string form: “long”, “flat”, or “short”.
{{strategy.prev_market_position_size}} - returns the size of the previous position as an absolute value, i.e. a non-negative number.
{{syminfo.currency}} - returns the currency code of the current symbol (“EUR”, “USD”, etc.).
{{syminfo.basecurrency}} - returns the base currency code of the current symbol if the symbol refers to a currency pair. Otherwise, it returns na. For example, it returns “EUR” when the symbol is “EURUSD”.