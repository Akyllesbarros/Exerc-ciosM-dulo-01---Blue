
# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.


from random import randint

N1 = (randint(1, 50))
N2 = (randint(1, 50))
N3 = (randint(1, 50))
N4 = (randint(1, 50))
N5 = (randint(1, 50))

tupla = (N1, N2, N3, N4, N5)
maior = max(tupla)
menor = min(tupla)
print(f'tupla {tupla}\nO maior valor dessa tupla é {maior}\nO menor valor dessa tupla é {menor}')






