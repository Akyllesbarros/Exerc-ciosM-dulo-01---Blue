#DESAFIO 04
nome = input("Olá, para iniciar, digite seu nome: ")
saque = int(input(f"Olá {nome}, Quanto você quer sacar hoje? [Mín R$ 10 e Máx R$ 600]\n"))
# Notas de 1, 5, 10, 50, 100. 

nota100 = nota50 = nota10 = nota5 = nota1 = 0
if saque >= 10 and saque <= 600 : 
    if saque >= 100 : 
        nota100 = saque // 100 
        saque -= 100 * nota100
    if saque >= 50 : 
        nota50 = saque // 50
        saque -= 50 * nota50
    if saque >= 10 : 
        nota10 = saque // 10
        saque -= 10* nota10
    if saque >= 5 : 
        nota5 = saque // 5
        saque -= 5 * nota5
    if saque >= 1 : 
        nota1 = saque
        saque -= nota1 
    print(f"Você recebeu {nota100} notas de cem reais.")
    print(f"Você recebeu {nota50} notas de cinquenta reais")
    print(f"Você recebeu {nota10} notas de dez reais")
    print(f"Você recebeu {nota5} notas de cinco reais")
    print(f"Você recebeu {nota1} moedas de um real")

else : 
    print("Valor inválido, por favor, escolha um valor entre R$ 10 e R$ 600.")
