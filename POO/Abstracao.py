class TempoTransporte:
    def __init__(self, kilometro, velocidade) -> None:
        self.kilometro = kilometro
        self.velocidade = velocidade

    def calcula_tempo(self) -> float:
        tempo = self.kilometro / self.velocidade
        return tempo


tempo_percorrido = TempoTransporte(50, 100)
print(tempo_percorrido.calcula_tempo())
