print("\nEjercicio 5: Orden descendente (mayor a menor)\n")
numeros_ej5 = [51, 23, 85, 17, 19]
print("Original: \n", numeros_ej5)
n = len(numeros_ej5)

for i in range(n):
    for j in range(0, n - i - 1):
        # CAMBIO: < en lugar de >
        if numeros_ej5[j] < numeros_ej5[j+1]:
            numeros_ej5[j], numeros_ej5[j + 1] = numeros_ej5[j + 1], numeros_ej5[j]

print("Ordenado (mayor a menor:)\n", numeros_ej5)
