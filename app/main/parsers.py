from flask import make_response

from error import InvalidInputError


def _parse_insert_user(req):
    if "email" not in req:
        res = {
            "error": "email is required"
        }
        return make_response(res, 400)

    elif "password" not in req:
        res = {
            "error": "password is required"
        }
        return make_response(res, 400)

    elif "first_name" not in req:
        res = {
            "error": "first_name is required"
        }
        return make_response(res, 400)

    elif "last_name" not in req:
        res = {
            "error": "last_name is required"
        }
        raise make_response(res, 400)


def _parse_get_user(req):
    if "Authorization" not in req.headers:
        raise InvalidInputError("user name can't be updated")


def _parse_update_user(req):
    if not req:
        raise InvalidInputError("Please provide at least one key to update")

    if 'username' in req:
        raise InvalidInputError("user name can't be updated")


def _validate_headers(req):
    if "Authorization" not in req.headers:
        raise InvalidInputError("Please provide auth")
