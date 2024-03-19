#!/bin/bash
set -e

sudo dnf install -y unzip
unzip webapp.zip -d webapp
pwd

HOME="/home/csye6225"

pip install -r $HOME/webapp/requirements.txt

PYTHON_PATH=$(which python3.9)
echo $PYTHON_PATH

#logs folder
sudo touch $LOG_FILE
sudo chown csye6225:csye6225 $LOG_FILE
sudo chown csye6225:csye6225 /var/log
sudo chmod 760 $LOG_FILE

sudo tee /etc/systemd/system/csye6225.service > /dev/null <<EOF
[Unit]
Description=CSYE 6225 App
ConditionPathExists=$HOME/webapp/run.py
After=network.target

[Service]
Type=simple
User=csye6225
Group=csye6225
WorkingDirectory=$HOME/webapp
EnvironmentFile=/etc/environment
ExecStart=${PYTHON_PATH} $HOME/webapp/run.py
Restart=always
RestartSec=3
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=csye6225

[Install]
WantedBy=multi-user.target

EOF

sudo systemctl daemon-reload
sudo systemctl enable csye6225.service

sleep 10
