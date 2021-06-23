cadastro = dict()
cadastro['nome'] = input('Digite seu nome: ')
cadastro['anoNascimento'] = int(input('Digite seu ano de nascimento: '))
cadastro['idade'] = 2021 - cadastro['anoNascimento']
cadastro['carteiraTrabalho'] = int(input('Digite sua carteira de Trabalho (digite 0 caso não possua) '))

if cadastro['carteiraTrabalho'] != 0 :
    cadastro['anoContratacao'] = int(input('Digite o ano de contratação: '))
    cadastro['salario'] = float(input('Digite seu salario: '))
    cadastro['anosAposentarei'] = (cadastro['anoContratacao'] - 2021) + 35
if cadastro['carteiraTrabalho'] == 0 :
    cadastro['anosAposentarei'] = 35 
print(cadastro)
