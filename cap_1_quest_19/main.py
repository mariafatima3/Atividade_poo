# 19) O sistema de e-commerce precisa de um carrinho de compras funcional. O carrinho deve conter produtos, mas também deve controlar a quantidade de cada um, 
# garantindo que não se possa adicionar mais produtos do que há em estoque. Tarefa:
# • Crie a classe Produto com nome, preco e estoque.
# • Crie a classe CarrinhoDeCompras. Ela deve ter um atributo itens, que pode ser um dicionário (ex: {'nome_produto': quantidade}).
# • Crie os métodos no CarrinhoDeCompras: o adicionar_produto(produto, quantidade): recebe um objeto Produto e uma quantidade. O método deve verificar se a 
# quantidade desejada é menor ou igual ao estoque do produto. Se for, adiciona ao carrinho e diminui o estoque do objeto Produto. Se não, exibe uma mensagem de erro.
# o finalizar_compra(): calcula e retorna o valor total dos itens no carrinho.

class Produto:
   def __init__(self, nome, preco:float, estoque:int):
      self.nome = nome
      self.preco = preco
      self.estoque = estoque
   
class CarrinhoDeCompras:
   def __init__(self):
      self.itens = {}
      
   def adicionar_produto(self, produto, quantidade):
       if quantidade <= produto.estoque:
            if produto.nome in self.itens:
                # Atualiza quantidade já no carrinho
                self.itens[produto.nome] = (produto, self.itens[produto.nome][1] + quantidade)
            else:
                self.itens[produto.nome] = (produto, quantidade)
            produto.estoque -= quantidade
            print(f"{quantidade} unidade(s) de '{produto.nome}' adicionada(s) ao carrinho.")
       else:
            print(f"Erro: Estoque insuficiente para '{produto.nome}'. Disponível: {produto.estoque}.")


   def finalizar_compra(self):
      valor_total = 0.0
      print("\nResumo da compra:")
      for nome, (produto, quantidade) in self.itens.items():
            subtotal = produto.preco * quantidade
            print(f"{produto.nome} - {quantidade} x R${produto.preco:.2f} = R${subtotal:.2f}")
            valor_total += subtotal
      print(f"\nTotal da compra: R${valor_total:.2f}")
      return valor_total

produto = Produto("Notebook", 2500.00, 10)

print("Adicionar produto de carinho:")

carrinhoDeCompras = CarrinhoDeCompras()
carrinhoDeCompras.adicionar_produto(produto, 3)
carrinhoDeCompras.finalizar_compra()
 


