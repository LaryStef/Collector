import os
from enum import IntEnum
from logging import (
    DEBUG, INFO, WARNING, ERROR, CRITICAL,
    Formatter, Logger, getLogger, Handler, StreamHandler
)
from logging.handlers import RotatingFileHandler

from src.config import settings


class _Levels(IntEnum):
    DEBUG = DEBUG
    INFO = INFO
    WARNING = WARNING
    ERROR = ERROR
    CRITICAL = CRITICAL


def _setup_logger(
    logger: Logger,
    *,
    level: _Levels,
    handlers: list[Handler]
) -> None:
    logger.setLevel(level)
    logger.handlers = []
    for handler in handlers:
        logger.addHandler(handler)


def setup_logging() -> None:
    log_directory: str = os.path.dirname("logs/")
    os.makedirs(log_directory, exist_ok=True)
    log_file: str = os.path.join(log_directory, "app.log")

    formatter: Formatter = Formatter(
        fmt="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",  # noqa: E501
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler: RotatingFileHandler = RotatingFileHandler(
        filename=log_file,
        mode="a",
        maxBytes=settings.MAX_BYTES_PER_FILE,
        backupCount=settings.BACKUP_COUNT
    )
    file_handler.setLevel(_Levels.DEBUG)
    file_handler.setFormatter(formatter)

    console_handler: StreamHandler = StreamHandler()
    console_handler.setLevel(_Levels.DEBUG)
    console_handler.setFormatter(formatter)

    _setup_logger(
        getLogger("celery"),
        level=_Levels.INFO,
        handlers=[file_handler, console_handler]
    )
    _setup_logger(
        getLogger("celery.task"),
        level=_Levels.INFO,
        handlers=[file_handler, console_handler]
    )
    _setup_logger(
        getLogger(),
        level=_Levels.DEBUG,
        handlers=[file_handler, console_handler]
    )
