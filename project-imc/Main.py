from model.Imc import Imc
from model.Pessoas import Pessoas

class Main:
    print("Calculadora de IMC...")

    # instânciando objeto pessoa ...
    pessoa1 = Pessoas()
    pessoa1.cadastrarPessoa()
    pessoa1.mostrarInformacoes()

    # instânciando objeto imc ...
    imc = Imc()
    imc.calcularImc(pessoa1.peso, pessoa1.altura)
    statusImc = imc.statusImc()

    print(f"Olá {pessoa1.nome} o seu IMC é {imc.imc} e o status é {statusImc}")