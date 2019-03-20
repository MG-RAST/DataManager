FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
COPY . .
RUN python3 -m pip install wheels/*.whl
