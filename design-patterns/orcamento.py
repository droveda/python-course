from abc import ABCMeta, abstractmethod


class EstadoOrcamento(metaclass=ABCMeta):

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoOrcamento):
    def aprova(self, orcamento):
        orcamento._estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento._estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('orcamento em aprovacao nao podem ir para finalizado')

    def aplica_desconto_extra(self, orcamento):
        if not orcamento.desconto_ja_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            orcamento.desconto_ja_aplicado = True
        else:
            raise Exception('desconto ja aplicado')


class Aprovado(EstadoOrcamento):
    def aprova(self, orcamento):
        raise Exception('orcamento ja esta aprovado')

    def reprova(self, orcamento):
        raise Exception('orcamento aprovados nao podem ser reprovados')

    def finaliza(self, orcamento):
        orcamento._estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        if not orcamento.desconto_ja_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            orcamento.desconto_ja_aplicado = True
        else:
            raise Exception('desconto ja aplicado')


class Reprovado(EstadoOrcamento):
    def aprova(self, orcamento):
        raise Exception('orcamento reprovado nao pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('orcamento ja reprovado')

    def finaliza(self, orcamento):
        orcamento._estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos reprovados nao recebem desconto extra')


class Finalizado(EstadoOrcamento):
    def aprova(self, orcamento):
        raise Exception('orcamento ja finalizado nao pode ser aprovado')

    def reprova(self, orcamento):
        raise Exception('orcamento ja finalizado nao pode ser reprovado')

    def finaliza(self, orcamento):
        raise Exception('orcamento ja finalizado')

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados nao recebem desconto extra')


class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self._estado_atual = EmAprovacao()
        self.__desconto_extra = 0
        self.desconto_ja_aplicado = False

    def aplica_desconto_extra(self):
        self._estado_atual.aplica_desconto_extra(self)

    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto

    @property
    def estado_atual(self):
        return self._estado_atual

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    def obter_item(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def aprova(self):
        self._estado_atual.aprova(self)

    def reprova(self):
        self._estado_atual.reprova(self)

    def finaliza(self):
        self._estado_atual.finaliza(self)


class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    o = Orcamento()
    o.adiciona_item(Item('Item1', 100))
    o.adiciona_item(Item('Item2', 50))
    o.adiciona_item(Item('Item3', 400))

    print(f'{o.valor} - {o.estado_atual}')
    o.aplica_desconto_extra()
    print(o.valor)

    o.aprova()
    print(f'{o.valor} - {o.estado_atual}')
    o.finaliza()

    print(f'{o.valor} - {o.estado_atual}')
