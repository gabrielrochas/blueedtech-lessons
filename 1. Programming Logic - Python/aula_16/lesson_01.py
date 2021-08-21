#01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
from random import randint
class SoccerPlayer():
    def __init__(self, name = ' '):
        self.name = name
        self.match = 0
        self.goal = 0

    def matchs(self, match, goal = 0):
        self.match += match
        self.goal += goal
    
        return f'Jogador: {self.name}\nGols marcados: {self.goal}\n'

player1 = SoccerPlayer('Gabriel')

print(player1.matchs(1,randint(0,3)))

print(f'{player1.saveAll()}')