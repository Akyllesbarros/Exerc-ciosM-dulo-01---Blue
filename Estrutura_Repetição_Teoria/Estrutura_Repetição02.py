
#02 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = 0
while sexo != 'M' or sexo != 'F' :
    sexo = input("Olá, Por favor digite seu Sexo no formato [ M (Masculino) ou F (Feminino) ]: ")
    if sexo != 'M' or sexo != 'F' :
        print("Não entendi, por favor, escreva novamente: ") 
    elif sexo == 'M' or sexo == "F" : 
        print("Acertou")
          