# imports
from flask import Flask, render_template, redirect, url_for, request, \
    session, flash

# import wraps for session controll
from functools import wraps

# import pandas for data manipulation
import pandas as pd
import numpy as np

import logging

## CAMBIOS
from werkzeug.utils import secure_filename

# HECHO PARA BUSCAR DENTRO DEL DIRECTORIO SI EXISTE O NO UN ARCHIVO
from pathlib import Path


def ls(ruta):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]


###

import sys
import csv
import os

UPLOAD_FOLDER = './data/'
ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__)  ## ESTO YA ESTABA
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


def allowed_file(filename):
    return filename[-3].lower() in ALLOWED_EXTENSIONS


## FIN DE LOS CAMBIOS

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
    # BUSCA EL ARCHIVO CSV ACTUAL Y DISPONIBLE PARA PRESENTAR
    oldfile = ls(UPLOAD_FOLDER)

    if oldfile[0] == '.DS_Store':
        fileProducto = os.path.join(app.config['UPLOAD_FOLDER'], oldfile[2])
        fileError = os.path.join(app.config['UPLOAD_FOLDER'], oldfile[1])
        fileTiempo = os.path.join(app.config['UPLOAD_FOLDER'], oldfile[3])
    else:
        fileProducto = os.path.join(app.config['UPLOAD_FOLDER'], oldfile[1])
        fileError = os.path.join(app.config['UPLOAD_FOLDER'], oldfile[2])
        fileTiempo = os.path.join(app.config['UPLOAD_FOLDER'], oldfile[0])

    # LEE EL ARCHIVO .CSV
    data1 = pd.read_csv(fileProducto, sep=',', header=0, encoding='latin1')
    data2 = pd.read_csv(fileError, sep=',', header=0, encoding='latin1')
    data3 = pd.read_csv(fileTiempo, sep=',', header=0, encoding='latin1')

    #print("file error" + fileError)
    print(data2)
    print ("=======================")
    print ("data2: " + data2['C1-L1'])

    #LEER PRODUCCION
    t = data1['Nombre']
    c1 = data1['C1']
    c2 = data1['C2']
    c3 = data1['C3']
    c4 = data1['C4']
    c5 = data1['C5']

    #LEER ERROR
    data2['C1-L1'] = data2['C1-L1'].astype('str')
    data2['C1-L2'] = data2['C1-L2'].astype('str')
    c1l1 = data2['C1-L1'].str.replace("[(%':]", "")
    c1l2 = data2['C1-L2'].str.replace("[(%':]", "")

    data2['C2-L1'] = data2['C2-L1'].astype('str')
    data2['C2-L2'] = data2['C2-L2'].astype('str')
    c2l1 = data2['C2-L1'].str.replace("[(%':]", "")
    c2l2 = data2['C2-L2'].str.replace("[(%':]", "")

    data2['C3-L1'] = data2['C3-L1'].astype('str')
    data2['C3-L2'] = data2['C3-L2'].astype('str')
    c3l1 = data2['C3-L1'].str.replace("[(%':]", "")
    c3l2 = data2['C3-L2'].str.replace("[(%':]", "")

    data2['C4-L1'] = data2['C4-L1'].astype('str')
    data2['C4-L2'] = data2['C4-L2'].astype('str')
    c4l1 = data2['C4-L1'].str.replace("[(%':]", "")
    c4l2 = data2['C4-L2'].str.replace("[(%':]", "")

    data2['C5-L1'] = data2['C5-L1'].astype('str')
    data2['C5-L2'] = data2['C5-L2'].astype('str')
    c5l1 = data2['C5-L1'].str.replace("[(%':]", "")
    c5l2 = data2['C5-L2'].str.replace("[(%':]", "")

    #LEER TIEMPO
    t1 = data3['C1']
    t2 = data3['C2']
    t3 = data3['C3']
    t4 = data3['C4']
    t5 = data3['C5']

    return render_template("index.html", title = t,
                           product1 = c1, product2 = c2, product3 = c3, product4 = c4, product5 = c5,
                           c1l1 = c1l1, c2l1 = c2l1, c3l1 = c3l1, c4l1 = c4l1, c5l1 = c5l1,
                           c1l2 = c1l2, c2l2 = c2l2, c3l2 = c3l2, c4l2 = c4l2, c5l2 = c5l2,
                           time1 = t1, time2 = t2, time3 = t3, time4 = t4, time5 = t5 )

## login
@app.route('/login', methods=['GET', 'POST'])
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
@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    ##CAMBIOS DE MANUEL
    if request.method == 'POST':
        # LEE EL NUEVO ARCHIVO Y LO GUARDA
        oldfile = ls(UPLOAD_FOLDER)

        if oldfile[0] == '.DS_Store':
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfile[1]))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfile[2]))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfile[3]))
        else:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfile[0]))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfile[1]))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], oldfile[2]))


        file1 = request.files['archivo1']
        file2 = request.files['archivo2']
        file3 = request.files['archivo3']

        if file1 and allowed_file(file1.filename):
            print('found file')

        filename1 = secure_filename(file1.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))

        if file2 and allowed_file(file2.filename):
            print('found file')

        filename2 = secure_filename(file2.filename)
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))

        if file3 and allowed_file(file3.filename):
            print('found file')

        filename3 = secure_filename(file3.filename)
        file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))

        return redirect(url_for('home'))
    # FIN DE LOS CAMBIOS
    return render_template("admin.html")

if __name__ == '__main__':
    app.run(debug=True)