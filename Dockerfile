FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./logging.conf /code/logging.conf

RUN apt update && pip install -r requirements.txt

COPY ./.cache /app

COPY ./.cache/app.log /app/.cache

COPY ./app /code/app

EXPOSE 8004

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8004"]
