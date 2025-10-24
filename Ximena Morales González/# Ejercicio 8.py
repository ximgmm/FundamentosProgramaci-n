# Ejercicio 8. Operadores lógicos
print("Ejercicio 8. Operadores lógicos")
# Imaginemos que queremos entrar a un juego online
tengo_internet = True # SÍ tengo internet
tengo_cuenta = True # SÍ tengo cuenta

# AND (y): Las DOS condiciones deben ser vedaderas
puedo_jugar = tengo_internet and tengo_cuenta
print("¿Puedo jugar? (ambas True):", puedo_jugar)

# Probemos cuando falta algo
tengo_internet2 = True
tengo_cuenta2 = False
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿Puedo jugar? (una es False):", puedo_jugar2)

# OR (o): Al menos UNA condición debe ser verdadera
tengo_celular = True
tengo_tablet = False
tengo_dispositivo = tengo_celular or tengo_tablet
print("¿Tengo dispositivo? (al menosuna True):", tengo_dispositivo)

# NOT (no): Invierte el valor: True se vuelve False y viceversa
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)