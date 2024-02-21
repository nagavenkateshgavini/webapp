#!/bin/bash
set -e

sudo dnf update -y
sudo dnf install -y python39

echo "Verifying Python version"
python3.9 --version

python3.9 -m ensurepip --upgrade
pip3 --version
