# Desafio: Continuando o exercício 3 crie agora um boletim escolar, 
# seu programa deve receber 5 notas de 15 alunos, 
# assim como o nome desses alunos, o programa tem que calcular a média 
# desse aluno e mostrar a situação dele, seguindo os mesmos critérios 
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as 
# situações dos 15 alunos de uma vez só

import tabulate # Format the list in tables. Run in terminal --> pip install tabulate
from names import get_first_name # Generate random names. Run in terminal --> pip install names
from random import uniform

students = []
student = {}

for i in range(0,16):
    media = 0
    student['Nome'] = get_first_name()
    for x in range(1,6):
        nota = round(uniform(0,10), 2)+1
        student['Nota '+str(x)] = nota
        media += (nota / 5)
    student['Media'] = round(media, 2)
    if student['Media'] >= 7:
        student['Status'] = 'Aprovado';
    elif 5 < student['Media'] < 7:
        student['Status'] = 'Recuperação';
    else: 
        student['Status'] = 'Reprovado';
    students.append(student.copy())

header = students[0].keys()
rows = [x.values() for x in students]
print(tabulate.tabulate(rows, header, tablefmt='grid'))

