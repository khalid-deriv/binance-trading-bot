from binance.spot import Spot as Client

client = Client(base_url="https://testnet.binance.vision")
print(client.time())

# Post a new order
params = {
    "symbol": "BTCUSDT",
    "side": "SELL",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 0.002,
    "price": 9500
}

response = client.new_order(params)
print(response)