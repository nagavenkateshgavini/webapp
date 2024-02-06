from flask import make_response


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
