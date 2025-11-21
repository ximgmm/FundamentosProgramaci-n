print("\nEjericicio 6 - Obtener las keys\n")
# Agrega vuestra canción fav
canción = {
    "título": "Deja vu",
    "artista": "Olivia Rodrigo",
    "album": "GUTS",
    "año": 2023,
    "género": "Pop rock",
    "duración_segundos": 300
}

print("Diccionario de canción:")
print(canción)
print("\nTodas las claves del diccionario:")
claves = canción.keys()
print(claves)

print("\nMostrando claves una por una:")
for clave in claves:
    print("-", clave)
