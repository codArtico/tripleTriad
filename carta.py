class Carta:
    def __init__(self, cima, direita, baixo, esquerda, dono):
        self.valores = {
            'cima': cima,
            'direita': direita,
            'baixo': baixo,
            'esquerda': esquerda
            
        }
        self.dono = dono