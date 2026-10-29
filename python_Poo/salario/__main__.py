from calcula_salario import Funcionario, FuncionarioHorista, FuncionarioMensalista
from rich import inspect


def main():
    f1 = FuncionarioHorista("maria", 7.37, 220)
    f1.calcular_salario()
    f1.analisar_salario()

    print()

    f2 = FuncionarioHorista("helio", 2.25, 220)
    f2.calcular_salario()
    f2.analisar_salario()

    print()

    f3 = FuncionarioMensalista("gustavo", 2300)
    f3.calcular_salario()
    f3.analisar_salario()


if __name__ == "__main__":
    main()
