nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    try:
        cantidad = int(input("¿Cuántas canciones deseas agregar? "))
    except ValueError:
        print(" Ingresa un número válido.")
        return

    for i in range(cantidad):
        print(f"\n--- Canción {i+1} ---")
        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")

        while True:
            try:
                duracion = float(input("Duración (en minutos): "))
                break
            except ValueError:
                print(" Ingresa un número válido.")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                else:
                    print(" Debe ser entre 1 y 100.")
            except ValueError:
                print(" Ingresa un número válido.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\n Canciones agregadas correctamente.")


def ver_reportes():
    if len(nombres) == 0:
        print(" No hay canciones registradas.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    max_pop = max(popularidades)
    min_pop = min(popularidades)
    promedio_pop = sum(popularidades) / total_canciones

    idx_max = popularidades.index(max_pop)
    idx_min = popularidades.index(min_pop)

    print("\n --- REPORTES DE LA PLAYLIST ---")
    print(f"Total de canciones: {total_canciones}")
    print(f"Duración total: {duracion_total:.2f} minutos")
    print(f"Canción más popular: {nombres[idx_max]} ({artistas[idx_max]}) - {max_pop}")
    print(f"Canción menos popular: {nombres[idx_min]} ({artistas[idx_min]}) - {min_pop}")
    print(f"Popularidad promedio: {promedio_pop:.2f}")


def buscar_canciones():
    if len(nombres) == 0:
        print(" No hay canciones registradas.")
        return

    print("\n Buscar canciones:")
    print("1. Por artista")
    print("2. Por rango de popularidad")

    op = input("Elige opción: ")

    if op == "1":
        artista_buscar = input("Nombre del artista: ").lower()
        print("\n Resultados:")
        encontrado = False

        for i in range(len(nombres)):
            if artistas[i].lower() == artista_buscar:
                print(f"- {nombres[i]} ({artistas[i]}) | Popularidad: {popularidades[i]}")
                encontrado = True
        
        if not encontrado:
            print("No se encontraron canciones de ese artista.")

    elif op == "2":
        try:
            min_p = int(input("Popularidad mínima: "))
            max_p = int(input("Popularidad máxima: "))
        except ValueError:
            print(" Ingresa números válidos.")
            return

        print("\n Resultados:")
        encontrado = False

        for i in range(len(nombres)):
            if min_p <= popularidades[i] <= max_p:
                print(f"- {nombres[i]} ({artistas[i]}) | Popularidad: {popularidades[i]}")
                encontrado = True
        
        if not encontrado:
            print("No hay canciones en ese rango.")

    else:
        print(" Opción no válida.")


def playlist_recomendada():
    if len(nombres) == 0:
        print(" No hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\n Playlist Recomendada (popularidad > promedio)")
    print(f"Popularidad promedio: {promedio:.2f}\n")

    recomendado = False

    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print(f"- {nombres[i]} ({artistas[i]}) | Popularidad: {popularidades[i]}")
            recomendado = True

    if not recomendado:
        print("No hay canciones con popularidad superior al promedio.")



def menu():
    while True:
        print("\n==============================")
        print(" MENU - FESTIVAL PLAYLIST ")
        print("==============================")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_canciones()
        elif opcion == "2":
            ver_reportes()
        elif opcion == "3":
            buscar_canciones()
        elif opcion == "4":
            playlist_recomendada()
        elif opcion == "5":
            print(" Saliendo... ¡Gracias por usar el programa!")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()