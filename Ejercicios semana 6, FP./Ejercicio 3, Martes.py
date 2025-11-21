print("\nEjercicio 3\n")
# Agrega tus datos
perfil = {
    "usuario": "Tu nombre",
    "seguidores": 500,
    "publicaciones": 25,
    "ciudad": "Tu ciudad"
}

print("Perfil original:")
print(perfil)
print("Seguidores antes:", perfil["seguidores"])

# Modificar valores (gana más seguidores)
perfil["seguidores"] = 1250
perfil["publicaciones"] = 45

print("\nPerfil actualizado:")
print(perfil)
print("Seguidores ahora:", perfil["seguidores"])
print("Publicaciones ahora:", perfil["publicaciones"])