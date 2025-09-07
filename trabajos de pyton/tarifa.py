print("Tarifa de entrada al parque")
edad = int(input("Ingresa tu edad: "))

if edad < 12:
    tarifa = 50
elif edad <= 17:
    tarifa = 80
else:
    tarifa = 120

print(f"El costo de entrada es: ${tarifa}")