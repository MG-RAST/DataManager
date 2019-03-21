FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY . .

# uncomment the 3 lines below to create new wheels:

RUN apk update && apk add --no-cache py3-psycopg2 && \
    #apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-libs postgresql-dev && \
    #pip wheel -r requirements.txt -w wheels && \
    #apk --purge del .build-deps && \
    python3 -m pip install wheels/*.whl --no-cache-dir