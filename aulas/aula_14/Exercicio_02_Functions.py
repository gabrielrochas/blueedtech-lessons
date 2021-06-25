# 2. Faça um programa, com uma função que necessite de um argumento. A função retorna 
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for 
# negativo e ‘0’ se for 0.
from random import randint

def defineValue(num = 0):
    if num == 0: numValue = '0'
    elif num > 0: numValue = 'P'
    else: numValue = 'N'

    return numValue

num = randint(-10,10)
numValue = defineValue(num)
if numValue == '0': numValue = 'Neutro'
elif numValue == 'P': numValue = 'Posito'
else: numValue = 'Negativo'

print(f'Número {num} é {numValue}')