
#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

import os

contIdade = 0
contSexo = 0
contMulherMenor20 = 0
idade = 0
continua = 0
sexo = ' '
while True : 
    os.system('cls')
    idade = int(input('Qual é sua idade?\n'))
    sexo = str(input('Digite seu sexo: [M/F]\n')).upper().strip()[0]
    
    if idade >= 18 :
        contIdade += 1 
    if sexo == 'M' :
        contSexo += 1
    if idade < 20 :
        if sexo == "F":
            contMulherMenor20 += 1    
    
    continua = int(input('Aperte 1 para continuar ou 0 para parar...\n'))   
    if continua == 1 : 
        continue

    elif continua != 1: 
        print(f'''{contIdade} Pessoas tem mais de 18 anos.
{contSexo} Homens cadastrados.
{contMulherMenor20} Mulheres menores de 20 anos. ''')
        break
     
