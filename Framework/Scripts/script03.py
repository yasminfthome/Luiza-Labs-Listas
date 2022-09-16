# Somar todos os elementos pares da lista
# com um laço de repetição

lista = [1,2,3,4,5,6,7,8,9,10]

# blocos de instrução: indentação
# laço de repetição
soma = 0
for valor in lista:
    # Somar somente para os casos em que os
    # números são pares
    if valor % 2 == 0:
        soma = soma + valor
# Fim do for

print("Resultado:", soma)

soma = sum(
    # Separar uma lista somente dos pares
    [
        valor
        for valor in lista   
        # Filtro
        if valor % 2 == 0
    ]
)
print("Resultado por sum(): ", soma)


# blocos de instrução: indentação
# laço de repetição
soma = 0
for valor in lista:
    # Somar somente para os casos em que os
    # números são pares
    if valor % 2 == 1:
        continue # Continue para o próximo se o nº é ímpar.
    # else:
    #     soma = soma + valor
    soma = soma + valor
# Fim do for

print("Resultado invertido:", soma)

