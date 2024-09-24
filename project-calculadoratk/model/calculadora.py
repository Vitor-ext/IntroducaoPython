class calculadora:
    def somarNumeros(self, numero1, numero2):
        print('Adição')
        self.soma = numero1 + numero2
        return self.soma

    def subtrairNumeros(self, numero1, numero2):
        print("Subtração")
        self.subtracao = numero1 - numero2
        return self.subtracao

    def multiplicarNumeros(self, numero1, numero2):
        print("Multiplição")
        self.mult = numero1 * numero2
        return self.mult

    def dividirnumero(self, numero1, numero2):
        print("Divisão")
        self.divisao = numero1 / numero2
        return self.divisao