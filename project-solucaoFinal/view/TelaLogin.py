import tkinter as tk
from tkinter import messagebox


class Login(tk.Frame):
    def __init__(self, master, mostrarHome, listPessoas):
        super().__init__(master)
        self.master = master
        self.listPessoas = listPessoas
        self.mostrarHome = mostrarHome

        # Labels e Entradas
        self.label = tk.Label(self, text="Tela de Login !")
        self.label.pack(pady=5)

        self.labelEmail = tk.Label(self, text="Informe o seu email: ")
        self.labelEmail.pack(pady=5)

        self.entryEmail = tk.Entry(self)
        self.entryEmail.pack(padx=5)

        self.labelSenha = tk.Label(self, text="Informe a sua senha: ")
        self.labelSenha.pack(pady=5)

        self.entrySenha = tk.Entry(self, show="*")
        self.entrySenha.pack(padx=5)

        self.button1 = tk.Button(self, text="Login", command=self.validarLogin)
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Sair", command=self.master.quit)
        self.buttonExit.pack(pady=3)

    def validarLogin(self):
        self.email = self.entryEmail.get()
        self.senha = self.entrySenha.get()

        if not self.email or not self.senha:
            messagebox.showinfo("Erro", "Por favor preencha todos os campos!")
            return

        pessoa = self.pesquisarPessoa()

        if pessoa:
            if pessoa.senha != self.senha:
                messagebox.showinfo("Erro", "Senha Incorreta!")
            else:
                self.mostrarHome()
        else:
            messagebox.showinfo("Erro", "Email não encontrado!")

    def pesquisarPessoa(self):
        for pessoa in self.listPessoas:
            if pessoa.email == self.email:
                return pessoa
        return None
