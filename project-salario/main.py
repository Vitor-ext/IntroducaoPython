from model.funcionario import funcionario
from model.reajusteSalarial import reajuste

class main:

    funcionario1 = funcionario()
    funcionario1.cadastrarFuncionario()

    reajuste = reajuste()
    novoSalario = reajuste.ajustarSalario(funcionario1.salario)
    print(novoSalario)