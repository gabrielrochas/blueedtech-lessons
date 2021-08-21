# Se a pessoa tiver mais que 30 anos, as calorias de 'comer' são em dobro
# Se a pessoa tiver menos que 30 anos, as colorias de 'malhar' são em dobro

from random import randrange, uniform
from names import get_first_name

class Person:
    def __init__(self, name, age, weight): # Método construtor de atributos
        self.name = name
        self.age = age
        self.weight = weight

    def eat(self, calories):
        if self.age > 30:
            self.weight += (calories*2)
        else:
            self.weight += calories
    def workout(self, calories):
        if self.age <= 30:
            self.weight -= (calories*2)
        else:
            self.weight -= calories
    def showData(self):
        return f'Nome: {self.name}\nIdade: {self.age}\nPeso: {self.weight}'
dictPersons = {}


name = get_first_name()
age = randrange(100)
weight = randrange(10,50) if age < 10 else randrange(50,120)
dictPersons = Person(name, age, weight)

print(dictPersons.showData())