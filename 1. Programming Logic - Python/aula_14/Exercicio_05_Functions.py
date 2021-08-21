# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 
# 1,68 e pese 75kg.

def calcImc():
    imc = 75 / (1.68 * 1.68)
    return f'O IMC é {imc:.2f}'

print(calcImc())