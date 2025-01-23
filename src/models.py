from pydantic import BaseModel, Field, TypeAdapter


class Coin(BaseModel):
    ticker: str = Field(alias="symbol")
    price: float = Field(alias="price_usd")
    volume: float = Field(alias="volume24")


coin_list: TypeAdapter = TypeAdapter(list[Coin])
