numeros = []
print("Ingresa números uno por uno. Escribe 'n' cuando hayas terminado.")
while True:
    entrada = input("ingresalo o 'n' para terminar: ")
    if entrada.lower() == 'n':
        break
    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("¡Error! Debes ingresar un número válido o 'n' para terminar.")
if numeros:
    promedio = sum(numeros) / len(numeros)
    print(f"\nNúmeros ingresados: {numeros}")
    print(f"Cantidad de números: {len(numeros)}")
    print(f"El promedio es: {promedio:.2f}")
else:
    print("\nNo se ingresaron números para calcular el promedio.")

    