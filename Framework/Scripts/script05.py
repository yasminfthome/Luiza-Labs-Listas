def ler_numeros():
    lista = [1, 2, 3, 4, 5, 6, 7]
    return lista


def somar_lista(lista):
    soma = sum(lista)
    return soma

def mostrar_resultado(soma):
    print("Resultado: ", soma)



## ==================================
## Corpo principal do script

###
# Ler números para uma lista 
lista = ler_numeros()
# Somar
soma = somar_lista(lista)
# Apresentar o resultado
mostrar_resultado(soma)

