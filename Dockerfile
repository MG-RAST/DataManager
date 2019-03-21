FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY . .

# uncomment the 3 lines below to create new wheels:

RUN apk update && apk add --no-cache py3-psycopg2; \
    if [ -d wheels ] ; then  \
      apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-libs postgresql-dev; \
      python3 -m pip install wheels/*.whl --no-cache-dir ; \
      apk --purge del .build-deps; \
    else \
      pip install -r requirements.txt --no-cache-dir; \
    fi