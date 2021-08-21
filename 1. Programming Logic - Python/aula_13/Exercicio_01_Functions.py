# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições
# < 16 = NEGADO
# 16, 18 e mais de 70 = OPCIONAL
# As demais = OBRIGATORIO

from random import randint;
from datetime import date;
import os;

def vote(birhtYear = 0):
    # Calcula idade
    age = date.today().year - birhtYear;
    # Faz a verificação da idade
    if age < 16:
        mustVote = 'NEGADO';
    elif (16 <= age < 18) or age > 70:
        mustVote = 'OPCIONAL';
    else:
        mustVote = 'OBRIGATORIO';
    # Retorna ida e diz se pessoa pode votar ou não
    return f'Idade: {age}\nVoto: {mustVote}';

os.system('cls' if os.name == 'nt' else 'clear'); # clear terminal
mustVote = vote(randint(1900,2021));
print(mustVote);