# 18) Uma universidade precisa de um sistema simples para associar professores às disciplinas que eles lecionam. 
# Tarefa: • Crie uma classe Disciplina com um atributo nome.
# • Crie uma classe Professor com os atributos nome e disciplinas_lecionadas (uma lista vazia).
# • Crie um método lecionar_disciplina(disciplina) na classe Professor que recebe um objeto Disciplina e o adiciona à sua lista.

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
    
class Professor:
    def __init__(self, nome):
           self.nome = nome 
           self.disciplinas_lecionadas = []

    def lecionar_disciplina(self, disciplina):
        self.disciplinas_lecionadas.append(disciplina)

    
disciplina = Disciplina("Matemática")

professor = Professor("José")
professor.lecionar_disciplina(disciplina) 

print(professor.nome)


for disciplina in professor.disciplinas_lecionadas:
  print(disciplina.nome )
  