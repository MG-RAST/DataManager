FROM python:3.7-alpine3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --upgrade pip
RUN apk update && apk add py3-psycopg2
RUN apk add --no-cache postgresql-libs && \
      apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
      

# uncomment to create new wheels:
#RUN cd /usr/src/app/wheels ; rm * ; pip wheel -r ../requirements.txt

RUN cd /usr/src/app ; python3 -m pip install wheels/*.whl