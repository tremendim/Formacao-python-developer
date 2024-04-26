class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzinar(self):
        print('Plim, Plim...')
    def parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')
    def correr(self):
        print('Vruuummmmm...')
    
    def __str__(self):
        return f'Bicicleta:{self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}'
    
    

b1 = Bicicleta('Vermelha','caloi',2022,600)

b1.buzinar()
b1.correr()
b1.parar()

b2 = Bicicleta('Verde','monark',2000,189)