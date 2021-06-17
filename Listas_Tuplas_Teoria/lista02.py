
# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

lista = []
verificador = 0

lista.append(input('Você telefonou para Vítima?\n').upper().strip()[0])
if lista[0] == 'S':
    verificador += 1
lista.append(input('Você esteve no Local do Crime?\n').upper().strip()[0])
if lista[1] == 'S':
    verificador += 1
lista.append(input('Você esteve no Local do Crime?\n').upper().strip()[0])
if lista[2] == 'S':
    verificador += 1
lista.append(input('Você esteve no Local do Crime?\n').upper().strip()[0])
if lista[3] == 'S':
    verificador += 1
lista.append(input('Você esteve no Local do Crime?\n').upper().strip()[0])
if lista[4] == 'S':
    verificador += 1


if verificador == 2 :
    print(" Ok, você ainda é um SUSPEITO")
if verificador == 5 :
    print("Então você é o Assassino, está preso! ")
if verificador == 4 or verificador == 3  :
    print("Você foi Cumplice! ")
else : 
    print(" Por enquanto não encontramos nada... ")

