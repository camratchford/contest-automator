#!/bin/bash

docker image build -t contest_automator:latest .
sudo docker run -it --rm \
        -e FIRST_NAME=Namey \
        -e LAST_NAME=McNamerson \
        -e EMAIL=firstname.lastname@domain.tld \
        -e PHONE=1234567890 \
        -v "${HOME}/contest_automator:/app" \
        --name contest_automator  \
        contest_automator:latest