# 3. Faça um programa com uma função chamada somaImposto. A função possui dois 
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em 
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o 
# valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto = 0, custo = 0):
    valor = custo * ((taxaImposto / 100) + 1)

    return valor


imposto = float(input('Digite o valor do imposto (%): '))
custo = float(input('Digite o valor do custo: '))
custoImposto = somaImposto(imposto, custo)

print(f'Valor do custo + imposto é: {custoImposto:.2f}')