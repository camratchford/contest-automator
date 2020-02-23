#!/bin/bash

sudo docker image build --network mac_net -t contest_automator . 
sudo docker run -it -d --rm \
	--env="DISPLAY" \
	--volume="$HOME/.Xauthority:/root/.Xauthority:rw"  \
	--net mac_net --ip=10.0.10.25 \
        -e FIRST_NAME=Namey \
        -e LAST_NAME=McNamerson \
        -e EMAIL=firstname.lastname@domain.tld \
        -e PHONE=1234567890 \
        --name contest_automator  \
        --shm-size="2g" \
	contest_automator python3 run.py
