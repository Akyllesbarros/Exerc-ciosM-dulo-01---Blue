# 6. Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa devereceber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só.




cadastro = dict()
mediaPortugues = mediaMatematica = mediaHistoria = mediaGeografia = mediaCiencias = 0
situacaoPortugues = situacaoMatematica = situacaoHistoria = situacaoGeografia = situacaoCiencias = 0

for c in range(15) :
    cadastro['nome'] = input('Digite seu nome: ')
    for m in range(5) :
        if m == 0 :
            cadastro['mediaPortugues'] = float(input('Digite sua média em Português: '))
            if cadastro['mediaPortugues'] >= 7 :
                cadastro['situacaoPortugues'] = 'Aprovado!'
            if 6.9 >= cadastro['mediaPortugues'] >= 5 : 
                cadastro['situacaoPortugues'] = 'Recuperação!'
            if cadastro['mediaPortugues'] < 5 : 
                cadastro['situacaoPortugues'] = 'Reprovado!'


        if m == 1 :
            cadastro['mediaMatematica'] = float(input('Digite sua média em Matemática: '))
            if cadastro['mediaMatematica'] >= 7 :
                cadastro['situacaoMatematica'] = 'Aprovado!'
            if 6.9 >= cadastro['mediaMatematica'] >= 5 : 
                cadastro['situacaoMatematica'] = 'Recuperação!'
            if cadastro['mediaMatematica'] < 5: 
                cadastro['situacaoMatematica'] = 'Reprovado!'

        if m == 2 :
            cadastro['mediaHistoria'] = float(input('Digite sua média em História: '))
            if cadastro['mediaHistoria'] >= 7 :
                cadastro['situacaoHistoria'] = 'Aprovado!'
            if 6.9 >= cadastro['mediaHistoria'] >= 5 : 
                cadastro['situacaoHistoria'] = 'Recuperação!'
            if cadastro['mediaHistoria'] < 5: 
                cadastro['situacaoHistoria'] = 'Reprovado!'

        if m == 3 :
            cadastro['mediaGeografia'] = float(input('Digite sua média em Geografia: '))
            if cadastro['mediaGeografia'] >= 7 :
                cadastro['situacaoGeografia'] = 'Aprovado!'
            if 6.9 >= cadastro['mediaGeografia'] >= 5 : 
                cadastro['situacaoGeografia'] = 'Recuperação!'
            if cadastro['mediaGeografia'] < 5: 
                cadastro['situacaoGeografia'] = 'Reprovado!'

        if m == 4 :
            cadastro['mediaCiencias'] = float(input('Digite sua média em Ciências: '))
            if cadastro['mediaCiencias'] >= 7 :
                cadastro['situacaoCiencias'] = 'Aprovado!'
            if 6.9 >= cadastro['mediaCiencias'] >= 5 : 
                cadastro['situacaoCiencias'] = 'Recuperação!'
            if cadastro['mediaCiencias'] < 5: 
                cadastro['situacaoCiencias'] = 'Reprovado!'


print(cadastro)
