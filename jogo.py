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
c1.setDono(p1)
p1.deck.deck.append(c1)

c2 = Carta()
c2.setDono(p2)
p2.deck.deck.append(c2)

c3 = Carta()
c3.setDono(p1)
p1.deck.deck.append(c3)

c4 = Carta()
c4.setDono(p2)
p2.deck.deck.append(c4)


c5 = Carta()
c5.setDono(p1)
p1.deck.deck.append(c5)


c6 = Carta()
c6.setDono(p2)
p2.deck.deck.append(c6)


c7 = Carta()
c7.setDono(p1)
p1.deck.deck.append(c7)


c8 = Carta()
c8.setDono(p2)
p2.deck.deck.append(c8)


c9 = Carta()
c9.setDono(p1)
p1.deck.deck.append(c9)


c10 = Carta()
c10.setDono(p2)
p2.deck.deck.append(c10)

t = Tabuleiro()
t.colocarCarta(0, 0, p1.deck.deck[0])
t.colocarCarta(0, 1, p2.deck.deck[0])
t.colocarCarta(0, 2, p1.deck.deck[1])
t.colocarCarta(1, 0, p2.deck.deck[1])
t.colocarCarta(1, 1, p1.deck.deck[2])
t.colocarCarta(1, 2, p2.deck.deck[2])
t.colocarCarta(2, 0, p1.deck.deck[3])
t.colocarCarta(2, 1, p2.deck.deck[3])
t.colocarCarta(2, 2, p1.deck.deck[4])
t.imprimir_tabuleiro()