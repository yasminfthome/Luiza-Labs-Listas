class Professor:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def __dados_privados(self):
        return f"O salario de {self.nome} é {self.salario} R$"

    def confirmacao(self):
        if self.nome == "Nicole":
            return self.__dados_privados()
        return "Você não tem acesso a está informação"


usuario1 = Professor("Nicole", 22, 800)
user1 = usuario1.confirmacao()
print(user1)
