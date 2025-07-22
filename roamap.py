edad = int(input("pon tu edad: "))
ticket = input("y tienes ticket? (si/no): ").lower()
if  ticket == "si" and edad >=18:
    print("puedes entrar")
elif ticket == "no" and edad <18:
    print ("no puedes entrar")
elif ticket == "no" and edad >=18:
    print ("debes compar un ticket")
elif ticket == "si" and edad <18:
    print ("no puedes pasar")
