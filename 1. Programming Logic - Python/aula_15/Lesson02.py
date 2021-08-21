# Crie uma classe chamada Conta para simular as operações de uma conta corrente.
# Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar.
# Crie um objeto da classe Conta e teste os atributos e métodos implementados.​
# Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, 
# caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, value):
        if 0 >= self.balance < value:
            return f'Saldo insuficiente'
        else:
            self.balance -= value
            return f'Saque de {value} realizado com sucesso'

    def deposit(self, value):
        self.balance += value
        return f'Deposito de {value} realizado com sucesso!'

    def statement(self):
        return f'Titular: {self.owner}\nSaldo: {self.balance}'

p1 = Account(
    owner='Gabriel',
    balance= 0
)

print(p1.deposit(10))
print(p1.withdraw(5))
print(p1.statement())
