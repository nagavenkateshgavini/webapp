#!/bin/bash
set -e

sudo dnf install -y python39
python3.9 -m ensurepip
python3.9 -m pip install --upgrade pip
python3.9 --version
python3.9 -m pip --version
