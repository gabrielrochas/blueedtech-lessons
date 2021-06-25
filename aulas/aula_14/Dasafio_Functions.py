# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no 
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que 
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro 
# terá 29 dias
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatDate(userDate):
    try:
        userDate = datetime.strptime(userDate, '%d/%m/%Y')
        return userDate.strftime('%d de %B de %Y')
    except ValueError:
        return 'Data inválida'

userDate = input('Informe uma data 00/00/0000: ')
print(formatDate(userDate))
