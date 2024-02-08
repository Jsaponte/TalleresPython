

suma = 0


for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero


promedio = suma / 10


print("La suma de los 10 números es:", suma)
print("El promedio de los 10 números es:", promedio)

