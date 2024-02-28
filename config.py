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
    LOG_FILE = env.get("LOG_FILE", "/var/log/webappLogs/webapp.log")
    DEBUG = env.get("DEBUG")
    MYSQL_USER = env.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = env.get("MYSQL_PASSWORD")
    MYSQL_HOST = env.get("MYSQL_HOST", '127.0.0.1:3306')
    MYSQL_DB = env.get("MYSQL_DB", 'webapp')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}' \
        if MYSQL_PASSWORD else f'mysql+pymysql://{MYSQL_USER}@{MYSQL_HOST}/{MYSQL_DB}'
    FLASK_APP = env.get("FLASK_APP")


app_config = Config()
