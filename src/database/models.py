from sqlalchemy import Float, ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class CryptoCurrency(Base):
    __tablename__: str = "cryptocurrency"

    ticker: Mapped[str] = mapped_column(String(8), primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(4096))
    volume: Mapped[float] = mapped_column(Float, default=0)
    crypto_course: Mapped[list["CryptoCourse"]] = relationship()


class CryptoCourse(Base):
    __tablename__: str = "CryptoCourse"

    ID: Mapped[str] = mapped_column(String(16), primary_key=True)
    ticker: Mapped[str] = mapped_column(ForeignKey("Cryptocurrency.ticker"))
    price: Mapped[float] = mapped_column(Float, default=0)
    type_: Mapped[str] = mapped_column("type", String(8))
    number: Mapped[int] = mapped_column(Integer)

    def __init__(
        self,
        *,
        ID: str,
        ticker: str,
        price: float,
        type_: str,
        number: int,
    ) -> None:
        self.ID = ID
        self.ticker = ticker
        self.price = price
        self.type_ = type_
        self.number = number
