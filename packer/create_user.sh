#!/bin/bash

set -e

# Create csye6225 user and group, no login shell
sudo groupadd csye6225
sudo useradd -g csye6225 -s /usr/sbin/nologin
