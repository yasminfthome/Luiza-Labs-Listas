Vi = float(input())
Vp = float(input())
Qt = int(input())

for i in range(Qt):
    Vi = Vi + (Vi * Vp)

    print(f"Parcela {i}: $ {Vi}")
