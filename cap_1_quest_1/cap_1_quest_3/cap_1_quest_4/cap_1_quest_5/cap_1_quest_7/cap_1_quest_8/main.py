# 8) Um software de mapeamento precisa representar coordenadas geográficas simplificadas como pontos em um plano 2D.
# Tarefa: Crie uma classe Ponto2D que receba as coordenadas x e y em seu construtor e as armazene.

class Ponto2D:
    def __init__(self, x , y):
        self.x = x
        self.y = y 
        
        
ponto = Ponto2D(4,6)
        
print(f"Ponto X: {ponto.x} e Ponto Y: {ponto.y}. ")
    

    