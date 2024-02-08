
cantidad_llantas = int(input("Ingrese el número de llantas a comprar: "))

precio_1_5_llantas = 240000
precio_6_7_llantas = 221000
precio_mas_7_llantas = 180000

if cantidad_llantas < 6:
    valor_total = cantidad_llantas * precio_1_5_llantas
elif 6 <= cantidad_llantas <= 7:
    valor_total = cantidad_llantas * precio_6_7_llantas
else:
    valor_total = cantidad_llantas * precio_mas_7_llantas


print(f"El valor total a pagar por {cantidad_llantas} llantas es: ${valor_total:.2f}")
