
import time as tm
import random as rd

class Objetos: 
    def __init__(self) -> None:
        pass
        

    def lancadorMoedas() :
        print('Lançando a moeda....')
        tm.sleep(2)
        moeda = rd.randrange(1, 2)
        if moeda == 1 :
            print('Cara')
        else : 
            print('Coroa')

    def lancadorDados() :
        print('lancando o dado....')
        tm.sleep(2)
        print(rd.randint(1, 6))
        
Objetos.lancadorMoedas()
Objetos.lancadorDados()
