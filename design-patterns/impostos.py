from abc import ABCMeta, abstractmethod


class Imposto(metaclass=ABCMeta):
    def __init__(self, outro_imposto=None):
        self.__outro_imposto = outro_imposto

    def calcula_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass


class TemplateDeImpostoCondicional(Imposto, metaclass=ABCMeta):

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calcula_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calcula_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento):
        pass


class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calcula_outro_imposto(orcamento)


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calcula_outro_imposto(orcamento)


class XYZ(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.01 + self.calcula_outro_imposto(orcamento)


class ICPP(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateDeImpostoCondicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reqis(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reqis(self, orcamento):
        for item in orcamento.obter_item():
            if item.valor > 100:
                return True

        return False
