import click
from flask import Flask
from flask.cli import AppGroup

from nakiri.routes import index
from nakiri.routes import user

from nakiri.models.db import db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(index.blueprint)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    db.init_app(app)
    populate_cli(app)

    return app


def populate_cli(app):
    db_cli = AppGroup('db', help='Database commands')

    @db_cli.command(name='init')
    @click.confirmation_option()
    def db_init():
        """ Initialize the database """
        click.secho('Initializing database...', fg='red', color=True)
        db.create_all()

    @db_cli.command(name='migrate')
    @click.confirmation_option()
    def db_migrate():
        """ Run migrations """
        click.secho('Starting migration...', fg='red', color=True)

    app.cli.add_command(db_cli)
