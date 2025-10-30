# INICIO

usuario = input("Ingresa tu usuario:")
edad = int(input("Ingresa tu edad:"))
género = input("Ingresa tu género favorito:")

if edad < 13:
    print("Te recomendamos películas infantiles")
elif edad >= 13 and edad <= 17 and género == "acción":
    print("Te recomendamos: Spider-Man (PG-13)")
elif edad >= 13 and edad <= 17 and género == "comedia":
    print("Te recomendamos: Shrek (PG-13)")
elif edad >= 13 and edad <= 17 and género == "terror":
    print("Te recomendamos: Scary stones (PG-13)")
elif edad >= 18 and género == "acción":
    print("Te recomendamos: John Wick")
elif edad >= 18 and género == "comedia":
    print("Te comendamos: Superbad")
elif edad >= 18 and género == "terror":
    print("Te recomendamos: El conjuro")
else:
    print("Género Inválido")

# FIN
