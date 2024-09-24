
class Retangulo:
    lado1 = 0
    lado2 = 0
    area = 0
    perimetro = 0

    def cadastrarRetangulo(self):
        print("*---------------------------*")
        print("*-        Retângulo        -*")
        print("*---------------------------*")

        self.lado1 = float(input("Digite o 1° lado: "))
        self.lado2 = float(input("Digite o 2° lado: "))

        print("*---------------------------*")

    def calcularArea(self):
        print("*--------------------------------*")
        print("*-        Area Retângulo        -*")
        print("*-------------------------------*")

        self.area = self.lado1 * self.lado2
        print(f"Area do retângulo: {self.area}")

        print("*-------------------------------*")


    def calcularPerimetro(self):
        print("*-------------------------------------*")
        print("*-        Perimetro Retângulo        -*")
        print("*-------------------------------------*")

        self.perimetro = self.lado1 * 2 + self.lado2 * 2
        print(f"Perimetro do retângulo: {self.perimetro}")

        print("*-------------------------------------*")

    def validarRetanguloEspecial(self):
        print("*--------------------------------------*")
        print("*-        Quadrado / Retângulo        -*")
        print("*--------------------------------------*")

        if self.lado1 == self.lado2:
            print("*--------------------------------------*")
            print("*-            É um Quadrado           -*")
            print("*--------------------------------------*")
        else:
            print("*--------------------------------------*")
            print("*-          Não é um Quadrado         -*")
            print("*--------------------------------------*")




