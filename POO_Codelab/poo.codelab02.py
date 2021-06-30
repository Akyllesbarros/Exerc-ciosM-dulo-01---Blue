# Vamos aprimorar o código: cadastro de jogador de futebol.py que foi
# desenvolvido no Code Lab da aula 14. Faça com que o seu código
# funcione para vários jogadores, incluindo um sistema de visualização de
# detalhes de aproveitamento de cada jogador.

# 01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

class Jogador : 
    def __init__(self, nome, gols, partidas) :
        self.nome = nome 
        self.gols = gols
        self.partidas = partidas
    
    def status(self):
        return f'nome : {self.nome}\ngols : {self.gols}\npartidas : {self.partidas}'

jogador1 = Jogador('akylles', 15, 20)
jogador2 = Jogador('Leticia', 20, 20)

print(jogador2.status())
