# Dictionary
personal_info = {
    "name": "Juan",
    "last_name": "Parra",
    "age": 29,
    "langs": ["python", "javascript"],
}

print(personal_info)
print(len(personal_info))

# Access to the values of the dictionary
print(personal_info["name"])
print(personal_info["last_name"])
print(personal_info["age"])

# Change the value of the dictionary
personal_info["age"] = 30

# better way to update info from a dict, because if you dont have response, you can handle the error
personal_info.update({"birth": "18/05/1993"})

print(personal_info)

# Add a new value to the dictionary
personal_info["city"] = "Bogota"
personal_info["langs"].append("typescript")

# better way to add info from a dict, because if you dont have response, you can handle the error
personal_info.setdefault("birth", "01/01/1993")
print(personal_info)

# better way to get info from a dict, because if you dont have response, you can handle the error
print(personal_info.get("name"))
print(personal_info.get("birth"))


print("name" in personal_info)

# del a value to the dictionary
del personal_info["city"]
print(personal_info)

# better way to del info from a dict, because if you dont have response, you can handle the error
personal_info.pop("langs")

print(f"Items", personal_info.items())
print(f"keys", personal_info.keys())
print(f"values", personal_info.values())
