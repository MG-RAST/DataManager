# Build mgrast/django-base via django-python-base.dockerfile
FROM mgrast/django-base:latest
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["start"]