from deck import Deck

class Jogador:
    def __init__ (self,cor,nome):
        self.nome = nome
        self.deck = Deck()
        self.pontuacao = 5
        self.inicial = False
        self.cor = cor