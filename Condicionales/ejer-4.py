
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))


if numero1 > numero2:
    mayor = numero1
    menor = numero2
elif numero1 < numero2:
    mayor = numero2
    menor = numero1
else:
    print("Los números son iguales.")
    exit()


print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
