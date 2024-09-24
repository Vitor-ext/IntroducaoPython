import tkinter as tk
from tkinter import messagebox
from model.Pessoa import Pessoa


class Cadastro(tk.Frame):
    def __init__(self, master, mostrarLogin, listPessoas):
        super().__init__(master)
        self.master = master
        self.listPessoas = listPessoas
        self.mostrarLogin = mostrarLogin

        # Labels e Entradas
        self.label = tk.Label(self, text="Tela de Cadastro !")
        self.label.pack(pady=5)

        self.labelNome = tk.Label(self, text="Informe o seu nome: ")
        self.labelNome.pack(pady=5)

        self.entryNome = tk.Entry(self)
        self.entryNome.pack(padx=5)

        self.labelEmail = tk.Label(self, text="Informe o seu email: ")
        self.labelEmail.pack(pady=5)

        self.entryEmail = tk.Entry(self)
        self.entryEmail.pack(padx=5)

        self.labelSenha = tk.Label(self, text="Informe a sua senha: ")
        self.labelSenha.pack(pady=5)

        self.entrySenha = tk.Entry(self, show="*")
        self.entrySenha.pack(padx=5)

        self.labelConfirmeSenha = tk.Label(self, text="Confirme sua senha: ")
        self.labelConfirmeSenha.pack(pady=5)

        self.entryConfirmeSenha = tk.Entry(self, show="*")
        self.entryConfirmeSenha.pack(padx=5)

        self.button1 = tk.Button(self, text="Realizar Cadastro", command=self.validarDados)
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Sair", command=self.master.quit)
        self.buttonExit.pack(pady=3)

    def validarDados(self):
        self.nome = self.entryNome.get()
        self.email = self.entryEmail.get()
        self.senha = self.entrySenha.get()
        self.confirmeSenha = self.entryConfirmeSenha.get()

        if not all([self.nome, self.email, self.senha, self.confirmeSenha]):
            messagebox.showinfo("Erro", "Por favor preencha todos os campos!")
            return

        if self.senha != self.confirmeSenha:
            messagebox.showinfo("Erro", "As senhas devem ser iguais!")
            return

        pessoa1 = Pessoa(self.nome, self.email, self.senha)
        self.listPessoas.append(pessoa1)

        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
        self.mostrarLogin()
