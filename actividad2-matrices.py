def crear_sala(filas, columnas):
    """Crea una matriz de asientos con 'L' para libre."""
    return [["L" for _ in range(columnas)] for _ in range(filas)]


def mostrar_sala(sala):
    """Imprime la matriz de asientos en formato bonito."""
    print("\nEstado actual de la sala:")
    for fila in sala:
        print(" ".join(fila))
    print()


def reservar_asiento(sala, fila, columna):
    """Reserva un asiento si está libre."""
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print(" Ese asiento no existe.\n")
        return

    if sala[fila][columna] == "X":
        print(" El asiento ya está ocupado.\n")
    else:
        sala[fila][columna] = "X"
        print(" Asiento reservado con éxito.\n")


def liberar_asiento(sala, fila, columna):
    """Libera un asiento si está ocupado."""
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print(" Ese asiento no existe.\n")
        return

    if sala[fila][columna] == "L":
        print(" El asiento ya está libre.\n")
    else:
        sala[fila][columna] = "L"
        print(" Asiento liberado con éxito.\n")


def contar_asientos(sala):
    """Cuenta asientos libres y ocupados."""
    libres = sum(fila.count("L") for fila in sala)
    ocupados = sum(fila.count("X") for fila in sala)

    print(f"\n ESTADÍSTICAS:")
    print(f" Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")



print(" Bienvenido al sistema de asientos del cine")

while True:
    try:
        filas = int(input("Ingrese número de filas: "))
        columnas = int(input("Ingrese número de columnas: "))
        if filas > 0 and columnas > 0:
            break
        else:
            print("Las dimensiones deben ser números positivos.")
    except ValueError:
        print("Ingrese valores numéricos válidos.")

sala = crear_sala(filas, columnas)

while True:
    print("""
========= MENÚ =========
1. Mostrar sala
2. Reservar asiento
3. Liberar asiento
4. Contar asientos
5. Salir
========================
""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_sala(sala)

    elif opcion == "2":
        try:
            f = int(input("Fila del asiento: ")) - 1
            c = int(input("Columna del asiento: ")) - 1
            reservar_asiento(sala, f, c)
        except ValueError:
            print(" Ingrese valores numéricos válidos.\n")

    elif opcion == "3":
        try:
            f = int(input("Fila del asiento: ")) - 1
            c = int(input("Columna del asiento: ")) - 1
            liberar_asiento(sala, f, c)
        except ValueError:
            print(" Ingrese valores numéricos válidos.\n")

    elif opcion == "4":
        contar_asientos(sala)

    elif opcion == "5":
        print(" Saliendo del sistema. ¡Gracias por usar el programa!")
        break

    else:
        print(" Opción inválida. Intente de nuevo.\n")