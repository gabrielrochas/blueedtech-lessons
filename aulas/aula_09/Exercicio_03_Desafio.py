# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
numbers = []
games = int(input('Digite quantos jogos deseja fazer: '))
i = x = 0
for i in range(games):
    numbers.append([])
    for x in range(6):
        num = randint(1,60)
        if num not in numbers:
            numbers[i].append(num)
        else:
            print(f'Número {num} já existe na lista')
            x =- 1
    numbers[i].sort();
i = 1
for num in numbers:
    print(f'Jogo {i}: ', end=" ")
    for n in num:
        print (n, end=' ')
    print('\n')
    i += 1