import random


class roleta:

    def jogar(self, numeroUser):
        self.numeroPc = random.randrange(1, 2)

        if numeroUser > 6 or numeroUser < 1:
            print("Por favor Digite um numero valido!")
            return False

        if numeroUser == self.numeroPc:
            print("Você Morreu !!! ")
            return True
        else:
            print("Você errou o numero !")
            return False

    def getNumberPc(self):
        return self.numeroPc
