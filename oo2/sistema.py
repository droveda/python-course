class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa..., Caelum')

    def busca_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos deste mes')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('fez muita coisa..., Alura')

    def busca_perguntas_sem_resposta(self):
        print(f'Mostrando perguntas nao respondidas no forum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


if __name__ == '__main__':
    jose = Junior('jose')
    jose.busca_perguntas_sem_resposta()

    luan = Pleno('luan')
    luan.busca_perguntas_sem_resposta()
    luan.busca_curso_do_mes()

    print(jose)
    print(luan)
