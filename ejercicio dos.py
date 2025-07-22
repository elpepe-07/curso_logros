def contar():
    palabra = input("pon la palabra : ").lower()
    vocal = 0
    consonante = 0
    vocales = {"a","e","i","o","u"}
    for letra in palabra:
        if letra.isalpha():
            if letra in vocales:
                vocal +=1
            else:
                consonante +=1
    print(f"{palabra} tiene {vocal} vocales y tiene {consonante} consonantes")
contar()