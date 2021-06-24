# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

def soma() :
    resultado = n1 + n2 + n3 
    return resultado

def media() :
    mediaN = soma() / 3
    print(f'A média é: {mediaN:.2f}')

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))
n3 = int(input('Digite n3: '))

soma()
media()


