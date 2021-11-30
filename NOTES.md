# Python

## Collections em python

* lista
    * days = ['S', 'T', 'Q']

* tupla (estrutura de dados imutavel)
    * dias = ('S', 'T', 'Q', 'Q', 'S', 'S', 'D')
    * type(dias)
    * ponto1 = (3, 5)
    * ponto2 = (4, 6)
    * line = [ponto1, ponto2]

* set em python (nao permite duplicados)
    * Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos
      duplicados dentro do set.
    * cpfs = {11122233344, 22233344455, 33344455566}
    * colecao.add(44455566677) -> adiciona elemento
    * set não possui um índice

* Dictionary
    * instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
    * instrutores['Flavio'] -> imprime 37

## Trabalhando com arquivos em python

* arquivo = open("palavras.txt", "w")
* arquivo.write('banana')
* arquivo.write('melancia')
* arquivo.close()
* arquivo = open("palavras.txt", "a")
* arquivo.write('morango\n')
* arquivo.write('maça\n')
* arquivo.close()
* arquivo.read()
* for linha in arquivo:
* linha = arquivo.readline()

## OO

* atrubutos comecando com '__' sao privados
* metodos comecando com '__' sao privados
* @property
* @limite.setter
* metodos estáticos
    * @staticmethod
* atributos estáticos
    * apenas definir uma variavel na classes fora do __init__
    * __class__.tamanho_cpf (exemplo de como acessar atributo estatico dentro da classe)
* Herança em python eh feita assim:
    * class Filme(Programa):
        * classe Filme extends Programa
    * exemplo chamada ao super: super().__init__(nome, ano)
* toString() -> def __str__(self):
* Exemplo de classe abstrata e metodo abstrato
    * programa.py
* Exemplo Herança Múltipla
    * sistema.py