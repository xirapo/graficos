# imports
from flask import Flask, render_template, redirect, url_for, request, \
session, flash

# import wraps for session controll
from functools import wraps

#import pandas for data manipulation
import pandas as pd
import numpy as np

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
    data = pd.read_csv('data/Libro.csv', sep=';', header=0, encoding='latin1')
    h = data['NOMBRE'][:1]
    p = data['PRODUCCION']
    t1 = data['TIPO1'].str.replace("[(%':]", "")
    t2 = data['TIPO2'].str.replace("[(%':]", "")
    print (h)
    print ("produccion: " + p)
    print (data)
    return render_template("index.html",tipo1=t1, tipo2=t2, header=h, production= p)
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
