# Métodos de Herança e Polimorfismo

from Classes import Transporte


class Viagem(Transporte):
    def __init__(self, conforto) -> None:
        super().__init__(conforto)

    def onibus(self):
        if self.conforto <= 20:
            return f"conforto {self.conforto}%"
        return "Por mais conforto procure outros tipos de transporte"

    def carro(self):
        if self.conforto > 40 and self.conforto <= 60:
            return f"conforto {self.conforto}%"
        return "temos outras opções de transporte"

    def moto(self):
        if self.conforto > 20 and self.conforto <= 40:
            return f"conforto {self.conforto}%"
        return "Por mais conforto procure outros tipos de transporte"

    def aviao(self):
        if self.conforto > 60 and self.conforto <= 80:
            return f"conforto {self.conforto}%"
        return "Por mais conforto procure outros tipos de transporte"

    def navio(self):
        if self.conforto > 80 and self.conforto <= 100:
            return f"conforto {self.conforto}%"
        return "Por mais conforto procure outros tipos de transporte"


# DADOS UTILIZADOS

user1 = Viagem(20)
user2 = Viagem(40)
user3 = Viagem(60)
user4 = Viagem(80)
user5 = Viagem(100)


print(user1.onibus())
print(user2.carro())
print(user3.moto())
print(user4.aviao())
print(user5.navio())
