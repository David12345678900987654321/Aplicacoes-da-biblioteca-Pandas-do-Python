class Game:
#método construtor
    def __init__(self, nome="",AnoLançamento=0,multiplayer=False,nota=0):
        self.nome = nome
        self.Anolançamento=AnoLançamento
        self.multiplayer=multiplayer
        self.nota=nota

    def __str__(self):
        return f"Jogo: {self.nome}"

    def ficha_técnica(self):
        print(f"Nome do jogo: {self.nome}")
        print(f"Ano de Lançamento: {self.Anolançamento}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"avaliação: {self.nota}")
class GameStudio:
    def __init__(self, nome=""):
        self.nome = nome
        self.Jogos = []

    def AdicionarJogo(self, jogo):
        self.Jogos.append(jogo)