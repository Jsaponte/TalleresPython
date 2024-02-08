
try:
    nombre = input ("ingrese su nombre")
    edad = int(input("ingrese su edad"))

    if 0 < edad < 18:
        print (f"{nombre}, eres menor de edad")
    elif 18 <= edad <= 100:
        print (f"{nombre}, eres mayor de edad")
    else:
        print("ERROR: la edad ingresada no es valida")

except ValueError:
    print("ERROR: Ingrese una edad valida")