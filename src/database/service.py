from sqlalchemy import select, Result

from . import engine
from .models import CryptoCurrency


class CRUD():
    @staticmethod
    def get_cryptocurrency_tickers() -> list[str]:
        with engine.connect() as session:

            result: Result = session.execute(
                select(CryptoCurrency.ticker)
            )

            return [ticker[0].lower() for ticker in result.fetchall()]
