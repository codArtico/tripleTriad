from random import randint
from colorama import Fore, Back, Style, init

# Inicializa o Colorama
init(autoreset=True)


def gerarValor():
    v = randint(1,10)

    if v == 10:
        return "A"
    return v


class Carta:
    def __init__(self):
        self.cor = None
        self.valores = {
            'cima': gerarValor(),
            'direita': gerarValor(),
            'baixo': gerarValor(),
            'esquerda': gerarValor()
            
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
            "__________{Style.RESET_ALL}"
        )