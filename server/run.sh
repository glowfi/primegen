#!/usr/bin/env bash

WORKERS=6
PORT=5000

gunicorn main:app --workers "${WORKERS}" --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:"${PORT}"
