FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/base
COPY requirements.txt .

RUN apk update && apk add --no-cache py3-psycopg2 postgresql-client; \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-libs postgresql-dev; \
    pip install -r requirements.txt --no-cache-dir; \
    apk --purge del .build-deps