FROM mgrast/django-base:latest
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
COPY ./services/wait-for /bin/wait-for

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["start"]