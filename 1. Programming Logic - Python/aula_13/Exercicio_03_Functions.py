# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.
from random import randint;

def sumValues(note1 = 0, note2 = 0, note3 = 0):
    values = [note1, note2, note3];
    sumNotes = sum(values);
    avarage = avarageNotes(sumNotes, len(values));

    return f'{sumNotes:.2f} e a média das notes é {avarage:.2f}';

def avarageNotes(sumNotes, lengthValues):
    avarage = sumNotes / lengthValues;
    return avarage;

# Generate some notes
note = dict()
for i in range(0,3):
    note[f'n{i+1}'] = float(randint(10,100)/10);


values = sumValues(note['n1'], note['n2'], note['n3']);

print(f'A soma dos valores é {values}');