# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
# 1,68 e pese 75kg.

def imc(altura, peso) :
    imc = peso // altura ** 2
    return imc

print(imc(1.68, 75))