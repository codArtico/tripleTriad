import jogo
import colorama
from mesa import Mesa
from utils import Util
from jogador import Jogador
from tabuleiro import Tabuleiro


def iniciarJogo():
    Util.limpa()
    mesa = Mesa()
    p1, p2 = configPlayers()

    # Criando decks
    Mesa.selecionarCarta(p1, p2, mesa)
    Util.limpa()

    # Hora do SWAP
    input(f"{p1.nome}, pressione ENTER para continuar!")
    Util.limpa()
    p1.mostrarMao()
    c1 = p1.cartaSwap(p2)

    Util.limpa()
    input(f"{p2.nome}, pressione ENTER para continuar!")
    p2.mostrarMao()
    c2 = p2.cartaSwap(p1)

    Util.limpa()
    p2.receberCartaSwap(c1)
    p1.receberCartaSwap(c2)

    # Criação do Tabuleiro
    t = criarTabuleiro(p1, p2)

    # Configurações gerais (Marcador do player da vez)
    player = 1

    while not (t.tabuleiroCheio()):
        t.imprimir_tabuleiro()

        if player == 1:
            jogo.rodada(p1, t)
            player = 2
        else:
            jogo.rodada(p2, t)
            player = 1

        # Exibe pontuação dos dois jogadores a cada rodada

        jogo.exibirPlacar(p1, p2)

    # Tabuleiro final
    Util.limpa()
    t.imprimir_tabuleiro()

    jogo.placarFinal(p1, p2)

    chave = input("Deseja jogar novamente? (S/N): ")
    if chave == "S" or chave == "s":
        return True
    return False


def configPlayers():
    nome = input("Insira o nome do Player 1: ")
    p1 = Jogador(colorama.Back.BLUE, nome)
    nome = input("Insira o nome do Player 2: ")
    p2 = Jogador(colorama.Back.RED, nome)
    Util.limpa()
    return p1, p2


def criarTabuleiro(p1, p2):
    return Tabuleiro(p1, p2)


Util.limpa()
input("Pressione ENTER para jogar!")
Util.limpa()

key = input("Deseja iniciar o jogo? (S/N): ")

if key == "S" or key == "s":
    key = True
    while key:
        key = iniciarJogo()
