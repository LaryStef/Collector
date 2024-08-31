from pydantic import BaseModel, Field


class Ticker(BaseModel):
    label: str = Field(alias="Label")
    price: float = Field(alias="Price")
    timestamp: int = Field(alias="Timestamp")
    volume: float = Field(alias="Volume_24h")


class CryptoData(BaseModel):
    Markets: list[Ticker]
