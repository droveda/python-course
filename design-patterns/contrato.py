from datetime import date


class Contrato:
    def __init__(self, cliente, data, tipo=None):
        self.__data = data
        self.__cliente = cliente
        if tipo is None:
            self.__tipo = 'NOVO'
        else:
            self.__tipo = tipo

    @property
    def data(self):
        return self.__data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    def avanca(self):
        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO':
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self):
        return Estado(Contrato(self.__cliente, self.__data, self.__tipo))


class Estado:
    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato


class Historico:
    def __init__(self):
        self.__estados_salvos = []

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)


if __name__ == '__main__':
    historico = Historico()

    c = Contrato('Jose', date.today())
    historico.adiciona_estado(c.salva_estado())
    c.avanca()

    historico.adiciona_estado(c.salva_estado())

    c.avanca()

    historico.adiciona_estado(c.salva_estado())

    c.avanca()

    historico.adiciona_estado(c.salva_estado())

    estado1 = historico.obtem_estado(1)

    print(estado1.contrato.tipo)
