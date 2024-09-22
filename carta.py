from random import randint

class Carta:
    def __init__(self):
        self.valores = {
            'cima': Carta.gerarValor(),
            'direita': Carta.gerarValor(),
            'baixo': Carta.gerarValor(),
            'esquerda': Carta.gerarValor()
            
        }

    def gerarValor(self):
        v = randint(1,11)

        if (v == 11):
            return "A"
        return v