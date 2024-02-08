
suma_numeros = 0


for i in range(5):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma_numeros += numero


promedio = suma_numeros // 5


print(f"El promedio de los 5 números es: {promedio}")
