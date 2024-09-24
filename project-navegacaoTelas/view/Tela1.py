import tkinter as tk
from tkinter import messagebox

class Tela1(tk.Frame):
    def __init__(self, master, mostarTela2):
        super().__init__(master)
        self.master = master

        self.mostarTela2 = mostarTela2

        # Label
        self.label = tk.Label(self, text="Tela 1")
        self.label.pack(pady=5)

        self.label1 = tk.Label(self, text="Informe um numero")
        self.label1.pack(pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)


        self.button1 = tk.Button(self, text="Navegar Tela 2", command=self.validarNavegacao)
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Sair", command=self.master.quit)
        self.buttonExit.pack(pady=3)


    def validarNavegacao(self):

        self.numberUser = int(self.entry.get())

        if self.numberUser == 8:
            print("Navega para outra tela...")
            self.mostarTela2()
        else:
            messagebox.showinfo("Erro", "Digite o numero correto !")