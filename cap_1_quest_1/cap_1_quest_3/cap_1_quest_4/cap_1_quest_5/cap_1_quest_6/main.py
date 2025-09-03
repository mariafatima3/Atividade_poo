# 6) A livraria "Saber em Páginas" precisa de um sistema para catalogar seus livros. Por enquanto, eles só precisam armazenar as informações básicas de cada um.
# Tarefa: Crie uma classe chamada Livro. Ao ser instanciada, ela deve receber titulo, autor e ano_publicacao como argumentos e armazená-los como atributos.

class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
     self.titulo = titulo
     self.autor = autor
     self.ano_publicacao = ano_publicacao

livraria = Livro( "O Pequeno Príncipe","Antoine de Saint-Exupéry", 1943)
livraria.titulo = " O Pequeno Príncipe "

livraria.autor = " Antoine de Saint-Exupéry "

livraria.ano_publicacao = 1943

print(livraria.titulo)
print(livraria.autor)
print(livraria.ano_publicacao)