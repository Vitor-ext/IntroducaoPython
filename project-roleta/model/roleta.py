import random


class roleta:
    def jogar(self):

        while True:
            numeroUser = int(input("Informe um numero:  [1 - 6]"))

            numeroPc = random.randrange(1, 6)

            if numeroUser > 6 or numeroUser < 1:
                print("Por favor Digite um numero valido!")


            if numeroUser == numeroPc:
                print("Você Morreu !!! ")
                break
            else:
                print("Você errou o numero !")
