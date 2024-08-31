# get out of here boy

from src.database.service import CRUD


class _Ticker():
    label: str
    price: float
    volume: float

    def __init__(self, ticker: str, price: float, volume: float):
        self.label = ticker
        self.price = price,
        self.volume = volume


obj = _Ticker(ticker="BTC", price=42351.12, volume=1232316542)
CRUD.update_crypto(obj)
