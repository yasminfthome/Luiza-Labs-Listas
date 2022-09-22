valor_emprestimo = float(input("Informe o valo do emprestimo: "))
taxa = float(input("Informe o valo da taxa: "))
tempo = int(input("Informe a quantidade de meses: "))

valor_final = valor_emprestimo + (valor_emprestimo * taxa * tempo)

print(valor_final)
