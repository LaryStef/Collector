#!/bin/bash

echo celery starting...
.venv/bin/python -m celery -A src beat &
.venv/bin/python -m celery -A src worker -l DEBUG &