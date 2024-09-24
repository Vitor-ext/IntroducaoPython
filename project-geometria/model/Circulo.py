import math

from select import select


class Circulo:
    raio = 0
    diametro = 0
    pi = math.pi
    area = 0
    perimetro = 0

    def cadastrarCirculo(self):
        print("*---------------------------*")
        print("*-         Circulo         -*")
        print("*---------------------------*")

        self.raio = float(input("Informe o raio: "))

        print("*---------------------------*")

    def calcularArea(self):
        print("*---------------------------*")
        print("*-     Area Circulo        -*")
        print("*---------------------------*")

        self.area = self.pi * self.raio ** 2
        print(f"Area: {self.area}" )

        print("*---------------------------*")

    def calcularPerimetro(self):
        print("*---------------------------*")
        print("*-   Perimetro Circulo     -*")
        print("*---------------------------*")

        self.perimetro = 2 * self.pi * self.raio
        print(f"Perimetro: {self.perimetro}")

        print("*---------------------------*")

    def mostarDiamentro(self):
        self.diametro = self.raio * 2
        print(f"Diametro: {self.diametro}")
        print("*---------------------------*")