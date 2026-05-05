from abc import ABC, abstractmethod
from pydantic import BaseModel, Field
from datetime import datetime
from rich import print
from rich.panel import Panel


class Cliente(BaseModel):
    nome: str
    cpf: str
    endereco: str


class Registro(BaseModel):
    tipo: str
    valor: float
    data: datetime = Field(default_factory=datetime.now)


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar(self, registro):
        self._transacoes.append(registro)

    @property
    def transacoes(self):
        return self._transacoes


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._Historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def historico(self):
        return self._Historico

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

            registro = Registro(
                tipo="Deposito",
                valor=valor
            )

            self._Historico.adicionar(registro)

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor

            registro = Registro(
                tipo="Saque",
                valor=valor
            )

            self._Historico.adicionar(registro)


class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite):
        super().__init__(numero, cliente)
        self._limite = limite


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


cliente1 = Cliente(
    nome="João",
    cpf="12345678900",
    endereco="Rua A"
)
print()

conta1 = Conta_Corrente(
    numero=1,
    cliente=cliente1,
    limite=500
)


print()

saldo_inicial = conta1.saldo
deposito1 = Deposito(1000)
deposito1.registrar(conta1)

saque1 = Saque(300)
saque1.registrar(conta1)


texto = (

    f"Saldo inicial: R${saldo_inicial:.2f}\n"
    f"Depositou: R${deposito1.valor:.2f}\n"
    f"Sacou: R${saque1.valor:.2f}\n"
    f"Saldo final: R${conta1.saldo:.2f}\n"

)

print(
    Panel(
        texto,
        title="Sistema Bancario",
        width=50
    )
)

print()


for transacao in conta1.historico.transacoes:
    texto = (
        f"Saldo inicial: R${saldo_inicial:.2f}\n"
        f"{transacao.tipo} de R${transacao.valor:.2f}\n"
        f"data: {transacao.data.strftime('%d/%m/%Y')}\n"
        f"às {transacao.data.strftime('%H:%M:%S')}\n"
        f"Saldo final: R${conta1.saldo:.2f}\n"

    )
    print(Panel(texto, title="Histórico"))
