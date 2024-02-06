from flask import Flask

from config import Config
from app.extensions import db

from flask import request, make_response
from constants import REGISTERED_APIS


def preprocess_request():
    if request.path not in REGISTERED_APIS:
        response = make_response('', 404)
        response.headers['Content-Type'] = 'text/plain'
        response.headers['Cache-Control'] = 'no-cache'
        return response


def add_no_cache_header(response):
    # if request
    #     response = make_response('')
    #     response.headers['Content-Type'] = 'text/plain'
    #     response.status_code = 405

    response.headers['Cache-Control'] = 'no-cache'

    return response


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    with app.app_context():
        from app.models import user
        db.create_all()

    # Register blueprints here
    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")

    # hooks
    app.before_request(preprocess_request)
    app.after_request(add_no_cache_header)

    return app
