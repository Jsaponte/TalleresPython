import math

def calcular_area_cuadrado(lado):
    return lado ** 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_trapecio(base_mayor, base_menor, altura):
    return ((base_mayor + base_menor) / 2) * altura

def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Calcular área de cuadrado")
        print("2. Calcular área de rectángulo")
        print("3. Calcular área de triángulo")
        print("4. Calcular área de círculo")
        print("5. Calcular área de rombo")
        print("6. Calcular área de trapecio")
        print("7. Salir")

        opcion = input("Seleccione una opción (1-7): ")

        if opcion == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            print(f"El área del cuadrado es: {calcular_area_cuadrado(lado)}")
        elif opcion == "2":
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            print(f"El área del rectángulo es: {calcular_area_rectangulo(base, altura)}")
        elif opcion == "3":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            print(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")
        elif opcion == "4":
            radio = float(input("Ingrese el radio del círculo: "))
            print(f"El área del círculo es: {calcular_area_circulo(radio)}")
        elif opcion == "5":
            diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
            diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
            print(f"El área del rombo es: {calcular_area_rombo(diagonal_mayor, diagonal_menor)}")
        elif opcion == "6":
            base_mayor = float(input("Ingrese la base mayor del trapecio: "))
            base_menor = float(input("Ingrese la base menor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            print(f"El área del trapecio es: {calcular_area_trapecio(base_mayor, base_menor, altura)}")
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
