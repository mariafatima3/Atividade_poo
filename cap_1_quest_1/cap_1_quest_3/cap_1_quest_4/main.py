# 4) Desenvolvedores de um jogo de RPG de mesa digital precisam de uma forma de simular a rolagem de diferentes tipos de dados
# (D6, D12, D20) sem precisar guardar os resultados, apenas obtendo um valor aleatório a cada chamada. Tarefa: Crie uma
# classe RoloDeDados com os seguintes métodos. (Dica: use o módulo random do Python).
# • rolar_d6(): retorna um número aleatório entre 1 e 6.
# • rolar_d12(): retorna um número aleatório entre 1 e 12.
# • rolar_d20(): retorna um número aleatório entre 1 e 20.

import random
class RoloDeDados:
    def  rolar_d6(self):
        return(random.randint(1,6))

    def  rolar_d12(self):
        return(random.randint(1,12))

    def  rolar_d20(self):
        return(random.randint(1, 20))

jogo = RoloDeDados()

print(jogo.rolar_d6())

print(jogo.rolar_d12())

print(jogo.rolar_d20())
    