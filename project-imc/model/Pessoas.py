

class Pessoas:
    nome = ""
    cpf = 0
    idade = 0
    peso = 0
    altura = 0


    def cadastrarPessoa(self):
        print("/***************************************/")
        print("/*         Cadastro de Pessoas         */")
        print("/***************************************/")
        self.nome = input("Qual é o seu nome: ")
        self.cpf = input("Informe o seu cpf: ")
        self.idade = int(input("Qual é a sua idade: "))
        self.peso = int(input("Qual é o seu peso: "))
        self.altura = float(input("Qual é a sua altura: "))
        print("/***************************************/")


    def mostrarInformacoes(self):
        print("/***************************************/ ")
        print("/*          Informações                */")
        print("/***************************************/")
        print(f"O nome da pessoa é {self.nome}")
        print(f"O cpf da pessoa é {self.cpf}")
        print(f"A idade da pessoa é {self.idade}")
        print(f"O peso da pessoa é {self.peso}")
        print(f"A altura da pessoa é {self.altura}")
        print("/***************************************/")

    def andar(self):
        print(f"A pessoa {self.nome} está andando...")













