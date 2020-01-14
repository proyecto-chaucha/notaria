from notaria import db


class cert_model(db.Model):
    __tablename__ = 'certificados'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    filename = db.Column(db.String(64), unique=True, nullable=False)
    size = db.Column(db.Integer, unique=False, nullable=False)
    sha3 = db.Column(db.String(64), unique=True, nullable=False)

