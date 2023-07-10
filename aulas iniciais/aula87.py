lista = [
    'a', 1, 1.1, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'}
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))
    elif isinstance(item, str):
        print(item.upper(), isinstance(item, str))
    elif isinstance(item, (int, float)):
        print(item, item * 2)
    else:
        print('outro')
        print(item)
# isinstance é um verificador de tipo de dados
