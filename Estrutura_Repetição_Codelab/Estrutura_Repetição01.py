#01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.


listapeso = list()
pesomax = 0
for c in range(4): 
    peso = int(input("Digite o peso: "))
    listapeso.append(peso)
print(f"O maior peso digitado foi : {max(listapeso)}")