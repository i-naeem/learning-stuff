from wtforms.validators import DataRequired
from wtforms import PasswordField
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField


class Signin(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField('Sign in')
