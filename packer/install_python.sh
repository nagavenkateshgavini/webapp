#!/bin/bash
set -e

sudo dnf install -y python39

echo "Verifying Python version"
python3.9 --version

python3.9 -m ensurepip --upgrade

sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3.9 1

echo "Verifying pip version"
pip --version
