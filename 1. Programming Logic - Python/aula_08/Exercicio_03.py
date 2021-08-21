# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]

print(f'''
Tamanho da lista: {len(l)}
Maior valor da lista: {max(l)}
Maior valor da lista: {min(l)}
Soma do valores da lista: {sum(l)}
Lista na ordem crescente: {sorted(l)}
Lista na ordem crescente: {sorted(l, reverse=True)}
''')