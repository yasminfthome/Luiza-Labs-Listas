import logging

#Configuração do logging
logging.basicConfig(level=logging.ERROR, filename="Lista_03/logs_example_Ex07_ERROR.log")
logging.basicConfig(level=logging.INFO, filename="Lista_03/logs_example_Ex07_INFO.log")


try:
    file = open("file.txt", "r")
    file_lines = file.readline()
    file.close()
except FileNotFoundError:
    logging.error("Nao existe o arquivo informado")
