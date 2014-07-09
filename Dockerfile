FROM fedora:latest
MAINTAINER Christophe Brun "christophe.brun.cl194@gadz.org"


# Update the package repository
RUN yum -y update

RUN yum  -y install htop iftop rsync screen ssh lsof unzip curl git
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5-curl php5-cli gcc
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-setuptools python2.7 python-pip
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python2.7-dev python-dev

RUN useradd -d /home/behat -m -s /bin/bash behat
RUN echo "behat:behat" | chpasswd

RUN cd /home/behat && git clone https://github.com/chbrun/testlinkconsole.git
#RUN cd /home/behat/testlinkconsole && pip install -r requirements.txt

#RUN mkdir -p /home/behat/composer
#ADD composer.json /home/behat/composer/composer.json
#RUN cd /home/behat/composer && curl http://getcomposer.org/installer | php
#RUN cd /home/behat/composer && php composer.phar install --prefer-source

EXPOSE 80

CMD /bin/bash
