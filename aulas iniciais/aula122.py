class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')
# classes são moldes por isso não a chamamos


fusca = Carro('fusca')
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro('celta')
celta.acelerar()
Carro.acelerar(celta)
