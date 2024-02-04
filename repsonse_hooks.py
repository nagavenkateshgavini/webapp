from flask import request, make_response


def add_no_cache_header(response):
    if request.path == '/healthz' and request.method != 'GET':
        response = make_response('')
        response.headers['Content-Type'] = 'text/plain'
        response.status_code = 405

    response.headers['Cache-Control'] = 'no-cache'

    return response
