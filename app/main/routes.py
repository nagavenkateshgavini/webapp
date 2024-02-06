from flask import Response, request, make_response
from flask import Blueprint

from error import error_handler
from log import logger
from service.utils import db_utils
from service.user import account_manager
from app.models import user
from app.main.parsers import _parse_insert_user

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


@bp.route("/v1/user/self", methods=['GET', 'PUT'])
@error_handler
def handle_user_account_req() -> Response:
    logger.debug("handle_user_account_req gets called")
    if request.method == "PUT":
        pass
    elif request.method == "GET":
        pass
    else:
        return make_response('', "404")


@bp.route("/v1/user", methods=['POST'])
@error_handler
def create_user() -> Response:
    logger.debug("create_user gets called")

    if request.method != "POST":
        return make_response('', 400)
    req = request.json
    _parse_insert_user(req)
    user_obj = user.User(
        email=req['email'],
        password=req['password'],
        first_name=req['first_name'],
        last_name=req['last_name']
    )
    account_manager.insert_user(user_obj)

    return make_response('', 201)
