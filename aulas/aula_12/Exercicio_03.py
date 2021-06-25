# Faça um programa que leia nome e média de um aluno, guardando também a situação 
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para 
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é 
# reprovado.
from names import get_first_name;
from random import randint
student = {
    'name': get_first_name(),
    'media': float(randint(10,100)/10)
}
if student['media'] >= 7: student['status'] = 'Aprovado';
elif 5 < student['media'] < 7: student['status'] = 'Recuperação';
else: student['status'] = 'Reprovado';

print(f'Aluno {student["name"]} - Média {student["media"]} - Status {student["status"]}')