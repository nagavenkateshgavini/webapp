import os
from sys import path

from dotenv import load_dotenv
from constants import PROJECT_ROOT

if os.path.exists('.env.local'):
    load_dotenv(dotenv_path='.env.local')

path.append(PROJECT_ROOT)
env = os.environ


class Config:
    LOG_LEVEL = env.get("LOG_LEVEL", "INFO")
    LOG_FILE = env.get("LOG_FILE", "/var/logs/webapp_aws_cicd.log")
    DEBUG = env.get("DEBUG")
    MYSQL_USER = env.get("MYSQL_USER")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD")
    MYSQL_HOST = env.get("MYSQL_HOST")
    MYSQL_DB = env.get("MYSQL_DB")
    MYSQL_PORT = env.get("MYSQL_PORT")
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
    FLASK_APP = env.get("FLASK_APP")

    def __init__(self):
        print(Config.SQLALCHEMY_DATABASE_URI)


app_config = Config()
