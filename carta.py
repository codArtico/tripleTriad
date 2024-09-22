from random import randint

class Carta:
    def __init__(self):
        self.valores = {
            'cima': Carta.gerarValor(),
            'direita': Carta.gerarValor(),
            'baixo': Carta.gerarValor(),
            'esquerda': Carta.gerarValor()
            
        }

    def gerarValor():
        v = randint(1,10)

        if (v == 10):
            return "A"
        return v
    
    def formatar(self):
        """Retorna uma string formatada com o estilo de caixa com margens específicas."""
        cima = f"{self.valores['cima']:^8}"  # 4 espaços de margem em cada lado
        baixo = f"{self.valores['baixo']:^8}"  # 4 espaços de margem em cada lado
        esquerda = f"{self.valores['esquerda']}   {self.valores['direita']}"  # 1 espaço de margem antes e depois, 3 espaços entre
        return (
            "__________\n"
            f"|{cima}|\n"
            f"| {esquerda} | \n"
            f"|{baixo}|\n"
            "__________"
        )