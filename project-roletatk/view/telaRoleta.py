import tkinter as tk
from logging import fatal
from tkinter import messagebox, Entry, Label, Button

from model.roleta import roleta


class telaRoleta:
    def jogar(self):
        self.root  = tk.Tk()
        self.root.title("Roleta Russa..")
        self.root.geometry("250x100")


        self.labelUser = Label(self.root, text="Digite um numero: ")
        self.labelUser.pack(pady=3)

        self.inputUser = Entry(self.root)
        self.inputUser.pack(pady=3)

        self.button = Button(self.root, text="validar", width=8, command=self.validarNumero)
        self.button.pack(pady=3)

        self.root.mainloop()


    def validarNumero(self):
        self.numeroUser = int(self.inputUser.get())

        objRoleta = roleta()

        validaNumero = objRoleta.jogar(self.numeroUser)
        numeroPc = objRoleta.getNumberPc()

        if validaNumero:
            messagebox.showinfo("Acertou!", "Você acertou o numero !!")
            self.root.destroy()
        else:
            messagebox.showinfo("Errou", f"Você errou o numero !!\n O numero era {numeroPc}")

