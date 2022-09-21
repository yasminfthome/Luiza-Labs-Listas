try:
    number_1 = float(input("Insira um numero: "))
    number_2 = float(input("Insira outro numero: "))
    
    print("Resultado: {.:2f}".format(resultado))


except ValueError:
    print("Isso nao eh um numero.")
except ZeroDivisionError:
    print("Divisao por 0 indeterminada.")
except:
    print("Algo deu errado")
    
# Algo deu errado, pois não está dividindo e não tem a variável resultado.
