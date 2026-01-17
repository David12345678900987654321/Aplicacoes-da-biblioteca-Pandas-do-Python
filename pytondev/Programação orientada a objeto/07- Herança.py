class Game:
    TotalDeJogos = 0
#método construtor
    def __init__(self, nome="",AnoLançamento=0,multiplayer=False,nota=0):
        Game.TotalDeJogos +=1
        self.nome = nome
        self.Anolançamento=AnoLançamento
        self.multiplayer=multiplayer
        self.nota=nota

    def __str__(self):
        return f"Jogo: {self.nome}"

    def ficha_técnica(self):
        print(f"\nNome do jogo: {self.nome}")
        print(f"Ano de Lançamento: {self.Anolançamento}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"avaliação: {self.nota}\n")

#Classe derivada (Subclasse) Herança
class SinglePlayerGame(Game):
    def __init__(self, nome="",AnoLançamento=0,multiplayer=False,nota=0,História=""):
        super().__init__(nome, AnoLançamento,multiplayer=False,nota=nota)
        self.História = História
    def ficha_técnica(self):
        super().ficha_técnica()
        print(f"Enredo: {self.História}\n")

JogoMultiplayer = Game ("Fortnite",2017,True,8)
JogoMultiplayer.ficha_técnica()
JogoSingleplayer = SinglePlayerGame("Mario",2020,False,9.5,"Jogo de um encanador")
JogoSingleplayer.ficha_técnica()