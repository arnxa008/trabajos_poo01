numero = input("Introduce un número entero: ")

numero_invertido = ''
for digito in reversed(numero):
    numero_invertido += digito

print(f"Número invertido: {numero_invertido}")