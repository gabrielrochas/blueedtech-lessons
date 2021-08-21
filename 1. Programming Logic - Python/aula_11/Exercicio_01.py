# 1. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

from names import get_first_name;
from random import randint;
from datetime import date;
currentYear = date.today().year;
# Generate some worker data
worker = {'name': get_first_name(), 'birthYear': randint(1950,2000), 'ctps': randint(0,100)*100};
# Calculate worker's age
worker['age'] = currentYear - worker['birthYear']
print(worker);
# Check if ctps number is diferent to 0
# If True add the hired year of worker
if worker.get('ctps') != 0:
    worker['hiredYear'] = int(input('Digite o ano de contratação: '));
    if worker.get('age') < 65 or (currentYear - worker.get('hiredYear')) < 35:
        # Check if worker age is bigger than 65
        # If True, worker should be already retired
        ageToRetire = (65 - worker.get('age')) if worker.get('age') < 65 else 0;
        # Check if worker hired year is bigger than 35
        # If True, worker should be already retired
        timeToRetire = 35 - (currentYear - worker.get('hiredYear')) if (currentYear - worker.get('hiredYear')) < 35 else 0;
        # Assign value to retired year.
        # ageToRetired or timeToRetired depends wich is smaller
        worker['retiredYear'] = (currentYear + ageToRetire) if ageToRetire < timeToRetire else (currentYear + timeToRetire);
        if ageToRetire == 0 or timeToRetire == 0:
            retire= 'Vá curtir a sua velhice';
        elif ageToRetire < timeToRetire:
            retire= 'Pessoa aposenta por idade';
        else:
            retire= 'Pessoa aposenta por tempo de serviço';
print(f'\n{retire}');
for i, d in worker.items():
    print(i.capitalize(),' - ', d);
# print(worker);
