# 20) O jogo de RPG agora precisa de uma arena onde dois personagens possam lutar até que a vida de um deles chegue a zero. 
# Tarefa: • Reutilize a classe Personagem do Tópico 3 (nome, vida, ataque). Adicione um método esta_vivo() que retorna True se a vida for maior que 0.
# • Crie uma classe Arena. Crie um método iniciar_batalha(personagem1, personagem2) na classe Arena. Este método deve: Iniciar um loop que continua enquanto ambos os
# personagens estiverem vivos. Em cada rodada do loop, o personagem1 ataca o personagem2, e depois o personagem2 ataca o personagem1.
# Imprimir o status da batalha a cada rodada (ex: "Gandalf ataca Sauron! Vida de Sauron agora é X.").
# Ao final do loop (quando um personagem morrer), declarar o vencedor.

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
       return self.vida > 0
    
    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0 

    def __str__(self):
        return f"Nome: {self.nome}, Vida:{self.vida}, Ataque: {self.ataque} "   
    
class Arena:
    def iniciar_batalha(self, personagem1, personagem2):
        print(f"A Batalha entre {personagem1.nome} e {personagem2.nome} começa!")
        rodada = 1
        
        while personagem1.esta_vivo() and personagem2.esta_vivo():
            print(f"\n Rodada {rodada}")
            if personagem1.esta_vivo():
                dano_p1 = personagem1.ataque
                personagem2.receber_dano(dano_p1)
                print(f"{personagem1.nome} ataca {personagem2.nome} causando {dano_p1} de dano!")
                print(f"Vida de {personagem2.nome} agora é {personagem2.vida}.")
            if not personagem2.esta_vivo():
                break 

            if personagem2.esta_vivo():
                dano_p2 = personagem2.ataque
                personagem1.receber_dano(dano_p2)
                print(f"{personagem2.nome} ataca {personagem1.nome} causando {dano_p2} de dano!")
                print(f"Vida de {personagem1.nome} agora é {personagem1.vida}.")
            rodada += 1
            print("\n Fim da Batalha")
        if personagem1.esta_vivo():
            print(f"O vencedor é {personagem1.nome}!")
        else:
            print(f"O vencedor é {personagem2.nome}!")

personagem1 = Personagem("Vivi", 10, 2)           
personagem2 = Personagem("Lyra", 8, 3)

arena = Arena()
arena.iniciar_batalha(personagem1, personagem2)
print(personagem1)
print(personagem2)

