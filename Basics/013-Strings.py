text = "Ella sabe programar en Python"

""" print('JavaScript' in text)
print('Python' in text)

if 'JavaScript' in text:
    print('elegiste bien!')
elif 'Python' in text:
    print('elegiste bien tambien') """

# text_size = text.__len__()
text_size = len(text)
print(text_size)

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.casefold())

print(text.count("a"))
print(text.startswith("Ella"))
print(text.endswith("Rust"))
print(text.swapcase())
print(text.replace("Python", "Go"))

text_2 = "este es un titulo"
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("398".isdigit())
