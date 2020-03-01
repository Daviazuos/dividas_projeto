from flask import Flask,render_template, redirect, url_for, request
from form import fields
import os
import conn

SECRET_KEY = os.urandom(32)

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/del_divida',methods=['POST','GET'])
def delete_db():
    msg = "Delete successfully"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            cur.execute("delete from dados")
            con.commit()
        except Exception:
            msg = "Error to delete"
    return msg

@app.route('/add_divida',methods=['POST','GET'])
def add_divida():
    msg = ''
    form = fields()
    if form.validate_on_submit():
        msg = insert_db(form)
    return render_template('add_divida.html', form= form, msg=msg)

@app.route('/add_card',methods=['POST','GET'])
def add_card():
    msg = ''
    form = fields()
    if form.validate_on_submit():
        msg = insert_db_card(form)
    return render_template('add_card.html', form= form, msg=msg)

@app.route('/edit_divida',methods=['POST','GET'])
def edit_divida():
    msg = "Record successfully edited"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            cur.execute("select nome from dados")
            dados = cur.fetchall()
            return render_template('edit_divida.html', msg=msg, dividas=dados)
        except Exception:
            msg = "Error"
    return msg

@app.route('/',methods=['POST','GET'])
def index():
    msg = ''
    form = fields()
    name = select_db()
    return render_template('home.html', form=form, msg=msg, names=name)

@app.route('/')
def home():
    return redirect(url_for('/index'))