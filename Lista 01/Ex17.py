a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("Nao tem raízes reais")

elif a == 0:
    print("O valor de a tem que ser diferente de 0")

else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f"x1: {x1} \nx2: {x2}")
