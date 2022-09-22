venda = float(input("Digite o valor da venda: "))

if venda < 1000:
    print("vendedor não ganha nenhuma comissão")

elif 1000 < venda <= 5000:
    comissao = venda * 0.1
    print(f"A comissão é: {comissao}")
elif 5000 < venda <= 10000:
    comissao = venda * 0.2
    print(f"A comissão é: {comissao}")
elif 10000 < venda <= 50000:
    comissao = venda * 0.25
    print(f"A comissão é: {comissao}")
else:
    comissao = venda * 0.3
    print(f"A comissão é: {comissao}")
