import logging

logging.basicConfig(level=logging.ERROR, filename="Teste/logs_example_divisao.log")

try:
    numerator = int(input("Numerador: "))
    denominator = int(input("Denominador: "))
    result = numerator / denominator
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
