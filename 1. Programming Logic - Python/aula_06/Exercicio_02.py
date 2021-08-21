#01 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

genderF = 'f';
genderM = 'm';

askGender = ' ';

while askGender not in 'fm':
    askGender = str(input('Digite o seu sexo biológico [F ou M]: ')).lower()[0];
    if askGender != genderF and askGender != genderM:
        print('Sexo errado. Digite novamente.\n');
    else: 
        print('Ok');