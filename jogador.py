from deck import Deck

class Jogador:
    def __init__ (self,cor,nome):
        self.nome = nome
        self.deck = Deck()
        self.pontuacao = 5
        self.inicial = False
        self.cor = cor

    def doarCartaSwap(self):
        index = (int(input(f"{self.nome}, informe o indice da carta a ser trocada: ")))
        return self.deck.deck[index]
    
    def receberCartaSwap(self, carta):
        self.deck.deck.append(carta)