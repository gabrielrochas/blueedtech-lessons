# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário 
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha 
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def extrasPay(salary = 0, hours = 0):
    valueHour = salary / 40
    hoursExtra = hours
    newSalary = salary
    if hours > 40:
        hoursExtra = hours - 40
        newSalary = salary + hoursExtra * valueHour * 1.5
        return f'Valor do salário é {salary:.2f}\nValor da hora trabalhada: {valueHour:.2f}\nFuncionário trabalhou {hoursExtra:.2f} horas extras.\nValor da hora extra: {hoursExtra * valueHour * 1.5:.2f}\nValor do salário atualizado: {newSalary:.2f}'
    return f'Salário sem alterações'


salary = float(input('Digite o salário: ').replace(',','.'))
hours = float(input('Digite as horas trabalhadas: ').replace(',','.'))
print(extrasPay(salary,hours))