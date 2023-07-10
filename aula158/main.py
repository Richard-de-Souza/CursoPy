import bancos
import pessoas
import contas


c1 = pessoas.Cliente('Richard', 17)
cc1 = contas.ContaCorrente(111, 222, 0, 0)
c1.conta = cc1
c2 = pessoas.Cliente('Marisa', 40)
cp1 = contas.ContaPoupanca(112, 222, 0)
c2.conta = cp1
itau = bancos.Banco()
itau.clientes.extend([c1, c2])
itau.contas.extend([cc1, cp1])
itau.agencias.extend([111, 112])
if itau.autenticar(c1, cc1):
    cc1.depositar(1000)
if itau.autenticar(c2, cp1):
    cc1.depositar(1000)
