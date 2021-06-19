# Utilizando os conceitos aprendidos até estruturas de repetição, crie um 
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
#
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de 
#   vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha 
#   de quantidade de rodadas, se não finalize o programa.

### Rock Paper Scissors ###

# from art import *
# options = ['Pedra','Papel','Tesoura'];
print('Rock Paper Scissors');
while True:
    rounds = str(input('Digite Quantas rodadas deseja jogar: ')).strip()[0]
    if rounds.isnumeric():
        break;
    else:
        print('Opção inválida. Você deve digitar um número inteiro\n');

for i in range(int(rounds)):
    for option in options:
        print(option);