# Faça um programa, com uma função que necessite de um parametro. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

from random import randint

def checkNum(num):
    # Verify if num is positive or negative
    if num > 0:
        value = 'P';
    else:
        value = 'N';
    return value;

# Random int
num = randint(-10,10);
# Assign checkNum() to var value
value = checkNum(num);
# Print 
print(f'{num} - {value}')