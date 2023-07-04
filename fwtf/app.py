from flask import Flask

app = Flask(__name__)


@app.get('/signin')
def signin():
    return 'Login'


@app.get('/signup')
def signup():
    return 'Sign up'


if __name__ == '__main__':
    app.run(debug=True)
