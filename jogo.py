from tabuleiro import Tabuleiro
from deck import Deck
from carta import Carta
from jogador import Jogador
from random import randint
from colorama import Fore, Back, Style, init
'''
class Jogo:

    def escolherPlayerInicial(p1,p2):
        sort = randint(1,2)
        if sort == 1:
            p1.inicial = True
        else:
             p2.inicial = True

    def criarDeckEscolha():
        d = Deck()
        
        while(d.numCartas!=10):
            carta = Carta()
            d.append(carta)
        return d  

    tab = Tabuleiro()
    
    deckEscolha = criarDeckEscolha()

    def escolherCarta(deckEscolha,p):
        for i in range(len(deckEscolha)):
                print(f"[{i}] - {deckEscolha[i]}")
            
        index = input("Selecione sua carta pelo número: ")
        p.deck.append(deckEscolha[index])
        deckEscolha.deck.pop(index)

    #Se um player começa jogando, logo ele tem vantagem no numero de cartas jogadas, sendo assim, o player 2 escolhe primeiro suas cartas e vice versa

    if (p1.inicial):
         while (len(deckEscolha)!=0):
            escolherCarta(p2)
            escolherCarta(p1)
         
    if (p2.inicial):
        while (len(deckEscolha)!=0):
            escolherCarta(p1)
            escolherCarta(p2)

   # while(not(tab.tabuleiroCheio())): //loop principal do jogo
        #Lógica do jogo aqui

    #Condição de vitória
    if p1.pontos > p2.pontos:
        print(f"{p1.nome} venceu")
    elif p2.pontos > p1.pontos:
        print(f"{p1.nome} venceu")
    else:
        print("Empate")
'''
p1 = Jogador(Back.BLUE)
p2 = Jogador(Back.RED)
c1 = Carta()
c1.setDono(p2)
c2 = Carta()
c2.setDono(p1)
c3 = Carta()
c3.setDono(p1)
t = Tabuleiro()
t.colocarCarta(0, 0, c1)
t.colocarCarta(0, 1, c2)
t.colocarCarta(0, 2, c3)
t.colocarCarta(1, 0, c1)
t.colocarCarta(1, 1, c2)
t.colocarCarta(1, 2, c3)
t.colocarCarta(2, 0, c1)
t.colocarCarta(2, 1, c2)
t.colocarCarta(2, 2, c3)
t.imprimir_tabuleiro()