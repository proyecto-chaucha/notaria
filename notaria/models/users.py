from flask_user import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from notaria import db


# Define the User data model. Make sure to add the flask_user.UserMixin !!
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # User authentication information (required for Flask-User)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User information
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')


# Define the User profile form
class UserProfileForm(FlaskForm):
    first_name = StringField('First name', validators=[validators.DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[validators.DataRequired('Last name is required')])
    submit = SubmitField('Save')