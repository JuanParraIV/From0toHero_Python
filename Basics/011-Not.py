print(not True)
print(not False)

# AND
print("NOT AND")
print("NOT TRUE and TRUE =>", not (True and True))
print("NOT TRUE and False =>", not (True and False))
print("NOT False and True =>", not (False and True))
print("NOT False and False =>", not (False and False))

stock = input('Ingrese numero de stock => ')
stock=int(stock)

#Not example
if (not (stock >= 100 and stock <=1000)):
    print('No esta en el rango')
else :
    print('Si esta en el rango')