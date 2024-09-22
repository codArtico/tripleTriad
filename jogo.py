from tabuleiro import Tabuleiro
from deck import Deck
from carta import Carta
from jogador import Jogador
from random import randint
from colorama import Fore, Back, Style, init

def fazerDeck(p):
    deck = []
    for i in range (5):
        c = Carta()
        c.setDono(p)
        deck.append(c)
    return deck


p1 = Jogador(Back.BLUE)
p1.deck.deck = fazerDeck(p1)
p2 = Jogador(Back.RED)
p2.deck.deck = fazerDeck(p2)

player = 1
p1Index = 0
p2Index = 0

t = Tabuleiro()


#Lógica do jogo
while(not(t.tabuleiroCheio())):
    t.imprimir_tabuleiro()
    linha = (input("Escolha a linha: "))
    coluna = (input("Escolha a coluna: "))
    if player == 1:
        if(t.colocarCarta(int(linha),int(coluna),p1.deck.deck[p1Index])):
            p1Index +=1
            player = 2
    else:
        if(t.colocarCarta(int(linha),int(coluna),p2.deck.deck[p2Index])):
            p2Index +=1
            player = 1

t.imprimir_tabuleiro()
