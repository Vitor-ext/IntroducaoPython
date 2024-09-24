import tkinter as tk


class Tela2(tk.Frame):
    def __init__(self, master, mostarTela1):
        super().__init__(master)
        self.master = master

        self.mostarTela1 = mostarTela1

        # Label
        self.label = tk.Label(self, text="Tela 2")
        self.label.pack(pady=5)

        self.button1 = tk.Button(self, text="Navegar Tela 1", command=self.mostarTela1)
        self.button1.pack(pady=10)

        self.buttonExit = tk.Button(self, text="Sair", command=self.master.quit)
        self.buttonExit.pack(pady=3)
