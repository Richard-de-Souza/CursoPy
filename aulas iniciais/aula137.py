class Motor:
    def __init__(self, nome_motor):
        self.nome_motor = nome_motor


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Carro:
    def __init__(self, nome_carro):
        self.nome = nome_carro
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


corsa = Carro('Corsa')
chevrolet = Fabricante('Chevrolet')
corsa.fabricante = chevrolet
motor_1_4 = Motor('Motor 1.4')
corsa.motor = motor_1_4
print(corsa.fabricante.nome, corsa.nome, corsa.motor.nome_motor)

uno = Carro('Uno')
fiat = Fabricante('Fiat')
uno.fabricante = fiat
motor_1_4 = Motor('Motor 1.4')
uno.motor = motor_1_4
print(uno.fabricante.nome, uno.nome, uno.motor.nome_motor)
