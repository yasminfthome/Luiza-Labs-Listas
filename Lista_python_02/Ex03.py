# Método de Polimorfismo
from Ex01 import Pessoa


class PessoaJuridica(Pessoa):
    def __init__(self, cpf, nome, idade, cnpj, empregador) -> None:
        super().__init__(cpf, nome, idade)
        self.cnpj = cnpj
        self.empregador = empregador

    def trabalho(self):
        if self.empregador == True:
            return f"{self.nome} é o dono da empresa com cnpj {self.cnpj}"
        return f"{self.nome} é o funcionario com cpf {self.cpf}"


bertano = PessoaJuridica("51548484848448", "Bertano", 40, "654893217812", True)
sicrano = PessoaJuridica("51548484848448", "Sicrano", 18, "654893217812", False)
print(bertano.trabalho())
print(sicrano.trabalho())
