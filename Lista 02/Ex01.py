# Método de Classe
class Pessoa:
    def __init__(self, cpf, nome, idade) -> None:
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        pass

    def maior_idade(self):
        if self.idade >= 18:
            return f"{self.nome} é maior de idade, portanto pode fumar"
        return f"{self.nome} é menor de idade, portanto não pode fumar"

# Método de Herança
class Fulano(Pessoa):
    def __init__(self, cpf, nome, idade, fumante) -> None:
        self.fumante = fumante
        super().__init__(cpf, nome, idade)

    def determinante(self):
        if self.fumante == True:
            return f"{self.nome} é fumante tem {self.idade} anos e seu documento de identificação é o cpf {self.cpf}"
        return f"{self.nome} não é fumante tem {self.idade} anos e o seu documento de identificação é o cpf {self.cpf}"


fulano = Pessoa("1234567899-87", "Fulano", 17)
fulano = Fulano("1234567899-87", "Fulano", 17, True)
print(fulano.maior_idade())
print(fulano.determinante())
