import logging

#Configuração do logging
logging.basicConfig(level=logging.ERROR, filename="Lista_03/logs_example_Ex08_ERROR.log")
logging.basicConfig(level=logging.INFO, filename="Lista_03/logs_example_Ex08_INFO.log")


try:
    file = open("file.txt", "r")
    file.write("Exemplo de texto.")
except IOError:
    logging.error("Nao foi possivel escrever no arquivo")
