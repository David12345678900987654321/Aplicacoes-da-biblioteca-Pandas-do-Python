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

Jogo1 = Game("Mario",1980, False,9.5)
Jogo2 = Game("Mega Man x",1980, False,9.5)
Jogo1.ficha_técnica ()
Jogo2.ficha_técnica ()

print(f"Jogoso criados: {Game.TotalDeJogos}")
