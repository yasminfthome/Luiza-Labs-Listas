import logging

#Configuração do logging
logging.basicConfig(level=logging.ERROR, filename="Lista_03/logs_example_Ex03_ERROR.log")
logging.basicConfig(level=logging.INFO, filename="Lista_03/logs_example_Ex03_INFO.log")

try:
    number: int = int(input("Digite um numero: "))
    logging.info(number)
    print(f"O numero eh {number}")
except (ValueError, TypeError):
    logging.error("Variavel errada")
except KeyboardInterrupt:
    logging.error("Dados nao informados")
finally:
    print("Obrigada!")