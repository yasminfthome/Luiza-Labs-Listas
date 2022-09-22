# ESTE CODIGO FOI EMBASADO NO CONFORTO DO PASSAGEIRO AO UTILIZAR 3 TIPOS DE TRANSPORTE


class Transporte:
    def __init__(self, conforto) -> None:
        self.conforto = conforto

    def onibus(self):
        if self.conforto <= 30:
            return f"conforto {self.conforto}%"
        return "Por mais conforto procure outros tipos de transporte"

    def carro(self):
        if self.conforto >= 80:
            return f"conforto {self.conforto}%"
        return "temos outras opções de transporte"

    def moto(self):
        if self.conforto > 30 and self.conforto < 80:
            return f"conforto {self.conforto}%"
        return "Por mais conforto procure outros tipos de transporte"


# DADOS UTILIZADOS

usuario1 = Transporte(10)
usuario3 = Transporte(40)
usuario2 = Transporte(90)

print(usuario1.onibus())
print(usuario2.carro())
print(usuario3.moto())
