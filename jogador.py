from deck import Deck

class Jogador:
    def __init__ (self,cor):
        self.nome = ""
        self.deck = Deck()
        self.pontuacao = 5
        self.inicial = False
        self.cor = cor