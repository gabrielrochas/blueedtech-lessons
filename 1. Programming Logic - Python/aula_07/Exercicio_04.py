# 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados
from random import randint
num = {}
count = sumNum = 0
for x in range(6):
    num[x] = randint(0,1000)
    print(num[x])

    if num[x] % 2 == 0:
        sumNum += num[x]
        count += 1

print(f'''\n
Soma dos números pares digitados: {sumNum}
Quantidade de números pares digitados: {count}
''')