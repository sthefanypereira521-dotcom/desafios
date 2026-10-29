from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):

    sal_min = 1621
    inss = 7.5

    def __init__(self, nome=None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod
    def calcular_salario(self):
        pass

    def analisar_salario(self):
        base = self.salario / Funcionario.sal_min

        mensagem = f"o salario de [red]{self.nome}[/] [purple] ({self.__class__.__name__}) [/] e de [blue]R${self.salario:.2f}[/] corresponde a [green]{base:.1f} salarios minimos[/]"

        painel = Panel(mensagem, title="analisando os salarios!", width=50)
        print(painel)


# É o funcionário que recebe pelo número de horas trabalhadas.

class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora=7.37, horas_trab=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trab

    def calcular_salario(self):
        self.salario = self.sal_bruto - \
            (self.sal_bruto * Funcionario.inss / 100)


# É o funcionário que recebe um salário mensal fixo, independentemente de o mês ter 28, 30 ou 31 dias, desde que cumpra suas obrigações contratuais.

class FuncionarioMensalista(Funcionario):

    def __init__(self, nome, sal_bruto=Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calcular_salario(self):
        self.salario = self.sal_bruto - \
            (self.sal_bruto * Funcionario.inss / 100)
