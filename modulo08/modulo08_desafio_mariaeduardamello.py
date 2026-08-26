class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def __str__(self):
        status = "Emprestado" if self.emprestado else "Disponível"
        return f"'{self.titulo}' por {self.autor} [{status}]"


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado à biblioteca.")

    def listar_livros(self):
        print("\n--- Acervo da Biblioteca ---")
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if not livro.emprestado:
                    livro.emprestado = True
                    print(f"Sucesso: O livro '{livro.titulo}' foi emprestado.")
                    return
                else:
                    print(f"Aviso: O livro '{livro.titulo}' já está emprestado.")
                    return
        print(f"Erro: Livro '{titulo}' não encontrado na biblioteca.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.emprestado:
                    livro.emprestado = False
                    print(f"Sucesso: O livro '{livro.titulo}' foi devolvido.")
                    return
                else:
                    print(f"Aviso: O livro '{livro.titulo}' já consta como disponível.")
                    return
        print(f"Erro: Livro '{titulo}' não encontrado na biblioteca.")



minha_biblioteca = Biblioteca()

# Adicionando livros
l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
l3 = Livro("Diario de Anne Frank", "Anne Frank")

minha_biblioteca.adicionar_livro(l1)
minha_biblioteca.adicionar_livro(l2)
minha_biblioteca.adicionar_livro(l3)


minha_biblioteca.listar_livros()

minha_biblioteca.emprestar_livro("Dom Casmurro")

minha_biblioteca.emprestar_livro("Dom Casmurro")

minha_biblioteca.listar_livros()

minha_biblioteca.devolver_livro("Dom Casmurro")