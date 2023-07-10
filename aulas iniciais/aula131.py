# codigo que usa outro codigo == codigo cliente
# atributos que começam com underline não devem ser usados
# fora da classe
class Caneta:
    def __init__(self, cor):
        #       self.cor_tinta = cor
        # private/protected não utilizar
        self._cor = cor

    @property
    # metodo que se comporta como atributo da classe
    def cor(self):
        return self._cor
    # serve para obter o valor

    @cor.setter
    def cor(self, valor):
        self._cor = valor
    # esse setta o valor do 'atributo'

#    @property
#    def cor_tampa(self):
#        return

    # um protetor de codigo (um getter)
#    def get_cor(self):
#        print('GET COR')
#        return self.cor

##############################################


caneta = Caneta('Azul')
caneta.cor = 'Rosa'

print(caneta.cor)

# print(caneta.cor_tampa)
