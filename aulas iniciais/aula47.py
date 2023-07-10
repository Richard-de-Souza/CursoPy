import os

palavra_secreta = 'gatúca'
letras_acertadas = ''
tentativas = 0

while True:

    letra_digitada = input('Digite uma letra\nou (Sair!) para desistir: ')
    tentativas += 1

    if letra_digitada == 'Sair!':
        os.system('cls')
        print('Você desistiu...')
        break

    if len(letra_digitada) > 1:
        print('é pra digitar só uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('-'*48)
        print('|               VOCÊ GANHOU!!!                 |')
        print('|           A palavra era gatúca               |')
        print('|         O numero de tentativas foi:', tentativas, '       |')
        print('-'*48)
        break
