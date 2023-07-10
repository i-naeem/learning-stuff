from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import EqualTo
from wtforms import PasswordField
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import EmailField


class Signup(FlaskForm):
    first_name = StringField(
        label="First Name", validators=[
            DataRequired(), Length(min=3, max=10)]
    )

    last_name = StringField(
        label="Last Name",
        validators=[]
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired(), Length(min=4, max=32)]
    )

    confirm_password = PasswordField(
        label="Confirm Password",
        validators=[DataRequired(), Length(min=4, max=32), EqualTo('Password')]
    )

    username = StringField(
        label="Username",
        validators=[DataRequired(),  Length(min=3, max=8)]
    )

    email = EmailField(
        label="Email",
        validators=[DataRequired()]
    )

    submit = SubmitField('Sign up')
