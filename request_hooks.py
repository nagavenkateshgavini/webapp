from flask import request, make_response
from blueprints.apis import registered_apis


def preprocess_request():
    path_elements = request.path.strip('/').split('/')
    api_name = path_elements[0] if path_elements else None

    if api_name not in registered_apis:
        response = make_response('', 404)
        response.headers['Content-Type'] = 'text/plain'
        response.headers['Cache-Control'] = 'no-cache'
        return response