from flask import Flask
from flask_cors import CORS
import os

from nakiri.routes import index
from nakiri.routes import user

from nakiri.models.db import db, migrate


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(index.blueprint)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['NAKIRI_DB']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app
