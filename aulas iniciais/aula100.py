import pprint
import copy

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# copy, sorted, produtos.sort
# Exercícios
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
    {**produtos, 'preco': round(produtos['preco'] * 1.10, 2)}
    for produtos in produtos
]
p(novos_produtos)
print('\n')
print(40*'-')
print('\n')

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse = True
)
p(produtos_ordenados_por_nome)
print('\n')
print(40*'-')
print('\n')
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)
p(produtos_ordenados_por_preco)
print('\n')
print(40*'-')
print('\n')
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)