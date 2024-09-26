from carta import Carta
from utils import Util


# gera as cartas aleatoriamente pra os players escolherem
def fazerDeck(p):
    deck = []
    for i in range(10):
        c = Carta()
        c.setDono(p)
        deck.append(c)

    return deck


# Realiza Jogada
def realizarJogada(p, t):
    p.mostrarMao()
    index = input(f"Escolha uma carta de 1 a {len(p.deck)}: ")
    while not index.isdigit() or int(index) < 1 or int(index) > len(p.deck):
        index = input(f"Escolha inválida! Escolha uma carta de 1 a {len(p.deck)}: ")
    linha = input("Escolha a linha: ")
    while not linha.isdigit() or 0 < linha < 3:
        linha = int(input(f"linha inválida, escolha uma linha de 1 a 3: "))
    coluna = input("Escolha a coluna: ")
    while not coluna.isdigit() or 0 < coluna < 3:
        coluna = int(input(f"coluna inválida, escolha uma coluna de 1 a 3: "))

    int(index)
    index -= 1
    if t.colocarCarta(int(linha) - 1, int(coluna) - 1, p.deck[index]):
        t.verificarVizinhas(int(linha), int(coluna), p.deck[index])
        p.deck.pop(index)
    return t


def checarVitoria(p1, p2):
    if p1.pontuacao > p2.pontuacao:
        return p1.nome
    elif p2.pontuacao > p1.pontuacao:
        return p2.nome
    else:
        return None


def placarFinal(p1, p2):
    print("Fim de jogo! Placar final: \n\n")
    print(f"{p1.nome} {p1.pontuacao} x {p2.pontuacao} {p2.nome} \n\n")
    print(f"{checarVitoria(p1,p2)} ganhou!")


def exibirPlacar(p1, p2):
    print(f"{p1.nome}: {p1.pontuacao}")
    print(f"{p2.nome}: {p2.pontuacao}")


def rodada(p, t):
    input(f"{p.nome}, pressione ENTER para continuar!")
    Util.limpa()
    t.imprimir_tabuleiro()
    realizarJogada(p, t)
