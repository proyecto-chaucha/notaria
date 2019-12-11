import os

# python -c "import os; print repr(os.urandom(24));"
SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgresql://notaria:notaria@localhost/notaria'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask settings
CSRF_ENABLED = True