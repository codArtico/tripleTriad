class Tabuleiro:
    def __init__(self):
        self.slots = [None,None,None],[None,None,None],[None,None,None]
        self.cartasColocadas = 0

    def colocarCarta(self,linha,coluna,carta):
        if self.slots[linha][coluna] == None:
            self.slots[linha][coluna] = carta
            cartasColocadas +=1
            return True
        else:
            print("Jogada inválida, insira uma posição dísponível!")
            return False

    def tabuleiroCheio(self): #Não é necessário passar parâmetro (Self == This)
        if (self.cartasColocadas == 9):
            return True
        return False