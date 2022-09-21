import logging

logging.basicConfig(level=logging.ERROR, filename="Teste/logging_users.log")

users = []

def users_validate(name):
    for user in users:
        if user["name"] == name:
            raise TypeError("Ja existe um Usuario cadastrado com esse nome")

def name_validate(name):
    if len(name) < 10:
        raise TypeError("Nome do Usuario deve conter mais de 10 caracteres")

def age_validate(age):
    if age < 18 or age > 100:
        raise TypeError("Usuario deve ser maior de 18 anos e menor de 100 anos.")

def user_add():
    try: 
        name = input("Digite o nome do Usuario: ")
        name_validate(name)
        users_validate(name)
        age = int(input("Digite a idade do Usuario: "))
        age_validate(age)
    except ValueError:
        print("Erro nos tipos de dados digitados")
        logging.error("Erro nos dados digitados")
        return
    except TypeError as error:
        print(error)
        logging.error(error)
        return
        
    users.append({"name": name, "age": age})
    
    print("\nUsuario cadastrado com sucesso!")
    
def users_list():
    print("\n")
    for user in users:
        print("{} - {} anos".format(user["name"], user["age"]))


while True:
    option = int(input("\nDigite a opção desejada:\n 1 - Cadastrar pessoas\n 2 - Listar pessoas\n 3 - Sair\n"))
    
    if option == 1:
        logging.info("Usuario digitou opção 1")
        user_add()
    elif option == 2:
        logging.info("Usuario digitou opção 2")
        users_list()
    elif option == 3:
        logging.info("Usuario digitou opção 3")
        exit()
    else:
        print("Opção invalida!")
            
