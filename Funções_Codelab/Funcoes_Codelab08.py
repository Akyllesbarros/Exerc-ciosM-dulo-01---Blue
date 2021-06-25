# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro
# terá 29 dias.
from datetime import datetime






# Validação do ano 

def data_valida(data):
 
    # mes ou ano inválido, retorna NULL
    if mes < 1 or mes > 12 or ano <= 0:
        return print('NULL')

    # verifica qual o último dia do mês
    if mes in (1, 3, 5, 7, 8, 10, 12):
        ultimo_dia = 31
    elif mes == 2:
        if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
            ultimo_dia = 29
        else:
            ultimo_dia = 28
    else:
        ultimo_dia = 30

    # verifica se o dia é válido
    if dia < 1 or dia > ultimo_dia:
        print('NULL')

    

# Função para transformar mês int, em String/ Extenso

def extenso_mes(mes):
	lista_de_mes = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]
	mes_ex = lista_de_mes[mes-1]
	return mes_ex

# Função para transformar Dia int, em String/ Extenso

def extenso_dia(dia):

	lista_de_dia = [
        "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze", "Treze", "Catorzer", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte", "Vinte e Um", "Vinte e Dois", "Vinte e Três", "Vinte e Quatro", "Vinte e Cinco", "Vinte e Seis", "Vinte e Sete", "Vinte e Oito", "Vinte e Nove", "Trinta", "Trinta e Um"
        ]
	dia_ex = lista_de_dia[dia-1]
	return dia_ex


# Entrada da data 

data = input('Digite a data no formato DD / MM / AAAA:\n') 
data = datetime.strptime(data, '%d/%m/%Y')  # transforma data string em formato DATA. 

#Pega a data e parte ela em MES, DIA e ANO (e transforma em INTEIRO)

mes = int('{}'.format(data.month))      
dia = int('{}'.format(data.day))
ano = int('{}'.format(data.year))

# Chamando as funções 
data_valida(data)
extenso_dia(dia)
extenso_mes(mes)
#print
print(f"O valor por extenso é {extenso_dia(dia)} de {extenso_mes(mes)} de {ano}")