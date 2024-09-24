import tkinter as tk
from model.Pessoa import Pessoa
from view import TelaCadastro, TelaHome, TelaLogin


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicação")
        self.geometry("300x300")

        self.listPessoas = []

        self.objTelaCadastro = TelaCadastro
        self.objTelaHome = TelaHome
        self.objTelaLogin = TelaLogin

        self.telaCadastro = self.objTelaCadastro.Cadastro(self, self.mostrarLogin, self.listPessoas)
        self.telaLogin = self.objTelaLogin.Login(self, self.mostrarHome, self.listPessoas)
        self.telaHome = self.objTelaHome.Home(self, self.mostrarCadastro)

        self.telaCadastro.pack(fill="both", expand=True)

    def mostrarLogin(self):
        self.telaCadastro.pack_forget()
        self.telaHome.pack_forget()
        self.telaLogin.pack(fill="both", expand=True)

    def mostrarHome(self):
        self.telaCadastro.pack_forget()
        self.telaLogin.pack_forget()
        self.telaHome.pack(fill="both", expand=True)

    def mostrarCadastro(self):
        self.telaHome.pack_forget()
        self.telaLogin.pack_forget()
        self.telaCadastro.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = Main()
    app.mainloop()
