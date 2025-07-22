def contar_letras():
    palabra = input("ingresa la palabra : ").lower()
    vocales = 0
    consonantes = 0
    vocales_set = {'a', 'e', 'i', 'o', 'u'}
    for letra in palabra:
        if letra.isalpha():  # Verificar que es una letra
            if letra in vocales_set:
                vocales += 1
            else:
                consonantes += 1
    print(f"La palabra '{palabra}' tiene:")
    print(f"- Vocales: {vocales}")
    print(f"- Consonantes: {consonantes}")
contar_letras()
