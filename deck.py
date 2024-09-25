from carta import Carta

class Deck:

    def __init__(self):
        self.deck = []
        self.numCartas = 0

    def addCarta(self,carta):
        self.deck[self.numCartas] = carta
        self.numCartas +=1