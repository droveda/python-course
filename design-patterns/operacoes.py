from abc import ABCMeta, abstractmethod


class Expressao(metaclass=ABCMeta):

    @abstractmethod
    def avalia(self):
        pass


class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita


class Soma(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita


class Numero(Expressao):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


if __name__ == '__main__':
    from impressao import Impressao

    impressao = Impressao()

    exp_esquerda = Soma(Numero(10), Numero(20))
    exp_direita = Subtracao(Numero(5), Numero(2))

    exp = Soma(exp_esquerda, exp_direita)
    exp.aceita(impressao)
    result = exp.avalia()
    print('')
    print(result)
