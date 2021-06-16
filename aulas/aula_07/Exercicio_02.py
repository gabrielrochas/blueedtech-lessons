# 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.

while True:
    num = int(input('Digite um para tabuada ou 0 (zero) para sair: '))
    print('\n')
    if num == 0:
        print('Você finalizou o programa!')
        break
    
    c = 1;
    print('Tabuada Multiplicação de ', num )
    while c <= 10:
        val = num * c
        print(f'{c} x {num} = {val}')
        c += 1
    
    