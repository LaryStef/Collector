class RequestUrl():
    def __init__(self, api_key: str, tickers: list[str]) -> None:
        self.__url = f"https://www.worldcoinindex.com/apiservice/ticker?key={api_key}&label={"btc-".join(tickers) + "btc"}&fiat=usd"  # noqa E501

    def get_url(self) -> str:
        return self.__url
