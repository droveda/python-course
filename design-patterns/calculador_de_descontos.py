from descontos import DescontoPorCincoItens, DescontoPorMaisDe500Reais, SemDesconto
from orcamento import Orcamento, Item


class CalculadorDeDescontos:

    def calcula(self, orcamento):
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDe500Reais(SemDesconto())
        ).calcula(orcamento)
        return desconto


if __name__ == '__main__':
    orcamento = Orcamento()

    orcamento.adiciona_item(Item('Item-1', 100))
    orcamento.adiciona_item(Item('Item-2', 500))

    calculador = CalculadorDeDescontos()

    desconto = calculador.calcula(orcamento)
    print(f'{desconto}')
