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
                'message': 'Missing authentication header.'
            }, 403
        except IndexError:
            return {
                'message': 'Invalid authentication header.'
            }, 400

        try:
            token = jwt.decode(encoded_token, os.environ['NAKIRI_KEY'])
        except InvalidSignatureError:
            return {
                'message': 'Invalid token signature.'
            }, 403
        except DecodeError:
            return {
                'message': 'Malformed authentication token.'
            }, 403

        db_token = Token.query.filter_by(token=encoded_token).first()
        current_timestamp = int(
            datetime.now()
            .replace(tzinfo=timezone.utc)
            .timestamp()
        )

        if db_token is None:
            return {
                'message': 'Invalid token.'
            }, 403

        if db_token.deleted or current_timestamp > token['exp']:
            return {
                'message': 'Token is expired.'
            }, 403

        # Inject the token into the application context
        g.user = token['user']
        g.token = db_token

        return f(*args, **kwargs)
    return wrapper
