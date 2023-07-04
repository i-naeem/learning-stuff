from flask import render_template
from forms.Signin import Signin
from flask import Flask
import os

app = Flask(__name__, template_folder='views')

app.secret_key = os.environ['SECRET_KEY']


@app.get('/')
def index():
    return render_template('index.jinja', title="Home")


@app.get('/signin')
def signin():
    form = Signin()
    return render_template('signin.jinja', title="Sign in", form=form)


@app.get('/signup')
def signup():
    return render_template('signup.jinja', title="Sign up")


if __name__ == '__main__':
    app.run(debug=True)
