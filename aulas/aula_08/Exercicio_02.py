# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
from random import randint

tp = (randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Valores da tupla: {tp}')
if tp.count(9) != 0:
    print(f'Quantos 9 na tupla: {tp.count(9)}')
else:
    print('Não foi encontrado nenhum 9 na tupla')
if tp.count(3) != 0:
    print(f'Posição do 3 na tupla: {tp.index(3)}')
else:
    print('Não foi encontrado nenhum 3 na tupla')