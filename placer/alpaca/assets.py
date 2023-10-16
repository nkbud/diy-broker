import json
import logging
import os

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass, AssetStatus

logger = logging.getLogger()
logger.setLevel(logging.INFO)

api_key = os.getenv('ALPACA_PAPER_API_KEY')
secret_key = os.getenv('ALPACA_PAPER_SECRET_KEY')
trading_client = TradingClient(api_key=api_key, secret_key=secret_key, paper=True)

if __name__ == "__main__":
    account = trading_client.get_account()
    print('${} is available as buying power.'.format(account.buying_power))
    # with open("data-out/account.json", "w") as f:
    #     f.write(account.model_dump_json(indent=2))

    # search for US equities
    search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY, status=AssetStatus.ACTIVE)
    assets = trading_client.get_all_assets(search_params)
    print('{} assets are available for trading.'.format(len(assets)))
    # with open("data-out/assets.json", "w") as f:
    #     f.write(account.model_dump_json(indent=2))
    with open("data-out/assets.csv", "w") as f:
        columns="Symbol,Tradable,Shortable,Fractionable,EasyToBorrow"
        print(columns)
        f.write(f"{columns}\n")
        for x in assets:
            line = f'{x.exchange}:{x.symbol},"{x.name}",{x.tradable},{x.shortable},{x.fractionable},{x.easy_to_borrow}'
            line = line.replace("\ufffd", "?")
            print(line)
            f.write(f"{line}\n")