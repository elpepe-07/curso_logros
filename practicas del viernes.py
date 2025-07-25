#datos = {
#    "nombre": "ana",
#    "edad": 20,
#    "carrera": "ingenieria"
#}
#print(datos["carrera"])

#cadena = input(" pon tu palabra : ")
#contador_letras = {}
#for letra in cadena:
#    if letra in contador_letras:
#        contador_letras[letra] += 1
#    else:
#        contador_letras[letra] = 1
#print(contador_letras)

#precios = {
#    "manzana": 0.5,
#    "banana": 0.3
#}
#precios["banana"] = 0.4
#print(precios)

capitales = {
    "Francia": "Paris",
    "Italia": "Roma",
    "España": "Madrid"
}
for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}")