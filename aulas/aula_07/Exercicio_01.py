# 01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos
from random import uniform

weight = {}
c = 0
heaviest = 0.00
lighter = 0.00

while c < 5:
    weight[c] = uniform(10.00, 150.00)+c
    print(f'Pessoa {c} - Peso {float(weight[c]):.2f}')
    
    if heaviest < weight[c]:
        heaviest = weight[c]
    
    if lighter == 0:
        lighter = weight[c]
    elif lighter > weight[c]:
        lighter = weight[c]
    c += 1
    
print(f'Maior peso: {float(heaviest):.2f}')
print(f'Menor peso: {float(lighter):.2f}')