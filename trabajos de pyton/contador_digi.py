numero = input("Introduce un número entero: ")

contador = 0
for digito in numero:
    if digito.isdigit():
        contador += 1

print(f"El número tiene {contador} dígito(s).")