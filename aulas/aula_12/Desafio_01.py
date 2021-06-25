# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma 
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando 
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
from names import get_first_name;
from random import randint
import os;
persons = list();
women = list();
overAge = list();
age = 0;
while True:
    person = {
        'name': get_first_name(),
        'gender': randint(0,1),
        'age': randint(1,100)
    }
    person['gender'] = 'f' if person['gender'] == 0 else 'm'
    # Create a women list
    if person['gender'] == 'f':
        women.append(person.copy());
    # Just print person inserted
    for i, d in person.items():
        print(f'{i} - {d}');
    # Copy person to a list
    persons.append(person.copy());
    age += person['age']; # Sum all ages
    if person['age'] > (age / len(persons)): overAge.append(person['age'])

    # cont = input('Deseja continuar Sim ou Não? ').strip().lower()[0];
    # Exit 
        
    cont = input('Digite NÃO para sair do programa ').strip().lower()[0];
    if cont == 'n': break

os.system('cls' if os.name == 'nt' else 'clear'); # clear terminal
# People inserted
print(f'Pessoas cadastradas: {len(persons)}')
# Sum of all ages
print(f'Todas as idades somadas: {age}')
# Age average
print(f'Média de idade da pessoas cadastradas: {age / len(persons)}')
# Ages higher average
print(overAge)
# Women list
print(women)
# for w in persons:

