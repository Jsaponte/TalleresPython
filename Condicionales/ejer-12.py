cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
precio_unitario_original = float(input("Ingrese el precio unitario original: "))


if cantidad_articulos <= 5:
    descuento = 0
elif 5 < cantidad_articulos < 10:
    descuento = 0.05
else:
    descuento = 0.08


precio_unitario_descuento = precio_unitario_original * (1 - descuento)
valor_total_pagar = cantidad_articulos * precio_unitario_descuento


print(f"El precio unitario con descuento es: ${precio_unitario_descuento:.2f}")
print(f"El valor total a pagar es: ${valor_total_pagar:.2f}")
