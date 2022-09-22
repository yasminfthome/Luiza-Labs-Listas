# Método de Herança
from Ex01 import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade, emprego) -> None:
        self.emprego = emprego
        super().__init__(cpf, nome, idade)

    def trabalho(self):
        if self.emprego == True:
            return f"{self.nome} possui um emprego"
        return f"{self.nome} não possui um emprego"


bertano = PessoaFisica("51548484848448", "Bertano", 21, True)
print(bertano.trabalho())
