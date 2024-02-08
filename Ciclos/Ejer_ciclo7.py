
filas = int(input("Ingrese el número de filas del triángulo: "))


for i in range(1, filas + 1):

    print(" ".join(str(j) for j in range(1, i + 1)))