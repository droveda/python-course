import random


def jogar():
    mensagem_jogo()
    palavra_secreta = cria_palavra_secreta()
    letras_acertadas = inicializa_letas_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = pede_chute(letras_acertadas)

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print('Voce errou, voce possui mais {} tentativas'.format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print('Voce ganhou!')
    else:
        print('Voce perdeu!')


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            # print('Encontrei a letra \'{}\' na posicao {}'.format(letra, index))
            letras_acertadas[index] = letra
        index += 1


def pede_chute(letras_acertadas):
    chute = input('Qual letra? {} '.format(letras_acertadas))
    chute = chute.strip().upper()
    return chute


def inicializa_letas_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def mensagem_jogo():
    print('####################################')
    print('Bem vindo ao jogo da Forca!')
    print('####################################')


def cria_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()
    index = random.randrange(0, len(palavras))
    return palavras[index].upper()


if __name__ == '__main__':
    jogar()
