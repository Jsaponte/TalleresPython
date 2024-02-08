
numero = float(input("Ingrese un número: "))

if numero < 0:
    print(f"{numero} es un número negativo.")
elif numero > 0:
    print(f"{numero} es un número positivo.")
else:
    print("El número ingresado es cero.")
