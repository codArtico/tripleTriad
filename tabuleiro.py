class Tabuleiro:
    def __init__(self):
        self.slots = [None,None,None],[None,None,None],[None,None,None]

    def colocarCarta(self,linha,coluna,carta):
        if self.slots[linha][coluna] == None:
            self.slots[linha][coluna] = carta
        else:
            while(self.slots[linha][coluna] != None):
                print("Jogada inválida, insira uma posição dísponível!")