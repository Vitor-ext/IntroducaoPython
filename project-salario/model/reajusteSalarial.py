
class reajuste:

    def ajustarSalario(self, salario):

        if salario < 1500:
            print("O aumento será de 15%")
            return salario * 1.15

        elif salario <= 3000:
            print("O aumento será de 10%")
            return salario * 1.10

        else:
            print("O aumento será de 5%")
            return salario * 1.05