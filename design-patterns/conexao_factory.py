class ConexaoFactory:

    def cria_conexao(self):
        connection = "Aqui seria a chamada ao driver para gerar a conexao"

        return connection


if __name__ == '__main__':
    c = ConexaoFactory()
    print(c.cria_conexao())
