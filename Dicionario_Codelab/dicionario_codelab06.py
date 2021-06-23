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
            cadastro['mediaPortugues'] = int(input('Digite sua média em Português: '))
            if cadastro['mediaPortugues'] >= 7 :
                cadastro['situacaoPortugues'] = 'Aprovado!'
            elif 6.9 >= cadastro['mediaPortugues'] >= 7 : 
                cadastro['mediaPortugues'] = 'Recuperação!'
            else : 
                cadastro['situacaoPortugues'] = 'Reprovado!'


        if m == 1 :
            cadastro['mediaMatematica'] = int(input('Digite sua média em Matemática: '))
            if cadastro['mediaMatematica'] >= 7 :
                cadastro['situacaoMatematica'] = 'Aprovado!'
            elif 6.9 >= cadastro['mediaMatematica'] >= 7 : 
                cadastro['mediaMatematica'] = 'Recuperação!'
            else : 
                cadastro['situacaoMatematica'] = 'Reprovado!'

        if m == 2 :
            cadastro['mediaHistoria'] = int(input('Digite sua média em História: '))
            if cadastro['mediaHistoria'] >= 7 :
                cadastro['situacaoHistoria'] = 'Aprovado!'
            elif 6.9 >= cadastro['mediaHistoria'] >= 7 : 
                cadastro['mediaHistoria'] = 'Recuperação!'
            else : 
                cadastro['situacaoHistoria'] = 'Reprovado!'

        if m == 3 :
            cadastro['mediaGeografia'] = int(input('Digite sua média em Geografia: '))
            if cadastro['mediaGeografia'] >= 7 :
                cadastro['situacaoGeografia'] = 'Aprovado!'
            elif 6.9 >= cadastro['mediaGeografia'] >= 7 : 
                cadastro['mediaGeografia'] = 'Recuperação!'
            else : 
                cadastro['situacaoPortugues'] = 'Reprovado!'

        if m == 4 :
            cadastro['mediaCiencias'] = int(input('Digite sua média em Ciências: '))
            if cadastro['mediaCiencias'] >= 7 :
                cadastro['situacaoCiencias'] = 'Aprovado!'
            elif 6.9 >= cadastro['mediaCiencias'] >= 7 : 
                cadastro['mediaCiencias'] = 'Recuperação!'
            else : 
                cadastro['situacaoCiencias'] = 'Reprovado!'


boletim = pd.DataFrame(cadastro)
print(boletim)

