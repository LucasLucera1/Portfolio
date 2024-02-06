

from .avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, _nome, categoria):
        self.nome = _nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.media_avaliacoes} | {restaurante.ativo.ljust(25)}')


    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)


    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "Sem Avaliações"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)

        media = round(soma_das_notas/quantidade_de_notas,1)
        return media
