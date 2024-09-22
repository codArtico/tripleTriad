from deck import Deck

class Jogador:
    def __init__ (self):
        self.nome = ""
        self.deck = Deck()
        self.pontuacao = 5
        self.inicial = False