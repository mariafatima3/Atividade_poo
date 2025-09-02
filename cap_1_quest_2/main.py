# 2) Um blogueiro precisa de ajuda para padronizar os títulos de suas postagens. Ele quer uma ferramenta que aplique diferentes
# formatações a um texto. Tarefa: Crie uma classe chamada FormatadorDeTexto com os seguintes métodos:
# • para_caixa_alta(texto): recebe uma string e a retorna em maiúsculas.
# • para_caixa_baixa(texto): recebe uma string e a retorna em minúsculas.

class FormatadorDeTexto:
    def para_caixa_alta(self, texto):
        print(texto.upper())

    def para_caixa_baixa(self, texto): 
        print(texto.lower())    

formatador = FormatadorDeTexto()

formatador.para_caixa_alta("boa tarde")

formatador.para_caixa_baixa("BOA TARDE")
  