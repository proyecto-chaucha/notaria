import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask.cli import with_appcontext

db = SQLAlchemy()
csrf_protect = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_object('notaria.settings')
    csrf_protect.init_app(app)
    db.init_app(app)

    from notaria.views import index
    app.register_blueprint(index.bp)

    app.cli.add_command(init_db_command)

    return app


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database.')