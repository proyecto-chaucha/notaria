from notaria import db


class user_model(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    passwd = db.Column(db.String(64), unique=False, nullable=False)
