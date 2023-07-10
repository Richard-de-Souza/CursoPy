import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

#lista = [
#    numero * 2
#    for numero in range(10)
#]
#print(lista)
#print(novos_produtos)
#print(*novos_produtos, sep='\n')
#lista = [n for n in range(10) if n < 5]
#print(lista)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p1', 'preco': 10,},
    {'nome': 'p1', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto ['preco' ] > 20 and produto['preco'] * 1.05 > 10
]
p(novos_produtos)