lista1 = [1, 2, 3, 4]

# Da lista1 incrementar os seus valores em 2
# E gerar uma lista2

# Forma 1 
lista2 = []
for valor in lista1:
    novo_valor = valor + 2
    lista2.append(novo_valor)

print(0, lista1)
print(1, lista2)

# Forma 2 - map
def somar_em2(valor):
    return valor + 2

objeto_mapeado = map(somar_em2, lista1)
lista2 = list(objeto_mapeado)
print(2, lista2)

# Forma 3
lista2 = [
    somar_em2(valor)
    for valor in lista2
]
print(3, lista2)