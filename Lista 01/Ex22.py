from __future__ import division

from ast import comprehension

lista = []
for i in range(5):
    lista.append(int(input()))

print(f"Lista: {lista} \n")
print(f"Lista Ordenada: {sorted(lista)} \n")

print("Contagem dos valores da lista:")
comprehensionValues = [print(f"{j}:{lista.count(j)}x") for j in lista]

print("Identificando se é par e um número primo na lista:")

listaPrimos = []


def primos(x):
    for i in range(1, x + 1):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div = div + 1
        if div == 2:
            listaPrimos.append(i)


primos(100)

for i in lista:
    if i % 2 == 0 and i in listaPrimos:
        print(f"{i} é par e é um numero primo")
    elif i % 2 == 0:
        print(f"{i} é par e não é um numero primo")
    elif i % 2 != 0 and i in listaPrimos:
        print(f"{i} é impar e é um numero primo")
    else:
        print(f"{i} é impar e não é um numero primo")
