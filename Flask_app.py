from flask import Flask,render_template, redirect, url_for, request
from form import fields
import os
import funcoes
import conn
import datetime

SECRET_KEY = os.urandom(32)

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/del_divida',methods=['POST','GET'])
def delete_db():
   form = fields()
   msg = conn.delete_database()
   return render_template('add_divida.html',form= form, msg=msg)

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
    msgcard = ''
    ChoicedMonth = str(datetime.datetime.now().month).zfill(2)
    form = fields()
    if request.method == 'POST':

        ChoicedMonth = request.form.get('StartMonth')
        CardId = request.form.get('ChoiceCard')
        ValueCard = request.form.get('ValueCard')
        DateBuy = request.form.get('DateBuy')
        msgcard = conn.UpdateCard([CardId,ValueCard,DateBuy])

        if ChoicedMonth is None:
            ChoicedMonth = str(datetime.datetime.now().month).zfill(2)
        name = conn.select_db(ChoicedMonth)
        msg = 'Dívidas referente ao mês: ' + funcoes.meses(name[2])
        cards = conn.select_db_card()
        return render_template('home.html', form=form, msg=msg, names=name[0], total=name[1], cards=cards,msgcard= msgcard, CardName = name[3])
    name = conn.select_db(ChoicedMonth)
    msg = 'Dívidas referente ao mês: '+ funcoes.meses(name[2])
    cards = conn.select_db_card()
    return render_template('home.html', form=form, msg=msg, names=name[0], total=name[1], cards=cards, msgcard= msgcard, CardName = name[3])

if __name__ == '__main__':
    app.run(debug=True)