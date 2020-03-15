import sqlite3 as sql
import datetime
import uuid
import funcoes

def insert_status(form):
    msg = "Record successfully added"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            for parcela in range(1, int(form.parcelas.data) + 1):
                cur.execute("INSERT INTO dados (status) VALUES(?)",(str(form.nome.status)))
            con.commit()
        except Exception:
            msg = "Error"
    return msg

def delete_database():
    msg = "Delete successfully"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            cur.execute("delete from dados")
            con.commit()
        except Exception:
            msg = "Error to delete"
    return msg

def edit_dividas():
    dados = []
    msg = "Record successfully edited"
    dados.insert(1, msg)
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            cur.execute("select nome from dados")
            dados.insert(0,cur.fetchall())
        except Exception:
            msg = "error"
            dados.insert(1,msg)
    return dados

def select_db(mes):
    ValuesCard = ''
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM dados")
        dados = cur.fetchall()
        cur.execute("SELECT * FROM dados_cartao")
        dados_cartao = cur.fetchall()

        dados_mes = [x for x in dados if x[3][5:7] == mes or x[5] == 'True']
        try:
            ValuesCard = [x for x in dados_cartao if x[3][5:7] == mes]
        except TypeError:
            pass
        total = sum([float(x[2]) for x in dados_mes])
        totalcard = sum([float(x[2]) for x in ValuesCard])

        total_geral = total + totalcard

    return [dados_mes, str(total_geral), mes, ValuesCard]

def select_db_card():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM dados_cartao")
        dados = [x for x in cur.fetchall()]
    return dados

def insert_db_card(form):
    msg = "Record successfully added"
    id_divida = uuid.uuid4()

    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO dados_cartao (nome,limitdate,id_divida) VALUES(?, ?, ?)",(str(form.nome.data),str(form.vencimento.data),str(id_divida)))
            con.commit()
        except Exception as e:
            msg = e
    return msg

def UpdateCard(Values):
    msg = "Record successfully added"
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("select * from dados_cartao where id_divida = {}".format("'"+Values[0]+"'"))
            CardDados = cur.fetchall()
            ValorAtual = [x[2] for x in CardDados]
            CardLimit = CardDados[0][7]
            BuyDate = funcoes.ChoiceCardMonth(Values[2],CardLimit)
            if ValorAtual[0]:
                NewValue = float(Values[1]) + float(''.join(ValorAtual[0][0]))
            else:
                NewValue = Values[1]
            cur.execute("UPDATE dados_cartao SET Valor = {}, vencimento = {} WHERE id_divida = {}".format(NewValue,"'"+BuyDate+"'","'"+Values[0]+"'"))
            cur.execute("COMMIT")
    except Exception as e:
        msg = e
    return msg


def insert_db(form):
    msg = "Record successfully added"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            if form.fixa.data:
                parcela = 'Divida Fixa'
                cur.execute("INSERT INTO dados (nome,parcelas,valor,vencimento,fixa) VALUES(?, ?, ?, ?, ?)",(str(form.nome.data), parcela, float(form.valor.data), str(form.vencimento.data), str(form.fixa.data)))
                con.commit()
            else:
                if int(form.parcelas.data) > 0:
                    for parcela in range(1, int(form.parcelas.data) + 1):
                        cur.execute("INSERT INTO dados (nome,parcelas,valor,vencimento,fixa) VALUES(?, ?, ?, ?, ?)",(str(form.nome.data), parcela, float(form.valor.data),str(form.vencimento.data), str(form.fixa.data)))
                    con.commit()
                else:
                    parcela = ''
                    cur.execute("INSERT INTO dados (nome,parcelas,valor,vencimento,fixa) VALUES(?, ?, ?, ?, ?)",(str(form.nome.data), parcela, float(form.valor.data),str(form.vencimento.data), str(form.fixa.data)))
                    con.commit()
        except Exception as e:
            msg = e
    return msg