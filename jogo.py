# Importações (Cor e POO)
from colorama import Fore, Back, Style, init
from carta import Carta
from jogador import Jogador
from tabuleiro import Tabuleiro

#Método que gera as cartas aleatoriamente pra os players escolherem
def fazerDeck(p):
    deck = []
    for i in range (10):
        c = Carta()
        c.setDono(p)
        deck.append(c)

    return deck

# Método pra selecionar a carta (Faz parte do selecionarCarta())
def select(p,mesa):
    index = (int(input(f"{p.nome}, Escolha 1 carta de 1 a {len(mesa.deck)}: ")))
    while(index<1 or index>len(mesa.deck)):
        index = (int(input(f"Escolha inválida! Escolha 1 carta de 1 a {len(mesa.deck)}: " )))
    carta = mesa.deck.pop(index-1)
    carta.setDono(p)
    p.deck.append(carta)

# Método para seleção de decks
def selecionarCarta(p1,p2,mesa):
    for i in range (10):
        mesa.mostrarDeckDividido()
        if i%2 == 0:
            select(p1,mesa)
        else:
            select(p2,mesa)

# Método para Realizar Jogada
def realizarJogada(p):
    p.mostrarMao()
    index = (int(input(f"Escolha uma carta de 1 a {len(p.deck)}: ")))
    while(index < 1 or index >len(p.deck)):
        index = (int(input(f"Escolha inválida! Escolha uma carta de 1 a {len(p.deck)}: ")))
    linha = (input("Escolha a linha: "))
    coluna = (input("Escolha a coluna: "))
    
    index -= 1
    if t.colocarCarta(int(linha), int(coluna), p.deck[index]):
        t.verificarVizinhas(int(linha),int(coluna),p.deck[index])
        p.deck.pop(index)

# Configuração da mesa
mesa = Jogador(Back.GREEN,"Mesa")
mesa.deck = fazerDeck(mesa)

# Configuração dos players
nome = (input("Insira um nome: "))
p1 = Jogador(Back.BLUE,nome)
nome = (input("Insira um nome: "))
p2 = Jogador(Back.RED,nome)

# Criando decks
selecionarCarta(p1,p2,mesa)

# Hora do SWAP
p1.mostrarMao()
c1 = p1.doarCartaSwap(p2)

p2.mostrarMao()
c2 = p2.doarCartaSwap(p1)

p2.receberCartaSwap(c1)   
p1.receberCartaSwap(c2) 

# Configurações gerais (Marcador do player da vez)
player = 1

# Criação do Tabuleiro
t = Tabuleiro(p1,p2)

#Lógica do jogo
while not(t.tabuleiroCheio()):
    t.imprimir_tabuleiro()
    
    if player == 1:
        input(f"{p1.nome}, pressione ENTER para continuar!")
        realizarJogada(p1)
        player = 2
    else:
        input(f"{p2.nome}, pressione ENTER para continuar!")
        realizarJogada(p2)
        player = 1

    # Exibe pontuação dos dois jogadores a cada rodada
    print(f"{p1.nome}: {p1.pontuacao}")
    print(f"{p2.nome}: {p2.pontuacao}")

# Tabuleiro final
t.imprimir_tabuleiro()


#Condições de vitória
if p1.pontuacao>p2.pontuacao:
    print(f"{p1.nome} ganhou!")
elif p2.pontuacao>p1.pontuacao:
    print(f"{p2.nome} ganhou!")
else:
    print("Empate")