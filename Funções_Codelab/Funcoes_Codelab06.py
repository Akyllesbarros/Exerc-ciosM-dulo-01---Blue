# 6. Escreva uma função que, dado um número nota representando a nota de um estudante,
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota Conceito
# >=9.0 A
# >=8.0 B
# >=7.0 C
# >=6.0 D
# <=4.0 F



def conceito(nota) :
    if nota >= 9.0 :
        return 'A'
    if nota >= 8.0 :
        return 'B'
    if nota >= 7.0 :
        return 'C'
    if nota >= 6.0 :
        return 'D'
    if nota >= 5.0 :
        return 'E'

print(conceito(5))