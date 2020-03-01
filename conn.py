import sqlite3 as sql

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

def select_db():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("select * from dados")
        dados = cur.fetchall()
        total = str(sum([float(x[2]) for x in dados]))
    return [dados, total]

def insert_db_card(form):
    msg = "Record successfully added"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO dados_cartao (nome,vencimento) VALUES(?, ?)",(str(form.nome.data),str(form.vencimento.data)))
            con.commit()
        except Exception:
            msg = "Error"
    return msg

def insert_db(form):
    msg = "Record successfully added"
    with sql.connect("database.db") as con:
        cur = con.cursor()
        try:
            if form.fixa.data:
                parcela = ''
                cur.execute("INSERT INTO dados (nome,parcelas,valor,vencimento) VALUES(?, ?, ?, ?)",(str(form.nome.data), parcela, float(form.valor.data), str(form.vencimento.data)))
                con.commit()
            else:
                for parcela in range(1, int(form.parcelas.data) + 1):
                    cur.execute("INSERT INTO dados (nome,parcelas,valor,vencimento) VALUES(?, ?, ?, ?)",(str(form.nome.data), parcela, float(form.valor.data),str(form.vencimento.data)))
                con.commit()
        except Exception:
            msg = "Error"
    return msg