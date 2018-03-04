# imports
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Routes

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
            error = "Invalid credentials. Please try again."
        else:
            return redirect(url_for('admin'))
    return render_template("login.html", err=error)

## admin
@app.route('/admin')
def admin():
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True)
