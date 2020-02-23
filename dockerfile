FROM selenium/standalone-chrome

USER root

MAINTAINER Cameron Ratchford <cameron@ratchfordconsulting.com>

ENV PYTHONUNBUFFERED 1

RUN sudo apt-get update && \
  sudo apt-get install -y --no-install-recommends \
  xvfb \
  xserver-xephyr \
  vnc4server \
  libdbus-glib-1-2 \
  libgtk2.0-0 \
  libasound2 \
  python3.7 \
  python3-pip \
  python3-setuptools\
  python3-dev \
  python3-venv \
  python-pil \
  && sudo rm -rf /var/lib/apt/lists/*

COPY ./ /app

WORKDIR /app/automator

RUN sudo -H python3 -m venv /app/automator/venv


RUN sudo -H bash /app/automator/venv/bin/activate
RUN sudo -H pip3 install --upgrade pip
RUN sudo -H pip3 install -r requirements.txt

WORKDIR /app/

