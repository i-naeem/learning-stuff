from flask import render_template
from forms.Signin import Signin
from forms.Signup import Signup
from flask import redirect
from flask import url_for
from flask import flash
from flask import Flask

app = Flask(__name__, template_folder='views')

app.secret_key = "8115f854ce4f72a249a573e3e122abffe85511915b5bb76988287c932956cbdb"


@app.get('/')
def index():
    return render_template('index.jinja', title="Home")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = Signin()

    if form.validate_on_submit():
        flash(f'You are logged in as {form.username.data}!')
        return redirect(url_for('index'))

    return render_template('signin.jinja', title="Sign in", form=form)


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = Signup()

    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('signup.jinja', title="Sign up", form=form)


if __name__ == '__main__':
    app.run(debug=True)
