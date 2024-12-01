from os import getenv

from celery.schedules import crontab
from dotenv import load_dotenv


load_dotenv()

imports: list[str] = ["src.tasks"]
broker_url: str = f"redis://{getenv('REDIS_USER')}:{getenv('REDIS_PASSWORD')}@host.docker.internal:6379/0"  # noqa: E501
task_ignore_result: bool = True
task_time_limit: int = 10
timezone: str = "UTC"
broker_connection_retry_on_startup: bool = True
broker_transport_options: dict[str, int] = {
    "visibility_timeout": 43200
}
beat_schedule: dict[str, dict[str, str | crontab]] = {
        "collect-data": {
            "task": "src.tasks.collect_prices",
            "schedule": crontab(minute="*/2"),
        }
}
