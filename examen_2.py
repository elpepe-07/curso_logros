import random

def numero_random():
    numero_secreto= random.randint(1,100)
    intentos = 0
    adivinando = False
    print("adivina un numero de entre 1 y 100 ")
    
    while not adivinando:
        try:
            intento = int(input("ingresa tu intento: ")).strip()
            intentos += 1
            if intento < numero_secreto:
                print("El numero es mayor sigue")
            elif intento > numero_secreto:
                print("El numero es menor sigue ")
            else:
                adivinando = True
                print(f"ese es el numero en {intentos} intentos lo adivinaste :D")
        except ValueError:
            print("so que w")                
numero_random()
