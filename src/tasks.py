from typing import Any
from logging import Logger, getLogger

import requests
from pydantic import ValidationError

from src import celery
from src.database.service import CRUDobj
from src.models import coin_list, Coin
from src.url import RequestUrl


logger: Logger = getLogger(__name__)


@celery.task(
    bind=True,
    max_retries=3,
    default_retry_delay=30,
    time_limit=15
)
def collect_prices(self: Any) -> None:
    requestUrl: RequestUrl = RequestUrl(
        tickers=CRUDobj.get_all_tickers()
    )

    r: requests.Response = requests.get(requestUrl.get_url())
    if (r.status_code != 200):
        logger.error("Request has status code different from 200")
        self.retry()

    try:
        price_data: list[Coin] = coin_list.validate_json(r.text)
    except ValidationError:
        logger.error("Api response is not valid")
        self.retry()

    for coin in price_data:
        CRUDobj.update_crypto(coin)
    logger.info("Prices updated successfully")
