numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

ascendente = sorted([numero1, numero2, numero3])

descendente = sorted([numero1, numero2, numero3], reverse=True)


print(f"Números en orden ascendente: {ascendente}")
print(f"Números en orden descendente: {descendente}")
