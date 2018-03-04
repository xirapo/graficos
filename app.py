# imports
from flask import Flask, render_template, redirect, url_for, request, \
session, flash

from functools import wraps

app = Flask(__name__)

# secret key for session
app.secret_key = "12345678"

# Routes

# login require

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

## home
@app.route('/')
def home():
    return render_template("index.html")
## login
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] \
         != 'admin':
            error = "Wrong username or password."
        else:
            session['logged_in'] = True
            return redirect(url_for('admin'))
    return render_template("login.html", err=error)

# logout
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

## admin
@app.route('/admin')
@login_required
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True)
