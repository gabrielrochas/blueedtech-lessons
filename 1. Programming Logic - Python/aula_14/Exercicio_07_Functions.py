# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles 
# forem iguais, imprima que eles são iguais.

from random import randint

def compareValues(n1 = 0, n2 = 0):
    if n1 < n2: 
        print(f'Dos valores {n1} e {n2} - {n1} é menor')
    elif n1 > n2: 
        print(f'Dos valores {n1} e {n2} - {n2} é menor')
    else:
        print(f'Valore {n1} e {n2} são iguais')


compareValues(randint(0,100), randint(0,100))