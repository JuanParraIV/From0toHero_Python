set_countries = {"Colombia", "Peru", "Venezuela", "Ecuador"}
"""
Funciones de set:

add(): Añade un elemento.

update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.

discard(): Elimina un elemento y si ya existe no lanza ningún error.

remove(): Elimina un elemento y si este no existe lanza el error “keyError”.

pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.

clear(): Elimina todo el contenido del conjunto.
"""

# Complete CRUD using Sets
size = len(set_countries)  #
print(size)

print("Colombia" in set_countries)
print("Peruu" in set_countries)

# Add element
set_countries.add("Chile")
print(set_countries)

# Update element
set_countries.update(["Argentina", "Brasil"])
print(set_countries)

# Delete element
set_countries.remove("Peru")
set_countries.discard("Peru")
print(set_countries)

# Delete Alls element
set_countries.clear()
print(set_countries)
print(len(set_countries))