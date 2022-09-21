import logging
from math import sqrt

#Configuração do logging
logging.basicConfig(level="ERROR", filename="Lista_03/logs_example_ex01_ERROR.log")
logging.basicConfig(level="INFO", filename="Lista_03/logs_example_ex01_INFO.log")

try:
    numero: float = float(input("Valor a ser informado: "))
    result = sqrt(numero)
    logging.info(result)
    print(f"O resultado eh {result}")
except (ValueError, TypeError):
    logging.error("Erro nos tipos de dados que voce digitou")
except KeyboardInterrupt:
    logging.error("Dados nao informados")
finally:
    print("Obrigada!")
