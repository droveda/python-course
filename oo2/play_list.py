from abc import ABC # abstract base classes
from collections.abc import MutableSequence
from numbers import Complex

class PlayList(MutableSequence):
    pass


class Numero(Complex):
    pass

if __name__ == '__main__':
    filmes = PlayList()