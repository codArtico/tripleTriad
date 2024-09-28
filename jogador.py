from random import randint


class Jogador:
    def __init__(self, cor, nome):
        self.nome = nome
        self.deck = []
        self.pontuacao = 5
        self.inicial = False
        self.cor = cor

    # Sistema de funções do SWAP
    def cartaSwap(self, p):
        index = randint(1, 5)
        carta = self.deck.pop(index - 1)
        carta.setDono(p)
        return carta

    def receberCartaSwap(self, carta):
        self.deck.append(carta)

    # Mostra as cartas do Player
    def mostrarMao(self):
        print(f"\n{self.nome}, suas cartas:")

        cartas_linha = [
            ""
        ] * 5  # Basicamente, ele vai criar o espaço máximo para guardar as cartas

        for carta in self.deck:
            carta_formatada = carta.formatar().split(
                "\n"
            )  # Ele vai despedaçar a função carta.formatar
            for j in range(5):
                cartas_linha[j] += (
                    carta_formatada[j] + " "
                )  # Adiciona espaço entre as cartas

        # vai imprimir todas as linhas (for each)
        contLinha = 1
        final = ""
        for linha in cartas_linha:
            print(linha)
            final += f"     {contLinha}     "
            contLinha += 1

        print(final)
        print("\n")
