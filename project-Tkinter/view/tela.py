import tkinter as tk
from tkinter import messagebox, Label, Entry, Button
from model.imc import Imc

class telaImc:
    def __init__(self):
        # Criar um Frame
        self. root = tk.Tk()

        # Definir o titulo
        self.root.title("Calculadora IMC")

        # Definir as medidas do frame
        self.root.geometry("300x200")

        # Definir os rotulos

        # Label para Peso
        self.labelPeso = Label(self.root, text="Informe o seu peso: ")
        self.labelPeso.pack(pady=7)

        # Input para Peso
        self.inputPeso = Entry(self.root)
        self.inputPeso.pack(pady=7)

        # Label para Altura
        self.labelAltura = Label(self.root, text="Informe a sua altura: ")
        self.labelAltura.pack(pady=7)

        # Input para Altura
        self.inputAltura = Entry(self.root)
        self.inputAltura.pack(pady=7)

        # Button para calcular Imc
        self.buttonImc = Button(self.root, text="Calcular IMC", command=self.onclick_button )
        self.buttonImc.pack(pady=20)

        # Habilitar o frame para o user
        self.root.mainloop()


    def onclick_button(self):

        peso = float(self.inputPeso.get())
        altura = float(self.inputAltura.get())

        objImc = Imc()

        imc = objImc.calcularImc(peso, altura)

        classificacao = objImc.classificarImc(imc)

        print(imc, classificacao)

        self.mostrarResultados(imc, classificacao)

    def mostrarResultados(self, imc, classificacao):
        messagebox.showinfo("Resultado do Imc", f"O seu IMC é {imc:.2f}" f"\n Classificação: {classificacao} ")







