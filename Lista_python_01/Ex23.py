notas = {}

for i in range(4):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota dele: "))

    if notas.get(nome):
        print("Ja existe o aluno ", nome)
    else:
        notas[nome] = nota
    print(notas)

chave = max(notas, key=lambda x: notas[x])

print(f"O melhor aluno foi: {chave}")
