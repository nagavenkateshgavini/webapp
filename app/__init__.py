from flask import Flask
from sqlalchemy_utils import database_exists, create_database
from flask_swagger_ui import get_swaggerui_blueprint

from app.extensions import db, bcrypt

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
    response.headers['Cache-Control'] = 'no-cache'

    return response


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    bcrypt.init_app(app)
    db.init_app(app)

    if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
        create_database(app.config['SQLALCHEMY_DATABASE_URI'])

    with app.app_context():
        from app.models import user
        db.create_all()

    SWAGGER_URL = "/apidocs"
    API_URL = "/static/swagger.json"

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Flask API'
        }
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    # Register blueprints here
    from app.main.routes import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")

    app.after_request(add_no_cache_header)

    return app
