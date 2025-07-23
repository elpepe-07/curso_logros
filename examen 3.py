"""Escribe un programa que pida al usuario que ingrese números uno por uno. Los números deben almacenarse en una lista. El usuario indicará que ha terminado de ingresar números
escribiendo la palabra n. En ese momento, el programa debe calcular y mostrar el promedio
de los números ingresados.
"""
lista = []
num_elementos = int(input("ingresa losnumeros 1 por 1 : "))

for i in range(num_elementos):
    elemento = input(f"Introduce el elemento {i+1}: ")
    lista.append(elemento)

print("La lista completa es:", lista)