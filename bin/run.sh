#!/bin/bash

gunicorn erp.asgi:application --bind :${PORT} -k uvicorn.workers.UvicornWorker --workers 3