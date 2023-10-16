# Assets

## Get a List of Assets
If you send a GET request to our /v2/assets endpoint, you’ll receive a list of US equities.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

trading_client = TradingClient('api-key', 'secret-key')

# search for US equities
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)

assets = trading_client.get_all_assets(search_params)
```

## See If a Particular Asset is Tradable on Alpaca
By sending a symbol along with our request, we can get the information about just one asset. This is useful if we just want to make sure that a particular asset is tradable before we attempt to buy it.

```python
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('api-key', 'secret-key')

# search for AAPL
aapl_asset = trading_client.get_asset('AAPL')

if aapl_asset.tradable:
    print('We can trade AAPL.')
```