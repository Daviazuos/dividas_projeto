from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField, DateField,  BooleanField

class fields(FlaskForm):
    parcelas = DecimalField("Parcelas")
    nome = StringField("Nome")
    valor = DecimalField("Valor")
    vencimento = StringField("vencimento")
    fixa = BooleanField('fixa')
    status = StringField('status')