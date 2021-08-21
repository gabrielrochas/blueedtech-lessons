# 02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.
from random import randint
matrix = []
even = line2 =0
for x in range(3):
    matrix.append([])
    for y in range(3):
        matrix[x].append(randint(0,100))
        # Soma de todos os números pares
        if matrix[x][y] % 2 == 0:
            even += matrix[x][y]
for line in matrix:
    for number in line:
        print(f'[ {number} ]', end=' ')
    print('\n')
print(f'''
A soma de todos os valores pares é: {even}
A soma de todos os da linha 3 é: {sum(matrix[2])}
O maior valor da linha 2 é: {max(matrix[1])}''')
