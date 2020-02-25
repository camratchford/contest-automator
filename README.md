# Contest Automator

A bot that will enter contests on your behalf. 
Extendable with configuration files.

(Disclaimer: This breaks the rules of every single contests it will enter. Use this program at your own risk.)
## Getting Started

### Prerequisites
 - A machine running Linux (tested in Ubuntu 16, Centos 7)
   (Needs X Server running if in testing mode)
 - Docker CE
 - Python 3.6 or better
 - Firefox-Geckodriver (Optional, for testing mode)

#### Installing DockerCE (Ubuntu)

#### Installing DockerCE (RHEL 7, CentOS 7, Fedora 7)

### Installing

1. If prerequistites are not met, follow the instructions above.
```bash
git pull https://github.com/camratchford/contest_automator.git
```
3. Edit run.sh to contain your information in the -e tags:
It should look something like this
```bash
#!/bin/bash

sudo docker image build --network bridge -t contest_automator .
sudo docker run -it --rm \
  --net bridge \
  -e FIRST_NAME="Namey" \
  -e LAST_NAME="McNameface" \
  -e BIRTH_MONTH="April" \
  -e BIRTH_DAY="20" \
  -e BIRTH_YEAR="1969" \
  -e GENDER="Male" \
  -e ADDRESS="123 Address Avenue" \
  -e CITY="Pseudoopolois" \
  -e POSTAL_CODE="T0X P9K" \
  -e PROVINCE="BC" \
  -e COUNTRY="Canada" \
  -e PHONE="15542245548" \
  --name contest_automator  \
  --shm-size="2g" \
contest_automator python3 ./run.py
```

### Running the tests


### Deployment


## Built With

- Requests
- Beatiful Soup 4
- Selenium
- Docker CE
- Selenium's Docker Container [selenium/standalone-chrome](https://hub.docker.com/r/selenium/standalone-chrome/)

## Authors

Cam Ratchford

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


