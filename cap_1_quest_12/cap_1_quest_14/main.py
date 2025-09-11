# 14) No desenvolvimento de um RPG, cada personagem tem um nome, nível de vida (HP) e pontos de ataque. Eles precisam ser 
# capazes de atacar outros personagens e receber dano. Tarefa: Crie uma classe Personagem com os atributos nome, vida e ataque.
#  Crie os métodos: 
# • atacar_oponente(alvo): recebe outro objeto Personagem (o alvo) e diminui a vida do alvo pelo valor de ataque do atacante.
# • receber_dano(dano): diminui a vida do personagem pelo valor do dano recebido. A vida não pode ser menor que 0.

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar_oponente(self, alvo):
        if alvo == self:
            print(f"Não pode atacar a si mesmo")
        else:
         alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0 

    def __str__(self):
        return f"Nome: {self.nome}, Vida:{self.vida}, Ataque: {self.ataque} "   
    
personagem1 = Personagem("Vivi", 10, 2)           
personagem2 = Personagem("Lyra", 8, 3)

personagem1.atacar_oponente(personagem2)
personagem1.atacar_oponente(personagem1)

print(personagem1)
print(personagem2)




