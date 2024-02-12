import os
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
    MYSQL_USER = env.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD", "root")
    MYSQL_HOST = env.get("MYSQL_HOST", "127.0.0.1")
    MYSQL_DB = env.get("MYSQL_DB", "application")
    MYSQL_PORT = env.get("MYSQL_PORT", "3306")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    FLASK_APP = env.get("FLASK_APP")


app_config = Config()
