from flask import Response, request, make_response
from flask import Blueprint

from error import error_handler
from log import logger
from service.utils import db_utils
from service.user import account_manager
from app.models import user
from app.main.parsers import _parse_insert_user, \
    _parse_get_user, _parse_update_user, _validate_headers

bp = Blueprint('main', __name__)


@bp.route("/healthz", methods=['GET'])
@error_handler
def healthcheck() -> Response:
    logger.debug("health api gets called")

    if request.get_data() or request.args:
        return make_response('', 400)

    try:
        db_utils.check_db_connection()
    except Exception as e:
        logger.info(f"Issue occurring with DB connection, error: {e}")
        return make_response('', 503)

    return make_response('', 200)


@bp.route("/v1/user/self", methods=['GET'])
@error_handler
def get_user() -> dict:
    logger.debug("get_user gets called")
    _parse_get_user(request)
    username, password = request.headers['Authorization'].split(':')
    user_obj = user.User(
        username=username,
        password=password
    )
    return account_manager.get_user_info(user_obj)


@bp.route("/v1/user/self", methods=['PUT'])
@error_handler
def update_user() -> Response:
    logger.debug("update_user gets called")
    _validate_headers(request)
    req = request.json
    _parse_update_user(req)

    # authenticate
    username, password = request.headers['Authorization'].split(":")
    user_obj = user.User(
        username=username,
        password=password
    )
    user_obj = account_manager.authenticate_user_and_return_obj(user_obj)

    # update_user
    account_manager.update_user(user_obj, req)

    return make_response('', 204)


@bp.route("/v1/user", methods=['POST'])
@error_handler
def create_user() -> Response:
    logger.debug("create_user gets called")

    if request.method != "POST":
        return make_response('', 400)

    req = request.json
    _parse_insert_user(req)
    user_obj = _prepare_user_obj(req)
    account_manager.insert_user(user_obj)

    return make_response('', 201)


def _prepare_user_obj(req):
    return user.User(
        username=req.get('username'),
        password=req.get('password'),
        first_name=req.get('first_name'),
        last_name=req.get('last_name')
    )
