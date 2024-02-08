

n = int(input("Ingrese el número de términos de la serie Fibonacci que desea mostrar: "))


num1, num2 = 0, 1


suma = 0


print("Serie Fibonacci:")
for i in range(n):
    print(num1, end=" ")
    suma += num1
    num1, num2 = num2, num1 + num2


print("\nSuma de los términos de la serie Fibonacci:", suma)
