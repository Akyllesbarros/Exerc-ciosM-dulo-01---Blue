#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.


# peso1 = int(input('Por favor, Digite o peso 1: '))
# peso2 = int(input('Por favor, Digite o peso 2: '))
# peso3 = int(input('Por favor, Digite o peso 3: '))
# peso4 = int(input('Por favor, Digite o peso 4: '))
# peso5 = int(input('Por favor, Digite o peso 5: '))
# maior = 0 
# for c in range(peso1, peso2, peso3, peso4, peso5) :
#     if peso1 > peso2 : 
#         maior = peso2
#     if peso2 > peso3 :
#         maior = peso2
#     if peso3 > peso4 : 
#         maior = peso3
#     if peso4 > peso5 : 
#         maior = peso4 
#     if peso5 > peso1 :
#         maior = peso5
    
# print(f"O maior peso é: {maior}")




# 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.


# int = int(input('Digite um número: '))

# for c in range(0, 11) :
#     resultado = c * int 
#     print(f'{c} x {int} = {resultado} ')


# #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

# ano = 0
# maioridade = 0
# menoridade = 0
# for c in range(0,7) :
#     ano = int(input('Por favor, Digite seu ano de nascimento: '))
#     ano = 2021 - ano 
#     if ano >= 18 :
#         maioridade += 1
#     else : 
#         menoridade += 1
# print(f'''{maioridade} Já atingiram a maioridade mas
# {menoridade} ainda são menores.
# ''')


#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados

# numero = 0
# par = 0
# resultpar = 0
# contagem = 0
# for c in range(0, 6) :
#     numero = int(input(' Digite um número: '))
#     resultpar = numero % 2
#     if resultpar == 0 :
#         par += numero
#         contagem += 1 
# print(f"Foram digitados {contagem} números pares e a soma entre eles é de {par}")


#01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break


####################################################################################################################
# import os 

# soma = 0
# mult = 0
# maior = 0
# menu = 0
# while menu != 5 :
#     valor1 = int(input('Digite o primeiro valor: '))
#     os.system('cls')
#     valor2 = int(input('Digite o segundo valor: '))
#     os.system('cls')
#     menu = int(input('''Por favor, selecione uma opção abaixo: 
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa\n'''))
#     if menu == 1 :
#       soma = valor1 + valor2 
#       os.system('cls')
#       print(f'Soma = {soma}')
#     if menu == 2 :
#         mult = valor1 * valor2
#         os.system('cls')
#         print( f'Multiplicação = {mult}')
#     if menu == 3 :
#         if valor1 >= valor2 :
#             os.system('cls')
#             print(f'Maior valor: {valor1}')
#         elif valor2 > valor1 :
#             os.system('cls')
#             print(f'Maior valor: {valor2}')
#         else : 
#             os.system('cls')
#             print(f' {valor1} é o mesmo!')
#     if menu == 4 :
#         os.system('cls')
#         continue
        
#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

#####################################################################################################
# import os

# contIdade = 0
# contSexo = 0
# contMulherMenor20 = 0
# idade = 0
# continua = 0
# sexo = ' '
# while True : 
#     os.system('cls')
#     idade = int(input('Qual é sua idade?\n'))
#     sexo = str(input('Digite seu sexo: [M/F]\n')).upper().strip()[0]
    
#     if idade >= 18 :
#         contIdade += 1 
#     if sexo == 'M' :
#         contSexo += 1
#     if idade < 20 :
#         if sexo == "F":
#             contMulherMenor20 += 1    
    
#     continua = int(input('Aperte 1 para continuar ou 0 para parar...\n'))   
#     if continua == 1 : 
#         continue

#     elif continua != 1: 
#         print(f'''{contIdade} Pessoas tem mais de 18 anos.
# {contSexo} Homens cadastrados.
# {contMulherMenor20} Mulheres menores de 20 anos. ''')
#         break
     


#03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.


while True : 
    nomeProduto = input('Digite o nome do Produto:\n')
    preço = input('Digite o preço desse produto:\n')

    if 
    input('Deseja continuar')
    continue
