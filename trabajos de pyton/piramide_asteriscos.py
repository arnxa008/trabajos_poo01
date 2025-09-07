altura = int(input("Introduce la altura de la pirámide: "))

for i in range(1, altura + 1):
    espacios = ' ' * (altura - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacios + asteriscos)