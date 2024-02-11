import sys
import traceback
from functools import wraps
from flask import make_response

from log import logger


def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except NotFoundError as e:
            return make_response({"error": e.message}, e.status_code)
        except AuthError as e:
            return make_response({"error": e.message}, e.status_code)
        except InvalidInputError as e:
            return make_response({"error": e.message}, e.status_code)
        except CustomError as e:
            return make_response({"error": e.message}, e.status_code)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            logger.error(error_message, sys.exc_info())
            return make_response({'error': error_message}, 500)

    return wrapper


class CustomError(Exception):
    """Base class for custom exceptions."""
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code
        self.message = message


class DatabaseConnectionError(CustomError):
    """Raised when there is an issue connecting to the database."""
    def __init__(self, message="Database connection error"):
        super().__init__(status_code=500, message=message)


class InvalidInputError(CustomError):
    """Raised when the input provided is invalid."""
    def __init__(self, message="Invalid input"):
        super().__init__(status_code=400, message=message)


class NotFoundError(CustomError):
    """Raised when the input provided is invalid."""
    def __init__(self, message="Invalid input"):
        super().__init__(status_code=404, message=message)


class ConflictError(CustomError):
    """Raised when the input provided is invalid."""
    def __init__(self, message="Invalid input"):
        super().__init__(status_code=409, message=message)


class AuthError(CustomError):
    """Raised when the input provided is invalid."""
    def __init__(self, message="Invalid input"):
        super().__init__(status_code=401, message=message)
