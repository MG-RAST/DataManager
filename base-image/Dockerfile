FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/base
COPY . .

RUN apk update && apk add --no-cache py3-psycopg2; \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-libs postgresql-dev; \
    pip install wheels/*.whl --no-cache-dir; \
    pip install -r requirements.txt --no-cache-dir; \
    apk --purge del .build-deps