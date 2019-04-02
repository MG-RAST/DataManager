FROM mgrast/django-base:latest
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./scripts/docker-entrypoint.sh /bin/docker-entrypoint.sh
COPY ./scripts/wait-for-postgres.sh /bin/wait-for-postgres.sh

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["start"]