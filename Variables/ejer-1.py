
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))


resultado = 0

if numero1 != 0:
    resultado = numero1

    if numero2 != 0:
        resultado *= numero2

        if numero3 != 0:
            resultado *= numero3


if resultado != 0:
    print(f"El resultado de la multiplicación es: {resultado}")

