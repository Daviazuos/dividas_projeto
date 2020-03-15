import datetime
from dateutil.relativedelta import relativedelta

def meses(numero_mes):
    dict_meses = {
        '01': 'janeiro',
        '02': 'fevereiro',
        '03': 'março',
        '04': 'abril',
        '05': 'maio',
        '06': 'junho',
        '07': 'julho',
        '08': 'agosto',
        '09': 'setembro',
        '10': 'outubro',
        '11': 'novembro',
        '12': 'dezembro'
    }
    return dict_meses[numero_mes]

def ChoiceCardMonth(Day, CardLimit):
    Month = datetime.datetime.today()
    if int(Day[-2:]) <= int(CardLimit[-2:]):
        Month = datetime.datetime.now().month
    elif int(Day[-2:]) > int(CardLimit[-2:]):
        Month = datetime.datetime.now() + relativedelta(months=+1)
    AdjustDate = [str(datetime.datetime.now().year), str(Month.month).zfill(2), str(CardLimit[-2:])]
    return '-'.join(AdjustDate)