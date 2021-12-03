from impostos import ICMS, ISS, XYZ
from orcamento import Orcamento


class CalculadorDeImpostos:

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    orcamento = Orcamento(1500)
    calc = CalculadorDeImpostos()
    calc.realiza_calculo(orcamento, ISS())
    calc.realiza_calculo(orcamento, ICMS())
    calc.realiza_calculo(orcamento, XYZ())
