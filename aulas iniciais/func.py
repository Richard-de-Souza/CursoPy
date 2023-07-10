import json


def print_iter(iterator):
    print(*list(iterator), sep='')
    print()
# ajuda a printar uma lista


def factorial(n):
    if n <= 1:
        return
    return n * factorial(n - 1)
# fatora um número


def adicionar(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
# adiciona itens auma lista


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa a listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()
# um listador melhor


def salvar(tarefas, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2,
                          ensure_ascii=False)
    return dados
# salvando dados em json (necessario o import do json)


def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho)
    return dados
# lê o arquivo json criado anteriormente
