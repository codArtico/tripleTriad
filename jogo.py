from colorama import Fore, Back, Style, init
from carta import Carta
from jogador import Jogador
from tabuleiro import Tabuleiro

def fazerDeck(p):
    deck = []
    for i in range (10):
        c = Carta()
        c.setDono(p)
        deck.append(c)

    return deck

def select(p,mesa):
    index = (int(input(f"{p.nome}, Escolha 1 carta de 1 a {len(mesa.deck.deck)}: ")))
    while(index<1 or index>len(mesa.deck.deck)):
        index = (int(input(f"Escolha inválida! Escolha 1 carta de 1 a {len(mesa.deck.deck)}: " )))
    carta = mesa.deck.deck.pop(index-1)
    carta.setDono(p)
    p.deck.deck.append(carta)


def selecionarCarta(p1,p2,mesa):
    for i in range (10):
        mesa.mostrarDeckDividido()
        if i%2 == 0:
            select(p1,mesa)
        else:
            select(p2,mesa)

mesa = Jogador(Back.GREEN,"Mesa")
mesa.deck.deck = fazerDeck(mesa)

nome = (input("Insira um nome: "))
p1 = Jogador(Back.BLUE,nome)

nome = (input("Insira um nome: "))
p2 = Jogador(Back.RED,nome)

selecionarCarta(p1,p2,mesa)

p1.mostrarMao()
c1 = p1.doarCartaSwap(p2)  

p2.mostrarMao()
c2 = p2.doarCartaSwap(p1)

p2.receberCartaSwap(c1)   
p1.receberCartaSwap(c2) 


player = 1
index = 0

t = Tabuleiro(p1,p2)

#Lógica do jogo
while not(t.tabuleiroCheio()):
    t.imprimir_tabuleiro()
    
    if player == 1:
        
        p1.mostrarMao()
        index = (int(input("Escolha uma carta de 1 a 5: ")))
        linha = (input("Escolha a linha: "))
        coluna = (input("Escolha a coluna: "))
        
        index -= 1
        if t.colocarCarta(int(linha), int(coluna), p1.deck.deck[index]):
            t.verificarVizinhas(int(linha),int(coluna),p1.deck.deck[index])
            p1.deck.deck.pop(index)
            player = 2
    else:
        p2.mostrarMao()
        index = (int(input("Escolha uma carta de 1 a 5: ")))
        linha = (input("Escolha a linha: "))
        coluna = (input("Escolha a coluna: "))
        
        index -= 1
        if t.colocarCarta(int(linha), int(coluna), p2.deck.deck[index]):
            t.verificarVizinhas(int(linha),int(coluna),p2.deck.deck[index])
            p2.deck.deck.pop(index)
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