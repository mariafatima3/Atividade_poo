# 6) A livraria "Saber em Páginas" precisa de um sistema para catalogar seus livros. Por enquanto, eles só precisam armazenar as informações básicas de cada um.
# Tarefa: Crie uma classe chamada Livro. Ao ser instanciada, ela deve receber titulo, autor e ano_publicacao como argumentos e armazená-los como atributos.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
     self.titulo = titulo
     self.autor = autor
     self.ano_publicacao = ano_publicacao

livro = Livro( "O Pequeno Príncipe","Antoine de Saint-Exupéry", 1943)
livro.titulo = " O Pequeno Príncipe "

livro.autor = " Antoine de Saint-Exupéry "

livro.ano_publicacao = 1943

print(livro.titulo)
print(livro.autor)
print(livro.ano_publicacao)