from datetime import datetime, UTC

from sqlalchemy import select, Result, Connection, ScalarResult
from sqlalchemy.orm import Session

from . import engine
from .models import CryptoCurrency, CryptoCourse
from ..models import Ticker
from ..generator import generate_id


class CRUD():
    @staticmethod
    def get_cryptocurrency_tickers() -> list[str]:
        with Session(engine) as session:

            result: Result[CryptoCurrency] = session.execute(
                select(CryptoCurrency.ticker)
            )

            return [ticker[0].lower() for ticker in result.fetchall()]

    @classmethod
    def update_crypto(cls, course: Ticker) -> None:
        with Session(engine) as session:
            hour: int = datetime.now(UTC).hour
            day: int = datetime.now(UTC).date().day
            month: int = datetime.now(UTC).month

            cls.update_course(session, course, type="hour", number=hour)

            if hour == 0:
                cls.update_course(session, course, type="day", number=day)

            if day == 1 or day == 16:
                cls.update_course(
                    session,
                    course,
                    type="month",
                    number=month,
                    extra="first" if day == 1 else "middle"
                )

            currency_raw: ScalarResult[CryptoCurrency] = session.query(
                CryptoCurrency).where(
                CryptoCurrency.ticker == course.label).first()

            currency_raw.volume = course.volume
            session.commit()

    def update_course(
        session: Connection,
        course: Ticker,
        *,
        type: str,
        number: int,
        extra: str = None
    ) -> None:
        course_raw: ScalarResult[CryptoCourse] | None = session.query(
            CryptoCourse).where(
            CryptoCourse.ticker == course.label).where(
            CryptoCourse.type_ == type).where(
            CryptoCourse.number == number).where(
            CryptoCourse.extra == extra).first()

        if course_raw is not None:
            course_raw.price = course.price
            return

        new_course: ScalarResult[CryptoCourse] = CryptoCourse(
            ID=generate_id(16),
            ticker=course.label,
            type_=type,
            number=number,
            extra=extra,
            price=course.price
        )
        session.add(new_course)
