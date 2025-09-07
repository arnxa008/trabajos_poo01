print("Conversor de calificaciones")
nota = int(input("Ingresa tu calificación (0-100): "))

if 90 <= nota <= 100:
    print("Tu calificación es: A")
elif 80 <= nota <= 89:
    print("Tu calificación es: B")
elif 70 <= nota <= 79:
    print("Tu calificación es: C")
elif 60 <= nota <= 69:
    print("Tu calificación es: D")
elif 0 <= nota < 60:
    print("Tu calificación es: F")
else:
    print("Calificación fuera de rango.")
    
