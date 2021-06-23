import os

lista = list()
cadastro = dict()
listaMulheres = list()
listaAcimaMedia = list()
contadorPessoas = 0
somaIdade = 0
mediaIdade = 0
continua = " "
while True : 
    os.system('cls')
    cadastro = {
        'nome' : input('Digite seu nome: '),
        'sexo' : input('Digite seu sexo [ M/F ]: ').upper().strip()[0],
        'idade' : int(input('Digite sua idade: '))
    }

    lista.append(cadastro)
    contadorPessoas += 1
    somaIdade += cadastro['idade']
    mediaIdade = somaIdade / contadorPessoas

    if cadastro['sexo'] == 'F' :
        listaMulheres.append(cadastro)

    if cadastro['idade'] >= mediaIdade :
        listaAcimaMedia.append(cadastro)
    os.system('cls')

    continua = input('Deseja continuar [ Sim / Não ] ? ').upper().strip()[0]
    if continua == 'S' :
        continue
    elif continua == 'N' :
        print(f'''São {contadorPessoas} pessoas cadastradas.\n
    A média de idade entre elas é de {mediaIdade:.1f}\n
    Essa é a lista com as mulheres {listaMulheres}\n
    Essa é a lista com as idades acima da média: {listaAcimaMedia}. ''')
        break
