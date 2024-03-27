import logging

from typing import Union
from flask import Response, request, make_response
from flask import Blueprint

from error import error_handler
from log import logger
from config import app_config
from service.utils import db_utils
from service.user import account_manager
from app.models import user
from app.main.parsers import _parse_insert_user, \
    _parse_get_user, _parse_update_user

bp = Blueprint('main', __name__)


@bp.route("/healthz", methods=['GET'])
@error_handler
def healthcheck() -> Response:
    logger.info("health api gets called")

    if request.get_data() or request.args:
        logger.warning("Bad request, data is not required")
        return make_response('', 400)

    try:
        db_utils.check_db_connection()
    except Exception as e:
        logger.error(f"Issue occurring with DB connection, error: {e}")
        return make_response('', 503)

    return make_response('', 200)


@bp.route("/v1/user/self", methods=['GET'])
@error_handler
def get_user() -> Union[Response, dict]:
    logger.info("get_user gets called")

    auth = request.authorization
    if not auth:
        return make_response({"error": "basic auth is required"}, 401)

    _parse_get_user(request)
    username, password = auth.username, auth.password
    user_obj = user.User(
        username=username,
        password=password
    )
    return account_manager.get_user_info(user_obj)


@bp.route("/v1/user/self", methods=['PUT'])
@error_handler
def update_user() -> Response:
    logger.info("update_user gets called")
    auth = request.authorization
    if not auth:
        return make_response({"error": "basic auth is required"}, 401)

    _parse_update_user(request)
    # authenticate
    username, password = auth.username, auth.password
    user_obj = user.User(
        username=username,
        password=password
    )
    user_obj = account_manager.authenticate_user_and_return_obj(user_obj)

    req = request.json

    # update_user
    account_manager.update_user(user_obj, req)

    return make_response('', 204)


@bp.route("/v1/user", methods=['POST'])
@error_handler
def create_user() -> Response:
    logger.info("create_user gets called")

    if request.method != "POST" or request.content_type != "application/json":
        logger.warning("Method should be post")
        return make_response('', 400)

    req = request.json
    _parse_insert_user(req)
    user_obj = _prepare_user_obj(req)
    account_manager.insert_user(user_obj)

    return make_response(user_obj.as_dict(), 201)


@bp.route("/v1/verify_email/<email_id>", methods=['GET'])
@error_handler
def verify_email(email_id) -> Response:
    logger.info("verify_email gets called")

    if not email_id:
        return make_response('', 400)

    user_obj = _prepare_user_obj({"username": email_id})
    account_manager.verify_email(user_obj)

    return make_response('User Successfully verified', 200)


def _prepare_user_obj(req):
    return user.User(
        username=req.get('username'),
        password=req.get('password'),
        first_name=req.get('first_name'),
        last_name=req.get('last_name'),
        email_verified=True if app_config.TEST_ENV else False
    )
