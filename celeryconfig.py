from celery.schedules import crontab


broker_url: str = "redis://localhost:6379/0"
task_ignore_result: bool = True
task_time_limit: int = 10
timezone: str = "UTC"
worker_logfile: str = "cryptodeal.log"
worker_hijack_root_logger: bool = False
worker_redirect_stdouts: bool = True
broker_transport_options: dict[str, int] = {
    "visibility_timeout": 43200
}
beat_schedule: dict[str, dict[str, str | crontab]] = {
        "clear-postgre": {
            "task": "delete_expired_sessions",
            "schedule": crontab(minute="0", hour="*/12")
        },
        "clear-redis": {
            "task": "delete_expired_applications",
            "schedule": crontab(minute="0", hour="*/12")
        }
}
