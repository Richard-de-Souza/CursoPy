#    .replace('.','')\
#    .replace(' ','')\
#    .replace('-','')
import re
import sys
entrada = input('CPF [746.824.890-70]: ')
cpf_informado = re.sub(
    r'[^0-9]',
    '',
    entrada
)
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você está de palhaçada')
    sys.exit()
nove_digitos = cpf_informado[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito = ((resultado_digito_1*10) % 11)
digito = digito if digito <= 9 else 0

dez_digitos = cpf_informado[:10]
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito2 in dez_digitos:
    resultado_digito_2 += int(digito2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito2 = ((resultado_digito_2*10) % 11)
digito2 = digito2 if digito2 <= 9 else 0
cpf_gerado = f'{nove_digitos}{digito}{digito2}'
if cpf_gerado == cpf_informado:
    print(f'{cpf_informado} é válido')
else:
    print('CPF inválido')
