# Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela
# menor que 21 anos, ela deve crescer 0,5 cm


class Pessoa : 
    global ano
    ano = 2021


    def __init__(self, nome, idade, peso, altura) :
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self) :
        self.idade += 1 
    
    def engordar(self) :
        self.peso += 1

    def emagrecer(self) :
        self.peso -= 1 

    def crescer(self) :
        if self.idade <= 21 :
            self.altura += 0.5

    def status(self) :
        print(f'O ano é {ano}\n\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}')

    def passarAno(self) :
        global ano
        ano += 1
        print('ano passou')
        self.crescer()
        self.envelhecer()
    

Pessoa1 = Pessoa('Akylles', 20, 66, 1.72)
Pessoa1.status()
Pessoa1.passarAno()
Pessoa1.status()
