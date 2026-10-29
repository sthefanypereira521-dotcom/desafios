from calcular_fretes import Moto, Carro, Caminhao, Drone
from rich import print, inspect
from rich.table import Table


def main():
    dist = 80

    viagem = [Moto(dist), Carro(dist), Caminhao(dist), Drone(dist)]

    

    """entrega = Drone(dist)
    print(
        f"frete de {type(entrega).__name__} em {dist}KM = {entrega.calcular_frete()}")"""


    tabela = Table(title= "tabela de fretes")
    tabela.add_column("distancia")
    tabela.add_column("tipo")
    tabela.add_column("frete")

    for item in viagem:
        tabela.add_row(f"{dist}km", f"{type(item).__name__}", f"{item.calcular_frete()}")

    print(tabela)


if __name__ == "__main__":
    main()
