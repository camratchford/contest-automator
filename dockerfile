FROM selenium/standalone-firefox

USER root

MAINTAINER Cameron Ratchford <cameron@ratchfordconsulting.com>

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update && \
  sudo apt-get install -y --no-install-recommends \
  xvfb \
  xdpyinfo \
  python3.7 \
  python3-pip \
  python3-setuptools\
  python3-dev \
  python3-venv \
  && sudo rm -rf /var/lib/apt/lists/*

COPY ./ /app

WORKDIR /app/automator

RUN python3 -m venv /app/automator/venv

run . /app/automator/venv/bin/activate
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /app/
RUN python3 run.py

