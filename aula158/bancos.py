import contas
import pessoas


class Banco():
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas   !r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Richard', 17)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Marisa', 40)
    cp1 = contas.ContaPoupanca(112, 222, 0)
    c2.conta = cp1
    itau = Banco()
    itau.clientes.extend([c1, c2])
    itau.contas.extend([cc1, cp1])
    itau.agencias.extend([111, 112])

    if itau.autenticar(c1, cc1):
        cc1.depositar(1000)

    if itau.autenticar(c2, cp1):
        cc1.depositar(1000)
