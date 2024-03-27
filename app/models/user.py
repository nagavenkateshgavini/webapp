import datetime
import uuid
from datetime import timedelta

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import bcrypt

from app.extensions import db, bcrypt
from config import app_config


class Base(DeclarativeBase):
    pass


class User(db.Model):
    id: Mapped[str] = mapped_column(String(60), nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    username: Mapped[str] = mapped_column(String(40), primary_key=True, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    password: Mapped[str] = mapped_column(String(120))

    account_created: Mapped[datetime.datetime] = mapped_column(default=datetime.datetime.utcnow)
    account_updated: Mapped[datetime.datetime] = mapped_column(
        default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    email_sent_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    email_verified: Mapped[bool] = mapped_column(Boolean, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in ['password', 'email_sent_time']}

    def hash_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def verify_email(self, curr_time):
        time_diff = curr_time - self.email_sent_time
        if time_diff > timedelta(minutes=app_config.EMAIL_VERIFY_TTL):
            return False
        return True
