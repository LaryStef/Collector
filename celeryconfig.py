from celery.schedules import crontab


imports: list[str] = ["src.tasks"]
broker_url: str = "redis://localhost:6379/0"
task_ignore_result: bool = True
task_time_limit: int = 10
timezone: str = "UTC"

# worker_logfile: str = "./logs/app.log"
# worker_hijack_root_logger: bool = False
# worker_redirect_stdouts: bool = True
# worker_log_format = "[%(asctime)s] [%(levelname)s] [%(task_name)s] %(message)s"

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
