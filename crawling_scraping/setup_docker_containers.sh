#!/usr/bin/env bash
# $1 sudu password

# requre sudo password
if [ "$1" == "" ]; then
    echo "[warning] require sudo password parameter."
    exit 1
fi

SUDO_PW=$1

# MySQL
# usage: $ mysql -u user -h 127.0.0.1 -p
echo $SUDO_PW | sudo -S docker run -d --name mysql -p 0.0.0.0:3306:3306 \
    -e MYSQL_ROOT_PASSWORD=root \
    -e MYSQL_DATABASE=db \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=pass \
    mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

#MongoDB
echo $SUDO_PW | sudo -S docker run -d --name mongo -p 127.0.0.1:27017:27017 mongo
