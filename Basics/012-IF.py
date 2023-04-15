""" if True:
    print("True")
if False:
    print("False")

pet=input('Cual es tu mascota favorita')

if (pet == 'perro' or pet == 'conejo' or pet=='gato'):
    print(f"Tu mascota es muy común , y es un {pet}")
else :
    print(f"Tu mascota no es común , y es un {pet}") """

num=int(input('Ingrese un numero'))
""" def primo(num):
 if num < 2: #si es menor de 2 no es primo, devolverá Falso
   return False
 for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
   if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
    return False
 return True #de lo contrario devuelve Verdadero """

if (num % 2 == 0) :
    print(f"el num: {num} es par")
elif (num % 3 == 0):
    print(f"el num: {num} es impar")
else: 
    print(f"el num: {num} es primo")