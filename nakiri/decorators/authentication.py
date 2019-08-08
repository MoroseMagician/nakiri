import os
import jwt
from flask import request, g
from typing import Callable
from functools import wraps
from jwt.exceptions import (
    InvalidSignatureError,
    DecodeError
)
from datetime import (
    datetime,
    timezone
)

from nakiri.models.token import Token


def token(f: Callable):
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

        db_token = Token.query.filter_by(token=encoded_token).first()
        current_timestamp = int(
            datetime.now()
            .replace(tzinfo=timezone.utc)
            .timestamp()
        )

        if db_token is None:
            return {
                'success': False,
                'message': 'Invalid token.'
            }

        if db_token.deleted or current_timestamp > token['exp']:
            return {
                'success': False,
                'message': 'Token is expired.'
            }

        # Inject the token into the application context
        g.user = token['user']
        g.token = db_token

        return f(*args, **kwargs)
    return wrapper
