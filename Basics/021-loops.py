matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print(matriz[0][0], matriz[0][1], matriz[0][2])
print(matriz[1][0], matriz[1][1], matriz[1][2])
print(matriz[2][0], matriz[2][1], matriz[2][2])

for i in matriz:
    print(i)
    for j in i:
        print(j)