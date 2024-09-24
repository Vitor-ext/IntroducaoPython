
class Imc:
    imc = 0
    status = ""

    def calcularImc(self, peso, altura):
        self.imc = peso / (altura ** 2)

    def statusImc(self):
        if self.imc < 18.5:
            self.status = "Baixo Peso"

        elif self.imc > 18.5 and self.imc < 24.99:
            self.status = "Peso Normal"

        elif self.imc > 24.99 and self.imc < 29.99:
            self.status = "Sobrepeso"
        else:
            self.status = "Obesidade"

        return self.status

