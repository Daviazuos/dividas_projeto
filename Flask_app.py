from flask import Flask,render_template
from form import fields
import os
import sqlite3 as sql

SECRET_KEY = os.urandom(32)

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY


def insert_db(form):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        for parcela in range(1, int(form.parcelas.data) + 1):
            cur.execute("INSERT INTO dados (nome,parcelas,valor) VALUES(?, ?, ?)",(str(form.nome.data), parcela, float(form.valor.data)))
        con.commit()
        msg = "Record successfully added"
    return msg

def select_db(form):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("select * from dados")
        dados = cur.fetchall()
    return dados

@app.route('/',methods=['POST','GET'])
def index():
    msg = ''
    form = fields()
    name = select_db(form)
    if form.validate_on_submit():
        msg = insert_db(form)
        names = name

    return render_template('home.html', form= form, msg=msg, names= name)

if __name__ == '__main__':
    app.run(debug=True)