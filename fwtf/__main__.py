from flask import render_template
from flask import Flask

app = Flask(__name__, template_folder='views')


@app.get('/')
def index():
    return render_template('index.jinja', title="Home")


@app.get('/signin')
def signin():
    return render_template('signin.jinja', title="Sign in")


@app.get('/signup')
def signup():
    return render_template('signup.jinja', title="Sign up")


if __name__ == '__main__':
    app.run(debug=True)
