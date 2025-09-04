# 7) Você está criando a primeira versão de uma rede social e precisa de uma forma de representar os usuários no sistema, guardando apenas seu nome e e-mail.
# Tarefa: Crie uma classe Usuario que, ao ser criada, receba nome e email e os guarde em atributos com os mesmos nomes.


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

nome = input("Digite seu nome: ")

email = input("Digite email: ")

conta = Usuario (nome, email)
print(conta.nome)
print(conta.email)