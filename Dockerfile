# Build mgrast/django-base via django-python-base.dockerfile
FROM mgrast/django-base:latest
ENV PYTHONUNBUFFERED 1

LABEL tag=mgrast/datamanager \
      from=mgrast/django-base:latest \
      git-commit=${GITCOMMIT:-'unknown'}

WORKDIR /usr/src/app

COPY ./docker-entrypoint.sh /docker-entrypoint.sh
COPY ./services/wait-for /bin/wait-for

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["start"]