# #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

ano = 0
maioridade = 0
menoridade = 0
for c in range(0,7) :
    ano = int(input('Por favor, Digite seu ano de nascimento: '))
    ano = 2021 - ano 
    if ano >= 18 :
        maioridade += 1
    else : 
        menoridade += 1
print(f'''{maioridade} Já atingiram a maioridade mas
{menoridade} ainda são menores.
''')
