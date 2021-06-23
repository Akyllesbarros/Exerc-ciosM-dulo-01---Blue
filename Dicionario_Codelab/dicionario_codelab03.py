from typing import Any


cadastro = dict()

cadastro['nome'] = input('Digite seu nome: ')
cadastro['media'] = int(input('Digite sua média: '))
if cadastro['media'] >= 7 :
    cadastro['situacao'] = 'Aprovado!'
elif 6.9 >= cadastro['media'] >= 7 : 
    cadastro['media'] = 'Recuperação!'
else : 
    cadastro['situacao'] = 'Reprovado!'

print(f'nome: {cadastro["nome"]}\nmédia: {cadastro["media"]}\nsituação: {cadastro["situacao"]}')

