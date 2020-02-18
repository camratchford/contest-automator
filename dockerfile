FROM ubuntu:18.04

MAINTAINER Cameron Ratchford <cameron@ratchfordconsulting.com>

ENV PYTHONUNBUFFERED 1

RUN apt update

RUN apt-get install -y python3.7 python3-pip

RUN pip3 install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY . /app

WORKDIR /app/automator
RUN pip3 install -r requirements.txt

WORKDIR /app
CMD python3 run.py
