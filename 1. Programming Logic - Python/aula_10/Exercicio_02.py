# 01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com essa formatação:
# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 
from random import randint

matrix = []
for x in range(3):
    matrix.append([])
    for y in range(3):
        matrix[x].append(randint(0,100))
for line in matrix:
    for number in line:
        print(f'[ {number} ]', end=' ')
    print('\n')