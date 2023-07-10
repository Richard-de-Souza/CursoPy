from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa('Richard', 17, 'Souza')
    p1.nome_completo = 'Richard de Souza'
    print(p1)
    print(p1.nome_completo)
