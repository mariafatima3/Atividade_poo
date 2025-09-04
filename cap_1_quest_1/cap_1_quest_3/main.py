# 3) Uma agência de viagens precisa de um conversor rápido para valores fixos de moedas para seus pacotes turísticos. 
# A cotação do dia já está definida. Tarefa: Crie uma classe chamada ConversorSimples com os seguintes métodos:
# • real_para_dolar(valor_real): recebe um valor em reais e o retorna em dólares (considere 1 dólar = 5.25 reais).
# • dolar_para_real(valor_dolar): recebe um valor em dólares e o retorna em reais (considere 1 dólar = 5.25 reais).

class ConversorSimples:
    def real_para_dolar(self, valor_real):
        return(valor_real /5.25)

    def dolar_para_real(self, valor_dolar):
        return(valor_dolar * 5.25)

Converter = ConversorSimples()

print(Converter.real_para_dolar (10.35))

print(Converter.dolar_para_real(2.25))