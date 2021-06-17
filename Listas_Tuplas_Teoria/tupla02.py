# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.


valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
valor3 = int(input('Digite um valor: '))
valor4 = int(input('Digite um valor: '))
tupla = (valor1, valor2, valor3, valor4)
tres = tupla.index(3)
nove = tupla.count(9)

print(f'O valor 9 apareceu {nove} vezes\nO valor 3 foi digitado na posição {tres}')