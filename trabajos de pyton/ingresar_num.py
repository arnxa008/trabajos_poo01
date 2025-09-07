suma_positivos = 0
suma_negativos = 0
contador_ceros = 0

for i in range(5):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num > 0:
        suma_positivos += num
    elif num < 0:
        suma_negativos += num
    else:
        print("Se ingresó un cero.")
        contador_ceros += 1


print(f"\nSuma de números positivos: {suma_positivos}")
print(f"Suma de números negativos: {suma_negativos}")
print(f"Cantidad de ceros ingresados: {contador_ceros}")