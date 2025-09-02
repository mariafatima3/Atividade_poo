# Uma startup de design gráfico precisa de uma ferramenta simples para realizar cálculos rápidos de geometria.
# Eles não precisam guardar nenhuma informação, apenas calcular valores sob demanda. 
# Tarefa: Crie uma classe chamada CalculadoraGeometrica com os seguintes métodos:
# • calcular_area_quadrado(lado): recebe o lado de um quadrado e retorna sua área.
# • calcular_area_circulo(raio): recebe o raio de um círculo e retorna sua área (use 3.1415 para π).

class CalculadoraGeometrica:
   def calcular_area_quadrado(self, lado): 
      print(lado * lado)
    
   def calcular_area_circulo(self, raio): 
      print(3.1415 * raio *  raio)

calculadora = CalculadoraGeometrica()

calculadora.calcular_area_quadrado(12)

calculadora.calcular_area_circulo(4)