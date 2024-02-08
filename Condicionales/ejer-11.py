
print("Tamaños disponibles:")
print("1: Pequeña - $15,000")
print("2: Mediana - $24,000")
print("3: Grande - $36,000")

tamaño_pizza = int(input("Seleccione el tamaño de la pizza (1, 2 o 3): "))

ingredientes_adicionales = int(input("Ingrese el número de ingredientes adicionales: "))

if tamaño_pizza == 1:
    precio_base = 15000
elif tamaño_pizza == 2:
    precio_base = 24000
elif tamaño_pizza == 3:
    precio_base = 36000
else:
    print("Opción no válida. Por favor, seleccione un tamaño válido.")
    exit()

precio_total = precio_base + (ingredientes_adicionales * 4000)


print(f"El precio a pagar por la pizza es: ${precio_total:.2f}")

