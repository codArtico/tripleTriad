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
    
    def verificarVizinhas (self,linha,coluna,carta):
        direcoes = {
            'cima': (-1, 0),
            'baixo': (1, 0),
            'esquerda': (0, -1),
            'direita': (0, 1)
        }

        somas = {

        }

        cartasAdj = {

        }

        oposto = {
            'cima':'baixo', 
            'baixo':'cima', 
            'esquerda':'direita', 
            'direita':'esquerda'
            }
            
            
        
        for direcao, (dx,dy) in direcoes.items:
            ax,ay = linha+dx,coluna+dy
            
            if 0 <= ax < 3 and 0 <= ay < 3 and self.slots[ax][ay]:
                cartaAdjacente = self.slots[ax][ay]
                
                valorAtual = carta.valores[direcao]
                valorAdjacente = cartaAdjacente.valores[oposto[direcao]]

                if valorAtual>valorAdjacente:
                    cartaAdjacente.dono = carta.dono
                    print(f'Carta na posição {ax},{ay} capturada por {carta.dono} pela regra padrão!')
                
                soma = valorAtual+valorAdjacente
                somas[direcao] = soma
                cartasAdj[direcao] = cartaAdjacente
        
        for direcao1, soma1 in direcoes.items:
            for direcao2, soma2 in direcoes.items:
                if direcao1 != direcao2 and soma1 == soma2:
                    cartaAdj1 = cartasAdj [direcao1]
                    cartaAdj2 = cartaAdj2 [direcao2]
                    cartaAdj1.dono = carta.dono
                    cartaAdj2.dono = carta.dono
                    print(f'Capturou as cartas em {direcao1} e {direcao2} pela regra Plus!')

