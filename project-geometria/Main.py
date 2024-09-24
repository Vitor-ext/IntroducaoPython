import math
from logging import fatal
from math import trunc

from model.Circulo import Circulo
from model.Retangulo import Retangulo
from model.Triangulo import Triangulo


class Main:
    print("*---------------------------*")
    print("*-        Geometria        -*")
    print("*---------------------------*")

    exit = False

    while not exit:
        print("*----------------------*")
        print("1 - Triângulo")
        print("2 - Circulo" )
        print("3 - Retângulo")
        print("4 - Sair")
        print("*----------------------*")

        opcaoUser = int(input("Escolha uma opção: "))

        if opcaoUser == 1:
            print("Escolheu 1")

            exitTriangulo = False

            while not exitTriangulo:
                print("*----------------------*")
                print("1 - Cadastrar Triângulo")
                print("2 - Calcular Area      ")
                print("3 - Validar Triângulo Retângulo")
                print("4 - Sair")
                print("*----------------------*")

                option = int(input("Escolha uma opção: "))

                if option == 1:
                    triangulo1 = Triangulo()
                    validaTriangulo = False

                    while not validaTriangulo:
                        triangulo1.cadastrarTriangulo()
                        validaTriangulo = triangulo1.validarTriangulo()

                elif option == 2:
                    triangulo1.calcularArea()

                elif option == 3:
                    validaRetangulo = triangulo1.calcularTrianguloRetangulo()

                    if validaRetangulo:
                        optionTriangulo = int(input("Deseja validar se é 3-4-5 : [1- SIM 2- NÃO] "))

                        if optionTriangulo == 1:
                            triangulo1.definirTrianguloPremium()

                elif option == 4:
                    validaTriangulo = True
                else:
                    print("Escolha uma opção válida...")



        elif opcaoUser == 2:
            print("Escolheu 2")

            exitCirculo = False

            while not exitCirculo:
                print("*----------------------*")
                print("1 - Cadastrar Circulo")
                print("2 - Calcular Area      ")
                print("3 - Calcular Perimetro")
                print("4 - Mostrar Diametro")
                print("5 - Sair")
                print("*----------------------*")

                option = int(input("Escolha uma opção: "))

                match option:
                    case 1:
                        print("Escolheu 1")
                        circulo1 = Circulo()
                        circulo1.cadastrarCirculo()
                    case 2:
                        print("Escolheu 2")
                        circulo1.calcularArea()
                    case 3:
                        print("Escolheu 3")
                        circulo1.calcularPerimetro()
                    case 4:
                        print("Escolheu 4")
                        circulo1.mostarDiamentro()
                    case 5:
                        print("Escolheu 5")
                        exitCirculo = True
                    case _:
                        print("Escolha uma opção valida !")


        elif opcaoUser == 3:
            print("Escolheu 3")

            exitRetangulo = False

            while not exitRetangulo:
                print("*----------------------*")
                print("1 - Cadastrar Retangulo")
                print("2 - Calcular Area      ")
                print("3 - Calcular Perimetro")
                print("4 - Validar Retangulo Especial")
                print("5 - Sair")
                print("*----------------------*")

                option = int(input("Escolha uma opção: "))

                match option:
                    case 1:
                        print("Escolheu 1")
                        retangulo1 = Retangulo()
                        retangulo1.cadastrarRetangulo()
                    case 2:
                        print("Escolheu 2")
                        retangulo1.calcularArea()
                    case 3:
                        print("Escolheu 3")
                        retangulo1.calcularPerimetro()
                    case 4:
                        print("Escolheu 4")
                        retangulo1.validarRetanguloEspecial()
                    case 5:
                        print("Escolheu 5")
                        exitRetangulo = True
                    case _:
                        print("Escolha uma opção valida !")


        elif opcaoUser == 4:
            print("Escolheu 4")
            exit = True

        else:
            print("Digite uma opção válida...")

