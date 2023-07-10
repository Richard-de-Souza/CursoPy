from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == 'main':
    p1 = Pessoa('Richard', 17)

# dataclass = classes de preguiçosos, muito mais facil
# (já vem com setter, getter)
# coisa nova do python
