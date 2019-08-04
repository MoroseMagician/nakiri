from flask import Flask
from api import auth
from api import index


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(index.blueprint)

    return app
