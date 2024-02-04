import os
import sys
from sys import path

from dotenv import load_dotenv
from constants import PROJECT_ROOT

if os.path.exists('.env.local'):
    load_dotenv(dotenv_path='.env.local')

path.append(PROJECT_ROOT)
env = os.environ


class Config:
    LOG_LEVEL = env.get("LOG_LEVEL", "DEBUG")
    LOG_FILE = env.get("LOG_FILE", "/var/logs/webapp_aws_cicd.log")
    DEBUG = env.get("DEBUG", True)
    MYSQL_USER = env.get("MYSQL_USER", "test")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD", "test@123")
    MYSQL_DB = env.get("MYSQL_DB", "DB")
    MYSQL_PORT = env.get("MYSQL_PORT", "3306")


app_config = Config()
