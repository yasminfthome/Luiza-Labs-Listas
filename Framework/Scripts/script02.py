# Somar todos os elementos da lista
# com um laço de repetição

lista = [1,2,3,4,5,6,7,8,9,10]

# blocos de instrução: indentação
# laço de repetição
soma = 0
for valor in lista:
    # Início do bloco/conjunto de instruções
    # a serem executadas pelo laço repetição
    soma = soma + valor
# Fim do for

print("Resultado:", soma)

soma = sum(lista)
print("Resultado por sum(): ", soma)
