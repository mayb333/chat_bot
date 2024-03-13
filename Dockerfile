FROM python:3.11.8

COPY . /app

WORKDIR /app

RUN pip install poetry

RUN poetry install
