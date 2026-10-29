from rich import print
from time import sleep


class Livro:
    def __init__(self, titulo, paginas, autor, sumário):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1
        self.autor = autor
        self.sumário = sumário

        print()
        print(
            f"[italic]estou lendo o livro [red]{self.titulo}[/], que tem [yellow2]{self.total_paginas} páginas[/] e no momento estou na[blue] página {self.pagina_atual}[/] que tem a dedicatóra da autor [red]{self.autor}[/][/]")
        print()

    def avancar_paginas(self, quantidade=1):
        cont = 0
        for pag in range(0, quantidade, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(
                    f"pág{self.pagina_atual}[yellow2]:arrow_forward:[/]", end=" ")
                sleep(0.3)
                cont += 1
                print()
        print(
            f"eu avancei [green]{cont} pág e estou agora na pág {self.pagina_atual}[/]\n")
        if self.fim_do_livro():
            print(f"[blue]acabei de ler o livro[/] [red]{self.titulo}[/]")

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False


l1 = Livro("diário de um vampiro", 240, "L.J.Smith", [
    "[yellow2]capitulo 1 = [/] A Chegada e o Diário",
    "[yellow2]capitulo 2 = [/] O Plano de Sedução",
    "[yellow2]capitulo 3 = [/] Revelações do Passado",
    "..."

])

sleep(3)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
# l1.avancar_paginas(209)


print()
sleep(1)
print()

print(f"[red]sumário do livro:[/]\n")
for capitulo in l1.sumário:
    print(capitulo)
