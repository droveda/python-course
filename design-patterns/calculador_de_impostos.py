from impostos import ICMS, ISS, XYZ, IKCV, ICPP
from orcamento import Orcamento, Item


class CalculadorDeImpostos:

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    pc = Item('PC', 1000)
    teclado = Item('Teclado', 500)

    orcamento = Orcamento()
    orcamento.adiciona_item(pc)
    orcamento.adiciona_item(teclado)

    calc = CalculadorDeImpostos()
    calc.realiza_calculo(orcamento, ISS())
    calc.realiza_calculo(orcamento, ICMS())
    calc.realiza_calculo(orcamento, ISS(ICMS()))
    calc.realiza_calculo(orcamento, XYZ())

    print('ICPP, IKCV')
    calc.realiza_calculo(orcamento, ICPP())
    calc.realiza_calculo(orcamento, IKCV())
    calc.realiza_calculo(orcamento, ICPP(IKCV()))
