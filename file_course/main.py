from converter_util import ConverterUtil


class Main:
    def __init__(self):
        pass

    def initializer(self):
        converter = ConverterUtil()
        contatos = converter.csv_para_contatos('dados/contatos.csv')
        converter.contatos_para_pickle(contatos, 'dados/contatos.pickle')
        print(contatos)

        contatos2 = converter.pickle_para_contatos('dados/contatos.pickle')
        print(contatos2)

        for contato in contatos2:
            print(f'{contato.id} - {contato.nome} - {contato.email}')

        # converter.contatos_para_json(contatos, 'dados/contatos.json')

        contatos3 = converter.json_para_contatos('dados/contatos.json')

        for contato in contatos3:
            print(f'{contato.id} - {contato.nome} - {contato.email}')


if __name__ == '__main__':
    main = Main()
    main.initializer()
