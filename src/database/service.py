from datetime import datetime
from uuid import uuid4

from sqlalchemy import Result, select
from sqlalchemy.orm import Session

from src.database import engine
from src.database.models import CryptoCourse, CryptoCurrency
from src.models import Coin


class CRUD():
    @staticmethod
    def get_all_tickers() -> list[str]:
        with Session(engine) as session:

            result: Result[tuple[CryptoCurrency]] = session.execute(
                select(CryptoCurrency.ticker)
            )

            return [ticker[0].lower() for ticker in result.fetchall()]

    def update_crypto(self, coin: Coin) -> None:
        with Session(engine) as session:
            hour: int = datetime.now().hour
            day: int = datetime.now().date().day
            month: int = datetime.now().month

            self._update_course(session, coin, type="hour", number=hour)

            if hour == 0:
                self._update_course(session, coin, type="day", number=day)

            if day == 1 or day == 16:
                self._update_course(
                    session,
                    coin,
                    type="month",
                    number=month * 2 if day == 16 else month * 2 - 1,
                )

            currency_raw: CryptoCurrency | None = session.query(
                CryptoCurrency).where(
                CryptoCurrency.ticker == coin.ticker).first()

            if currency_raw is not None:
                currency_raw.volume = coin.volume
            session.commit()

    @staticmethod
    def _update_course(
        session: Session,
        coin: Coin,
        *,
        type: str,
        number: int,
    ) -> None:
        course_raw: CryptoCourse | None = session.query(
            CryptoCourse).where(
            CryptoCourse.ticker == coin.ticker).where(
            CryptoCourse.type_ == type).where(
            CryptoCourse.number == number).first()

        if course_raw is not None:
            course_raw.price = round(coin.price, ndigits=2)
            return

        new_course: CryptoCourse = CryptoCourse(
            ID=uuid4().__str__(),
            ticker=coin.ticker,
            type_=type,
            number=number,
            price=round(coin.price, ndigits=2)
        )
        session.add(new_course)


CRUDobj: CRUD = CRUD()
