from datetime import datetime, UTC

from sqlalchemy import select, Result
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

    @staticmethod
    def update_crypto(course: Ticker) -> None:
        with Session(engine) as session:
            hour: str = "hour" + str(datetime.now(UTC).hour)

            currency_raw: CryptoCurrency = session.query(
                CryptoCurrency).where(
                CryptoCurrency.ticker == course.label).first()

            currency_raw.volume = course.volume

            course_raw: CryptoCourse | None = session.query(
                CryptoCourse).where(
                CryptoCourse.ticker == course.label).where(
                CryptoCourse.time_frame == hour).first()

            if course_raw is not None:
                course_raw.price = course.price
                session.commit()
                return

            new_course: CryptoCourse = CryptoCourse(
                ID=generate_id(16),
                ticker=course.label,
                time_frame=hour,
                price=course.price
            )

            session.add(new_course)
            session.commit()
