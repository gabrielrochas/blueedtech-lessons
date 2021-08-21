# 05 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

from time import sleep

optn = ' '
options = ['1','2','3','4','5']

while optn != '5' or optn == '4':
    num1 = float(input('Digite um número: ').replace(',','.'))
    num2 = float(input('Digite outro número: ').replace(',','.'))

    optn = str(input('''
Qual operação deseja realizar:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Operação: '''))
        
    if optn not in options:
        print('Opção inválida. Tente novamente')
    else:
        if optn == '1':
            print(f'Soma de {num1:.2f} + {num2:.2f} = {(num1 + num2):.2f}')
        elif optn == '2':
            print(f'Produto de {num1:.2f} x {num2:.2f} = {(num1 * num2):.2f}')
        elif optn == '3':
            if num1 > num2:
                print(f'Número {num1:.2f} é maior')
            elif num1 < num2:
                print(f'Número {num2:.2f} é maior')
            else:
                print('Os número são iguais')
        elif optn == '4':
            print('Digite novos números\n')
        else:
            print('Sair do programa')
    sleep(2)