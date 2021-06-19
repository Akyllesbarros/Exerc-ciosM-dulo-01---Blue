# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

lista_nomes = []
pessoas = []

for i in range(4):
    nome = input('Digite o nome: ')
    idade = (input('Digite a idade: '))
    pessoas.append(nome)
    pessoas.append(idade)
    lista_clientes.append(pessoas[:])