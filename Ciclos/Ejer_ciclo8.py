
filas = int(input("Ingrese el número de filas de la pirámide: "))


for i in range(1, filas + 1):
  
    print(" " * (filas - i), end="")

    for j in range(1, i * 2):
        print(j, end="")
    print()  
