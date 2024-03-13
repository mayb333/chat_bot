FROM python:3.11.8

COPY . /app

WORKDIR /app

RUN pip install poetry

RUN poetry install

RUN chmod +x /app/ml_service/run_ml.sh
RUN chmod +x /app/bot_service/run_bot.sh
