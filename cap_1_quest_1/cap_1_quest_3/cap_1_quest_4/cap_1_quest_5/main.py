# 5) Uma equipe de desenvolvimento de software quer padronizar as mensagens de log (registros de eventos) do sistema. Eles precisam de uma classe que gere strings de log formatadas.
# Tarefa: Crie uma classe GeradorDeLog com os seguintes métodos:
# • info(mensagem): recebe uma string e retorna uma mensagem formatada como "[INFO] - {mensagem}".
# • alerta(mensagem): recebe uma string e retorna uma mensagem formatada como "[ALERTA] - {mensagem}".
# • erro(mensagem): recebe uma string e retorna uma mensagem formatada como "[ERRO] - {mensagem}".

class GeradorDeLog:
   def info(self, mensagem):
        return f"[INFO] - {mensagem}" 

   def alerta(self, mensagem): 
        return f"[ALERTA] - {mensagem}"
    
   def erro(self, mensagem): 
        return f"[ERRO] - {mensagem}"

gerador = GeradorDeLog()

print (gerador.info("iniciando o sistaema"))

print (gerador.alerta(" meroria cheia "))

print(gerador.erro("falha a conctetar "))