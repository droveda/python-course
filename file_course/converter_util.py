import csv
import json
import pickle

from contato import Contato


class ConverterUtil:
    def __init__(self):
        pass

    def csv_para_contatos(self, caminho: str, encoding='utf-8'):
        contatos = []

        with open(caminho, encoding=encoding) as file:
            leitor = csv.reader(file)

            for linha in leitor:
                id, nome, email = linha

                contato = Contato(id, nome, email)
                contatos.append(contato)

        return contatos

    def contatos_para_pickle(self, contatos, caminho):
        with open(caminho, mode='wb') as file:
            pickle.dump(contatos, file)

    def pickle_para_contatos(self, caminho):
        with open(caminho, mode='rb') as file:
            contatos = pickle.load(file)

        return contatos

    def contatos_para_json(self, contatos, caminho):
        with open(caminho, mode='w') as file:
            json.dump(contatos, file, default=self._contato_para_json)

    def _contato_para_json(self, contato):
        return contato.__dict__

    def json_para_contatos(self, caminho):
        contatos = []

        with open(caminho) as file:
            contatos_json = json.load(file)

            for contato in contatos_json:
                # c = Contato(id=contato['id'], nome=contato['nome'], email=contato['email'])
                c = Contato(**contato) # python consegue desempacotar
                contatos.append(c)

        return contatos
