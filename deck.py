class Deck:

    def __init__(self):
        deck = []
        numCartas = 0

    def addCarta(self,carta):
        self.deck[self.numCartas] = carta
        self.numCartas +=1