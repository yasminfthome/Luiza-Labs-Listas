import logging

#Configuração do logging
logging.basicConfig(level=logging.ERROR, filename="Lista_03/logs_example_Ex04_ERROR.log")
logging.basicConfig(level=logging.INFO, filename="Lista_03/logs_example_Ex04_INFO.log")

try:
    number: int = int(input("Digite um numero: "))
    logging.info(number)
    print(f"O numero eh {n}")
except NameError:
    logging.error("Nome da variavel nao condizente")
except (ValueError, TypeError):
    logging.error("Variavel errada")
except KeyboardInterrupt:
    logging.error("Dados nao informados")
finally:
    print("Obrigada!")
