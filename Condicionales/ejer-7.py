def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        print("\nMenú de Opciones:")
        print("1. Convertir de Celsius a Fahrenheit")
        print("2. Convertir de Fahrenheit a Celsius")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            print(f"{celsius} grados Celsius son {celsius_a_fahrenheit(celsius):.2f} grados Fahrenheit.")
        elif opcion == "2":
            fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
            print(f"{fahrenheit} grados Fahrenheit son {fahrenheit_a_celsius(fahrenheit):.2f} grados Celsius.")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

if __name__ == "__main__":
    main()
