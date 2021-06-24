# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(anoNascimento) :
    idade = 2021 - anoNascimento
    if 18 <= idade < 70:
        return 'Pessoa com o voto OBRIGATORIO'
    elif 18 > idade >= 16 or idade >= 70:
        return ' Pessoa tem o voto OPCIONAL'
    else : 
        return 'Pessoa com o voto NEGADO'
print(voto(2000))