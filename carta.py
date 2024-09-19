class Carta:
    def __init__(self, cima, baixo, esquerda, direita, dono):
        self.valores = {
            'cima': cima,
            'baixo': baixo,
            'esquerda': esquerda,
            'direita': direita
        }
        self.dono = dono