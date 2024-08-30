from celery import Celery

import celeryconfig


celery: Celery = Celery()
celery.config_from_object(celeryconfig)
