personal_info = {
    "name": "Juan",
    "last_name": "Parra",
    "age": 29,
    "langs": ["python", "javascript"],
}
users = [
    {
        "firstName": "Juan",
        "lastName": "Parra",
        "buyerAddress": "avenida por alli",
        "langs": ["python", "javascript"],
        "userName": "juanp2",
        "rol": "user",
    },
    {
        "firstName": "Daniela",
        "lastName": "Gomez",
        "buyerAddress": "avenida por alli ",
        "langs": ["python", "javascript"],
        "userName": "DanielaUser",
        "rol": "user",
    },
]
# Correct way to make a for loop counter 1-10
for i in range(1, 11):
    print(i)

# Correct way to make a for loop counter 1-10
for i in range(1, 11):
    print(i)
    if i == 5:
        break

# list 1-10

my_list = []
for i in range(1, 11):
    my_list.append(i)

print(my_list)

for i in my_list:
    if i == 5:
        my_list[i] = 99
print(my_list)


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in my_tuple:
    print(i)

# best way to iterate dictionary personal_info , output key, value
for key, value in personal_info.items():
    print(f"{key}:{value}")

# best way to iterate dictionary users , output key, value
for user in users:
    print(user)
    for key, value in user.items():
        print(f"{key}:{value}")