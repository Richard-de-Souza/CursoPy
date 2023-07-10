import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar [s]air: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Digite o item: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Diga um indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um número inteiro por favor.')
        except IndexError:
            print('Não existe este indice')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
        for i, valor in enumerate(lista):
            indice = len(lista)
            print(i, valor)
    elif opcao == 's':
        print('Você saiu do sitema.')
        break
    else:
        print('Esta opção não existe')
