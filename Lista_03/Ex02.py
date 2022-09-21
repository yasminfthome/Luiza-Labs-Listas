import logging

#Configuração do logging
logging.basicConfig(level=logging.ERROR, filename="Lista_03/logs_example_Ex02_ERROR.log")
logging.basicConfig(level=logging.INFO, filename="Lista_03/logs_example_Ex02_INFO.log")

def divisao(numerador: float,denominador: float):
    resultado = numerador/denominador
    return resultado

try:
    numerador:float = float(input("Digite o numerador: "))
    denominador:float = float(input("Digite o denominador: "))
    result = divisao(numerador=numerador, denominador=denominador)
    logging.info(result)
    print(f"O resultado eh {result}")
except ZeroDivisionError:
    logging.error("Nao eh possivel dividir um numero por zero")
except (ValueError, TypeError):
    logging.error("Erro nos tipos de dados que voce digitou")
except KeyboardInterrupt:
    logging.error("Dados nao informados")
finally:
    print("Obrigada!")