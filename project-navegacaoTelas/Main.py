import tkinter as tk

from view import Tela1
from view import Tela2

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Navegação Telas")
        self.geometry("300x300")

        self.objTela1 = Tela1
        self.objTela2 = Tela2

        self.tela1 = self.objTela1.Tela1(self, self.mostrarTela2)
        self.tela2 = self.objTela2.Tela2(self, self.mostrarTela1)

        self.tela1.pack(fill="both", expand=True)

    def mostrarTela1(self):
        self.tela2.pack_forget()
        self.tela1.pack(fill="both", expand=True)

    def mostrarTela2(self):
        self.tela1.pack_forget()
        self.tela2.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = Main()
    app.mainloop()