personal_info = { 'name':'Juan', 'last_name':'Parra', 'age':29 }
print(type(personal_info['name']))

personal_info['name'] = True


print(str(personal_info['name']) + personal_info['last_name'] + str(personal_info['age']))

print(f"{personal_info['name']} {personal_info['last_name']} {personal_info['age']}")

total = personal_info['age'] + 10 # input siempre sera Tipo de dato string

print(type(personal_info['age']))

print(f"Tu edad en 10 años sera: {total}")
