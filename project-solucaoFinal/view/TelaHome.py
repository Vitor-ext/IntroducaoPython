import tkinter as tk


class Home(tk.Frame):
    def __init__(self, master, mostrarCadastro):
        super().__init__(master)
        self.master = master

        self.mostarCadastro = mostrarCadastro

        # Label
        self.label = tk.Label(self, text="Tela Home!")
        self.label.pack(pady=5)

        self.label= tk.Label(self, text="Parabéns você concluiu... ")
        self.label.pack(pady=5)

        self.button1 = tk.Button(self, text="Logout", command=self.mostarCadastro)
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Sair", command=self.master.quit)
        self.buttonExit.pack(pady=3)

