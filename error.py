from functools import wraps
from flask import jsonify


def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return jsonify({'error': error_message}), 500

    return wrapper
