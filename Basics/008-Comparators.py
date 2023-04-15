# Operadores Relacionales
# Un operador relacional se emplea para comparar y establecer la relación entre ellos. Devuelve un valor booleano (true o false) basado en la condición.
#
# OPERADOR	DESCRIPCIÓN	USO
# >	Devuelve True si el operador de la izquierda es mayor que el operador de la derecha	12 > 3 devuelve True
# <	Devuelve True si el operador de la derecha es mayor que el operador de la izquierda	12 < 3 devuelve False
# ==	Devuelve True si ambos operandos son iguales	12 == 3 devuelve False
# >=	Devuelve True si el operador de la izquierda es mayor o igual que el operador de la derecha	12 >= 3 devuelve True
# <=	Devuelve True si el operador de la derecha es mayor o igual que el operador de la izquierda	12 <= 3 devuelve False
# !=	Devuelve True si ambos operandos no son iguales
# >
print(7 > 3)  # True

num = 100


# ==
if num == 3:  # Si es true imprime
    print(f"num: {num} es 3")

# >
elif num > 3:  # Si no imprime
    print(f" num: {num} es mayor que 3")
# <
elif num < 3:  # Si no imprime
    print(f"num: {num} es menor que 3")

# >=

# <=

# !=
# Operadores Bit a Bit
# &	Realiza bit a bit la operación AND en los operandos	a & b = 2 (Binario: 10 & 11 = 10)
# |	Realiza bit a bit la operación OR en los operandos	a | b = 3 (Binario: 10 | 11 = 11)
# ^	Realiza bit a bit la operación XOR en los operandos	a ^ b = 1 (Binario: 10 ^ 11 = 01)
# ~	Realiza bit a bit la operación NOT bit a bit. Invierte cada bit en el operando	~a = -3 (Binario: ~(00000010) = (11111101))
# >>	Realiza un desplazamiento a la derecha bit a bit. Desplaza los bits del operador de la izquierda a la derecha tantos bits como indica el operador de la derecha	a >> b = 0 (Binario: 00000010 >> 00000011 = 0)
# <<	Realiza un desplazamiento a la izquierda bit a bit. Desplaza los bits del operando de la izquierda a la izquierda tantos bits como especifique el operador de la derecha	a << b = 16 (Binario: 00000010 << 00000011 = 00001000)
