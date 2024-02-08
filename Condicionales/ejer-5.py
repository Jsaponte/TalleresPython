nota1 = float(input("Ingrese la primera nota (de 0.0 a 5.0): "))
nota2 = float(input("Ingrese la segunda nota (de 0.0 a 5.0): "))
nota3 = float(input("Ingrese la tercera nota (de 0.0 a 5.0): "))


promedio = (nota1 + nota2 + nota3) / 3


if promedio >= 3.0:
    resultado = "Aprobó"
else:
    resultado = "No aprobó"

print(f"El promedio de las notas es: {promedio:.2f}")
print(f"Resultado: {resultado}")
