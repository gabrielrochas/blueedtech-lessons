# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".
from time import sleep
i = count = 0
questions = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?'
]

results = ['inocente', 'suspeito', 'cúmplice', 'assassino']

print('Vou fazer algumas perguntas. Por favor, responda "sim" ou "não"\n')
sleep(2)
for question in questions:
    # print(question)
    for i in range(0,3):
        answer = str(input(f'{question[i]} Sim ou Não? ')).lower()[0]
        if answer == 'n': # if answer is No break and no count.
            break

        if answer == 's': # if answer is yes break and count + 1.
            count += 1
            break

        if answer != 's' and answer != 'n':
            print(f'Resposta errada.\nVou perguntar novamente: {question}')
        
        if i == 1:
            print('Você só tem mais uma change.\nCuidado! Se responder errado novamente vou considerar a sua resposta como SIM!')
        
        if i == 2:
            count += 1
        # i += 1
        sleep(1)
    print('\n')
sleep(1)
print(f'''
Respotas SIM: {count}
Estamos processando as suas respostas
''')
i = 0
for i in range(3):
    print(f'.')
    i += 1
    sleep(1)
print('\n')

# if count < 0 and count >= 2:
#     print('Você é suspeito do crime. Voltaremos a fazer contato contigo.')
# elif count >= 3 and count <= 4:
#     print('Você foi considerado cúmplice. Ficará sob custódia da justiça')
# elif count == 5:
#     print('Você foi considerado culpado. Seguirá diretamente para o presídio')
# else:
#     print('Você está livre')
