print("Ejercicio 4: Búsqueda en un diccionario")

try:
    telefonos = {
        "Yami": "555-12342",
        "Allison": "555-5678",
        "Saul": "555-9012"
    }

    nombre = input("¿De quién quieres el teléfono?")
    telefono = telefonos[nombre]
    print(f"El teléfono de {nombre} es: {telefono}")
except KeyError:
    print("ERROR: Ese nombre no está en la agenda")
    