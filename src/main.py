import click
from flask import Flask
from flask.cli import AppGroup
from flask_sqlalchemy import SQLAlchemy
from api import auth
from api import index

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth.blueprint)
    app.register_blueprint(index.blueprint)

    populate_cli(app)

    return app


def populate_cli(app):
    db_cli = AppGroup('db', help='Database commands')

    @db_cli.command(name='init')
    @click.confirmation_option()
    def db_init():
        """ Initialize the database """
        click.secho('Initializing database...', fg='red', color=True)

    @db_cli.command(name='migrate')
    @click.confirmation_option()
    def db_migrate():
        """ Run migrations """
        click.secho('Starting migration...', fg='red', color=True)

    app.cli.add_command(db_cli)
