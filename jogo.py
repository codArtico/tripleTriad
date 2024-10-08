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


def receberLinha():
    x = Util.excecao("Escolha a linha de 1 a 3:")
    x -= 1
    return x


def receberColuna():
    x = Util.excecao("Escolha a coluna de 1 a 3:")
    x -= 1
    return x


# Realiza Jogada
def realizarJogada(p, t):
    p.mostrarMao()

    index = Util.excecao(f"Escolha uma carta de 1 a {len(p.deck)}: ")
    index -= 1

    linha = receberLinha()

    coluna = receberColuna()

    while not t.colocarCarta(int(linha), int(coluna), p.deck[index]):
        linha = receberLinha()

        coluna = receberColuna()

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
