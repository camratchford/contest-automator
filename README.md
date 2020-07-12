# Contest Automator

A bot that will enter contests on your behalf. 
Extendable with configuration files.

### Prerequisites
 - A machine running Linux (tested in Ubuntu 16, Centos 7)
   (Needs X Server running if in testing mode)
 - Docker CE
 - Python 3.6 or better
 - Firefox-Geckodriver (Optional, for testing mode)

### Installing

1. If prerequistites are not met, follow the instructions above.
```bash
git pull https://github.com/camratchford/contest_automator.git
```
2. Edit run.sh to contain your information in the -e tags:
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

 Container [selenium/standalone-chrome](https://hub.docker.com/r/selenium/standalone-chrome/)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


