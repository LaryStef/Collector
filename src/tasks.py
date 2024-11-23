from typing import Any

import requests
from pydantic import ValidationError

from src import celery
from src.config import settings
from src.database.service import CRUDobj
from src.models import CryptoData
from src.url import RequestUrl


@celery.task(
    bind=True,
    max_retries=3,
    default_retry_delay=30,
    time_limit=15
)
def collect_prices(self: Any) -> None:
    requestUrl: RequestUrl = RequestUrl(
        api_key=settings.API_KEY,
        tickers=CRUDobj.get_cryptocurrency_tickers()
    )

    r: requests.Response = requests.get(requestUrl.get_url())

    if (r.status_code != 200):
        self.retry()

    try:
        courses: CryptoData = CryptoData.model_validate_json(r.text)
    except ValidationError:
        self.retry()

    for course in courses.Markets:
        course.label = course.label.split("/")[0]
        CRUDobj.update_crypto(course)
