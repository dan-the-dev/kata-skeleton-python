FROM python:3.11.3-slim as base

WORKDIR /app

COPY . .

RUN python -m pip install -U pytest
