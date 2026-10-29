from abc import ABC, abstractmethod
from rich import print


class BebidaQuente(ABC):

    def preparar(self):
        print("[yellow]--- iniciando o preparo ---[/]")

        self.ferver()
        self.misturar()
        self.servir()

        print("[yellow]--- bebiba pronta ---\n[/]")

    def ferver(self):
        print("1° fervendo algo...")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):

    def misturar(self):
        print(
            "2° passando [bright_blue] agua no [/] coador contendo o [orange4]Pó de café [/]")

    def servir(self):
        print("3° servir em uma xícara...")


class Cha(BebidaQuente):

    def misturar(self):
        print(
            "2° mergulho o [green] sache de cha [/] [bright_blue] na agua [/]")

    def servir(self):
        print("3° servir em uma xícara...")


class ChocolateQuente(BebidaQuente):

    def misturar(self):
        print(
            "2° misturo [bright_white] leite[/] com [orange4]tody com uma colher[/] ")

    def servir(self):
        print("3° servir em uma caneca...")
