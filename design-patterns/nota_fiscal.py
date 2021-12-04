from datetime import date

from observadores import imprime, salva_no_banco, envia_por_email


class NotaFiscalBuilder:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__itens = None
        self.__data_de_emissao = None
        self.__detalhes = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_data_de_emissao(self, data_de_emissao: date):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def build(self):

        if self.__razao_social is None:
            raise Exception('Razao social nao informada')
        if self.__cnpj is None:
            raise Exception('CNPJ nao informada')
        if self.__itens is None:
            raise Exception('Itens nao informada')
        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()

        return NotaFiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            data_de_emissao=self.__data_de_emissao,
            detalhes=self.__detalhes
        )


class Item:

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class NotaFiscal:
    def __init__(self, razao_social: str, cnpj: str, itens,
                 data_de_emissao: date = date.today(), detalhes: str = '',
                 observadores=[]):
        self.__observadores = observadores
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__itens = itens
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota nao pode ter mais que 20 caracteres')
        self.__detalhes = detalhes

        for observador in self.__observadores:
            observador(self)

    def addAcao(self, execucao):
        self.__observadores.append(execucao)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':
    itens = [
        Item('Item a', 100),
        Item('Item b', 200)
    ]

    nota_fiscal = NotaFiscal(
        razao_social='Empresa LTDS',
        cnpj='012345670001',
        itens=itens,
        observadores=[imprime, salva_no_banco, envia_por_email]
    )

    nf = NotaFiscalBuilder() \
        .com_cnpj('12345566555') \
        .com_itens(itens) \
        .com_detalhes('Some details') \
        .com_razao_social('LTDA 123') \
        .com_data_de_emissao(date.today()) \
        .build()

    print(nf)
    print(nf.razao_social)
