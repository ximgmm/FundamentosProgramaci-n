print("\nEjercicio 4: Ver cada paso del ordenamiento\n")
numeros_ej4 = [25, 18, 34, 79, 83]
print("Inicio:", numeros_ej4)
print("-" * 30)
n = len(numeros_ej4)

for i in range(n):
    print(f"\nPasada {i + 1}:")
    for j in range(0, n - i - 1):
        print(f" Comparando {numeros_ej4[j]} y {numeros_ej4 [j + 1]}")
        if numeros_ej4[j] > numeros_ej4[j + 1]:
            # Intercambiar
            numeros_ej4[j], numeros_ej4[j + 1] = numeros_ej4[j + 1], numeros_ej4[j]
            print(f"Intercambio → {numeros_ej4}")
        else:
            print(f"No cambiar → {numeros_ej4}")

print("\n" + "-" * 30)
print("Final:\n", numeros_ej4)


