# 13) Em uma escola de magia, os aprendizes precisam de uma ferramenta para calcular rapidamente as propriedades de seus círculos de invocação. 
# Tarefa: Crie uma classe Circulo que seja inicializada com um raio. Crie os métodos:
# • calcular_area(): retorna a área do círculo (A=π⋅r2).
# • calcular_circunferencia(): retorna a circunferência do círculo (C=2⋅π⋅r).

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        
    def calcular_area(self):
         return math.pi * self.raio ** 2

    def calcular_circunferencia(self):
        return  2 * math.pi * self.raio
    

circulo = Circulo(6)

print("Área:", circulo.calcular_area())
print("Circunferencia:", circulo.calcular_circunferencia())
        