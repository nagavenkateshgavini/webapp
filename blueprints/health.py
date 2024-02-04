from flask import Blueprint, make_response, Response, request

from log import logger
from error import error_handler
from service.utils.db_utils import check_db_connection

health_bp = Blueprint(name="health_bp", import_name=__name__)


@health_bp.route("/healthz", methods=['GET'])
@error_handler
def healthcheck() -> Response:
    logger.debug("health api gets called")

    if request.get_data() or request.args:
        return make_response('', 400)

    try:
        check_db_connection()
    except Exception as e:
        logger.info(f"Issue occurring with DB connection, error: {e}")
        return make_response('', 503)

    return make_response('', 200)
