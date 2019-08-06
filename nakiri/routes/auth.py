from flask import (
    Blueprint,
    request
)

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=['POST'])
def register():
    return 'register'


@blueprint.route('/login', methods=['POST'])
def login():
    return 'login'


@blueprint.route('/logout', methods=['POST'])
def logout():
    return request.form
