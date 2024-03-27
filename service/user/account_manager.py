import datetime

from app.extensions import db
from sqlalchemy.exc import NoResultFound, IntegrityError

from app.models.user import User
from error import AuthError, ConflictError, CustomError

from publisher import publish_message
from log import logger
from config import app_config


def authenticate_user_and_return_obj(user_obj: User):
    logger.debug("inside auth function")
    try:
        user_from_db = db.session.execute(db.select(User).filter_by(
            username=user_obj.username)).scalar_one()
    except NoResultFound:
        raise AuthError("user is not authenticated")

    if not user_from_db:
        raise AuthError("user is not authenticated")

    if not user_from_db.verify_password(user_obj.password):
        raise AuthError("user is not authenticated")

    if not user_from_db.email_verified:
        raise AuthError("user email is not yet verified")

    return user_from_db


def get_user_info(user_obj: User) -> dict:
    user_obj = authenticate_user_and_return_obj(user_obj)
    res = user_obj.as_dict()
    return res


def get_user_info_without_verify_email(user_obj: User) -> User:
    try:
        user_from_db = db.session.execute(db.select(User).filter_by(
            username=user_obj.username)).scalar_one()
    except NoResultFound:
        raise AuthError("user is not authenticated")

    return user_from_db


def insert_user(user_obj: User) -> None:
    logger.debug("Creating user...")
    user_obj.hash_password(user_obj.password)
    db.session.add(user_obj)
    try:
        db.session.commit()
        publish_message(user_obj.username)
    except IntegrityError:
        db.session.rollback()
        raise ConflictError("user exists already, create  a new one")


def update_user(user_obj: User, req: dict) -> None:
    if "password" in req:
        user_obj.hash_password(req['password'])

    if "first_name" in req:
        user_obj.first_name = req['first_name']

    if "last_name" in req:
        user_obj.last_name = req['last_name']

    db.session.commit()


def verify_email(user_obj: User) -> None:
    user_obj_from_db = get_user_info_without_verify_email(user_obj)
    if user_obj_from_db.email_verified:
        raise CustomError(400, "User already verified")

    if user_obj_from_db.verify_email(datetime.datetime.utcnow()):
        user_obj_from_db.email_verified = True
        db.session.commit()
        return
    raise CustomError(403, "Request timed out")
