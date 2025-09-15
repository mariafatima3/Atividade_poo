# 16) A livraria "Saber em Páginas" agora quer um sistema que não apenas catalogue os livros, mas que também controle o estoque da própria livraria. Tarefa:
# • Reutilize (ou recrie) a classe Livro do Tópico 2, com titulo e autor.
# • Crie uma classe Livraria com o atributo catalogo (um dicionário onde a chave é o título do livro e o valor é o objeto Livro).
# • Crie os métodos na Livraria: o adicionar_livro(livro): recebe um objeto Livro e o adiciona ao catalogo. o buscar_livro(titulo): 
# retorna o objeto Livro correspondente ao título buscado.

class Livro:
    def __init__(self, titulo, autor):
     self.titulo = titulo
     self.autor = autor
    
    def __repr__(self):
       return f"Livro(titulo='{self.titulo}', autor='{self.autor}')"

       
class Livraria:
    def __init__(self):
       self.catalogo = {}
    

    def adicionar_livro(self, livro):
        self.catalogo[livro.titulo] = livro


    def buscar_livro(self, titulo):
       return self.catalogo.get(titulo, None)
    

livro = Livro( "O Pequeno Príncipe","Antoine de Saint-Exupéry")

    
livraria = Livraria()
livraria.adicionar_livro(livro)

resultado = livraria.buscar_livro("O Pequeno Príncipe")
print(resultado)

