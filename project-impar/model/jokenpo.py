import random


class jokenpo:

    def jogar(self):
        print("/**********************************/")
        print("/*           Jokenpô              */")
        print("/**********************************/")

        print("1 - [Pedra]")
        print("2 - [Papel]")
        print("3 - [Tesoura]")
        numeroPlayer = int(input("Escolha uma opção: "))

        if numeroPlayer < 0 or numeroPlayer > 3:
            print("Escolha uma opção valida")
            return

        numeroMachine = random.randrange(1, 3)

        print(f"O pc escolheu {numeroMachine}")

        if numeroPlayer == numeroMachine:
            print("*****************************")
            print("*******    Empate      ******")
            print("*****************************")

        elif numeroPlayer == 1 and numeroMachine == 3 or numeroPlayer == 3 and numeroMachine == 2 or numeroPlayer == 2 and numeroMachine == 1:
            print("*****************************")
            print("*******    Venceu      ******")
            print("*****************************")

        else:
            print("*****************************")
            print("*******    Perdeu      ******")
            print("*****************************")