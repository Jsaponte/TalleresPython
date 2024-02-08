
filas = int(input("Ingrese el número de filas del triángulo: "))


for i in range(1, filas + 1):

    for j in range(filas - i):
        print(" ", end="")

    for k in range(2 * i - 1):
        print("*", end="")
    print() 
