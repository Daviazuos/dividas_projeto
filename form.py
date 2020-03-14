from flask_wtf import FlaskForm
from wtforms import StringField,DecimalField, BooleanField,DateField, validators

class fields(FlaskForm):
    parcelas = DecimalField("Parcelas",[validators.optional()])
    nome = StringField("Nome")
    valor = DecimalField("Valor")
    vencimento = DateField("vencimento")
    fixa = BooleanField('fixa',[validators.optional()])
    status = StringField('status',[validators.optional()])