from flask import render_template
from flask import Flask

app = Flask(__name__, template_folder='views')


@app.get('/signin')
def signin():
    return 'Login'


@app.get('/signup')
def signup():
    return 'Sign up'


@app.get('/')
def index():
    return render_template('index.jinja')


if __name__ == '__main__':
    app.run(debug=True)
