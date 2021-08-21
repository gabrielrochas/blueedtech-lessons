# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a 
# soma desses três argumentos.
from random import randint
import random

# Function sum values
def sumValues(values):
    sumNum = sum(values)

    return f'A soma dos valores é {sumNum}'

num = []
for i in range(0,3):
    num.append(randint(0,100))

print(f'Valores - {num}')
sumNum = sumValues(num)
print(sumNum)  