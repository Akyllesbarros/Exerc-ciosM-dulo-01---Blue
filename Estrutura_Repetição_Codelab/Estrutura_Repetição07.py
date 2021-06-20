
#03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.
contCaro = 0
listaPreco = list()
listaProduto = list()
n_min = 0
posMin = 0
indexMin = 0
while True: 
    produto = input('Digite o produto: ')
    preço = float(input('Digite o preço: '))
    listaProduto.append(produto)
    listaPreco.append(preço)
    listaMinimo = min(listaPreco)
    indexMin = listaPreco.index(listaMinimo)

    if preço > 1000 : 
        contCaro += 1
    continuar = int(input('Clique 1 para continuar e 0 para parar.'))
    if continuar == 1 :
        continue
    if continuar == 0 :
        print(f'''São {contCaro} produtos que custam mais de 1k
O total da compra é de R$ {sum(listaPreco)}
O produto mais barato é {listaProduto[indexMin]} 
''') 
        break


