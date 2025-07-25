comidas = []
precios = []
total = 0

while True:
    comida = input("ingresa un tipo de comida (fruta/verdura) o 'q' para terminar: ").strip().lower()
    if comida == "q":
        break
    else:
        precio = float(input(f"ingresa el precio de la {comida}: "))
        comidas.append(comida)
        precios.append(precio)

# Option to remove items
while True:
    print("\nLista actual de comidas:")
    for idx, (comida, precio) in enumerate(zip(comidas, precios)):
        print(f"{idx+1}. {comida} - ${precio}")
    borrar = input("¿Quieres borrar algún elemento? Escribe el número o 'n' para continuar: ").strip().lower()
    if borrar == "n":
        break
    try:
        borrar_idx = int(borrar) - 1
        if 0 <= borrar_idx < len(comidas):
            comidas.pop(borrar_idx)
            precios.pop(borrar_idx)
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido o 'n'.")

print("--- Lista de Comidas Final ---")
for comida in comidas:
    print(comida, end=" ")

for precio in precios:
    total += precio
print(f"\nTu total es: {total}")