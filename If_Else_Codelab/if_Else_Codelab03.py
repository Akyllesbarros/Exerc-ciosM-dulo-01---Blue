# DESAFIO 03

import random
nome = input("Olá, para iniciar, digite seu nome: ")
numeroUsuario = int(input(f'''Olá {nome}, 
Você acha que é capaz de adivinhar o número que eu estou pensando? 
Digite abaixo sua primeira aposta de 0 a 10.\n\n'''))

sorte = random.randint(0, 10)
if numeroUsuario == sorte : 
    print("Você é demais em, acertou de primeira!! Parabéns!")
elif numeroUsuario != sorte : 
    print("Acho que está perto, mas não foi dessa vez!...")


