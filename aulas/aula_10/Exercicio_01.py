# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, 
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela 
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' 
# e  também quantos são maiores e quantos são menores de idade.
from names import get_first_name
from random import randint
from time import sleep
import os
persons = []
underAge = ofAge = 0
# Gera 5 pessoas com nome e idade aleatórios
for x in range(5):
    persons.append([])
    for y in range(1):
        persons[x].append(get_first_name())
        persons[x].append(randint(1,100))
        # Verifica se maior ou menor de idade
        if persons[x][1] < 18:
            underAge += 1
        else:
            ofAge += 1
## Tratando plural 
minor = 'menores' if underAge > 1 else 'menor'
major = 'maiores' if ofAge > 1 else 'maior'
# Imprimindo lista de nomes
os.system('cls' if os.name == 'nt' else 'clear') # Limpa terminal
for x, y in persons:
    age = 'maior' if y > 18 else 'menor'
    print(f'{x} é {age} de idade')
print(f'A lista tem {underAge} {minor} e tem {ofAge} {major}')
sleep(5)
os.system('cls' if os.name == 'nt' else 'clear') # Limpa terminal