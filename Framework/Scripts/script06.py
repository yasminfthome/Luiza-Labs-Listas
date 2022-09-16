def comissao_vendedor(valor):
    return valor + (valor * 0.1)

def comissao_gerente(valor):
    return valor + (valor + 0.2)

def calcular_comissao(valor, tipo_empregado):
    # Forma 1
    if tipo_empregado == "gerente":
        return comissao_gerente(valor)
    #else
    return comissao_vendedor(valor)


def calcular_comissao2(valor, tipo_empregado):
    # Forma 2
    if tipo_empregado == "gerente":
        funcao_comissao = comissao_gerente
    else:
        funcao_comissao = comissao_vendedor
    return funcao_comissao(valor)


def calcular_comissao3(valor, tipo_empregado):
    # Forma 3
    motor_calculo = {
        "gerente": comissao_gerente,
        # "empregado": comissao_vendedor
    }
    funcao_comissao = motor_calculo.get(
        # Chave / cargo /tipo-empregado
        tipo_empregado,
        # Tipo de empregado for deconhecido
        comissao_vendedor
    )
    comissao = funcao_comissao(valor)
    return comissao


tipo_empregado ="gerente"
valor = 1000

comissao = calcular_comissao(valor, tipo_empregado)
print(1, comissao)

comissao = calcular_comissao2(valor, tipo_empregado)
print(2, comissao)