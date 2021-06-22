# 1.    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.

cadastro = dict()
cadastro['nome'] = input(' Digite o nome:')
cadastro['idade'] = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = 2021 - cadastro['idade']
cadastro['carteiraTrabalho'] = int(input('Digite sua carteira de trabalho (digite 0 se nunca tiver assinado): '))

if cadastro['carteiraTrabalho'] == 0 : 
    cadastro["aposentarei"] = 35

elif cadastro['carteiraTrabalho'] != 0 :
    cadastro['anoContratacao'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite o salario: '))
    cadastro["aposentarei"] = ( 2021 -  cadastro['anoContratacao'] - 35 ) * -1 

print(f'Aposentarei daqui a {cadastro["aposentarei"]} anos com {cadastro["idade"] + cadastro["aposentarei"]}')
