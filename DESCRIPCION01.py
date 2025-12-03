import os
import pickle

TXT_FILE = "pokedex.txt"
BIN_FILE = "pokedex_stats.bin"



def crear_archivo_texto():
    """Crea el archivo de texto si no existe."""
    if not os.path.exists(TXT_FILE):
        with open(TXT_FILE, "w", encoding="utf-8") as f:
            f.write("=== MINI POKEDEX ===\n")
        print("Archivo de texto creado correctamente.")
    else:
        print("El archivo de texto ya existe.")


def guardar_pokemon_texto(nombre, tipo, region, año):
    """Guarda un nuevo Pokémon en el archivo .txt."""
    try:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")

        with open(TXT_FILE, "a", encoding="utf-8") as f:
            f.write(f"{nombre}|{tipo}|{region}|{año}\n")

    except Exception as e:
        print("Error al guardar en el archivo de texto:", e)


def leer_pokedex_texto():
    """Lee todos los registros del archivo de texto."""
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            contenido = f.readlines()

        if len(contenido) <= 1:
            print("No hay Pokémon registrados.")
        else:
            print("\n=== LISTA COMPLETA DE POKÉMON ===")
            for linea in contenido[1:]:
                nombre, tipo, region, año = linea.strip().split("|")
                print(f"- {nombre} ({tipo}) | Región: {region} | Año: {año}")

    except FileNotFoundError:
        print("ERROR: El archivo de texto no existe. Debes crearlo primero.")


def buscar_pokemon(nombre_buscar):
    """Busca un Pokémon por su nombre."""
    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            for linea in f:
                if nombre_buscar.lower() in linea.lower():
                    nombre, tipo, region, año = linea.strip().split("|")
                    print("\n=== POKÉMON ENCONTRADO ===")
                    print(f"Nombre: {nombre}")
                    print(f"Tipo: {tipo}")
                    print(f"Región: {region}")
                    print(f"Año: {año}")
                    return
        print("No se encontró el Pokémon.")

    except FileNotFoundError:
        print("ERROR: No existe el archivo de texto.")




def guardar_stats_binario(nombre, poder, rareza):
    """Guarda estadísticas numéricas de un Pokémon en .bin."""
    datos = {}

    if os.path.exists(BIN_FILE):
        try:
            with open(BIN_FILE, "rb") as f:
                datos = pickle.load(f)
        except:
            print("Error al leer archivo binario, se regenerará.")

    datos[nombre] = {"poder": poder, "rareza": rareza}

    try:
        with open(BIN_FILE, "wb") as f:
            pickle.dump(datos, f)
    except Exception as e:
        print("Error al guardar datos binarios:", e)


def leer_stats():
    """Lee y muestra las estadísticas binarias."""
    try:
        with open(BIN_FILE, "rb") as f:
            datos = pickle.load(f)

        print("\n=== ESTADÍSTICAS BINARIAS ===")
        for nombre, stats in datos.items():
            print(f"{nombre} → Poder: {stats['poder']} | Rareza: {stats['rareza']}")

    except FileNotFoundError:
        print("ERROR: No existe el archivo binario.")
    except Exception as e:
        print("Error al leer archivo binario:", e)



def menu():
    crear_archivo_texto()

    while True:
        print("\n===== MINI POKEDEX =====")
        print("1. Agregar Pokémon")
        print("2. Mostrar toda la Pokédex")
        print("3. Buscar Pokémon por nombre")
        print("4. Mostrar datos binarios (poder/rareza)")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del Pokémon: ")
                tipo = input("Tipo: ")
                region = input("Región: ")
                año = input("Año de creación: ")

               
                if not año.isdigit():
                    raise ValueError("El año debe ser un número.")

                guardar_pokemon_texto(nombre, tipo, region, año)

                poder = int(input("Nivel de poder (1-900): "))
                rareza = int(input("Rareza (1-100): "))

                guardar_stats_binario(nombre, poder, rareza)

                print("Pokémon agregado con éxito.")

            except ValueError as err:
                print("ERROR:", err)
            finally:
                print("Proceso completado.")

        elif opcion == "2":
            leer_pokedex_texto()

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            buscar_pokemon(nombre)

        elif opcion == "4":
            leer_stats()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta nuevamente.")


menu()