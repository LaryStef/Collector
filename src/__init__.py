from celery import Celery

import celeryconfig
from src.setup_logging import setup_logging


celery: Celery = Celery()
celery.config_from_object(celeryconfig)
setup_logging()
