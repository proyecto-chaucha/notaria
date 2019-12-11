from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from notaria.views import index

db = SQLAlchemy()
csrf_protect = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object('notaria.settings')
    csrf_protect.init_app(app)
    db.init_app(app)
    
    app.register_blueprint(index.bp)

    return app