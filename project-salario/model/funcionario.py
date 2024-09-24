
class funcionario:

    nome = ""
    idade = 0
    cpf = 0
    cargo = ""
    salario = 0

    def cadastrarFuncionario(self):
        print("***************************")
        print("*   Cadastro Funcionario  *")
        print("***************************")
        self.nome = input("Informe o seu nome: ")
        self.idade = int(input("Informe a sua idade: "))
        self.cpf = int(input("Informe o seu CPF: "))
        self.cargo = input("Informe o seu Cargo: ")
        self.salario = float(input("Informe o seu salario: "))
        print("***************************")