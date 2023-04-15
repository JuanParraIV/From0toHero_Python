from personal_info import personal_info

name=personal_info['name']
last_name = personal_info['sur_name']
age=personal_info['age']
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Nicolas"
print(quote)

quote2 = ' She said "Hello"  '
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name + " y mi edad es " + str(age) 
print('v1', template)

template = "Hola, mi nombre es {} y mi apellido es {} y mi edad es {}".format(name, last_name, age)

print('v2', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {age}"
print('v3', template)