class Main:

    def __init__(self):
        pass

    def read_file(self):
        try:
            with open('dados/contatos.csv', 'r') as my_file:
                for line in my_file:
                    print(line, end='')
        except FileNotFoundError:
            print('Arquivo nao encontrado')

    def write_file(self):
        print('')
        file = open('dados/contatos-escrita.csv', 'a+')
        contatos = ['11,teste,teste@gmail.com\n', '12,test2,teste2@gmail.com\n', '13,teste3,teste3@gmail.com\n']

        for contato in contatos:
            file.write(contato)

        file.flush()

        file.seek(0)  # volta para o inicio do arquivo
        for linha in file:
            print(linha, end='')

        file.close()


if __name__ == '__main__':
    main = Main()
    main.read_file()
    # main.write_file()
