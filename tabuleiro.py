from colorama import Fore, Back, Style, init

class Tabuleiro:
    def __init__(self):
        self.slots = [None,None,None],[None,None,None],[None,None,None]
        self.cartasColocadas = 0

    def colocarCarta(self,linha,coluna,carta):

        if coluna<0 or coluna>2:
            print("Jogada inválida, insira uma posição dísponível!")
            return False
        elif linha<0 or linha >2:
            print("Jogada inválida, insira uma posição dísponível!")
            return False
        else:
            if self.slots[linha][coluna] == None:
                self.slots[linha][coluna] = carta
                self.cartasColocadas +=1
                return True
            else:
                print("Jogada inválida, insira uma posição dísponível!")
                return False

    def tabuleiroCheio(self): 
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

        somas = []

        cartasAdj = {

        }

        oposto = {
            'cima':'baixo', 
            'baixo':'cima', 
            'esquerda':'direita', 
            'direita':'esquerda'
            }
            
            
        
        for direcao, (dx,dy) in direcoes.items():
            ax,ay = linha+dx,coluna+dy
            
            if 0 <= ax < 3 and 0 <= ay < 3 and self.slots[ax][ay]:
                cartaAdjacente = self.slots[ax][ay]
                
                valorAtual = carta.valores[direcao]
                valorAdjacente = cartaAdjacente.valores[oposto[direcao]]

                if valorAtual>valorAdjacente:
                    cartaAdjacente.dono = carta.dono
                    print(f'Carta na posição {ax},{ay} capturada por {carta.dono} pela regra padrão!')
                
                soma = valorAtual+valorAdjacente
                somas.append = ((direcao,soma))
                cartasAdj[direcao] = cartaAdjacente
        
        for i in range (len(somas)):
            for j in range(i+1,len(somas)):
                if somas[i][1] == somas [j][1]:
                    direcao1, direcao2 = somas[i][0], somas[j][0]
                    cartaAdj1 = cartasAdj[direcao1]
                    cartaAdj2 = cartasAdj[direcao2]
                    cartaAdj1.dono = carta.dono
                    cartaAdj2.dono = carta.dono

    def imprimir_linha(self, linha):
        """Imprime uma linha do tabuleiro formatada com alinhamento garantido e cores das cartas."""
        if not (0 <= linha < 3):
            raise ValueError("Índice de linha inválido. Deve estar entre 0 e 2.")

        # Prepara a estrutura de linhas para cada carta na linha específica
        linhas = [""] * 4  # 4 linhas para cada carta

        for j in range(3):
            carta = self.slots[linha][j]
            if carta is None:
                carta_formatada = (
                    f"{Style.RESET_ALL}__________{Style.RESET_ALL}\n"
                    f"{Style.RESET_ALL}|        |{Style.RESET_ALL}\n"
                    f"{Style.RESET_ALL}|        |{Style.RESET_ALL}\n"
                    f"{Style.RESET_ALL}|        |{Style.RESET_ALL}\n"
                    f"{Style.RESET_ALL}__________{Style.RESET_ALL}"
                )
            else:
                carta_formatada = carta.formatar()

            # Adiciona cada linha formatada da carta na linha correspondente da impressão do tabuleiro
            carta_linhas = carta_formatada.split('\n')
            for k in range(len(carta_linhas)-1):
                if j == 0:
                    linhas[k] = carta_linhas[k]  # Primeiro item em cada linha
                else:
                    linhas[k] += " " + carta_linhas[k]  # Adiciona espaço e adiciona o próximo item

        # Imprime a linha formatada
        for linha in linhas:
            print(linha)
        
        #imprime linha no final
        print(f"{Style.RESET_ALL}__________ __________ __________{Style.RESET_ALL}")
        
        
    def imprimir_tabuleiro(self):
        self.imprimir_linha(0)
        self.imprimir_linha(1)
        self.imprimir_linha(2)