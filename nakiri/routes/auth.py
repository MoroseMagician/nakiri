from flask import (
    Blueprint,
    request
)

from nakiri.models.user import User
from werkzeug.exceptions import BadRequestKeyError


blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=['POST'])
def register():
    try:
        user = User(username=request.form['username'])
    except BadRequestKeyError:
        return 'Username required'


@blueprint.route('/login', methods=['POST'])
def login():
    return 'login'


@blueprint.route('/logout', methods=['POST'])
def logout():
    return request.form
