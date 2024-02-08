
edad = int(input("Ingrese la edad: "))
genero = int(input("Ingrese el género (1 para femenino, 2 para masculino): "))

if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10
else:
    print("Opción no válida para el género. Por favor, ingrese 1 para femenino o 2 para masculino.")
    exit()

print(f"El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: {pulsaciones}")
