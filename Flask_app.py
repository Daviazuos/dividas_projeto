from flask import Flask,render_template, redirect, url_for
from form import fields
import os
import conn

SECRET_KEY = os.urandom(32)

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/del_divida',methods=['POST','GET'])
def delete_db():
   msg = conn.delete_database()
   return msg

@app.route('/add_divida',methods=['POST','GET'])
def add_divida():
    msg = ''
    form = fields()
    if form.validate_on_submit():
        msg = conn.insert_db(form)
    return render_template('add_divida.html', form= form, msg=msg)

@app.route('/add_card',methods=['POST','GET'])
def add_card():
    msg = ''
    form = fields()
    if form.validate_on_submit():
        msg = conn.insert_db_card(form)
    return render_template('add_card.html', form= form, msg=msg)

@app.route('/edit_divida',methods=['POST','GET'])
def edit_divida():
    dados = conn.edit_dividas()
    return render_template('edit_divida.html', msg=dados[1], dividas=dados[0])

@app.route('/',methods=['POST','GET'])
def index():
    msg = ''
    form = fields()
    name = conn.select_db()
    return render_template('home.html', form=form, msg=msg, names=name[0], total=name[1])

@app.route('/')
def home():
    return redirect(url_for('/index'))

if __name__ == '__main__':
    app.run(debug=True)