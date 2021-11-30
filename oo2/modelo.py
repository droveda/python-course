class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    def __str__(self):
        return f'Nome {self.nome} - Ano: {self.ano} - Likes: {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Duracao: {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome {self.nome} - Ano: {self.ano} - Likes: {self.likes} - Temporadas: {self.temporadas}'


class PlayList:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


if __name__ == '__main__':
    vingadores = Filme('Vingadores guerra infinita', 2018, 160)
    vingadores.dar_like()
    vingadores.dar_like()
    print(vingadores.nome)
    print(vingadores.likes)

    atlanta = Serie('Atlanta', 2018, 2)
    print(f'Nome {atlanta.nome} - Ano: {atlanta.ano}')

    todo_mundo_em_panico = Filme('Todo mundo em panico', 2002, 60)

    demolidor = Serie('Demolidor', 2015, 3)

    filmes_e_series = [vingadores, atlanta, todo_mundo_em_panico, demolidor]

    playlist_fim_de_semana = PlayList('fim de semana', filmes_e_series)

    print('\n')
    print(len(playlist_fim_de_semana))
    for f in playlist_fim_de_semana:
        print(f)
