FROM python:3.8.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/config

ADD ./srv/docker-server

WORKDIR /srv/docker-server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80
