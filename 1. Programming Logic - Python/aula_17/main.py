# Fazer o método sacar(), se o saldo for menor ou igual a 0, retorne uma mensagem dizendo que o saldo é insuficiente, 
# caso o contrário, realize a operação de saque e mostre o saldo atual dessa conta;

from conta import Accounts


if __name__ == '__main__':
    # bank = []
    # while True:
    #     account = Accounts(input('Titular: '))
    #     bank.append(account)

    #     check = input('Deseja continuar: [Sim ou Não]: ').strip().lower()[0]
    #     if check == 'n':
    #         break

    acc01 = Accounts('Gabriel', 100)
    
    print(acc01.balance)