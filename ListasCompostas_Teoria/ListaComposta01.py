# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

lista_nomes = []
contIdadeMaior = 0
contIdadeMenor = 0
for i in range(4):
    pessoas = []
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    pessoas.append(nome)
    pessoas.append(idade)
    lista_nomes.append(pessoas[:])
    if idade >= 18 :
        print(f'{nome} é maior de idade.')
        contIdadeMaior += 1
    elif idade < 18 : 
        print(f'{nome} é menor de idade.')
        contIdadeMenor += 1
print(f' São {contIdadeMaior} maiores de idade e {contIdadeMenor} menores de idade! ')
    
    

