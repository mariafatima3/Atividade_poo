# 9) Um sistema de e-commerce precisa de uma estrutura para manter os dados de cada produto em seu inventário, incluindo nome, preço e a quantidade em estoque.
# Tarefa: Crie uma classe Produto que inicialize com os atributos nome, preco (um float) e estoque (um inteiro).

class Produto:
    def __init__(self, nome, preco: float, estoque:int):
        self.nome = nome 
        self.preco = preco 
        self.estoque = estoque

produto = Produto("celular", 980.00, 50)

print(produto.nome)
print(produto.preco)
print(produto.estoque)