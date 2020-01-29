from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField

class fields(FlaskForm):
    parcelas = DecimalField("Parcelas")
    nome = StringField("Nome")
    valor = DecimalField("Valor")