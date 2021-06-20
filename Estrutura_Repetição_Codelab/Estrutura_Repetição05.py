#01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break
import os
soma = 0
mult = 0
maior = 0
menu = 0
while menu != 5 :
    valor1 = int(input('Digite o primeiro valor: '))
    os.system('cls')
    valor2 = int(input('Digite o segundo valor: '))
    os.system('cls')
    menu = int(input('''Por favor, selecione uma opção abaixo: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\n'''))
    if menu == 1 :
      soma = valor1 + valor2 
      os.system('cls')
      print(f'Soma = {soma}')
    if menu == 2 :
        mult = valor1 * valor2
        os.system('cls')
        print( f'Multiplicação = {mult}')
    if menu == 3 :
        if valor1 >= valor2 :
            os.system('cls')
            print(f'Maior valor: {valor1}')
        elif valor2 > valor1 :
            os.system('cls')
            print(f'Maior valor: {valor2}')
        else : 
            os.system('cls')
            print(f' {valor1} é o mesmo!')
    if menu == 4 :
        os.system('cls')
        continue
        