# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente

lista = []
numero = 1
while numero != 0: 
    numero = int(input("Digite um número:\n"))
    if numero not in lista :
        lista.append(numero) 
lista.pop()   
sorted(lista)
print(lista)