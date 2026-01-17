class Game:
#método construtor
    def __init__(self, nome="",AnoLançamento=0,multiplayer=False,nota=0):
        self.nome = nome
        self.Anolançamento=AnoLançamento
        self.multiplayer=multiplayer
        self.nota=nota

    def __str__(self):
        return f"Jogo: {self.nome}"

Jogo1 = Game("Mario",1980, False,9.5) 
print(Jogo1.nome)   