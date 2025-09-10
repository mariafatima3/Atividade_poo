# 11) Você está criando um simulador de corrida e precisa modelar um carro. O carro deve ter uma velocidade inicial e ser capaz de acelerar e frear. 
# Tarefa: Crie uma classe Carro com o atributo velocidade (inicializada com 0). Crie os métodos:
# • acelerar(valor): aumenta a velocidade em valor.
# • frear(valor): diminui a velocidade em valor, mas sem deixar a velocidade ficar negativa (o mínimo é 0).

class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, valor):
        if valor > 0:
         self.velocidade += valor

    def frear(self, valor):
        if valor > 0:
         self.velocidade -= valor
        if self.velocidade < 0:
           self.velocidade = 0
        
carro = Carro()

carro.acelerar(80)
carro.frear(60)
print(carro.velocidade)




   