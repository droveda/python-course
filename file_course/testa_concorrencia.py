if __name__ == '__main__':
    contato1 = '11,teste,teste@gmail.com\n'
    contato2 = '12,teste2,teste2@gmail.com\n'

    with open('dados/contatos-escrita.csv', mode='w') as file1:
        file1.write(contato1)
    with open('dados/contatos-escrita.csv', mode='a') as file2:
        file2.write(contato2)
