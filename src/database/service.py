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

            result: Result = session.execute(
                select(CryptoCurrency.ticker)
            )

            return [ticker[0].lower() for ticker in result.fetchall()]

    @classmethod
    def update_crypto(cls, course: Ticker) -> None:
        with Session(engine) as session:
            hour: str = "hour" + str(datetime.now(UTC).hour)
            day: str = "day" + str(datetime.now(UTC).date().day)
            month: str = "month" + str(datetime.now(UTC).date().month)

            cls.update_course(session, course, hour)

            if hour == "hour0":
                cls.update_course(session, course, day)

            if day == "day1" or day == "day16":
                if day == "day1":
                    month += "fst"
                elif day == "day16":
                    month += "mid"

                cls.update_course(session, course, month)

            currency_raw: ScalarResult[CryptoCurrency] = session.query(
                CryptoCurrency).where(
                CryptoCurrency.ticker == course.label).first()

            currency_raw.volume = course.volume
            session.commit()

    def update_course(session: Connection, course: Ticker, time: str) -> None:
        course_raw: ScalarResult[CryptoCourse] | None = session.query(
            CryptoCourse).where(
            CryptoCourse.ticker == course.label).where(
            CryptoCourse.time_frame == time).first()

        if course_raw is not None:
            course_raw.price = course.price
            return

        new_course: ScalarResult[CryptoCourse] = CryptoCourse(
            ID=generate_id(16),
            ticker=course.label,
            time_frame=time,
            price=course.price
        )
        session.add(new_course)
