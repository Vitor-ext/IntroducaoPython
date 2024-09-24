
# Criando a class Triângulo
class Triangulo:
    # Criando as variaveis do triângulo
    ladoA = 0
    ladoB = 0
    ladoC = 0

    # Variaveis para area do triângulo
    base = 0
    altura = 0
    area = 0


    # Criando Metodo
    def cadastrarTriangulo(self):
        print("*---------------------------*")
        print("*-        Triângulo        -*")
        print("*---------------------------*")

        self.ladoA = float(input("Digite o 1° lado do triângulo"))
        self.ladoB = float(input("Digite o 2° lado do triângulo"))
        self.ladoC = float(input("Digite o 3° lado do triângulo"))

        print("*---------------------------*")


    def validarTriangulo(self):
        print("*---------------------------*")
        print("*-        Validando        -*")
        print("*---------------------------*")

        if self.ladoA + self.ladoB < self.ladoC or self.ladoA + self.ladoC < self.ladoB or self.ladoB + self.ladoC < self.ladoA:
            print("*-   Não é um triângulo válido  -*")
            return False

        else:
            print("*-  Triângulo válido  -*")
            return True


    def calcularArea(self):
        print("*---------------------------*")
        print("*-          Area           -*")
        print("*---------------------------*")

        self.base = float(input("Informe a base: "))
        self.altura = float(input("Informe a altura: "))

        self.area = (self.base * self.altura) / 2
        print(f"A area é {self.area} m²")


    def calcularTrianguloRetangulo(self):
        print("*---------------------------*")
        print("*-        Pitagoras        -*")
        print("*---------------------------*")

        segmento = [self.ladoA, self.ladoB, self.ladoC]

        lA, lB, lC = sorted(segmento)

        if lA**2 + lB**2 == lC**2:
            print("*-   Triângulo Retângulo  -*")
            return True

        else:
            print("*-   Triângulo Comum  -*")
            return False


    def   definirTrianguloPremium(self):
        print("*---------------------------*")
        print("*-     Triângulo 3-4-5     -*")
        print("*---------------------------*")

        segmento = [self.ladoA, self.ladoB, self.ladoC]

        lA, lB, lC = sorted(segmento)

        if lA % 3 == 0 and lB % 4 == 0 and lC % 5 == 0:
            print("*-    Triângulo 3-4-5   -*")
        else:
            print("*-    Triângulo comum   -*")









