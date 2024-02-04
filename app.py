from flask import Flask
from blueprints.health import health_bp

from config import app_config
import repsonse_hooks
import request_hooks

app = Flask(__name__)
app.before_request(request_hooks.preprocess_request)
app.after_request(repsonse_hooks.add_no_cache_header)
app.register_blueprint(health_bp, url_prefix="/")


if __name__ == "__main__":
    app.run(debug=app_config.DEBUG, port=8000)
