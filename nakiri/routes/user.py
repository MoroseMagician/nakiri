from flask import (
    Blueprint,
    request
)
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash

from nakiri.models.user import User
from nakiri import util


blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/<username>')
def get(username):
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return {
            'id':       user.id,
            'username': user.username,
            'password': user.password
        }
    return {
        'message': 'User doesn\'t exist.'
    }


@blueprint.route('/register', methods=['POST'])
def register():
    try:
        user = User(
            username=request.form['username'],
            password=request.form['password']
        )
    except KeyError as ex:
        missing_arg = ex.args[0]
        return {
            'success': False,
            'message': f'{missing_arg.title()} required'
        }

    try:
        user.add()
    except IntegrityError:
        # Constraint failed - user exists
        return {
            'success': False,
            'message': 'This user already exists.'
        }

    return {
        'success': True,
        'message': f'User {user.username} registered.'
    }


@blueprint.route('/login', methods=['POST'])
def login():
    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError as ex:
        missing_arg = ex.args[0]
        return {
            'success': False,
            'message': f'{missing_arg.title()} required'
        }

    # Get user
    user = User.query.filter_by(username=username).first()
    if user is None:
        return {
            'success': False,
            'message': 'User doesn\'t exist.'
        }

    # Check password
    if not check_password_hash(user.password, password):
        return {
            'success': False,
            'message': 'Wrong password.'
        }

    return {
        'success': True,
        'message': 'Logged in!'
    }


@blueprint.route('/logout', methods=['POST'])
def logout():
    return request.form
