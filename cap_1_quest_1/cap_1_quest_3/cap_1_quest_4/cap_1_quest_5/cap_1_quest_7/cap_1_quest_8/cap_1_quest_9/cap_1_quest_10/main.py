# 10) Um desenvolvedor de jogos quer criar um objeto que guarde as configurações de um jogador, como resolucao_tela (ex: "1920x1080"), volume_audio (um inteiro de 0 a 100) e 
# dificuldade (ex: "Fácil"). Tarefa: Crie uma classe ConfiguracaoJogo que armazene os três atributos (resolucao_tela, volume_audio, dificuldade) ao ser instanciada.

class ConfiguracaoJogo:
    def __init__(self, tela, audio, dificuldade):

        self.resolucao_tela = tela
        self.volume_audio = audio
        self.dificuldade = dificuldade
       
configuracao = ConfiguracaoJogo( "2560x1440", 55 , "Fácil")


print(configuracao.resolucao_tela)
print(configuracao.volume_audio)
print(configuracao.dificuldade )