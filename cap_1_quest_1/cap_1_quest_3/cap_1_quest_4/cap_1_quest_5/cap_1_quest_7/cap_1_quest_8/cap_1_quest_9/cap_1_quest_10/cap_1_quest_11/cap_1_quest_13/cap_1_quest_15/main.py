# 15) Um serviço de streaming de música quer que seus usuários possam criar playlists. Uma playlist deve ter um nome e uma lista de músicas,
# com a funcionalidade de adicionar e remover faixas. Tarefa: Crie uma classe Playlist com os atributos nome e musicas (inicializada como uma lista vazia). Crie os métodos:
# • adicionar_musica(musica): adiciona uma string (o nome da música) à lista de musicas.
# • remover_musica(musica): remove uma música da lista.
# • listar_musicas(): imprime no console todas as músicas da playlist.

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []
    
    def  adicionar_musica(self, musica):
         self.musicas.append(musica)
         print(f"Música: {musica} adicionada a playlist {self.nome}.")

    def remover_musica(self, musica):
        if musica in self.musicas:
            self.musicas.remove(musica)
            print(f"Música: {musica} removida da playlist {self.nome}")
        else:
            print(f"Música: {musica} Música não encontrada na playlist {self.nome}")


    def listar_musicas(self):
        
        if not self.musicas:
            print(f"A playlist {self.nome}, Está vazia.")

        else:
            print(f"Músicas na playlist '{self.nome}':")

            for musica in self.musicas:
                print(f"- {musica}")

playlist = Playlist("Músicas Favoritas")

playlist.adicionar_musica("Jesus filho de Davi.")
playlist.remover_musica("Eu te levatarei")
playlist.listar_musicas()

