# INICIO

usuario = input ("Ingresa tu usuario:")
calificación = int (input("Ingresa tu calificación:"))

if calificación >= 90:
    print("Excelente")
elif calificación >=70 and calificación <=89:
    print("Aprobado")
elif calificación <70:
    print("Reprobado")
else:
    print("Calificación inválida")

# FIN

