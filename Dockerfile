FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN apk update && apk add py3-psycopg2


RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install wheels/*.whl --no-cache-dir && \
    apk --purge del .build-deps
      
      