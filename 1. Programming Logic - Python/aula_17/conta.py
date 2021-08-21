class Accounts:
    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance

    def __str__(self):
        if self.__balance <= 0:
            return f'Titular: {self.__owner}'
        else:
            return f'Titular: {self.__owner}\nSaldo: {self.__balance}'

    def deposit(self, value):
        oldBalance = self.__balance
        self.__balance += value

        return f'Depósito de {value} realizado com sucesso\n\nTitular: {self.__owner}\nSaldo anterior: {oldBalance}\nSaldo atual: {self.__balance}'
    
    def withdraw(self, value):
        if 0 >= self.__balance < value or value < 0:
            return f'Saldo insuficiente'
        else:
            oldBalance = self.__balance
            self.__balance -= value
            return f'Saque de {value} realizado com sucesso\n\nTitular: {self.__owner}\nSaldo anterior: {oldBalance}\nSaldo atual: {self.__balance}'
    
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, name):
        self.__owner = name
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance
        return self.__balance