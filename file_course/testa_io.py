if __name__ == '__main__':
    file = open('dados/contatos.csv', mode='r')
    print(type(file.buffer))

    conteudo = file.buffer.read()

    # texto_em_bytes = b'Esse e um texto em bytes'
    texto_em_bytes = bytes('Esse é um texto em bytes', 'utf8')
    print(texto_em_bytes)
    print(type(texto_em_bytes))

    file.close()

    file2 = open('dados/contatos-escrita.csv', mode='a+')
    print(type(file2.buffer))
    contato = bytes('15,Verônica,veronica@gmail.com\n', 'utf8')
    file2.buffer.write(contato)

    file2.close()
