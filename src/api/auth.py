from flask import Blueprint

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/register', methods=['POST'])
def register():
    return 'register'


@blueprint.route('/login', methods=['POST'])
def login():
    return 'login'
