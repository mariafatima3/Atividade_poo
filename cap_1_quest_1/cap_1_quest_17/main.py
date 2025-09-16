# 17) O e-commerce agora precisa modelar o conceito de um "Pedido", que é essencialmente uma coleção de produtos que um cliente comprou. Tarefa:
# • Reutilize (ou recrie) a classe Produto do Tópico 2, com nome e preco.
# • Crie uma classe Pedido com os atributos cliente (string) e itens (lista vazia).
# • Crie os métodos no Pedido: o adicionar_item(produto): recebe um objeto Produto e o adiciona à lista de itens.
# o calcular_total(): percorre a lista de itens e retorna a soma dos preços de todos os produtos no pedido.

class Produto:
    def __init__(self, nome, preco: float):
        self.nome = nome 
        self.preco = preco 

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
    
    def adicionar_item(self, produto):
        self.itens.append(produto)
        
    def calcular_total(self):
      return sum(item.preco for item in self.itens)
    
produto = Produto("celular", 980.00)

pedido = Pedido("José")

pedido.adicionar_item(produto)
pedido.calcular_total()

total = pedido.calcular_total()

print(f"Cliente: {pedido.cliente}")
print(f"Total do pedido: R$ {total:.2f}")




