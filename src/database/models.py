from sqlalchemy import Float, ForeignKey, String
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
    __tablename__: str = "crypto_course"

    ID: Mapped[str] = mapped_column(String(16), primary_key=True)
    ticker: Mapped[str] = mapped_column(ForeignKey("cryptocurrency.ticker"))
    time_frame: Mapped[str] = mapped_column(String(16))
    price: Mapped[float] = mapped_column(Float, default=0)
