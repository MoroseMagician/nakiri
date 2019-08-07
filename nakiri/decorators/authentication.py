import os
import jwt
from flask import request, g
from typing import Callable
from functools import wraps
from jwt.exceptions import (
    InvalidSignatureError,
    DecodeError
)


def token_required(f: Callable):
    """ Authenticate a request with a token header """
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            header = request.headers['Authentication']
            encoded_token = header.split(' ')[1]
        except KeyError:
            return {
                'success': False,
                'message': 'Missing authentication header.'
            }
        except IndexError:
            return {
                'success': False,
                'message': 'Invalid authentication header.'
            }

        try:
            token = jwt.decode(encoded_token, os.environ['NAKIRI_KEY'])
        except InvalidSignatureError:
            return {
                'success': False,
                'message': 'Invalid token signature.'
            }
        except DecodeError:
            return {
                'success': False,
                'message': 'Malformed authentication token.'
            }

        # Inject the token into the application context
        g.token = token
        return f(*args, **kwargs)
    return wrapper
