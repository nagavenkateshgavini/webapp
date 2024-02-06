import datetime

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.extensions import db


class Base(DeclarativeBase):
    pass


class User(db.Model):
    email: Mapped[str] = mapped_column(String(40), primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    password: Mapped[str] = mapped_column(String(200))
    account_created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    account_updated: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

