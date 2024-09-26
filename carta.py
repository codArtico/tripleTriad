from random import randint
from colorama import Fore, Back, Style, init

# Inicializa o Colorama
init(autoreset=True)

def gerarValor():
    while True:
        valores = [randint(1, 10) for _ in range(4)]

        contagem = {}
        for valor in valores:
            if valor in contagem:
                contagem[valor] += 1
            else:
                contagem[valor] = 1

        if any(contagem[v] > 2 for v in contagem):
            continue

        if 14 <= sum(v for v in valores) <= 30:
            return ['A' if v == 10 else v for v in valores]

class Carta:
    def __init__(self):
        self.cor = None
        valores = gerarValor()
        self.valores = {
            'cima': valores[0],
            'direita': valores[1],
            'baixo': valores[2],
            'esquerda': valores[3]
        }
        self.dono = None


    def setDono(self,p):
        self.dono = p

    def colocarCor(self):
          self.cor =  Back.RED

    def formatar(self):
        """Retorna uma string formatada com o estilo de caixa com margens específicas."""
        cima = f"{self.valores['cima']:^8}"  # 4 espaços de margem em cada lado
        baixo = f"{self.valores['baixo']:^8}"  # 4 espaços de margem em cada lado
        esquerda = f"{self.valores['esquerda']:^4}{self.valores['direita']:^4}"  # 1 espaço de margem antes e depois, 3 espaços entre
        return (
            f"__________\n"
            f"{self.dono.cor}|{cima}|\n"
            f"{self.dono.cor}|{esquerda}|\n"
            f"{self.dono.cor}|{baixo}|\n"
            "__________"
    )