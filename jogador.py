from deck import Deck

class Jogador:
    def __init__ (self,cor,nome):
        self.nome = nome
        self.deck = Deck()
        self.pontuacao = 5
        self.inicial = False
        self.cor = cor

    def doarCartaSwap(self,p):
        index = (int(input(f"{self.nome}, informe o indice da carta a ser trocada: ")))
        carta = self.deck.deck.pop(index-1)
        carta.setDono(p)
        return carta
    
    def receberCartaSwap(self, carta):
        self.deck.deck.append(carta)

    def mostrarMao(self):
        print(f"\n{self.nome}, suas cartas:")

        cartas_linha = [""] * 5  #Basicamente, ele vai criar o espaço máximo pra guardar as cartas

        for carta in self.deck.deck:
            carta_formatada = carta.formatar().split('\n') # Ele vai despedaçar a função carta.formatar
            for j in range(5):
                cartas_linha[j] += carta_formatada[j] + " "  # Adiciona espaço entre as cartas
            
        # vai imprimir todas as linhas (for each)
        contLinha = 1
        final = ""
        for linha in cartas_linha:
            print(linha)
            final += f"     {contLinha}     "
            contLinha +=1
            
        print(final)
        print("\n")
