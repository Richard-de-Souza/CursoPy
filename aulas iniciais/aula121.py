import os
import json


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa a listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa a desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa a desfazer')
        return
    print()
    listar(tarefas)

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada a lista')
    tarefas.append(tarefa)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return
    print(f'{tarefa=} adicionada a lista')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def ler(tarefas, caminho):
    dados = []
    try:
        with open(caminho, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho)
    return dados


def salvar(tarefas, caminho):
    with open(caminho, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2,
                          ensure_ascii=False)
    return dados


def sair():
    return exit()


CAMINHO_ARQUIVO = 'aula121.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'clear': lambda: os.system('cls'),
        'sair': lambda: sair(),

    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else\
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)
