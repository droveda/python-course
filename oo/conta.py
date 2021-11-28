class Conta:
    ip = '127.0.0.1'

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto... {} '.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo, self.__titular))

    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor {} passou o limite'.format(valor))

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor: float, destino: "Conta"):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return '001'
