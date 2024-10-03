from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import Connection, Result, ScalarResult, select
from sqlalchemy.orm import Session

from database import engine
from database.models import CryptoCourse, CryptoCurrency
from src.models import Ticker


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
                    number=month*2 if day == 16 else month*2-1,
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
    ) -> None:
        course_raw: ScalarResult[CryptoCourse] | None = session.query(
            CryptoCourse).where(
            CryptoCourse.ticker == course.label).where(
            CryptoCourse.type_ == type).where(
            CryptoCourse.number == number).first()

        if course_raw is not None:
            course_raw.price = course.price
            return

        new_course: ScalarResult[CryptoCourse] = CryptoCourse(
            ID=uuid4().__str__(),
            ticker=course.label,
            type_=type,
            number=number,
            price=course.price
        )
        session.add(new_course)
