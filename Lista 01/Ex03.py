# a. Operadores matemáticos
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 / 3.0)
print(13 / 3)
print(13 / 3.0)
print(13 // 3.0)
print(f"\n")

"""
13
7
30
3.3333333333333335
3.3333333333333335
4.333333333333333
4.333333333333333
4.0
"""

# b. Ordem dos operadores
print(5 + 30 * 20)
print((5 + 30) * 20)
print(((5 + 30) * 20) / 10)
print(5 + 30 * 20 / 10)
print(f"\n")
"""
605
700
70.0
65.0
"""

# c. Operadores comparação
print(2 < 3)
print(9 > 8)
print(1 == 1)
print(1 != 2)
print(1 != 1)
print(4 <= 4)
print(5 >= 6)
print(1 < 2 < 3)
print(1 < 2 < 2)
print(1 + 2 < 25 / 5)
print(f"\n")
"""
True
True
True
True
False
True
False
True
False
True
"""

# d. Mais operadores matemáticos:
print(2**4)
print(26 % 5)
print(f"\n")
"""
16
1
"""

# e. Operadores lógicos
print(not True)
print(not False)
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(True or True and False)
print((True or True) and False)
print(not True or False)
print(not (True or False))
print(not (True and False) and (True or False))
print(1 > 2 and 3 > 4)
print(1 > 2 and 3 < 4)
print(1 < 2 and 3 < 4)
print(1 + 2 and 3 + 4)
print(1 + 2 or 3 + 4)
print(True and 3 > 5)
print(False and 3 > 5)
print(f"\n")

""""
False
True
True
False
False
False
True
True
True
False
True
False
False
False
True
False
False
True
7
3
False
False
"""
