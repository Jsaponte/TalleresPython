
peso = float(input("Ingrese el peso en Kg: "))
estatura = float(input("Ingrese la estatura en metros: "))

imc = peso / (estatura ** 2)

if imc < 15.5:
    estado_imc = "Infrapeso severo"
elif 15.5 <= imc < 18.5:
    estado_imc = "Infrapeso"
elif 18.5 <= imc < 25:
    estado_imc = "Peso normal"
elif 25 <= imc < 30:
    estado_imc = "Sobrepeso"
elif 30 <= imc < 35:
    estado_imc = "Obesidad Grado 1"
elif 35 <= imc < 40:
    estado_imc = "Obesidad Grado 2"
else:
    estado_imc = "Obesidad Grado 3"

if imc < 18.5:
    estado_adicional = "Desnutrido"
elif 18.5 <= imc < 25:
    estado_adicional = "Normal"
elif 25 <= imc < 30:
    estado_adicional = "Sobrepeso"
elif 30 <= imc < 35:
    estado_adicional = "Obesidad Grado 1"
elif 35 <= imc < 40:
    estado_adicional = "Obesidad Grado 2"
else:
    estado_adicional = "Obesidad Grado 3"


print(f"El Índice de Masa Corporal (IMC) es: {imc:.2f}")
print(f"Estado IMC: {estado_imc}")
print(f"Estado Adicional: {estado_adicional}")

