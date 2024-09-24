class Pessoa:
    def __init__(self, nome="", email="", senha=""):
        self.nome = nome
        self.email = email
        self.senha = senha

    def cadastrarPessoa(self, nome, email, senha):
        print("** Cadastro **")
        self.nome = nome
        self.email = email
        self.senha = senha
