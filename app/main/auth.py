from error import AuthError
from flask import request

from service.user import account_manager
from app.models.user import User


def authenticate(view_func):
    def wrapper(*args, **kwargs):
        password_header = request.headers.get('Authorization')

        if not password_header:
            raise AuthError("auth not provided")

        username, password = password_header.split(':')
        account_manager.authenticate_user_and_return_obj(User(
            username=username,
            password=password
        ))

        return view_func(*args, **kwargs)

    return wrapper
