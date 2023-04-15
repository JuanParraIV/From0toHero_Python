# The correct way to name Variables is using snake_case

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 1
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

# Concatenación de cadenas en un print
print(my_string_variable, my_int_variable)

print("Este es mi string variable:", my_string_variable)
print(f"Este es mi string variable: {my_string_variable}")

# Algunas funciones del sistema
print(len(my_string_variable))

# Variable en una sola linea
[name, sur_name, alias, age] = ["Juan", "Parra", "JotaMario", 29]

# Ahora con diccionario
personal_info = {"name": "Juan", "sur_name": "Parra", "alias": "JotaMario", "age": 29}
print(
    f" Me llamo: {personal_info['name']} {personal_info['sur_name']}. Mi edad es: {personal_info['age']}. Y mi alias es: {personal_info['alias']}"
)
print(personal_info["name"])

# Modifica la variable text por un número y luego imprímelo 👇
change_name = input("ingrese el nuevo nombre")

if change_name:
    personal_info["name"] = change_name

print(personal_info["name"])

# Modifica la variable text por un número y luego imprímelo 👇
text = "My text"
print(text)

new_text = 123

if new_text:
    try:
        text = int(new_text)
    except ValueError:
        print("El valor ingresado no es un número")

print(text)
