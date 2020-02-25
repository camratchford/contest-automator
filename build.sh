#!/bin/bash

sudo docker image build --network bridge -t contest_automator .
sudo docker run -it --rm \
	--net bridge \
  -e FIRST_NAME=Namey \
  -e LAST_NAME=McNamerson \
  -e EMAIL=firstname.lastname@domain.tld \
  -e PHONE=1234567890 \
  --name contest_automator  \
  --shm-size="2g" \
	contest_automator python3 ./run.py
