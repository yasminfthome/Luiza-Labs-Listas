import mathmatics
import logging

#Configuração do logging
logging.basicConfig(level=logging.ERROR, filename="Lista_03/logs_example_Ex05_ERROR.log")
logging.basicConfig(level=logging.INFO, filename="Lista_03/logs_example_Ex05_INFO.log")

try:
    resultado = math.sqrt(25)
    logging.info(resultado)
    print(f"O resultado eh {resultado}")
except ModuleNotFoundError:
    logging.error("Não existe um modulo chamado mathmatics")
except (ValueError, TypeError):
    logging.error("Variavel errada")
except KeyboardInterrupt:
    logging.error("Dados nao informados")
finally:
    print("Obrigada!")

# Exceção: ModuleNotFoundError: No module named 'mathmatics'