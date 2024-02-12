from app import db
from sqlalchemy import text

from error import DatabaseConnectionError


def check_db_connection():
    try:
        db.session.execute(text('SELECT 1'))
    except DatabaseConnectionError as e:
        raise DatabaseConnectionError(f"{e.message}")
