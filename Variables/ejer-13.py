
tiempo_segundos = int(input("Ingrese el tiempo en segundos: "))


horas = tiempo_segundos // 3600
minutos = (tiempo_segundos % 3600) // 60


print(f"{tiempo_segundos} segundos son equivalentes a {horas} horas y {minutos} minutos.")
