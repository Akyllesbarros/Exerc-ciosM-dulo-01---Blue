# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
# forem iguais, imprima que eles são iguais.

def compara(n1, n2) : 
    if n1 > n2 :
        print(f'{n2}')
    elif n1 < n2 :
        print(f'{n1}')
    elif n1 == n2 :
        print('n1 é igual a n2!')

compara(5,5)
