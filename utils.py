import os
import platform


class Util:
    @staticmethod
    def limpa():
        # Identifica o sistema operacional
        sistema = platform.system()

        if sistema == "Windows":
            os.system("cls")
        else:
            os.system("clear")
        Util._logo()

    @staticmethod
    def _logo():
        print(
            "███████ ██████ ████ ███████ ██      █████████    ██████ ████████ ██ ███████  ██████"
        )
        print(
            "  ██    ██  ██  ██  ██   ██ ██      ██             ██    ██   ██ ██ ██   ██ ██   ██"
        )
        print(
            "  ██    ██████  ██  ██████  ██      ████████       ██    ██████  ██ ███████ ██   ██"
        )
        print(
            "  ██    ██   ██ ██  ██      ██      ██             ██    ██   ██ ██ ██   ██ ██   ██"
        )
        print(
            "  ██    ██   ██ ██  ██      ███████ ████████       ██    ██   ██ ██ ██   ██ ██████ "
        )
        print("")

    @staticmethod
    def excecao(mensagem):
        while True:
            try:
                numero = int(input(mensagem))
                return numero
            except ValueError:
                print("Por favor, digite um número válido")