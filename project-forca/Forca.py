import random


class Forca:
    # Isso está comentado !
    listNomes = ["Samantha", "Maria","Vitor", "Bianca", "Joao", "Fanti", "Godoy", "Carlos", "Arthur", "Livia", "Melissy", "Raquelyy", "Otavio", "Julia" ]

    # Selecionando um nome de forma aleatória
    nome = random.choice(listNomes)

    letrasUser = []
    venceu = False
    tentativas = 6

    while True:

        for letra in nome:

            if letra.lower() in letrasUser:
                print(letra, end=" ")

            else:
                print("_", end=" ")

        print("\nCaso saiba a palavra digite @")
        tentativa = input("Escolha uma letra: ")

        if  tentativa == "@":
            print("*********************************")
            chuteUser = input("Qual é a palavra:  ")

            if chuteUser.lower() == nome.lower():
                venceu = True
                break


        letrasUser.append(tentativa.lower())

        if tentativa.lower() not in nome.lower():
            tentativas -= 1
            print(f"Você ainda tem {tentativas} chances...")

        venceu = True

        for letra in nome:
            if letra.lower() not in letrasUser:
                venceu = False


        if tentativas == 0 or venceu:
            break

    if  venceu:
        print(f"Parabéns ! Você venceu.. O nome era: {nome}")
    else:
        print(f"Parabéns ! Você perdeu.. O nome era: {nome}")


