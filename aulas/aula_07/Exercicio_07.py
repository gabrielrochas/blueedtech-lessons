# 07 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# C) Qual é o nome do produto mais barato
from random import uniform

products = { }
price = { }

x = y = 0

while True:
    y += 1
    print(y)
    price[x] = uniform(1.00,2000.00)
    print(f'Produto {y} custa R$ {price[x]:.2f}')

    cont = str(input('Deseja comprar mais produtos [Sim ou Não]?: ')).lower()[0]

    if cont == 'n':
        break
    
    x += 1