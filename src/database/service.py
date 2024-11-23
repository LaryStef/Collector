from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import Result, select
from sqlalchemy.orm import Session

from src.database import engine
from src.database.models import CryptoCourse, CryptoCurrency
from src.models import Ticker


class CRUD():
    @staticmethod
    def get_cryptocurrency_tickers() -> list[str]:
        with Session(engine) as session:

            result: Result[tuple[CryptoCurrency]] = session.execute(
                select(CryptoCurrency.ticker)
            )

            return [ticker[0].lower() for ticker in result.fetchall()]

    def update_crypto(self, course: Ticker) -> None:
        with Session(engine) as session:
            hour: int = datetime.now(UTC).hour
            day: int = datetime.now(UTC).date().day
            month: int = datetime.now(UTC).month

            self.update_course(session, course, type="hour", number=hour)

            if hour == 0:
                self.update_course(session, course, type="day", number=day)

            if day == 1 or day == 16:
                self.update_course(
                    session,
                    course,
                    type="month",
                    number=month*2 if day == 16 else month*2-1,
                )

            currency_raw: CryptoCurrency | None = session.query(
                CryptoCurrency).where(
                CryptoCurrency.ticker == course.label).first()

            if currency_raw is not None:
                currency_raw.volume = course.volume
            session.commit()

    @staticmethod
    def update_course(
        session: Session,
        course: Ticker,
        *,
        type: str,
        number: int,
    ) -> None:
        course_raw: CryptoCourse | None = session.query(
            CryptoCourse).where(
            CryptoCourse.ticker == course.label).where(
            CryptoCourse.type_ == type).where(
            CryptoCourse.number == number).first()

        if course_raw is not None:
            course_raw.price = round(course.price, ndigits=2)
            return

        new_course: CryptoCourse = CryptoCourse(
            ID=uuid4().__str__(),
            ticker=course.label,
            type_=type,
            number=number,
            price=round(course.price, ndigits=2)
        )
        session.add(new_course)


CRUDobj: CRUD = CRUD()
