# Desafio: Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os palpites diga ao jogador se o número do computador é maior ou menor ao que ele digitou,no final mostre quantos palpites foram necessários para vencer.

from time import sleep;
from random import randint;

rdmNumber = randint(0,10);

userNumber = int(input('Qual número o computador pensou? R: '));
count = 1;

while userNumber != rdmNumber:
    sleep(1);
    print('Oops. Você errou, tente novamente!');
    userNumber = int(input('Qual número o computador pensou? R: '));
    count += 1;

print(f'Parabéns! Você acertou na {count}ª tentiva.')