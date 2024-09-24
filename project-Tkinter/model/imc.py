
class Imc:

    def calcularImc(self, peso, altura):
        print("Calculando Imc...")

        if peso <= 0 or altura <=0:
            raise ValueError("Por favor preencha os campos corretamente !")

        return peso / altura ** 2


    def classificarImc(self, imc):
        print("Classificando o Imc...")

        if imc < 18.5:
            return "Abaixo do peso"

        elif  18.5 <= imc < 24.9:
            return "Peso normal"

        elif 24.9 <= imc < 29.9:
            return "Sobrepeso"

        else:
            return "Obesidade"









