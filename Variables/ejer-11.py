
numero = float(input("Ingrese un número para calcular su raíz cuadrada: "))


aproximacion = numero / 2


for _ in range(10):  
    aproximacion = 0.5 * (aproximacion + numero / aproximacion)


print(f"La raíz cuadrada de {numero} es aproximadamente: {aproximacion}")
