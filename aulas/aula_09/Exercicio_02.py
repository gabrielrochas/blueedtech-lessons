# 02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas
from random import randint
myList = []
even = []
odd = []
while True:
    myList.append(randint(0,1000))
    print(myList[(len(myList)-1)])
    if (myList[(len(myList)-1)]) % 2 == 0:
        even.append(myList[(len(myList)-1)])
    else:
        odd.append(myList[(len(myList)-1)])
    exit = str(input('Digite "Não" para sair ou qualquer outra tecla para continuar? ')).strip().lower()[0]
    if exit == 'n':
        break
print(f'''
Lista principal: {myList}
Lista de números pares: {even}
Lista de número ímpares: {odd}''')