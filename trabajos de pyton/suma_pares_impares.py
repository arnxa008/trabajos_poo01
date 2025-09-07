n = int(input("Introduce un número: "))

suma_pares = 0
suma_impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i

print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")