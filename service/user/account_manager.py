from app.extensions import db
from sqlalchemy.exc import NoResultFound, IntegrityError

from app.models.user import User
from error import NotFoundError, AuthError, InvalidInputError

from log import logger


def authenticate_user_and_return_obj(user_obj: User):
    logger.debug("inside auth function")
    try:
        user_from_db = db.session.execute(db.select(User).filter_by(
            username=user_obj.username)).scalar_one()
    except NoResultFound:
        raise NotFoundError("no user found")

    if not user_from_db:
        raise NotFoundError("entry not found")

    if user_from_db.verify_password(user_obj.password):
        return user_from_db
    else:
        raise AuthError("user is not authenticated")


def get_user_info(user_obj: User) -> dict:
    user_obj = authenticate_user_and_return_obj(user_obj)
    res = user_obj.as_dict()
    return res


def insert_user(user_obj: User) -> None:
    user_obj.hash_password(user_obj.password)
    db.session.add(user_obj)
    try:
        db.session.commit()
    except IntegrityError:
        raise InvalidInputError("user exists already, create  a new one")


def update_user(user_obj: User, req: dict) -> None:
    if "password" in req:
        user_obj.hash_password(req['password'])

    if "first_name" in req:
        user_obj.first_name = req['first_name']

    if "last_name" in req:
        user_obj.last_name = req['last_name']

    db.session.commit()

