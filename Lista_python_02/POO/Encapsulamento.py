# CLASSE SOMATORIO DO VALOR DAS PASSAGENS DOS PASSAGEIROS

lista = []


class Passagem:
    def __init__(self, nome) -> None:
        self.nome = nome

    def __somatorio(self) -> None:
        return sum(lista)

    def passagem_onibus(self, numero) -> None:
        return lista.append(numero)

    def passagem_barco(self, numero) -> None:
        return lista.append(numero)

    def get_valor(self):
        if self.nome == "Nicole":
            return self.__somatorio()
        return "Você não tem acesso a está informação"


# DADOS DOS PASSAGEIROS

passageiro1 = Passagem("Lucas")
passageiro1.passagem_onibus(6)

passageiro2 = Passagem("Bernado")
passageiro2.passagem_barco(5)

passageiro = Passagem("Nicole")
passageiro.passagem_barco(5)
print(passageiro.get_valor())
