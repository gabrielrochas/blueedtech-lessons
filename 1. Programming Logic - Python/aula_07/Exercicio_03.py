# 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

from datetime import date
from random import randint

birthyear = {}
age = {}
curYear = date.today()
c = underAge = ofAge = 0

for c in range(7):
    birthyear[c] = randint(1920, curYear.year)
    age[c] = curYear.year - birthyear[c]
    print(f'Idade pessoa {c+1}: {age[c]}')
   
    if int(age[c]) < 18:
        underAge += 1
    else:
        ofAge += 1

    c += 1

print(f'\n\nPessoas com menos de 18 anos: {underAge}\nPessoas com 18 anos ou mais: {ofAge}')