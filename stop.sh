#!/bin/bash

pkill -f "beat"
pkill -f "worker"
echo celery stopped