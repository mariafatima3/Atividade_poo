# 12) Um banco digital precisa de uma representação de uma conta corrente para seu aplicativo. A conta tem um titular, um saldo e permite depósitos e saques. 
# Tarefa: Crie uma classe ContaBancaria com os atributos titular e saldo. Crie os métodos:
# • depositar(valor): aumenta o saldo.
# • sacar(valor): diminui o saldo, mas apenas se houver saldo suficiente. O método deve retornar True se o saque foi bem-sucedido e False caso contrário.


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def  depositar(self,valor):
        if valor > 0:
            self.saldo += valor   
        else:
            print("Depósito inválido")  

    def sacar(self, valor):
       if self.saldo >= valor:
          self.saldo -= valor
          return True
      else:
        return False
    
   
    
          
           