from sqlalchemy import create_engine
from config import app_config


def check_db_connection():
    user_name = app_config.MYSQL_USER
    password = app_config.MYSQL_PASSWORD
    port = app_config.MYSQL_PORT
    db_name = app_config.MYSQL_DB
    database_uri = f'mysql+pymysql://{user_name}:{password}@127.0.0.1:{port}/{db_name}'
    engine = create_engine(database_uri)
    with engine.connect() as connection:
        return connection

