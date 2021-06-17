# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.


l = [5, 7, 2, 9, 4, 1, 3]
ltamanho = len(l)
lmaior = max(l)
lmenor = min(l)
lsoma = sum(l)
lcresc = sorted(l)
ldecresc = sorted(l, reverse=True)

print(f"Lista: {l}\nTamanho: {ltamanho}\nMaior valor: {lmaior}\nMenor valor: {lmenor}\nSoma: {lsoma}\nOrdem Crescente: {lcresc}\nOrdem Decrescente: {ldecresc}")
