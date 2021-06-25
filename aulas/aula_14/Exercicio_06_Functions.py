# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).
from random import randint


def convertNote(note = 0):
    if note >= 9: conNote = 'A'
    elif 9 > note >=8: conNote = 'B'
    elif 8 > note >=7: conNote = 'C'
    elif 7 > note >=6: conNote = 'D'
    elif 6 > note >=5: conNote = 'D'
    elif 5 > note: conNote = 'F'

    return conNote


note = float(randint(10,100)/10)
print(f'Nota {note:.2f} - {convertNote(note)}')