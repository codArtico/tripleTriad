from colorama import Fore, Back, Style, init
from carta import Carta
from jogador import Jogador
from tabuleiro import Tabuleiro

def fazerDeck(p):
    deck = []
    for i in range (5):
        c = Carta()
        c.setDono(p)
        deck.append(c)
    return deck

nome = (input("Insira um nome: "))
p1 = Jogador(Back.BLUE,nome)
p1.deck.deck = fazerDeck(p1)

nome = (input("Insira um nome: "))
p2 = Jogador(Back.RED,nome)
p2.deck.deck = fazerDeck(p2)

player = 1
p1Index = 0
p2Index = 0

t = Tabuleiro(p1,p2)

#Lógica do jogo
while not(t.tabuleiroCheio()):
    t.imprimir_tabuleiro()
    linha = (input("Escolha a linha: "))
    coluna = (input("Escolha a coluna: "))
    if player == 1:
        if t.colocarCarta(int(linha), int(coluna), p1.deck.deck[p1Index]):
            t.verificarVizinhas(int(linha),int(coluna),p1.deck.deck[p1Index])
            p1Index +=1
            player = 2
    else:
        if t.colocarCarta(int(linha), int(coluna), p2.deck.deck[p2Index]):
            t.verificarVizinhas(int(linha),int(coluna),p2.deck.deck[p2Index])
            p2Index +=1
            player = 1
    print(f"{p1.nome}: {p1.pontuacao}")
    print(f"{p2.nome}: {p2.pontuacao}")

t.imprimir_tabuleiro()

if p1.pontuacao>p2.pontuacao:
    print(f"{p1.nome} ganhou!")
elif p2.pontuacao>p1.pontuacao:
    print(f"{p2.nome} ganhou!")
else:
    print("Empate")