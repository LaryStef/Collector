from src.ticker_id import TickerID


class RequestUrl():
    def __init__(self, tickers: list[str]) -> None:
        self.__url = (
            f"https://api.coinlore.net/api/ticker/?id={",".join([str(getattr(TickerID, ticker.upper())) for ticker in tickers])}"  # noqa E501
        )

    def get_url(self) -> str:
        return self.__url
