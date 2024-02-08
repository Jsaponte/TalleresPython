
valor_unitario = float(input("Ingrese el valor unitario del producto: "))


cantidad_productos = int(input("Ingrese la cantidad de productos comprados: "))


valor_total_sin_iva = valor_unitario * cantidad_productos


iva = 0.16 * valor_total_sin_iva


valor_total_con_iva = valor_total_sin_iva + iva


print(f"El valor total de la compra, incluyendo el 16% de IVA, es: {valor_total_con_iva}")
