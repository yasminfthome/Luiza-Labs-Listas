lista = []
lista = [1, 2, 3, 4]
# indexada
x = lista[0]

# lista 'nomeada'
# Estrutura: chave/valor
dicionario = {}
print("Dicionário vazio: ", dicionario)
dicionario = {
    # chave inteira : "valor texto"
    2: "pamela",
    3: "amanda",
    1: "ozair",
    4: "aline",
    50: "luan",
    # Repete o nº1, ela que permanece
    # Tchau ozair!
    1: "hozania",
    44: [1, 2, 3]
}
print("Dicionário chaves numéricas: ", dicionario)
print("Chave 3:", dicionario[3])
# print("Chave 5:", dicionario[5]) # Dá erro!

# Como vejo se a chave está no dicionário?
etiqueta =  5
existe_chave_5 = etiqueta in dicionario

if existe_chave_5: 
    print("Chave 5:", dicionario[5])
else:
    print("Chave 5 nao existe")
# Tentar pegar uma chave, sem precisar testar
valor_chave_5 = dicionario.get(etiqueta)
print("Valor com chave 5: ", valor_chave_5) 

# Pegadinha
dicionario = {
    5: None
}
print("Engana 1: ", dicionario.get(5))
print("Confirmando a chave? ", 5 in dicionario)

dicionario = {
    "nome": "paloma",
    "sobrenome": "santos",
    "fazLuizaCode": True
}
print(dicionario)

dicionario = {
    True: "ozair",
    1: "garcia",
    "campos": 44,
    "junior": {
        "a": [1, 2, 3],
    }
}
print("Dicionário mais robusto: ", dicionario)
print("Chave campos: ",
    dicionario.get("campos"), 
    # dicionario["campos"], 
)
dicionario["campos"] = 45
print(dicionario["campos"])