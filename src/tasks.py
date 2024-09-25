import requests
from pydantic import ValidationError

from src import celery
from src.config import API_KEY
from src.database.service import CRUD
from src.models import CryptoData


@celery.task(
    bind=True,
    max_retries=3,
    default_retry_delay=30,
    time_limit=15
)
def collect_prices(self) -> None:
    tickers: list[str] = CRUD.get_cryptocurrency_tickers()

    r: requests.Response = requests.get(url=f"https://www.worldcoinindex.com/apiservice/ticker?key={API_KEY}&label={"btc-".join(tickers) + "btc"}&fiat=usd")  # noqa E501

    if (r.status_code != 200):
        self.retry()

    try:
        courses: CryptoData = CryptoData.model_validate_json(r.text)
    except ValidationError:
        self.retry()

    for course in courses.Markets:
        course.label = course.label.split("/")[0]
        CRUD.update_crypto(course)
