#!/bin/bash

docker image build -t contest_automator:latest .
sudo docker run -it --rm \
        -e FIRST_NAME=Cameron \
        -e LAST_NAME=Ratchford \
        -e EMAIL=cjratchford@hotmail.com \
        -e PHONE=4033899337 \
        -v "${HOME}/contest_automator:/app" \
        --name contest_automator  \
        contest_automator:latest