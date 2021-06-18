# 02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

lista = []
pares = []
impares = []
numero = 1
while numero != 0 :
    numero = int(input('Digite um número: '))
    lista.append(numero)
    if numero % 2 == 0 :
        pares.append(numero) 
    else : 
        impares.append(numero)
pares.pop()
lista.pop()
print(f'''lista: {lista}
pares: {pares}
impares: {impares}''')


