from wtforms.validators import DataRequired
from wtforms import PasswordField
from flask_wtf import FlaskForm
from wtforms import StringField


class Signin(FlaskForm):
    username = StringField(
        label="Username",
        validators=[DataRequired()],
    )
    password = PasswordField(label="Password", validators=[DataRequired()])
