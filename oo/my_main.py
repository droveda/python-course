from conta import Conta
from minha_data import MinaData

if __name__ == '__main__':
    conta = Conta(numero=123, titular='Fulano', saldo=55.0, limite=1000.0)
    conta2 = Conta(numero=1234, titular='Beltrano', saldo=100.0, limite=1000.0)
    print(conta)

    conta.extrato()
    conta.deposita(100)
    conta.saca(50)
    conta.extrato()

    # conta2 = None

    data = MinaData(21, 11, 2021)
    data.formatada()

    conta.transfere(20, conta2)

    conta.extrato()
    conta2.extrato()
    conta.limite = 10000.0
    print(conta.limite)

    conta.saca(30000)

    print(Conta.codigo_banco())
    print(Conta.ip)
