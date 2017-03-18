#!/usr/bin/env bash
# $1 sudu password

# requre sudo password
if [ "$1" == "" ]; then
    echo "[warning] require sudo password parameter."
    exit 1
fi

SUDO_PW=$1

echo $SUDO_PW | sudo -S aptitude install -y libxml2-dev libxslt-dev libpython3-dev zlib1g-dev

# MySQL client installation
echo $SUDO PW | sudo -S aptitude install -y mysql-client

# docker installation
echo $SUDO_PW | sudo -S aptitude install -y apt-transport-https ca-certificates curl software-properties-common
echo $SUDO_PW | curl -fsSL https://apt.dockerproject.org/gpg | sudo -S apt-key add -                                                
apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D                                                                        
echo $SUDO_PW | sudo -S add-apt-repository "deb https://apt.dockerproject.org/repo/ ubuntu-$(lsb_release -cs) main"                 
echo $SUDO_PW | sudo -S aptitude update                                                                                             
echo $SUDO_PW | sudo -S aptitude install -y docker-engine

# @chapter 05
echo $SUDO_PW | sudo -S aptitude install -y mecab mecab-ipadic-utf8 libmecab-dev
echo $SUDO_PW | sudo -S aptitude build-dep -y python3-matplotlib
echo $SUDO_PW | sudo -S aptitude install -y fonts-migmix
