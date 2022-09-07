Nota = int(input("A nota que ser um valor inteiro entre 0 e 100: "))

if Nota > 100:
    print("Nota invalida")
elif Nota > 60:
    print("Aluno aprovado, parabéns")
else:
    print("Aluno Reprovado, não foi desta vez tente de novo ao que vem")
