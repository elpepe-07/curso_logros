start = print("estas perdido en el bosque y para guiarte solo tienes un fosforo y una linterna")
opcion_1 = input(" cual escojes : FOSFORO o LINTERNA : ").lower()
if opcion_1 == "fosforo":
    print("iluminas con tu fosforo y al hacerlo un oso nota tu presencia ")
    opcion_1_1= input(" que haces CORRES O TE ESCONDES : ").lower()
    if opcion_1_1 == "corres":
        print("corres y pierdes al oso y te salvas")
    elif opcion_1_1 == "esconderse":
        print("te escondes pero el oso te encuentra fin del juego")
    else:
        print("no hagas eso")
if opcion_1 == "linterna":
    print("\n al usarla ves la salida al bosque y al salir ves dos caminos ,uno te lleva a la ciudad y el otro a una cueva\n")
    opcion_1_2 = input("cual tomas el de la CUEVA o EL DE LA CIUDAD ? :").lower()
    if opcion_1_2 == "cueva":
        print("al ir a la cueva y ver dentro te encuentras con un oso , este te ataca y fin del juego. ")
    elif opcion_1_2 == "ciudad":
        print("al ir a la ciudad llegas a tu hogar y descansas , has ganado.")
    else :
        print("oye no hagas eso!! ")
start