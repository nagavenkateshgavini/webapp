import re

from error import InvalidInputError


def validate_email(email):
    # Regular expression for a basic email validation
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    return bool(re.match(pattern, email))


def validate_password(password):
    # At least 8 characters
    # At least one uppercase letter
    # At least one lowercase letter
    # At least one digit
    # At least one special character (e.g., !@#$%^&*)
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

    return bool(re.match(pattern, password))


def validate_dict_keys(dictionary):
    allowed_keys = {"password", "username", "first_name", "last_name"}
    extra_keys = set(dictionary.keys()) - allowed_keys

    if extra_keys:
        raise InvalidInputError(f"Invalid keys found: {extra_keys}")


def _parse_insert_user(req):

    validate_dict_keys(req)

    if not req.get("username"):
        raise InvalidInputError("all fields are mandatory")

    if not validate_email(req['username']):
        raise InvalidInputError("username should be your email")

    if not req.get("password"):
        raise InvalidInputError("all fields are mandatory")

    if not validate_password(req["password"]):
        raise InvalidInputError("atleast 8 chars, one upper, one lower, one digit, "
                                "one special, eg: R@123d45jn")

    if not req["first_name"]:
        raise InvalidInputError("all fields are mandatory")

    if not req["last_name"]:
        raise InvalidInputError("all fields are mandatory")

    if has_numbers(req['last_name']):
        raise InvalidInputError("last_name should be string")

    if has_numbers(req['first_name']):
        raise InvalidInputError("first_name should be string")


def _parse_get_user(req):
    if req.data or req.query_string:
        raise InvalidInputError("no data is accepted")


def has_numbers(input_str):
    return any(char.isdigit() for char in input_str)


def _parse_update_user(req):
    if req.content_type != "application/json":
        raise InvalidInputError("Please pass only application/json content type")

    if not req.json:
        raise InvalidInputError("Please provide at least one key to update")

    validate_dict_keys(req.json)
    req = req.json
    if req.get('password'):
        validate_password(req['password'])

    if req.get("first_name"):
        if has_numbers(req['first_name']):
            raise InvalidInputError("first_name should be string")

    if req.get("last_name"):
        if has_numbers(req['last_name']):
            raise InvalidInputError("last_name should be string")

    if "last_name" in req:
        if not req['last_name']:
            raise InvalidInputError("last_name should not be empty")

    if "first_name" in req:
        if not req['first_name']:
            raise InvalidInputError("first_name should not be empty")

    if "username" in req:
        raise InvalidInputError("username can not be updated")
