def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)


def par_impar(numero):
    multiplo_2 = numero % 2 == 0

    if multiplo_2:
        return f'{numero} é par'
    return f'{numero} é impar'


print(par_impar(2))
print(par_impar(39))
print(par_impar(23))
print(par_impar(4))
print(par_impar(8))
print(par_impar(12))
