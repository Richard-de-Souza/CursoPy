def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero*multiplicador
    return multiplicar
dupli = criar_multiplicador(2)
tripli = criar_multiplicador(3)
quadpli = criar_multiplicador(4)
#recebe o mulriplicador

print(dupli(2))
print(tripli(2))
print(quadpli(2))
#recebe o numero