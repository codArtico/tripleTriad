from tabuleiro import Tabuleiro
from deck import Deck
from carta import Carta

class Jogo:

    tab,p1,p2 = None

    def iniciarJogo():
        tab = Tabuleiro()
        #p1 = Jogador()
        #p2 = Jogador()

        name = (input("Digite o nome do jogador 1: "))
        #p1.nome = name
        name = (input("Digite o nome do jogador 2: "))
        #p2.nome = name

        ''' Colocar aqui a lógica de escolher decks

        Colocar aqui a lógica do swap'''


    iniciarJogo()

   # while(not(tab.tabuleiroCheio())): //loop principal do jogo
        #Lógica do jogo aqui

    #//Condição de vitória
        #if p1.pontos > p2.pontos:
        #   print(f"{p1.nome} venceu")
        #else if p2.pontos > p1.pontos:
        #   print(f"{p1.nome} venceu")
        #else:
        #   print("Empate")