# 06 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos
from random import randint
person = {}
age = {}
i = 1
x = ofAge = men = womenUnder20 = 0
while True:
    person[x] = randint(0,1) # 0 to woman and 1 to man
    age[x] = randint(0,99)
    i += x
    
    if person[x] == 0:
        gender = 'Feminino'
    else:
        gender = 'Masculino'

    print(f'Pessoa {i} - Sexo: {gender} | Idade: {age[x]}')
    if age[x] > 18:
        ofAge += 1
    if person[x] == 1:
        men += 1
    if person[x] == 0 and age[x] < 20:
        womenUnder20 += 1

    x += 1

    out = randint(0,1) # 1 to exit
    if out == 1:
        break

print(f'''
Pessoas com mais de 18 anos: {ofAge}
Homens cadastrados: {men}
Mulheres com menos de 20 anos: {womenUnder20}''')