from flask import Blueprint
import os

blueprint = Blueprint('index', __name__)


@blueprint.route('/')
def index():
    return os.environ['NAKIRI_KEY']
