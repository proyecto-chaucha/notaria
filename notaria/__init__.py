from flask import Flask
from notaria.views import index

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY='dev')
    app.register_blueprint(index.bp)

    return app