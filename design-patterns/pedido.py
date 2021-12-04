from abc import ABCMeta, abstractmethod
from datetime import date


class Pedido:

    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao


class Comando(metaclass=ABCMeta):

    @abstractmethod
    def executa(self):
        pass


class ConcluiPedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        print('concluindo pedido')
        self.__pedido.finaliza()


class PagaPedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        print('pagando pedido')
        self.__pedido.paga()


class FilaDeTrabalho:

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


if __name__ == '__main__':
    pedido1 = Pedido('Fulano', 200)
    pedido2 = Pedido('Beltrano', 400)

    fila = FilaDeTrabalho()
    fila.adiciona(ConcluiPedido(pedido1))
    fila.adiciona(PagaPedido(pedido1))
    fila.adiciona(PagaPedido(pedido2))

    fila.processa()
