import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_qrcode import QRcode
from flask.cli import with_appcontext
from flask_uploads import patch_request_class


db = SQLAlchemy()
csrf_protect = CSRFProtect()
qrcode = QRcode()


def create_app():
    app = Flask(__name__)
    app.config.from_object('notaria.settings')
    csrf_protect.init_app(app)
    db.init_app(app)
    qrcode.init_app(app)
    patch_request_class(app, size=2*1024*1024)

    from notaria.blueprints import index, wallet, cert
    app.register_blueprint(index.bp)
    app.register_blueprint(wallet.bp)
    app.register_blueprint(cert.bp)

    app.cli.add_command(init_db_command)

    return app


@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('Initialized the database.')
