from colorama import Fore, Back, Style, init

def atualizarPontuacao(jogador, valor):
    jogador.pontuacao += valor
    if valor > 0:
        print(f"{jogador.nome} agora tem {jogador.pontuacao} pontos.")
    else:
        print(f"{jogador.nome} agora tem {jogador.pontuacao} pontos.")


class Tabuleiro:
    def __init__(self,jogador1,jogador2):
        self.slots = [[None, None, None], [None, None, None], [None, None, None]]
        self.cartasColocadas = 0
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def colocarCarta(self,linha,coluna,carta):

        if coluna<0 or coluna>2:
            print("Jogada inválida, insira uma posição disponível!")
            return False
        elif linha<0 or linha >2:
            print("Jogada inválida, insira uma posição disponível!")
            return False
        else:
            if self.slots[linha][coluna] is None:
                self.slots[linha][coluna] = carta
                self.cartasColocadas +=1
                return True
            else:
                print("Jogada inválida, insira uma posição disponível!")
                return False

    def tabuleiroCheio(self): 
        if self.cartasColocadas == 9:
            return True
        return False
    
    def verificarVizinhas(self, linha, coluna, carta):
        direcoes = {
            'cima': (-1, 0),
            'baixo': (1, 0),
            'esquerda': (0, -1),
            'direita': (0, 1)
        }

        somas = []
        cartasAdj = {}
        oposto = {
            'cima': 'baixo',
            'baixo': 'cima',
            'esquerda': 'direita',
            'direita': 'esquerda'
        }
        
        for direcao, (dx, dy) in direcoes.items():
            ax, ay = linha + dx, coluna + dy
            
            if 0 <= ax < 3 and 0 <= ay < 3 and self.slots[ax][ay]:
                cartaAdjacente = self.slots[ax][ay]
                
                valorAtual = carta.valores[direcao]
                valorAdjacente = cartaAdjacente.valores[oposto[direcao]]
                
                # Convertendo valores 'A' para 10
                if valorAtual == 'A':
                    valorAtual = 10
                if valorAdjacente == 'A':
                    valorAdjacente = 10

                if valorAtual > valorAdjacente:
                    if cartaAdjacente.dono != carta.dono:
                        cartaAdjacente.dono = carta.dono
                        atualizarPontuacao(carta.dono, 1)  # Atualiza a pontuação do jogador que capturou a carta
                        atualizarPontuacao(self.getAdversario(carta.dono), -1)  # Atualiza a pontuação do adversário
                        print(f'Carta na posição {ax},{ay} capturada por {carta.dono.nome} pela regra padrão!')
                
                soma = valorAtual + valorAdjacente
                somas.append((direcao, soma))
                cartasAdj[direcao] = cartaAdjacente

        # Implementação da regra PLUS
        soma_dict = {}
        for direcao, soma in somas:
            if soma not in soma_dict:
                soma_dict[soma] = []
            soma_dict[soma].append(direcao)
        
        # Verifica se há múltiplas direções com o mesmo valor de soma
        for soma, direcoes_lista in soma_dict.items():
            if len(direcoes_lista) > 1:
                for direcao in direcoes_lista:
                    cartaAdj = cartasAdj[direcao]
                    if cartaAdj.dono != carta.dono:
                        cartaAdj.dono = carta.dono
                        atualizarPontuacao(carta.dono, 1)  # Atualiza a pontuação do jogador que capturou a carta
                        atualizarPontuacao(self.getAdversario(carta.dono), -1)  # Atualiza a pontuação do adversário
                        print(f'Carta na posição adjacente capturada por {carta.dono.nome} pela regra PLUS!')



    def getAdversario(self, jogador):
        return self.jogador1 if jogador == self.jogador2 else self.jogador2


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

    def swap(self,i,j,p1,p2):
        v = []
        v.append(p1.deck[i])
        p1.deck.pop(i)
        v.append(p2.deck[j])
        p1.deck.pop(j)
        p1.deck.append[v[1]]
        p2.deck.append[v[0]]