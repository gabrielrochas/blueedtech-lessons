# Exercícios Tuplas:
# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.
from random import randint

tp = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))

print(f'Valores na tupla: {tp}')

print(f'Valor no menor número: {sorted(tp)[0]}')
print(f'Valor no maior número: {sorted(tp)[len(tp) - 1]}')