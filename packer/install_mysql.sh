#!/bin/bash
set -e

sudo dnf install -y mysql-server
sudo systemctl start mysqld
sudo systemctl enable mysqld

sudo systemctl status mysqld

echo "Printing mysql username from env"
echo $MYSQL_USER

# Verify mysql version
mysql --version
