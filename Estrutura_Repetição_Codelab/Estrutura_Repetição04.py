#04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados

numero = 0
par = 0
resultpar = 0
contagem = 0
for c in range(0, 6) :
    numero = int(input(' Digite um número: '))
    resultpar = numero % 2
    if resultpar == 0 :
        par += numero
        contagem += 1 
print(f"Foram digitados {contagem} números pares e a soma entre eles é de {par}")