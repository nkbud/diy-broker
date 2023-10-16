# Alpaca

alpaca-py: https://github.com/alpacahq/alpaca-py


## Live or Paper Trading

Every private API call requires key-based authentication. API keys can be acquired in the developer web console. The client must provide a pair of API key ID and secret key in the HTTP request headers named APCA-API-KEY-ID and APCA-API-SECRET-KEY, respectively.

```shell
curl -X GET \
    -H "APCA-API-KEY-ID: {YOUR_API_KEY_ID}"  
    -H "APCA-API-SECRET-KEY: {YOUR_API_SECRET_KEY}"  
    https://{apiserver_domain}/v2/account
```

| Account | URL                              |
|---------|----------------------------------|
| Live    | https://api.alpaca.markets       |
| Paper   | https://paper-api.alpaca.markets |


