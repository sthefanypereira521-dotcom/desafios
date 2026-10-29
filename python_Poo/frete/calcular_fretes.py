from abc import ABC, abstractmethod


class Transporte(ABC):

    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"


class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return "distancia minima de 50km..."
        else:
            self.frete = self.distancia * Caminhao.fator
            return f"R${self.frete:.2f}"


class Carro(Transporte):
    fator = 3.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.distancia < 80:
            self.frete = 0
            return "distancia minima de 80km..."
        else:
            self.frete = self.distancia * Carro.fator
            return f"R${self.frete:.2f}"


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
         if self.distancia > 10:
                    self.frete = 0
                    return "distancia maxima de 10km..."
         else:
                    self.frete = self.distancia * Drone.fator
                    return f"R${self.frete:.2f}"
        
