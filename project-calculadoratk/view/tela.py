import tkinter as tk
from tkinter import messagebox, mainloop, Label, Entry, Button

from model.calculadora import calculadora


class tela:
    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Calculadora")

        self.root.geometry("250x220")

        self.frame_central = tk.Frame(self.root)
        self.frame_central.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.frame_lateral = tk.Frame(self.root)
        self.frame_lateral.pack(side="right", fill="y", padx=15, pady=15)

        self.labelNumero1 = Label(self.frame_central, text="Informe um número: ")
        self.labelNumero1.pack(pady=7)
        self.inputNumero1 = Entry(self.frame_central)
        self.inputNumero1.pack(pady=7)

        self.labelNumero2 = Label(self.frame_central, text="Informe um número: ")
        self.labelNumero2.pack(pady=7)
        self.inputNumero2 = Entry(self.frame_central)
        self.inputNumero2.pack(pady=7)


        self.labelResultado = Label(self.frame_central, text="Calculando...")
        self.labelResultado.pack(padx=5, pady=10)

        self.buttonSoma = Button(self.frame_lateral, text="+", command=self.somabutton, width=5)
        self.buttonSoma.pack(pady=5)

        self.buttonSub = Button(self.frame_lateral, text="-", command=self.subtraibutton, width=5)
        self.buttonSub.pack(pady=5)

        self.buttonMult = Button(self.frame_lateral, text="x", command=self.multbutton, width=5)
        self.buttonMult.pack(pady=5)

        self.buttonDivisao = Button(self.frame_lateral, text="/", command=self.dividbutton, width=5)
        self.buttonDivisao.pack(pady=5)

        self.root.mainloop()

    def somabutton(self):
        numero1 = float(self.inputNumero1.get())
        numero2 = float(self.inputNumero2.get())

        somar = calculadora()

        soma = somar.somarNumeros(numero1, numero2)

        self.labelResultado.config(text=f"{soma}")
        self.labelResultado.pack(pady=7)


    def subtraibutton(self):
        numero1 = float(self.inputNumero1.get())
        numero2 = float(self.inputNumero2.get())

        subtrair = calculadora()

        subtracao = subtrair.subtrairNumeros(numero1, numero2)
        self.labelResultado.config(text=f"{subtracao}")
        self.labelResultado.pack(pady=7)

    def multbutton(self):
        numero1 = float(self.inputNumero1.get())
        numero2 = float(self.inputNumero2.get())

        multiplicar = calculadora()

        mult = multiplicar.multiplicarNumeros(numero1, numero2)
        self.labelResultado.config(text=f"{mult}")
        self.labelResultado.pack(pady=7)

    def dividbutton(self):
        numero1 = float(self.inputNumero1.get())
        numero2 = float(self.inputNumero2.get())

        dividir = calculadora()

        divisao = dividir.dividirnumero(numero1, numero2)
        self.labelResultado.config(text=f"{divisao}")
        self.labelResultado.pack(pady=7)
