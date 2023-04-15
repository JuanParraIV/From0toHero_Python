"""
C reate
R ead
U pdate
D elete
  Métodos de las listas

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

"""

import random
# Create

personal_info = {'name': 'Juan', 'last_name': 'Parra', 'age': 29}

lida_info = {'name': 'Lida', 'last_name': 'Cujia', 'age': 42}

personal_list2 = [{'name': 'Pilar', 'last_name': 'Rumbo', 'age': 24}]

personal_list = []

personal_list.append(personal_info)
print(personal_list)

personal_list.insert(0, lida_info)

print(personal_list)
new_list = personal_list + personal_list2

print(new_list)

todo_list = ['todo 1', 'todo 2', 'todo 3',
             'todo 4', 'todo 5', 'todo 6', 'todo 7']

index = todo_list.index('todo 1')

print(index)

todo_list[index] = 'todo_new'
print(todo_list)

todo_list.remove('todo_new')
print(todo_list)

todo_list.insert(0, 'todo 1')
print(todo_list)

todo_list.pop()
print(todo_list)
todo_list.reverse()
print(todo_list)

number_list=[]

for i in range(10):
    number_list.append(random.randint(1, 10))
number_list.sort()
new_list.sort()

print(number_list)
