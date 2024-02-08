
def factorial(numero):
 
    resultado = 1
   
    for i in range(1, numero + 1):
        resultado *= i
    return resultado


try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))

    if numero < 0:
        print("Error: Por favor ingrese un número entero no negativo.")
    else:
   
        resultado_factorial = factorial(numero)
        print(f"El factorial de {numero} es: {resultado_factorial}")
except ValueError:
    print("Error: Por favor ingrese un número entero válido.")

