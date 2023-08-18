# Casting
x = float(9)  # 9.0
x = int(6.5)  # 6
x = int(float('2.5'))  # 2
print(x)

# Operações Aritméticas

print(4 + 4)  # Soma
print(3 - 4)  # Subtração
print(4 * 2)  # Multiplicação
print(4 / 3)  # Divisão
print(4 ** 2)  # Potência
print(10 % 3)  # Módulo

print(10/4)  # Resultado é um número float
print(10//4)  # Resultado apenas a parte inteira

# incremento e decremento: em python n existe pre-in(de)cremento
x = 1
x += 1  # Incremento
print("X: ", x)
x -= 1  # Decremento
print("X: ", x)

# Operadores logicos
''' para x = 4
and 	ex:   x < 2 and  x == 4	     -> false
or	    ex:   x < 5 or x < 4	     -> true
not	    ex:   not(x < 2 and x == 4)  -> true
'''


# Comparando valores
print(isinstance(1, float))
print(isinstance("Silva", str))
print("Oi" == "oi")
x = 3
print(x > 4)
print(x <= 4)
print(x != 4)
