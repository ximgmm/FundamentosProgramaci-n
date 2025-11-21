print("\nEjercicio 4 - Eliminar un par clave-valor\n")
# Escribe tus datos
cuenta = {
    "usuario": "pon tu usuario",
    "email": "agrega tu email",
    "teléfono": "escribe tu número",
    "ciudad": "pon tu cd"
}

print("Cuenta original (con teléfono):")
print(cuenta)
# Eliminar el número de teléfono por privacidad
del cuenta["teléfono"]

print("\nCuenta después de eliminar teléfono")
print(cuenta)
print("\nVerificación - ¿existe 'teléfono'?:", "teléfono" in cuenta)
