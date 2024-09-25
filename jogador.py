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
        print(f"\n{self.nome}', suas cartas:'")

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

    def mostrarDeckDividido(self):
    # Código pra mostrar cartas da mesa, para escolha. Não confundir com MostrarMao()

        print(f"\n{self.nome}, suas cartas disponíveis:")
        
        num_cartas = len(self.deck.deck)
        max_linhas = 5

        # Divide as cartas em duas linhas
        num_cartas_por_linha = 5 
        num_cartas_total = min(num_cartas, 10) 
        
        cartas_linha1 = [""] * max_linhas
        cartas_linha2 = [""] * max_linhas

        for i in range(num_cartas_total):
            carta = self.deck.deck[i]
            carta_formatada = carta.formatar().split('\n')
            if i < num_cartas_por_linha:
                linha_destino = cartas_linha1
            else:
                linha_destino = cartas_linha2
            
            for j in range(max_linhas):
                if j < len(carta_formatada):
                    linha_destino[j] += carta_formatada[j] + " "  # Adiciona espaço entre cartas

        

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
