import colorama
import jogo
from utils import Util
from jogador import Jogador


class Mesa:
    def __init__(self):
        self.nome = "Mesa"
        self.mesa = Jogador(colorama.Back.GREEN, "Mesa")
        self.deck = jogo.fazerDeck(self.mesa)

    # seleciona a carta (Faz parte do selecionarCarta())
    @staticmethod
    def select(p, mesa):
        index = Util.excecao(f"{p.nome}, Escolha uma carta de 1 a {len(mesa.deck)}: ")
        carta = mesa.deck.pop(index - 1)
        carta.setDono(p)
        p.deck.append(carta)

    #seleção de decks
    @staticmethod
    def selecionarCarta(p1, p2, mesa):
        for i in range(10):
            mesa.mostrarDeckDividido()
            if i % 2 == 0:
                Mesa.select(p1, mesa)
            else:
                Mesa.select(p2, mesa)
            Util.limpa()

    def mostrarDeckDividido(self):
        print("Cartas disponíveis:")

        num_cartas = len(self.deck)
        max_linhas = 5

        # Divide as cartas em duas linhas
        num_cartas_por_linha = 5
        num_cartas_total = min(num_cartas, 10)

        cartas_linha1 = [""] * max_linhas
        cartas_linha2 = [""] * max_linhas

        for i in range(num_cartas_total):
            carta = self.deck[i]
            carta_formatada = carta.formatar().split("\n")
            if i < num_cartas_por_linha:
                linha_destino = cartas_linha1
            else:
                linha_destino = cartas_linha2

            for j in range(max_linhas):
                if j < len(carta_formatada):
                    linha_destino[j] += (
                        carta_formatada[j] + " "
                    )  # Adiciona espaço entre cartas

        # Aqui imprime de 1 a 5
        final = ""
        indices_linha1 = 1

        for linha in cartas_linha1:
            print(linha)
            final += f"     {indices_linha1}     "
            indices_linha1 += 1
        print(final)

        # Aqui imprime de 6 a 10
        final = ""
        indices_linha2 = 6

        for linha in cartas_linha2:
            print(linha)
            final += f"     {indices_linha2}     "
            indices_linha2 += 1
        print(final)
        print("\n")
