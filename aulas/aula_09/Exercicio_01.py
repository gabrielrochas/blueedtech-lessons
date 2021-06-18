# 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.
from random import randint
myList = []
while True:
    # num = randint(0,100)
    num = int(input('Digite um número: '))
    print(f'Número: {num}')
    if num not in myList:
        myList.append(num)
    else:
        print('Numero já existe')
    exit = str(input('Deseja digitar outro número SIM ou NÃO?: ')).strip().lower()[0]
    if exit == 'n':
        break
myList.sort()
print(f'Lista gerada: {myList}')    
