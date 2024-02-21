#!/bin/bash
set -e

sudo dnf install -y unzip
unzip webapp.zip -d webapp

sudo chown csye6225:csye6225 ~/webapp
sudo chmod 650 ~/webapp

HOME="/home/csye6225/"
sudo mv ~/webapp $HOME

cd $HOME/webapp

echo "Listing all the contents of the /opt/webapp/"
ls

pip install -r requirements.txt

PYTHON_PATH=$(which python3)
echo $PYTHON_PATH

#logs folder
sudo mkdir -p /var/log/webappLogs
chown csye6225:csye6225 /var/log/webappLogs
sudo chmod 650 /var/log/webappLogs
sudo touch $LOG_FILE

sudo tee /etc/systemd/system/csye6225.service <<EOF
[Unit]
Description=CSYE 6225 App
ConditionPathExists=$HOME/webapp/run.py
After=network.target

[Service]
Type=simple
User=csye6225
Group=csye6225
WorkingDirectory=$HOME/webapp
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
