class Livro:

    livros = []

    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._atributo = True

        Livro.livros.append(self)
    
    def mostrar_livros():
        for livro in Livro.livros:
            print(f'{livro._titulo} | {livro._autor} | {livro._ano_publicacao}')


livro = Livro('Miranha', 'Tobias', '2022')
livro = Livro('Cavalo', 'Ui', '1980')
Livro.mostrar_livros()