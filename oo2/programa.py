from abc import ABCMeta, abstractmethod


class Programa(metaclass=ABCMeta):

    @abstractmethod
    def __str__(self):
        pass


class MeuPrograma(Programa):
    def __str__(self):
        return 'Hello!!!'


if __name__ == '__main__':
    p = MeuPrograma()
    print(p)
