# Método de Classe


class Quadrado:
    def __init__(self, comprimento) -> None:
        self.comprimento = comprimento

    def area(self):
        return self.comprimento**2

    def perimetro(self):
        return self.comprimento * 4
