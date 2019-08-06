from flask import (
    Blueprint,
    request
)
from nakiri.models import User

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=['POST'])
def register():
    if (request.form['username'] is None):
        return 'Username required!'
    print(User)


@blueprint.route('/login', methods=['POST'])
def login():
    return 'login'


@blueprint.route('/logout', methods=['POST'])
def logout():
    return request.form
